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


def registry_owner_documents():
    """Real frozen preimages; no optional LinkML runtime or live corpus dependency."""
    import ast

    from mediaingredientmech import registry_correction_refresh as registry

    constants = {
        item.targets[0].id: ast.literal_eval(item.value)
        for item in ast.parse((ROOT / "scripts/correct_izalpinin_cas.py").read_text()).body
        if isinstance(item, ast.Assign)
        and isinstance(item.targets[0], ast.Name)
        and item.targets[0].id in {"VERIFICATION", "CHANGE", "EVIDENCE_SOURCE"}
    }
    packets = {name: read_json((ROOT / name).read_bytes()) for name in registry.PACKETS}
    node_packet = packets[registry.NODE_PACKET]
    old = {
        name: (ROOT / item["preimage"]).read_bytes() for name, item in node_packet["owners"].items()
    }
    old[registry.CAS_OWNER] = (
        ROOT / "reports/izalpinin_registry_753_20261101/preimages/Izalpinin.yaml"
    ).read_bytes()
    stamp = "2026-11-02T02:00:00+00:00"
    new = {}
    for name, raw in old.items():
        data = yaml.safe_load(raw)
        if name == registry.CAS_OWNER:
            action, curator, changes = "CORRECTED_EXISTING_CAS_VALUE", "claude", constants["CHANGE"]
            data["identifier"] = data["ontology_mapping"]["ontology_id"] = "cas:480-14-8"
            data["ontology_mapping"]["evidence"].append(
                dict(
                    evidence_type="DATABASE_MATCH",
                    source=constants["EVIDENCE_SOURCE"],
                    notes=constants["VERIFICATION"],
                )
            )
            data["chemical_properties"].update(
                cas_rn="480-14-8", data_source=constants["EVIDENCE_SOURCE"], retrieval_date=stamp
            )
        else:
            action, curator = "REMOVED_STALE_KG_MICROBE_NODE_ID", "Codex"
            node, identity = data.pop("kg_microbe_node_id"), data["identifier"]
            changes = (
                f"Removed stale kg_microbe_node_id {node} after the recorded "
                f"identity correction to {identity} (#870). Preserved primary "
                "identity, ontology mapping, chemistry, synonyms, roles, counts, status "
                "and existing tombstone metadata. Source-only correction: the fixed "
                "unified snapshot still contains the documented 21 stale cells in 15 "
                "rows; #870 remains open. No mapping, role or release approval. "
                f"Decision: {node_packet['decision_url']}; evidence: {registry.NODE_PACKET} "
                f"sha256={registry.PACKETS[registry.NODE_PACKET]}."
            )
        data["curation_history"].append(
            dict(
                timestamp=stamp,
                curator=curator,
                action=action,
                changes=changes,
                previous_status=data["mapping_status"],
                new_status=data["mapping_status"],
                llm_assisted=True,
                llm_model="gpt-6",
            )
        )
        new[name] = yaml.safe_dump(data, sort_keys=False, allow_unicode=True).encode()
    return old, new, packets


