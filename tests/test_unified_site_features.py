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
            "discussion_id": "gap-1",
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


@pytest.mark.parametrize(
    ("text", "targets"),
    [
        # Curation notes are written in Markdown; its marks are not part of a target.
        (
            "[10.1038/x](https://doi.org/10.1038/x)",
            ["https://doi.org/10.1038/x", "https://doi.org/10.1038/x"],
        ),
        ("**10.1099/y**", ["https://doi.org/10.1099/y"]),
        ("`10.1146/z`", ["https://doi.org/10.1146/z"]),
        ("see `https://example.org/c`.", ["https://example.org/c"]),
        ('cited as "https://example.org/q"(quoted)', ["https://example.org/q"]),
        ("**Recommended:** doi:10.1000/abc: `UNMAPPED`", ["https://doi.org/10.1000/abc"]),
    ],
)
def test_markdown_marks_stay_out_of_reference_links(text, targets):
    linked = str(render.linked_text(text))
    assert hrefs(linked) == targets
    assert visible_text(linked) == text


@pytest.mark.parametrize(
    ("text", "targets"),
    [
        # A closer with no opener inside the token ends it, and the scan
        # resumes there, so the second reference is linked on its own.
        ("(https://a.example/x)-(https://b.example/y)", ["https://a.example/x", "https://b.example/y"]),
        ("(doi:10.1000/a)/(doi:10.1000/b)", ["https://doi.org/10.1000/a", "https://doi.org/10.1000/b"]),
        # Balanced parentheses or brackets inside one URL belong to it.
        ("https://en.wikipedia.org/wiki/Foo_(bar)", ["https://en.wikipedia.org/wiki/Foo_(bar)"]),
        ("see https://example.org/q?a[0]=1.", ["https://example.org/q?a[0]=1"]),
    ],
)
def test_references_end_at_an_unopened_closer_and_the_next_one_is_found(text, targets):
    linked = str(render.linked_text(text))
    assert hrefs(linked) == targets
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
    assert blob.replace("/blob/main/", "/edit/main/") in links
    issue = next(link for link in links if "/issues/new?" in link)
    parts = urlsplit(issue)
    assert f"{parts.scheme}://{parts.netloc}{parts.path}" == f"{render.GITHUB_REPO}/issues/new"
    # The fleet template: title "Problem with <record id>", body the page URL.
    query = parse_qs(parts.query)
    assert query["title"] == ["Problem with MIM:~28-~29-Fixture~20~2B~20mix"]
    slug = render.slug_for({}, Path("mapped") / name)
    assert query["body"] == [f"{render.SITE_ROOT}records/ingredient/{slug}.html"]


def breadcrumb(page: str) -> str:
    match = re.search(r'<nav class="breadcrumb" aria-label="Breadcrumb">(.*?)</nav>', page, re.DOTALL)
    assert match, "record page has no breadcrumb trail"
    return match.group(1)


def test_record_breadcrumb_trails_home_listing_status_and_record(tmp_path, monkeypatch):
    page = render_record(tmp_path, monkeypatch, {**REFERENCED_RECORD, "mapping_status": "REJECTED"})
    trail = breadcrumb(page)
    items = re.findall(r"<li>(.*?)</li>", trail, re.DOTALL)
    assert [visible_text(item).strip() for item in items] == ["Home", "Ingredients", "REJECTED", "Fixture salt"]
    # Every crumb but the current page links, relative to records/ingredient/<status>/.
    assert [hrefs(item) for item in items] == [
        ["../../../index.html"],
        ["../../../browser.html"],
        ["../../../browser.html?status=REJECTED"],
        [],
    ]
    assert 'aria-current="page"' in items[-1]
    # The site menu stays, as its own navigation.
    assert '<nav class="site-nav" aria-label="Site navigation">' in page


def status_explanation(page: str) -> str:
    disclosure = page.split('class="status-meaning', 1)[1].split("</details>", 1)[0]
    return " ".join(visible_text(disclosure).split())


