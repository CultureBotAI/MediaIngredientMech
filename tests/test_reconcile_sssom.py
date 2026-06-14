"""Tests for scripts/reconcile_sssom.py — in particular the registry→OBO parent
remap that --apply previously could not fix.

The reconciler used to identify the stale ontology row by an ``obo:`` object_source.
MeSH is an ontology source here but its object_source is ``registry:mesh``, so a
mesh→CHEBI parent remap was detected as drift yet ``--apply`` synced 0 rows. The
fix recognises the ontology row by its object_id PREFIX instead. These pin that.

OAK is stubbed (``_canonical_label_resolver`` monkeypatched) so the tests are
CI-safe — no chebi.db / network.
"""

import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location(
    "reconcile_sssom",
    Path(__file__).parent.parent / "scripts" / "reconcile_sssom.py",
)
mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(mod)

COLS = [
    "subject_id", "subject_label", "predicate_id", "object_id", "object_label",
    "object_source", "mapping_justification", "source", "mapping_date",
    "confidence", "comment", "other", "validation_method",
]


def _row(**kw):
    return "\t".join(str(kw.get(c, "")) for c in COLS)


def _write_sssom(path, rows):
    head = ['# mapping_set_version: "2026-01-01"', '# mapping_date: "2026-01-01"']
    path.write_text("\n".join(head + ["\t".join(COLS)] + rows) + "\n")


def _curated(term, oid, label, source, quality):
    return {"ingredients": [{
        "preferred_term": term, "mapping_status": "MAPPED",
        "ontology_mapping": {
            "ontology_id": oid, "ontology_label": label,
            "ontology_source": source, "mapping_quality": quality,
        },
    }]}


def _stub_resolver(monkeypatch, labels):
    monkeypatch.setattr(mod, "_canonical_label_resolver", lambda: (lambda oid: labels.get(oid)))


# -- _is_ontology_row -------------------------------------------------------

def test_is_ontology_row_recognises_ontology_vs_registry_prefixes():
    assert mod._is_ontology_row("CHEBI:28874")
    assert mod._is_ontology_row("FOODON:03315720")
    assert mod._is_ontology_row("mesh:D013025")        # lowercase mesh — the bug case
    assert mod._is_ontology_row("MESH:C016600")        # uppercase too
    assert not mod._is_ontology_row("cas:97281-52-2")
    assert not mod._is_ontology_row("kgmicrobe.compound:foo")
    assert not mod._is_ontology_row("registry:bar")


# -- the registry(mesh)→OBO remap that used to sync 0 -----------------------

def _mesh_parent_fixture(tmp_path):
    sssom = tmp_path / "m.sssom.tsv"
    rows = [
        _row(subject_id="MIM:Foo", subject_label="Foo", predicate_id="skos:narrowMatch",
             object_id="mesh:D013025", object_label="Glycine max", object_source="registry:mesh",
             mapping_justification="semapv:ManualMappingCuration", source="MIM:x",
             mapping_date="2026-01-01", confidence="0.9", comment="", other="",
             validation_method="none"),
        _row(subject_id="MIM:Foo", subject_label="Foo", predicate_id="skos:exactMatch",
             object_id="cas:1-1-1", object_label="Foo", object_source="registry:cas",
             mapping_justification="semapv:ManualMappingCuration", source="MIM:x",
             mapping_date="2026-01-01", confidence="0.99",
             comment="Registry/identity row for narrowMatch subject alongside parent mesh:D013025.",
             other="", validation_method="none"),
    ]
    _write_sssom(sssom, rows)
    return sssom


def test_find_drift_detects_stale_mesh_parent(tmp_path, monkeypatch):
    sssom = _mesh_parent_fixture(tmp_path)
    monkeypatch.setattr(mod, "SSSOM", sssom)
    _, _, _, rows = mod._read_sssom()
    curated = _curated("Foo", "CHEBI:28874", "phosphatidylinositol", "CHEBI", "BROAD_MATCH")
    drift = mod.find_drift(curated, rows)
    assert drift["gaps"] == [] and drift["orphans"] == []
    assert drift["stale"] and drift["stale"][0][0] == "Foo"
    assert drift["stale"][0][1] == "CHEBI:28874"  # expected id


