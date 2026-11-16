"""Cheap captured-producer adapter controls; full native proof is separate (#1426)."""

import base64
import copy
import json
from pathlib import Path
from types import ModuleType

import pytest

SOURCE = (
    Path(__file__).resolve().parents[1] / "src/mediaingredientmech/curate/stable_sssom_replay.py"
)
MODULE = ModuleType("_replay_contract_test")
exec(compile(SOURCE.read_bytes(), str(SOURCE), "exec"), MODULE.__dict__)

ENTRY = r"""
import json
import os
from pathlib import Path
from types import SimpleNamespace, ModuleType
MIM_ROOT = Path(os.environ["MEDIAINGREDIENTMECH_ROOT"])
KGM_ROOT = Path(os.environ["KGMICROBE_ROOT"])
RESIDUAL_JSON = Path(__file__).parent / "residual.json"
KGM_UNIFIED_TSV = KGM_ROOT / "mapping.tsv.gz"
MIM_PUBLISHED_SSSOM = MIM_ROOT / "mappings/ingredient_mappings.sssom.tsv"
_IMPORTED_PRODUCER_BYTES = {}
OWNED_NAME_EVIDENCE = []
_ARTIFACT_PRODUCER = SimpleNamespace(POLICY_VERSION="synthetic-v1")
def _check_producer_bindings():
    pass
def _producer_paths():
    return [Path(__file__)]
def _read_mapped_records(directory, snapshot, **kwargs):
    return {p: json.loads(snapshot[p]) for p in sorted(directory.glob("*.yaml"), reverse=REVERSE)}
def identity(root, records, *args):
    return {p: r["mim_id"] for p, r in records.items()}, {}, "https://example.invalid/mim/"
def compatibility(*args, **kwargs):
    return {}
_STABLE_PRODUCER = SimpleNamespace(identity_snapshot=identity, compatibility_registry_objects=compatibility)
def build_owner_index(records):
    return {}
def render_suppressed_aliases(rows):
    return b"synthetic suppressions\n"
def _write_sssom(rows, path, **kwargs):
    path.write_bytes(json.dumps(rows, sort_keys=True).encode())
"""
NEW = r"""
def contract(source, path):
    if source is None:
        return None
    captured = ModuleType("_captured_test_contract")
    exec(compile(source, str(path), "exec"), captured.__dict__)
    return captured
_STABLE_PRODUCER.additional_mapping_contract = contract
def _row_from_yaml(path, *args, record, additional_contract=None, **kwargs):
    if record.get("additional") and additional_contract is None:
        raise ValueError("additional assertions require captured contract")
    return record["rows"] + ([] if additional_contract is None else additional_contract.rows(record))
"""
OLD = r"""
def _row_from_yaml(path, *args, record, owners, suppressions, stable_subject, registry_objects):
    return record["rows"]
"""
CONTRACT = b"def rows(record):\n    return record.get('additional', [])\n"


def fixture(tmp_path, monkeypatch, *, modern=True, reverse=False, extras=True, absent=False):
    root, claw, kg = (tmp_path / name for name in ("mim", "claw", "kg"))
    monkeypatch.setenv("MEDIAINGREDIENTMECH_ROOT", str(root))
    monkeypatch.setenv("KGMICROBE_ROOT", str(kg))
    entry = claw / "scripts/build_mim_ingredient_sssom.py"
    entry.parent.mkdir(parents=True)
    entry.write_text(ENTRY.replace("REVERSE", str(reverse)) + (NEW if modern else OLD))
    snapshot = {entry: entry.read_bytes()}
    for name, subject in (("Z.yaml", "MIM:2"), ("A.yaml", "MIM:1")):
        path = root / "data/ingredients/mapped" / name
        path.parent.mkdir(parents=True, exist_ok=True)
        record = {
            "mim_id": subject,
            "mapping_status": "MAPPED",
            "rows": [
                {
                    "subject_id": subject,
                    "object_id": "NCIT:primary",
                    "predicate_id": "skos:exactMatch",
                }
            ],
        }
        if extras and name == "A.yaml":
            record["additional"] = [
                {
                    "subject_id": subject,
                    "object_id": "NCIT:broad",
                    "predicate_id": "skos:broadMatch",
                    "status": "SUPPORTED",
                },
                {
                    "subject_id": subject,
                    "object_id": "NCIT:held",
                    "predicate_id": "skos:closeMatch",
                    "status": "WITHHOLD",
                },
            ]
        path.write_text(json.dumps(record))
        snapshot[path] = path.read_bytes()
    (root / "data/ingredients/unmapped").mkdir()
    for path in (
        root / "data/ids/mim_id_registry.tsv",
        root / "data/ids/mim_id_lifecycle.tsv",
        root / "src/mediaingredientmech/stable_ids.py",
    ):
        snapshot[path] = b"synthetic identity contract input"
    for path in (
        entry.parent / "residual.json",
        kg / "mapping.tsv.gz",
        root / "mappings/ingredient_mappings.sssom.tsv",
    ):
        snapshot[path] = None
    source = root / "src/mediaingredientmech/additional_mappings.py"
    if modern:
        snapshot[source] = None if absent else CONTRACT
    source.parent.mkdir(parents=True)
    source.write_text("raise AssertionError('ambient contract must never execute')\n")
    return {
        "root": str(root),
        "claw": str(claw),
        "kg_microbe": str(kg),
        "inputs": {
            str(p): None if raw is None else base64.b64encode(raw).decode()
            for p, raw in snapshot.items()
        },
        "canonical_label_resolution": {},
        "source_revisions": {"claw": "synthetic", "mim": "synthetic", "kg_microbe": "synthetic"},
        "outputs": {
            "sssom": str(root / "candidate.tsv"),
            "suppressions": str(root / "suppressed.tsv"),
        },
    }, source


