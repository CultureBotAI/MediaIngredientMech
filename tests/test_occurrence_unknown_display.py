"""#1431: run public display code with unknown counts beside true zero.

The producers' explicit state is not mapping approval. These tests exercise the
maintained HTML scripts, not a substitute display implementation.
"""

from __future__ import annotations

import json
import re
import shutil
import subprocess
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]


def inline_script(name: str) -> str:
    scripts = re.findall(
        r"<script(?:\s[^>]*)?>(.*?)</script>",
        (ROOT / name).read_text(),
        re.DOTALL,
    )
    return next(s for s in scripts if "function occurrenceCountText" in s)


def run_js(tmp_path: Path, source: str) -> None:
    node = shutil.which("node")
    assert node is not None, "Node.js is required to check the public count contract"
    program = tmp_path / "unknown-counts.cjs"
    program.write_text(source)
    result = subprocess.run([node, str(program)], capture_output=True, text=True, timeout=20)
    assert result.returncode == 0, result.stdout + result.stderr


DOM = r"""
const assert = require('node:assert/strict');
const vm = require('node:vm');
const escaped = value => String(value ?? '').replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
function element() {
  const el = {innerHTML:'', value:'', options:[{value:''}], style:{}, clientWidth:1000,
    addEventListener() {}, setAttribute() {}, replaceChildren(...items) {this.options=items;},
    appendChild() {}, add(option) {this.options.push(option);}, querySelector() {return element();}};
  let text = '';
  Object.defineProperty(el, 'textContent', {get() {return text;}, set(v) {text=v;el.innerHTML=escaped(v);}});
  return el;
}
const elements = new Map();
const document = {getElementById(id) {if (!elements.has(id)) elements.set(id, element()); return elements.get(id);},
  createElement:element, querySelectorAll() {return [];}, documentElement:{}};
const context = {document, URLSearchParams, console,
  Option: function(text, value) {return {textContent:text, value};},
  window:{location:{hash:'', search:''}, addEventListener() {}},
  fetch:() => new Promise(() => {})};
vm.createContext(context);
"""


def test_browser_renders_unknown_and_keeps_it_after_true_zero(tmp_path):
    program = (
        DOM
        + "\nvm.runInContext("
        + json.dumps(inline_script("docs/browser.html"))
        + ", context);\n"
    )
    program += r"""
const rows = [
  {preferred_term:'A unknown', total_occurrences:null, media_count:null,
   occurrence_statistics_state:'UNKNOWN', occurrence_statistics_reason:'Evidence <held> & incomplete'},
  {preferred_term:'Z zero', total_occurrences:0, media_count:0, occurrence_statistics_state:'RECORDED'},
  {preferred_term:'P positive', total_occurrences:12, media_count:3, occurrence_statistics_state:'RECORDED'},
  {preferred_term:'B missing', occurrence_statistics_state:'MISSING'},
].map((row, i) => ({id:'MIM:000000'+i, searchable:row.preferred_term.toLowerCase(),
  synonyms:[], mapping_status:'MAPPED', detail_page:'records/ingredient/mapped/example.html', ...row}));
context.fixture = rows;
vm.runInContext('allIngredients=fixture; dataReady=true;', context);
for (const sort of ['occurrences-desc','media-desc']) {
  document.getElementById('sort-by').value=sort;
  context.applyFilters();
  assert.equal(vm.runInContext('filteredIngredients.map(r=>r.preferred_term).join("|")', context),
    'P positive|Z zero|A unknown|B missing');
  const html=document.getElementById('ingredient-list').innerHTML;
  assert.ok(html.includes('Occurrences:</span> Unknown'));
  assert.ok(html.includes('Occurrences:</span> 0'));
  assert.ok(html.includes('Occurrences:</span> 12'));
  assert.ok(html.includes('Media Count:</span> Unknown'));
  assert.ok(html.includes('Media usage unknown: Evidence &lt;held&gt; &amp; incomplete'));
  assert.ok(html.includes('Media usage not declared'));
  assert.ok(!html.includes('Evidence <held>'));
}
for (const bad of [null, undefined, false, '', '0', -1, 1.2, NaN, Infinity]) {
  assert.equal(context.occurrenceCountText(bad), 'Unknown');
}
assert.equal(context.occurrenceCountText(0), '0');
"""
    run_js(tmp_path, program)


