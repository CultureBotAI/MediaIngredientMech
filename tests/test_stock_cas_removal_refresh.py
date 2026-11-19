"""The stock-CAS successor withdraws a token without renewing any science."""

import subprocess
from copy import deepcopy
from pathlib import Path

import pytest

from tests.pre_mint_schema import pre_mint_schema  # noqa: F401

pytestmark = pytest.mark.usefixtures("pre_mint_schema")
import yaml

from mediaingredientmech import ingredient_bundle_refresh as refresh
from mediaingredientmech import stock_cas_removal_refresh as stock
from mediaingredientmech.export.reviewed_sssom import load_review
from mediaingredientmech.ingredient_bundle_contract import _base_table, content_sha256, read_json
from mediaingredientmech.validation import mapping_change_receipts as chain
from tests.test_ingredient_bundle_dependency_refresh import cohort as cohort
from tests.test_ingredient_bundle_dependency_refresh import table_bytes

ROOT = Path(__file__).resolve().parents[1]
SOURCE = chain.SSSOM_SOURCE
EVIDENCE = "reports/sssom_completion_20260921/mapping-evidence.json"
EXTRA = "data/ingredients/mapped/Refresh_Unselected_Fixture.yaml"
STAMP = "2026-11-03T12:00:00+00:00"  # Explicit synthetic time; no live-header dependency.


def source_documents():
    raw = (ROOT / stock.PACKET).read_bytes()
    assert content_sha256(raw) == stock.PACKET_SHA256
    packet = read_json(raw)
    before, after = {}, {}
    for name, spec in packet["owners"].items():
        original = (ROOT / spec["preimage"]).read_bytes()
        assert content_sha256(original) == spec["before_yaml_sha256"]
        old = yaml.safe_load(original)
        new = deepcopy(old)
        for field in spec["delete"]:
            keys = field.split(".")
            parent = new
            for key in keys[:-1]:
                parent = parent[key]
            del parent[keys[-1]]
        for field, value in spec["set"].items():
            keys = field.split(".")
            parent = new
            for key in keys[:-1]:
                parent = parent[key]
            parent[keys[-1]] = deepcopy(value)
        new["curation_history"].append(
            {
                "timestamp": STAMP,
                "curator": packet["curator"],
                "action": packet["action"],
                "changes": spec["event_changes"],
                "previous_status": old["mapping_status"],
                "new_status": old["mapping_status"],
                "llm_assisted": True,
                "llm_model": packet["llm_model"],
            }
        )
        before[name] = original
        after[name] = yaml.safe_dump(new, sort_keys=False, allow_unicode=True).encode()
    return packet, before, after


@pytest.mark.parametrize("owner", sorted(read_json((ROOT / stock.PACKET).read_bytes())["owners"]))
def test_exact_source_matrix_and_preserved_history(owner):
    packet, before, after = source_documents()
    event = stock.verify_source_transition(
        owner, yaml.safe_load(before[owner]), yaml.safe_load(after[owner]), packet
    )
    assert event["timestamp"] == STAMP and event["llm_assisted"] is True


@pytest.mark.parametrize(
    "field",
    [
        "identifier",
        "preferred_term",
        "synonyms",
        "roles",
        "source_count",
        "ingredient_type",
        "curation_history",
    ],
)
def test_source_matrix_rejects_unrelated_changes(field):
    packet, before, after = source_documents()
    name = "data/ingredients/mapped/Cocl2_X_2_H2o.yaml"
    old, new = yaml.safe_load(before[name]), yaml.safe_load(after[name])
    if field == "curation_history":
        new[field][0]["changes"] = "rewritten history"
    else:
        new[field] = "unsupported change"
    with pytest.raises(ValueError):
        stock.verify_source_transition(name, old, new, packet)


