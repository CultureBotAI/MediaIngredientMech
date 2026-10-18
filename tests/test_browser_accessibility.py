from html.parser import HTMLParser
from pathlib import Path


class Elements(HTMLParser):
    def __init__(self, html):
        super().__init__()
        self.items = []
        self.feed(html)

    def handle_starttag(self, tag, attrs):
        self.items.append((tag, dict(attrs)))

    def find(self, tag=None, **attrs):
        return [
            a
            for t, a in self.items
            if (tag is None or t == tag)
            and all(a.get(k.rstrip("_").replace("_", "-")) == v for k, v in attrs.items())
        ]


ROOT = Path(__file__).resolve().parents[1]
DIRECTORY = "https://culturebotai.github.io/mechs/"


def test_browser_search_and_result_updates_have_accessible_semantics():
    dom = Elements((ROOT / "docs/browser.html").read_text())
    assert dom.find("label", for_="search")
    assert dom.find(role="status", aria_live="polite", aria_atomic="true")
    assert dom.find("button", id="reset-filters", type="button")
    assert dom.find("a", href=DIRECTORY)
    assert Elements((ROOT / "docs/index.html").read_text()).find("a", href=DIRECTORY)


def test_browser_javascript_parses(tmp_path):
    import re
    import shutil
    import subprocess

    import pytest

    node = shutil.which("node")
    if node is None:
        pytest.skip("Node.js is required for the browser JavaScript syntax check")
    html = (ROOT / "docs/browser.html").read_text()
    scripts = re.findall(r"<script(?:\s[^>]*)?>(.*?)</script>", html, re.DOTALL)
    assert scripts
    for number, script in enumerate(scripts):
        source = tmp_path / f"inline-{number}.js"
        source.write_text(script)
        checked = subprocess.run([node, "--check", str(source)], capture_output=True, text=True)
        assert checked.returncode == 0, checked.stderr


def test_loading_errors_remain_distinct_from_empty_catalogs(tmp_path):
    """Execute the maintained loader, including its real catch and filter guards."""
    import json
    import re
    import shutil
    import subprocess

    import pytest

    node = shutil.which("node")
    if node is None:
        pytest.skip("Node.js is required for the browser runtime regression")
    html = (ROOT / "docs/browser.html").read_text()
    script = next(
        s
        for s in re.findall(r"<script(?:\s[^>]*)?>(.*?)</script>", html, re.DOTALL)
        if "function loadIngredients" in s
    )
    harness = r"""
const vm = require('node:vm');
const source = SOURCE;
const empty = {ingredients: [], metadata: {total_ingredients: 0, mapped_count: 0, unmapped_count: 0}};
const valid = {ingredients: [{searchable:'salt', synonyms:[], mapping_status:'MAPPED',
  preferred_term:'Salt', detail_page:'records/ingredient/mapped/Salt.html'}],
  metadata:{total_ingredients:1,mapped_count:1,unmapped_count:0}};
const cases = [
  ['record', 200, valid, false],
  ['unsafe-url', 200, {...valid, ingredients:[{...valid.ingredients[0], detail_page:'javascript:alert(1)'}]}, true],
  ['missing-url', 200, {...valid, ingredients:[{...valid.ingredients[0], detail_page:undefined}]}, true],
  ['empty', 200, empty, false],
  ['http', 500, empty, true],
  ['shape', 200, {}, true],
  ['counts-missing', 200, {ingredients: [], metadata: {}}, true],
  ['counts-negative', 200, {...empty, metadata: {...empty.metadata, mapped_count: -1}}, true],
  ['counts-mismatch', 200, {...empty, metadata: {...empty.metadata, total_ingredients: 1}}, true],
];
function element() { return {textContent: '', innerHTML: '', value: '', options: [{value:''}],
  addEventListener() {}, setAttribute() {}, replaceChildren(...children) { this.options = children; }, add(option) { this.options.push(option); }, appendChild() {}}; }
(async () => {
  for (const [name, status, data, failed] of cases) {
    const elements = new Map();
    const document = {getElementById(id) {if (!elements.has(id)) elements.set(id, element()); return elements.get(id);},
      createElement: element, querySelectorAll() {return []}};
    const context = {document, URLSearchParams, Option: function(text, value) { return {textContent:text, value}; }, window: {location: {hash:''}, addEventListener() {}},
      fetch: async () => ({ok: status === 200, status, json: async () => data})};
    vm.createContext(context); vm.runInContext(source, context);
    await new Promise(resolve => setImmediate(resolve));
    const statusText = elements.get('results-status').textContent;
    if (failed) {
      if (!statusText.includes('could not be loaded')) throw Error(name + ': not reported as failed');
      for (const id of ['total-count','mapped-count','unmapped-count','filtered-count']) {
        if (elements.get(id).textContent !== 'Unavailable') throw Error(name + ': misleading ' + id);
      }
      context.applyFilters();
      if (elements.get('results-status').textContent !== statusText) throw Error(name + ': filtering hid failure');
    } else if (statusText !== `Showing ${data.ingredients.length} of ${data.ingredients.length} ingredients`) throw Error(name + ': legitimate empty data rejected');
  }
})().catch(error => {console.error(error); process.exitCode=1});
""".replace("SOURCE", json.dumps(script))
    runtime = tmp_path / "loader-contract.cjs"
    runtime.write_text(harness)
    checked = subprocess.run([node, str(runtime)], capture_output=True, text=True)
    assert checked.returncode == 0, checked.stderr