@pytest.fixture
def registry_correction(cohort, tmp_path):
    """Complete native history, old FORM history, exact seven source preimages."""
    from mediaingredientmech import registry_correction_refresh as registry
    from mediaingredientmech.curie import mim_curie_for_stem
    from mediaingredientmech.validation import mapping_change_receipts as chain

    prior, before, _, contracts = deepcopy(cohort)
    before.pop(EXTRA_OWNER)
    prior["inputs"].pop(EXTRA_OWNER)
    old_owners, new_owners, packets = registry_owner_documents()
    metadata, fields, rows = _base_table(before[SOURCE])
    rows[-1] = read_json(
        (
            ROOT / "reports/izalpinin_registry_753_20261101/preimages/mapping-before.json"
        ).read_bytes()
    )["row"]
    positions = {len(rows): registry.CAS_OWNER}
    # Four active node owners produce five rows, including the thiamine registry sibling.
    for name in list(registry.NODE_OWNERS)[:4]:
        data = yaml.safe_load(old_owners[name])
        row = dict.fromkeys(fields, "")
        row.update(
            subject_id=mim_curie_for_stem(Path(name).stem),
            subject_label=data["preferred_term"],
            object_id=data["identifier"],
            object_label=data["preferred_term"],
            predicate_id="skos:exactMatch",
            mapping_date="2026-05-02",
            object_source="fixture",
        )
        rows.append(row)
        positions[len(rows)] = name
        if "02_Thiamine" in name:
            rows.append(dict(row, object_id="CHEBI:9532", predicate_id="skos:broadMatch"))
            positions[len(rows)] = name
    latest = max(r["mapping_date"] for r in rows)
    metadata.update(mapping_date=latest, mapping_set_version=latest)
    before[SOURCE] = table_bytes(metadata, fields, rows)
    base = read_json(before[prior["base_review"]])
    evidence = read_json(before[EVIDENCE])
    base["decisions"] = base["decisions"][:-1]
    base["record_inputs"].pop(EXTRA_OWNER)
    evidence["entries"].pop("unselected-fixture")
    for position, owner in positions.items():
        key = "registry-fixture-" + str(position)
        decision = dict(
            source_position=position,
            owner_record=owner,
            row_sha256=content_sha256(refresh.canonical_json(rows[position - 1])),
            disposition="WITHHOLD",
            review_reason="Fixture retains scientific hold",
            review_evidence=EVIDENCE,
            evidence_key=key,
        )
        base["decisions"].append(decision)
        proof = {
            k: v
            for k, v in decision.items()
            if k not in {"source_position", "review_evidence", "evidence_key"}
        }
        proof["owner_record_sha256"] = content_sha256(old_owners[owner])
        evidence["entries"][key] = proof
        base["record_inputs"][owner] = content_sha256(old_owners[owner])
    before[EVIDENCE] = refresh.encode(evidence)
    base["inputs"][EVIDENCE] = content_sha256(before[EVIDENCE])
    base["source_sha256"] = content_sha256(before[SOURCE])
    before[prior["base_review"]] = refresh.encode(base)
    for name in (SOURCE, EVIDENCE):
        prior["inputs"][name] = content_sha256(before[name])
    prior["base_review_sha256"] = content_sha256(before[prior["base_review"]])
    for name in (refresh.POLICY_SIDECAR, refresh.POLICY_BASELINE):
        before[name] = b"fixture policy\n"
        prior["inputs"][name] = content_sha256(before[name])
    manifest = dict(
        schema_version=1,
        policy_version="owned-name-policy-v1",
        approval="NONE: fixture",
        scope="Synthetic history, not approval",
        decisions=[],
        policy_evidence=[],
        producer_revision="a" * 40,
        generation_manifest_sha256="a" * 64,
        generation_receipt_sha256="b" * 64,
        source_receipt_sha256="c" * 64,
        sssom_before_sha256="d" * 64,
        baseline_before_sha256="e" * 64,
        source_owner_sha256={p: content_sha256(raw) for p, raw in old_owners.items()},
        artifacts={
            p: content_sha256(before[p])
            for p in (SOURCE, refresh.POLICY_SIDECAR, refresh.POLICY_BASELINE)
        },
        form_projection_updates=[
            {"history": "First immutable FORM update"},
            {"history": "Second immutable FORM update"},
        ],
    )
    before[refresh.POLICY_MANIFEST] = refresh.encode(manifest)
    prior["inputs"][refresh.POLICY_MANIFEST] = content_sha256(before[refresh.POLICY_MANIFEST])
    current = dict(before)
    new_rows = deepcopy(rows)
    cas_position = next(p for p, n in positions.items() if n == registry.CAS_OWNER)
    new_rows[cas_position - 1].update(
        object_id="cas:480-14-8",
        other="CAS:480-14-8",
        mapping_date="2026-11-02",
        source="MIM:CultureBotHT|MIM:" + registry.CAS_SOURCE + "|MIM:curator=claude",
        validation_method="",
    )
    metadata.update(mapping_date="2026-11-02", mapping_set_version="2026-11-02")
    current[SOURCE] = table_bytes(metadata, fields, new_rows)
    new_base, new_evidence = deepcopy(base), deepcopy(evidence)
    for decision in new_base["decisions"]:
        owner = decision["owner_record"]
        if owner not in old_owners:
            continue
        decision["row_sha256"] = content_sha256(
            refresh.canonical_json(new_rows[decision["source_position"] - 1])
        )
        item = new_evidence["entries"][decision["evidence_key"]]
        item.update(
            row_sha256=decision["row_sha256"], owner_record_sha256=content_sha256(new_owners[owner])
        )
        new_base["record_inputs"][owner] = content_sha256(new_owners[owner])
    current[EVIDENCE] = refresh.encode(new_evidence)
    new_base["inputs"][EVIDENCE] = content_sha256(current[EVIDENCE])
    new_base["source_sha256"] = content_sha256(current[SOURCE])
    current[prior["base_review"]] = refresh.encode(new_base)
    update = dict(
        issue=753,
        scope="Bounded CAS correction and six source pointer removals",
        approval="NONE: retain WITHHOLD",
        prior_manifest_sha256=content_sha256(before[refresh.POLICY_MANIFEST]),
        source_record=registry.CAS_OWNER,
        owner_before_sha256=content_sha256(old_owners[registry.CAS_OWNER]),
        owner_after_sha256=content_sha256(new_owners[registry.CAS_OWNER]),
        source_receipt="/captured/source.json",
        source_receipt_sha256="1" * 64,
        generation_manifest_sha256="2" * 64,
        generation_receipt_sha256="3" * 64,
        sssom_before_sha256=content_sha256(before[SOURCE]),
        sssom_after_sha256=content_sha256(current[SOURCE]),
        sidecar_sha256=content_sha256(before[refresh.POLICY_SIDECAR]),
        baseline_sha256=content_sha256(before[refresh.POLICY_BASELINE]),
    )
    new_manifest = deepcopy(manifest)
    new_manifest["registry_correction_updates"] = [update]
    new_manifest["artifacts"][SOURCE] = content_sha256(current[SOURCE])
    new_manifest["source_owner_sha256"][registry.CAS_OWNER] = content_sha256(
        new_owners[registry.CAS_OWNER]
    )
    current[refresh.POLICY_MANIFEST] = refresh.encode(new_manifest)

    def write(name, raw):
        path = tmp_path / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(raw)

    for name, raw in (before | contracts | old_owners).items():
        write(name, raw)
    write("history/prior.json", refresh.encode(prior))
    for name in registry.VERIFIERS + registry.FORM_REVIEWS:
        write(name, (ROOT / name).read_bytes())
    for name, packet in packets.items():
        write(name, (ROOT / name).read_bytes())
        for path in packet["files"]:
            write(path, (ROOT / path).read_bytes())
    # A metadata-only historical receipt proves that a self-consistent rewrite
    # of the prefix must still be rejected against the durable Git baseline.
    prehistory_sha = content_sha256(before[SOURCE] + b"# historical metadata\n")
    write(
        chain.BASELINE,
        refresh.encode(dict(schema_version=1, source_sha256=prehistory_sha, rows=rows)),
    )
    for name in (chain.TRAIT_REFRESH, chain.PARENT_REFRESH):
        write(
            name,
            refresh.encode(
                dict(
                    schema_version=1,
                    before_sha256=prehistory_sha,
                    after_sha256=prehistory_sha,
                    row_count=len(rows),
                    changed_rows=0,
                    changes=[],
                )
            ),
        )
    prefix = dict(
        schema_version=1,
        sequence=1,
        batch="historical-prefix",
        approval="NONE: fixture",
        issue="fixture",
        before_sha256=prehistory_sha,
        after_sha256=content_sha256(before[SOURCE]),
        before_row_count=len(rows),
        after_row_count=len(rows),
        changed_rows=0,
        added_rows=0,
        removed_rows=0,
        position_map=list(range(1, len(rows) + 1)),
        touched_subjects=[],
        changes=[],
        records=[],
    )
    write(chain.RECEIPTS_DIR + "/prefix.json", refresh.encode(prefix))
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
            "Durable prefix",
        ],
        check=True,
    )
    baseline = (
        subprocess.check_output(["git", "-C", str(tmp_path), "rev-parse", "HEAD"]).decode().strip()
    )
    for name, raw in (current | new_owners).items():
        write(name, raw)
    receipt_path = chain.RECEIPTS_DIR + "/registry-fixture.json"
    receipt = dict(
        prefix,
        sequence=2,
        batch="registry-correction",
        issue="https://github.com/CultureBotAI/MediaIngredientMech/issues/753",
        before_sha256=content_sha256(before[SOURCE]),
        after_sha256=content_sha256(current[SOURCE]),
        changed_rows=1,
        touched_subjects=["MIM:Izalpinin"],
        changes=[
            dict(
                kind="changed",
                before_position=cas_position,
                after_position=cas_position,
                before=rows[cas_position - 1],
                after=new_rows[cas_position - 1],
            )
        ],
        records=[
            dict(
                source_record=name,
                before_yaml_sha256=content_sha256(old_owners[name]),
                after_yaml_sha256=content_sha256(new_owners[name]),
                shape=(
                    "registry_value_correction"
                    if name == registry.CAS_OWNER
                    else "stale_node_pointer_removal"
                ),
            )
            for name in old_owners
        ],
    )
    write(receipt_path, refresh.encode(receipt))
    context = refresh.RegistryCorrectionContext(
        tmp_path, baseline, content_sha256(current[refresh.POLICY_MANIFEST])
    )
    chain.verify_mapping_chain(tmp_path)
    load_review(tmp_path, Path(prior["base_review"]))
    return prior, before, current, contracts, context, receipt_path


