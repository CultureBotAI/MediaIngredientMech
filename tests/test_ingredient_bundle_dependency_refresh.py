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


@pytest.fixture
def form_projection(cohort, tmp_path):
    """A real Git baseline and native receipt, outside the unchanged cohort."""
    from mediaingredientmech.validation import mapping_change_receipts as chain

    prior, before, current, contracts = deepcopy(cohort)
    old_owner = before.pop(EXTRA_OWNER)
    current.pop(EXTRA_OWNER)
    prior["inputs"].pop(EXTRA_OWNER)
    new_owner = old_owner + b"# source form correction fixture\n"
    for name in (refresh.POLICY_SIDECAR, refresh.POLICY_BASELINE):
        before[name] = current[name] = b"fixture\n"
        prior["inputs"][name] = content_sha256(before[name])
    fixed = dict(
        schema_version=1,
        policy_version="owned-name-policy-v1",
        approval="NONE: fixture",
        scope="Synthetic source-derived policy",
        decisions=[],
        policy_evidence=[],
        producer_revision="a" * 40,
        generation_manifest_sha256="a" * 64,
        generation_receipt_sha256="b" * 64,
        source_receipt_sha256="c" * 64,
        sssom_before_sha256="d" * 64,
        baseline_before_sha256="e" * 64,
    )
    old = dict(
        fixed,
        artifacts={
            p: content_sha256(before[p])
            for p in (SOURCE, refresh.POLICY_SIDECAR, refresh.POLICY_BASELINE)
        },
        source_owner_sha256={**prior["record_inputs"], EXTRA_OWNER: content_sha256(old_owner)},
    )
    before[refresh.POLICY_MANIFEST] = refresh.encode(old)
    prior["inputs"][refresh.POLICY_MANIFEST] = content_sha256(before[refresh.POLICY_MANIFEST])
    before[prior["base_review"]] = refresh.encode(read_json(before[prior["base_review"]]))
    prior["base_review_sha256"] = content_sha256(before[prior["base_review"]])
    metadata, fields, old_rows = _base_table(before[SOURCE])
    _, _, new_rows = _base_table(current[SOURCE])
    old_sha, new_sha = content_sha256(before[SOURCE]), content_sha256(current[SOURCE])
    position = len(old_rows)
    link = dict(
        schema_version=1,
        batch="form-fixture",
        sequence=1,
        approval="NONE: no approval",
        issue="https://github.com/CultureBotAI/MediaIngredientMech/issues/901",
        before_sha256=old_sha,
        after_sha256=new_sha,
        before_row_count=position,
        after_row_count=position,
        changed_rows=1,
        added_rows=0,
        removed_rows=0,
        position_map=list(range(1, position + 1)),
        touched_subjects=[old_rows[-1]["subject_id"]],
        changes=[
            dict(
                kind="changed",
                before_position=position,
                after_position=position,
                before=old_rows[-1],
                after=new_rows[-1],
            )
        ],
        records=[
            dict(
                source_record=EXTRA_OWNER,
                before_yaml_sha256=content_sha256(old_owner),
                after_yaml_sha256=content_sha256(new_owner),
                shape="hydrate_parent_predicate",
                change="Synthetic form correction",
                verification="Synthetic test evidence",
            )
        ],
    )
    update = dict(
        issue=901,
        scope="One form fixture",
        approval="NONE: source-only",
        prior_manifest_sha256=content_sha256(before[refresh.POLICY_MANIFEST]),
        source_record=EXTRA_OWNER,
        owner_before_sha256=content_sha256(old_owner),
        owner_after_sha256=content_sha256(new_owner),
        source_receipt="/historical/source-receipt.json",
        source_receipt_sha256="1" * 64,
        generation_manifest_sha256="2" * 64,
        generation_receipt_sha256="3" * 64,
        sssom_before_sha256=old_sha,
        sssom_after_sha256=new_sha,
        sidecar_sha256=content_sha256(current[refresh.POLICY_SIDECAR]),
        baseline_sha256=content_sha256(current[refresh.POLICY_BASELINE]),
    )
    new = deepcopy(old)
    new["artifacts"][SOURCE] = new_sha
    new["source_owner_sha256"][EXTRA_OWNER] = content_sha256(new_owner)
    new["form_projection_updates"] = [update]
    current[refresh.POLICY_MANIFEST] = refresh.encode(new)
    base = read_json(current[prior["base_review"]])
    base["record_inputs"][EXTRA_OWNER] = content_sha256(new_owner)
    evidence = read_json(current[EVIDENCE])
    evidence["entries"]["unselected-fixture"]["owner_record_sha256"] = content_sha256(new_owner)
    current[EVIDENCE] = refresh.encode(evidence)
    base["inputs"][EVIDENCE] = content_sha256(current[EVIDENCE])
    current[prior["base_review"]] = refresh.encode(base)

    def write(name, raw):
        path = tmp_path / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(raw)

    for name, raw in before.items() | contracts.items():
        write(name, raw)
    write(EXTRA_OWNER, old_owner)
    write("history/prior.json", refresh.encode(prior))
    write(
        chain.BASELINE, refresh.encode(dict(schema_version=1, source_sha256=old_sha, rows=old_rows))
    )
    for name in (chain.TRAIT_REFRESH, chain.PARENT_REFRESH):
        write(
            name,
            refresh.encode(
                dict(
                    schema_version=1,
                    before_sha256=old_sha,
                    after_sha256=old_sha,
                    row_count=position,
                    changed_rows=0,
                    changes=[],
                )
            ),
        )
    for name in (
        "src/mediaingredientmech/ingredient_bundle_refresh.py",
        "src/mediaingredientmech/validation/mapping_change_receipts.py",
    ):
        write(name, (ROOT / name).read_bytes())
    subprocess.run(["git", "init", "-q", str(tmp_path)], check=True)
    subprocess.run(["git", "-C", str(tmp_path), "add", "."], check=True)
    subprocess.run(
        [
            "git",
            "-C",
            str(tmp_path),
            "-c",
            "user.name=Fixture",
            "-c",
            "user.email=fixture@example.invalid",
            "commit",
            "-qm",
            "Immutable fixture baseline",
        ],
        check=True,
    )
    baseline = (
        subprocess.check_output(["git", "-C", str(tmp_path), "rev-parse", "HEAD"]).decode().strip()
    )
    for name, raw in current.items():
        write(name, raw)
    write(EXTRA_OWNER, new_owner)
    receipt_path = chain.RECEIPTS_DIR + "/form-fixture.json"
    write(receipt_path, refresh.encode(link))
    context = refresh.FormProjectionContext(
        tmp_path, baseline, content_sha256(current[refresh.POLICY_MANIFEST])
    )
    chain.verify_mapping_chain(tmp_path)
    return prior, before, current, contracts, context, receipt_path


