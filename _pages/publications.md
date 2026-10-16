---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

<link rel="stylesheet" href="/assets/css/soft-academic.css">

<p class="soft-intro">
Peer-reviewed publications and technical reports, ordered by year. Resource links and BibTeX are shown when available.
You can also find me on
<a href="https://orcid.org/0000-0001-8059-7094" target="_blank" rel="noopener noreferrer">ORCID</a>,
<a href="https://dblp.uni-trier.de/pid/248/5342.html" target="_blank" rel="noopener noreferrer">DBLP</a>, and
<a href="https://scholar.google.com/citations?hl=en&user=VJgSocwAAAAJ&view_op=list_works&sortby=pubdate" target="_blank" rel="noopener noreferrer">Google Scholar</a>.
</p>

<div class="pub-minimal-tools">
  <div class="pub-search-line">
    <i class="fas fa-search" aria-hidden="true"></i>
    <input id="pub-search" type="search" autocomplete="off" placeholder="Search publications…" aria-label="Search publications">
  </div>
  <nav id="pub-year-index" class="pub-year-index" aria-label="Publication sections"></nav>
  <div id="pub-count" class="pub-count" aria-live="polite"></div>
</div>

<div class="pubs-app" id="publications-app">
  <div id="pubs-state" class="pubs-state">Publication content is generated during the website build.</div>
  <div id="pubs-list" class="pubs-list"></div>
</div>

<script>
(() => {
  const root = document.getElementById('pubs-list');
  const search = document.getElementById('pub-search');
  const count = document.getElementById('pub-count');
  const yearIndex = document.getElementById('pub-year-index');
  if (!root || !search || !count || !yearIndex) return;

  const cards = Array.from(root.querySelectorAll('.pub-card[data-year]'));
  const groups = Array.from(root.querySelectorAll('.pub-year-group'));
  // Use the rendered sections so report dates never create extra year links
  // or inflate a year's publication count.
  const reportCards = Array.from(root.querySelectorAll('#pub-technical-reports .pub-card'));
  const publicationCards = cards.filter((card) => !reportCards.includes(card));
  groups.forEach((group) => {
    const reports = group.id === 'pub-technical-reports';
    const label = reports ? 'Technical reports' : group.id.replace(/^pub-/, '');
    const anchor = document.createElement('a');
    anchor.href = `#${group.id}`;
    anchor.textContent = `${label} (${group.querySelectorAll('.pub-card').length})`;
    if (reports) anchor.className = 'pub-year-index__reports';
    yearIndex.appendChild(anchor);
  });

  const apply = () => {
    const q = search.value.trim().toLocaleLowerCase();
    cards.forEach((card) => {
      const show = !q || card.textContent.toLocaleLowerCase().includes(q);
      card.hidden = !show;
    });
    groups.forEach((group) => {
      group.hidden = !Array.from(group.querySelectorAll('.pub-card')).some((card) => !card.hidden);
    });
    const describe = (items, label) => {
      const matches = items.filter((card) => !card.hidden).length;
      return `${q ? `${matches} of ` : ''}${items.length} ${label}${items.length === 1 ? '' : 's'}`;
    };
    count.textContent = [
      describe(publicationCards, 'publication'),
      ...(reportCards.length ? [describe(reportCards, 'technical report')] : []),
    ].join(' · ');
  };

  search.addEventListener('input', apply);
  apply();
})();
</script>
