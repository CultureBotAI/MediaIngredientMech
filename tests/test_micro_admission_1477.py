"""Admission evidence stays separate from ingredient mapping or source approval."""

import csv
import hashlib
import importlib.util
import io
import json
import shutil
from pathlib import Path

import pytest

from mediaingredientmech.curie import MICRO_VERIFIED, CurieNormalizer
from mediaingredientmech.micro_source import SOURCE, load_source, source_term

CANONICAL = {"MICRO:0000181", "MICRO:0001736", "MICRO:0001795"}
LEGACY = {"MICRO:0002115", "MICRO:0002390", "MICRO:0002399"}
PARENTS = {
    "MICRO:0002115": ["MICRO:0001233"],
    "MICRO:0002390": ["MICRO:0000067"],
    "MICRO:0002399": ["MICRO:0002401"],
}


def evidence():
    return json.loads((SOURCE / "admission-1477.json").read_text())


def rows(path):
    with path.open(newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


@pytest.fixture
def verifier():
    path = Path(__file__).resolve().parents[1] / "scripts/verify_micro_ids.py"
    spec = importlib.util.spec_from_file_location("micro_verifier_1477", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_retained_canonical_and_legacy_authorities_are_distinct():
    captures = evidence()["retained_ols_responses"]
    assert set(captures) == CANONICAL | LEGACY
    assert CANONICAL <= MICRO_VERIFIED
    assert not LEGACY & MICRO_VERIFIED
    for curie, ref in captures.items():
        raw = (SOURCE / ref["path"]).read_bytes()
        assert hashlib.sha256(raw).hexdigest() == ref["sha256"]
        terms = json.loads(raw)["_embedded"]["terms"]
        assert len(terms) == 1
        term = terms[0]
        assert term["obo_id"] == curie
        assert term["label"] == ref["label"]
        assert term["is_obsolete"] is False
        assert term["is_defining_ontology"] is (curie in CANONICAL)
        prefix = "http://purl.obolibrary.org/obo/"
        if curie in LEGACY:
            prefix += "MicrO.owl/"
            assert source_term(curie).iri == term["iri"]
            assert source_term(curie).label == term["label"]
        else:
            assert source_term(curie) is None
        assert term["iri"] == prefix + curie.replace(":", "_") == ref["iri"]
        assert CurieNormalizer().normalize(curie).curie == curie


@pytest.mark.parametrize("curie", sorted(CANONICAL))
def test_canonical_verifier_uses_complete_retained_response(verifier, monkeypatch, curie):
    ref = evidence()["retained_ols_responses"][curie]
    raw = (SOURCE / ref["path"]).read_bytes()
    monkeypatch.setattr(verifier.urllib.request, "urlopen", lambda *a, **kw: io.BytesIO(raw))
    assert verifier.check(curie) == (True, "OK", ref["label"])


@pytest.mark.parametrize(
    "field,value,reason",
    [
        ("is_obsolete", True, "OBSOLETE"),
        ("is_defining_ontology", False, "NOT_DEFINING"),
        ("iri", "http://purl.obolibrary.org/obo/MicrO.owl/MICRO_0001736", "MALFORMED_IRI"),
    ],
)
def test_canonical_verifier_keeps_its_refusals(verifier, monkeypatch, field, value, reason):
    ref = evidence()["retained_ols_responses"]["MICRO:0001736"]
    response = json.loads((SOURCE / ref["path"]).read_bytes())
    response["_embedded"]["terms"][0][field] = value
    raw = json.dumps(response).encode()
    monkeypatch.setattr(verifier.urllib.request, "urlopen", lambda *a, **kw: io.BytesIO(raw))
    assert verifier.check("MICRO:0001736")[:2] == (False, reason)


def test_new_legacy_parents_and_iris_are_native_axioms():
    ref = evidence()["native_extraction"]["packaged_graph"]
    raw = (SOURCE / ref["path"]).read_bytes()
    assert hashlib.sha256(raw).hexdigest() == ref["sha256"]
    graph = json.loads(raw)["graphs"][0]
    nodes = {node["id"]: node for node in graph["nodes"]}
    table = {row["id"]: row for row in rows(SOURCE / "micro_nodes.tsv")}
    legacy = {row["id"]: row for row in rows(SOURCE / "legacy_nodes.tsv")}
    for curie, expected in PARENTS.items():
        term = source_term(curie)
        node = nodes[term.iri]
        assert node["lbl"] == term.label == table[curie]["name"]
        assert not node.get("meta", {}).get("deprecated", False)
        native_parents = [
            edge["obj"]
            for edge in graph["edges"]
            if edge["sub"] == term.iri and edge["pred"] == "is_a"
        ]
        assert (
            sorted(iri.rsplit("/", 1)[-1].replace("MICRO_", "MICRO:") for iri in native_parents)
            == expected
            == list(term.parents)
        )
        assert (
            legacy[term.iri.replace("http://purl.obolibrary.org/obo/", "OBO:")]["name"]
            == term.label
        )
        for iri in native_parents:
            parent = iri.rsplit("/", 1)[-1].replace("MICRO_", "MICRO:")
            assert nodes[iri]["lbl"] == table[parent]["name"]
            legacy_id = (
                iri.replace("http://purl.obolibrary.org/obo/", "OBO:")
                if "/MicrO.owl/" in iri
                else parent
            )
            assert legacy[legacy_id]["name"] == nodes[iri]["lbl"]


def test_original_snapshot_and_three_admissions_are_unchanged():
    base = evidence()["packaging"]["base_manifest"]
    current = json.loads((SOURCE / "manifest.json").read_text())
    for curie, term in base["reviewed_terms"].items():
        assert current["reviewed_terms"][curie] == term
    assert set(base["reviewed_terms"]) == {"MICRO:0002393", "MICRO:0002392", "MICRO:0002250"}
    for filename, ref in base["files"].items():
        original = b"".join(
            (SOURCE / filename).read_bytes().splitlines(keepends=True)[: ref["records"] + 1]
        )
        assert hashlib.sha256(original).hexdigest() == ref["sha256"]


@pytest.mark.parametrize(
    "curie", ["MICRO:0002401", "MICRO:0001232", "MICRO:0002398", "MICRO:0002402"]
)
def test_context_or_obo_id_existence_does_not_admit_more_terms(curie):
    assert source_term(curie) is None
    assert curie not in MICRO_VERIFIED
    assert not CurieNormalizer().normalize(curie)


@pytest.mark.parametrize("mutation", ["node", "legacy", "parent", "deprecated", "row_count"])
def test_new_legacy_admission_refuses_incomplete_or_contradictory_tables(tmp_path, mutation):
    target = tmp_path / "micro"
    shutil.copytree(SOURCE, target)
    manifest_path = target / "manifest.json"
    manifest = json.loads(manifest_path.read_text())
    if mutation == "row_count":
        manifest["files"]["micro_nodes.tsv"]["records"] += 1
    else:
        filename = "legacy_nodes.tsv" if mutation == "legacy" else "micro_nodes.tsv"
        path = target / filename
        table = rows(path)
        if mutation == "deprecated":
            next(row for row in table if row["id"] == "MICRO:0002399")["deprecated"] = "true"
        else:
            removed = {
                "node": "MICRO:0002399",
                "legacy": "OBO:MicrO.owl/MICRO_0002399",
                "parent": "MICRO:0002401",
            }[mutation]
            table = [row for row in table if row["id"] != removed]
        with path.open("w", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=list(table[0]), delimiter="\t")
            writer.writeheader()
            writer.writerows(table)
        manifest["files"][filename].update(
            sha256=hashlib.sha256(path.read_bytes()).hexdigest(), records=len(table)
        )
    manifest_path.write_text(json.dumps(manifest))
    with pytest.raises(ValueError, match="MICRO source"):
        load_source(target)