def verify_registry(fixture, context=None):
    prior, before, current, contracts, expected, _ = fixture
    return refresh.verify_unchanged_cohort(
        prior,
        before,
        current,
        contracts,
        contracts,
        registry_correction=expected if context is None else context,
    )


def registry_argv(fixture):
    return form_argv(fixture, pin=False) + [
        "--registry-correction-manifest-sha256",
        fixture[4].manifest_sha256,
    ]


def test_registry_native_suffix_preserves_all_companion_science(registry_correction):
    from mediaingredientmech import registry_correction_refresh as registry

    prior, before, current, _, context, _ = registry_correction
    successor, audit = verify_registry(registry_correction)
    assert successor["decisions"] == prior["decisions"]
    assert successor["record_inputs"] == prior["record_inputs"]
    assert successor["claims_sha256"] == prior["claims_sha256"]
    assert audit["scientific_approval_added"] is False
    assert "form_projection" not in audit
    assert len(prior["record_inputs"]) == 20
    assert sum(d["disposition"] == "SUPPORTED" for d in prior["decisions"]) == 50
    assert sum(d["disposition"] == "WITHHOLD" for d in prior["decisions"]) == 1
    proof = audit["registry_correction"]
    assert proof["registry_transition"]["historical_receipt_count"] == 1
    assert proof["registry_transition"]["current_receipt_count"] == 2
    assert len(proof["registry_transition"]["owners"]) == 7
    assert len(audit["selected_mapping_evidence_unchanged"]) == 20
    assert audit["claim_counts"] == {
        "mapping": 20,
        "identifier": 18,
        "product": 3,
        "occurrence": 10,
    }
    assert "not replayed" in proof["attribution_contract"]
    old, new = [read_json(v[refresh.POLICY_MANIFEST]) for v in (before, current)]
    assert old["form_projection_updates"] == new["form_projection_updates"]
    assert all(
        old["source_owner_sha256"][p]
        == new["source_owner_sha256"][p]
        != content_sha256((context.root / p).read_bytes())
        for p in registry.NODE_OWNERS
    )
    reviewed_products(successor, current)
    refresh.main(registry_argv(registry_correction))
    published = read_json((context.root / "history/audit.json").read_bytes())
    assert published["registry_correction"] == proof


