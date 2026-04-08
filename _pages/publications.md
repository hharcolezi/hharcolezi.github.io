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

  .pubs-state {
    padding: 0.8rem 0;
    color: #6b7280;
    font-style: italic;
  }

  .pubs-list {
    display: grid;
    gap: 1.4rem;
  }

  .pub-year-group {
    display: grid;
    gap: 0.8rem;
  }

  .pub-year-heading {
    margin: 0;
    font-size: 1.1rem;
    letter-spacing: 0.03em;
    text-transform: uppercase;
    color: #374151;
    border-left: 4px solid #9ca3af;
    padding-left: 0.6rem;
  }

  .pub-year-list {
    display: grid;
    gap: 0.9rem;
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
    font-weight: 600;
    text-transform: lowercase;
  }

  .pub-chip--conference {
    border-color: #93c5fd;
    background: #eff6ff;
    color: #1d4ed8;
  }

  .pub-chip--journal {
    border-color: #86efac;
    background: #f0fdf4;
    color: #166534;
  }

  .pub-chip--workshop {
    border-color: #fcd34d;
    background: #fffbeb;
    color: #92400e;
  }

  .pub-chip--preprint {
    border-color: #c4b5fd;
    background: #f5f3ff;
    color: #6d28d9;
  }

  .pub-chip--publication {
    border-color: #d1d5db;
    background: #f9fafb;
    color: #374151;
  }

  .pub-title {
    margin: 0;
    font-size: 1.23rem;
    line-height: 1.35;
  }

  .pub-authors {
    margin-top: 0.45rem;
    color: #4b5563;
  }

  .pub-venue-line {
    margin-top: 0.5rem;
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

  .pub-links .pub-link-badge {
    display: inline-flex;
    align-items: center;
    border: 1px solid #d1d5db;
    border-radius: 999px;
    padding: 0.2rem 0.62rem;
    font-size: 0.82rem;
    color: #374151;
    background: #fff;
  }

  .pub-links a span,
  .pub-links .pub-link-badge span {
    margin-right: 0.3rem;
  }

  .pub-links a:hover {
    border-color: #60a5fa;
    color: #1d4ed8;
  }

  .pub-links .pub-link-badge--award {
    border-color: #fbbf24;
    background: #fffbeb;
    color: #92400e;
    font-weight: 600;
  }

  .pub-links .pub-link-badge--venue {
    border-color: #93c5fd;
    background: #eff6ff;
    color: #1d4ed8;
    font-weight: 600;
  }
</style>

<script>
(() => {
  const SHEET_ID = '12bFYV-4WC1PhxKrnSVh5s3SPfe63fY3qd_qXybD43qw';
  const SHEET_GID = '1565301812';
  const CSV_URL = `https://docs.google.com/spreadsheets/d/${SHEET_ID}/gviz/tq?tqx=out:csv&gid=${SHEET_GID}`;

  const listNode = document.getElementById('pubs-list');
  const stateNode = document.getElementById('pubs-state');

  if (!listNode || !stateNode) {
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
    if (raw === 'preprint') return 'preprint';
    return 'publication';
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
        dataset: item.dataset || '',
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

  const createLink = (label, href, icon = '') => {
    if (!href) return '';
    const prefix = icon ? `<span aria-hidden="true">${icon}</span>` : '';
    return `<a href="${href}" target="_blank" rel="noopener noreferrer">${prefix}${label}</a>`;
  };

  const createBadge = (label, icon = '', className = '') => {
    if (!label) return '';
    const prefix = icon ? `<span aria-hidden="true">${icon}</span>` : '';
    const extraClass = className ? ` ${className}` : '';
    return `<span class="pub-link-badge${extraClass}">${prefix}${label}</span>`;
  };

  const createVenueElement = (venue, urlPub) => {
    if (!venue) return '';
    if (urlPub) return createLink(venue, urlPub, '🏛️');
    return createBadge(venue, '🏛️', 'pub-link-badge--venue');
  };

  const renderCard = (entry) => {
    const links = [
      createBadge(entry.awards, '🏆', 'pub-link-badge--award'),
      createLink('ArXiv', entry.pdf, '📄'),
      createLink('Code', entry.code, '💻'),
      createLink('Slides', entry.slides, '🖼️'),
      createLink('Poster', entry.poster, '🧾'),
      createLink('Video', entry.video, '🎥'),
      createLink('BibTeX', entry.bibtex, '📚'),
    ].filter(Boolean).join('');
    const venueElement = createVenueElement(entry.venue, entry.urlPub);

    const typeClass = `pub-chip--${entry.type.replace(/[^a-z0-9]+/g, '-')}`;

    return `
      <article class="pubs-card pub-card">
        <div class="pub-card-top">
          <span class="pub-chip pub-chip--type ${typeClass}">${entry.type}</span>
        </div>
        <h3 class="pub-title">${entry.title}</h3>
        ${entry.authors ? `<div class="pub-authors">${entry.authors}</div>` : ''}
        ${venueElement ? `<div class="pub-links pub-venue-line">${venueElement}</div>` : ''}
        ${links ? `<div class="pub-links">${links}</div>` : ''}
      </article>
    `;
  };

  const setState = (text) => {
    stateNode.textContent = text;
    stateNode.style.display = text ? 'block' : 'none';
  };

  const groupByYear = (entries) => entries.reduce((acc, entry) => {
    const key = entry.year || 'Unknown year';
    if (!acc[key]) acc[key] = [];
    acc[key].push(entry);
    return acc;
  }, {});

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
        return;
      }

      const groups = groupByYear(entries);
      const years = Object.keys(groups).sort((a, b) => Number(b) - Number(a));

      setState('');
      listNode.innerHTML = years.map((year) => `
        <section class="pub-year-group" aria-label="Publications from ${year}">
          <h2 class="pub-year-heading">${year}</h2>
          <div class="pub-year-list">
            ${groups[year].map(renderCard).join('')}
          </div>
        </section>
      `).join('');
    } catch (error) {
      setState(`Unable to load publications from Google Sheets. ${error.message}`);
    }
  };

  run();
})();
</script>