# Literal values, not HUMAN_REVIEW_QUALITIES itself: emptying the set must fail, not skip.
@pytest.mark.parametrize("quality", ["LLM_ASSISTED", "MANUAL_CURATION"])
def test_status_explanation_never_claims_human_review(tmp_path, monkeypatch, quality):
    assert quality in render.HUMAN_REVIEW_QUALITIES
    record = {
        **REFERENCED_RECORD,
        "ontology_mapping": {**REFERENCED_RECORD["ontology_mapping"], "mapping_quality": quality},
    }
    text = status_explanation(render_record(tmp_path, monkeypatch, record))
    claim = render.enum_meanings()["MappingQualityEnum"][quality]
    # The badge is explained: the schema's words, attributed to it, with the caveat.
    assert claim and f"{quality}: the schema describes this value as “{claim}”. This page cannot confirm that" in text
    assert f"{quality}: {claim}" not in text
    # Outside that quotation, nothing speaks of a human or expert review.
    assert re.search(r"\b(human|expert)", text.replace(f"“{claim}”", ""), re.IGNORECASE) is None


def test_status_explanation_names_the_records_own_curators(tmp_path, monkeypatch):
    history = [
        {"timestamp": "2026-01-01T00:00:00Z", "curator": "manual", "action": "CREATED", "llm_assisted": False},
        {"timestamp": "2026-01-02T00:00:00Z", "curator": "claude", "action": "MAPPED", "llm_assisted": True},
        {"timestamp": "2026-01-03T00:00:00Z", "curator": "manual", "action": "ANNOTATED", "llm_assisted": False},
    ]
    text = status_explanation(render_record(tmp_path, monkeypatch, {**REFERENCED_RECORD, "curation_history": history}))
    assert "lists 3 events by 2 curators (manual, claude); 1 is marked LLM-assisted" in text


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


def test_bulk_download_writes_unquoted_yaml_dates_as_iso_8601(tmp_path):
    root = tmp_path / "ingredients"
    (root / "mapped").mkdir(parents=True)
    dated = root / "mapped" / "Dated.yaml"
    dated.write_text(
        "identifier: CHEBI:1\npreferred_term: Dated\nmapping_status: MAPPED\n"
        "curation_history:\n- timestamp: 2026-01-02T03:04:05Z\n  curator: fixture\n  action: CREATED\n"
        "chemical_properties:\n  retrieval_date: 2026-01-02\n"
    )
    payload = records_export.export_lines(root, [dated])
    record = json.loads(payload)["record"]
    assert record["curation_history"][0]["timestamp"] == "2026-01-02T03:04:05+00:00"
    assert record["chemical_properties"]["retrieval_date"] == "2026-01-02"
    assert records_export.export_lines(root, [dated]) == payload
    # Any other value with no JSON form still fails the build instead of being stringified.
    odd = root / "mapped" / "Odd.yaml"
    odd.write_text("identifier: CHEBI:2\nvalues: !!set {a: null}\n")
    with pytest.raises(TypeError, match="set has no JSON form"):
        records_export.export_lines(root, [odd])


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
    disclosure = header.split('class="status-meaning', 1)[1].split("</details>", 1)[0]
    assert "<summary>What this status means</summary>" in disclosure
    meaning = " ".join(visible_text(disclosure).split())
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


def test_landing_listing_record_and_map_pages_start_with_a_skip_link(tmp_path, monkeypatch):
    pages = licence_pages(tmp_path, monkeypatch)
    for name in (
        "index.html",
        "browser.html",
        "404.html",
        "text_map.html",
        "ingredient_umap.html",
        "ingredient_graph.html",
        "record",
        "records index",
        "schema index",
        "schema class",
    ):
        dom = Focusables(pages[name])
        tag, attrs = dom.order[0]
        assert tag == "a" and "skip-link" in attrs.get("class", "").split(), name
        assert attrs["href"] == "#main-content", name
        assert dom.main_ids == ["main-content"], name


@pytest.mark.parametrize(
    "page", ["index.html", "browser.html", "text_map.html", "ingredient_umap.html", "ingredient_graph.html"]
)
def test_javascript_pages_point_to_the_static_index_without_it(page):
    # It says plainly that the page needs JavaScript, and where to go instead.
    blocks = re.findall(r"<noscript>(.*?)</noscript>", (DOCS / page).read_text(encoding="utf-8"), re.DOTALL)
    assert any("JavaScript" in block and 'href="records/index.html"' in block for block in blocks), page