@pytest.mark.parametrize("failure", ["no-context", "missing-pin", "stale-pin", "both", "unchanged"])
def test_registry_requires_one_explicit_changed_manifest_pin(registry_correction, failure):
    prior, before, current, contracts, context, _ = registry_correction
    kwargs = {"registry_correction": context}
    if failure == "no-context":
        kwargs = {}
    elif failure in {"missing-pin", "stale-pin"}:
        kwargs["registry_correction"] = refresh.RegistryCorrectionContext(
            context.root, context.baseline, "" if failure == "missing-pin" else "a" * 64
        )
    elif failure == "both":
        kwargs["form_projection"] = refresh.FormProjectionContext(
            context.root, context.baseline, context.manifest_sha256
        )
    else:
        current = before
    with pytest.raises(ValueError):
        refresh.verify_unchanged_cohort(prior, before, current, contracts, contracts, **kwargs)


def repin_registry(fixture, document):
    current, context = fixture[2], fixture[4]
    current[refresh.POLICY_MANIFEST] = refresh.encode(document)
    (context.root / refresh.POLICY_MANIFEST).write_bytes(current[refresh.POLICY_MANIFEST])
    return refresh.RegistryCorrectionContext(
        context.root, context.baseline, content_sha256(current[refresh.POLICY_MANIFEST])
    )