def decoded(request):
    return {name: base64.b64decode(raw) for name, raw in MODULE.replay(request).items()}


def test_captured_contract_keeps_supported_and_withheld_rows(tmp_path, monkeypatch):
    request, source = fixture(tmp_path, monkeypatch)
    output = decoded(request)
    assert [(row["object_id"], row.get("status")) for row in json.loads(output["sssom"])] == [
        ("NCIT:primary", None),
        ("NCIT:broad", "SUPPORTED"),
        ("NCIT:held", "WITHHOLD"),
        ("NCIT:primary", None),
    ]
    inputs = {row["path"]: row["sha256"] for row in json.loads(output["manifest"])["source_inputs"]}
    assert inputs[str(source)] == MODULE.digest(CONTRACT)
    changed = copy.deepcopy(request)
    changed["inputs"][str(source)] = base64.b64encode(
        CONTRACT.replace(b"record.get('additional', [])", b"[]")
    ).decode()
    assert decoded(changed)["sssom"] != output["sssom"]
    assert decoded(changed)["manifest"] != output["manifest"]


@pytest.mark.parametrize("change", ["omitted", "unexpected"])
def test_complete_capture_membership_remains_required(tmp_path, monkeypatch, change):
    request, source = fixture(tmp_path, monkeypatch)
    if change == "omitted":
        del request["inputs"][str(source)]
    else:
        request["inputs"][str(source.with_name("unrecorded.py"))] = None
    with pytest.raises(ValueError, match="complete native generation input membership differs"):
        decoded(request)


def test_absent_contract_cannot_erase_owner_assertions(tmp_path, monkeypatch):
    request, _ = fixture(tmp_path, monkeypatch, absent=True)
    with pytest.raises(ValueError, match="additional assertions require captured contract"):
        decoded(request)


@pytest.mark.parametrize("modern", [False, True])
def test_old_signature_and_explicit_absence_remain_compatible(tmp_path, monkeypatch, modern):
    request, source = fixture(tmp_path, monkeypatch, modern=modern, extras=False, absent=True)
    output = decoded(request)
    assert len(json.loads(output["sssom"])) == 2
    inputs = {row["path"]: row["sha256"] for row in json.loads(output["manifest"])["source_inputs"]}
    if modern:
        assert inputs[str(source)] is None
    else:
        assert str(source) not in inputs
        request["inputs"][str(source)] = None
        with pytest.raises(ValueError, match="complete native generation input membership differs"):
            decoded(request)


def test_owner_order_and_last_duplicate_match_generator(tmp_path, monkeypatch):
    request, _ = fixture(tmp_path, monkeypatch, reverse=True, extras=False)
    a = next(path for path in request["inputs"] if path.endswith("/A.yaml"))
    record = json.loads(base64.b64decode(request["inputs"][a]))
    record["rows"].append({**record["rows"][0], "predicate_id": "skos:broadMatch", "last": True})
    request["inputs"][a] = base64.b64encode(json.dumps(record).encode()).decode()
    output = decoded(request)
    rows = json.loads(output["sssom"])
    assert [row["subject_id"] for row in rows] == ["MIM:1", "MIM:2"]
    assert rows[0]["last"] is True and rows[0]["predicate_id"] == "skos:broadMatch"
    paths = json.loads(output["manifest"])["mapped_record_paths"]
    assert paths == sorted(paths)
