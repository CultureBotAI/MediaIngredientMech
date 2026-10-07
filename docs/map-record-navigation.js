/* Exact stable-record lookup; shared ontology identities and labels are not keys. */
(() => {
  'use strict';
  let catalog;
  let selected = 0;
  const panel = document.createElement('section');
  panel.id = 'selected-record';
  panel.setAttribute('aria-live', 'polite');
  panel.style.cssText = 'margin:1rem;padding:1rem;border:1px solid currentColor';
  panel.textContent = 'Select a point to inspect its ingredient record. Points also support Enter or Space.';
  const header = document.querySelector('header');
  (header || document.body.firstElementChild).after(panel);
  async function records() {
    if (!catalog) catalog = fetch('data/ingredients.json').then(response => {
      if (!response.ok) throw new Error('Catalog unavailable');
      return response.json();
    }).then(data => {
      if (!Array.isArray(data.ingredients)) throw new Error('Invalid catalog');
      const byId = new Map();
      for (const row of data.ingredients) {
        if (!row.record_id || !/^records\/ingredient\/(mapped|unmapped)\/[A-Za-z0-9._-]+\.html$/.test(row.detail_page || '')) continue;
        byId.set(row.record_id, byId.has(row.record_id) ? null : row);
      }
      return byId;
    }).catch(error => { catalog = null; throw error; });
    return catalog;
  }
  async function select(point) {
    const generation = ++selected;
    panel.textContent = `Loading record for ${point.name || point.id}…`;
    try {
      const row = (await records()).get(point.id);
      if (generation !== selected) return;
      panel.replaceChildren();
      const title = document.createElement('h2'); title.textContent = point.name || point.id; panel.append(title);
      if (row) {
        const link = document.createElement('a'); link.href = row.detail_page;
        link.textContent = `Open ingredient record: ${row.preferred_term} (${row.record_id})`; panel.append(link);
      } else {
        panel.append('This historic point has no unique current record match. ');
        const link = document.createElement('a'); link.href = 'browser.html'; link.textContent = 'Browse current ingredients'; panel.append(link);
      }
    } catch (_) {
      if (generation !== selected) return;
      panel.textContent = 'The ingredient catalog could not be loaded. ';
      const retry = document.createElement('button'); retry.textContent = 'Retry record lookup';
      retry.addEventListener('click', () => select(point)); panel.append(retry);
    }
  }
  window.MimRecords = {select};
})();