@pytest.mark.parametrize(
    "failure",
    [
        "extra-owner",
        "missing-owner",
        "wrong-shape",
        "node-identity",
        "node-chemistry",
        "node-status",
        "node-history",
        "node-duplicate-key",
        "cas-note",
        "cas-chemistry",
        "cas-label",
        "form-history",
        "extra-manifest-field",
        "all-current-policy-owners",
        "form-document",
        "prefix-bytes",
        "prefix-removal",
        "ignored-nested-receipt",
        "source-packet",
        "aliased-owner",
    ],
)
def test_registry_rejects_coordinated_out_of_scope_changes(registry_correction, failure):
    from mediaingredientmech import registry_correction_refresh as registry
    from mediaingredientmech.validation import mapping_change_receipts as chain

    _, _, current, _, context, receipt_path = registry_correction
    root = context.root
    receipt = read_json((root / receipt_path).read_bytes())
    manifest = read_json(current[refresh.POLICY_MANIFEST])
    update = manifest["registry_correction_updates"][-1]
    if failure == "extra-owner":
        receipt["records"].append(dict(receipt["records"][0], source_record=EXTRA_OWNER))
    elif failure == "missing-owner":
        receipt["records"].pop(0)
    elif failure == "wrong-shape":
        receipt["records"][0]["shape"] = "hydrate_parent_predicate"
    elif failure.startswith("node-") or failure.startswith("cas-"):
        owner = (
            next(iter(registry.NODE_OWNERS)) if failure.startswith("node-") else registry.CAS_OWNER
        )
        data = yaml.safe_load((root / owner).read_bytes())
        if failure.endswith("identity"):
            data["identifier"] = "CHEBI:15377"
        elif failure.endswith("chemistry"):
            data.setdefault("chemical_properties", {})["molecular_formula"] = "H2O"
        elif failure.endswith("status"):
            data["mapping_status"] = "REJECTED"
        elif failure.endswith("history"):
            data["curation_history"][0]["changes"] = "Rewritten history"
        elif failure.endswith("note"):
            data["ontology_mapping"]["evidence"][-1]["notes"] = "CAS approved as final identity"
        elif failure != "node-duplicate-key":
            data["preferred_term"] = "Different material"
        raw = yaml.safe_dump(data, sort_keys=False).encode()
        if failure == "node-duplicate-key":
            raw += yaml.safe_dump({"identifier": data["identifier"]}).encode()
        (root / owner).write_bytes(raw)
        next(r for r in receipt["records"] if r["source_record"] == owner)["after_yaml_sha256"] = (
            content_sha256(raw)
        )
        if owner == registry.CAS_OWNER:
            update["owner_after_sha256"] = manifest["source_owner_sha256"][owner] = content_sha256(
                raw
            )
    elif failure == "form-history":
        manifest["form_projection_updates"][0]["history"] = "Rewritten history"
    elif failure == "extra-manifest-field":
        update["review_waiver"] = True
    elif failure == "all-current-policy-owners":
        manifest["source_owner_sha256"].update(
            {p: content_sha256((root / p).read_bytes()) for p in registry.NODE_OWNERS}
        )
    elif failure == "form-document":
        path = root / registry.FORM_REVIEWS[0]
        path.write_bytes(path.read_bytes() + b"\n")
    elif failure == "prefix-bytes":
        path = root / chain.RECEIPTS_DIR / "prefix.json"
        data = read_json(path.read_bytes())
        data["batch"] = "Coherent replay with rewritten attribution"
        path.write_bytes(refresh.encode(data))
    elif failure == "prefix-removal":
        (root / chain.RECEIPTS_DIR / "prefix.json").unlink()
        receipt["sequence"] = 1
        for name in chain.HISTORICAL_CONTEXT:
            data = read_json((root / name).read_bytes())
            for key in ("source_sha256", "before_sha256", "after_sha256"):
                if key in data:
                    data[key] = receipt["before_sha256"]
            (root / name).write_bytes(refresh.encode(data))
    elif failure == "ignored-nested-receipt":
        (root / ".gitignore").write_text("hidden/\n")
        path = root / chain.RECEIPTS_DIR / "hidden/extra.json"
        path.parent.mkdir()
        path.write_bytes(refresh.encode(receipt))
    elif failure == "source-packet":
        path = root / registry.CAS_PACKET
        path.write_bytes(path.read_bytes() + b"\n")
    else:
        path = root / next(iter(registry.NODE_OWNERS))
        real = path.with_suffix(".real")
        path.rename(real)
        path.symlink_to(real.name)
    (root / receipt_path).write_bytes(refresh.encode(receipt))
    context = repin_registry(registry_correction, manifest)
    with pytest.raises(ValueError):
        verify_registry(registry_correction, context)


