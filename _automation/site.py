#!/usr/bin/env python3
"""Read the public Sheet at build time; render only approved website fields.

prepare changes the runner checkout only: no commits and no Sheet writes.
verify checks the complete Jekyll output before publication.
"""
from __future__ import annotations
import argparse
import csv
import hashlib
import html
import io
import json
import os
import re
import sys
import time
import unicodedata
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlsplit
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

SHEET_ID = "12bFYV-4WC1PhxKrnSVh5s3SPfe63fY3qd_qXybD43qw"
SPECS = {
    "homepage": ("1002262062", {"section", "sort_order", "text_before", "link_label", "link_url", "text_after"}),
    "news": ("1326369063", {"date", "description"}),
    "publications": ("1565301812", {"category", "year", "authors", "title", "not_on_website"}),
    "projects": ("1323298866", {"title", "period", "in_website"}),
    "students": ("1794000060", {"level", "name", "completed", "project_title"}),
    "teaching": ("1100989932", {"course", "year", "institution"}),
    "software": ("1684913614", {"category", "name", "in_website", "sort_order"}),
}
PAGES = {
    "news": ("_pages/about.md", "news-list", "news-state", ".news-item", "index.html"),
    "publications": ("_pages/publications.md", "pubs-list", "pubs-state", ".pub-card", "publications/index.html"),
    "projects": ("_pages/projects.md", "projects-list", "projects-state", ".sheet-card", "projects/index.html"),
    "students": ("_pages/students.md", "students-list", "students-state", ".sheet-card", "students/index.html"),
    "teaching": ("_pages/teaching.md", "teaching-list", "teaching-state", ".sheet-card", "teaching/index.html"),
    "software": ("_pages/software.md", "software-list", "software-state", ".sheet-card", "software/index.html"),
}
NAV_PATHS = ["/", "/publications/", "/projects/", "/students/", "/teaching/", "/software/", "/cv/"]
SOFTWARE_CATEGORIES = ["Libraries & Tools", "Datasets"]
FORMULA_ERRORS = {"#REF!", "#VALUE!", "#DIV/0!", "#N/A", "#NAME?", "#NUM!", "#ERROR!"}

class InvalidData(ValueError):
    pass


def key(value: str) -> str:
    value = unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode().lower().strip()
    return re.sub(r"[^a-z0-9]+", "_", value).strip("_")


def h(value: object) -> str:
    # Keep authored content out of both HTML and Liquid's template language.
    return html.escape(str(value), quote=True).replace("{", "&#123;").replace("}", "&#125;")


def get(row: dict, *fields: str) -> str:
    return next((str(row[f]).strip() for f in fields if str(row.get(f, "")).strip()), "")


def boolean(value: object) -> bool:
    v = str(value).strip().lower()
    if v in {"true", "1", "yes", "y", "x"}:
        return True
    if v in {"false", "0", "no", "n", ""}:
        return False
    raise InvalidData(f"Unrecognized boolean {value!r}; use TRUE or FALSE.")


def public(row: dict) -> bool:
    return not boolean(row.get("not_on_website", ""))


def safe_url(value: str) -> str:
    value = str(value).strip()
    parsed = urlsplit(value)
    if (parsed.scheme not in {"https", "http"} or not parsed.hostname
            or parsed.username or parsed.password or re.search(r"[\x00-\x20]", value)):
        raise InvalidData("A website link must be an absolute HTTP(S) URL without credentials.")
    return value


def link(label: str, url: str = "") -> str:
    if not str(url).strip():
        return h(label)
    return f'<a href="{h(safe_url(url))}" target="_blank" rel="noopener noreferrer">{h(label)}</a>'


def rich(value: str) -> str:
    """Keep basic authored formatting; reject executable markup."""
    soup = BeautifulSoup(value, "html.parser")
    allowed = {"b", "strong", "i", "em", "sub", "sup", "br", "span", "p", "ul", "ol", "li", "a"}
    for node in list(soup.find_all(True)):
        if node.name in {"script", "style", "iframe", "object", "svg", "form"}:
            raise InvalidData("Executable markup is not permitted in Sheet content.")
        if node.name not in allowed:
            node.unwrap()
            continue
        url = node.get("href", "") if node.name == "a" else ""
        node.attrs = {}
        if url:
            node.attrs = {"href": safe_url(url), "target": "_blank", "rel": "noopener noreferrer"}
    return str(soup).replace("{", "&#123;").replace("}", "&#125;")


