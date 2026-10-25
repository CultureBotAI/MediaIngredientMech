"""Unified X-Mech website features: references, source and feedback routes,
verified sibling routes, URL state, licences, bulk download, skip links and the
not-found page.

Page assertions are scoped to the section or footer under test: a page-wide
"link X appears" also passes when the same link happens to sit elsewhere.
"""

from __future__ import annotations

import gzip
import hashlib
import html as html_lib
import importlib.util
import json
import re
import shutil
import subprocess
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import parse_qs, quote, urlsplit

import pytest
import yaml

from mediaingredientmech import records_export
from mediaingredientmech import render_ingredient_pages as render
from mediaingredientmech.schema_site import write_schema_site

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
LICENCE = str(render.LICENCE_HTML)

# The fleet's sibling search routes, each verified live on 2026-10-25 to load
# with HTTP 200 and restore ?q= into its search box. A specific-record route
# is listed only where it was verified: TaxonMech taxa, and CultureMech
# normalized recipes (every id the corpus links returned HTTP 200).
VERIFIED_SIBLING_ROUTES = (
    "https://culturebotai.github.io/CultureMech/app/browser.html?q=",
    "https://culturebotai.github.io/CommunityMech/browser.html?q=",
    "https://culturebotai.github.io/TraitMech/pages/browse.html?q=",
    "https://culturebotai.github.io/proteintraitsmech/browse.html?q=",
    "https://culturebotai.github.io/AntibioticMech/pages/browse.html?q=",
    "https://culturebotai.github.io/CellStructureMech/pages/browse.html?q=",
    "https://culturebotai.github.io/HabitatMech/pages/browse.html?q=",
    "https://culturebotai.github.io/NaturalProductMech/pages/browse.html?q=",
    "https://culturebotai.github.io/TaxonMech/pages/browse.html?q=",
    "https://culturebotai.github.io/TaxonMech/pages/taxon.html?id=NCBITaxon:",
    "https://culturebotai.github.io/PathwayMech/pages/browse.html?q=",
    "https://culturebotai.github.io/DUFMech/index.html?q=",
    "https://culturebotai.github.io/CMMMech/pages/browse.html?q=",
    "https://culturebotai.github.io/AIMech/pages/browse.html?q=",
    "https://culturebotai.github.io/CultureMech/pages/normalized/",
)
# Sibling landing pages linked from the site footer (HTTP 200, 2026-10-25).
SIBLING_SITE_ROOTS = {
    "https://culturebotai.github.io/mechs/",
    "https://culturebotai.github.io/CultureMech/",
    "https://culturebotai.github.io/CommunityMech/",
    "https://culturebotai.github.io/TraitMech/",
    "https://culturebotai.github.io/proteintraitsmech/",
}

REFERENCED_RECORD = {
    "identifier": "CHEBI:26710",
    "preferred_term": "Fixture salt",
    "mapping_status": "MAPPED",
    "kg_microbe_node_id": "CHEBI:26710",
    "ontology_mapping": {
        "ontology_id": "CHEBI:26710",
        "ontology_label": "sodium chloride",
        "ontology_source": "CHEBI",
        "mapping_quality": "EXACT_MATCH",
        "evidence": [
            {
                "evidence_type": "DATABASE_MATCH",
                "source": "https://example.org/evidence-source ; DOI:10.5109/24265",
                "snippet": "quoted from https://example.org/snippet",
                "explanation": "see https://example.org/explanation",
                "notes": "Cross-reference: CultureMech:002706",
            }
        ],
    },
    "curation_history": [
        {
            "timestamp": "2026-01-01T00:00:00Z",
            "curator": "fixture",
            "action": "ANNOTATED",
            "changes": "Added https://example.org/history-note",
            "llm_assisted": False,
        }
    ],
    "chemical_properties": {
        "data_source": "https://example.org/datasheet.pdf",
        "cas_rn": "7647-14-5",
    },
    "components": [
        {"component_name": "water", "component_id": "CHEBI:15377", "reference_scope": "EXTERNAL_TERM"}
    ],
    "component_assertion": {
        "method": "LABEL_ENUMERATION",
        "completeness": "COMPLETE",
        "notes": "per https://example.org/assertion-note",
        "evidence": [
            {
                "evidence_type": "SOURCE_LABEL",
                "source": "bergey",
                "source_record": "Bergey doi:10.1002/9781118960608.gbm00618",
            }
        ],
    },
    "synonyms": [
        {
            "synonym_text": "table salt",
            "synonym_type": "EXACT_SYNONYM",
            "source": "https://www.ebi.ac.uk/chebi/CHEBI:37585",
        },
        {
            "synonym_text": "salt pork",
            "synonym_type": "REJECTED_LABEL",
            "source": "https://example.org/rejected-source",
        },
    ],
    "discussions": [
        {
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "prompt": "Is https://example.org/prompt right?",
            "rationale": "PMID:41373036 reports it",
            "evidence": [
                {
                    "reference": "doi:10.1000/discussion",
                    "snippet": "from https://example.org/discussion-snippet",
                    "explanation": "and https://example.org/discussion-explanation",
                }
            ],
            "resolution_note": "https://example.org/resolution",
        }
    ],
    "datasets": [
        {"title": "Fixture dataset", "description": "Described at https://example.org/dataset"}
    ],
}


