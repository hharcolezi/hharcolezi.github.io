---
layout: archive
title: "Software & Datasets"
permalink: /software/
author_profile: true
---

<link rel="stylesheet" href="/assets/css/sheet-cards.css">
<script src="/assets/js/google-sheet-utils.js"></script>

<p>Selected open-source libraries and datasets associated with my work on privacy-preserving and responsible machine learning.</p>

<div class="sheet-app">
  <div class="sheet-state" id="software-state">Loading software and datasets…</div>
  <div id="software-list"></div>
</div>

<script>
(async () => {
  const S = window.HHASheets;
  const state = document.getElementById('software-state');
  const root = document.getElementById('software-list');
  const setState = (t) => { state.textContent = t; state.style.display = t ? 'block' : 'none'; };

  try {
    const allowed = new Set(['Libraries & Tools','Datasets']);
    const rows = (await S.load('1684913614'))
      .filter((r) => r.name && S.truthy(r.in_website) && allowed.has(r.category))
      .sort((a,b) => Number(a.sort_order || 999) - Number(b.sort_order || 999));

    if (!rows.length) { setState('No software or datasets found.'); return; }

    const groups = {};
    rows.forEach((r) => (groups[r.category || 'Other'] ||= []).push(r));

    const card = (r) => {
      const links = [
        r.github ? S.link('GitHub', r.github) : '',
        r.pypi ? S.link('PyPI', r.pypi) : '',
        r.paper ? S.link('Paper', r.paper) : '',
        r.arxiv ? S.link('arXiv', r.arxiv) : '',
        r.data_url ? S.link('Data', r.data_url) : ''
      ].filter(Boolean).map((x) => '<span>' + x + '</span>').join('');

      return '<article class="sheet-card">' +
        '<h3>' + S.escapeHTML(r.name) + '</h3>' +
        (r.description ? '<p>' + S.escapeHTML(r.description) + '</p>' : '') +
        (links ? '<div class="sheet-links">' + links + '</div>' : '') +
        '</article>';
    };

    const order = ['Libraries & Tools','Datasets'];
    const keys = Object.keys(groups).sort((a,b) => {
      const ai = order.indexOf(a), bi = order.indexOf(b);
      return (ai < 0 ? 99 : ai) - (bi < 0 ? 99 : bi) || a.localeCompare(b);
    });

    setState('');
    root.innerHTML = keys.map((category) =>
      '<section class="sheet-section"><h2>' + S.escapeHTML(category) + '</h2>' +
      '<div class="sheet-grid">' + groups[category].map(card).join('') + '</div></section>'
    ).join('');
  } catch (e) {
    setState('Unable to load software and datasets from Google Sheets. ' + e.message);
  }
})();
</script>