def news_text(text: str) -> str:
    """Same link notation as the news sheet; preserve text and newlines."""
    pattern = re.compile(r"\[([^\]]+)\]\((https?://[^\s)]+)\)|<(https?://[^ <>]+)>")
    parts, end = [], 0
    for match in pattern.finditer(text):
        parts.append(h(text[end:match.start()]))
        parts.append(link(match[1] or match[3], match[2] or match[3]))
        end = match.end()
    parts.append(h(text[end:]))
    return "".join(parts).replace("\n", "<br>")


def parse_csv(text: str, name: str) -> list[dict[str, str]]:
    if text.lstrip().lower().startswith(("<!doctype", "<html")):
        raise InvalidData(f"{name}: Google returned an HTML/login page, not CSV.")
    lines = list(csv.reader(io.StringIO(text.lstrip("\ufeff")), strict=True))
    if not lines:
        raise InvalidData(f"{name}: empty response.")
    headers = [key(x) for x in lines[0]]
    nonempty = [x for x in headers if x]
    if len(nonempty) != len(set(nonempty)):
        raise InvalidData(f"{name}: duplicate column headings.")
    missing = SPECS[name][1] - set(headers)
    if missing:
        raise InvalidData(f"{name}: missing columns {sorted(missing)}.")
    rows = []
    for number, values in enumerate(lines[1:], 2):
        if len(values) > len(headers) and any(values[len(headers):]):
            raise InvalidData(f"{name}: row {number} has more values than headers.")
        # Whitespace in homepage text fragments is intentional.
        row = {header: values[i] if i < len(values) else "" for i, header in enumerate(headers) if header}
        if any(str(v).strip() in FORMULA_ERRORS for v in row.values()):
            raise InvalidData(f"{name}: row {number} contains a spreadsheet formula error.")
        if any(str(v).strip() for v in row.values()):
            rows.append(row)
    return rows


def download(name: str) -> str:
    gid = SPECS[name][0]
    url = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv&headers=1&gid={gid}"
    error = None
    for attempt in range(3):
        try:
            request = Request(url, headers={"User-Agent": "HHA-monthly-static-website/1.0", "Cache-Control": "no-cache"})
            with urlopen(request, timeout=30) as response:
                content = response.read(4_000_001)
                if len(content) > 4_000_000:
                    raise InvalidData(f"{name}: unexpected response size.")
                return content.decode("utf-8-sig", errors="strict")
        except (OSError, UnicodeError) as exc:
            error = exc
            if attempt < 2:
                time.sleep(2 ** attempt)
    raise InvalidData(f"Could not fetch {name} after three attempts: {error}")


def number(value: str, default: int = 0) -> int:
    return int(value) if str(value).strip().isdigit() else default


def chip(value: str) -> str:
    return f'<span class="sheet-chip">{h(value)}</span>' if value else ""


def paragraph(label: str, value: str, *, markup: bool = False, muted: bool = False) -> str:
    if not value:
        return ""
    css = ' class="sheet-meta"' if muted else ""
    prefix = f"<strong>{h(label)}:</strong> " if label else ""
    return f"<p{css}>{prefix}{value if markup else h(value)}</p>"


def card(title: str, contents: str, chips: str = "") -> str:
    return f'<article class="sheet-card"><div>{chips}</div><h3>{title}</h3>{contents}</article>'


def section(title: str, content: str) -> str:
    return f'<section class="sheet-section"><h2>{h(title)}</h2><div class="sheet-grid">{content}</div></section>' if content else ""


