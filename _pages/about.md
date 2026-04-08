---
permalink: /
title: "About Me"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

<section class="about-hero">
  <div class="about-hero__main">
    <p class="about-hero__eyebrow">Assistant Professor · ÉTS Montréal</p>
    <h1 class="about-hero__title">Heber Hwang Arcolezi</h1>
    <p class="about-hero__lead">Designing trustworthy information systems for Responsible AI.</p>

    <div class="about-hero__chips" aria-label="Topics">
      <span>Fairness</span>
      <span>Privacy-Preserving Techniques</span>
      <span>Explainability</span>
      <span>Responsible AI</span>
    </div>

    <div class="about-hero__links">
      <a href="mailto:heber.hwang-arcolezi@etsmtl.ca">Email</a>
      <a href="/files/HHA_CV.pdf">CV</a>
      <a href="https://scholar.google.com/citations?user=lt28fGUAAAAJ&hl=en" target="_blank" rel="noopener noreferrer">Scholar</a>
      <a href="https://github.com/hharcolezi" target="_blank" rel="noopener noreferrer">GitHub</a>
    </div>

    <ul class="about-hero__details" aria-label="Contact and profile details">
      <li>📍 Montréal, Canada</li>
      <li><a href="mailto:heber.hwang-arcolezi@etsmtl.ca">✉️ heber.hwang-arcolezi@etsmtl.ca</a></li>
      <li><a href="https://scholar.google.com/citations?user=lt28fGUAAAAJ&hl=en" target="_blank" rel="noopener noreferrer">🎓 Google Scholar</a></li>
      <li><a href="https://github.com/hharcolezi" target="_blank" rel="noopener noreferrer">💻 GitHub</a></li>
      <li><a href="https://x.com/hharcolezi" target="_blank" rel="noopener noreferrer">🐦 Twitter/X</a></li>
    </ul>
  </div>

  <aside class="about-hero__card">
    <h2>About me</h2>
    <p>
      I am an Assistant Professor in the Department of Software and Information Technology Engineering at
      <a href="https://www.etsmtl.ca/" target="_blank" rel="noopener noreferrer">ÉTS Montréal</a>, where I co-lead the
      <a href="https://tisl-lab.github.io/" target="_blank" rel="noopener noreferrer">Trustworthy Information Systems Lab (TISL)</a>
      research group. Previously, I was a Tenured Research Scientist at
      <a href="https://www.inria.fr/en/inria-centre-university-grenoble-alpes" target="_blank" rel="noopener noreferrer">Inria Grenoble</a>.
      I received my Ph.D. in Computer Science from the University of Bourgogne Franche-Comté (UBFC) and my M.Sc.
      in Electrical Engineering from the São Paulo State University (UNESP).
    </p>
  </aside>
</section>

<section class="about-focus">
  <h2>Research interests</h2>
  <p>
    My research addresses the technical challenges of Responsible AI through the lenses of fairness,
    privacy-preserving techniques, and explainability. My goal is to design systems that are both
    mathematically private and socially equitable.
  </p>
</section>

