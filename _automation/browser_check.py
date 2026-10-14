#!/usr/bin/env python3
"""Smoke-test the finished website, not the source templates."""
import functools
import http.server
import json
import threading
from pathlib import Path
from urllib.parse import urlsplit
from playwright.sync_api import sync_playwright

ROOT = Path('_site').resolve()
OUT = Path('_automation-output')
REPORT = json.loads((OUT / 'report.json').read_text(encoding='utf-8'))
ROUTES = {'/': ('#news-list .news-item', 'news'), '/publications/': ('#pubs-list .pub-card','publications'), '/projects/': ('#projects-list .sheet-card','projects'), '/students/': ('#students-list .sheet-card','students'), '/teaching/': ('#teaching-list .sheet-card','teaching'), '/software/': ('#software-list .sheet-card','software')}

class QuietHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *args):
        pass

handler = functools.partial(QuietHandler, directory=str(ROOT))
server = http.server.ThreadingHTTPServer(('127.0.0.1', 0), handler)
threading.Thread(target=server.serve_forever, daemon=True).start()
base = f'http://127.0.0.1:{server.server_port}'
checks = []
try:
    with sync_playwright() as p:
        browser = p.chromium.launch()
        # Every public record must be present even with JavaScript disabled.
        for js in (False, True):
            context = browser.new_context(java_script_enabled=js, viewport={'width': 1440, 'height': 1050})
            sheet_requests = []
            asset_failures = []
            def guard(route):
                url = route.request.url
                parsed = urlsplit(url)
                if 'docs.google.com/spreadsheets' in url or '/gviz/tq' in url:
                    sheet_requests.append(url)
                if parsed.hostname == '127.0.0.1':
                    route.continue_()
                elif parsed.hostname == 'hharcolezi.github.io':
                    # Jekyll emits absolute asset URLs using site.url. Serve them
                    # from this candidate build, never from the previous live site.
                    local = base + parsed.path + ('?' + parsed.query if parsed.query else '')
                    response = route.fetch(url=local)
                    if response.status >= 400:
                        asset_failures.append({'url': url, 'status': response.status})
                    headers = dict(response.headers)
                    headers['access-control-allow-origin'] = '*'
                    route.fulfill(response=response, headers=headers)
                else:
                    route.abort()
            context.route('**/*', guard)
            for path, (selector, name) in ROUTES.items():
                page = context.new_page()
                response = page.goto(base + path, wait_until='networkidle')
                assert response.status == 200, f'{path}: HTTP failure'
                assert page.locator(selector).count() == REPORT['counts'][name], f'{path}: record-count mismatch'
                assert page.locator('#site-nav a[href$="/talks/"], #site-nav a[href$="/academic/"]').count() == 0, f'{path}: removed navigation appeared'
                assert page.evaluate("!!Array.from(document.styleSheets).find(s => s.href && s.href.includes('/assets/css/main.css'))"), f'{path}: main theme stylesheet did not load'
                assert page.evaluate("!!Array.from(document.styleSheets).find(s => s.href && s.href.includes('/assets/css/theme-toggle.css'))"), f'{path}: appearance stylesheet did not load'
                if js:
                    assert page.locator('#theme-toggle:visible').count() == 1, f'{path}: theme toggle is missing'
                else:
                    assert page.locator('#theme-toggle:visible').count() == 0, f'{path}: theme toggle should be hidden without JavaScript'
                canonical = page.locator('link[rel="canonical"]').get_attribute('href')
                expected_canonical = 'https://hharcolezi.github.io' + path
                assert canonical == expected_canonical, f'{path}: canonical mismatch: {canonical!r} != {expected_canonical!r}'
                robots = page.locator('meta[name="robots"]')
                if robots.count():
                    assert 'noindex' not in (robots.get_attribute('content') or '').lower(), f'{path}: unexpectedly marked noindex'
                if path == '/':
                    assert page.locator('#profile-background a').count() == 3
                    assert page.locator('#profile-position a').count() == 0
                    assert page.locator('#profile-keywords span').count() > 0, 'Homepage keywords are missing'
                    assert page.locator('.profile-hero, .featured-publications, .home-panel').count() == 0, 'Old dashboard homepage components reappeared'
                    assert page.locator('.soft-home-hero').count() == 1
                    assert page.locator('#profile-hero-lead').count() == 0, 'Removed hero tagline reappeared'
                    if REPORT['counts']['news'] > 5:
                        assert page.locator('details.news-more').count() == 1, 'Expandable news control is missing'
                        assert page.locator('details.news-more .news-more__items .news-item').count() == REPORT['counts']['news'] - 5
                if path == '/publications/':
                    assert page.locator('#pub-search').count() == 1
                    assert page.locator('#pub-year-index').count() == 1
                    assert page.locator('.pub-year-count').count() > 0
                    assert page.locator('.pub-bibtex').count() > 0, 'BibTeX controls are missing'
                    if js:
                        total = REPORT['counts']['publications']
                        assert page.locator('#pub-count').inner_text().strip() == f'{total} publications'
                        page.locator('#pub-search').fill('Differential Privacy')
                        visible_count = page.locator('.pub-card:visible').count()
                        assert 0 < visible_count < total, 'Publication search did not filter'
                        page.locator('#pub-search').fill('')
                        assert page.locator('.pub-card:visible').count() == total, 'Clearing search did not restore publications'
                if js and path in ('/', '/publications/', '/projects/', '/students/', '/teaching/', '/software/'):
                    filename = 'homepage' if path == '/' else path.strip('/')
                    page.screenshot(path=str(OUT / f'{filename}-desktop.png'), full_page=True)
                    page.set_viewport_size({'width':390, 'height':844})
                    page.wait_for_timeout(200)
                    page.screenshot(path=str(OUT / f'{filename}-mobile.png'), full_page=True)
                checks.append({'path': path, 'javascript': js, 'records': REPORT['counts'][name]})
                page.close()
            assert not sheet_requests, 'Finished site attempted a Google Sheets request.'
            assert not asset_failures, f'Same-site assets failed: {asset_failures}'
            context.close()

        # Appearance regression: OS preference, manual toggle, and persistence
        # across navigation must all work without changing the greedy-nav menu.
        context = browser.new_context(
            java_script_enabled=True,
            viewport={'width': 1440, 'height': 1050},
            color_scheme='dark',
        )
        theme_asset_failures = []
        theme_sheet_requests = []

        def theme_guard(route):
            url = route.request.url
            parsed = urlsplit(url)
            if 'docs.google.com/spreadsheets' in url or '/gviz/tq' in url:
                theme_sheet_requests.append(url)
            if parsed.hostname == '127.0.0.1':
                route.continue_()
            elif parsed.hostname == 'hharcolezi.github.io':
                local = base + parsed.path + ('?' + parsed.query if parsed.query else '')
                response = route.fetch(url=local)
                if response.status >= 400:
                    theme_asset_failures.append({'url': url, 'status': response.status})
                headers = dict(response.headers)
                headers['access-control-allow-origin'] = '*'
                route.fulfill(response=response, headers=headers)
            else:
                route.abort()

        context.route('**/*', theme_guard)
        page = context.new_page()

        response = page.goto(base + '/', wait_until='networkidle')
        assert response.status == 200
        assert page.locator('html').get_attribute('data-theme') == 'dark', 'OS dark preference was not honored'
        assert page.locator('#theme-toggle:visible').count() == 1
        assert page.locator('#theme-toggle').get_attribute('aria-pressed') == 'true'
        dark_body = page.evaluate("getComputedStyle(document.body).backgroundColor")
        dark_panel = page.evaluate("getComputedStyle(document.querySelector('.soft-home-section')).color")

        page.screenshot(path=str(OUT / 'homepage-dark-desktop.png'), full_page=True)

        page.locator('#theme-toggle').click()
        assert page.locator('html').get_attribute('data-theme') == 'light'
        assert page.locator('#theme-toggle').get_attribute('aria-pressed') == 'false'
        assert page.evaluate("localStorage.getItem('hha-theme')") == 'light'
        light_body = page.evaluate("getComputedStyle(document.body).backgroundColor")
        light_panel = page.evaluate("getComputedStyle(document.querySelector('.soft-home-section')).color")
        assert dark_body != light_body, 'Body appearance did not visibly change'
        assert dark_panel != light_panel, 'Homepage text appearance did not visibly change'

        response = page.goto(base + '/publications/', wait_until='networkidle')
        assert response.status == 200
        assert page.locator('html').get_attribute('data-theme') == 'light', 'Saved light theme did not persist'
        assert page.locator('#site-nav .visible-links a').count() > 0
        page.locator('#theme-toggle').click()
        assert page.locator('html').get_attribute('data-theme') == 'dark'
        assert page.evaluate("localStorage.getItem('hha-theme')") == 'dark'
        pub_input_bg = page.evaluate("getComputedStyle(document.querySelector('#pub-search')).backgroundColor")
        pub_title_color = page.evaluate("getComputedStyle(document.querySelector('.pub-title')).color")
        assert pub_input_bg != 'rgb(255, 255, 255)', 'Publication search stayed light in dark mode'
        assert pub_title_color != 'rgb(31, 41, 55)', 'Publication titles did not adapt to dark mode'
        page.screenshot(path=str(OUT / 'publications-dark-desktop.png'), full_page=True)

        response = page.goto(base + '/projects/', wait_until='networkidle')
        assert response.status == 200
        assert page.locator('html').get_attribute('data-theme') == 'dark', 'Saved dark theme did not persist'
        assert page.locator('.sheet-card').count() == REPORT['counts']['projects']
        sheet_card_bg = page.evaluate("getComputedStyle(document.querySelector('.sheet-card')).backgroundColor")
        assert sheet_card_bg != 'rgb(255, 255, 255)', 'Sheet-backed cards stayed light in dark mode'

        page.set_viewport_size({'width':390, 'height':844})
        page.goto(base + '/', wait_until='networkidle')
        assert page.locator('#theme-toggle:visible').count() == 1, 'Theme toggle disappeared on mobile'
        assert page.locator('html').get_attribute('data-theme') == 'dark'
        page.screenshot(path=str(OUT / 'homepage-dark-mobile.png'), full_page=True)

        assert not theme_sheet_requests, 'Dark-mode checks attempted a Google Sheets request.'
        assert not theme_asset_failures, f'Dark-mode same-site assets failed: {theme_asset_failures}'
        context.close()

        browser.close()
finally:
    server.shutdown()
(OUT / 'browser-checks.json').write_text(json.dumps(checks, indent=2) + '\n', encoding='utf-8')
print(f'Passed {len(checks)} finished-page checks, including JavaScript-disabled content and local theme assets.')
