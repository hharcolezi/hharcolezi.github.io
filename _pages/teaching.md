---
layout: archive
title: "Teaching"
permalink: /teaching/
author_profile: true
---

<link rel="stylesheet" href="/assets/css/sheet-cards.css">
<script src="/assets/js/google-sheet-utils.js"></script>

<div class="sheet-app">
  <div class="sheet-state" id="teaching-state">Loading teaching…</div>
  <div id="teaching-list"></div>
</div>

<script>
(async () => {
  const S = window.HHASheets;
  const state = document.getElementById('teaching-state');
  const root = document.getElementById('teaching-list');
  const setState = (t) => { state.textContent = t; state.style.display = t ? 'block' : 'none'; };

  try {
    const rows = (await S.load('1100989932'))
      .filter((r) => r.course || r.description)
      .sort((a,b) => Number(b.year||0)-Number(a.year||0));

    const groups = {};
    rows.forEach((r) => (groups[r.year || 'Other'] ||= []).push(r));

    const card = (r) => {
      const course = r.course || r.description;
      const inst = r.institution_url ? S.link(r.institution || r.organization, r.institution_url) : S.escapeHTML(r.institution || r.organization || '');
      return `<article class="sheet-card">
        <div>
          ${r.period ? `<span class="sheet-chip">${S.escapeHTML(r.period)}</span>` : ''}
          ${r.hours ? `<span class="sheet-chip">${S.escapeHTML(r.hours)}h</span>` : ''}
          ${r.role ? `<span class="sheet-chip">${S.escapeHTML(r.role)}</span>` : ''}
        </div>
        <h3>${S.escapeHTML(course)}</h3>
        ${r.program ? `<p>${S.escapeHTML(r.program)}${inst ? ', ' + inst : ''}</p>` : (inst ? `<p>${inst}</p>` : '')}
        ${r.topics ? `<p class="sheet-meta">${S.escapeHTML(r.topics)}</p>` : ''}
      </article>`;
    };

    setState('');
    root.innerHTML = Object.keys(groups).sort((a,b)=>Number(b)-Number(a)).map((year) => `
      <section class="sheet-section"><h2>${S.escapeHTML(year)}</h2>
      <div class="sheet-grid">${groups[year].map(card).join('')}</div></section>`).join('');
  } catch (e) {
    setState('Unable to load teaching from Google Sheets. ' + e.message);
  }
})();
</script>