def test_not_found_page_routes_resolve_from_any_depth():
    # GitHub serves this one file for a missing URL at any depth, so every link
    # and asset is site-root-absolute; a relative one would 404 again.
    page = (DOCS / "404.html").read_text(encoding="utf-8")
    refs = re.findall(r'(?:href|src|action)="([^"]*)"', page)
    site = urlsplit(render.SITE_ROOT).path
    for ref in refs:
        assert ref.startswith((site, "https://", "#")), f"relative route {ref!r} 404s below the site root"
    own = [ref.split("#", 1)[0] for ref in refs if ref.startswith(site)]
    assert {f"{site}browser.html", f"{site}theme-toggle.js", f"{site}app/discussions/index.html"} <= set(own)
    assert len(own) >= 11
    built_later = {"records/index.html", "schema/index.html", "app/discussions/index.html"}
    for ref in own:
        name = ref[len(site):]
        assert name in built_later or (DOCS / name).is_file(), ref


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


# ---------- visual_alternative / text_map ----------


RECORD_LOOKUP_HARNESS = r"""
const vm = require('node:vm');
const source = SOURCE;
const node = () => ({style: {}, setAttribute() {}, replaceChildren() {}, append() {}, addEventListener() {}});
const catalog = {ingredients: [
  {record_id: 'MIM:A', detail_page: 'records/ingredient/mapped/A.html'},
  {record_id: 'MIM:B', detail_page: 'records/ingredient/mapped/B.html'},
  {record_id: 'MIM:B', detail_page: 'records/ingredient/unmapped/B.html'},
  {record_id: 'MIM:C', detail_page: 'javascript:alert(1)'},
]};
const context = {window: {}, document: {createElement: node, querySelector: () => ({after() {}})},
  fetch: async () => ({ok: true, json: async () => catalog})};
vm.createContext(context);
vm.runInContext(source, context);
context.window.MimRecords.pages().then(pages => console.log(JSON.stringify({
  A: pages.get('MIM:A'), B: pages.get('MIM:B'), C: pages.has('MIM:C')})));
"""


def test_map_record_lookup_is_exposed_for_the_data_tables(tmp_path):
    source = (DOCS / "map-record-navigation.js").read_text(encoding="utf-8")
    pages = run_node(tmp_path, RECORD_LOOKUP_HARNESS.replace("SOURCE", json.dumps(source)))
    assert pages["A"]["detail_page"] == "records/ingredient/mapped/A.html"
    assert pages["B"] is None and pages["C"] is False


MAP_TABLE_HARNESS = r"""
const vm = require('node:vm');
const source = SOURCE;
async function run(pagesResult) {
  const table = {innerHTML: ''};
  const details = {open: false, listeners: [], addEventListener(name, fn) { this.listeners.push(fn); }};
  const context = {
    ingredientData: [{id: 'MIM:A', name: 'Agar <b>', identifier: 'CHEBI:1'}, {id: 'MIM:B', name: 'Broth'}],
    document: {getElementById: id => (id === 'data-table' ? details : table)},
    window: {MimRecords: {pages: async () => { if (pagesResult instanceof Error) throw pagesResult; return pagesResult; }}},
  };
  vm.createContext(context);
  vm.runInContext(source + '\nbuildTable();', context);
  await new Promise(resolve => setTimeout(resolve, 10));  // any eager render would land now
  const before = table.innerHTML;
  details.open = true;
  details.listeners.forEach(fn => fn());
  await new Promise(resolve => setTimeout(resolve, 10));
  return {before, after: table.innerHTML};
}
(async () => {
  console.log(JSON.stringify({
    linked: await run(new Map([['MIM:A', {detail_page: 'records/ingredient/mapped/A.html'}], ['MIM:B', null]])),
    failed: await run(new Error('catalog unavailable')),
  }));
})().catch(error => { console.error(error); process.exitCode = 1; });
"""


def build_table_source(page: str) -> str:
    text = (DOCS / page).read_text(encoding="utf-8")
    start = text.index("        function buildTable() {")
    return text[start : text.index("\n        }\n", start) + len("\n        }\n")]