def write_record(repo: Path, data: dict, name: str = "Fixture.yaml", status: str = "mapped") -> Path:
    source = repo / "data" / "ingredients" / status / name
    source.parent.mkdir(parents=True, exist_ok=True)
    source.write_text(yaml.safe_dump(data, sort_keys=False), encoding="utf-8")
    return source


def render_record(tmp_path, monkeypatch, data, name="Fixture.yaml", status="mapped") -> str:
    monkeypatch.setattr(render, "REPO_ROOT", tmp_path)
    source = write_record(tmp_path, data, name, status)
    out = tmp_path / "records" / "ingredient"
    result, _, slug = render.render_one(render.make_env(), source, out, force=True)
    assert result == "rendered"
    return (out / f"{slug}.html").read_text(encoding="utf-8")


def section(html: str, section_id: str) -> str:
    start = html.index(f'<section id="{section_id}">')
    return html[start : html.index("</section>", start)]


def footer(html: str) -> str:
    match = re.search(r"<footer[^>]*>(.*?)</footer>", html, re.DOTALL)
    assert match, "page has no footer"
    return match.group(1)


def hrefs(fragment: str) -> list[str]:
    return [html_lib.unescape(h) for h in re.findall(r'href="([^"]*)"', fragment)]


def visible_text(fragment: str) -> str:
    return html_lib.unescape(re.sub(r"<[^>]+>", "", fragment))


# ---------- evidence ----------


@pytest.mark.parametrize(
    ("text", "target"),
    [
        (
            "(database.csv row 8022; Bergey doi:10.1002/9781118960608.gbm00644)",
            "https://doi.org/10.1002/9781118960608.gbm00644",
        ),
        ("Love et al. 1979 (doi:10.1099/00207713-29-3-241).", "https://doi.org/10.1099/00207713-29-3-241"),
        ("see (https://pmc.ncbi.nlm.nih.gov/articles/PMC145376/)", "https://pmc.ncbi.nlm.nih.gov/articles/PMC145376/"),
        ("[https://example.org/a]", "https://example.org/a"),
        ('"https://example.org/q".', "https://example.org/q"),
        ("https://en.wikipedia.org/wiki/Agar_(gel)", "https://en.wikipedia.org/wiki/Agar_(gel)"),
        ("(https://en.wikipedia.org/wiki/Agar_(gel))", "https://en.wikipedia.org/wiki/Agar_(gel)"),
    ],
)
def test_reference_links_stop_before_enclosing_brackets_and_punctuation(text, target):
    linked = str(render.linked_text(text))
    assert hrefs(linked) == [target]
    assert visible_text(linked) == text


def test_a_pmid_slot_links_its_bare_number_to_pubmed():
    linked = str(
        render.structured_value(
            {"doi": "10.1128/AAC.01623-08", "pmid": "27565613", "page_count": "27565613"}
        )
    )
    assert hrefs(linked) == [
        "https://doi.org/10.1128/AAC.01623-08",
        "https://pubmed.ncbi.nlm.nih.gov/27565613/",
    ]
    assert visible_text(linked).count("27565613") == 2


