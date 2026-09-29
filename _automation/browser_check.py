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
            def guard(route):
                url = route.request.url
                if 'docs.google.com/spreadsheets' in url or '/gviz/tq' in url:
                    sheet_requests.append(url)
                if urlsplit(url).hostname == '127.0.0.1':
                    route.continue_()
                else:
                    route.abort()
            context.route('**/*', guard)
            for path, (selector, name) in ROUTES.items():
                page = context.new_page()
                response = page.goto(base + path, wait_until='networkidle')
                assert response.status == 200, f'{path}: HTTP failure'
                assert page.locator(selector).count() == REPORT['counts'][name], f'{path}: record-count mismatch'
                assert page.locator('#site-nav a[href$="/talks/"], #site-nav a[href$="/academic/"]').count() == 0, f'{path}: removed navigation appeared'
                if path == '/':
                    assert page.locator('#profile-background a').count() == 3
                    assert page.locator('#profile-position a').count() == 0
                if js and path in ('/', '/teaching/', '/software/'):
                    filename = 'homepage' if path == '/' else path.strip('/')
                    page.screenshot(path=str(OUT / f'{filename}-desktop.png'), full_page=True)
                    page.set_viewport_size({'width':390, 'height':844})
                    page.wait_for_timeout(200)
                    page.screenshot(path=str(OUT / f'{filename}-mobile.png'), full_page=True)
                checks.append({'path': path, 'javascript': js, 'records': REPORT['counts'][name]})
                page.close()
            assert not sheet_requests, 'Finished site attempted a Google Sheets request.'
            context.close()
        browser.close()
finally:
    server.shutdown()
(OUT / 'browser-checks.json').write_text(json.dumps(checks, indent=2) + '\n', encoding='utf-8')
print(f'Passed {len(checks)} finished-page checks, including JavaScript-disabled content.')