def verify_projection(fixture, context=None):
    prior, before, current, contracts, expected, _ = fixture
    return refresh.verify_unchanged_cohort(
        prior,
        before,
        current,
        contracts,
        contracts,
        form_projection=expected if context is None else context,
    )


def test_native_form_projection_preserves_all_companion_science(form_projection):
    prior, _, current, _, _, _ = form_projection
    successor, audit = verify_projection(form_projection)
    assert successor["decisions"] == prior["decisions"]
    assert successor["record_inputs"] == prior["record_inputs"]
    assert successor["inputs"][refresh.POLICY_MANIFEST] == content_sha256(
        current[refresh.POLICY_MANIFEST]
    )
    assert audit["form_projection"]["scientific_approval_added"] is False
    assert "not replayed" in audit["form_projection"]["attribution_contract"]
    assert set(audit["form_projection"]["input_sha256"]) >= {EXTRA_OWNER, SOURCE}
    reviewed_products(successor, current)


@pytest.mark.parametrize("context", ["missing", "wrong-pin", "arbitrary"])
def test_changed_manifest_requires_explicit_context_and_pin(form_projection, context):
    prior, before, current, contracts, actual, _ = form_projection
    supplied = {
        "missing": None,
        "wrong-pin": refresh.FormProjectionContext(actual.root, actual.baseline, "0" * 64),
        "arbitrary": {"manifest_sha256": actual.manifest_sha256},
    }[context]
    with pytest.raises(ValueError, match="Non-global|Form projection"):
        refresh.verify_unchanged_cohort(
            prior, before, current, contracts, contracts, form_projection=supplied
        )


