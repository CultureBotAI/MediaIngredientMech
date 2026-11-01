"""An unrelated batch cannot renew or alter a companion scientific approval."""

import csv
import io
import subprocess
import sys
from copy import deepcopy
from datetime import date, timedelta
from pathlib import Path

import pytest
import yaml

from mediaingredientmech import ingredient_bundle_refresh as refresh
from mediaingredientmech.export.reviewed_sssom import load_review
from mediaingredientmech.ingredient_bundle_contract import (
    _base_table,
    content_sha256,
    read_json,
    reviewed_products,
)

ROOT = Path(__file__).resolve().parents[1]
HELPER = ROOT / "scripts/refresh_unchanged_cohort.py"
HISTORICAL = "reports/ingredient_bundle_20261101/review.json"
EVIDENCE = "reports/sssom_completion_20260921/mapping-evidence.json"
SOURCE = "mappings/ingredient_mappings.sssom.tsv"
EXTRA_OWNER = "data/ingredients/mapped/Refresh_Unselected_Fixture.yaml"


def table_bytes(metadata, fields, rows):
    header = "".join(
        "# " + line + "\n" for line in yaml.safe_dump(metadata, sort_keys=False).splitlines()
    )
    stream = io.StringIO()
    writer = csv.DictWriter(stream, fieldnames=fields, delimiter="\t", lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    return (header + stream.getvalue()).encode()


def advance_unselected_generation(review, sources, new_date):
    """Produce a fully valid fixture change outside the selected cohort."""
    result = dict(sources)
    base = read_json(result[review["base_review"]])
    source = base["source_sssom"]
    metadata, fields, rows = _base_table(result[source])
    rows[-1]["mapping_date"] = new_date.isoformat()
    metadata.update(mapping_date=new_date.isoformat(), mapping_set_version=new_date.isoformat())
    result[source] = table_bytes(metadata, fields, rows)
    evidence = read_json(result[EVIDENCE])
    decision = base["decisions"][-1]
    digest = content_sha256(refresh.canonical_json(rows[-1]))
    decision["row_sha256"] = digest
    evidence["entries"][decision["evidence_key"]]["row_sha256"] = digest
    result[EVIDENCE] = refresh.encode(evidence)
    base["source_sha256"] = content_sha256(result[source])
    base["inputs"][EVIDENCE] = content_sha256(result[EVIDENCE])
    result[review["base_review"]] = refresh.encode(base)
    return result


@pytest.fixture(scope="module")
def cohort():
    """Synthetic base review; no dependency on the live canonical header/date."""
    prior = read_json((ROOT / HISTORICAL).read_bytes())
    before = {p: (ROOT / p).read_bytes() for p in refresh.source_names(prior)}
    archived = read_json(
        (ROOT / "reports/ingredient_bundle_20261101/dependency-refresh.json").read_bytes()
    )
    selected = archived["selected_mapping_evidence_unchanged"]
    fields = archived["columns_unchanged"]
    rows = [deepcopy(entry["original_row"]) for entry in selected]
    baseline_date = max(date.fromisoformat(row["mapping_date"]) for row in rows) + timedelta(days=1)
    metadata = deepcopy(archived["semantic_metadata_unchanged"])
    metadata.update(
        mapping_date=baseline_date.isoformat(), mapping_set_version=baseline_date.isoformat()
    )
    extra = dict.fromkeys(fields, "")
    extra.update(
        subject_id="MIM:Refresh_Unselected_Fixture",
        subject_label="Refresh Unselected Fixture",
        predicate_id="skos:closeMatch",
        object_id="CHEBI:17126",
        object_label="carnitine",
        object_source="CHEBI",
        mapping_date=baseline_date.isoformat(),
        confidence="0.5",
    )
    rows.append(extra)
    extra_owner = b"preferred_term: Refresh Unselected Fixture\nmapping_status: MAPPED\nidentifier: CHEBI:17126\n"
    before[EXTRA_OWNER] = extra_owner
    prior["inputs"][EXTRA_OWNER] = content_sha256(extra_owner)
    decisions = []
    entries = {}
    for position, entry in enumerate(selected, 1):
        decision = deepcopy(entry["base_decision"])
        decision["source_position"] = position
        decisions.append(decision)
        entries[decision["evidence_key"]] = entry["base_evidence"]
    extra_decision = {
        "source_position": len(rows),
        "row_sha256": content_sha256(refresh.canonical_json(extra)),
        "owner_record": EXTRA_OWNER,
        "disposition": "WITHHOLD",
        "review_reason": "Synthetic unselected fixture, never scientific approval",
        "review_evidence": EVIDENCE,
        "evidence_key": "unselected-fixture",
    }
    decisions.append(extra_decision)
    entries["unselected-fixture"] = {
        k: v
        for k, v in extra_decision.items()
        if k not in {"source_position", "review_evidence", "evidence_key"}
    }
    entries["unselected-fixture"]["owner_record_sha256"] = content_sha256(extra_owner)
    before[EVIDENCE] = refresh.encode({"schema_version": 1, "entries": entries})
    before[SOURCE] = table_bytes(metadata, fields, rows)
    base = {
        "schema_version": 1,
        "scope": "Synthetic test history; no curation approval",
        "source_sssom": SOURCE,
        "source_sha256": content_sha256(before[SOURCE]),
        "inputs": {EVIDENCE: content_sha256(before[EVIDENCE])},
        "record_inputs": {**prior["record_inputs"], EXTRA_OWNER: content_sha256(extra_owner)},
        "decisions": decisions,
    }
    before[prior["base_review"]] = refresh.encode(base)
    prior["base_review_sha256"] = content_sha256(before[prior["base_review"]])
    for path in (SOURCE, EVIDENCE):
        prior["inputs"][path] = content_sha256(before[path])
    current = advance_unselected_generation(prior, before, baseline_date + timedelta(days=5))
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
        EVIDENCE,
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


def relocate_source_rows(prior, sources, order):
    """Reindex complete rows and their original proofs without approving anything."""
    result = dict(sources)
    base = read_json(result[prior["base_review"]])
    metadata, fields, rows = _base_table(result[SOURCE])
    evidence = read_json(result[EVIDENCE])
    decisions = {d["source_position"]: d for d in base["decisions"]}
    new_rows, new_decisions, entries = [], [], {}
    for position, old_index in enumerate(order, 1):
        row = deepcopy(rows[old_index])
        decision = deepcopy(decisions[old_index + 1])
        proof = deepcopy(evidence["entries"][decision["evidence_key"]])
        decision.update(source_position=position, evidence_key=str(position))
        new_rows.append(row)
        new_decisions.append(decision)
        entries[str(position)] = proof
    latest = max(row["mapping_date"] for row in new_rows)
    metadata.update(mapping_date=latest, mapping_set_version=latest)
    base["decisions"] = new_decisions
    owners = {d["owner_record"] for d in new_decisions}
    base["record_inputs"] = {path: content_sha256(result[path]) for path in owners}
    result[SOURCE] = table_bytes(metadata, fields, new_rows)
    result[EVIDENCE] = refresh.encode({"schema_version": 1, "entries": entries})
    base["source_sha256"] = content_sha256(result[SOURCE])
    base["inputs"][EVIDENCE] = content_sha256(result[EVIDENCE])
    result[prior["base_review"]] = refresh.encode(base)
    return result


def positional_cohort(cohort, operation):
    prior, original, _, contracts = cohort
    prior = deepcopy(prior)
    _, _, rows = _base_table(original[SOURCE])
    selected = list(range(len(rows) - 1))
    extra = len(rows) - 1
    orders = {
        "remove": ([extra, *selected], selected),
        "insert": (selected, [extra, *selected]),
        "reorder": ([extra, *selected], [*reversed(selected), extra]),
    }
    old_order, new_order = orders[operation]
    before = relocate_source_rows(prior, original, old_order)
    current = relocate_source_rows(prior, original, new_order)
    prior["base_review_sha256"] = content_sha256(before[prior["base_review"]])
    for path in (SOURCE, EVIDENCE):
        prior["inputs"][path] = content_sha256(before[path])
    return prior, before, current, contracts


@pytest.mark.parametrize("operation", ["insert", "remove", "reorder"])
def test_position_only_changes_preserve_scientific_evidence(cohort, tmp_path, operation):
    shifted = positional_cohort(cohort, operation)
    prior, before, current, _ = shifted
    # Both endpoints are complete native reviews, not merely unchecked hashes.
    for name, sources in (("before", before), ("after", current)):
        root = tmp_path / name
        for path, content in sources.items():
            destination = root / path
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.write_bytes(content)
        load_review(root, Path(prior["base_review"]))
    successor, receipt = verify(shifted)
    assert successor["decisions"] == prior["decisions"]
    assert successor["record_inputs"] == prior["record_inputs"]
    assert receipt["scientific_approval_added"] is False
    selected = receipt["selected_mapping_evidence_unchanged"]
    assert len(selected) == 20
    assert any(
        entry["base_decision_locations"]["before"] != entry["base_decision_locations"]["after"]
        for entry in selected
    )
    for entry in selected:
        locations = entry["base_decision_locations"]
        for sources, location in ((before, locations["before"]), (current, locations["after"])):
            proof = read_json(sources[EVIDENCE])["entries"][location["evidence_key"]]
            assert entry["base_evidence"] == proof
    reviewed_products(successor, current)


@pytest.mark.parametrize(
    "change", ["evidence", "reason", "disposition", "owner", "duplicate", "predicate", "alias"]
)
def test_position_shift_does_not_hide_scientific_changes(cohort, change):
    shifted = positional_cohort(cohort, "remove")
    prior, _, source, _ = shifted
    current = dict(source)
    base = read_json(current[prior["base_review"]])
    decision = base["decisions"][0]
    evidence = read_json(current[EVIDENCE])
    if change == "evidence":
        evidence["entries"][decision["evidence_key"]]["basis"] = ["changed rationale"]
    elif change in {"reason", "disposition"}:
        field = "review_reason" if change == "reason" else "disposition"
        decision[field] = "changed rationale" if change == "reason" else "WITHHOLD"
        evidence["entries"][decision["evidence_key"]][field] = decision[field]
    elif change == "owner":
        current[decision["owner_record"]] += b"\n"
    else:
        metadata, fields, rows = _base_table(current[SOURCE])
        if change == "duplicate":
            rows.append(deepcopy(rows[0]))
        else:
            rows[0]["predicate_id" if change == "predicate" else "other"] = "changed"
        current[SOURCE] = table_bytes(metadata, fields, rows)
    current[EVIDENCE] = refresh.encode(evidence)
    base["inputs"][EVIDENCE] = content_sha256(current[EVIDENCE])
    base["source_sha256"] = content_sha256(current[SOURCE])
    current[prior["base_review"]] = refresh.encode(base)
    with pytest.raises(ValueError, match="changed|ambiguous"):
        verify(shifted, current)


def stable_evidence_keys(prior, sources):
    result = dict(sources)
    base = read_json(result[prior["base_review"]])
    evidence = read_json(result[EVIDENCE])
    entries = {}
    for decision in base["decisions"]:
        proof = evidence["entries"][decision["evidence_key"]]
        decision["evidence_key"] = "row:" + decision["row_sha256"]
        entries[decision["evidence_key"]] = proof
    result[EVIDENCE] = refresh.encode({"schema_version": 1, "entries": entries})
    base["inputs"][EVIDENCE] = content_sha256(result[EVIDENCE])
    result[prior["base_review"]] = refresh.encode(base)
    return result


@pytest.mark.parametrize("mode", ["position_only", "key_only", "wrong_key"])
def test_independent_position_and_evidence_locators(cohort, mode):
    prior, before, current, contracts = positional_cohort(cohort, "remove")
    if mode == "position_only":
        before = stable_evidence_keys(prior, before)
        current = stable_evidence_keys(prior, current)
    else:
        current = stable_evidence_keys(prior, before)
    prior["base_review_sha256"] = content_sha256(before[prior["base_review"]])
    prior["inputs"][EVIDENCE] = content_sha256(before[EVIDENCE])
    if mode == "wrong_key":
        base = read_json(current[prior["base_review"]])
        selected = [d for d in base["decisions"] if d["disposition"] == "SUPPORTED"]
        selected[0]["evidence_key"] = selected[1]["evidence_key"]
        current[prior["base_review"]] = refresh.encode(base)
        with pytest.raises(ValueError, match="Selected original scientific evidence changed"):
            verify((prior, before, current, contracts))
        return
    successor, receipt = verify((prior, before, current, contracts))
    assert successor["decisions"] == prior["decisions"]
    assert receipt["scientific_approval_added"] is False
    for entry in receipt["selected_mapping_evidence_unchanged"]:
        old, new = (entry["base_decision_locations"][key] for key in ("before", "after"))
        stable = "evidence_key" if mode == "position_only" else "source_position"
        moving = "source_position" if mode == "position_only" else "evidence_key"
        assert old[stable] == new[stable]
        assert old[moving] != new[moving]


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


@pytest.mark.parametrize("change", ["predicate_semantics", "prefix", "column", "invalid_date"])
def test_semantics_columns_and_invalid_date_refused(cohort, change):
    _, _, source, _ = cohort
    current = dict(source)
    metadata, fields, rows = _base_table(current[SOURCE])
    if change == "predicate_semantics":
        metadata["predicate_semantics"] = "inverted"
    elif change == "prefix":
        metadata["curie_map"]["CHEBI"] = "https://incorrect.example/CHEBI_"
    elif change == "column":
        fields.append("unreviewed_column")
    else:
        year = date.fromisoformat(str(metadata["mapping_date"])).year
        metadata["mapping_date"] = f"{year}-02-30"
    current[SOURCE] = table_bytes(metadata, fields, rows)
    with pytest.raises(ValueError):
        verify(cohort, current)


def test_valid_but_stale_header_refused(cohort):
    _, _, source, _ = cohort
    current = dict(source)
    metadata, fields, rows = _base_table(current[SOURCE])
    stale = max(date.fromisoformat(r["mapping_date"]) for r in rows) + timedelta(days=1)
    metadata.update(mapping_date=stale.isoformat(), mapping_set_version=stale.isoformat())
    current[SOURCE] = table_bytes(metadata, fields, rows)
    with pytest.raises(ValueError, match="Rule G"):
        verify(cohort, current)


def test_later_header_date_still_tests_actual_rule_g(cohort):
    prior, before, current, contracts = cohort
    _, _, rows = _base_table(current[SOURCE])
    later = max(date.fromisoformat(r["mapping_date"]) for r in rows) + timedelta(days=400)
    advanced = advance_unselected_generation(prior, current, later)
    successor, _ = refresh.verify_unchanged_cohort(prior, before, advanced, contracts, contracts)
    reviewed_products(successor, advanced)
    metadata, fields, rows = _base_table(advanced[SOURCE])
    metadata.update(
        mapping_date=(later + timedelta(days=1)).isoformat(),
        mapping_set_version=(later + timedelta(days=1)).isoformat(),
    )
    advanced[SOURCE] = table_bytes(metadata, fields, rows)
    with pytest.raises(ValueError, match="Rule G"):
        verify(cohort, advanced)


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
            "--baseline",
            "HEAD",
            "--prior-review",
            "history/prior.json",
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


@pytest.mark.parametrize("pair", [(0, 1), (0, 2), (1, 2)])
def test_main_symlink_alias_destinations_refused_without_writes(tmp_path, pair):
    real = tmp_path / "real"
    real.mkdir()
    alias = tmp_path / "alias"
    alias.symlink_to(real, target_is_directory=True)
    outputs = [real / name for name in ("review.json", "receipt.json", "prior.json")]
    outputs[pair[1]] = alias / outputs[pair[0]].name
    with pytest.raises(ValueError, match="Output paths collide"):
        refresh.main(
            [
                "--root",
                str(tmp_path),
                "--baseline",
                "HEAD",
                "--prior-review",
                "history/prior.json",
                "--output",
                str(outputs[0]),
                "--receipt",
                str(outputs[1]),
                "--prior-copy",
                str(outputs[2]),
            ]
        )
    assert list(real.iterdir()) == []
    assert alias.is_symlink()


def test_reusable_cli_across_two_baselines_prior_paths_and_later_dates(cohort, tmp_path):
    prior, before, current, contracts = cohort

    def write_sources(sources):
        for name, content in sources.items():
            path = tmp_path / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(content)

    def git(*args):
        return subprocess.check_output(["git", "-C", str(tmp_path), *args]).decode().strip()

    def commit(message):
        git("add", ".")
        git(
            "-c",
            "user.name=Fixture",
            "-c",
            "user.email=fixture@example.invalid",
            "commit",
            "-qm",
            message,
        )
        return git("rev-parse", "HEAD")

    def invoke(baseline, old, output):
        args = [
            sys.executable,
            str(HELPER),
            "--root",
            str(tmp_path),
            "--baseline",
            baseline,
            "--prior-review",
            old,
            "--output",
            output,
            "--receipt",
            output + ".receipt.json",
            "--prior-copy",
            output + ".prior.json",
        ]
        completed = subprocess.run(args, cwd=ROOT, capture_output=True, text=True)
        assert completed.returncode == 0, completed.stderr
        return read_json((tmp_path / output).read_bytes()), read_json(
            (tmp_path / (output + ".receipt.json")).read_bytes()
        )

    first_path = "history/first.json"
    write_sources(before | contracts | {first_path: refresh.encode(prior)})
    git("init", "-q")
    first_baseline = commit("Synthetic initial reviewed inputs")
    write_sources(current)
    first, first_receipt = invoke(first_baseline, first_path, "history/second.json")
    assert first_receipt["historical_commit"] == first_baseline
    assert first_receipt["prior_review"] == first_path
    assert (tmp_path / first_path).read_bytes() == refresh.encode(prior)
    second_baseline = commit("Synthetic unchanged-cohort successor")
    _, _, rows = _base_table(current[SOURCE])
    later = max(date.fromisoformat(r["mapping_date"]) for r in rows) + timedelta(days=400)
    advanced = advance_unselected_generation(first, current, later)
    write_sources(advanced)
    second, second_receipt = invoke(second_baseline, "history/second.json", "history/third.json")
    assert second_receipt["historical_commit"] == second_baseline != first_baseline
    assert second_receipt["prior_review"] == "history/second.json"
    assert second_receipt["header_date_changes"]["mapping_date"]["after"] == later.isoformat()
    assert second["decisions"] == prior["decisions"] == first["decisions"]
    assert second["record_inputs"] == prior["record_inputs"]
    assert (tmp_path / "history/third.json.prior.json").read_bytes() == refresh.encode(first)
    reviewed_products(second, advanced)


def test_original_review_scope_change_refused(cohort):
    prior, _, source, _ = cohort
    current = dict(source)
    base = read_json(current[prior["base_review"]])
    base["scope"] = "Expanded scope is not an unchanged dependency refresh"
    current[prior["base_review"]] = refresh.encode(base)
    with pytest.raises(ValueError, match="Original review scope or contract changed"):
        verify(cohort, current)


@pytest.mark.parametrize("replacement", ["symlink", "regular"])
@pytest.mark.parametrize("callback_raises", [False, True])
def test_reserved_output_replacement_never_overwrites_or_deletes_other_writer(
    tmp_path, replacement, callback_raises
):
    victim = tmp_path / "immutable-review.json"
    victim.write_bytes(b"original immutable review")
    outputs = [
        tmp_path / name for name in ("new-review.json", "new-receipt.json", "prior-copy.json")
    ]
    replaced = outputs[0]

    def replace_reservation():
        replaced.unlink()
        if replacement == "symlink":
            replaced.symlink_to(victim)
        else:
            replaced.write_bytes(b"competing writer's output")
        if callback_raises:
            raise ValueError("input snapshot changed")

    with pytest.raises(ValueError, match="input snapshot changed|Output reservation changed"):
        refresh.publish_new_files([(p, b"our new bytes") for p in outputs], replace_reservation)
    assert victim.read_bytes() == b"original immutable review"
    if replacement == "symlink":
        assert replaced.is_symlink()
        assert replaced.readlink() == victim
    else:
        assert replaced.read_bytes() == b"competing writer's output"
    assert all(not p.exists() for p in outputs[1:])