@pytest.mark.parametrize("page", ["docs/ingredient_umap.html", "docs/ingredient_graph.html"])
def test_plot_sizes_tooltips_and_tables_preserve_unknown(tmp_path, page):
    program = DOM + r"""
const radii=[];const handlers={};let tooltip='';const domains=[];
const selection={append() {return this;}, selectAll() {return this;}, data(rows) {this.rows=rows;return this;},
  join() {return this;}, attr(key,value) {if (key==='r') radii.push(this.rows.map(value));return this;},
  style() {return this;}, text() {return this;}, call() {return this;},
  on(key,value) {handlers[key]=value;return this;}, html(value) {tooltip=value;return this;},
  transition() {return this;}, duration() {return this;}, scaleExtent() {return this;}};
function scale(sqrt=false) {
  let domain=[0,1],range=[0,1];
  const f=x=>range[0]+(sqrt?Math.sqrt(x/domain[1]):x)*(range[1]-range[0]);
  f.domain=d=>{if (d===undefined) return domain;domain=d;if(sqrt) domains.push(d);return f;};
  f.range=r=>{range=r;return f;};return f;
}
context.d3={select:()=>selection, extent:(rows,f)=>[Math.min(...rows.map(f)),Math.max(...rows.map(f))],
  scaleLinear:()=>scale(), scaleSqrt:()=>scale(true), scaleOrdinal:()=>scale(),
  axisBottom:()=>({ticks:()=>selection}),axisLeft:()=>({ticks:()=>selection}),zoom:()=>selection};
context.getComputedStyle=()=>({getPropertyValue:()=>''});
"""
    program += "\nvm.runInContext(" + json.dumps(inline_script(page)) + ", context);\n"
    program += r"""
const rows=[
  {name:'unknown',total_occurrences:null,media_count:null,occurrence_statistics_state:'UNKNOWN',
   occurrence_statistics_reason:'Coverage <not complete>'},
  {name:'zero',total_occurrences:0,media_count:0,occurrence_statistics_state:'RECORDED'},
  {name:'positive',total_occurrences:16,media_count:4,occurrence_statistics_state:'RECORDED'},
].map((r,i)=>({...r,id:'MIM:000000'+i,umap_x:i,umap_y:i,mapping_status:'MAPPED',num_synonyms:1}));
context.fixture=rows;
vm.runInContext('ingredientData=fixture; renderUMAP(); buildTable();',context);
assert.deepEqual(radii[0],[3,5,15]);
assert.deepEqual(Array.from(domains[0]),[0,16]);
const table=elements.get('data-table-el').innerHTML;
assert.ok(table.includes('<td>Unknown</td><td>Unknown</td>'));
assert.ok(table.includes('<td>0</td><td>0</td>'));
assert.ok(table.includes('<td>16</td><td>4</td>'));
handlers.mouseover.call({}, {pageX:0,pageY:0},rows[0]);
assert.ok(tooltip.includes('Occurrences: Unknown'));
assert.ok(tooltip.includes('Media count: Unknown'));
assert.ok(tooltip.includes('Coverage &lt;not complete&gt;'));
assert.ok(!tooltip.includes('Coverage <not complete>'));
handlers.mouseover.call({}, {pageX:0,pageY:0},rows[1]);
assert.ok(tooltip.includes('Occurrences: 0'));
const radiusArgs=[];
assert.equal(context.metricRadius(rows[0],'media_count',v=>{radiusArgs.push(v);return v;}),3);
assert.equal(radiusArgs.length,0);
assert.equal(context.metricRadius(rows[1],'media_count',v=>{radiusArgs.push(v);return v;}),0);
assert.deepEqual(radiusArgs,[0]);
assert.equal(context.metricMaximum([{x:null},{x:undefined},{x:0},{x:'99'},{x:false}],'x'),1);
assert.equal(context.metricMaximum([{x:null},{x:7}],'x'),7);
assert.ok(Number.isFinite(context.metricMaximum([{x:null}],'x')));
"""
    run_js(tmp_path, program)


def test_text_map_tooltip_keeps_null_distinct_from_zero(tmp_path):
    template = (ROOT / "src/mediaingredientmech/templates/text_map.html").read_text()
    line = next(line.strip() for line in template.splitlines() if "Media: ${" in line)
    program = "const assert=require('node:assert/strict');\n"
    program += "const esc = value => String(value ?? '');\n"
    program += "const render = best => `" + line + "`;\n"
    program += "assert.ok(render({media_count:null}).includes('Media: Unknown'));\n"
    program += "assert.ok(render({}).includes('Media: Unknown'));\n"
    program += "assert.ok(render({media_count:0}).includes('Media: 0'));\n"
    program += "assert.ok(render({media_count:7}).includes('Media: 7'));\n"
    run_js(tmp_path, program)
