"""Bounded stock-CAS promotion and exact completed-source transition tests."""

import csv
import gzip
import importlib.util
import io
import json
import os
import shutil
import subprocess
import sys
from contextlib import contextmanager
from pathlib import Path

import pytest
import yaml

from tests.pre_mint_schema import pre_mint_schema  # noqa: F401

# Replay dated, checksum-bound sources under their exact pre-mint schema.
pytestmark = pytest.mark.usefixtures("pre_mint_schema")

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "stock_promoter", ROOT / "scripts/promote_stock_cas_removal.py"
)
mod = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(mod)
STAMP = "2030-01-02T00:00:00+00:00"


def frozen(path):
    raw = subprocess.check_output(
        ["git", "cat-file", "blob", f'{mod.source.META["base_revision"]}:{path}'], cwd=ROOT
    )
    assert mod.digest(raw) == mod.BEFORE[path]
    return raw


@pytest.fixture(scope="session")
def anchors():
    return {p: frozen(p) for p in mod.source.ANCHORS}


@pytest.fixture(scope="module")
def proposals(pre_mint_schema):
    return mod.source.propose_sources(
        {p: mod.source.frozen(p) for p in mod.source.OWNERS}, timestamp=STAMP
    )


def tsv(fields, rows, header=b""):
    stream = io.StringIO(newline="")
    writer = csv.DictWriter(stream, fieldnames=fields, delimiter="\t", lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    return header + stream.getvalue().encode()


def candidate(before, current):
    _, fields, pairs = mod.table(before)
    old = next(row for row, _ in pairs if row["subject_id"] == mod.SUBJECT)
    record = yaml.safe_load(current[mod.OWNER])
    row = dict(old)
    row.update(
        other="|".join(t for t in old["other"].split("|") if t != mod.CAS_TOKEN),
        source="MIM:CultureMech|MIM:MIM curation (#288/#320)|MIM:curator=Codex",
        mapping_date=record["curation_history"][-1]["timestamp"][:10],
    )
    return tsv(fields, [row])


def test_exact_one_row_projection_and_history_prefix(anchors, proposals):
    before = anchors[mod.SSSOM]
    after = mod.promoted_sssom(before, candidate(before, proposals), proposals)
    _, cols, old = mod.table(before)
    _, newcols, new = mod.table(after)
    assert cols == newcols and len(old) == len(new) == 2983
    changed = [(i, a, b) for i, (a, b) in enumerate(zip(old, new, strict=True), 1) if a[1] != b[1]]
    assert len(changed) == 1 and changed[0][0] == 9
    a, b = changed[0][1][0], changed[0][2][0]
    assert len(b["other"].split("|")) == 6 and b["other"] == "|".join(
        t for t in a["other"].split("|") if t != mod.CAS_TOKEN
    )
    assert b["object_id"] == a["object_id"] == mod.IDENTITY
    assert b["validation_method"] == ""
    assert all(
        a[k] == b[k]
        for k in cols
        if k not in {"other", "source", "mapping_date", "validation_method"}
    )
    manifest = mod.promotion_manifest(
        anchors[mod.MANIFEST],
        after,
        proposals,
        Path("/tmp/stock-source.json").resolve(),
        generation_manifest_sha256="a" * 64,
        generation_receipt_sha256="b" * 64,
        source_receipt_sha256="c" * 64,
    )
    original = json.loads(anchors[mod.MANIFEST])
    updated = json.loads(manifest)
    note = updated.pop("stock_cas_removal_updates")
    assert len(note) == 1 and note[0]["historical_owner_sha256"] == mod.HISTORICAL_OWNER
    assert "native_receipt_sha256" not in note[0]
    updated["artifacts"][str(mod.SSSOM)] = original["artifacts"][str(mod.SSSOM)]
    updated["source_owner_sha256"][mod.RECORD] = original["source_owner_sha256"][mod.RECORD]
    assert updated == original


@pytest.mark.parametrize(
    "field,value",
    [
        ("other", "CAS:154-87-0"),
        ("other", "ThPP|ThDP"),
        ("source", "MIM:invented"),
        ("mapping_date", "2000-01-01"),
        ("object_id", "CHEBI:9532"),
        ("predicate_id", "skos:broadMatch"),
        ("object_label", "new label"),
        ("comment", "invented approval"),
        ("confidence", "1.0"),
        ("validation_method", "fabricated stamp"),
        ("validation_method", ""),
    ],
)
def test_candidate_scope_refuses(anchors, proposals, field, value):
    raw = candidate(anchors[mod.SSSOM], proposals)
    _, fields, rows = mod.table(raw)
    row = rows[0][0]
    row[field] = value
    with pytest.raises(ValueError):
        mod.promoted_sssom(anchors[mod.SSSOM], tsv(fields, [row]), proposals)


@pytest.mark.parametrize("kind", ["missing", "extra", "wrong-owner", "changed-prefix"])
def test_projection_requires_complete_exact_source_batch(anchors, proposals, kind):
    current = dict(proposals)
    if kind == "missing":
        current.pop(next(iter(current)))
    elif kind == "extra":
        current[Path("data/ingredients/mapped/other.yaml")] = next(iter(current.values()))
    else:
        p = mod.source.OWNERS[-1]
        doc = yaml.safe_load(current[p])
        doc["identifier" if kind == "wrong-owner" else "preferred_term"] = "unreviewed"
        current[p] = yaml.safe_dump(doc).encode()
    with pytest.raises(ValueError):
        mod.promoted_sssom(anchors[mod.SSSOM], candidate(anchors[mod.SSSOM], proposals), current)


@pytest.fixture
def native_runtime():
    return pytest.importorskip("kg_microbe_write", reason="Real native transaction required")


@pytest.fixture
def case(tmp_path, anchors):
    root = tmp_path.resolve() / "mim"
    root.mkdir()
    for name in [str(mod.source.MANIFEST), *mod.source.META["files"]]:
        path = root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(ROOT / name, path)
    for path, data in (anchors | {p: mod.source.frozen(p) for p in mod.source.OWNERS}).items():
        target = root / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(data)
    receipts = tmp_path.resolve() / "receipts"
    receipts.mkdir()
    return root, receipts / "source.json", receipts / "capture.json", receipts / "promote.json"


@pytest.fixture
def captured(case, native_runtime):
    root, source, proof, _ = case
    mod.source.apply_sources(root, source, apply=True)
    assert not mod.capture_sources(root, source, proof)["applied"] and not proof.exists()
    assert mod.capture_sources(root, source, proof, apply=True)["applied"]
    return case


def test_capture_reconstructs_original_frozen_source_receipt(captured):
    root, source, proof, _ = captured
    direct, expected = mod.source.source_receipt(root, source)
    bound, actual, old = mod._captured_sources(root, source, proof)
    assert actual == expected and all(bound[p] == b for p, b in direct.items())
    assert all(mod.digest(b) == mod.BEFORE[p] for p, b in old.items())


@pytest.mark.parametrize(
    "kind",
    [
        "proof",
        "anchor",
        "source-receipt",
        "backup",
        "journal",
        "owner",
        "other-anchor",
        "extra-owner",
    ],
)
def test_historical_source_capture_tampering_refuses(captured, kind):
    root, source, proof, _ = captured
    if kind == "extra-owner":
        path = root / "data/ingredients/mapped/.ignored/extra.yaml"
        path.parent.mkdir()
        path.write_bytes(mod.source.frozen(mod.OWNER))
    else:
        path = {
            "proof": proof,
            "anchor": mod.capture_anchors(proof)[mod.SSSOM],
            "source-receipt": source,
            "backup": mod.source.backups(source)[mod.OWNER],
            "journal": Path(json.loads(source.read_bytes())["transaction"]["journal"]),
            "owner": root / mod.source.OWNERS[-1],
            "other-anchor": root / mod.BASELINE,
        }[kind]
        path.write_bytes(path.read_bytes() + b"\n")
    with pytest.raises(ValueError):
        mod._captured_sources(root, source, proof)


@pytest.mark.parametrize("kind", ["proof", "anchor", "symlink"])
def test_capture_reserves_every_output_before_any_proof_bytes(case, native_runtime, kind):
    root, source, proof, _ = case
    mod.source.apply_sources(root, source, apply=True)
    anchor_paths = mod.capture_anchors(proof)
    path = next(iter(anchor_paths.values())) if kind == "anchor" else proof
    if kind == "symlink":
        foreign = proof.parent / "foreign"
        foreign.write_bytes(b"competitor")
        path.symlink_to(foreign)
    else:
        path.write_bytes(b"competitor")
    with pytest.raises((ValueError, FileExistsError)):
        mod.capture_sources(root, source, proof, apply=True)
    assert path.read_bytes() == b"competitor"
    assert not any(p.exists() for p in anchor_paths.values() if p != path)


def test_capture_parent_swap_at_acquisition_writes_no_foreign_files(
    case, native_runtime, monkeypatch
):
    root, source, _, _ = case
    mod.source.apply_sources(root, source, apply=True)
    parent = source.parent / "capture-dir"
    parent.mkdir()
    proof = parent / "capture.json"
    foreign = source.parent / "foreign"
    foreign.mkdir()
    retained = source.parent / "retained"
    opened = os.open

    def race(path, flags, *args, **kwargs):
        if path == parent and kwargs.get("dir_fd") is None:
            parent.rename(retained)
            parent.symlink_to(foreign, target_is_directory=True)
        return opened(path, flags, *args, **kwargs)

    monkeypatch.setattr(os, "open", race)
    with pytest.raises((ValueError, OSError)):
        mod.capture_sources(root, source, proof, apply=True)
    assert list(foreign.iterdir()) == list(retained.iterdir()) == []


def test_capture_late_alias_stays_in_owned_descriptors(case, native_runtime, monkeypatch):
    root, source, _, _ = case
    mod.source.apply_sources(root, source, apply=True)
    parent = source.parent / "capture-dir"
    parent.mkdir()
    proof = parent / "capture.json"
    foreign = source.parent / "foreign"
    foreign.mkdir()
    retained = source.parent / "retained"
    write = mod.write_fd
    fired = []

    def race(fd, data):
        if not fired:
            parent.rename(retained)
            parent.symlink_to(foreign, target_is_directory=True)
            fired.append(True)
        return write(fd, data)

    monkeypatch.setattr(mod, "write_fd", race)
    with pytest.raises(ValueError, match="parent changed"):
        mod.capture_sources(root, source, proof, apply=True)
    assert not list(foreign.iterdir()) and len(list(retained.iterdir())) == 3


_GEN = r"""
import importlib.util,json,sys,yaml
from pathlib import Path
producer,root,kg,bundle=map(Path,sys.argv[1:])
entry=producer/'scripts/build_mim_ingredient_sssom.py'
spec=importlib.util.spec_from_file_location('stock_cas_native_fixture_generation',entry)
b=importlib.util.module_from_spec(spec);sys.modules[spec.name]=b
exec(compile(entry.read_bytes(),str(entry),'exec'),b.__dict__)
records={path:yaml.safe_load(path.read_bytes()) for path in sorted((root/'data/ingredients/mapped').glob('*.yaml'))}
owners=b.build_owner_index({b._mim_curie(path.name):data for path,data in records.items()})
labels={}
sources=b.load_kgm_source_index(kg);klabels=b.load_kgm_labels(kg)
rows=[];events=[]
for path,record in records.items():rows.extend(b._row_from_yaml(path,{},sources,klabels,labels,record=record,owners=owners,suppressions=events))
rows=list({(r['subject_id'],r['object_id']):r for r in rows}.values())
b.apply_replayed_stamps(rows,b._load_existing_validation_method(root/'mappings/ingredient_mappings.sssom.tsv'))
b._write_sssom(rows,bundle/'candidate.sssom.tsv')
errors=b._sssom_validate(bundle/'candidate.sssom.tsv')
if errors:raise ValueError(errors)
(bundle/'suppressed_aliases.tsv').write_bytes(b.render_suppressed_aliases(events))
(bundle/'label-input-01.json').write_text(json.dumps({'loader':'immutable-test-labels','labels':labels}))
print(json.dumps({'rows':len(rows),'labels':labels}))
"""


def stock_producer_path():
    """Keep this producer pin separate from historical owned-name fixtures (#1103)."""
    producer_env = os.environ.get("MIM_STOCK_CAS_PRODUCER_ROOT")
    if not producer_env:
        pytest.skip("Explicit MIM_STOCK_CAS_PRODUCER_ROOT required for native integration")
    producer = Path(producer_env).resolve()
    revision = mod.native.git(producer, "rev-parse", "HEAD").decode().strip()
    if revision != mod.PRODUCER:
        pytest.fail("Stock-CAS producer context does not match its immutable revision")
    return producer


def test_stock_producer_context_does_not_substitute_historical_pin(tmp_path, monkeypatch):
    historical = tmp_path / "historical-owned-name"
    stock = tmp_path / "stock-cas"
    historical.mkdir()
    stock.mkdir()
    monkeypatch.setenv("MIM_OWNED_NAME_PRODUCER_ROOT", str(historical))
    monkeypatch.delenv("MIM_STOCK_CAS_PRODUCER_ROOT", raising=False)
    calls = []

    def revision(root, *args):
        calls.append((root, args))
        assert args == ("rev-parse", "HEAD")
        return (
            mod.PRODUCER if root == stock.resolve() else "9bd09b2ba163212a65289b91313f98cb0937476f"
        ).encode()

    monkeypatch.setattr(mod.native, "git", revision)
    with pytest.raises(pytest.skip.Exception, match="MIM_STOCK_CAS_PRODUCER_ROOT"):
        stock_producer_path()
    assert not calls
    monkeypatch.setenv("MIM_STOCK_CAS_PRODUCER_ROOT", str(historical))
    with pytest.raises(pytest.fail.Exception, match="immutable revision"):
        stock_producer_path()
    monkeypatch.setenv("MIM_STOCK_CAS_PRODUCER_ROOT", str(stock))
    assert stock_producer_path() == stock.resolve()
    assert [root for root, _ in calls] == [historical.resolve(), stock.resolve()]


@pytest.fixture
def native_case(captured, native_runtime, tmp_path, anchors):
    producer = stock_producer_path()
    root, source_log, proof, promotion_log = captured
    before = anchors
    for args in [
        ("init", "-q"),
        ("add", "."),
        (
            "-c",
            "user.name=Fixture",
            "-c",
            "user.email=fixture@example.invalid",
            "commit",
            "-qm",
            "immutable source checkpoint",
        ),
    ]:
        mod.native.git(root, *args)
    revision = mod.native.git(root, "rev-parse", "HEAD").decode().strip()
    bundle = tmp_path.resolve() / "candidate"
    bundle.mkdir()
    kgroot = tmp_path.resolve() / "kg"
    kg = kgroot / "mappings/kgmicrobe_unified_entity_mappings.sssom.tsv.gz"
    kg.parent.mkdir(parents=True)
    fields = ["subject_id", "subject_label", "predicate_id", "object_id", "object_label", "source"]
    kg.write_bytes(
        gzip.compress(
            tsv(
                fields,
                [
                    dict(
                        zip(
                            fields,
                            [
                                "test:stock",
                                "Stock",
                                "skos:exactMatch",
                                mod.IDENTITY,
                                "Stock",
                                "fixture",
                            ],
                            strict=True,
                        )
                    )
                ],
            ),
            mtime=0,
        )
    )
    result = subprocess.run(
        [sys.executable, "-I", "-c", _GEN, str(producer), str(root), str(kg), str(bundle)],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, result.stderr
    produced = json.loads(result.stdout)
    producers = mod.native.producer_paths(producer)
    mapped = set((root / "data/ingredients/mapped").glob("*.yaml"))
    residual = producer / "workspace/reports/kg_microbe_residual_p25_categorized.json"
    assert not residual.exists(), "Native fixture requires currently absent optional residual"
    declared = {
        path: mod.digest(path.read_bytes()) for path in mapped | producers | {kg, root / mod.SSSOM}
    }
    declared[residual] = None
    inventory = {
        str(path): {"sha256": sha, "bytes": path.stat().st_size}
        for path, sha in declared.items()
        if sha is not None
    }
    for name in ("inputs-before.json", "inputs-after.json"):
        (bundle / name).write_bytes(mod.encoded(inventory))
    manifest = {
        "schema_version": 1,
        "policy_version": "owned-name-policy-v1",
        "external_sssom_validation": "passed",
        "source_revisions": {
            "claw": mod.PRODUCER,
            "mim": revision,
            "kg_microbe": "fixture-ignored-input",
        },
        "artifacts": [
            {
                "path": str(bundle / name),
                "role": role,
                "sha256": mod.digest((bundle / name).read_bytes()),
            }
            for name, role in [
                ("candidate.sssom.tsv", "sssom"),
                ("suppressed_aliases.tsv", "suppressed_aliases"),
            ]
        ],
        "producer_import_snapshot": {str(path): declared[path] for path in producers},
        "mapped_record_paths": list(map(str, sorted(mapped))),
        "source_inputs": [
            {"path": str(path), "sha256": sha} for path, sha in sorted(declared.items())
        ],
        "canonical_label_resolution": produced["labels"],
        "prior_stamp_sources": [str(root / mod.SSSOM)],
        "emitted_rows": produced["rows"],
    }
    mpath = bundle / "candidate.sssom.tsv.manifest.json"
    mpath.write_bytes(mod.encoded(manifest))
    entry = declared[producer / "scripts/build_mim_ingredient_sssom.py"]
    receipt = {
        "input_bytes_unchanged": True,
        "scientific_approval_added": False,
        "supervisor_binding": None,
        "producer_revision": mod.PRODUCER,
        "candidate_sha256": manifest["artifacts"][0]["sha256"],
        "sidecar_sha256": manifest["artifacts"][1]["sha256"],
        "native_generation_manifest_sha256": mod.digest(mpath.read_bytes()),
        "input_manifest_sha256": mod.digest((bundle / "inputs-before.json").read_bytes()),
        "executed_entry_source_sha256": entry,
        "producer_sha256": entry,
        "label_maps": {
            "label-input-01.json": mod.digest((bundle / "label-input-01.json").read_bytes())
        },
        "prior_stamps": str(root / mod.SSSOM),
        "prior_sha256": mod.BEFORE[mod.SSSOM],
    }
    (bundle / "generation-receipt.json").write_bytes(mod.encoded(receipt))
    context = {
        key: {"path": str(path), "revision": rev, "status": ""}
        for key, path, rev in [
            ("mim", root, revision),
            ("claw", producer, mod.PRODUCER),
            ("kg_microbe", kgroot, "fixture-ignored-input"),
        ]
    }
    (bundle / "repository-context.json").write_bytes(mod.encoded(context))
    return (
        root,
        bundle,
        producer,
        source_log,
        proof,
        promotion_log,
        mod.digest(mpath.read_bytes()),
        before,
    )


def promote(case, apply=False):
    root, bundle, producer, source, proof, log, sha, _ = case
    return mod.promote(
        root, bundle, producer, source, proof, log, generation_manifest_sha256=sha, apply=apply
    )


def test_real_native_candidate_replay_promotion_and_posttransition_source_proof(native_case):
    root, _, _, source, proof, log, _, before = native_case
    assert promote(native_case)["applied"] is False and not log.exists()
    result = promote(native_case, True)
    assert (
        result["applied"] is True
        and result["validation_stamp_override"]["native_candidate"] == mod.OLD_STAMP
    )
    assert set(result["transaction"]["changed"]) == {str(root / p) for p in mod.OUTPUTS}
    assert result["transaction"]["created"] == []
    # The old frozen API intentionally refuses the changed two anchors.
    with pytest.raises(ValueError, match="Protected anchor changed"):
        mod.source.source_receipt(root, source)
    inputs, verified = mod.verify_completed(root, log, source_log=source, source_proof=proof)
    assert len(verified["records"]) == 15 and verified["approval"].startswith("NONE:")
    assert promote(native_case, True)["changed"] is False
    mod.native.git(
        root, "remote", "add", "origin", "https://github.com/CultureBotAI/MediaIngredientMech.git"
    )
    env = dict(
        os.environ,
        MEDIAINGREDIENTMECH_ROOT=str(root),
        OPENCLAW_WORKSPACE=str(root.parent / "cli-workspace"),
    )
    cli = subprocess.run(
        [
            sys.executable,
            "-B",
            str(ROOT / "scripts/promote_stock_cas_removal.py"),
            "verify-completed",
            "--root",
            str(root),
            "--source-log",
            str(source),
            "--source-proof",
            str(proof),
            "--log",
            str(log),
        ],
        env=env,
        capture_output=True,
        text=True,
    )
    assert cli.returncode == 0, cli.stderr
    assert len(json.loads(cli.stdout)["records"]) == 15
    assert inputs[root / mod.SSSOM] == (root / mod.SSSOM).read_bytes()
    assert all(
        (root / p).read_bytes() == before[p] for p in mod.source.ANCHORS if p not in mod.OUTPUTS
    )


@pytest.mark.parametrize(
    "kind",
    [
        "candidate",
        "sidecar",
        "labels",
        "manifest",
        "owner",
        "source_receipt",
        "proof",
        "producer_code",
        "new_label",
        "inventory",
        "prefix",
    ],
)
def test_native_substitution_and_inventory_refusals(native_case, kind):
    root, bundle, producer, source, proof, log, sha, before = native_case
    if kind == "producer_code":
        # Alter the captured producer hash declaration; never mutate the shared isolated producer.
        path = bundle / "candidate.sssom.tsv.manifest.json"
        doc = json.loads(path.read_bytes())
        key = next(iter(doc["producer_import_snapshot"]))
        doc["producer_import_snapshot"][key] = "0" * 64
        path.write_bytes(mod.encoded(doc))
    elif kind == "prefix":
        path = mod.capture_anchors(proof)[mod.MANIFEST]
        doc = json.loads(path.read_bytes())
        doc["form_projection_updates"] = []
        path.write_bytes(mod.encoded(doc))
    elif kind == "new_label":
        (bundle / "label-input-extra.json").write_text("{}")
    else:
        path = {
            "candidate": bundle / "candidate.sssom.tsv",
            "sidecar": bundle / "suppressed_aliases.tsv",
            "labels": bundle / "label-input-01.json",
            "manifest": bundle / "candidate.sssom.tsv.manifest.json",
            "owner": root / mod.source.OWNERS[-1],
            "source_receipt": source,
            "proof": proof,
            "inventory": bundle / "inputs-after.json",
        }[kind]
        path.write_bytes(path.read_bytes() + b"\n")
    with pytest.raises(ValueError):
        promote(native_case, True)
    assert not log.exists() and (root / mod.SSSOM).read_bytes() == before[mod.SSSOM]


def test_consistently_rehashed_wrong_native_candidate_refused(native_case):
    root, bundle, producer, source, proof, log, _, before = native_case
    path = bundle / "candidate.sssom.tsv"
    head, fields, rows = mod.table(path.read_bytes())
    objects = [r for r, _ in rows]
    objects[0]["object_label"] = "invented candidate label"
    path.write_bytes(tsv(fields, objects, "".join(head[:-1]).encode()))
    mpath = bundle / "candidate.sssom.tsv.manifest.json"
    m = json.loads(mpath.read_bytes())
    m["artifacts"][0]["sha256"] = mod.digest(path.read_bytes())
    mpath.write_bytes(mod.encoded(m))
    rpath = bundle / "generation-receipt.json"
    r = json.loads(rpath.read_bytes())
    r["candidate_sha256"] = mod.digest(path.read_bytes())
    r["native_generation_manifest_sha256"] = mod.digest(mpath.read_bytes())
    rpath.write_bytes(mod.encoded(r))
    with pytest.raises(ValueError, match="native replay"):
        mod.promote(
            root,
            bundle,
            producer,
            source,
            proof,
            log,
            generation_manifest_sha256=mod.digest(mpath.read_bytes()),
            apply=True,
        )
    assert not log.exists() and (root / mod.SSSOM).read_bytes() == before[mod.SSSOM]


@pytest.mark.parametrize("kind", ["candidate", "new-owner", "new-label", "alias", "receipt"])
def test_precommit_race_or_reservation_refuses(native_case, monkeypatch, kind):
    root, bundle, _, _, _, log, _, before = native_case
    if kind == "receipt":
        log.write_bytes(b"competitor")
        with pytest.raises(FileExistsError):
            promote(native_case, True)
        assert log.read_bytes() == b"competitor"
    else:
        reserve = mod.guarded.reserve_receipt_outputs

        @contextmanager
        def race(*args, **kwargs):
            with reserve(*args, **kwargs) as handles:
                if kind == "new-owner":
                    p = root / "data/ingredients/mapped/.ignored/extra.yaml"
                    p.parent.mkdir()
                    p.write_bytes(mod.source.frozen(mod.OWNER))
                elif kind == "new-label":
                    (bundle / "label-input-extra.json").write_text("{}")
                elif kind == "alias":
                    p = bundle / "candidate.sssom.tsv"
                    q = bundle / "original-candidate"
                    p.rename(q)
                    p.symlink_to(q)
                else:
                    p = bundle / "candidate.sssom.tsv"
                    p.write_bytes(p.read_bytes() + b"\n")
                yield handles

        monkeypatch.setattr(mod.guarded, "reserve_receipt_outputs", race)
        with pytest.raises(Exception, match="changed|aliased|differs"):
            promote(native_case, True)
        assert json.loads(log.read_bytes())["state"] == "failed"
    assert (root / mod.SSSOM).read_bytes() == before[mod.SSSOM]


def test_partial_native_promotion_keeps_recovery_evidence(native_case, monkeypatch):
    from kg_microbe_write import transaction

    root, _, _, _, _, log, _, before = native_case
    replace = transaction._atomic_replace

    def fail_manifest(path, text):
        if path == root / mod.MANIFEST:
            raise OSError("injected second replacement failure")
        return replace(path, text)

    monkeypatch.setattr(transaction, "_atomic_replace", fail_manifest)
    with pytest.raises(Exception, match="write failed after 1"):
        promote(native_case, True)
    saved = json.loads(log.read_bytes())
    assert saved["state"] == "failed" and saved["recovery_required"] is True
    journal = list(Path(saved["journal_directory"]).glob("write-*.json"))
    assert len(journal) == 1
    assert transaction.recover(journal[0]) == {
        str(root / p): before[p].decode() for p in mod.OUTPUTS
    }


def test_cli_missing_arguments_refuses_without_any_work(tmp_path):
    p = subprocess.run(
        [
            sys.executable,
            "-I",
            "-B",
            str(ROOT / "scripts/promote_stock_cas_removal.py"),
            "promote",
            "--source-log",
            str(tmp_path / "missing.json"),
            "--source-proof",
            str(tmp_path / "proof.json"),
        ],
        capture_output=True,
        text=True,
    )
    assert p.returncode == 2 and "promote requires" in p.stderr
    assert not list(tmp_path.iterdir())
