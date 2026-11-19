/* Match text-map points to the current ingredient catalog: record links and coverage. */
(() => {
  'use strict';
  // Pages are named by render_ingredient_pages.slug_for(). The committed map's
  // points kept the page names embed_records.py used, which dropped the "_" that
  // a leading or trailing parenthesis becomes, and curation moves records between
  // mapped/ and unmapped/. A point is matched to a record by its page's file name
  // under either rule; a name two records share matches neither.
  const slug = stem => stem.replace(/[^A-Za-z0-9._-]+/g, '_');
  const legacySlug = stem => slug(stem).replace(/^_+|_+$/g, '') || 'ingredient';
  const pageName = url => String(url || '').split('/').pop().replace(/\.html$/, '');

  function linkPoints(points, rows) {
    const pages = new Set(rows.map(row => row.detail_page));
    const byName = new Map();
    const add = (name, page) => byName.set(name, byName.has(name) && byName.get(name) !== page ? null : page);
    for (const row of rows) {
      const stem = String(row.source_file || '').split('/').pop().replace(/\.yaml$/, '');
      add(slug(stem), row.detail_page);
      add(legacySlug(stem), row.detail_page);
    }
    for (const point of points) {
      point.page = pages.has(point.url) ? point.url : (byName.get(pageName(point.url)) || '');
    }
  }

  // REJECTED records are left out of the embedding by design (embed_records.py);
  // any other record missing from the map did not exist when it was computed.
  function coverage(points, rows) {
    const plotted = new Set(points.map(point => point.page).filter(Boolean));
    const missing = rows.filter(row => !plotted.has(row.detail_page));
    return {
      plotted: rows.length - missing.length,
      total: rows.length,
      rejected: missing.filter(row => row.mapping_status === 'REJECTED'),
      later: missing.filter(row => row.mapping_status !== 'REJECTED'),
      unpublished: points.filter(point => !point.page).length,
    };
  }

  window.TextMapRecords = { linkPoints, coverage };
})();
