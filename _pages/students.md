---
permalink: /students/
title: "Students"
excerpt: "Students"
author_profile: true
---

<link rel="stylesheet" href="/assets/css/sheet-cards.css">
<script src="/assets/js/google-sheet-utils.js"></script>

<div class="sheet-app" id="students-app">
  <div class="sheet-state" id="students-state">Loading students…</div>
  <div id="students-list"></div>
</div>

<script>
(async () => {
  const S = window.HHASheets;
  const state = document.getElementById('students-state');
  const root = document.getElementById('students-list');
  const setState = (t) => { state.textContent = t; state.style.display = t ? 'block' : 'none'; };

  try {
    const rows = (await S.load('1794000060'))
      .filter((r) => r.name)
      .sort((a,b) => (Number(b.year||0)-Number(a.year||0)) || a.name.localeCompare(b.name));

    if (!rows.length) { setState('No student records found.'); return; }

    const current = rows.filter((r) => !S.truthy(r.completed));
    const alumni = rows.filter((r) => S.truthy(r.completed));

    const typeLabel = (level) => {
      const x = String(level || '').toLowerCase();
      if (x.includes('phd')) return 'PhD Students';
      if (x.includes('meng') || x.includes('master')) return "Master's Students";
      if (x.includes('bachelor')) return 'Bachelor Students';
      return level || 'Students';
    };

    const card = (r) => {
      const name = r.profile_url ? S.link(r.name, r.profile_url) : S.escapeHTML(r.name);
      const project = r.project_url ? S.link(r.project_title, r.project_url) : S.escapeHTML(r.project_title || '');
      return `<article class="sheet-card">
        <div>
          ${r.level ? `<span class="sheet-chip">${S.escapeHTML(r.level)}</span>` : ''}
          ${r.period ? `<span class="sheet-chip">${S.escapeHTML(r.period)}</span>` : ''}
        </div>
        <h3>${name}</h3>
        ${r.organization ? `<p class="sheet-meta">${S.escapeHTML(r.organization)}</p>` : ''}
        ${r.project_title ? `<p><strong>${S.truthy(r.completed) && String(r.level).toLowerCase().includes('phd') ? 'Thesis' : 'Topic'}:</strong> ${project}</p>` : ''}
        ${r.co_supervisor ? `<p><strong>Co-supervised with:</strong> ${S.escapeHTML(r.co_supervisor)}</p>` : ''}
        ${r.position_after ? `<p><strong>Current Position:</strong> ${S.escapeHTML(r.position_after)}</p>` : ''}
        ${r.award ? `<p><strong>🏆 Prize:</strong> ${r.award_url ? S.link(r.award, r.award_url) : S.escapeHTML(r.award)}</p>` : ''}
      </article>`;
    };

    const grouped = (title, data) => {
      if (!data.length) return '';
      const groups = {};
      data.forEach((r) => {
        const k = typeLabel(r.level);
        (groups[k] ||= []).push(r);
      });
      const order = ['PhD Students', "Master's Students", 'Bachelor Students', 'Students'];
      const keys = Object.keys(groups).sort((a,b) => {
        const ai = order.indexOf(a);
        const bi = order.indexOf(b);
        return (ai < 0 ? 99 : ai) - (bi < 0 ? 99 : bi) || a.localeCompare(b);
      });
      return `<section class="sheet-section"><h2>${title}</h2>` +
        keys.map((k) => `<h3>${S.escapeHTML(k)}</h3><div class="sheet-grid">${groups[k].map(card).join('')}</div>`).join('') +
        `</section>`;
    };

    setState('');
    root.innerHTML = grouped('Current Students', current) + grouped('Alumni', alumni);
  } catch (e) {
    setState('Unable to load students from Google Sheets. ' + e.message);
  }
})();
</script>