def render_home(rows: list[dict]) -> dict[str, str]:
    allowed = {"about", "research", "background", "keyword", "position"}
    groups = defaultdict(list)
    seen = set()
    for row in rows:
        label = get(row, "section").lower()
        if not label:
            continue
        if label not in allowed:
            raise InvalidData(f"homepage: unknown section {label!r}.")
        identity = (label, get(row, "sort_order"))
        if identity in seen:
            raise InvalidData(f"homepage: duplicate section/order {identity}.")
        seen.add(identity)
        groups[label].append(row)
    result = {}
    for label in allowed:
        if not groups[label]:
            raise InvalidData(f"homepage: required section {label!r} is empty.")
        ordered = sorted(groups[label], key=lambda r: number(get(r, "sort_order")))
        if label == "keyword":
            result[label] = "".join(f'<span>{h(r.get("text_before", ""))}</span>' for r in ordered)
        else:
            fragments = []
            for row in ordered:
                # The owner deliberately made the position headline non-clickable.
                url = "" if label == "position" else get(row, "link_url")
                fragments.append(h(row.get("text_before", "")) + link(row.get("link_label", ""), url) + h(row.get("text_after", "")))
            result[label] = "".join(fragments)
        if not BeautifulSoup(result[label], "html.parser").get_text().strip():
            raise InvalidData(f"homepage: section {label!r} has no text.")
    return result


def visible_rows(name: str, rows: list[dict]) -> list[dict]:
    rows = [r for r in rows if public(r)]
    if name == "news":
        return [r for r in rows if get(r, "description", "news", "content", "news_html")]
    if name == "publications":
        return [r for r in rows if get(r, "title")]
    if name == "projects":
        return [r for r in rows if get(r, "title") and boolean(r.get("in_website", ""))]
    if name == "students":
        return [r for r in rows if get(r, "name")]
    if name == "teaching":
        return [r for r in rows if get(r, "course", "description")]
    if name == "software":
        return [r for r in rows if get(r, "name") and get(r, "category") in SOFTWARE_CATEGORIES and boolean(r.get("in_website", ""))]
    return rows


def render_news(rows: list[dict]) -> str:
    out = []
    for row in sorted(rows, key=lambda r: get(r, "date"), reverse=True):
        date = get(row, "date")
        match = re.fullmatch(r"(\d{4})-(\d{2})(?:-\d{2})?", date)
        if not match or not 1 <= int(match[2]) <= 12:
            raise InvalidData("news: dates must use YYYY-MM-DD or YYYY-MM.")
        label = f"{['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'][int(match[2])-1]} {match[1]}"
        contents = rich(get(row, "news_html")) if get(row, "news_html") else news_text(get(row, "description", "news", "content"))
        out.append(f'<article class="news-item"><div class="news-date">{h(label)}</div><div class="news-content">{contents}</div></article>')
    return "".join(out)


def render_publications(rows: list[dict]) -> str:
    groups = defaultdict(list)

    resource_icons = {
        "venue": "fas fa-building",
        "pdf": "fas fa-file-pdf",
        "code": "fas fa-code",
        "dataset": "fas fa-database",
        "slides": "fas fa-images",
        "poster": "fas fa-image",
        "video": "fas fa-video",
        "bibtex": "fas fa-book",
        "award": "fas fa-trophy",
    }

    def resource(label: str, url: str, kind: str) -> str:
        if not url:
            return ""
        icon = resource_icons[kind]
        return (
            f'<a class="pub-resource pub-resource--{h(kind)}" href="{h(safe_url(url))}" '
            f'target="_blank" rel="noopener noreferrer">'
            f'<i class="{h(icon)}" aria-hidden="true"></i><span>{h(label)}</span></a>'
        )

    for row in sorted(rows, key=lambda r: get(r, "pub_date", "year"), reverse=True):
        category = get(row, "category")
        technical = any(s in category.lower() for s in ("thesis", "technical report"))
        group = "Technical Reports" if technical else get(row, "year")
        if not group:
            raise InvalidData("publications: a visible publication is missing its year.")

        kind = "technical-report" if technical else key(category).replace("_", "-") or "publication"
        year = get(row, "year") or ("technical-report" if technical else group)

        links = []
        award = get(row, "awards")
        if award:
            links.append(
                f'<span class="pub-link-badge pub-link-badge--award">'
                f'<i class="{resource_icons["award"]}" aria-hidden="true"></i><span>{h(award)}</span></span>'
            )

        venue = get(row, "venue")
        venue_url = get(row, "url_pub", "url")
        if venue:
            if venue_url:
                links.append(resource(venue, venue_url, "venue"))
            else:
                links.append(
                    f'<span class="pub-link-badge pub-resource--venue">'
                    f'<i class="{resource_icons["venue"]}" aria-hidden="true"></i><span>{h(venue)}</span></span>'
                )

        for field, label, resource_kind in (
            ("pdf", "PDF / preprint", "pdf"),
            ("code", "Code", "code"),
            ("dataset", "Dataset", "dataset"),
            ("slides", "Slides", "slides"),
            ("poster", "Poster", "poster"),
            ("video", "Video", "video"),
            ("bibtex", "BibTeX", "bibtex"),
        ):
            url = get(row, field)
            if url and not (field == "bibtex" and url.startswith("@")):
                links.append(resource(label, url, resource_kind))

        groups[group].append(
            f'<article class="pubs-card pub-card pub-card--{h(kind)}" '
            f'data-year="{h(year)}" data-type="{h(kind)}">'
            f'<div class="pub-card-top"><span class="pub-chip pub-chip--type pub-chip--{h(kind)}">{h(category)}</span></div>'
            f'<h3 class="pub-title">{rich(get(row, "title"))}</h3>'
            f'<div class="pub-authors">{rich(get(row, "authors"))}</div>'
            f'<div class="pub-links">{"".join(links)}</div></article>'
        )

    ordered = sorted((x for x in groups if x != "Technical Reports"), reverse=True)
    if "Technical Reports" in groups:
        ordered.append("Technical Reports")

    return "".join(
        f'<section class="pub-year-group"><h2 class="pub-year-heading">{h(year)}</h2>'
        f'<div class="pub-year-list">{"".join(groups[year])}</div></section>'
        for year in ordered
    )


