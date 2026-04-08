---
permalink: /
author_profile: false
redirect_from: 
  - /about/
  - /about.html
---

<section class="profile-hero" aria-labelledby="home-title">
  <div class="profile-hero__content">
    <h1 id="home-title" class="profile-hero__title">Héber H. Arcolezi</h1>
    <p class="profile-hero__lead">Advancing Responsible and Trustworthy AI.</p>
    <p class="profile-hero__eyebrow">Assistant Professor · ETS Montreal</p>

    <div class="profile-hero__keywords" aria-label="Research keywords">
      <span>Differential Privacy</span>
      <span>Responsible AI</span>
      <span>Trustworthy AI</span>
    </div>

    <nav class="profile-hero__links" aria-label="Contact links">
      <a href="mailto:heber.hwang-arcolezi@etsmtl.ca" aria-label="Email">
        <i class="fas fa-envelope" aria-hidden="true"></i>
        <span>Email</span>
      </a>
      <a href="https://scholar.google.com/citations?hl=en&user=VJgSocwAAAAJ&view_op=list_works&sortby=pubdate" target="_blank" rel="noopener noreferrer" aria-label="Google Scholar">
        <i class="ai ai-google-scholar" aria-hidden="true"></i>
        <span>Google Scholar</span>
      </a>
      <a href="https://x.com/hharcolezi" target="_blank" rel="noopener noreferrer" aria-label="X profile">
        <svg viewBox="0 0 24 24" role="img" aria-hidden="true" focusable="false">
          <path d="M18.901 1.153h3.68l-8.04 9.19L24 22.847h-7.406l-5.8-7.584-6.637 7.584H.478l8.6-9.83L0 1.153h7.594l5.243 6.932zM17.61 20.645h2.04L6.486 3.24H4.298z"/>
        </svg>
        <span>X</span>
      </a>
      <a href="/files/HHA_CV.pdf" aria-label="Curriculum Vitae">
        <i class="fas fa-file-pdf" aria-hidden="true"></i>
        <span>CV</span>
      </a>
    </nav>
  </div>

  <aside class="profile-hero__aside" aria-label="Portrait and affiliation">
    <img class="profile-hero__image" src="/images/HHA_profile.png" alt="Portrait of Héber H. Arcolezi" />
    <p class="profile-hero__location">Montréal, Canada</p>
  </aside>
</section>

<section class="profile-columns" aria-label="About and research overview">
  <article>
    <h2>About</h2>
    <p>
      I am an Assistant Professor in the Department of Software and Information Technology Engineering at
      <a href="https://www.etsmtl.ca/" target="_blank" rel="noopener noreferrer">ÉTS Montréal</a>, where I co-lead the
      Trustworthy Information Systems Lab
      <a href="https://tisl-lab.github.io/" target="_blank" rel="noopener noreferrer">(TISL)</a> research group.
      Previously, I was a Tenured Research Scientist at
      <a href="https://www.inria.fr/en/inria-centre-university-grenoble-alpes" target="_blank" rel="noopener noreferrer">Inria Grenoble</a>.
    </p>
  </article>

  <article>
    <h2>Research Interests</h2>
    <p>
      My research addresses the technical challenges of Responsible AI through the lenses of fairness,
      privacy-preserving techniques, and explainability. My goal is to design systems that are both
      mathematically private and socially equitable.
    </p>
  </article>

  <article>
    <h2>Background</h2>
    <p>
      I received my Ph.D. in Computer Science from the University of Bourgogne Franche-Comté (UBFC) and my
      M.Sc. in Electrical Engineering from the São Paulo State University (UNESP).
    </p>
  </article>
</section>

<section aria-labelledby="recent-news-title">
  <h2 id="recent-news-title">Recent News</h2>
  <div class="news-app" id="news-app">
    <div id="news-state" class="news-state">Loading news…</div>
    <div id="news-list" class="news-list"></div>
  </div>
</section>

<section class="contact-card" aria-labelledby="contact-title">
  <h2 id="contact-title">Contact</h2>
  <p>I am always happy to discuss the possibility of new collaborations.</p>
  <ul class="contact-card__list">
    <li>
      <strong>Email:</strong>
      <a href="mailto:heber.hwang-arcolezi@etsmtl.ca">heber.hwang-arcolezi@etsmtl.ca</a>
    </li>
    <li>
      <strong>Postal Address:</strong>
      1100, rue Notre-Dame Ouest, Montréal (Qc) H3C 1K3, Canada.
    </li>
  </ul>
  <p class="contact-card__updated">Last update: {{ site.time | date: "%b %-d, %Y" }}.</p>
</section>

