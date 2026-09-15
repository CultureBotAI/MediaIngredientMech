"""Execute the browser's actual hash and filter code against duplicate ontology IDs."""
import json
import shutil
import subprocess
from pathlib import Path

import pytest


def test_exact_record_link_is_decoded_and_clear_preserves_filters():
    node = shutil.which("node")
    if node is None:
        pytest.skip("Node is required to execute browser JavaScript")
    root = Path(__file__).resolve().parents[1]
    browser = (root / "docs/browser.html").read_text()
    # Execute the real initialization and filter functions. Rendering/network
    # are replaced by stubs; selection logic itself is never reimplemented.
    start = browser.index('        let selectedRecord = "";')
    stop = browser.index('        // Load data', start)
    filters_start = browser.index('        function applyFilters()')
    filters_stop = browser.index('        // Render ingredients', filters_start)
    script = r"""
const vm = require('node:vm');
const assert = require('node:assert/strict');
const handlers = {};
const controls = Object.fromEntries(['search', 'filter-status', 'filter-source', 'filter-quality',
    'filtered-count', 'record-selection-notice', 'clear-record-selection'].map(id => [id, {
        value: '', hidden: true, textContent: '',
        options: [{value: ''}, {value: 'MAPPED'}, {value: 'UNMAPPED'}],
        addEventListener: (event, handler) => { handlers[id + ':' + event] = handler; }
    }]));
const context = vm.createContext({URLSearchParams, document: {getElementById: id => controls[id]},
    window: {location: {hash: '#record=mapped%2Fsalt%2Bhydrate.yaml&status=MAPPED',
        pathname: '/browser.html', search: ''}, addEventListener: () => {}},
    history: {replaceState: (a, b, path) => { context.savedPath = path; }},
    renderIngredients: () => {}});
vm.runInContext(HELPER, context);
vm.runInContext(BOOTSTRAP + FILTERS, context);
vm.runInContext(`allIngredients = [
 {id:'CHEBI:1', source_file:'mapped/salt+hydrate.yaml', searchable:'salt', mapping_status:'MAPPED'},
 {id:'CHEBI:1', source_file:'mapped/salt.yaml', searchable:'salt', mapping_status:'MAPPED'},
 {id:'UNMAPPED_1', source_file:'unmapped/unknown.yaml', searchable:'unknown', mapping_status:'UNMAPPED'}
]; applyFilters();`, context);
assert.equal(vm.runInContext('filteredIngredients.length', context), 1);
assert.equal(vm.runInContext('filteredIngredients[0].source_file', context), 'mapped/salt+hydrate.yaml');
assert.equal(controls['record-selection-notice'].hidden, false);
controls['filter-status'].value = 'UNMAPPED';
handlers['clear-record-selection:click']();
assert.equal(controls['filter-status'].value, 'UNMAPPED');
assert.equal(controls['record-selection-notice'].hidden, true);
assert.equal(vm.runInContext('filteredIngredients[0].source_file', context), 'unmapped/unknown.yaml');
assert.equal(context.savedPath, '/browser.html#status=MAPPED');
"""
    definitions = "\n".join([
        "const HELPER = " + json.dumps((root / "docs/record-selection.js").read_text()) + ";",
        "const BOOTSTRAP = " + json.dumps(browser[start:stop]) + ";",
        "const FILTERS = " + json.dumps(browser[filters_start:filters_stop]) + ";",
    ])
    subprocess.run([node, "-e", definitions + script], check=True, capture_output=True, text=True)
