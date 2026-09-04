"""Guards for the flat-export coverage gate and the synonyms column (#229).

MIM's product is turning a raw ingredient string into an ontology term, and
consumers do that against `docs/data/all_ingredients.csv`. A merge deletes the
duplicate record and keeps its raw label only as a synonym, adding no SSSOM row
— so `D-lactate` resolved to UNMAPPED_0654 before PR #227 and to nothing after,
while reconcile, roundtrip and duplicate-ids all stayed green. These tests pin
both halves of the fix: the column exists, and the gate fails without it.
"""

import csv
import importlib.util
import subprocess
import sys
from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).parent.parent
EXPORT = ROOT / "scripts" / "export_lists.py"
CHECK = ROOT / "scripts" / "check_flat_export_coverage.py"


def _load(path):
    spec = importlib.util.spec_from_file_location(path.stem, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = mod
    spec.loader.exec_module(mod)
    return mod


@pytest.fixture(scope="module")
def export_lists():
    return _load(EXPORT)


def rec(identifier, term, synonyms=(), status="MAPPED"):
    return {
        "identifier": identifier, "preferred_term": term, "mapping_status": status,
        "synonyms": [{"synonym_text": s, "synonym_type": "RAW_TEXT"} for s in synonyms],
        "ontology_mapping": {"ontology_id": identifier, "ontology_label": term},
        "occurrence_statistics": {"total_occurrences": 0, "media_count": 0},
    }


def test_synonyms_excludes_the_preferred_term_and_dedupes(export_lists):
    r = rec("CHEBI:1", "Glycerol", ["Glycerol", "glycerine", "glycerine"])
    assert export_lists._synonyms(r) == ["glycerine"]


def test_synonyms_handles_records_with_no_synonyms(export_lists):
    assert export_lists._synonyms({"preferred_term": "X"}) == []
    assert export_lists._synonyms({"preferred_term": "X", "synonyms": None}) == []


def test_csv_publishes_a_merged_label(export_lists, tmp_path):
    """The #229 scenario: the raw label survives only as a synonym."""
    out = tmp_path / "all.csv"
    export_lists.export_to_csv([rec("CHEBI:16004", "(R)-lactate", ["D-lactate"])], out)
    rows = list(csv.DictReader(out.open()))
    assert "synonyms" in rows[0]
    assert rows[0]["synonyms"] == "D-lactate"
    assert rows[0]["identifier"] == "CHEBI:16004", "must resolve to the merge target"


def test_csv_synonyms_column_is_appended_last(export_lists, tmp_path):
    """Positional consumers keep working only if the column goes on the end."""
    out = tmp_path / "all.csv"
    export_lists.export_to_csv([rec("CHEBI:1", "X")], out)
    header = out.read_text().splitlines()[0].split(",")
    assert header[-1] == "synonyms"
    assert header[:9] == ["identifier", "ontology_id", "preferred_term", "mapping_status",
                          "ontology_label", "ontology_source", "mapping_quality",
                          "total_occurrences", "media_count"]


def test_csv_uses_lf_line_endings(export_lists, tmp_path):
    out = tmp_path / "all.csv"
    export_lists.export_to_csv([rec("CHEBI:1", "X")], out)
    assert b"\r\n" not in out.read_bytes()


def test_json_carries_synonyms_as_a_list(export_lists, tmp_path):
    import json
    out = tmp_path / "all.json"
    export_lists.export_to_json([rec("CHEBI:16004", "(R)-lactate", ["D-lactate"])], out)
    assert json.loads(out.read_text())[0]["synonyms"] == ["D-lactate"]


def test_markdown_deliberately_has_no_synonyms_column(export_lists, tmp_path):
    """A pipe-joined list would collide with the table's own separator."""
    out = tmp_path / "all.md"
    export_lists.export_to_markdown([rec("CHEBI:1", "X", ["y"])], out, "T")
    header = [ln for ln in out.read_text().splitlines() if ln.startswith("| Identifier")][0]
    assert "Synonym" not in header


# --- the gate itself -------------------------------------------------------

def build(tmp_path, records, csv_rows, header=None):
    (tmp_path / "data" / "curated").mkdir(parents=True)
    (tmp_path / "data" / "curated" / "mapped_ingredients.yaml").write_text(
        yaml.safe_dump({"ingredients": records}))
    (tmp_path / "data" / "curated" / "unmapped_ingredients.yaml").write_text(
        yaml.safe_dump({"ingredients": []}))
    (tmp_path / "docs" / "data").mkdir(parents=True)
    cols = header or ["identifier", "preferred_term", "synonyms"]
    lines = [",".join(cols)] + [",".join(r) for r in csv_rows]
    body = "\n".join(lines) + "\n"
    # the gate covers all three flat CSVs; mapped/ mirror `records`, unmapped is
    # empty here so its header alone satisfies it
    (tmp_path / "docs" / "data" / "all_ingredients.csv").write_text(body)
    (tmp_path / "docs" / "data" / "mapped_ingredients.csv").write_text(body)
    (tmp_path / "docs" / "data" / "unmapped_ingredients.csv").write_text(",".join(cols) + "\n")
    # the label index is a different shape (one row per label) and has its own check
    idx = ["label,match_type,identifier,preferred_term,ontology_id,mapping_status"]
    for r in records:
        idx.append(f'"{r["preferred_term"]}",preferred_term,{r["identifier"]},'
                   f'"{r["preferred_term"]}",{r["identifier"]},{r.get("mapping_status","")}')
        for syn in (r.get("synonyms") or []):
            idx.append(f'"{syn["synonym_text"]}",synonym,{r["identifier"]},'
                       f'"{r["preferred_term"]}",{r["identifier"]},{r.get("mapping_status","")}')
    (tmp_path / "docs" / "data" / "label_index.csv").write_text("\n".join(idx) + "\n")
    (tmp_path / "scripts").mkdir(exist_ok=True)
    (tmp_path / "scripts" / CHECK.name).write_text(CHECK.read_text())
    # the gate imports the exporter's _synonyms() on purpose, so the rule for
    # what is publishable cannot drift between producing and checking
    (tmp_path / "scripts" / EXPORT.name).write_text(EXPORT.read_text())
    (tmp_path / "src" / "mediaingredientmech").mkdir(parents=True)
    (tmp_path / "src" / "mediaingredientmech" / "__init__.py").write_text("")
    (tmp_path / "src" / "mediaingredientmech" / "synonym_policy.py").write_text(
        "NON_RESOLVING_SYNONYM_TYPES = frozenset({'REJECTED_LABEL'})\n\n"
        "def is_resolving_synonym(synonym):\n"
        "    synonym_type = str(synonym.get('synonym_type') or '').strip().upper()\n"
        "    return synonym_type not in NON_RESOLVING_SYNONYM_TYPES\n"
    )
    return tmp_path


def run(tmp_path, *args):
    """Coverage only: the synthetic repo has no exporter for the freshness half."""
    return subprocess.run(
        [sys.executable, str(tmp_path / "scripts" / CHECK.name), "--skip-freshness", *args],
        capture_output=True, text=True)


def test_gate_passes_when_every_label_is_published(tmp_path):
    repo = build(tmp_path, [rec("CHEBI:16004", "(R)-lactate", ["D-lactate"])],
                 [["CHEBI:16004", "(R)-lactate", "D-lactate"]])
    assert run(repo).returncode == 0


def test_gate_fails_when_a_synonym_is_unpublished(tmp_path):
    """Exactly the regression: the record is there, the merged label is not."""
    repo = build(tmp_path, [rec("CHEBI:16004", "(R)-lactate", ["D-lactate"])],
                 [["CHEBI:16004", "(R)-lactate", ""]])
    out = run(repo)
    assert out.returncode == 2
    assert "D-lactate" in out.stdout


def test_gate_fails_when_the_synonyms_column_is_missing_entirely(tmp_path):
    """The pre-#229 artifact shape must not read as success."""
    repo = build(tmp_path, [rec("CHEBI:16004", "(R)-lactate", ["D-lactate"])],
                 [["CHEBI:16004", "(R)-lactate"]],
                 header=["identifier", "preferred_term"])
    out = run(repo)
    assert out.returncode == 2
    assert "synonyms" in out.stdout


def test_gate_fails_when_the_flat_artifact_is_absent(tmp_path):
    repo = build(tmp_path, [rec("CHEBI:1", "X")], [])
    (repo / "docs" / "data" / "all_ingredients.csv").unlink()
    assert run(repo).returncode == 2


# --- detritus filtering and separator safety (#231 review) ------------------

@pytest.mark.parametrize("text", [
    "Role: Carbon source; Properties: Organic compound, Defined component",
    "Role: Mineral source; Properties: Solution",
    "(sodium salt)",
    "(for solid medium, alternative)",
    "( Noble)",
])
def test_curation_annotations_are_not_published_as_labels(export_lists, text):
    """No record answers to `(sodium salt)`; publishing it made it 'resolve' to
    eight different CHEBI ids."""
    assert export_lists._synonyms(rec("CHEBI:1", "X", [text])) == []


@pytest.mark.parametrize("text", [
    "Role reversal buffer",      # 'Role' without the annotation shape
    "Sodium acetate (anhydrous)", # parenthetical inside a real name
    "(R)-lactate",                # a real name that starts with a parenthesis
])
def test_real_labels_survive_the_detritus_filter(export_lists, text):
    assert export_lists._synonyms(rec("CHEBI:1", "X", [text])) == [text]


def test_a_pipe_in_a_synonym_is_refused_not_silently_split(export_lists, tmp_path):
    """Joining it would read back as two bogus labels, and the coverage gate
    would then advise re-running the export forever."""
    with pytest.raises(ValueError, match="separator"):
        export_lists._join_synonyms(rec("CHEBI:9", "X", ["Glucose|Fructose mix"]))


def test_coverage_counter_is_a_ratio_not_the_published_set_size(tmp_path):
    """It printed '8116/8116 resolvable' directly above a failure."""
    repo = build(tmp_path, [rec("CHEBI:1", "A", ["missing-one"])],
                 [["CHEBI:1", "A", ""], ["CHEBI:2", "extra-published", ""]])
    out = run(repo)
    assert out.returncode == 2
    assert "1/2 curated label(s) resolvable" in out.stdout


# --- browser_export: the #233 silent-drop (PR #237 review) ------------------

@pytest.fixture(scope="module")
def browser_export():
    return _load(ROOT / "scripts" / "browser_export.py")


def test_null_ontology_mapping_does_not_drop_the_record(browser_export):
    """`ontology_mapping: null` is valid on an unmapped record. `.get(k, {})`
    returned None, `None.get()` raised, the per-file except swallowed it and the
    run still exited 0 — so TAPSO vanished from the deployed catalog (#233)."""
    rec = {"identifier": "UNMAPPED_1", "preferred_term": "TAPSO",
           "mapping_status": "UNMAPPED", "ontology_mapping": None,
           "synonyms": None, "occurrence_statistics": None}
    out = browser_export.extract_ingredient_for_browser(rec, "Tapso.yaml")
    assert out["preferred_term"] == "TAPSO"


def test_browser_export_preserves_and_indexes_component_partonomy(browser_export):
    rec = {
        "identifier": "kgmicrobe.ingredient:test_mix",
        "preferred_term": "Test mix",
        "mapping_status": "MAPPED",
        "components": [
            {
                "component_name": "clarified rumen fluid",
                "component_id": "MICRO:0000520",
                "reference_scope": "EXTERNAL_TERM",
            }
        ],
        "component_assertion": {
            "method": "LABEL_ENUMERATION",
            "completeness": "COMPLETE",
            "evidence": [{"evidence_type": "SOURCE_LABEL", "source": "test"}],
        },
    }
    out = browser_export.extract_ingredient_for_browser(rec, "test.yaml")
    assert out["components"] == rec["components"]
    assert out["component_assertion"] == rec["component_assertion"]
    assert "clarified rumen fluid" in out["searchable"]
    assert "micro:0000520" in out["searchable"]


def test_browser_export_does_not_change_search_text_without_components(browser_export):
    rec = {
        "identifier": "CHEBI:1",
        "preferred_term": "Test ingredient",
        "mapping_status": "MAPPED",
        "ontology_mapping": {
            "ontology_id": "CHEBI:1",
            "ontology_label": "test chemical",
        },
        "synonyms": [{"synonym_text": "example synonym"}],
    }
    out = browser_export.extract_ingredient_for_browser(rec, "test.yaml")
    expected = "Test ingredient test chemical example synonym CHEBI:1".lower()
    assert out["searchable"] == expected


def test_browser_export_exits_nonzero_when_a_record_fails(tmp_path):
    """A short catalog deploys to Pages; nothing downstream notices the gap."""
    src = (ROOT / "scripts" / "browser_export.py").read_text()
    assert "sys.exit(1)" in src, "per-record failures must fail the run"
    assert "failures.append" in src


def test_stale_ingredients_json_names_export_browser_not_export_lists():
    """browser_export.py reads data/ingredients/, not data/curated/, and
    `just export-lists` does not regenerate it — the first message sent the
    curator to a command that produces no diff."""
    src = (ROOT / "scripts" / "check_flat_export_coverage.py").read_text()
    assert "just export-browser" in src
    assert "browser_export.py, reads data/ingredients/" in src


def test_published_browser_renders_typed_components():
    html = (ROOT / "docs" / "browser.html").read_text()
    assert "ing.components" in html
    assert "component.reference_scope" in html
    assert "Material components" in html


# --- label_index.csv: per-label resolution with precedence (#232) -----------

def test_label_index_puts_preferred_term_before_synonym(export_lists, tmp_path):
    """`Vitamin B12` is the preferred_term of one record and a synonym of two.
    A consumer joining a raw string had no way to choose."""
    out = tmp_path / "label_index.csv"
    export_lists.export_label_index([
        rec("CHEBI:17439", "Cyanocobalamin", ["Vitamin B12"]),
        rec("CHEBI:176843", "Vitamin B12"),
    ], out)
    rows = [r for r in csv.DictReader(out.open()) if r["label"] == "Vitamin B12"]
    assert rows[0]["match_type"] == "preferred_term"
    assert rows[0]["identifier"] == "CHEBI:176843"
    assert rows[1]["match_type"] == "synonym"


def test_label_index_has_a_row_per_label_not_per_record(export_lists, tmp_path):
    out = tmp_path / "label_index.csv"
    n = export_lists.export_label_index([rec("CHEBI:1", "A", ["b", "c"])], out)
    assert n == 3, "one preferred_term row plus one per synonym"


def test_label_index_uses_lf_line_endings(export_lists, tmp_path):
    out = tmp_path / "label_index.csv"
    export_lists.export_label_index([rec("CHEBI:1", "A", ["b", "c"])], out)
    assert b"\r\n" not in out.read_bytes()


def test_label_index_excludes_curation_detritus(export_lists, tmp_path):
    """It reuses _synonyms(), so `Role: …; Properties: …` must not become a label."""
    out = tmp_path / "label_index.csv"
    export_lists.export_label_index(
        [rec("CHEBI:1", "A", ["Role: Carbon source; Properties: Organic compound"])], out)
    labels = {r["label"] for r in csv.DictReader(out.open())}
    assert labels == {"A"}


def test_label_index_is_in_the_freshness_set():
    """Asserting the string appears *somewhere* in the checker would pass on a
    comment; assert the actual set membership."""
    mod = _load(ROOT / "scripts" / "check_flat_export_coverage.py")
    assert "label_index.csv" in mod.DETERMINISTIC


def test_mapped_record_outranks_a_rejected_one(export_lists, tmp_path):
    """A REJECTED record's preferred_term must not outrank a MAPPED record's
    synonym — `Bacto Soytone` resolved to a rejected tombstone."""
    out = tmp_path / "label_index.csv"
    export_lists.export_label_index([
        rec("CHEBI:8150", "Bacto Soytone", status="REJECTED"),
        rec("FOODON:03315720", "Soy peptone", ["Bacto Soytone"]),
    ], out)
    rows = [r for r in csv.DictReader(out.open()) if r["label"] == "Bacto Soytone"]
    assert rows[0]["mapping_status"] == "MAPPED"
    assert rows[0]["identifier"] == "FOODON:03315720"


def test_rows_for_one_label_are_contiguous_case_insensitively(export_lists, tmp_path):
    """Contiguity is guaranteed for the CASE-INSENSITIVE group, not the exact
    string.

    This test used to require rows for the exact string `Peptone` to be
    adjacent, which needed the raw `label` to sort directly after
    `label.lower()` — above every semantic key. That is what let an ALL-CAPS
    synonym outrank the record owning the label: `FRUCTOSE` beat `Fructose`,
    `Citric Acid` (on *Trisodium citrate*) beat `Citric acid`, and 16 labels
    resolved to the wrong identifier (#232).

    The two properties are incompatible — ordering cannot put both the raw
    string and the semantic keys first — and correctness wins, because
    `LABEL_INDEX_CONTRACT` promises *take the first row for a label*, matched
    case-insensitively. It never promised exact-case runs. `label` is now the
    final tie-break, for determinism only.
    """
    out = tmp_path / "label_index.csv"
    export_lists.export_label_index([
        rec("CHEBI:1", "Peptone", ["shared"]),
        rec("CHEBI:2", "peptone"),
        rec("CHEBI:3", "Other", ["Peptone"]),
    ], out)
    labels = [r["label"] for r in csv.DictReader(out.open())]
    idx = [i for i, label in enumerate(labels) if label.lower() == "peptone"]
    assert idx == list(range(idx[0], idx[0] + len(idx))), "must be contiguous"


def test_label_with_comma_and_quote_round_trips(export_lists, tmp_path):
    out = tmp_path / "label_index.csv"
    tricky = 'bromocresol purple", 0.04%'
    export_lists.export_label_index([rec("CHEBI:1", "X", [tricky])], out)
    assert tricky in {r["label"] for r in csv.DictReader(out.open())}