@pytest.mark.parametrize("page", ["ingredient_umap.html", "ingredient_graph.html"])
def test_map_data_table_rows_link_their_records_when_opened(tmp_path, page):
    harness = MAP_TABLE_HARNESS.replace("SOURCE", json.dumps(build_table_source(page)))
    result = run_node(tmp_path, harness)
    assert "<tbody>" not in result["linked"]["before"], "rows render only when the table opens"
    linked = result["linked"]["after"]
    assert '<a href="records/ingredient/mapped/A.html">Agar &lt;b&gt;</a>' in linked
    assert "<td>Broth</td>" in linked and "<caption>" not in linked
    failed = result["failed"]["after"]
    assert "<a " not in failed and "<caption>Record links are unavailable" in failed
    wrap = '<div class="data-table-wrap" role="region" aria-label="Map data as a table" tabindex="0">'
    assert wrap in (DOCS / page).read_text(encoding="utf-8")


TEXT_MAP_RECORDS_HARNESS = r"""
const vm = require('node:vm');
const context = {window: {}};
vm.createContext(context);
vm.runInContext(SOURCE, context);
const {linkPoints, coverage} = context.window.TextMapRecords;
const points = [
  {url: 'records/ingredient/mapped/-_-anisomycin.html'},
  {url: 'records/ingredient/unmapped/Moved.html'},
  {url: 'records/ingredient/mapped/Gone.html'},
  {url: 'records/ingredient/mapped/Plain.html'},
  // Embedded under the current page-name rule, then moved to mapped/.
  {url: 'records/ingredient/unmapped/_-_-Renamed.html'},
];
const rows = [
  {source_file: 'mapped/(-)-Renamed.yaml', detail_page: 'records/ingredient/mapped/_-_-Renamed.html', mapping_status: 'MAPPED'},
  {source_file: 'mapped/(-)-anisomycin.yaml', detail_page: 'records/ingredient/mapped/_-_-anisomycin.html', mapping_status: 'MAPPED'},
  {source_file: 'mapped/Moved.yaml', detail_page: 'records/ingredient/mapped/Moved.html', mapping_status: 'MAPPED'},
  {source_file: 'mapped/Plain.yaml', detail_page: 'records/ingredient/mapped/Plain.html', mapping_status: 'MAPPED'},
  {source_file: 'mapped/Dead.yaml', detail_page: 'records/ingredient/mapped/Dead.html', mapping_status: 'REJECTED'},
  {source_file: 'unmapped/New.yaml', detail_page: 'records/ingredient/unmapped/New.html', mapping_status: 'UNMAPPED'},
];
linkPoints(points, rows);
const c = coverage(points, rows);
console.log(JSON.stringify({pages: points.map(p => p.page), plotted: c.plotted, total: c.total,
  rejected: c.rejected.map(r => r.source_file), later: c.later.map(r => r.source_file), unpublished: c.unpublished}));
"""


def test_text_map_points_open_the_published_record_and_coverage_is_stated(tmp_path):
    source = (DOCS / "text-map-records.js").read_text(encoding="utf-8")
    result = run_node(tmp_path, TEXT_MAP_RECORDS_HARNESS.replace("SOURCE", json.dumps(source)))
    assert result["pages"] == [
        "records/ingredient/mapped/_-_-anisomycin.html",  # embedded under the old page-name rule
        "records/ingredient/mapped/Moved.html",  # curation moved the record
        "",  # no longer published: never linked
        "records/ingredient/mapped/Plain.html",
        "records/ingredient/mapped/_-_-Renamed.html",  # current-rule name, moved record
    ]
    assert (result["plotted"], result["total"], result["unpublished"]) == (4, 6, 1)
    assert result["rejected"] == ["mapped/Dead.yaml"] and result["later"] == ["unmapped/New.yaml"]


@pytest.mark.parametrize(
    "page",
    [render.TEMPLATES_DIR / "text_map.html", DOCS / "ingredient_umap.html", DOCS / "ingredient_graph.html"],
    ids=lambda path: path.name,
)
def test_narrow_map_layout_is_not_widened_by_an_opened_table(page):
    # A bare 1fr track grows to its content's min-content width: opening the
    # text map's table widened the page to 1,295 px at 390 px.
    css = page.read_text(encoding="utf-8")
    assert "grid-template-columns: 1fr;" not in css
    assert "grid-template-columns: minmax(0, 1fr);" in css