def test_apply_remaps_mesh_parent_to_chebi(tmp_path, monkeypatch):
    sssom = _mesh_parent_fixture(tmp_path)
    monkeypatch.setattr(mod, "SSSOM", sssom)
    _stub_resolver(monkeypatch, {"CHEBI:28874": "phosphatidylinositol"})
    curated = _curated("Foo", "CHEBI:28874", "phosphatidylinositol", "CHEBI", "BROAD_MATCH")

    n_stale, n_orphan = mod.apply_reconcile(curated, "2026-06-13")
    assert (n_stale, n_orphan) == (1, 0)  # before the fix this was (0, 0)

    _, _, _, parsed = mod._read_sssom()
    onto = [r for r in parsed if r["object_id"] == "CHEBI:28874"][0]
    assert onto["predicate_id"] == "skos:broadMatch"
    assert onto["object_label"] == "phosphatidylinositol"
    assert onto["object_source"] == "obo:chebi.owl"
    assert onto["mapping_date"] == "2026-06-13"
    assert "REMAPPED" in onto["validation_method"]
    assert "reconciled to curated mapping" in onto["comment"]
    # the registry/identity row's comment is repointed to the new parent
    ident = [r for r in parsed if r["object_id"] == "cas:1-1-1"][0]
    assert "CHEBI:28874" in ident["comment"] and "mesh:D013025" not in ident["comment"]


# -- regression: obo→obo remap still works ----------------------------------

def test_apply_still_remaps_obo_to_obo(tmp_path, monkeypatch):
    sssom = tmp_path / "o.sssom.tsv"
    rows = [
        _row(subject_id="MIM:Bar", subject_label="Bar", predicate_id="skos:closeMatch",
             object_id="FOODON:00001", object_label="old", object_source="obo:foodon.owl",
             mapping_justification="semapv:ManualMappingCuration", source="MIM:x",
             mapping_date="2026-01-01", confidence="0.8", comment="", other="",
             validation_method="none"),
    ]
    _write_sssom(sssom, rows)
    monkeypatch.setattr(mod, "SSSOM", sssom)
    _stub_resolver(monkeypatch, {"CHEBI:28874": "phosphatidylinositol"})
    curated = _curated("Bar", "CHEBI:28874", "phosphatidylinositol", "CHEBI", "EXACT_MATCH")

    n_stale, n_orphan = mod.apply_reconcile(curated, "2026-06-13")
    assert (n_stale, n_orphan) == (1, 0)
    _, _, _, parsed = mod._read_sssom()
    onto = parsed[0]
    assert onto["object_id"] == "CHEBI:28874"
    assert onto["object_source"] == "obo:chebi.owl"
    assert onto["predicate_id"] == "skos:exactMatch"


# -- orphan handling unchanged ----------------------------------------------

def test_apply_drops_orphan_subject(tmp_path, monkeypatch):
    sssom = tmp_path / "p.sssom.tsv"
    rows = [
        _row(subject_id="MIM:Gone", subject_label="Gone", predicate_id="skos:exactMatch",
             object_id="CHEBI:9", object_label="x", object_source="obo:chebi.owl",
             mapping_justification="semapv:ManualMappingCuration", source="MIM:x",
             mapping_date="2026-01-01", confidence="0.9", comment="", other="",
             validation_method="none"),
    ]
    _write_sssom(sssom, rows)
    monkeypatch.setattr(mod, "SSSOM", sssom)
    _stub_resolver(monkeypatch, {})
    curated = {"ingredients": []}  # no record for "Gone" -> orphan
    n_stale, n_orphan = mod.apply_reconcile(curated, "2026-06-13")
    assert (n_stale, n_orphan) == (0, 1)
    _, _, _, parsed = mod._read_sssom()
    assert parsed == []  # orphan row dropped