@pytest.mark.parametrize(
    "field",
    ["predicate_id", "object_label", "mapping_justification", "confidence", "comment", "source"],
)
def test_registry_row_allowlist_cannot_be_bypassed_by_repinned_receipt(registry_correction, field):
    _, _, current, _, context, receipt_path = registry_correction
    root = context.root
    receipt = read_json((root / receipt_path).read_bytes())
    metadata, fields, rows = _base_table(current[SOURCE])
    change = receipt["changes"][0]
    rows[change["after_position"] - 1][field] = "0.8" if field == "confidence" else "Out of scope"
    change["after"] = rows[change["after_position"] - 1]
    current[SOURCE] = table_bytes(metadata, fields, rows)
    (root / SOURCE).write_bytes(current[SOURCE])
    receipt["after_sha256"] = content_sha256(current[SOURCE])
    (root / receipt_path).write_bytes(refresh.encode(receipt))
    manifest = read_json(current[refresh.POLICY_MANIFEST])
    manifest["artifacts"][SOURCE] = manifest["registry_correction_updates"][-1][
        "sssom_after_sha256"
    ] = receipt["after_sha256"]
    with pytest.raises(ValueError, match="allowlist"):
        verify_registry(registry_correction, repin_registry(registry_correction, manifest))


@pytest.mark.parametrize(
    "drift", ["sixth-owner", "prefix", "new-receipt", "dependency", "form", "same-byte-alias"]
)
def test_registry_publication_rechecks_all_proof_inputs(registry_correction, monkeypatch, drift):
    from mediaingredientmech import registry_correction_refresh as registry
    from mediaingredientmech.validation import mapping_change_receipts as chain

    root = registry_correction[4].root
    real = refresh.publish_new_files

    def publish(outputs, check):
        def changed():
            path = root / list(registry.NODE_OWNERS)[-1]
            if drift == "prefix":
                path = root / chain.RECEIPTS_DIR / "prefix.json"
            elif drift == "new-receipt":
                path = root / chain.RECEIPTS_DIR / "late.json"
            elif drift == "dependency":
                path = root / registry.VERIFIERS[-1]
            elif drift == "form":
                path = root / registry.FORM_REVIEWS[-1]
            if drift == "same-byte-alias":
                target = path.with_suffix(".real")
                path.rename(target)
                path.symlink_to(target.name)
            else:
                path.write_bytes((path.read_bytes() if path.exists() else b"") + b"\n")
            check()

        return real(outputs, changed)

    monkeypatch.setattr(refresh, "publish_new_files", publish)
    with pytest.raises(ValueError):
        refresh.main(registry_argv(registry_correction))
    assert not any(
        (root / "history" / n).exists() for n in ("successor.json", "audit.json", "copy.json")
    )