def render_projects(rows: list[dict]) -> str:
    groups = {"Current Projects": [], "Past Projects": []}
    this_year = datetime.now(timezone.utc).year
    for row in sorted(rows, key=lambda r: get(r, "date"), reverse=True):
        years = re.findall(r"\d{4}", get(row, "period"))
        current = not years or int(years[-1]) >= this_year or "present" in get(row, "period").lower()
        title = link(get(row, "title"), get(row, "project_url"))
        body = paragraph("Program", get(row, "program"), muted=True) + paragraph("Role", get(row, "role")) + paragraph("Partners", get(row, "institutions")) + paragraph("Scope", get(row, "scope"))
        links = "".join(link(label, get(row, f)) for f, label in (("program_url", "Program"), ("project_url", "Project")) if get(row, f))
        body += f'<div class="sheet-links">{links}</div>' if links else ""
        groups["Current Projects" if current else "Past Projects"].append(card(title, body, chip(get(row, "period")) + chip(get(row, "organization"))))
    return "".join(section(title, "".join(cards)) for title, cards in groups.items())


def student_group(level: str) -> tuple[int, str]:
    v = level.lower().replace(".", "")
    if "phd" in v:
        return 0, "PhD Students"
    if "master" in v or "meng" in v or "msc" in v:
        return 1, "Master's Students"
    if "bachelor" in v or "beng" in v or "bsc" in v:
        return 2, "Bachelor Students"
    return 3, level or "Students"


def render_students(rows: list[dict]) -> str:
    groups = {False: defaultdict(list), True: defaultdict(list)}
    for row in sorted(rows, key=lambda r: (-number(get(r, "year")), get(r, "name"))):
        alumni = boolean(row.get("completed", ""))
        degree = student_group(get(row, "level"))
        project = get(row, "project_title")
        body = paragraph("", get(row, "organization"), muted=True)
        body += paragraph("Thesis" if alumni and degree[0] == 0 else "Topic", link(project, get(row, "project_url")) if project else "", markup=True)
        body += paragraph("Co-supervised with", get(row, "co_supervisor"))
        body += paragraph("Current Position", get(row, "position_after")) if alumni else ""
        body += paragraph("Prize", link(get(row, "award"), get(row, "award_url")) if get(row, "award") else "", markup=True)
        groups[alumni][degree].append(card(link(get(row, "name"), get(row, "profile_url")), body, chip(get(row, "level")) + chip(get(row, "period"))))
    output = []
    for alumni, title in ((False, "Current Students"), (True, "Alumni")):
        if groups[alumni]:
            content = "".join(f'<h3>{h(group[1])}</h3><div class="sheet-grid">{"".join(groups[alumni][group])}</div>' for group in sorted(groups[alumni]))
            output.append(f'<section class="sheet-section"><h2>{title}</h2>{content}</section>')
    return "".join(output)


