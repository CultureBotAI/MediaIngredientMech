"""An unrelated batch cannot renew or alter a companion scientific approval."""

import importlib.util
import sys
from copy import deepcopy
from pathlib import Path

import pytest

from mediaingredientmech.ingredient_bundle_contract import (
    _base_table,
    content_sha256,
    read_json,
    reviewed_products,
)

ROOT = Path(__file__).resolve().parents[1]
HELPER = ROOT / "reports/ingredient_bundle_20261101/refresh_unchanged_cohort.py"
spec = importlib.util.spec_from_file_location("refresh_unchanged_cohort", HELPER)
refresh = importlib.util.module_from_spec(spec)
spec.loader.exec_module(refresh)


@pytest.fixture(scope="module")
def cohort():
    """Portable synthetic history, without git objects or external providers."""
    current_review = read_json((ROOT / refresh.SUCCESSOR).read_bytes())
    current = {p: (ROOT / p).read_bytes() for p in refresh.source_names(current_review)}
    prior = deepcopy(current_review)
    before = dict(current)
    base_path = prior["base_review"]
    base = read_json(before[base_path])
    source = base["source_sssom"]
    # Current batch's newest date belongs only to owners outside this cohort.
    before[source] = before[source].replace(b"2026-11-01", b"2026-10-15")
    evidence = read_json(before[refresh.EVIDENCE])
    evidence["fixture_marker"] = "unselected container-only historical change"
    before[refresh.EVIDENCE] = refresh.encode(evidence)
    base["source_sha256"] = content_sha256(before[source])
    base["inputs"][refresh.EVIDENCE] = content_sha256(before[refresh.EVIDENCE])
    before[base_path] = refresh.encode(base)
    prior["base_review_sha256"] = content_sha256(before[base_path])
    prior["inputs"][source] = content_sha256(before[source])
    prior["inputs"][refresh.EVIDENCE] = content_sha256(before[refresh.EVIDENCE])
    contracts = {p: (ROOT / p).read_bytes() for p in refresh.CONTRACTS}
    reviewed_products(prior, before)
    return prior, before, current, contracts


def verify(cohort, current=None, contracts=None):
    prior, before, source, old_contracts = cohort
    return refresh.verify_unchanged_cohort(
        prior,
        before,
        source if current is None else current,
        old_contracts,
        old_contracts if contracts is None else contracts,
    )


def selected_decision(cohort):
    prior, _, current, _ = cohort
    base = read_json(current[prior["base_review"]])
    claims = read_json(current[prior["claims_file"]])["claims"]
    claim = next(c for c in claims if c["kind"] == "mapping")
    return base, next(
        d
        for d in base["decisions"]
        if d["owner_record"] == claim["owner_record"] and d["disposition"] == "SUPPORTED"
    )


def test_only_dependency_hashes_change(cohort):
    prior, _, current, _ = cohort
    successor, receipt = verify(cohort)
    assert successor["decisions"] == prior["decisions"]
    assert successor["record_inputs"] == prior["record_inputs"]
    assert successor["claims_sha256"] == prior["claims_sha256"]
    assert set(receipt["dependency_changes"]) == {
        prior["base_review"],
        refresh.EVIDENCE,
        "mappings/ingredient_mappings.sssom.tsv",
    }
    assert len(receipt["selected_mapping_evidence_unchanged"]) == 20
    assert receipt["claim_counts"] == {
        "mapping": 20,
        "identifier": 18,
        "product": 3,
        "occurrence": 10,
    }
    reviewed_products(successor, current)


@pytest.mark.parametrize("kind", ["owner", "claims", "scope_rulings", "companion_evidence"])
def test_changed_non_global_inputs_refused(cohort, kind):
    prior, _, source, _ = cohort
    current = dict(source)
    name = {
        "owner": next(iter(prior["record_inputs"])),
        "claims": prior["claims_file"],
        "scope_rulings": "reports/ingredient_bundle_20260924/scope-rulings.json",
        "companion_evidence": "reports/ingredient_bundle_20260924/review-evidence.json",
    }[kind]
    current[name] += b"\n"
    with pytest.raises(ValueError, match="Non-global input or owner changed"):
        verify(cohort, current)


@pytest.mark.parametrize("change", ["predicate", "other", "duplicate"])
def test_changed_selected_row_refused(cohort, change):
    prior, _, source, _ = cohort
    current = dict(source)
    base, decision = selected_decision(cohort)
    name = base["source_sssom"]
    _, fields, rows = _base_table(current[name])
    row = rows[decision["source_position"] - 1]
    original = "\t".join(row[f] for f in fields).encode()
    if change == "duplicate":
        current[name] += original + b"\n"
    else:
        row["predicate_id" if change == "predicate" else "other"] = "changed"
        current[name] = current[name].replace(
            original, "\t".join(row[f] for f in fields).encode(), 1
        )
    with pytest.raises(
        ValueError, match="Selected complete original row changed or became ambiguous"
    ):
        verify(cohort, current)