@pytest.fixture
def stock_transition(cohort, tmp_path):
    prior, before, _, contracts = deepcopy(cohort)
    before.pop(EXTRA)
    prior["inputs"].pop(EXTRA)
    packet, old_owners, new_owners = source_documents()
    raw = (ROOT / "tests/fixtures/stock_cas_removal/mapping-before.json").read_bytes()
    assert content_sha256(raw) == "744bde708c3647d7a84555550842c2bd981512e53dc696760e7e9401433c5d86"
    frozen = read_json(raw)
    metadata, fields, rows = _base_table(before[SOURCE])
    rows = rows[:-1]
    positions = {}
    for entry in frozen["rows"]:
        rows.append(deepcopy(entry["row"]))
        positions[len(rows)] = entry["owner"]
    latest = max(row["mapping_date"] for row in rows)
    metadata.update(mapping_date=latest, mapping_set_version=latest)
    before[SOURCE] = table_bytes(metadata, fields, rows)
    base = read_json(before[prior["base_review"]])
    evidence = read_json(before[EVIDENCE])
    base["decisions"] = base["decisions"][:-1]
    base["record_inputs"].pop(EXTRA)
    evidence["entries"].pop("unselected-fixture")
    for position, owner in positions.items():
        key = "stock-fixture-" + str(position)
        decision = {
            "source_position": position,
            "owner_record": owner,
            "row_sha256": content_sha256(refresh.canonical_json(rows[position - 1])),
            "disposition": "WITHHOLD",
            "review_reason": "Synthetic fixture retains hold",
            "review_evidence": EVIDENCE,
            "evidence_key": key,
        }
        base["decisions"].append(decision)
        entry = {
            k: v
            for k, v in decision.items()
            if k not in {"source_position", "review_evidence", "evidence_key"}
        }
        entry["owner_record_sha256"] = content_sha256(old_owners[owner])
        evidence["entries"][key] = entry
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
    manifest = {
        "schema_version": 1,
        "policy_version": "owned-name-policy-v1",
        "approval": "NONE: fixture",
        "scope": "Synthetic fixture, no approval",
        "decisions": [],
        "policy_evidence": [],
        "producer_revision": "a" * 40,
        "generation_manifest_sha256": "a" * 64,
        "generation_receipt_sha256": "b" * 64,
        "source_receipt_sha256": "c" * 64,
        "sssom_before_sha256": "d" * 64,
        "baseline_before_sha256": "e" * 64,
        "source_owner_sha256": frozen["historical_owner_pins"],
        "artifacts": {
            p: content_sha256(before[p])
            for p in (SOURCE, refresh.POLICY_SIDECAR, refresh.POLICY_BASELINE)
        },
        "form_projection_updates": [{"history": "first FORM"}, {"history": "second FORM"}],
        "registry_correction_updates": [{"history": "prior registry correction"}],
    }
    before[refresh.POLICY_MANIFEST] = refresh.encode(manifest)
    prior["inputs"][refresh.POLICY_MANIFEST] = content_sha256(before[refresh.POLICY_MANIFEST])
    current = dict(before)
    new_rows = deepcopy(rows)
    position = next(p for p, n in positions.items() if n == stock.STOCK)
    old_row = rows[position - 1]
    new_row = new_rows[position - 1]
    new_row.update(
        other="|".join(t for t in old_row["other"].split("|") if t != stock.CAS_TOKEN),
        source=stock.expected_stock_source(yaml.safe_load(new_owners[stock.STOCK])),
        mapping_date=STAMP[:10],
        validation_method="",
    )
    metadata.update(mapping_date=STAMP[:10], mapping_set_version=STAMP[:10])
    current[SOURCE] = table_bytes(metadata, fields, new_rows)
    new_base, new_evidence = deepcopy(base), deepcopy(evidence)
    for decision in new_base["decisions"]:
        owner = decision["owner_record"]
        if owner not in new_owners:
            continue
        decision["row_sha256"] = content_sha256(
            refresh.canonical_json(new_rows[decision["source_position"] - 1])
        )
        new_evidence["entries"][decision["evidence_key"]].update(
            row_sha256=decision["row_sha256"], owner_record_sha256=content_sha256(new_owners[owner])
        )
        new_base["record_inputs"][owner] = content_sha256(new_owners[owner])
    current[EVIDENCE] = refresh.encode(new_evidence)
    new_base["inputs"][EVIDENCE] = content_sha256(current[EVIDENCE])
    new_base["source_sha256"] = content_sha256(current[SOURCE])
    current[prior["base_review"]] = refresh.encode(new_base)
    update = {
        "issue": 268,
        "scope": "Bounded stock-CAS removal and fourteen chemistry-only owners",
        "approval": "NONE: retain holds",
        "prior_manifest_sha256": content_sha256(before[refresh.POLICY_MANIFEST]),
        "source_record": stock.STOCK,
        "historical_owner_sha256": stock.HISTORICAL_OWNER,
        "owner_before_sha256": stock.ACTUAL_PREIMAGE,
        "owner_after_sha256": content_sha256(new_owners[stock.STOCK]),
        "source_receipt": "/captured/source.json",
        "source_receipt_sha256": "1" * 64,
        "generation_manifest_sha256": "2" * 64,
        "generation_receipt_sha256": "3" * 64,
        "sssom_before_sha256": content_sha256(before[SOURCE]),
        "sssom_after_sha256": content_sha256(current[SOURCE]),
        "sidecar_sha256": content_sha256(before[refresh.POLICY_SIDECAR]),
        "baseline_sha256": content_sha256(before[refresh.POLICY_BASELINE]),
    }
    new_manifest = deepcopy(manifest)
    new_manifest["stock_cas_removal_updates"] = [update]
    new_manifest["artifacts"][SOURCE] = content_sha256(current[SOURCE])
    new_manifest["source_owner_sha256"][stock.STOCK] = update["owner_after_sha256"]
    current[refresh.POLICY_MANIFEST] = refresh.encode(new_manifest)

    def write(name, raw):
        path = tmp_path / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(raw)

    for name, raw in (before | contracts | old_owners).items():
        write(name, raw)
    write("history/prior.json", refresh.encode(prior))
    for name in stock.VERIFIERS + stock.FORM_REVIEWS:
        write(name, (ROOT / name).read_bytes())
    write(stock.PACKET, (ROOT / stock.PACKET).read_bytes())
    for name in packet["files"]:
        write(name, (ROOT / name).read_bytes())
    prehistory = content_sha256(before[SOURCE] + b"# synthetic historical metadata\n")
    write(
        chain.BASELINE,
        refresh.encode({"schema_version": 1, "source_sha256": prehistory, "rows": rows}),
    )
    for name in (chain.TRAIT_REFRESH, chain.PARENT_REFRESH):
        write(
            name,
            refresh.encode(
                {
                    "schema_version": 1,
                    "before_sha256": prehistory,
                    "after_sha256": prehistory,
                    "row_count": len(rows),
                    "changed_rows": 0,
                    "changes": [],
                }
            ),
        )
    prefix = {
        "schema_version": 1,
        "sequence": 1,
        "batch": "synthetic-node-bridge",
        "approval": "NONE: fixture",
        "issue": "fixture",
        "before_sha256": prehistory,
        "after_sha256": content_sha256(before[SOURCE]),
        "before_row_count": len(rows),
        "after_row_count": len(rows),
        "changed_rows": 0,
        "added_rows": 0,
        "removed_rows": 0,
        "position_map": list(range(1, len(rows) + 1)),
        "touched_subjects": [],
        "changes": [],
        "records": [
            {
                "source_record": stock.STOCK,
                "before_yaml_sha256": stock.HISTORICAL_OWNER,
                "after_yaml_sha256": stock.ACTUAL_PREIMAGE,
                "shape": "stale_node_pointer_removal",
            }
        ],
    }
    write(stock.BRIDGE, refresh.encode(prefix))
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
            "Durable synthetic historical bridge",
        ],
        check=True,
    )
    baseline = (
        subprocess.check_output(["git", "-C", str(tmp_path), "rev-parse", "HEAD"]).decode().strip()
    )
    for name, raw in (current | new_owners).items():
        write(name, raw)
    receipt_path = chain.RECEIPTS_DIR + "/stock-fixture.json"
    receipt = dict(
        prefix,
        sequence=2,
        batch="stock-cas-removal",
        issue="https://github.com/CultureBotAI/MediaIngredientMech/issues/268",
        before_sha256=content_sha256(before[SOURCE]),
        after_sha256=content_sha256(current[SOURCE]),
        changed_rows=1,
        touched_subjects=[stock.SUBJECT],
        changes=[
            {
                "kind": "changed",
                "before_position": position,
                "after_position": position,
                "before": old_row,
                "after": new_row,
            }
        ],
        records=[
            {
                "source_record": n,
                "before_yaml_sha256": content_sha256(old_owners[n]),
                "after_yaml_sha256": content_sha256(new_owners[n]),
                "shape": packet["owners"][n]["shape"],
            }
            for n in old_owners
        ],
    )
    write(receipt_path, refresh.encode(receipt))
    context = refresh.StockCasRemovalContext(
        tmp_path, baseline, content_sha256(current[refresh.POLICY_MANIFEST])
    )
    chain.verify_mapping_chain(tmp_path)
    load_review(tmp_path, Path(prior["base_review"]))
    return prior, before, current, contracts, context, receipt_path