def test_free_text_references_link_in_every_record_section(tmp_path, monkeypatch):
    page = render_record(tmp_path, monkeypatch, REFERENCED_RECORD)
    expected = {
        "evidence": [
            "https://example.org/evidence-source",
            "https://doi.org/10.5109/24265",
            "https://example.org/snippet",
            "https://example.org/explanation",
            "https://culturebotai.github.io/CultureMech/pages/normalized/002706.html",
        ],
        "curation_history": ["https://example.org/history-note"],
        "chemical_properties": ["https://example.org/datasheet.pdf"],
        "components": [
            "https://doi.org/10.1002/9781118960608.gbm00618",
            "https://example.org/assertion-note",
        ],
        "synonyms": ["https://www.ebi.ac.uk/chebi/CHEBI:37585"],
        "rejected-labels": ["https://example.org/rejected-source"],
        "discussions": [
            "https://example.org/prompt",
            "https://pubmed.ncbi.nlm.nih.gov/41373036/",
            "https://example.org/discussion-snippet",
            "https://example.org/discussion-explanation",
            "https://example.org/resolution",
        ],
        "datasets": ["https://example.org/dataset"],
    }
    for section_id, targets in expected.items():
        links = hrefs(section(page, section_id))
        for target in targets:
            assert target in links, f"{section_id} does not link {target}"


def test_kg_microbe_node_and_graph_components_link_their_resolver(tmp_path, monkeypatch):
    page = render_record(tmp_path, monkeypatch, REFERENCED_RECORD)
    node = section(page, "overview").split("kg-microbe node", 1)[1]
    assert hrefs(node)[0] == render.curie_to_url("CHEBI:26710")
    graph = section(page, "causal-graph").split("[HAS_COMPONENT]", 1)[1]
    assert hrefs(graph)[0] == render.curie_to_url("CHEBI:15377")


# ---------- source_link / feedback_route ----------


def test_record_footer_links_its_yaml_and_a_prefilled_issue(tmp_path, monkeypatch):
    name = "(-)-Fixture + mix.yaml"
    page = render_record(tmp_path, monkeypatch, {**REFERENCED_RECORD, "preferred_term": "Fixture mix"}, name)
    links = hrefs(footer(page))
    blob = f"{render.GITHUB_REPO}/blob/main/data/ingredients/mapped/%28-%29-Fixture%20%2B%20mix.yaml"
    assert blob in links
    assert blob.replace("/blob/main/", "/raw/main/") in links
    issue = next(link for link in links if "/issues/new?" in link)
    parts = urlsplit(issue)
    assert f"{parts.scheme}://{parts.netloc}{parts.path}" == f"{render.GITHUB_REPO}/issues/new"
    query = parse_qs(parts.query)
    assert query["title"] == ["Record feedback: Fixture mix (MIM:~28-~29-Fixture~20~2B~20mix)"]
    slug = render.slug_for({}, Path("mapped") / name)
    assert f"{render.SITE_ROOT}records/ingredient/{slug}.html" in query["body"][0]
    assert "data/ingredients/mapped/(-)-Fixture + mix.yaml" in query["body"][0]
    assert not any("/edit/" in link for link in links)


# ---------- cross_mech_links ----------


def sibling_links(fragment: str) -> list[str]:
    own = render.SITE_ROOT
    return [
        link
        for link in hrefs(fragment)
        if link.startswith("https://culturebotai.github.io/") and not link.startswith(own)
    ]


def test_record_page_sibling_links_use_verified_routes(tmp_path, monkeypatch):
    record = {
        **REFERENCED_RECORD,
        "culturemech_reference": {"medium_id": "CultureMech:002799", "relationship": "SIMILAR_COMPOSITION"},
    }
    page = render_record(tmp_path, monkeypatch, record)
    links = [link for link in sibling_links(page) if link not in SIBLING_SITE_ROOTS]
    assert links
    for link in links:
        assert link.startswith(VERIFIED_SIBLING_ROUTES), link
    search = hrefs(section(page, "cross-mech-links"))
    assert render.SIBLING_SEARCH["CultureMech"] + quote("Fixture salt") in search