@pytest.mark.parametrize(
    "failure",
    ["raw-row", "raw-header", "permutation", "extra-change", "cas-alias", "cas-stamp", "cas-date"],
)
def test_registry_native_chain_cannot_hide_extra_row_changes(registry_correction, failure):
    from mediaingredientmech.validation import mapping_change_receipts as chain

    _, _, current, _, context, receipt_path = registry_correction
    root = context.root
    receipt = read_json((root / receipt_path).read_bytes())
    metadata, fields, rows = _base_table(current[SOURCE])
    if failure == "raw-header":
        current[SOURCE] = current[SOURCE].replace(b"# license:", b"# license: ", 1)
    elif failure == "raw-row":
        lines = current[SOURCE].splitlines(keepends=True)
        position = next(i for i, line in enumerate(lines) if not line.startswith(b"#")) + 1
        token, rest = lines[position].split(b"\t", 1)
        lines[position] = b'"' + token + b'"\t' + rest
        current[SOURCE] = b"".join(lines)
    else:
        if failure == "permutation":
            rows[0], rows[1] = rows[1], rows[0]
            receipt["position_map"][:2] = [2, 1]
        elif failure == "extra-change":
            original = deepcopy(rows[0])
            rows[0]["comment"] += "Unapproved additional change"
            receipt["changes"].append(
                dict(
                    kind="changed",
                    before_position=1,
                    after_position=1,
                    before=original,
                    after=rows[0],
                )
            )
            receipt["changed_rows"] += 1
            receipt["touched_subjects"].append(rows[0]["subject_id"])
        else:
            row = rows[receipt["changes"][0]["after_position"] - 1]
            key, value = {
                "cas-alias": ("other", "CAS:480-14-8|Unreviewed alias"),
                "cas-stamp": ("validation_method", "none|UNKNOWN_TERM|2026-07-07"),
                "cas-date": ("mapping_date", "2026-11-03"),
            }[failure]
            row[key] = value
            receipt["changes"][0]["after"] = row
        current[SOURCE] = table_bytes(metadata, fields, rows)
    (root / SOURCE).write_bytes(current[SOURCE])
    receipt["after_sha256"] = content_sha256(current[SOURCE])
    (root / receipt_path).write_bytes(refresh.encode(receipt))
    # It is internally valid replay; the new bounded proof supplies the missing gate.
    chain.verify_mapping_chain(root)
    manifest = read_json(current[refresh.POLICY_MANIFEST])
    manifest["artifacts"][SOURCE] = manifest["registry_correction_updates"][-1][
        "sssom_after_sha256"
    ] = receipt["after_sha256"]
    with pytest.raises(ValueError, match="canonical .* bytes|position map|allowlist"):
        verify_registry(registry_correction, repin_registry(registry_correction, manifest))