def test_text_map_page_states_coverage_and_offers_its_points_as_a_table():
    page = (DOCS / "text_map.html").read_text(encoding="utf-8")
    assert page.index('<script src="text-map-records.js"></script>') < page.index("const MAP_DATA")
    assert '<p class="coverage" id="map-coverage" role="status">' in page
    assert '<div class="table-scroll" role="region" aria-label="Text map points as a table" tabindex="0">' in page
    assert 'href="${esc(recordHref(p))}"' in page and 'href="${esc(p.url)}"' not in page


def test_text_embedding_names_the_page_the_site_publishes():
    spec = importlib.util.spec_from_file_location("mim_embed_records", ROOT / "scripts/embed_records.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    for name in ("(-)-anisomycin", "Calcium(2)", "Mix + tea", "Nacl"):
        path = Path("mapped") / f"{name}.yaml"
        assert module.slug_for_source("mapped", path) == render.slug_for({}, path), name


# ---------- discussions ----------


def discussion_data(entries: list[dict]) -> str:
    return (
        f"window.searchData = {json.dumps(entries, indent=1)};\n"
        'window.searchMetrics = {};\nwindow.repoName = "MediaIngredientMech";\n'
    )


def add_discussion_browser(repo: Path, page_url: str) -> None:
    folder = repo / "app" / "discussions"
    folder.mkdir(parents=True)
    shutil.copyfile(ROOT / "app/discussions/index.html", folder / "index.html")
    (folder / "data.js").write_text(
        discussion_data([{"discussion_id": "gap-1", "source_file": "Salt.yaml", "page_url": page_url}])
    )


def test_discussion_index_is_published_with_a_way_back_and_the_licence(site_repo, builder, tmp_path):
    repo, _ = site_repo
    add_discussion_browser(repo, "../../records/ingredient/mapped/Salt.html#discussions")
    output = tmp_path / "site"
    builder.build_site(repo, output)
    builder.check_site(repo, output)
    page = (output / "app/discussions/index.html").read_text(encoding="utf-8")
    nav = page.split('<nav aria-label="Project navigation">', 1)[1].split("</nav>", 1)[0]
    assert hrefs(nav)[:2] == ["../../index.html", "../../browser.html"]
    assert LICENCE in footer(page)
    assert (output / "app/discussions/data.js").read_bytes() == (repo / "app/discussions/data.js").read_bytes()
    receipt = json.loads((output / "records/build.json").read_text())
    assert set(builder.DISCUSSION_FILES) <= set(receipt["assets"])


@pytest.mark.parametrize(
    "page_url",
    [
        "../../pages/ingredient/mapped/Salt.html#discussions",  # the route the config used to name
        "../../records/ingredient/mapped/Mud.html#discussions",  # a record without that discussion
    ],
)
def test_build_refuses_a_discussion_index_that_does_not_match_the_records(site_repo, builder, tmp_path, page_url):
    repo, _ = site_repo
    add_discussion_browser(repo, page_url)
    with pytest.raises(ValueError, match="gen-discussions-data"):
        builder.build_site(repo, tmp_path / "site")


def test_committed_discussion_index_matches_the_records(builder, tmp_path):
    pages: dict[str, set[str]] = {}
    for source in builder.source_files(ROOT):
        text = source.read_text(encoding="utf-8")
        ids = set()
        if "\ndiscussions:" in text:
            ids = {str(d.get("discussion_id", "")) for d in yaml.safe_load(text)["discussions"]}
        pages[f"records/ingredient/{render.slug_for({}, source)}.html"] = ids
    assert builder.publish_discussions(ROOT, tmp_path, pages) == list(builder.DISCUSSION_FILES)


def test_pages_redeploy_when_the_discussion_index_or_its_route_changes():
    workflow = yaml.safe_load((ROOT / ".github/workflows/generate-pages.yaml").read_text(encoding="utf-8"))
    paths = workflow.get("on", workflow.get(True))["push"]["paths"]
    assert {"app/discussions/**", "conf/discussions_config.yaml"} <= set(paths)
    assert workflow["permissions"]["contents"] == "read"


def test_navigation_links_the_discussion_index():
    for page in ("index.html", "browser.html", "ingredient_umap.html", "ingredient_graph.html", "text_map.html"):
        header = re.search(r"<header[^>]*>(.*?)</header>", (DOCS / page).read_text(encoding="utf-8"), re.DOTALL)
        assert "app/discussions/index.html" in hrefs(header.group(1)), page