def verify(fixture, **kwargs):
    prior, before, current, contracts, context, _ = fixture
    return refresh.verify_unchanged_cohort(
        prior,
        before,
        current,
        contracts,
        contracts,
        stock_cas_removal=kwargs.pop("context", context),
        **kwargs,
    )


def repin(fixture, manifest):
    prior, before, current, contracts, context, receipt = fixture
    current[refresh.POLICY_MANIFEST] = refresh.encode(manifest)
    (context.root / refresh.POLICY_MANIFEST).write_bytes(current[refresh.POLICY_MANIFEST])
    return (
        prior,
        before,
        current,
        contracts,
        refresh.StockCasRemovalContext(
            context.root, context.baseline, content_sha256(current[refresh.POLICY_MANIFEST])
        ),
        receipt,
    )


def test_native_fifteen_owner_transition_preserves_science(stock_transition):
    prior, _, _, _, _, _ = stock_transition
    successor, audit = verify(stock_transition)
    assert successor["decisions"] == prior["decisions"]
    assert successor["record_inputs"] == prior["record_inputs"]
    proof = audit["stock_cas_removal"]["stock_cas_transition"]
    assert len(proof["owners"]) == 15 and proof["scientific_approval_added"] is False
    assert len(proof["stock_historical_supersession"]["receipts"]) == 2
    assert len(proof["stock_actual_preimage_supersession"]["receipts"]) == 1