@pytest.mark.parametrize(
    "mutation",
    [
        "unknown-field",
        "schema",
        "policy",
        "policy-evidence",
        "generation-attribution",
        "prior-hash",
        "owner-before",
        "owner-after",
        "canonical-before",
        "canonical-after",
        "sidecar",
        "baseline",
        "extra-owner",
        "extra-update-field",
        "missing-update-field",
        "update-history",
        "extra-owner-record",
        "extra-touched-subject",
        "receipt-bytes",
        "actual-owner",
    ],
)
def test_coordinated_pinned_manifest_corruption_refused(form_projection, mutation):
    prior, before, current, contracts, context, receipt_path = form_projection
    doc = read_json(current[refresh.POLICY_MANIFEST])
    update = doc["form_projection_updates"][0]
    if mutation == "unknown-field":
        doc["unreviewed"] = "field"
    elif mutation == "schema":
        doc["schema_version"] = True
    elif mutation == "policy":
        doc["policy_version"] = "other"
    elif mutation == "policy-evidence":
        doc["policy_evidence"] = ["changed"]
    elif mutation == "generation-attribution":
        doc["generation_manifest_sha256"] = "0" * 64
    elif mutation == "prior-hash":
        update["prior_manifest_sha256"] = "0" * 64
    elif mutation == "owner-before":
        update["owner_before_sha256"] = "0" * 64
    elif mutation == "owner-after":
        update["owner_after_sha256"] = "0" * 64
    elif mutation == "canonical-before":
        update["sssom_before_sha256"] = "0" * 64
    elif mutation == "canonical-after":
        update["sssom_after_sha256"] = "0" * 64
    elif mutation == "sidecar":
        update["sidecar_sha256"] = "0" * 64
    elif mutation == "baseline":
        update["baseline_sha256"] = "0" * 64
    elif mutation == "extra-owner":
        doc["source_owner_sha256"][next(iter(prior["record_inputs"]))] = "0" * 64
    elif mutation == "extra-update-field":
        update["invented"] = "field"
    elif mutation == "missing-update-field":
        update.pop("generation_receipt_sha256")
    elif mutation == "update-history":
        doc["form_projection_updates"].append(deepcopy(update))
    elif mutation == "actual-owner":
        (context.root / EXTRA_OWNER).write_bytes(b"wrong owner")
    else:
        path = context.root / receipt_path
        link = read_json(path.read_bytes())
        if mutation == "extra-owner-record":
            record = deepcopy(link["records"][0])
            record["source_record"] = next(iter(prior["record_inputs"]))
            link["records"].append(record)
        elif mutation == "extra-touched-subject":
            link["touched_subjects"].append("MIM:Other")
        else:
            link["changes"][0]["after"]["object_label"] = "corrupted"
        path.write_bytes(refresh.encode(link))
    current[refresh.POLICY_MANIFEST] = refresh.encode(doc)
    (context.root / refresh.POLICY_MANIFEST).write_bytes(current[refresh.POLICY_MANIFEST])
    pin = refresh.FormProjectionContext(
        context.root, context.baseline, content_sha256(current[refresh.POLICY_MANIFEST])
    )
    with pytest.raises(ValueError):
        verify_projection(form_projection, pin)


def form_argv(fixture, *, pin=True):
    _, _, _, _, context, _ = fixture
    argv = [
        "--root",
        str(context.root),
        "--baseline",
        context.baseline,
        "--prior-review",
        "history/prior.json",
        "--output",
        "history/successor.json",
        "--receipt",
        "history/audit.json",
        "--prior-copy",
        "history/copy.json",
    ]
    if pin:
        argv += ["--form-projection-manifest-sha256", context.manifest_sha256]
    return argv