@pytest.mark.parametrize(
    "field,value", [("disposition", "WITHHOLD"), ("review_reason", "different scientific basis")]
)
def test_selected_decision_change_refused_even_if_rebound(cohort, field, value):
    prior, _, source, _ = cohort
    current = dict(source)
    base, decision = selected_decision(cohort)
    decision[field] = value
    proof = read_json(current[decision["review_evidence"]])
    proof["entries"][decision["evidence_key"]][field] = value
    current[decision["review_evidence"]] = refresh.encode(proof)
    base["inputs"][decision["review_evidence"]] = content_sha256(
        current[decision["review_evidence"]]
    )
    current[prior["base_review"]] = refresh.encode(base)
    with pytest.raises(ValueError, match="Selected original scientific decision changed"):
        verify(cohort, current)


def test_selected_evidence_basis_change_refused(cohort):
    _, _, source, _ = cohort
    current = dict(source)
    _, decision = selected_decision(cohort)
    proof = read_json(current[decision["review_evidence"]])
    proof["entries"][decision["evidence_key"]]["basis"] = ["invented replacement rationale"]
    current[decision["review_evidence"]] = refresh.encode(proof)
    with pytest.raises(ValueError, match="Selected original scientific evidence changed"):
        verify(cohort, current)


@pytest.mark.parametrize(
    "old,new",
    [
        (b"# predicate_semantics: skos", b"# predicate_semantics: inverted"),
        (b"http://purl.obolibrary.org/obo/CHEBI_", b"https://incorrect.example/CHEBI_"),
        (b"subject_id\tsubject_label", b"subject_id\tchanged_column"),
        (b'# mapping_date: "2026-11-01"', b'# mapping_date: "2026-02-30"'),
    ],
)
def test_semantics_columns_and_invalid_date_refused(cohort, old, new):
    _, _, source, _ = cohort
    current = dict(source)
    name = "mappings/ingredient_mappings.sssom.tsv"
    assert old in current[name]
    current[name] = current[name].replace(old, new)
    with pytest.raises(ValueError):
        verify(cohort, current)


def test_valid_but_stale_header_refused(cohort):
    _, _, source, _ = cohort
    current = dict(source)
    name = "mappings/ingredient_mappings.sssom.tsv"
    current[name] = current[name].replace(
        b'# mapping_date: "2026-11-01"', b'# mapping_date: "2026-11-02"'
    )
    current[name] = current[name].replace(
        b'# mapping_set_version: "2026-11-01"', b'# mapping_set_version: "2026-11-02"'
    )
    with pytest.raises(ValueError, match="Rule G"):
        verify(cohort, current)


@pytest.mark.parametrize("contract", refresh.CONTRACTS)
def test_profile_or_schema_change_refused(cohort, contract):
    contracts = dict(cohort[3])
    contracts[contract] += b"\n"
    with pytest.raises(ValueError, match="Packaged schema/profile contract changed"):
        verify(cohort, contracts=contracts)


@pytest.mark.parametrize("existing", [0, 1, 2])
def test_output_collisions_preserve_existing_files(tmp_path, existing):
    paths = [tmp_path / n for n in ("review.json", "receipt.json", "prior-review.json")]
    paths[existing].write_bytes(b"immutable prior artifact")
    with pytest.raises(FileExistsError):
        refresh.publish_new_files([(p, b"successor") for p in paths], lambda: None)
    assert paths[existing].read_bytes() == b"immutable prior artifact"
    assert all(not p.exists() for p in paths if p != paths[existing])


def test_input_race_removes_only_new_outputs(tmp_path):
    path = tmp_path / "new.json"

    def changed():
        raise ValueError("input changed")

    with pytest.raises(ValueError, match="input changed"):
        refresh.publish_new_files([(path, b"successor")], changed)
    assert not path.exists()


@pytest.mark.parametrize("same_index", [1, 2])
@pytest.mark.parametrize("alias", [False, True])
def test_main_duplicate_destinations_refused_before_any_write(
    tmp_path, monkeypatch, same_index, alias
):
    outputs = [tmp_path / name for name in ("review.json", "receipt.json", "prior.json")]
    outputs[same_index] = tmp_path / "unused" / ".." / "review.json" if alias else outputs[0]
    monkeypatch.setattr(
        sys,
        "argv",
        [
            str(HELPER),
            "--root",
            str(tmp_path),
            "--output",
            str(outputs[0]),
            "--receipt",
            str(outputs[1]),
            "--prior-copy",
            str(outputs[2]),
        ],
    )
    with pytest.raises(ValueError, match="Output paths collide"):
        refresh.main()
    assert list(tmp_path.iterdir()) == []