@pytest.mark.parametrize(
    "failure",
    [
        "missing_context",
        "bad_pin",
        "form_context",
        "registry_context",
        "mixed_context",
        "root_alias",
    ],
)
def test_only_explicit_stock_context_can_authorize_transition(stock_transition, failure):
    p, b, c, k, context, _ = stock_transition
    options = {"stock_cas_removal": context}
    if failure == "missing_context":
        options = {}
    elif failure == "bad_pin":
        options["stock_cas_removal"] = refresh.StockCasRemovalContext(
            context.root, context.baseline, "0" * 64
        )
    elif failure == "form_context":
        options = {
            "form_projection": refresh.FormProjectionContext(
                context.root, context.baseline, context.manifest_sha256
            )
        }
    elif failure == "registry_context":
        options = {
            "registry_correction": refresh.RegistryCorrectionContext(
                context.root, context.baseline, context.manifest_sha256
            )
        }
    elif failure == "mixed_context":
        options["registry_correction"] = refresh.RegistryCorrectionContext(
            context.root, context.baseline, context.manifest_sha256
        )
    else:
        alias = context.root.parent / (context.root.name + "-alias")
        alias.symlink_to(context.root, target_is_directory=True)
        options["stock_cas_removal"] = refresh.StockCasRemovalContext(
            alias, context.baseline, context.manifest_sha256
        )
    with pytest.raises(ValueError):
        refresh.verify_unchanged_cohort(p, b, c, k, k, **options)