def test_cli_native_projection_with_explicit_pin(form_projection):
    refresh.main(form_argv(form_projection))
    root = form_projection[4].root
    successor = read_json((root / "history/successor.json").read_bytes())
    assert successor["decisions"] == form_projection[0]["decisions"]
    assert read_json((root / "history/audit.json").read_bytes())["form_projection"][
        "receipt_paths"
    ] == [form_projection[5]]


@pytest.mark.parametrize("drift", ["owner", "receipt", "new-receipt"])
def test_projection_proof_rechecked_after_reservation(form_projection, monkeypatch, drift):
    root = form_projection[4].root
    path = root / form_projection[5]
    real = refresh.publish_new_files

    def publish(outputs, check):
        def changed():
            if drift == "owner":
                (root / EXTRA_OWNER).write_bytes(b"late owner drift")
            elif drift == "receipt":
                path.write_bytes(path.read_bytes() + b"\n")
            else:
                path.with_name("late.json").write_bytes(path.read_bytes())
            check()

        return real(outputs, changed)

    monkeypatch.setattr(refresh, "publish_new_files", publish)
    with pytest.raises(ValueError):
        refresh.main(form_argv(form_projection))
    assert not any(
        (root / "history" / name).exists() for name in ["successor.json", "audit.json", "copy.json"]
    )


def test_cohort_owner_cannot_use_projection_exception(form_projection):
    prior, before, current, contracts, context, _ = form_projection
    changed = read_json(current[refresh.POLICY_MANIFEST])
    changed["form_projection_updates"][0]["source_record"] = next(iter(prior["record_inputs"]))
    current[refresh.POLICY_MANIFEST] = refresh.encode(changed)
    (context.root / refresh.POLICY_MANIFEST).write_bytes(current[refresh.POLICY_MANIFEST])
    context = refresh.FormProjectionContext(
        context.root, context.baseline, content_sha256(current[refresh.POLICY_MANIFEST])
    )
    with pytest.raises(ValueError, match="belongs to companion"):
        verify_projection(form_projection, context)


@pytest.mark.parametrize("mutate_prefix", [False, True])
def test_preexisting_projection_prefix_preserved_exactly(form_projection, mutate_prefix):
    prior, before, current, contracts, context, _ = form_projection
    old = read_json(before[refresh.POLICY_MANIFEST])
    new = read_json(current[refresh.POLICY_MANIFEST])
    historical = {"historical": "Already reviewed original attribution retained verbatim"}
    old["form_projection_updates"] = [historical]
    before[refresh.POLICY_MANIFEST] = refresh.encode(old)
    new["form_projection_updates"].insert(0, deepcopy(historical))
    new["form_projection_updates"][-1]["prior_manifest_sha256"] = content_sha256(
        before[refresh.POLICY_MANIFEST]
    )
    prior["inputs"][refresh.POLICY_MANIFEST] = content_sha256(before[refresh.POLICY_MANIFEST])
    (context.root / refresh.POLICY_MANIFEST).write_bytes(before[refresh.POLICY_MANIFEST])
    (context.root / "history/prior.json").write_bytes(refresh.encode(prior))
    subprocess.run(
        ["git", "-C", str(context.root), "add", refresh.POLICY_MANIFEST, "history/prior.json"],
        check=True,
    )
    subprocess.run(
        [
            "git",
            "-C",
            str(context.root),
            "-c",
            "user.name=Fixture",
            "-c",
            "user.email=fixture@example.invalid",
            "commit",
            "-qm",
            "Reviewed prior projection prefix",
        ],
        check=True,
    )
    baseline = (
        subprocess.check_output(["git", "-C", str(context.root), "rev-parse", "HEAD"])
        .decode()
        .strip()
    )
    if mutate_prefix:
        new["form_projection_updates"][0]["historical"] = "Silently rewritten provenance"
    current[refresh.POLICY_MANIFEST] = refresh.encode(new)
    (context.root / refresh.POLICY_MANIFEST).write_bytes(current[refresh.POLICY_MANIFEST])
    context = refresh.FormProjectionContext(
        context.root, baseline, content_sha256(current[refresh.POLICY_MANIFEST])
    )
    if mutate_prefix:
        with pytest.raises(ValueError, match="preserved history"):
            verify_projection(form_projection, context)
    else:
        successor, _ = verify_projection(form_projection, context)
        assert successor["decisions"] == prior["decisions"]