@pytest.mark.parametrize(
    "page",
    [
        "index.html",
        "browser.html",
        "404.html",
        "text_map.html",
        "ingredient_umap.html",
        "ingredient_graph.html",
    ],
)
def test_static_page_sibling_links_are_verified_routes_or_site_roots(page):
    for link in sibling_links((DOCS / page).read_text(encoding="utf-8")):
        assert link in SIBLING_SITE_ROOTS or link.startswith(VERIFIED_SIBLING_ROUTES), link


# ---------- license ----------


def licence_pages(tmp_path, monkeypatch) -> dict[str, str]:
    pages = {name: (DOCS / name).read_text(encoding="utf-8") for name in (
        "index.html",
        "browser.html",
        "404.html",
        "text_map.html",
        "ingredient_umap.html",
        "ingredient_graph.html",
    )}
    pages["template text_map.html"] = (render.TEMPLATES_DIR / "text_map.html").read_text(encoding="utf-8")
    pages["record"] = render_record(tmp_path, monkeypatch, REFERENCED_RECORD)
    render.write_index(tmp_path / "index", [{"ingredient": REFERENCED_RECORD, "slug": "mapped/Fixture"}])
    pages["records index"] = (tmp_path / "index" / "index.html").read_text(encoding="utf-8")
    write_schema_site(ROOT / "src/mediaingredientmech/schema/mediaingredientmech.yaml", tmp_path / "schema")
    pages["schema index"] = (tmp_path / "schema" / "index.html").read_text(encoding="utf-8")
    pages["schema class"] = (tmp_path / "schema" / "classes-IngredientRecord.html").read_text(encoding="utf-8")
    return pages


def test_every_page_type_footer_states_the_repository_licences(tmp_path, monkeypatch):
    for name, page in licence_pages(tmp_path, monkeypatch).items():
        assert LICENCE in footer(page), f"{name} footer lacks the licence line"


def test_footers_leave_room_for_the_fixed_theme_toggle():
    # theme-toggle.js pins a 40px button 18px above the bottom-right corner; at
    # 390px it covered the licence line that now ends record and map pages.
    reserved_px = 40 + 18
    css = (render.TEMPLATES_DIR / "style.css").read_text(encoding="utf-8")
    bottoms = [
        float(value)
        for body in re.findall(r"(?m)^footer \{([^}]*)\}", css)
        for value in re.findall(r"padding-bottom:\s*([\d.]+)rem", body)
    ]
    assert bottoms and bottoms[-1] * 16 >= reserved_px
    for page in (DOCS / "ingredient_umap.html", DOCS / "ingredient_graph.html", render.TEMPLATES_DIR / "text_map.html"):
        block = re.search(r"\.site-footer \{([^}]*)\}", page.read_text(encoding="utf-8")).group(1)
        bottom = re.search(r"padding:\s*[\d.]+rem [\d.]+rem ([\d.]+)rem", block).group(1)
        assert float(bottom) * 16 >= reserved_px, page.name


def test_footer_licences_are_the_ones_the_licence_files_grant():
    scope = " ".join((ROOT / "LICENSE").read_text().split())
    assert "(CC-BY-4.0). See LICENSE-DATA" in scope
    assert "is licensed under BSD-3-Clause. See LICENSE-CODE" in scope
    assert "Third-party data" in scope and "retain their own licenses" in scope
    assert (ROOT / "LICENSE-DATA").read_text().startswith("Attribution 4.0 International")
    assert "Redistribution and use in source and binary forms" in (ROOT / "LICENSE-CODE").read_text()
    assert f'<a href="{render.GITHUB_REPO}/blob/main/LICENSE-DATA">CC BY 4.0</a>' in LICENCE
    assert f'<a href="{render.GITHUB_REPO}/blob/main/LICENSE-CODE">BSD-3-Clause</a>' in LICENCE
    assert f'<a href="{render.GITHUB_REPO}/blob/main/LICENSE">licence scope</a>' in LICENCE


# ---------- downloads ----------