@pytest.mark.parametrize(
    "failure",
    [
        "unknown_field",
        "wrong_issue",
        "historical_equals_actual",
        "restamp_other_owner",
        "change_form_history",
        "change_registry_history",
        "extra_owner",
        "missing_owner",
        "owner_role",
        "owner_history",
        "bridge_change",
        "nested_receipt",
    ],
)
def test_coordinated_repins_do_not_expand_scope(stock_transition, failure):
    p, b, c, k, context, receipt_path = stock_transition
    root = context.root
    manifest = read_json(c[refresh.POLICY_MANIFEST])
    update = manifest["stock_cas_removal_updates"][-1]
    receipt = read_json((root / receipt_path).read_bytes())
    if failure == "unknown_field":
        manifest["unreviewed_history"] = []
    elif failure == "wrong_issue":
        update["issue"] = 753
    elif failure == "historical_equals_actual":
        update["historical_owner_sha256"] = stock.ACTUAL_PREIMAGE
        manifest["source_owner_sha256"][stock.STOCK] = update["owner_after_sha256"]
    elif failure == "restamp_other_owner":
        owner = next(n for n in manifest["source_owner_sha256"] if n != stock.STOCK)
        manifest["source_owner_sha256"][owner] = content_sha256((root / owner).read_bytes())
    elif failure == "change_form_history":
        manifest["form_projection_updates"][0]["history"] = "changed"
    elif failure == "change_registry_history":
        manifest["registry_correction_updates"][0]["history"] = "changed"
    elif failure == "extra_owner":
        receipt["records"].append(deepcopy(receipt["records"][0]))
    elif failure == "missing_owner":
        receipt["records"].pop()
    elif failure in {"owner_role", "owner_history"}:
        owner = next(n for n in manifest["source_owner_sha256"] if n != stock.STOCK)
        doc = yaml.safe_load((root / owner).read_bytes())
        if failure == "owner_role":
            doc["roles"] = [{"role": "unsupported"}]
        else:
            doc["curation_history"][0]["changes"] = "rewritten"
        raw = yaml.safe_dump(doc, sort_keys=False).encode()
        (root / owner).write_bytes(raw)
        next(r for r in receipt["records"] if r["source_record"] == owner)["after_yaml_sha256"] = (
            content_sha256(raw)
        )
    elif failure == "bridge_change":
        bridge = read_json((root / stock.BRIDGE).read_bytes())
        bridge["batch"] = "rewritten historical bridge"
        (root / stock.BRIDGE).write_bytes(refresh.encode(bridge))
    else:
        path = root / chain.RECEIPTS_DIR / "ignored-nested/extra.json"
        path.parent.mkdir()
        path.write_text("{}\n")
    (root / receipt_path).write_bytes(refresh.encode(receipt))
    changed = repin(stock_transition, manifest)
    with pytest.raises(ValueError):
        verify(changed)


def stock_argv(fixture):
    _, _, _, _, context, _ = fixture
    out = context.root / "successor"
    out.mkdir(exist_ok=True)
    return [
        "--root",
        str(context.root),
        "--baseline",
        context.baseline,
        "--prior-review",
        "history/prior.json",
        "--output",
        "successor/review.json",
        "--receipt",
        "successor/audit.json",
        "--prior-copy",
        "successor/prior.json",
        "--stock-cas-removal-manifest-sha256",
        context.manifest_sha256,
    ]


