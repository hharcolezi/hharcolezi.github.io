"""Regression tests for monthly publishing; no network required."""
import unittest
from bs4 import BeautifulSoup
import importlib.util
from pathlib import Path
spec = importlib.util.spec_from_file_location("website_build", Path(__file__).with_name("site.py"))
s = importlib.util.module_from_spec(spec)
spec.loader.exec_module(s)

class BuildTests(unittest.TestCase):
    def test_header_normalization(self):
        self.assertEqual(s.key("not-on-website"), "not_on_website")
        self.assertEqual(s.key("Étudiant"), "etudiant")

    def test_preserves_csv_spaces_quotes_and_newlines(self):
        raw = 'section,sort_order,text_before,link_label,link_url,text_after\nabout,1,"Hello, ",ETS,https://example.org/," after\nline"\n'
        row = s.parse_csv(raw, "homepage")[0]
        self.assertEqual(row["text_before"], "Hello, ")
        self.assertEqual(row["text_after"], " after\nline")

    def test_html_response_rejected(self):
        with self.assertRaises(s.InvalidData):
            s.parse_csv('<!DOCTYPE html><html>Log in</html>', 'news')

    def test_missing_and_duplicate_headers_rejected(self):
        for raw in ('name,value\none,two', 'date,description,description\n2026-01-01,x,y'):
            with self.assertRaises(s.InvalidData):
                s.parse_csv(raw, 'news')

    def test_formula_errors_rejected(self):
        with self.assertRaises(s.InvalidData):
            s.parse_csv('date,description\n2026-01-01,#REF!', 'news')

    def test_url_and_markup_security(self):
        for url in ('javascript:alert(1)', 'data:text/html,test', 'https://user:pass@example.org', '//example.org'):
            with self.assertRaises(s.InvalidData):
                s.safe_url(url)
        with self.assertRaises(s.InvalidData):
            s.rich('<script>alert(1)</script>')
        self.assertNotIn('onclick', s.rich('<b onclick="alert(1)">bold</b>'))
        self.assertNotIn('{{', s.h('{{ site.secret }}'))

    def test_exact_homepage_prose_and_headline_no_link(self):
        rows = []
        for section in ('about','research','background','position'):
            rows.append(dict(section=section, sort_order='1', text_before='Before ', link_label='ÉTS', link_url='https://www.etsmtl.ca/', text_after=' after.'))
        rows.extend([
            dict(section='keyword', sort_order='1', text_before='Differential Privacy'),
            dict(section='hero_summary', sort_order='1', text_before='Audit privacy-preserving machine learning systems.'),
            dict(section='focus', sort_order='1', text_before='Privacy auditing', text_after='Inference attacks and empirical audits.'),
        ])
        out = s.render_home(rows)
        self.assertEqual(BeautifulSoup(out['about'], 'html.parser').get_text(), 'Before ÉTS after.')
        self.assertIn('href="https://www.etsmtl.ca/"', out['about'])
        self.assertNotIn('<a', out['position'])
        self.assertIn('Privacy auditing', out['focus'])
        self.assertIn('Inference attacks', out['focus'])
        with self.assertRaises(s.InvalidData):
            s.render_home(rows + [rows[0]])

    def test_homepage_missing_section_rejected(self):
        with self.assertRaises(s.InvalidData):
            s.render_home([])

    def test_project_flags_no_money(self):
        rows = [dict(title='Grant A', in_website='TRUE', period='2025 -- 2099', amount='999999$'), dict(title='Hidden', in_website='FALSE'), dict(in_website='FALSE')]
        selected = s.visible_rows('projects', rows)
        self.assertEqual(len(selected), 1)
        markup = s.render_projects(selected)
        self.assertNotIn('999999', markup)
        self.assertNotIn('Hidden', markup)

    def test_phd_alumni_before_other_degrees(self):
        rows = [dict(name='Master Alumni',level='MEng',completed='TRUE',year='2025'), dict(name='PhD Alumni',level='PhD',completed='TRUE',year='2022'), dict(name='Bachelor Alumni',level='Bachelor',completed='TRUE',year='2026')]
        markup = s.render_students(rows)
        self.assertLess(markup.index('PhD Alumni'), markup.index('Master Alumni'))
        self.assertLess(markup.index('Master Alumni'), markup.index('Bachelor Alumni'))

    def test_software_allowlist_and_user_deletions(self):
        rows = [dict(name='Library', category='Libraries & Tools', in_website='TRUE'), dict(name='Data', category='Datasets', in_website='TRUE'), dict(name='Old code', category='Research Code', in_website='TRUE'), dict(name='Hidden', category='Datasets', in_website='FALSE')]
        self.assertEqual([r['name'] for r in s.visible_rows('software', rows)], ['Library', 'Data'])

    def test_publication_visibility_not_selected_filter(self):
        rows = [dict(title='Visible', selected='FALSE', not_on_website='FALSE'), dict(title='Hidden', not_on_website='TRUE')]
        self.assertEqual([r['title'] for r in s.visible_rows('publications', rows)], ['Visible'])


    def test_publication_icons_filter_metadata_and_award(self):
        rows = [
            dict(
                category='conference', year='2026', pub_date='2026-07-01',
                authors='A. Author, H. Arcolezi', title='Paper One',
                venue='PETS 2026', url_pub='https://example.org/paper',
                pdf='https://example.org/preprint.pdf', code='https://example.org/code',
                slides='https://example.org/slides.pdf', video='https://example.org/video',
                awards='Best Paper Award', not_on_website='FALSE'
            ),
            dict(
                category='journal', year='2025', pub_date='2025-01-01',
                authors='H. Arcolezi', title='Paper Two',
                venue='Journal X', not_on_website='FALSE'
            ),
        ]
        markup = s.render_publications(rows)
        soup = BeautifulSoup(markup, 'html.parser')
        cards = soup.select('.pub-card[data-year][data-type]')
        self.assertEqual(len(cards), 2)
        self.assertEqual(cards[0]['data-year'], '2026')
        self.assertEqual(cards[0]['data-type'], 'conference')
        self.assertIsNotNone(soup.select_one('.pub-resource--pdf .fa-file-pdf'))
        self.assertIsNotNone(soup.select_one('.pub-resource--code .fa-code'))
        self.assertIsNotNone(soup.select_one('.pub-resource--slides .fa-images'))
        self.assertIsNotNone(soup.select_one('.pub-resource--video .fa-video'))
        self.assertIsNotNone(soup.select_one('.pub-link-badge--award .fa-trophy'))
        self.assertIn('Best Paper Award', soup.select_one('.pub-link-badge--award').get_text())

    def test_featured_publications_are_sheet_selected(self):
        rows = [
            dict(title='Featured A', authors='A', venue='VLDB 2026', year='2026', pub_date='2026-08-01', featured_home='TRUE', pdf='https://example.org/a.pdf'),
            dict(title='Featured B', authors='B', venue='PETS 2026', year='2026', pub_date='2026-07-01', featured_home='TRUE'),
            dict(title='Not featured', authors='C', venue='X', year='2026', pub_date='2026-06-01', featured_home='FALSE'),
        ]
        markup = s.render_featured_publications(rows)
        soup = BeautifulSoup(markup, 'html.parser')
        self.assertEqual(len(soup.select('.featured-pub-card')), 2)
        self.assertIn('Featured A', markup)
        self.assertNotIn('Not featured', markup)
        self.assertIsNotNone(soup.select_one('.featured-pub-links .fa-file-pdf'))

    def test_news_collapses_after_five_without_javascript(self):
        rows = [dict(date=f'2026-{month:02d}-01', description=f'News {month}') for month in range(1, 8)]
        markup = s.render_news(rows)
        soup = BeautifulSoup(markup, 'html.parser')
        self.assertEqual(len(soup.select('.news-item')), 7)
        self.assertEqual(len(soup.select('details.news-more > .news-more__items .news-item')), 2)
        self.assertIn('Show all news', soup.select_one('details.news-more summary').get_text())

    def test_news_links_and_dates(self):
        rendered = s.render_news([dict(date='2026-09-01',description='News [link](https://example.org) and <https://example.com>.')])
        self.assertEqual(len(BeautifulSoup(rendered,'html.parser').select('a')), 2)
        with self.assertRaises(s.InvalidData):
            s.render_news([dict(date='2026-13-01', description='Bad date')])

    def test_source_replacement_leaves_style_and_removes_runtime(self):
        source = '---\npermalink: /\n---\n<style>.x{color:red}</style><p id="profile-about">Old</p><div id="state">Loading</div><script src="/assets/js/google-sheet-utils.js"></script><script>const S=window.HHASheets;</script>'
        updated = s.replace_sections(source, {'profile-about': 'Full text <a href="https://example.org">link</a>.'}, ['state'])
        self.assertIn('Full text', updated)
        self.assertIn('<style>', updated)
        self.assertNotIn('HHASheets', updated)
        self.assertNotIn('Loading', updated)
        self.assertTrue(updated.startswith('---\npermalink: /\n---'))
        with self.assertRaises(s.InvalidData):
            s.replace_sections(source, {'missing': 'text'}, [])

if __name__ == '__main__':
    unittest.main()
