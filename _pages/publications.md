---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

Here I list my peer-reviewed publications ordered by year, including their pdf (or author's pdf version) and their resources when applicable (e.g., presentation, video-presentation, dataset, codes).  
The author order indicates the magnitude of contribution, with the first author adding the most value.  
The superscript \* indicates equal contributions to the paper.  
You can also check out my [ORCID](https://orcid.org/0000-0001-8059-7094), [DBLP](https://dblp.uni-trier.de/pid/248/5342.html), [Google Scholar](https://scholar.google.com/citations?hl=en&user=VJgSocwAAAAJ&view_op=list_works&sortby=pubdate), [Web of Science](https://www.webofscience.com/wos/author/record/2095547) and [Lattes CV](http://lattes.cnpq.br/6492386691695466) pages.

<div class="pubs-app" id="publications-app">
  <div class="pubs-card pubs-controls">
    <div class="pubs-control-grid">
      <label class="pubs-control">
        <span>Type</span>
        <select id="pubs-type-filter" aria-label="Filter publications by type">
          <option value="all">All</option>
        </select>
      </label>

      <label class="pubs-control">
        <span>Year</span>
        <select id="pubs-year-filter" aria-label="Filter publications by year">
          <option value="all">All</option>
        </select>
      </label>
    </div>

    <div class="pubs-controls-footer">
      <button type="button" id="pubs-clear-filters" class="btn btn--small">Clear</button>
      <span id="pubs-results-count" class="pubs-count" aria-live="polite">0/0</span>
    </div>
  </div>

  <div id="pubs-state" class="pubs-state">Loading publications…</div>
  <div id="pubs-list" class="pubs-list"></div>
</div>

<style>
  .pubs-app {
    margin-top: 1.5rem;
  }

  .pubs-card {
    background: #fff;
    border: 1px solid #e5e7eb;
    border-radius: 14px;
    box-shadow: 0 8px 24px rgba(17, 24, 39, 0.06);
  }

  .pubs-controls {
    padding: 1rem;
    margin-bottom: 1rem;
  }

  .pubs-control-grid {
    display: grid;
    gap: 0.8rem;
    grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
  }

  .pubs-control span {
    display: block;
    font-weight: 600;
    margin-bottom: 0.3rem;
  }

  .pubs-control select {
    width: 100%;
    border: 1px solid #d1d5db;
    border-radius: 8px;
    padding: 0.55rem 0.7rem;
    background: #fff;
  }

  .pubs-controls-footer {
    margin-top: 0.8rem;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }

  .pubs-count {
    color: #6b7280;
    font-size: 0.95rem;
  }

  .pubs-state {
    padding: 0.8rem 0;
    color: #6b7280;
    font-style: italic;
  }

  .pubs-list {
    display: grid;
    gap: 1rem;
  }

  .pub-card {
    padding: 0.95rem 1rem;
  }

  .pub-card-top {
    display: flex;
    gap: 0.4rem;
    flex-wrap: wrap;
    margin-bottom: 0.55rem;
  }

  .pub-chip {
    display: inline-flex;
    align-items: center;
    border-radius: 999px;
    font-size: 0.82rem;
    padding: 0.12rem 0.55rem;
    border: 1px solid #d1d5db;
    background: #f9fafb;
  }

  .pub-chip--type {
    border-color: #93c5fd;
    background: #eff6ff;
    color: #1d4ed8;
    text-transform: lowercase;
    font-weight: 600;
  }

  .pub-title {
    margin: 0;
    font-size: 1.23rem;
    line-height: 1.35;
  }

  .pub-authors,
  .pub-venue {
    margin-top: 0.45rem;
    color: #4b5563;
  }

  .pub-links {
    margin-top: 0.75rem;
    display: flex;
    flex-wrap: wrap;
    gap: 0.45rem;
  }

  .pub-links a {
    display: inline-flex;
    align-items: center;
    border: 1px solid #d1d5db;
    border-radius: 999px;
    padding: 0.2rem 0.62rem;
    font-size: 0.82rem;
    text-decoration: none;
    color: #374151;
    background: #fff;
  }

  .pub-links a:hover {
    border-color: #60a5fa;
    color: #1d4ed8;
  }

  .pub-award {
    margin-top: 0.55rem;
    color: #b45309;
    font-weight: 600;
  }
</style>

<script>
(() => {
  const SHEET_ID = '12bFYV-4WC1PhxKrnSVh5s3SPfe63fY3qd_qXybD43qw';
  const SHEET_GID = '1565301812';
  const CSV_URL = `https://docs.google.com/spreadsheets/d/${SHEET_ID}/gviz/tq?tqx=out:csv&gid=${SHEET_GID}`;

  const typeFilter = document.getElementById('pubs-type-filter');
  const yearFilter = document.getElementById('pubs-year-filter');
  const clearButton = document.getElementById('pubs-clear-filters');
  const countNode = document.getElementById('pubs-results-count');
  const listNode = document.getElementById('pubs-list');
  const stateNode = document.getElementById('pubs-state');

  if (!typeFilter || !yearFilter || !clearButton || !countNode || !listNode || !stateNode) {
    return;
  }

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
        if (c === '\r' && next === '\n') {
          i += 1;
        }
        row.push(field);
        if (row.some((value) => value.trim() !== '')) {
          rows.push(row);
        }
        row = [];
        field = '';
      } else {
        field += c;
      }
    }

    if (field.length > 0 || row.length > 0) {
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

  const truthy = (value) => {
    const normalized = String(value || '').toLowerCase().trim();
    return ['true', 'yes', 'y', '1'].includes(normalized);
  };

  const prettyType = (value) => {
    const raw = String(value || '').toLowerCase().trim();
    if (!raw) return 'publication';
    if (raw === 'journal') return 'journal';
    if (raw === 'conference') return 'conference';
    if (raw === 'workshop') return 'workshop';
    return raw;
  };

  const toEntries = (rows) => {
    if (!rows.length) return [];

    const headers = rows[0].map(normalizeKey);
    const entries = rows.slice(1).map((columns) => {
      const item = {};
      headers.forEach((header, index) => {
        item[header] = (columns[index] || '').trim();
      });

      const year = item.year || (item.pub_date || '').slice(0, 4);
      return {
        type: prettyType(item.category || item.type),
        pubDate: item.pub_date || '',
        year,
        authors: item.authors || '',
        title: item.title || '',
        venue: item.venue || '',
        urlPub: item.url_pub || item.url || '',
        code: item.code || '',
        pdf: item.pdf || '',
        slides: item.slides || '',
        poster: item.poster || '',
        video: item.video || '',
        awards: item.awards || '',
        bibtex: item.bibtex || '',
        hidden: truthy(item.not_on_website),
      };
    }).filter((entry) => entry.title && !entry.hidden);

    return entries.sort((a, b) => {
      if (a.pubDate && b.pubDate) {
        return b.pubDate.localeCompare(a.pubDate);
      }
      return String(b.year).localeCompare(String(a.year));
    });
  };

  const createLink = (label, href) => {
    if (!href) return '';
    return `<a href="${href}" target="_blank" rel="noopener noreferrer">${label}</a>`;
  };

  const renderCard = (entry) => {
    const links = [
      createLink('Venue', entry.urlPub),
      createLink('Code', entry.code),
      createLink('PDF', entry.pdf),
      createLink('Slides', entry.slides),
      createLink('Poster', entry.poster),
      createLink('Video', entry.video),
      createLink('BibTeX', entry.bibtex),
    ].filter(Boolean).join('');

    return `
      <article class="pubs-card pub-card">
        <div class="pub-card-top">
          <span class="pub-chip pub-chip--type">${entry.type}</span>
          <span class="pub-chip">${entry.year || 'n/a'}</span>
        </div>
        <h3 class="pub-title">${entry.title}</h3>
        ${entry.authors ? `<div class="pub-authors">${entry.authors}</div>` : ''}
        ${entry.venue ? `<div class="pub-venue">${entry.venue}</div>` : ''}
        ${entry.awards ? `<div class="pub-award">🏆 ${entry.awards}</div>` : ''}
        ${links ? `<div class="pub-links">${links}</div>` : ''}
      </article>
    `;
  };

  const uniqueSorted = (items) => Array.from(new Set(items.filter(Boolean)));

  const setOptions = (node, values) => {
    const base = node.id === 'pubs-type-filter' ? 'Type' : 'Year';
    const sorted = base === 'Year'
      ? values.sort((a, b) => Number(b) - Number(a))
      : values.sort();

    node.innerHTML = `<option value="all">All ${base}s</option>${sorted
      .map((value) => `<option value="${value}">${value}</option>`)
      .join('')}`;
  };

  const setState = (text) => {
    stateNode.textContent = text;
    stateNode.style.display = text ? 'block' : 'none';
  };

  const run = async () => {
    try {
      const response = await fetch(CSV_URL);
      if (!response.ok) {
        throw new Error(`Could not load spreadsheet (${response.status})`);
      }

      const text = await response.text();
      const entries = toEntries(parseCSV(text));

      if (!entries.length) {
        setState('No publications found in the spreadsheet.');
        countNode.textContent = '0/0';
        return;
      }

      setOptions(typeFilter, uniqueSorted(entries.map((entry) => entry.type)));
      setOptions(yearFilter, uniqueSorted(entries.map((entry) => entry.year)));

      const render = () => {
        const currentType = typeFilter.value;
        const currentYear = yearFilter.value;
        const filtered = entries.filter((entry) => {
          const typeOk = currentType === 'all' || entry.type === currentType;
          const yearOk = currentYear === 'all' || String(entry.year) === currentYear;
          return typeOk && yearOk;
        });

        countNode.textContent = `${filtered.length}/${entries.length}`;

        if (!filtered.length) {
          listNode.innerHTML = '';
          setState('No publications match the selected filters.');
          return;
        }

        setState('');
        listNode.innerHTML = filtered.map(renderCard).join('');
      };

      typeFilter.addEventListener('change', render);
      yearFilter.addEventListener('change', render);
      clearButton.addEventListener('click', () => {
        typeFilter.value = 'all';
        yearFilter.value = 'all';
        render();
      });

      render();
    } catch (error) {
      setState(`Unable to load publications from Google Sheets. ${error.message}`);
      countNode.textContent = '0/0';
    }
  };

  run();
})();
</script>
