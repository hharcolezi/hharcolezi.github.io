window.HHASheets = (() => {
  const SHEET_ID = '12bFYV-4WC1PhxKrnSVh5s3SPfe63fY3qd_qXybD43qw';

  const parseCSV = (text) => {
    const rows = [];
    let row = [], field = '', inQuotes = false;
    for (let i = 0; i < text.length; i += 1) {
      const c = text[i], next = text[i + 1];
      if (c === '"') {
        if (inQuotes && next === '"') { field += '"'; i += 1; }
        else inQuotes = !inQuotes;
      } else if (c === ',' && !inQuotes) {
        row.push(field); field = '';
      } else if ((c === '\n' || c === '\r') && !inQuotes) {
        if (c === '\r' && next === '\n') i += 1;
        row.push(field);
        if (row.some((x) => String(x).trim() !== '')) rows.push(row);
        row = []; field = '';
      } else field += c;
    }
    if (field.length || row.length) { row.push(field); rows.push(row); }
    return rows;
  };

  const key = (value) => String(value || '').toLowerCase().trim()
    .replace(/[^a-z0-9]+/g, '_').replace(/^_+|_+$/g, '');

  const truthy = (value) => ['1','true','yes','y','x'].includes(String(value || '').trim().toLowerCase());

  const escapeHTML = (value) => String(value ?? '')
    .replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;')
    .replace(/"/g,'&quot;').replace(/'/g,'&#39;');

  const safeUrl = (value) => {
    const raw = String(value || '').trim();
    if (!raw) return '';
    try {
      const url = new URL(raw);
      return ['http:','https:'].includes(url.protocol) ? url.toString() : '';
    } catch (_) { return ''; }
  };

  const link = (label, url) => {
    const safe = safeUrl(url);
    return safe
      ? `<a href="${escapeHTML(safe)}" target="_blank" rel="noopener noreferrer">${escapeHTML(label)}</a>`
      : escapeHTML(label);
  };

  const load = async (gid) => {
    const url = `https://docs.google.com/spreadsheets/d/${SHEET_ID}/gviz/tq?tqx=out:csv&gid=${gid}`;
    const response = await fetch(url);
    if (!response.ok) throw new Error(`Could not load spreadsheet (${response.status})`);
    const rows = parseCSV(await response.text());
    if (!rows.length) return [];
    const headers = rows[0].map(key);
    return rows.slice(1).map((cols) => {
      const item = {};
      headers.forEach((h, i) => { if (h) item[h] = String(cols[i] || '').trim(); });
      return item;
    }).filter((item) => Object.values(item).some((v) => String(v).trim()));
  };

  const year = (item) => Number(item.year || String(item.date || item.pub_date || '').slice(0,4) || 0);

  const selected = (item) => !item.selected || truthy(item.selected);

  return { load, key, truthy, escapeHTML, safeUrl, link, year, selected };
})();