def repin_row(fixture, field, value, *, quote_other_row=False):
    p, b, c, k, context, receipt_path = fixture
    root = context.root
    receipt = read_json((root / receipt_path).read_bytes())
    metadata, columns, rows = _base_table(c[SOURCE])
    position = receipt["changes"][0]["after_position"]
    rows[position - 1][field] = value
    metadata.update(
        mapping_date=max(r["mapping_date"] for r in rows),
        mapping_set_version=max(r["mapping_date"] for r in rows),
    )
    c[SOURCE] = table_bytes(metadata, columns, rows)
    if quote_other_row:
        lines = c[SOURCE].splitlines(keepends=True)
        line = next(i for i, raw_line in enumerate(lines) if raw_line.startswith(b"MIM:"))
        first, rest = lines[line].split(b"\t", 1)
        lines[line] = b'"' + first + b'"\t' + rest
        c[SOURCE] = b"".join(lines)
    receipt["changes"][0]["after"] = rows[position - 1]
    receipt["after_sha256"] = content_sha256(c[SOURCE])
    base = read_json(c[p["base_review"]])
    evidence = read_json(c[EVIDENCE])
    decision = next(d for d in base["decisions"] if d["source_position"] == position)
    decision["row_sha256"] = content_sha256(refresh.canonical_json(rows[position - 1]))
    evidence["entries"][decision["evidence_key"]]["row_sha256"] = decision["row_sha256"]
    c[EVIDENCE] = refresh.encode(evidence)
    base["inputs"][EVIDENCE] = content_sha256(c[EVIDENCE])
    base["source_sha256"] = content_sha256(c[SOURCE])
    c[p["base_review"]] = refresh.encode(base)
    for name in (SOURCE, EVIDENCE, p["base_review"]):
        (root / name).write_bytes(c[name])
    (root / receipt_path).write_bytes(refresh.encode(receipt))
    manifest = read_json(c[refresh.POLICY_MANIFEST])
    manifest["artifacts"][SOURCE] = content_sha256(c[SOURCE])
    manifest["stock_cas_removal_updates"][-1]["sssom_after_sha256"] = content_sha256(c[SOURCE])
    return repin(fixture, manifest)


@pytest.mark.parametrize(
    ("field", "value"),
    [
        ("other", "ThDP|ThPP|CAS:154-87-0"),
        ("other", "extra alias"),
        ("source", "MIM:unreviewed"),
        ("mapping_date", "2030-01-01"),
        ("validation_method", "OAK+OLS:chebi|SYNONYM_ENRICH|2026-07-07"),
        ("comment", "unreviewed claim"),
        ("confidence", "0.91"),
        ("object_id", "CHEBI:9532"),
        ("predicate_id", "skos:closeMatch"),
        ("subject_label", "Thiamine pyrophosphate"),
    ],
)
def test_one_row_scope_survives_coordinated_receipt_and_review_repins(
    stock_transition, field, value
):
    changed = repin_row(stock_transition, field, value)
    with pytest.raises(ValueError):
        verify(changed)


def test_unrelated_raw_row_bytes_are_preserved(stock_transition):
    receipt = read_json((stock_transition[4].root / stock_transition[5]).read_bytes())
    changed = repin_row(
        stock_transition, "other", receipt["changes"][0]["after"]["other"], quote_other_row=True
    )
    with pytest.raises(ValueError, match="unrelated canonical row bytes"):
        verify(changed)


def test_stock_cli_positive_publishes_all_three_bound_outputs(stock_transition):
    refresh.main(stock_argv(stock_transition))
    root = stock_transition[4].root
    audit = read_json((root / "successor/audit.json").read_bytes())
    assert audit["scientific_approval_added"] is False
    assert len(audit["stock_cas_removal"]["stock_cas_transition"]["owners"]) == 15
    assert (root / "successor/prior.json").read_bytes() == (
        root / "history/prior.json"
    ).read_bytes()