def render_teaching(rows: list[dict]) -> str:
    groups = defaultdict(list)
    for row in rows:
        inst = link(get(row, "institution", "organization"), get(row, "institution_url"))
        program = h(get(row, "program"))
        body = paragraph("", program + (", " if program and inst else "") + inst, markup=True) + paragraph("", get(row, "topics"), muted=True)
        hours = get(row, "hours")
        groups[get(row, "year")].append(card(h(get(row, "course", "description")), body, chip(get(row, "period")) + chip(hours + "h" if hours and not hours.endswith("h") else hours) + chip(get(row, "role"))))
    return "".join(section(year, "".join(groups[year])) for year in sorted(groups, reverse=True))


def render_software(rows: list[dict]) -> str:
    groups = defaultdict(list)
    for row in sorted(rows, key=lambda r: number(get(r, "sort_order"), 999)):
        links = "".join(link(label, get(row, field)) for field, label in (("github", "GitHub"), ("pypi", "PyPI"), ("paper", "Paper"), ("arxiv", "arXiv"), ("data_url", "Data")) if get(row, field))
        groups[get(row, "category")].append(card(h(get(row, "name")), paragraph("", get(row, "description")) + f'<div class="sheet-links">{links}</div>'))
    return "".join(section(name, "".join(groups[name])) for name in SOFTWARE_CATEGORIES if groups[name])


RENDERERS = {"news": render_news, "publications": render_publications, "projects": render_projects, "students": render_students, "teaching": render_teaching, "software": render_software}


def replace_sections(source: str, updates: dict[str, str], states: list[str]) -> str:
    parts = source.split("---", 2)
    if len(parts) != 3 or parts[0].strip():
        raise InvalidData("A page is missing its Jekyll front matter.")
    soup = BeautifulSoup(parts[2], "html.parser")
    for script in soup.find_all("script"):
        if any(t in str(script) for t in ("google-sheet-utils", "HHASheets", "CSV_URL", SHEET_ID, "/gviz/tq")):
            script.decompose()
    for name in states:
        node = soup.find(id=name)
        if node:
            node.decompose()
    replacements = {}
    for name, content in updates.items():
        node = soup.find(id=name)
        if node is None:
            raise InvalidData(f"Required page element #{name} is missing; refusing to publish.")
        marker = f"HHA_BUILD_SLOT_{hashlib.sha256(name.encode()).hexdigest()}"
        if marker in source:
            raise InvalidData("Unexpected replacement marker.")
        node.clear()
        node.append(marker)
        replacements[marker] = content
    result = "---" + parts[1] + "---" + str(soup)
    for marker, content in replacements.items():
        result = result.replace(marker, content)
    return result


def prepare(root: Path, fixtures: Path | None = None) -> None:
    data = {name: parse_csv((fixtures / f"{name}.csv").read_text(encoding="utf-8") if fixtures else download(name), name) for name in SPECS}
    home = render_home(data["homepage"])
    report = {"schema": 1, "generated_at": datetime.now(timezone.utc).isoformat(), "source_commit": os.getenv("GITHUB_SHA", "local"), "counts": {}, "homepage": home, "labels": {}}
    pending = {}
    # Generate everything successfully before changing any source file.
    for name, (path, target, state, _, _) in PAGES.items():
        rows = visible_rows(name, data[name])
        if not rows:
            raise InvalidData(f"{name}: no visible records; refusing to replace a working page with an empty one.")
        report["counts"][name] = len(rows)
        label_key = {"news": "description", "students": "name", "software": "name", "teaching": "course"}.get(name, "title")
        report["labels"][name] = [get(r, label_key) for r in rows]
        updates = {target: RENDERERS[name](rows)}
        if name == "news":
            updates.update({f"profile-{k}": v for k, v in home.items() if k != "keyword"})
            updates["profile-keywords"] = home["keyword"]
        pending[root / path] = replace_sections((root / path).read_text(encoding="utf-8"), updates, [state])
    for path, content in pending.items():
        path.write_text(content, encoding="utf-8")
    report_path = root / "_automation-output" / "report.json"
    report_path.parent.mkdir(exist_ok=True)
    report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"counts": report["counts"], "homepage_sections": sorted(home)}, indent=2))


