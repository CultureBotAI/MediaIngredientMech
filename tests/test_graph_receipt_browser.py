"""Exercise the actual browser provenance consumer without a browser network."""

import shutil
import subprocess
from pathlib import Path

import pytest


@pytest.mark.skipif(
    shutil.which("node") is None, reason="Node is required for browser JavaScript tests"
)
def test_browser_checks_actual_bytes_coverage_lookup_and_legacy_labels():
    helper = Path(__file__).resolve().parents[1] / "docs/graph-receipt.js"
    program = r"""
const assert = require('node:assert/strict');
const crypto = require('node:crypto');
const graph = require(process.argv[1]);
const rows = [1,2].map(i=>({id:`MIM:${i}`,umap_x:i,umap_y:-i,
    embedding_method:'direct_identifier',embedding_source_node:`CHEBI:${i}`}));
const bytes = Buffer.from(JSON.stringify(rows));
const receipt = {schema_version:2,embedding_family:'kg_microbe_deepwalk',
    source:{lineage:'parsed-source-bytes',filename:'actual.tsv.gz',sha256:'a'.repeat(64)},
    outputs:{'map.json':crypto.createHash('sha256').update(bytes).digest('hex')},
    coverage:{eligible:3,projected:2},matrix:{row_ids:['MIM:1','MIM:2']},projection:{method:'pacmap'},
    matching:{rows:[...rows.map(row=>({identifier:row.id,status:'projected',
        match_method:row.embedding_method,source_nodes:[row.embedding_source_node]})),
        {identifier:'MIM:missing',status:'missing_vector',source_nodes:[]}]}};
(async()=>{
    const result=await graph.verify(bytes,receipt,'map.json');
    assert.equal(result.verified,true);assert.match(result.description,/2 of 3/);
    assert.match(result.description,/actual.tsv.gz/);assert.match(result.title,/PaCMAP/);
    const legacy=await graph.verify(bytes,null,'map.json');
    assert.equal(legacy.verified,false);assert.match(legacy.description,/unverified/);
    assert.doesNotMatch(legacy.title,/PaCMAP|sfdp|UMAP/);
    await assert.rejects(graph.verify(Buffer.concat([bytes,Buffer.from(' ')]),receipt,'map.json'),/checksum/);
    const wrongRows=structuredClone(receipt);wrongRows.matrix.row_ids.reverse();
    await assert.rejects(graph.verify(bytes,wrongRows,'map.json'),/identities/);
    const wrongMatch=structuredClone(receipt);wrongMatch.matching.rows[0].source_nodes=['CHEBI:wrong'];
    await assert.rejects(graph.verify(bytes,wrongMatch,'map.json'),/lookup ledger/);
    const wrongMethod=structuredClone(receipt);wrongMethod.projection.method='invented';
    await assert.rejects(graph.verify(bytes,wrongMethod,'map.json'),/coverage/);
    global.fetch=async url=>url.endsWith('metadata.json')?{ok:false,status:500}:{ok:true,arrayBuffer:async()=>bytes};
    await assert.rejects(graph.load('data/map.json','data/map.metadata.json'),/500/);
    global.fetch=async url=>url.endsWith('metadata.json')?{ok:false,status:404}:{ok:true,arrayBuffer:async()=>bytes};
    assert.equal((await graph.load('data/map.json','data/map.metadata.json')).verified,false);
    global.fetch=async url=>url.endsWith('metadata.json')?{ok:true,status:200,json:async()=>receipt}:{ok:true,arrayBuffer:async()=>bytes};
    assert.equal((await graph.load('data/map.json','data/map.metadata.json')).verified,true);
})().catch(error=>{console.error(error);process.exitCode=1});
"""
    result = subprocess.run(
        [shutil.which("node"), "-e", program, str(helper)], capture_output=True, text=True
    )
    assert result.returncode == 0, result.stdout + result.stderr


@pytest.mark.skipif(
    shutil.which("node") is None, reason="Node is required for browser JavaScript tests"
)
@pytest.mark.parametrize("page", ["ingredient_umap.html", "ingredient_graph.html"])
def test_actual_page_explanation_and_hover_preserve_verified_vs_legacy(page):
    docs = Path(__file__).resolve().parents[1] / "docs"
    program = r"""
const assert = require('node:assert/strict');
const fs = require('node:fs');
const graph = require(process.argv[1]);
const page = fs.readFileSync(process.argv[2], 'utf8');
const ready = page.match(/\.then\(result => \{([\s\S]*?)\n            \}\)/)[1];
const hover = page.match(/\.on\('mouseover', function\(event, d\) \{([\s\S]*?)\n                \}\)\n                \.on\('mouseout'/)[1];
const row = {id:'MIM:1',name:'Example',mapping_status:'UNMAPPED',
    embedding_method:'synonym',embedding_source_node:'CHEBI:<node>'};
for (const verified of [true, false]) {
    const nodes = new Map();
    const document = {createElement:()=>({}), getElementById:id=>{
        if(!nodes.has(id))nodes.set(id,{textContent:'',appendChild:()=>{}});
        return nodes.get(id);
    }};
    global.document = document;
    const result = {data:[row], verified, title:'Title', description:'Description', receiptUrl:'receipt.json'};
    const runReady = new Function('IngredientGraphReceipt','document','result',
        'let ingredientData, graphGeneration; const renderUMAP=()=>{},buildFacets=()=>{},buildTable=()=>{},applyFilters=()=>{};' +
        ready + ';return {ingredientData, graphGeneration};');
    const state = runReady(graph,document,result);
    assert.equal(state.graphGeneration,result);
    assert.equal(state.ingredientData,result.data);
    const explanation = nodes.get('graph-coverage-explanation').textContent;
    if(verified)assert.match(explanation,/without vectors are omitted/);
    else assert.match(explanation,/legacy coordinates have unverified matching and coverage/);
    assert.doesNotMatch(explanation,/synthetic|cluster center/);
    let html='',text='',appendCount=0;
    const tooltip={style:()=>tooltip,html:value=>{html=value;return tooltip},
        append:()=>{appendCount++;return tooltip},attr:()=>tooltip,text:value=>{text=value;return tooltip}};
    const d3={select:()=>({attr:function(){return this}})};
    const runHover = new Function('d3','tooltip','HILITE','IngredientGraphReceipt','graphGeneration','event','d',hover);
    runHover(d3,tooltip,'black',graph,state.graphGeneration,{pageX:0,pageY:0},row);
    assert.equal(appendCount,1);
    assert.doesNotMatch(html,/synthetic|CHEBI:<node>/);
    if(verified)assert.equal(text,'Graph match: synonym; source node: CHEBI:<node>.');
    else {assert.match(text,/unverified/);assert.doesNotMatch(text,/synonym|CHEBI:/);}
}
"""
    result = subprocess.run(
        [shutil.which("node"), "-e", program, str(docs / "graph-receipt.js"), str(docs / page)],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, result.stdout + result.stderr