<style>
  :root {
    --profile-bg: #f7f8fb;
    --profile-text: #111318;
    --profile-muted: #50545f;
    --profile-line: #dfe4ee;
    --profile-accent: #1f4aa2;
  }

  body,
  .masthead {
    background: var(--profile-bg);
    color: var(--profile-text);
  }

  .masthead {
    border-bottom: 1px solid var(--profile-line);
  }

  .masthead .greedy-nav,
  .masthead .greedy-nav .visible-links,
  .masthead .greedy-nav .visible-links a {
    background: transparent;
  }

  .page {
    padding-inline: clamp(1.1rem, 3vw, 2.2rem);
  }

  #main {
    max-width: 1480px;
  }

  #main > .page {
    float: none;
    width: 100%;
    margin-inline: auto;
  }

  .page__content {
    max-width: 1280px;
  }

  .profile-hero {
    margin: clamp(1.8rem, 4vw, 3rem) 0 clamp(2rem, 5vw, 3.4rem);
    display: grid;
    grid-template-columns: minmax(0, 1.5fr) minmax(240px, 0.8fr);
    gap: clamp(1.2rem, 3.4vw, 2.8rem);
    align-items: center;
    padding: clamp(1rem, 2vw, 1.5rem);
    border: 1px solid var(--profile-line);
    background: #ffffff;
    border-radius: 18px;
  }

  .profile-hero__eyebrow {
    margin: 0.95rem 0 0;
    text-transform: uppercase;
    letter-spacing: 0.11em;
    font-size: 0.76rem;
    color: var(--profile-muted);
    font-weight: 600;
  }

  .profile-hero__title {
    margin: 0.35rem 0 0;
    font-size: clamp(1.8rem, 4.2vw, 3rem);
    letter-spacing: -0.02em;
    line-height: 1.05;
  }

  .profile-hero__lead {
    margin: 0.95rem 0 0;
    max-width: 38ch;
    font-size: clamp(1rem, 1.8vw, 1.25rem);
    color: #1f2634;
  }

  .profile-hero__keywords {
    margin-top: 1rem;
    display: flex;
    gap: 0.6rem;
    flex-wrap: wrap;
  }

  .profile-hero__keywords span {
    font-size: 0.8rem;
    border: 1px solid #c9d3e6;
    border-radius: 999px;
    padding: 0.3rem 0.7rem;
    color: #23406f;
    background: #f5f8ff;
  }

  .profile-hero__links {
    margin-top: 1.2rem;
    display: flex;
    flex-wrap: wrap;
    gap: 0.65rem;
  }

  .profile-hero__links a {
    display: inline-flex;
    align-items: center;
    gap: 0.45rem;
    padding: 0.42rem 0.7rem;
    border: 1px solid var(--profile-line);
    border-radius: 999px;
    color: #1a2233;
    text-decoration: none;
    font-size: 0.77rem;
    letter-spacing: 0.05em;
    text-transform: uppercase;
    transition: border-color 0.2s ease, background-color 0.2s ease;
  }

  .profile-hero__links a:hover {
    border-color: var(--profile-accent);
    background: #f2f6ff;
  }

  .profile-hero__links i,
  .profile-hero__links svg {
    width: 1rem;
    height: 1rem;
    font-size: 1rem;
    flex-shrink: 0;
  }

  .profile-hero__links svg {
    fill: currentColor;
  }

  .profile-hero__aside {
    text-align: center;
  }

  .profile-hero__image {
    width: min(100%, 320px);
    aspect-ratio: 1 / 1;
    object-fit: cover;
    border-radius: 14px;
    border: 1px solid var(--profile-line);
  }

  .profile-hero__location {
    margin: 0.65rem 0 0;
    font-size: 0.88rem;
    color: var(--profile-muted);
  }

  .profile-columns {
    display: grid;
    grid-template-columns: repeat(3, minmax(0, 1fr));
    gap: clamp(1rem, 2.5vw, 2rem);
    margin-bottom: 2rem;
  }

  .profile-columns article {
    background: #ffffff;
    border: 1px solid var(--profile-line);
    border-radius: 14px;
    padding: 1rem 1rem 1.1rem;
  }

  .profile-columns h2 {
    margin: 0;
    font-size: 0.92rem;
    letter-spacing: 0.08em;
    text-transform: uppercase;
  }

  .profile-columns p {
    margin: 0.7rem 0 0;
    color: #1d2130;
    line-height: 1.64;
    font-size: 0.97rem;
  }

  .profile-columns a {
    color: inherit;
    text-underline-offset: 0.2em;
  }

  @media (max-width: 980px) {
    .profile-hero {
      grid-template-columns: 1fr;
    }

    .profile-hero__aside {
      text-align: left;
    }

    .profile-columns {
      grid-template-columns: 1fr;
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

  .contact-card {
    margin: 1rem 0 2rem;
    border: 1px solid var(--profile-line);
    border-radius: 16px;
    background: #ffffff;
    padding: 1rem 1.1rem;
  }

  .contact-card h2 {
    margin: 0;
    font-size: 0.92rem;
    letter-spacing: 0.08em;
    text-transform: uppercase;
  }

  .contact-card p {
    margin: 0.75rem 0 0;
  }

  .contact-card__list {
    margin: 0.65rem 0 0;
    padding-left: 1.1rem;
    line-height: 1.6;
  }

  .contact-card__updated {
    margin-top: 0.85rem;
    color: var(--profile-muted);
    font-size: 0.9rem;
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
