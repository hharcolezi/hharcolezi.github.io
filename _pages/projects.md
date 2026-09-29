---
permalink: /projects/
title: "Projects"
excerpt: "Research Projects"
author_profile: true
redirect_from:
  - /projects.html
---

<link rel="stylesheet" href="/assets/css/sheet-cards.css">
<script src="/assets/js/google-sheet-utils.js"></script>

<div class="sheet-app" id="projects-app">
  <div class="sheet-state" id="projects-state">Loading projects…</div>
  <div id="projects-list"></div>
</div>

<script>
(async () => {
  const state = document.getElementById('projects-state');
  const root = document.getElementById('projects-list');
  const S = window.HHASheets;
  const setState = (t) => { state.textContent = t; state.style.display = t ? 'block' : 'none'; };

  try {
    const rows = (await S.load('1323298866'))
      .filter((r) => r.title && (!r.awarded || S.truthy(r.awarded)))
      .sort((a,b) => String(b.date || '').localeCompare(String(a.date || '')));

    if (!rows.length) { setState('No projects found.'); return; }

    const now = new Date().getFullYear();
    const endYear = (period) => {
      const years = String(period || '').match(/\d{4}/g) || [];
      return years.length ? Number(years[years.length - 1]) : 9999;
    };
    const current = rows.filter((r) => endYear(r.period) >= now);
    const past = rows.filter((r) => endYear(r.period) < now);

    const card = (r) => {
      const title = r.project_url ? S.link(r.title, r.project_url) : S.escapeHTML(r.title);
      const funding = [r.amount, r.program].filter(Boolean).join(' — ');
      const meta = [
        r.period ? `<span class="sheet-chip">${S.escapeHTML(r.period)}</span>` : '',
        r.organization ? `<span class="sheet-chip">${S.escapeHTML(r.organization)}</span>` : ''
      ].join('');
      const links = [
        r.program_url ? S.link('Program', r.program_url) : '',
        r.project_url ? S.link('Project', r.project_url) : ''
      ].filter(Boolean).map(x => `<span>${x}</span>`).join('');
      return `<article class="sheet-card">
        <div>${meta}</div>
        <h3>${title}</h3>
        ${funding ? `<p class="sheet-meta"><strong>Funding:</strong> ${S.escapeHTML(funding)}</p>` : ''}
        ${r.role ? `<p><strong>Role:</strong> ${S.escapeHTML(r.role)}</p>` : ''}
        ${r.institutions ? `<p><strong>Partners:</strong> ${S.escapeHTML(r.institutions)}</p>` : ''}
        ${r.scope ? `<p><strong>Scope:</strong> ${S.escapeHTML(r.scope)}</p>` : ''}
        ${links ? `<div class="sheet-links">${links}</div>` : ''}
      </article>`;
    };

    const section = (title, data) => data.length ? `
      <section class="sheet-section">
        <h2>${title}</h2>
        <div class="sheet-grid">${data.map(card).join('')}</div>
      </section>` : '';

    setState('');
    root.innerHTML = section('Current Projects', current) + section('Past Projects', past);
  } catch (e) {
    setState('Unable to load projects from Google Sheets. ' + e.message);
  }
})();
</script>