def test_same_bytes_owner_alias_after_reservation_refused(form_projection, monkeypatch):
    root = form_projection[4].root
    real = refresh.publish_new_files
    owner = root / EXTRA_OWNER
    unrelated = root / "unrelated.yaml"
    unrelated.write_bytes(owner.read_bytes())

    def publish(outputs, check):
        def changed():
            owner.unlink()
            owner.symlink_to(unrelated)
            check()

        return real(outputs, changed)

    monkeypatch.setattr(refresh, "publish_new_files", publish)
    with pytest.raises(ValueError, match="aliased proof"):
        refresh.main(form_argv(form_projection))
    assert unrelated.read_bytes() == owner.read_bytes()
    assert not any(
        (root / "history" / name).exists() for name in ["successor.json", "audit.json", "copy.json"]
    )


@pytest.mark.parametrize("manifest_state", ["absent", "unchanged"])
@pytest.mark.parametrize("pin", [None, "0" * 64, "not-a-sha256"])
def test_cli_explicit_projection_requires_manifest_transition(
    cohort, tmp_path, manifest_state, pin
):
    prior, before, current, contracts = deepcopy(cohort)
    if manifest_state == "unchanged":
        # Ordinary unchanged input bytes do not request a projection review.
        manifest = refresh.encode({"fixture": "unchanged policy input"})
        before[refresh.POLICY_MANIFEST] = current[refresh.POLICY_MANIFEST] = manifest
        prior["inputs"][refresh.POLICY_MANIFEST] = content_sha256(manifest)

    def write_sources(sources):
        for name, content in sources.items():
            path = tmp_path / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(content)

    def git(*args):
        return subprocess.check_output(["git", "-C", str(tmp_path), *args]).decode().strip()

    write_sources(before | contracts | {"history/prior.json": refresh.encode(prior)})
    git("init", "-q")
    git("add", ".")
    git(
        "-c",
        "user.name=Fixture",
        "-c",
        "user.email=fixture@example.invalid",
        "commit",
        "-qm",
        "Synthetic unchanged-cohort inputs",
    )
    baseline = git("rev-parse", "HEAD")
    write_sources(current)
    outputs = ["history/successor.json", "history/audit.json", "history/copy.json"]
    argv = [
        sys.executable,
        "-B",
        str(HELPER),
        "--root",
        str(tmp_path),
        "--baseline",
        baseline,
        "--prior-review",
        "history/prior.json",
        "--output",
        outputs[0],
        "--receipt",
        outputs[1],
        "--prior-copy",
        outputs[2],
    ]
    if pin is not None:
        argv += ["--form-projection-manifest-sha256", pin]
    completed = subprocess.run(argv, cwd=ROOT, capture_output=True, text=True)
    if pin is None:
        assert completed.returncode == 0, completed.stderr
        successor = read_json((tmp_path / outputs[0]).read_bytes())
        audit = read_json((tmp_path / outputs[1]).read_bytes())
        assert successor["decisions"] == prior["decisions"]
        assert successor["record_inputs"] == prior["record_inputs"]
        assert "form_projection" not in audit
        assert (tmp_path / outputs[2]).read_bytes() == refresh.encode(prior)
    else:
        assert completed.returncode != 0, completed.stdout
        assert "Form projection requested without a changed policy manifest" in completed.stderr
        assert all(not (tmp_path / name).exists() for name in outputs)
    assert all((tmp_path / name).read_bytes() == data for name, data in current.items())