def test_registry_cannot_renew_affected_mapping_approval(registry_correction):
    from mediaingredientmech import registry_correction_refresh as registry

    prior, _, current, _, _, _ = registry_correction
    base = read_json(current[prior["base_review"]])
    decision = next(d for d in base["decisions"] if d["owner_record"] in registry.NODE_OWNERS)
    decision["disposition"] = "SUPPORTED"
    current[prior["base_review"]] = refresh.encode(base)
    with pytest.raises(ValueError, match="retain all affected mapping holds"):
        verify_registry(registry_correction)


def test_registry_output_collision_preserves_source(registry_correction):
    from mediaingredientmech import registry_correction_refresh as registry

    root = registry_correction[4].root
    before = (root / registry.CAS_OWNER).read_bytes()
    argv = registry_argv(registry_correction)
    argv[argv.index("--output") + 1] = registry.CAS_OWNER
    with pytest.raises((ValueError, FileExistsError)):
        refresh.main(argv)
    assert (root / registry.CAS_OWNER).read_bytes() == before


def test_registry_replaced_output_reservation_is_not_overwritten(registry_correction, monkeypatch):
    root = registry_correction[4].root
    real = refresh.publish_new_files
    victim = root / "history/successor.json"

    def publish(outputs, check):
        def changed():
            check()
            victim.unlink()
            victim.write_bytes(b"Competing output")

        return real(outputs, changed)

    monkeypatch.setattr(refresh, "publish_new_files", publish)
    with pytest.raises(ValueError, match="Output reservation changed"):
        refresh.main(registry_argv(registry_correction))
    assert victim.read_bytes() == b"Competing output"
    assert not (root / "history/audit.json").exists()
    assert not (root / "history/copy.json").exists()


def test_registry_root_alias_refused(registry_correction):
    context = registry_correction[4]
    alias = context.root / "root-alias"
    alias.symlink_to(context.root, target_is_directory=True)
    with pytest.raises(ValueError, match="aliased context"):
        verify_registry(
            registry_correction,
            refresh.RegistryCorrectionContext(alias, context.baseline, context.manifest_sha256),
        )


@pytest.mark.parametrize("consumer", ["direct", "cli"])
@pytest.mark.parametrize("input_kind", ["historical-receipt", "historical-context"])
def test_registry_replay_bytes_cannot_be_rebound_after_restore(
    registry_correction, monkeypatch, consumer, input_kind
):
    """#1088: real native replay sees changed bytes, then the durable bytes return."""
    from mediaingredientmech.validation import mapping_change_receipts as chain

    root = registry_correction[4].root
    name = (
        chain.RECEIPTS_DIR + "/prefix.json"
        if input_kind == "historical-receipt"
        else chain.BASELINE
    )
    path = root / name
    original = path.read_bytes()
    document = read_json(original)
    document["batch" if input_kind == "historical-receipt" else "scope"] = (
        "Different attribution observed during real native replay"
    )
    changed = refresh.encode(document)
    real_replay = chain.verify_mapping_chain
    observations = []

    def replay_then_restore(actual_root):
        assert actual_root == root
        path.write_bytes(changed)
        try:
            proof = real_replay(actual_root)
        finally:
            path.write_bytes(original)
        # Return the real proof untouched; this is a file race, not a fake proof.
        observations.append(proof["input_hashes"][name])
        return proof

    reservations = []
    real_publish = refresh.publish_new_files

    def observed_publish(outputs, check):
        reservations.append(True)
        return real_publish(outputs, check)

    monkeypatch.setattr(chain, "verify_mapping_chain", replay_then_restore)
    monkeypatch.setattr(refresh, "publish_new_files", observed_publish)
    with pytest.raises(ValueError, match="conflicting proof input hash"):
        if consumer == "direct":
            verify_registry(registry_correction)
        else:
            refresh.main(registry_argv(registry_correction))
    assert observations == [content_sha256(changed)]
    assert observations[0] != content_sha256(original)
    assert path.read_bytes() == original
    assert reservations == []
    assert not any(
        (root / "history" / name).exists() for name in ("successor.json", "audit.json", "copy.json")
    )