<style>
  .about-hero {
    display: grid;
    grid-template-columns: minmax(0, 1.45fr) minmax(260px, 1fr);
    gap: 1.5rem;
    align-items: stretch;
    margin: 0.6rem 0 1.5rem;
  }

  .about-hero__main,
  .about-hero__card,
  .about-focus {
    border: 1px solid #e5e7eb;
    border-radius: 18px;
    background: linear-gradient(180deg, #ffffff 0%, #f9fafb 100%);
    box-shadow: 0 14px 30px rgba(17, 24, 39, 0.06);
  }

  .about-hero__main {
    padding: 1.5rem;
  }

  .about-hero__eyebrow {
    margin: 0;
    color: #2563eb;
    font-weight: 700;
    letter-spacing: 0.04em;
    text-transform: uppercase;
    font-size: 0.78rem;
  }

  .about-hero__title {
    margin: 0.35rem 0 0.45rem;
    font-size: clamp(2rem, 6vw, 3.25rem);
    line-height: 1;
    letter-spacing: -0.03em;
  }

  .about-hero__lead {
    margin: 0;
    font-size: 1.15rem;
    color: #374151;
    max-width: 36ch;
  }

  .about-hero__chips {
    display: flex;
    flex-wrap: wrap;
    gap: 0.55rem;
    margin: 1.05rem 0 1.2rem;
  }

  .about-hero__chips span {
    border-radius: 999px;
    padding: 0.28rem 0.72rem;
    border: 1px solid #dbeafe;
    background: #eff6ff;
    color: #1e40af;
    font-size: 0.83rem;
    font-weight: 600;
  }

  .about-hero__links {
    display: flex;
    flex-wrap: wrap;
    gap: 0.75rem;
  }

  .about-hero__links a {
    display: inline-block;
    border-bottom: 2px solid #f59e0b;
    color: #7c2d12;
    font-weight: 700;
    letter-spacing: 0.03em;
    text-transform: uppercase;
    font-size: 0.78rem;
    text-decoration: none;
    padding-bottom: 0.1rem;
  }

  .about-hero__card {
    padding: 1rem;
  }

  .about-hero__details {
    list-style: none;
    margin: 1.1rem 0 0;
    padding: 0;
    display: grid;
    gap: 0.4rem;
    font-size: 0.93rem;
  }

  .about-hero__details li {
    color: #1f2937;
  }

  .about-hero__details a {
    color: #1f2937;
    text-decoration: none;
    border-bottom: 1px dashed #93c5fd;
  }

  .about-hero__details a:hover {
    color: #1d4ed8;
    border-bottom-color: #1d4ed8;
  }

  .about-hero__card h2,
  .about-focus h2 {
    margin: 0 0 0.4rem;
    font-size: 1.2rem;
  }

  .about-hero__card p,
  .about-focus p {
    margin: 0;
    color: #374151;
    line-height: 1.6;
  }

  .about-focus {
    padding: 1.25rem 1.4rem;
    margin-bottom: 1.2rem;
  }

  @media (max-width: 900px) {
    .about-hero {
      grid-template-columns: 1fr;
    }

    .about-hero__main,
    .about-hero__card {
      padding: 1.15rem;
    }
  }

  @media (max-width: 640px) {
    .about-hero__title {
      font-size: clamp(1.85rem, 11vw, 2.5rem);
    }

    .about-hero__lead {
      font-size: 1.03rem;
    }
  }

  .news-app {
    margin-top: 0.75rem;
  }

  .news-state {
    margin: 0.35rem 0 0;
    color: #6b7280;
    font-style: italic;
  }

  .news-list {
    display: grid;
    gap: 0.8rem;
    margin-top: 0.35rem;
  }

  .news-item {
    display: grid;
    grid-template-columns: 7.2rem 1fr;
    gap: 0.8rem;
    align-items: start;
    background: linear-gradient(180deg, #ffffff 0%, #fafcff 100%);
    border: 1px solid #e5e7eb;
    border-radius: 12px;
    padding: 0.75rem 0.85rem;
    box-shadow: 0 6px 16px rgba(17, 24, 39, 0.05);
  }

  .news-date {
    display: inline-flex;
    justify-content: center;
    align-items: center;
    text-align: center;
    border-radius: 999px;
    border: 1px solid #bfdbfe;
    background: #eff6ff;
    color: #1d4ed8;
    font-weight: 600;
    font-size: 0.82rem;
    padding: 0.2rem 0.55rem;
    white-space: nowrap;
  }

  .news-content {
    color: #374151;
    line-height: 1.55;
  }

  .news-content p {
    margin: 0;
  }

  .news-content a {
    text-underline-offset: 2px;
  }

  @media (max-width: 640px) {
    .news-item {
      grid-template-columns: 1fr;
      gap: 0.45rem;
    }

    .news-date {
      justify-self: start;
    }
  }
</style>

## Recent News

<div class="news-app" id="news-app">
  <div id="news-state" class="news-state">Loading news…</div>
  <div id="news-list" class="news-list"></div>
</div>


<script>
(() => {
  const SHEET_ID = '12bFYV-4WC1PhxKrnSVh5s3SPfe63fY3qd_qXybD43qw';
  const SHEET_GID = '1326369063';
  const CSV_URL = `https://docs.google.com/spreadsheets/d/${SHEET_ID}/gviz/tq?tqx=out:csv&gid=${SHEET_GID}`;

  const stateNode = document.getElementById('news-state');
  const listNode = document.getElementById('news-list');

  if (!stateNode || !listNode) return;

  const monthNames = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];

  const setState = (text) => {
    stateNode.textContent = text;
    stateNode.style.display = text ? 'block' : 'none';
  };

  const parseCSV = (text) => {
    const rows = [];
    let row = [];
    let field = '';
    let inQuotes = false;

    for (let i = 0; i < text.length; i += 1) {
      const c = text[i];
      const next = text[i + 1];

      if (c === '"') {
        if (inQuotes && next === '"') {
          field += '"';
          i += 1;
        } else {
          inQuotes = !inQuotes;
        }
      } else if (c === ',' && !inQuotes) {
        row.push(field);
        field = '';
      } else if ((c === '\n' || c === '\r') && !inQuotes) {
        if (c === '\r' && next === '\n') i += 1;
        row.push(field);
        if (row.some((value) => value.trim() !== '')) rows.push(row);
        row = [];
        field = '';
      } else {
        field += c;
      }
    }

    if (field.length || row.length) {
      row.push(field);
      rows.push(row);
    }

    return rows;
  };

  const normalizeKey = (value) => (value || '')
    .toLowerCase()
    .trim()
    .replace(/[^a-z0-9]+/g, '_')
    .replace(/^_+|_+$/g, '');

  const findKey = (source, candidates) => {
    const keys = Object.keys(source);
    for (const candidate of candidates) {
      const normalized = normalizeKey(candidate);
      const exact = keys.find((key) => key === normalized);
      if (exact) return exact;
      const partial = keys.find((key) => key.includes(normalized) || normalized.includes(key));
      if (partial) return partial;
    }
    return '';
  };

  const parseDate = (value) => {
    const raw = String(value || '').trim();
    if (!raw) return null;

    const isoMatch = raw.match(/^(\d{4})[-/](\d{1,2})(?:[-/](\d{1,2}))?/);
    if (isoMatch) {
      const year = Number(isoMatch[1]);
      const month = Number(isoMatch[2]);
      if (month >= 1 && month <= 12) return { year, month };
    }

    const native = new Date(raw);
    if (!Number.isNaN(native.getTime())) {
      return { year: native.getUTCFullYear(), month: native.getUTCMonth() + 1 };
    }

    const compact = raw.match(/^(\w{3,9})[-\s](\d{2,4})$/i);
    if (compact) {
      const monthToken = compact[1].slice(0, 3).toLowerCase();
      const month = monthNames.findIndex((m) => m.toLowerCase() === monthToken) + 1;
      const yearNum = Number(compact[2].length === 2 ? `20${compact[2]}` : compact[2]);
      if (month > 0 && yearNum) return { year: yearNum, month };
    }

    return null;
  };

  const formatMonthYear = (dateObj) => {
    if (!dateObj) return 'Date unavailable';
    return `${monthNames[dateObj.month - 1]} ${dateObj.year}`;
  };

  const escapeHTML = (value) => String(value || '')
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#39;');

  const safeUrl = (value) => {
    const trimmed = String(value || '').trim();
    if (!trimmed) return '';

    try {
      const parsed = new URL(trimmed);
      if (parsed.protocol === 'http:' || parsed.protocol === 'https:') {
        return parsed.toString();
      }
    } catch (_error) {
      return '';
    }

    return '';
  };

  const toRichText = (content, isHtml) => {
    if (!content) return '';
    if (isHtml) return content;

    let result = escapeHTML(content);

    result = result.replace(/\[([^\]]+)\]\((https?:\/\/[^\s)]+)\)/g, (_match, label, url) => {
      const safe = safeUrl(url);
      if (!safe) return `${label} (${url})`;
      return `<a href="${escapeHTML(safe)}" target="_blank" rel="noopener noreferrer">${label}</a>`;
    });

    result = result.replace(/&lt;(https?:\/\/[^\s<]+)&gt;/g, (_match, url) => {
      const safe = safeUrl(url);
      if (!safe) return escapeHTML(url);
      return `<a href="${escapeHTML(safe)}" target="_blank" rel="noopener noreferrer">${escapeHTML(safe)}</a>`;
    });

    result = result.replace(/\n/g, '<br>');

    return result;
  };

  const renderNews = (items) => {
    listNode.innerHTML = items.map((item) => `
      <article class="news-item">
        <div class="news-date">${item.dateLabel}</div>
        <div class="news-content">${item.content}</div>
      </article>
    `).join('');
  };

  const run = async () => {
    try {
      const response = await fetch(CSV_URL);
      if (!response.ok) throw new Error(`Could not load spreadsheet (${response.status})`);

      const rows = parseCSV(await response.text());
      if (!rows.length) {
        setState('No news found in the spreadsheet.');
        return;
      }

      const headers = rows[0].map(normalizeKey);
      const entries = rows.slice(1).map((columns) => {
        const item = {};
        headers.forEach((header, index) => {
          item[header] = String(columns[index] || '').trim();
        });

        const dateKey = findKey(item, ['date', 'news_date', 'month', 'year_month']);
        const textKey = findKey(item, ['news', 'content', 'description', 'text', 'item']);
        const htmlKey = findKey(item, ['news_html', 'html', 'content_html']);

        const parsedDate = parseDate(item[dateKey]);
        const rawHtml = item[htmlKey] || '';
        const rawText = item[textKey] || '';
        const content = toRichText(rawHtml || rawText, Boolean(rawHtml));

        return {
          content,
          parsedDate,
          dateLabel: formatMonthYear(parsedDate),
          sortKey: parsedDate ? `${parsedDate.year}${String(parsedDate.month).padStart(2, '0')}` : '000000',
        };
      }).filter((entry) => entry.content);

      entries.sort((a, b) => b.sortKey.localeCompare(a.sortKey));

      if (!entries.length) {
        setState('No visible news entries were found in the spreadsheet.');
        return;
      }

      setState('');
      renderNews(entries);
    } catch (error) {
      setState(`Unable to load recent news from Google Sheets. ${error.message}`);
    }
  };

  run();
})();
</script>

## Contact

I am always happy to discuss the possibility of new collaborations.

* Email: heber.hwang-arcolezi@etsmtl.ca
* Postal Address: 1100, rue Notre-Dame Ouest, Montréal (Qc) H3C 1K3, Canada.

Last update: {{ site.time | date: "%b %-d, %Y" }}.
