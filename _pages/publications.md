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
  <div id="pub-year-index" class="pub-year-index"></div>
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
  const yearCounts = {};
  cards.forEach((card) => { yearCounts[card.dataset.year] = (yearCounts[card.dataset.year] || 0) + 1; });

  yearIndex.innerHTML = Object.keys(yearCounts)
    .filter((year) => /^\d{4}$/.test(year))
    .sort((a,b) => Number(b) - Number(a))
    .map((year) => `<a href="#pub-${year}">${year} <span>(${yearCounts[year]})</span></a>`)
    .join('');

  const apply = () => {
    const q = search.value.trim().toLocaleLowerCase();
    let visible = 0;
    cards.forEach((card) => {
      const show = !q || card.textContent.toLocaleLowerCase().includes(q);
      card.hidden = !show;
      if (show) visible += 1;
    });
    groups.forEach((group) => {
      group.hidden = !Array.from(group.querySelectorAll('.pub-card')).some((card) => !card.hidden);
    });
    count.textContent = q ? `${visible} of ${cards.length} publications` : `${cards.length} publications`;
  };

  search.addEventListener('input', apply);
  apply();
})();
</script>
