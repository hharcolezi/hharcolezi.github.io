---
permalink: /
title: "About Me"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

👋 **Welcome!**   
I'm a Tenure-Track Assistant Professor in the Software and Information Technology Engineering Department at [ÉTS Montréal](https://www.etsmtl.ca/).    
Previously, I was a Tenured Research Scientist at [Inria Grenoble](https://www.inria.fr/en/inria-centre-university-grenoble-alpes) working with the [Privatics](https://team.inria.fr/privatics/) team, and a Postdoctoral Researcher in the [Comète](https://team.inria.fr/Comete/) team at [Inria Saclay](https://www.inria.fr/en/inria-saclay-centre).    
I received my Ph.D. in Computer Science from the University Bourgogne Franche-Comté ([UBFC](https://spim.ubfc.fr/en/)) and my M.Sc. in Electrical Engineering from the São Paulo State University ([UNESP](https://www.feis.unesp.br/#!/ppgee)). 

🔬 **Research Interests:**  
Differential Privacy • Responsible AI • Trustworthy AI 🛡️🤖⚖️

## Recent News

<div class="news-app" id="news-app">
  <div id="news-state" class="news-state">Loading news…</div>
  <div id="news-list" class="news-list"></div>
</div>

<style>
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