@pytest.fixture
def builder():
    spec = importlib.util.spec_from_file_location("mim_site_builder_unified", ROOT / "scripts/build_pages_site.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@pytest.fixture
def site_repo(tmp_path, builder, monkeypatch):
    repo = tmp_path / "repo"
    (repo / "docs").mkdir(parents=True)
    for name in (
        "index.html",
        "browser.html",
        "theme-toggle.js",
        "map-record-navigation.js",
        "ingredient_umap.html",
        "ingredient_graph.html",
    ):
        shutil.copyfile(DOCS / name, repo / "docs" / name)
    sources = [
        write_record(repo, REFERENCED_RECORD, "Salt.yaml", "mapped"),
        write_record(repo, {"identifier": "UNMAPPED_0001", "preferred_term": "Mud", "mapping_status": "UNMAPPED"},
                     "Mud.yaml", "unmapped"),
        write_record(repo, {"identifier": "CHEBI:15377", "preferred_term": "Water", "mapping_status": "MAPPED"},
                     "(-)-Water.yaml", "mapped"),
    ]
    monkeypatch.setattr(builder.render, "REPO_ROOT", repo)
    return repo, sources


def export_rows(output: Path) -> list[dict]:
    data = (output / "downloads" / records_export.EXPORT_NAME).read_bytes()
    return [json.loads(line) for line in gzip.decompress(data).decode("utf-8").splitlines()]


def test_bulk_download_holds_every_complete_record_in_source_order(site_repo, builder, tmp_path):
    repo, sources = site_repo
    output = tmp_path / "site"
    builder.build_site(repo, output)
    builder.check_site(repo, output)
    manifest = json.loads((output / "downloads/manifest.json").read_text())
    data = (output / "downloads" / records_export.EXPORT_NAME).read_bytes()
    assert manifest["sha256"] == hashlib.sha256(data).hexdigest()
    rows = export_rows(output)
    assert manifest["record_count"] == len(rows) == len(sources)
    assert [row["source_file"] for row in rows] == ["mapped/(-)-Water.yaml", "mapped/Salt.yaml", "unmapped/Mud.yaml"]
    assert [row["record_id"] for row in rows] == ["MIM:~28-~29-Water", "MIM:Salt", "MIM:Mud"]
    for row in rows:
        assert row["record"] == yaml.safe_load((repo / "data/ingredients" / row["source_file"]).read_text())
    receipt = json.loads((output / "records/build.json").read_text())
    assert {"downloads/manifest.json", f"downloads/{records_export.EXPORT_NAME}"} <= set(receipt["assets"])


def test_site_check_refuses_an_export_that_lost_a_record(site_repo, builder, tmp_path):
    repo, sources = site_repo
    output = tmp_path / "site"
    builder.build_site(repo, output)
    export = output / "downloads" / records_export.EXPORT_NAME
    lines = gzip.decompress(export.read_bytes()).decode("utf-8").splitlines()[:-1]
    shortened = gzip.compress(("\n".join(lines) + "\n").encode("utf-8"), mtime=0)
    export.write_bytes(shortened)
    manifest_path = output / "downloads" / records_export.MANIFEST_NAME
    manifest = json.loads(manifest_path.read_text())
    manifest.update(sha256=hashlib.sha256(shortened).hexdigest(), record_count=len(lines))
    manifest_path.write_text(json.dumps(manifest))
    expected = {p.relative_to(repo / "data/ingredients").as_posix() for p in sources}
    with pytest.raises(ValueError, match="every ingredient source exactly once"):
        records_export.check_records_export(output, expected)
    with pytest.raises(ValueError):
        builder.check_site(repo, output)


def test_bulk_download_bytes_do_not_depend_on_build_time(site_repo, tmp_path, monkeypatch):
    repo, sources = site_repo
    ingredient_root = repo / "data" / "ingredients"
    monkeypatch.setattr("time.time", lambda: 1_000_000_000.0)
    records_export.write_records_export(ingredient_root, sources, tmp_path / "first")
    monkeypatch.setattr("time.time", lambda: 2_000_000_000.0)
    records_export.write_records_export(ingredient_root, list(reversed(sources)), tmp_path / "second")
    for name in (records_export.EXPORT_NAME, records_export.MANIFEST_NAME):
        assert (tmp_path / "first/downloads" / name).read_bytes() == (tmp_path / "second/downloads" / name).read_bytes()


def test_landing_downloads_card_links_the_deploy_time_export():
    index = (DOCS / "index.html").read_text(encoding="utf-8")
    card = index.split('id="downloads"', 1)[1].split('<div class="card">', 1)[0]
    assert f"downloads/{records_export.EXPORT_NAME}" in hrefs(card)
    assert "downloads/manifest.json" in hrefs(card)
    assert "when the site is deployed" in " ".join(visible_text(card).split())


# ---------- shareable_state / load_failure (executed in Node) ----------


def inline_script(page: str, marker: str) -> str:
    text = (DOCS / page).read_text(encoding="utf-8")
    return next(s for s in re.findall(r"<script(?:\s[^>]*)?>(.*?)</script>", text, re.DOTALL) if marker in s)


def run_node(tmp_path: Path, harness: str) -> dict:
    node = shutil.which("node")
    if node is None:
        pytest.skip("Node.js is required for the browser runtime regression")
    script = tmp_path / "harness.cjs"
    script.write_text(harness, encoding="utf-8")
    result = subprocess.run([node, str(script)], capture_output=True, text=True)
    assert result.returncode == 0, result.stderr
    return json.loads(result.stdout)


BROWSE_HARNESS = r"""
const vm = require('node:vm');
const source = SOURCE;
const rows = [
  {searchable: 'salt', synonyms: [], mapping_status: 'MAPPED', preferred_term: 'Salt',
   detail_page: 'records/ingredient/mapped/Salt.html', ontology_source: 'CHEBI', mapping_quality: 'EXACT_MATCH'},
  {searchable: 'mud', synonyms: [], mapping_status: 'UNMAPPED', preferred_term: 'Mud',
   detail_page: 'records/ingredient/unmapped/Mud.html', ontology_source: '', mapping_quality: ''},
];
const data = {ingredients: rows, metadata: {total_ingredients: 2, mapped_count: 1, unmapped_count: 1}};
const staticOptions = STATIC_OPTIONS;
function element(id) {
  return {textContent: '', innerHTML: '', value: '',
    options: (staticOptions[id] || ['']).map(value => ({value})), addEventListener() {},
    setAttribute() {}, replaceChildren(...c) { this.options = c; }, add(o) { this.options.push(o); },
    appendChild() {}, focus() {}};
}
async function open(search, hash) {
  const elements = new Map();
  const urls = [];
  const document = {getElementById(id) { if (!elements.has(id)) elements.set(id, element(id)); return elements.get(id); },
    createElement: element, querySelectorAll() { return []; }};
  const context = {document, URLSearchParams, Option: function (text, value) { return {textContent: text, value}; },
    window: {location: {pathname: '/browser.html', search, hash}, addEventListener() {}},
    history: {replaceState(state, title, url) { urls.push(url); }},
    fetch: async () => ({ok: true, status: 200, json: async () => data})};
  vm.createContext(context);
  vm.runInContext(source, context);
  await new Promise(resolve => setImmediate(resolve));
  const value = id => elements.get(id).value;
  return {q: value('search'), status: value('filter-status'), source: value('filter-source'),
    quality: value('filter-quality'), sort: value('sort-by'), url: urls[urls.length - 1],
    shown: elements.get('results-status').textContent};
}
(async () => {
  console.log(JSON.stringify({
    stale_hash: await open('?status=UNMAPPED', '#status=MAPPED'),
    legacy_hash: await open('', '#status=MAPPED'),
    other_hash: await open('?q=salt', '#record=mapped%2FSalt.yaml&status=MAPPED'),
    unknown: await open('?status=NOSUCH&sort=bogus', ''),
    full: await open('?q=salt&status=MAPPED&source=CHEBI&quality=EXACT_MATCH&sort=name-desc', ''),
  }));
})().catch(error => { console.error(error); process.exitCode = 1; });
"""


def static_select_options(page: str) -> dict[str, list[str]]:
    """Option values the page's own markup gives each select before data loads."""
    text = (DOCS / page).read_text(encoding="utf-8")
    return {
        select_id: re.findall(r'<option value="([^"]*)"', body)
        for select_id, body in re.findall(r'<select id="([^"]+)">(.*?)</select>', text, re.DOTALL)
    }


def test_query_string_state_wins_over_a_legacy_status_hash(tmp_path):
    source = inline_script("browser.html", "function applyHashFilters")
    harness = BROWSE_HARNESS.replace("STATIC_OPTIONS", json.dumps(static_select_options("browser.html")))
    state = run_node(tmp_path, harness.replace("SOURCE", json.dumps(source)))
    # The review's reproduction: chose UNMAPPED after arriving from #status=MAPPED.
    assert state["stale_hash"]["status"] == "UNMAPPED"
    assert state["stale_hash"]["url"] == "/browser.html?status=UNMAPPED"
    assert state["stale_hash"]["shown"] == "Showing 1 of 2 ingredients"
    # An old bookmark still opens its subset, and the URL moves to the query string.
    assert state["legacy_hash"]["status"] == "MAPPED"
    assert state["legacy_hash"]["url"] == "/browser.html?status=MAPPED"
    # Only the filter state leaves the hash.
    assert state["other_hash"]["url"] == "/browser.html?q=salt&status=MAPPED#record=mapped%2FSalt.yaml"
    unknown = state["unknown"]
    assert (unknown["status"], unknown["sort"], unknown["url"]) == ("", "", "/browser.html")
    full = state["full"]
    assert (full["q"], full["status"], full["source"], full["quality"], full["sort"]) == (
        "salt", "MAPPED", "CHEBI", "EXACT_MATCH", "name-desc")
    assert full["url"] == "/browser.html?q=salt&status=MAPPED&source=CHEBI&quality=EXACT_MATCH&sort=name-desc"


def test_landing_status_tiles_link_the_query_string_state():
    index = (DOCS / "index.html").read_text(encoding="utf-8")
    stats = index.split('<div class="stats">', 1)[1].split("</div>", 1)[0]
    assert hrefs(stats) == ["browser.html", "browser.html?status=MAPPED", "browser.html?status=MAPPED"]


LANDING_HARNESS = r"""
const vm = require('node:vm');
const source = SOURCE;
function element(tag) {
  return {tag, textContent: '', hidden: true, children: [], className: '', type: '', listeners: {},
    addEventListener(name, fn) { this.listeners[name] = fn; },
    replaceChildren(...c) { this.children = c; }, append(...c) { this.children.push(...c); }};
}
async function run(first) {
  const elements = new Map();
  const responses = [first, {ok: true, status: 200,
    json: async () => ({ingredients: [{mapping_status: 'MAPPED'}, {mapping_status: 'UNMAPPED'}]})}];
  let call = 0;
  const document = {getElementById(id) { if (!elements.has(id)) elements.set(id, element('p')); return elements.get(id); },
    createElement: element};
  const context = {document, fetch: async () => { const r = responses[call++]; if (r instanceof Error) throw r; return r; }};
  vm.createContext(context);
  vm.runInContext(source, context);
  const settle = () => new Promise(resolve => setTimeout(resolve, 20));
  await settle();
  const notice = elements.get('count-status');
  const failed = {hidden: notice.hidden, text: notice.children.filter(c => typeof c === 'string').join(''),
    buttons: notice.children.filter(c => typeof c === 'object').map(c => c.textContent),
    tiles: ['ingredient-count', 'mapped-count', 'coverage-count'].map(id => elements.get(id).textContent)};
  const retry = notice.children.find(c => typeof c === 'object');
  if (retry) { retry.listeners.click(); await settle(); }
  return {failed, retried: {hidden: notice.hidden,
    tiles: ['ingredient-count', 'mapped-count', 'coverage-count'].map(id => elements.get(id).textContent)}};
}
(async () => {
  console.log(JSON.stringify({
    aborted: await run(new TypeError('Failed to fetch')),
    // A parseable error body must not read as an empty catalog of 0 records.
    http: await run({ok: false, status: 503, json: async () => ({message: 'Service Unavailable'})}),
  }));
})().catch(error => { console.error(error); process.exitCode = 1; });
"""


def test_landing_count_failure_is_visible_and_recoverable(tmp_path):
    source = inline_script("index.html", "data/ingredients.json")
    outcome = run_node(tmp_path, LANDING_HARNESS.replace("SOURCE", json.dumps(source)))
    for case in ("aborted", "http"):
        failed, retried = outcome[case]["failed"], outcome[case]["retried"]
        assert failed["hidden"] is False, case
        assert failed["text"].startswith("Counts unavailable"), case
        assert failed["buttons"] == ["Retry"], case
        assert failed["tiles"] == ["—", "—", "—"], case
        assert retried == {"hidden": True, "tiles": ["2", "1", "50%"]}, case


# ---------- curation_notice ----------


def test_record_header_quotes_the_schema_meaning_of_its_status_and_quality(tmp_path, monkeypatch):
    page = render_record(tmp_path, monkeypatch, {**REFERENCED_RECORD, "mapping_status": "REJECTED"})
    header = page.split("<header>", 1)[1].split("</header>", 1)[0]
    enums = yaml.safe_load(render.SCHEMA_PATH.read_text(encoding="utf-8"))["enums"]
    status = enums["MappingStatusEnum"]["permissible_values"]["REJECTED"]["description"]
    quality = enums["MappingQualityEnum"]["permissible_values"]["EXACT_MATCH"]["description"]
    meaning = " ".join(visible_text(header.split('class="status-meaning', 1)[1]).split())
    assert f"REJECTED: {status}" in meaning
    assert f"EXACT_MATCH: {quality}" in meaning


def test_landing_quotes_how_the_readme_says_records_are_made():
    readme = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", (ROOT / "README.md").read_text(encoding="utf-8"))
    readme = " ".join(readme.split())
    about = footer((DOCS / "index.html").read_text(encoding="utf-8")).split('class="about"', 1)[1]
    quotes = re.findall(r"&ldquo;(.*?)&rdquo;", about.split("</p>", 1)[0])
    assert len(quotes) == 2
    for quoted in quotes:
        assert quoted in readme, quoted


# ---------- skip_link / not_found_page ----------


class Focusables(HTMLParser):
    FOCUSABLE = {"a", "button", "input", "select", "textarea", "summary"}

    def __init__(self, page: str) -> None:
        super().__init__()
        self.order: list[tuple[str, dict]] = []
        self.main_ids: list[str] = []
        self.feed(page)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag in self.FOCUSABLE and not (tag == "a" and "href" not in attrs):
            self.order.append((tag, attrs))
        if tag == "main":
            self.main_ids.append(attrs.get("id", ""))


def test_landing_listing_and_record_pages_start_with_a_skip_link(tmp_path, monkeypatch):
    pages = licence_pages(tmp_path, monkeypatch)
    for name in ("index.html", "browser.html", "404.html", "record", "records index", "schema index", "schema class"):
        dom = Focusables(pages[name])
        tag, attrs = dom.order[0]
        assert tag == "a" and "skip-link" in attrs.get("class", "").split(), name
        assert attrs["href"] == "#main-content", name
        assert dom.main_ids == ["main-content"], name


def test_not_found_page_routes_resolve_from_any_depth():
    page = (DOCS / "404.html").read_text(encoding="utf-8")
    refs = re.findall(r'(?:href|src|action)="([^"]*)"', page)
    for ref in refs:
        assert ref.startswith(("https://", "#")), f"relative route {ref!r} 404s below the site root"
    own = [ref for ref in refs if ref.startswith(render.SITE_ROOT)]
    assert f"{render.SITE_ROOT}browser.html" in own and f"{render.SITE_ROOT}theme-toggle.js" in own
    assert len(own) >= 10


# ---------- maps ----------


@pytest.mark.parametrize("page", ["ingredient_umap.html", "ingredient_graph.html"])
def test_map_help_describes_the_record_link_it_has(page):
    help_list = (DOCS / page).read_text(encoding="utf-8").split("How to Interpret This Visualization", 1)[1]
    help_list = help_list.split("</ul>", 1)[0]
    assert "future" not in help_list
    assert "record page" in help_list


def test_published_text_map_is_current_with_its_template(tmp_path):
    rendered = tmp_path / "text_map.html"
    subprocess.run(
        [sys.executable, str(ROOT / "scripts/embed_map.py"), "--render-only", "--html-out", str(rendered)],
        check=True,
        capture_output=True,
    )
    assert rendered.read_text(encoding="utf-8") == (DOCS / "text_map.html").read_text(encoding="utf-8")
