---
layout: archive
title: "Academic Profile"
permalink: /academic/
author_profile: true
---

<link rel="stylesheet" href="/assets/css/sheet-cards.css">
<script src="/assets/js/google-sheet-utils.js"></script>

<p>This page summarizes professional positions, education, honors, academic service, affiliations, research interests, and other academic activities from the same Google Sheet used for my CV.</p>

<div class="sheet-app">
  <div class="sheet-state" id="academic-state">Loading academic profile…</div>
  <div id="academic-list"></div>
</div>

<script>
(async () => {
  const S = window.HHASheets;
  const state = document.getElementById('academic-state');
  const root = document.getElementById('academic-list');
  const setState = (t) => { state.textContent = t; state.style.display = t ? 'block' : 'none'; };

  const specs = [
    { title:'Professional Experience', gid:'637699561', render:(r) => `
      <article class="sheet-card">
        <div>${r.period ? `<span class="sheet-chip">${S.escapeHTML(r.period)}</span>` : ''}</div>
        <h3>${S.escapeHTML(r.role || '')}</h3>
        <p>${S.escapeHTML([r.institution,r.location].filter(Boolean).join(', '))}</p>
        ${r.note ? `<p class="sheet-meta">${S.escapeHTML(r.note)} ${r.note_url ? S.link('More information', r.note_url) : ''}</p>` : ''}
      </article>` },
    { title:'Education', gid:'591062090', render:(r) => `
      <article class="sheet-card">
        <div>${r.period ? `<span class="sheet-chip">${S.escapeHTML(r.period)}</span>` : ''}</div>
        <h3>${S.escapeHTML(r.degree || '')}</h3>
        <p>${S.escapeHTML(r.institution || '')}</p>
        ${r.thesis ? `<p><strong>Thesis:</strong> ${r.thesis_url ? S.link(r.thesis, r.thesis_url) : S.escapeHTML(r.thesis)}</p>` : ''}
        ${r.advisors ? `<p class="sheet-meta"><strong>Advisor(s):</strong> ${S.escapeHTML(r.advisors)}</p>` : ''}
      </article>` },
    { title:'Honors & Awards', gid:'927050591', filter:(r)=>S.selected(r), render:(r) => `
      <article class="sheet-card">
        <div>${r.year ? `<span class="sheet-chip">${S.escapeHTML(r.year)}</span>` : ''}</div>
        <h3>${r.url ? S.link(r.name, r.url) : S.escapeHTML(r.name || '')}</h3>
        ${r.venue ? `<p>${S.escapeHTML(r.venue)}</p>` : ''}
        ${r.description ? `<p class="sheet-meta">${S.escapeHTML(r.description)}</p>` : ''}
      </article>` },
    { title:'Academic Service', gid:'254675640', filter:(r)=>S.selected(r), render:(r) => `
      <article class="sheet-card">
        <div>
          ${r.year ? `<span class="sheet-chip">${S.escapeHTML(r.year)}</span>` : ''}
          ${r.role ? `<span class="sheet-chip">${S.escapeHTML(r.role)}</span>` : ''}
        </div>
        <h3>${r.url ? S.link(r.venue || r.description, r.url) : S.escapeHTML(r.venue || r.description || '')}</h3>
        ${r.description && r.venue ? `<p>${S.escapeHTML(r.description)}</p>` : ''}
        ${r.location ? `<p class="sheet-meta">${S.escapeHTML(r.location)}</p>` : ''}
      </article>` },
    { title:'Affiliations', gid:'1505546709', render:(r) => `
      <article class="sheet-card"><h3>${S.escapeHTML(r.role || r.institution || '')}</h3>
      <p>${S.escapeHTML([r.institution,r.location,r.period].filter(Boolean).join(' · '))}</p></article>` },
    { title:'Research Interests', gid:'1563030652', render:(r) => `
      <article class="sheet-card"><h3>${S.escapeHTML(r.item || r.interest || r.title || Object.values(r)[0] || '')}</h3></article>` },
    { title:'Community Outreach', gid:'259198762', filter:(r)=>S.selected(r), render:(r) => `
      <article class="sheet-card"><div>${r.year ? `<span class="sheet-chip">${S.escapeHTML(r.year)}</span>` : ''}</div>
      <h3>${S.escapeHTML(r.item || r.category || '')}</h3>${r.description ? `<p>${S.escapeHTML(r.description)}</p>` : ''}</article>` },
    { title:'Skills', gid:'986343425', render:(r) => `
      <article class="sheet-card"><h3>${S.escapeHTML(r.category || '')}</h3><p>${S.escapeHTML(r.item || '')}</p></article>` }
  ];

  try {
    const rendered = [];
    for (const spec of specs) {
      let rows = await S.load(spec.gid);
      if (spec.filter) rows = rows.filter(spec.filter);
      rows = rows.filter((r) => Object.values(r).some((v)=>String(v).trim()));
      if (!rows.length) continue;
      rows.sort((a,b)=>S.year(b)-S.year(a));
      rendered.push(`<section class="sheet-section"><h2>${spec.title}</h2>
        <div class="sheet-grid">${rows.map(spec.render).join('')}</div></section>`);
    }
    setState('');
    root.innerHTML = rendered.join('');
  } catch (e) {
    setState('Unable to load academic profile from Google Sheets. ' + e.message);
  }
})();
</script>
