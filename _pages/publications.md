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

<div class="pub-toolbar" aria-label="Filter publications">
  <div class="pub-search">
    <i class="fas fa-search" aria-hidden="true"></i>
    <input id="pub-search" type="search" autocomplete="off" placeholder="Search title, authors, venue…" aria-label="Search publications">
  </div>

  <label class="pub-filter">
    <span>Year</span>
    <select id="pub-year" aria-label="Filter publications by year">
      <option value="">All years</option>
    </select>
  </label>

  <label class="pub-filter">
    <span>Type</span>
    <select id="pub-type" aria-label="Filter publications by type">
      <option value="">All types</option>
    </select>
  </label>

  <button id="pub-clear" class="pub-clear" type="button">
    <i class="fas fa-times" aria-hidden="true"></i>
    Clear
  </button>

  <div id="pub-count" class="pub-count" aria-live="polite"></div>
</div>

<div class="pubs-app" id="publications-app">
  <div id="pubs-state" class="pubs-state">Publication content is generated during the website build.</div>
  <div id="pubs-list" class="pubs-list"></div>
</div>

<style>
  .pubs-app {
    margin-top: 1.15rem;
  }

  .pub-toolbar {
    margin: 1.35rem 0 1.1rem;
    padding: 0.9rem;
    display: grid;
    grid-template-columns: minmax(240px, 1fr) minmax(125px, 0.28fr) minmax(145px, 0.32fr) auto;
    gap: 0.65rem;
    align-items: end;
    border: 1px solid #dfe4ec;
    border-radius: 14px;
    background: linear-gradient(180deg, #ffffff 0%, #fafcff 100%);
    box-shadow: 0 8px 24px rgba(17, 24, 39, 0.045);
  }

  .pub-search {
    position: relative;
    display: flex;
    align-items: center;
  }

  .pub-search > i {
    position: absolute;
    left: 0.78rem;
    color: #64748b;
    pointer-events: none;
  }

  .pub-search input,
  .pub-filter select {
    width: 100%;
    min-height: 2.55rem;
    border: 1px solid #cfd7e3;
    border-radius: 10px;
    background: #fff;
    color: #263244;
    font: inherit;
    font-size: 0.9rem;
    outline: none;
    transition: border-color .18s ease, box-shadow .18s ease;
  }

  .pub-search input {
    padding: 0.48rem 0.75rem 0.48rem 2.35rem;
  }

  .pub-filter select {
    padding: 0.45rem 2rem 0.45rem 0.68rem;
  }

  .pub-search input:focus,
  .pub-filter select:focus {
    border-color: #60a5fa;
    box-shadow: 0 0 0 3px rgba(96, 165, 250, 0.15);
  }

  .pub-filter {
    display: grid;
    gap: 0.25rem;
    margin: 0;
  }

  .pub-filter > span {
    color: #64748b;
    font-size: 0.72rem;
    font-weight: 700;
    letter-spacing: 0.06em;
    text-transform: uppercase;
  }

  .pub-clear {
    min-height: 2.55rem;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    gap: 0.38rem;
    padding: 0.45rem 0.8rem;
    border: 1px solid #cfd7e3;
    border-radius: 10px;
    background: #fff;
    color: #475569;
    font: inherit;
    font-size: 0.85rem;
    cursor: pointer;
    transition: color .18s ease, border-color .18s ease, background .18s ease;
  }

  .pub-clear:hover {
    color: #1d4ed8;
    border-color: #93c5fd;
    background: #f8fbff;
  }

  .pub-count {
    grid-column: 1 / -1;
    min-height: 1.1rem;
    color: #64748b;
    font-size: 0.82rem;
  }

  .pubs-state {
    padding: 0.8rem 0;
    color: #6b7280;
    font-style: italic;
  }

  .pubs-list {
    display: grid;
    gap: 1.55rem;
  }

  .pub-year-group {
    display: grid;
    gap: 0.78rem;
  }

  .pub-year-heading {
    margin: 0;
    padding-left: 0.7rem;
    border-left: 4px solid #94a3b8;
    color: #334155;
    font-size: 1.08rem;
    font-weight: 750;
    letter-spacing: 0.025em;
    text-transform: uppercase;
  }

  .pub-year-list {
    display: grid;
    gap: 0.78rem;
  }

  .pubs-card {
    --pub-accent: #94a3b8;
    position: relative;
    background: #fff;
    border: 1px solid #e2e8f0;
    border-left: 4px solid var(--pub-accent);
    border-radius: 13px;
    box-shadow: 0 6px 20px rgba(15, 23, 42, 0.045);
    transition: transform .16s ease, box-shadow .16s ease, border-color .16s ease;
  }

  .pubs-card:hover {
    transform: translateY(-1px);
    box-shadow: 0 11px 28px rgba(15, 23, 42, 0.075);
  }

  .pub-card--conference { --pub-accent: #3b82f6; }
  .pub-card--journal { --pub-accent: #22a06b; }
  .pub-card--workshop { --pub-accent: #d97706; }
  .pub-card--preprint { --pub-accent: #7c3aed; }
  .pub-card--technical-report { --pub-accent: #db2777; }

  .pub-card {
    padding: 0.92rem 1rem 0.95rem;
  }

  .pub-card-top {
    display: flex;
    gap: 0.4rem;
    flex-wrap: wrap;
    margin-bottom: 0.48rem;
  }

  .pub-chip {
    display: inline-flex;
    align-items: center;
    border-radius: 999px;
    font-size: 0.76rem;
    line-height: 1;
    padding: 0.28rem 0.58rem;
    border: 1px solid #d1d5db;
    background: #f8fafc;
  }

  .pub-chip--type {
    font-weight: 700;
    text-transform: lowercase;
  }

  .pub-chip--conference { border-color: #93c5fd; background: #eff6ff; color: #1d4ed8; }
  .pub-chip--journal { border-color: #86efac; background: #f0fdf4; color: #166534; }
  .pub-chip--workshop { border-color: #fcd34d; background: #fffbeb; color: #92400e; }
  .pub-chip--preprint { border-color: #c4b5fd; background: #f5f3ff; color: #6d28d9; }
  .pub-chip--technical-report { border-color: #f9a8d4; background: #fdf2f8; color: #9d174d; }

  .pub-title {
    margin: 0;
    color: #263244;
    font-size: 1.16rem;
    line-height: 1.34;
    letter-spacing: -0.01em;
  }

  .pub-authors {
    margin-top: 0.38rem;
    color: #526071;
    font-size: 0.91rem;
    line-height: 1.45;
  }

  .pub-links {
    margin-top: 0.7rem;
    display: flex;
    flex-wrap: wrap;
    gap: 0.4rem;
  }

  .pub-resource,
  .pub-link-badge {
    display: inline-flex;
    align-items: center;
    gap: 0.36rem;
    min-height: 1.9rem;
    border: 1px solid #d6dde7;
    border-radius: 999px;
    padding: 0.22rem 0.62rem;
    background: #fff;
    color: #475569;
    font-size: 0.78rem;
    text-decoration: none !important;
    transition: transform .15s ease, border-color .15s ease, background .15s ease, color .15s ease;
  }

  .pub-resource i,
  .pub-link-badge i {
    width: 0.9rem;
    text-align: center;
    font-size: 0.82rem;
  }

  .pub-resource:hover {
    transform: translateY(-1px);
  }

  .pub-resource--venue { border-color: #bfdbfe; background: #f5f9ff; color: #1e40af; }
  .pub-resource--pdf { border-color: #fecaca; background: #fff7f7; color: #b91c1c; }
  .pub-resource--code { border-color: #ddd6fe; background: #faf8ff; color: #6d28d9; }
  .pub-resource--dataset { border-color: #bbf7d0; background: #f5fff8; color: #166534; }
  .pub-resource--slides { border-color: #bae6fd; background: #f4fbff; color: #0369a1; }
  .pub-resource--poster { border-color: #fde68a; background: #fffdf2; color: #92400e; }
  .pub-resource--video { border-color: #fecdd3; background: #fff6f7; color: #be123c; }
  .pub-resource--bibtex { border-color: #cbd5e1; background: #f8fafc; color: #334155; }

  .pub-link-badge--award {
    border-color: #f6cf61;
    background: #fff8dc;
    color: #8a5600;
    font-weight: 700;
  }

  .pub-empty {
    display: none;
    padding: 1rem;
    border: 1px dashed #cbd5e1;
    border-radius: 12px;
    color: #64748b;
    text-align: center;
  }

  @media (max-width: 800px) {
    .pub-toolbar {
      grid-template-columns: 1fr 1fr;
    }
    .pub-search {
      grid-column: 1 / -1;
    }
    .pub-clear {
      align-self: end;
    }
  }

  @media (max-width: 520px) {
    .pub-toolbar {
      grid-template-columns: 1fr;
    }
    .pub-search,
    .pub-count {
      grid-column: 1;
    }
    .pub-card {
      padding: 0.85rem 0.85rem 0.9rem;
    }
    .pub-title {
      font-size: 1.06rem;
    }
  }
</style>

<script>
(() => {
  const initFilters = () => {
    const root = document.getElementById('pubs-list');
    const search = document.getElementById('pub-search');
    const yearSelect = document.getElementById('pub-year');
    const typeSelect = document.getElementById('pub-type');
    const clear = document.getElementById('pub-clear');
    const count = document.getElementById('pub-count');
    if (!root || !search || !yearSelect || !typeSelect || !clear || !count) return;

    const cards = Array.from(root.querySelectorAll('.pub-card[data-year][data-type]'));
    if (!cards.length) return;

    const years = [...new Set(cards.map((card) => card.dataset.year).filter(Boolean))]
      .sort((a, b) => Number(b) - Number(a));

    const typeLabels = {
      conference: 'Conference',
      journal: 'Journal',
      workshop: 'Workshop',
      preprint: 'Preprint',
      'technical-report': 'Technical reports',
      publication: 'Other'
    };

    const types = [...new Set(cards.map((card) => card.dataset.type).filter(Boolean))]
      .sort((a, b) => (typeLabels[a] || a).localeCompare(typeLabels[b] || b));

    years.forEach((year) => {
      yearSelect.insertAdjacentHTML('beforeend', `<option value="${year}">${year}</option>`);
    });

    types.forEach((type) => {
      const label = typeLabels[type] || type.replace(/-/g, ' ').replace(/\b\w/g, (m) => m.toUpperCase());
      typeSelect.insertAdjacentHTML('beforeend', `<option value="${type}">${label}</option>`);
    });

    const apply = () => {
      const query = search.value.trim().toLocaleLowerCase();
      const year = yearSelect.value;
      const type = typeSelect.value;
      let visible = 0;

      cards.forEach((card) => {
        const matchesSearch = !query || card.textContent.toLocaleLowerCase().includes(query);
        const matchesYear = !year || card.dataset.year === year;
        const matchesType = !type || card.dataset.type === type;
        const show = matchesSearch && matchesYear && matchesType;
        card.hidden = !show;
        if (show) visible += 1;
      });

      root.querySelectorAll('.pub-year-group').forEach((section) => {
        const hasVisible = Array.from(section.querySelectorAll('.pub-card')).some((card) => !card.hidden);
        section.hidden = !hasVisible;
      });

      count.textContent = visible === cards.length
        ? `${cards.length} publications`
        : `${visible} of ${cards.length} publications`;
    };

    [search, yearSelect, typeSelect].forEach((control) => {
      control.addEventListener(control === search ? 'input' : 'change', apply);
    });

    clear.addEventListener('click', () => {
      search.value = '';
      yearSelect.value = '';
      typeSelect.value = '';
      apply();
      search.focus();
    });

    apply();
  };

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initFilters);
  } else {
    initFilters();
  }
})();
</script>