@pytest.mark.parametrize(
    "drift",
    ["owner_symlink", "nested_receipt", "verifier_bytes", "parent_alias", "parent_replacement"],
)
def test_stock_cli_rechecks_new_proof_and_parent_ownership(stock_transition, monkeypatch, drift):
    args = stock_argv(stock_transition)
    root = stock_transition[4].root
    original = refresh.publish_new_files
    moved = root / "moved-successor"

    def publish(outputs, verify_snapshot):
        def mutate_then_verify():
            if drift == "owner_symlink":
                path = root / stock.STOCK
                saved = path.with_suffix(".saved")
                path.rename(saved)
                path.symlink_to(saved)
            elif drift == "nested_receipt":
                path = root / chain.RECEIPTS_DIR / "nested/extra.json"
                path.parent.mkdir()
                path.write_text("{}\n")
            elif drift == "verifier_bytes":
                path = root / stock.VERIFIERS[0]
                path.write_bytes(path.read_bytes() + b"\n# changed during verification\n")
            else:
                parent = root / "successor"
                parent.rename(moved)
                if drift == "parent_alias":
                    parent.symlink_to(moved, target_is_directory=True)
                else:
                    parent.mkdir()
                    (parent / "review.json").write_bytes(b"another writer\n")
            verify_snapshot()

        return original(outputs, mutate_then_verify)

    monkeypatch.setattr(refresh, "publish_new_files", publish)
    with pytest.raises(ValueError):
        refresh.main(args)
    if moved.exists():
        assert not list(moved.iterdir())
    if drift == "parent_replacement":
        assert (root / "successor/review.json").read_bytes() == b"another writer\n"
    elif drift != "parent_alias":
        assert not list((root / "successor").iterdir())


@pytest.mark.parametrize("change", ["alias", "replacement"])
def test_companion_publisher_refuses_parent_changes_and_cleans_held_directory(tmp_path, change):
    parent = tmp_path / "outputs"
    parent.mkdir()
    moved = tmp_path / "moved"
    output = parent / "review.json"

    def mutate():
        parent.rename(moved)
        if change == "alias":
            parent.symlink_to(moved, target_is_directory=True)
        else:
            parent.mkdir()
            (parent / "review.json").write_bytes(b"unrelated writer\n")

    with pytest.raises(ValueError, match="Output parent"):
        refresh.publish_new_files([(output, b"new data\n")], mutate)
    assert not list(moved.iterdir())
    if change == "replacement":
        assert output.read_bytes() == b"unrelated writer\n"


def test_companion_publisher_refuses_initial_parent_alias(tmp_path):
    parent = tmp_path / "real"
    parent.mkdir()
    alias = tmp_path / "alias"
    alias.symlink_to(parent, target_is_directory=True)
    with pytest.raises(ValueError, match="Output parent is aliased"):
        refresh.publish_new_files([(alias / "review.json", b"new data\n")], lambda: None)
    assert not list(parent.iterdir())


def test_companion_publisher_refuses_parent_replacement_during_acquisition(tmp_path, monkeypatch):
    parent = tmp_path / "outputs"
    parent.mkdir()
    foreign = tmp_path / "foreign"
    foreign.mkdir()
    (foreign / "sentinel").write_bytes(b"unrelated writer\n")
    displaced = tmp_path / "displaced"
    original = refresh.os.open
    seen = []

    def swap_at_open(path, flags, *args, **kwargs):
        if Path(path) == parent and flags & refresh.os.O_DIRECTORY:
            seen.append(path)
            parent.rename(displaced)
            foreign.rename(parent)
        return original(path, flags, *args, **kwargs)

    monkeypatch.setattr(refresh.os, "open", swap_at_open)
    outputs = [
        (parent / name, b"new bytes\n") for name in ("review.json", "audit.json", "prior.json")
    ]
    with pytest.raises(ValueError, match="Output parent changed during acquisition"):
        refresh.publish_new_files(outputs, lambda: None)
    assert seen == [parent]
    assert not list(displaced.iterdir())
    assert sorted(p.name for p in parent.iterdir()) == ["sentinel"]
    assert (parent / "sentinel").read_bytes() == b"unrelated writer\n"