def text_normalized(markup: str) -> str:
    return " ".join(BeautifulSoup(markup, "html.parser").get_text().split())


def verify(site: Path, report_path: Path) -> None:
    report = json.loads(report_path.read_text(encoding="utf-8"))
    for name, (_, target, _, selector, filename) in PAGES.items():
        path = site / filename
        if not path.is_file():
            raise InvalidData(f"Jekyll did not produce {filename}.")
        soup = BeautifulSoup(path.read_text(encoding="utf-8"), "html.parser")
        root = soup.find(id=target)
        if root is None or len(root.select(selector)) != report["counts"][name]:
            raise InvalidData(f"{filename}: rendered record count does not match the live Sheet.")
        for label in report["labels"][name]:
            if name != "news" and text_normalized(label) not in text_normalized(str(root)):
                raise InvalidData(f"{filename}: a title/name disappeared during the build.")
        nav = [urlsplit(a.get("href", "")).path for a in soup.select("#site-nav .visible-links a")]
        if nav != NAV_PATHS:
            raise InvalidData(f"{filename}: navigation differs from the approved shared menu: {nav}.")
        for script in soup.find_all("script"):
            if any(t in str(script) for t in ("google-sheet-utils", "HHASheets", "CSV_URL", SHEET_ID, "/gviz/tq")):
                raise InvalidData(f"{filename}: browser-time Sheet code is still present.")
        for anchor in root.select("a[href]"):
            safe_url(anchor["href"])
    home = BeautifulSoup((site / "index.html").read_text(encoding="utf-8"), "html.parser")
    for name in ("about", "research", "background", "position"):
        node = home.find(id=f"profile-{name}")
        expected = BeautifulSoup(report["homepage"][name], "html.parser")
        if node is None or text_normalized(str(node)) != text_normalized(str(expected)):
            raise InvalidData(f"Homepage {name} wording differs from its Sheet text.")
        if [a.get("href") for a in node.select("a")] != [a.get("href") for a in expected.select("a")]:
            raise InvalidData(f"Homepage {name} hyperlinks differ from the Sheet.")
    if home.select_one("#profile-position a"):
        raise InvalidData("The non-clickable position headline was changed into a link.")
    for resource in ("files/HHA_CV.pdf", "images/HHA_profile.png", "assets/css/sheet-cards.css", "assets/js/main.min.js"):
        if not (site / resource).is_file():
            raise InvalidData(f"Missing existing site resource: {resource}.")
    cv_page = site / "cv/index.html"
    if not cv_page.is_file():
        raise InvalidData("Jekyll did not produce the CV redirect page.")
    cv_html = cv_page.read_text(encoding="utf-8")
    if "<!doctype html>" not in cv_html.lower():
        raise InvalidData("CV route is not a standalone HTML redirect page.")
    if "https://hharcolezi.github.io/files/HHA_CV.pdf" not in cv_html:
        raise InvalidData("CV route no longer points to the compiled PDF.")
    if "<main" in cv_html.lower() or 'class="archive"' in cv_html.lower():
        raise InvalidData("CV redirect was wrapped in the site layout instead of staying standalone.")
    if (site / "talks/index.html").exists() or (site / "academic/index.html").exists():
        raise InvalidData("A removed Talks/Academic route has reappeared.")
    if (site / "_automation").exists() or (site / "_automation-output").exists():
        raise InvalidData("Build internals were copied into the public site.")
    manifest = {k: report[k] for k in ("schema", "generated_at", "source_commit", "counts")}
    (site / "website-build.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print("Static-site validation passed: content, links, counts, navigation and assets.")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=["prepare", "verify"])
    parser.add_argument("--root", type=Path, default=Path("."))
    parser.add_argument("--site", type=Path, default=Path("_site"))
    parser.add_argument("--fixtures", type=Path)
    args = parser.parse_args()
    if args.command == "prepare":
        prepare(args.root.resolve(), args.fixtures)
    else:
        verify(args.site.resolve(), args.root / "_automation-output/report.json")


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(f"::error::{exc}", file=sys.stderr)
        sys.exit(1)
