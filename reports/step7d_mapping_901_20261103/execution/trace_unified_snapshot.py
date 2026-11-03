"""Replay and trace the Step7d unified pair using pinned native code and bytes.

Writes only a new external evidence directory and private temporary fixture
trees. It never writes, stamps or promotes maintained outputs. Untraced cells
are saved as failures; a successful native replay alone does not approve them.
"""
from pathlib import Path
from collections import Counter, defaultdict
from datetime import datetime
import argparse
import copy
import csv
import gzip
import hashlib
import importlib.util
import io
import json
import os
import stat
import subprocess
import sys
import tarfile
import tempfile

import yaml

D = Path(__file__).resolve().parent
TRACER_RAW = Path(__file__).read_bytes()
R = D.parent
W = R / "step7d"
C = R / "step7c-claw"
CULTURE = Path("/Users/marcin/Documents/VIMSS/ontology/Mechs/CultureMech")
BASE = "467aa319a06ef992035f509f66fe251082b44ae1"
PRODUCER = "3022b8738dcc9e01c7464a8d5c95aa9be2eef141"
CULTURE_REV = "a74dd489720c9df96cc073ffd11568d407d3c06c"
PLAN_SHA = "a82bc6d32e750f16fc7ecfa4c0a5e172a5930c849d7dc3ec5a6ca106ed60fca4"
SOURCE_SHA = "965f29ff2c35e789be007f2177a12b0c463c7a2ec4c5671b71433ef8038c99d0"
PRODUCER_SHA = "26d0c6808728ddaef5201ccebe24fff8c4174c4a5b37753e79c671a628c521d1"
BEFORE_SHA = "1edaba0f0f2d1afb84129a2ba185963a2cdf3e9b982690fdfd610df1fd78cc88"
TSV = "UNIFIED_INGREDIENT_MAPPING.tsv"
PROVENANCE = "UNIFIED_INGREDIENT_MAPPING.provenance.json"
LABEL = "docs/data/label_index.csv"
LEDGER = "mappings/unified_mapping_rejections.tsv"
COLLECTIONS = tuple("data/curated/" + category + "_ingredients.yaml" for category in ("mapped", "unmapped"))
sha = lambda raw: hashlib.sha256(raw).hexdigest()
enc = lambda value: (json.dumps(value, indent=2, sort_keys=True, ensure_ascii=False) + "\n").encode()


def require(ok, reason):
    if not ok:
        raise ValueError("Step7d unified trace: " + reason)


def regular(path):
    path = Path(path).absolute()
    require(path == path.resolve(), "aliased input/output path: " + str(path))
    info = path.lstat()
    require(stat.S_ISREG(info.st_mode) and info.st_nlink == 1, "nonregular or hardlinked input: " + str(path))
    return path.read_bytes()


def git(root, *args):
    return subprocess.check_output(["git", *args], cwd=root, env={**os.environ, "GIT_OPTIONAL_LOCKS": "0"})


def load(name, path, expected=None):
    raw = regular(path)
    if expected:
        require(sha(raw) == expected, "executed module pin differs: " + str(path))
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    exec(compile(raw, str(path), "exec"), module.__dict__)
    return module, raw


def native_input_paths():
    paths = set((CULTURE / "data/normalized_yaml").rglob("*.yaml"))
    for category in ("mapped", "unmapped"):
        paths.update((W / "data/ingredients" / category).glob("*.yaml"))
    paths.update(W / name for name in (LABEL, LEDGER, TSV, PROVENANCE))
    paths.update(C / name for name in ("scripts/build_unified_ingredient_mapping.py", "plugins/ingredient_name_normalizer.py",
                                      "plugins/__init__.py", "src/kg_microbe_fleet/fleet.yaml"))
    paths.update((C / "src/kg_microbe_fleet").rglob("*.py"))
    return paths


def inventory(paths):
    result = {}
    for path in sorted(paths):
        raw = regular(path)
        result[str(path)] = {"sha256": sha(raw), "bytes": len(raw)}
    return result


def direct_paths(root):
    return sorted(path for category in ("mapped", "unmapped")
                  for path in (root / "data/ingredients" / category).glob("*.yaml"))


def unpack_base(destination):
    selected = ["data/ingredients", *COLLECTIONS, LABEL, LEDGER, TSV, PROVENANCE]
    archive = git(W, "archive", "--format=tar", BASE, *selected)
    with tarfile.open(fileobj=io.BytesIO(archive)) as stream:
        for member in stream.getmembers():
            require(member.isfile() or member.isdir(), "nonregular base archive member")
            require(not Path(member.name).is_absolute() and ".." not in Path(member.name).parts, "unsafe base archive member")
        stream.extractall(destination, filter="data")
    return sha(archive)


def identity(record):
    return json.dumps(record, sort_keys=True, ensure_ascii=False, default=str)


def records(root):
    return {str(path.relative_to(root)): yaml.safe_load(regular(path)) for path in direct_paths(root)}


def verify_collection_and_labels(root, exporter, expected_label):
    """Reproduce the native label export only after exact direct/collection equality."""
    data = records(root)
    combined = []
    for category, name in zip(("mapped", "unmapped"), COLLECTIONS, strict=True):
        collection = yaml.safe_load(regular(root / name))["ingredients"]
        expected = [copy.deepcopy(record) for path, record in data.items() if Path(path).parent.name == category]
        for record in expected:
            record.pop("discussions", None)  # native PER_RECORD_AUTHORED_FIELDS pin checked by caller
        require(Counter(map(identity, collection)) == Counter(map(identity, expected)),
                "collection does not exactly reproduce direct owners: " + category)
        combined.extend(collection)
    emitted = root / "native-label-index-replay.csv"
    exporter.export_label_index(combined, emitted)
    require(regular(emitted) == expected_label, "native label-index replay differs")
    return data


def encode_native(value):
    if isinstance(value, dict):
        return {key: encode_native(item) for key, item in value.items()}
    if isinstance(value, (set, frozenset)):
        return sorted(encode_native(item) for item in value)
    if isinstance(value, (tuple, list)):
        return [encode_native(item) for item in value]
    return value


def replay(native, root, occurrences):
    """Observe unchanged resolver results; never replace its choices."""
    data = records(root)
    paths_by_data = defaultdict(list)
    for path, record in data.items():
        paths_by_data[identity(record)].append(path)
    indexes = native.load_mim_index(root)
    names, chebi, ontology = indexes
    labels = native.load_mim_label_index(root)
    live = native.live_records(*indexes)
    rejections = native.load_mapping_rejections(root, names, label_index=labels, live=live)
    live_paths, retired_paths = defaultdict(set), defaultdict(set)
    for source, result in names.source_records:
        matching = paths_by_data[identity(source)]
        require(matching, "native source catalogue cannot be bound to input path")
        target = retired_paths if source.get("mapping_status") == "REJECTED" else live_paths
        target[id(result)].update(matching)

    def bind(record):
        if record is None:
            return {"owner_paths": [], "native_record": None}
        owners = live_paths.get(id(record)) or retired_paths.get(id(record)) or set()
        return {"owner_paths": sorted(owners), "native_record": encode_native(record)}

    original = native.resolve_mim_record
    trace = {}

    def observed(name, term_id, *args, **kwargs):
        result = original(name, term_id, *args, **kwargs)
        anchor = native._anchor_record(name, names, labels, live)
        ruled = native.label_ruling(name, names.get(native._normalize(name)), labels, live)
        trace[name] = {**bind(result), "raw_culturemech_term_id": occurrences[name]["term_id"],
                       "effective_term_id": term_id, "label_index_first_row": labels.get(native._label_key(name)),
                       "label_ruling": bind(ruled), "anchor": bind(anchor),
                       "published_ids": list(native._published_ids(term_id, result)),
                       "source_label_rejection": ["source_label", native._label_key(name), occurrences[name]["term_id"]]
                       if ("source_label", native._label_key(name), occurrences[name]["term_id"]) in rejections else None,
                       "owner_rejection": [anchor.get("mim_id"), occurrences[name]["term_id"]]
                       if anchor and (anchor.get("mim_id"), occurrences[name]["term_id"]) in rejections else None}
        return result

    native.resolve_mim_record = observed
    try:
        rows = native.build_unified_rows(occurrences, *indexes, rejections=rejections, label_index=labels)
    finally:
        native.resolve_mim_record = original
    destination = root / "native-unified-replay.tsv"
    native.write_tsv(rows, destination)
    require(set(trace) == set(occurrences), "resolver trace does not cover complete occurrence inventory")
    return regular(destination), trace, data


def table(raw):
    reader = csv.DictReader(io.StringIO(raw.decode(), newline=""), delimiter="\t")
    rows = list(reader)
    require(all(None not in row and None not in row.values() for row in rows), "malformed unified table")
    require(len({row["ingredient_name"] for row in rows}) == len(rows), "duplicate unified name")
    return reader.fieldnames, rows


def operation_refs(item, predicate):
    return [{"operation_index": i, "operation": operation} for i, operation in enumerate(item["operations"])
            if predicate(operation)]


def synonym_refs(token, old, new, item, native):
    references = []
    for i, operation in enumerate(item["operations"]):
        path = operation["path"]
        if path[0] == "synonyms":
            if len(path) > 1 and isinstance(path[1], int):
                index = path[1]
                old_syn = (old.get("synonyms") or [])[index]
                new_syn = (new.get("synonyms") or [])[index]
                texts = [native._synonym_text(value) for value in (old_syn, new_syn)]
            else:
                texts = [native._synonym_text(value) for record in (old, new) for value in (record.get("synonyms") or [])]
            if any(token in text.split("|") for text in texts):
                references.append({"operation_index": i, "operation": operation})
    old_label = native._identity_ontology_mapping(old).get("ontology_label") or ""
    new_label = native._identity_ontology_mapping(new).get("ontology_label") or ""
    if token in (old_label, new_label) and old_label != new_label:
        references.extend(operation_refs(item, lambda op: op["path"][:1] == ["ontology_mapping"]
                                          and len(op["path"]) > 1 and op["path"][1] in ("ontology_label", "mapping_quality")))
    return references


def trace_cell(name, column, old_cell, new_cell, before_trace, after_trace, old_data, new_data, plan, native):
    result = {"ingredient_name": name, "column": column, "before": old_cell, "after": new_cell,
              "before_resolution": before_trace, "after_resolution": after_trace, "status": "UNTRACED"}
    old_paths, new_paths = before_trace["owner_paths"], after_trace["owner_paths"]
    if len(old_paths) != 1 or old_paths != new_paths:
        return dict(result, reason="Owner-path change or ambiguous native binding requires explicit review; identifiers alone cannot settle it")
    owner = old_paths[0]
    if owner not in plan["owners"]:
        return dict(result, reason="Changed cell belongs to an unselected owner")
    item = plan["owners"][owner]
    result.update(owner_path=owner, source_group=item["group"], before_owner_sha256=item["before_sha256"],
                  after_owner_sha256=item["after_sha256"], scientific_approval_added=False)
    refs = []
    if column == "mim_id":
        refs = operation_refs(item, lambda op: op["path"] == ["identifier"] and op["before"] == old_cell and op["after"] == new_cell)
        result["native_basis"] = "load_mim_index.record.mim_id -> build_unified_rows.mim_id"
    elif column == "cas_rn":
        refs = operation_refs(item, lambda op: op["path"] == ["chemical_properties", "cas_rn"]
                              and (op["before"] or "") == old_cell and (op.get("after") or "") == new_cell)
        result["native_basis"] = "load_mim_index.record.cas_rn -> build_unified_rows.cas_rn"
    elif column == "synonyms":
        old_tokens, new_tokens = set(filter(None, old_cell.split("|"))), set(filter(None, new_cell.split("|")))
        differences = [(token, "removed") for token in sorted(old_tokens - new_tokens)] + [(token, "added") for token in sorted(new_tokens - old_tokens)]
        token_traces = [{"token": token, "change": kind,
                         "operations": synonym_refs(token, old_data[owner], new_data[owner], item, native)}
                        for token, kind in differences]
        result["token_traces"] = token_traces
        if not token_traces or any(not token["operations"] for token in token_traces):
            return dict(result, reason="A changed synonym token has no exact reviewed alias/equivalence-label operation")
        refs = [ref for token in token_traces for ref in token["operations"]]
        result["native_basis"] = "load_mim_index._identity_ontology_mapping/_is_publishable_mim_synonym/rejected-name filters -> sorted synonyms"
    elif column in {"chebi_id", "culturemech_term_id"}:
        index = 0 if column == "chebi_id" else 1
        require(before_trace["published_ids"][index] == old_cell and after_trace["published_ids"][index] == new_cell,
                "native published-ID trace differs from row cell")
        refs = operation_refs(item, lambda op: op["path"] == ["identifier"])
        if before_trace["effective_term_id"] != after_trace["effective_term_id"]:
            migrations = [stage for stage in plan["auxiliary"].get(LEDGER, [])
                          if any(migration["owner_path"] == owner for migration in stage["migrations"])]
            if not migrations:
                return dict(result, reason="Effective source-ID change lacks this owner's reviewed ledger migration")
            result["ledger_stages"] = migrations
        result["native_basis"] = "observed native source rejection and _published_ids on this owner's exact identifier transition"
    else:
        return dict(result, reason="This column has no approved source operation class")
    if not refs:
        return dict(result, reason="No precise reviewed operation supports the changed cell")
    unique = {ref["operation_index"]: ref for ref in refs}
    return dict(result, status="TRACED", operations=[unique[index] for index in sorted(unique)])


def run(args):
    out = Path(args.out).absolute()
    require(out == out.resolve() and out.is_relative_to(D) and out != D and not os.path.lexists(out)
            and out.parent.is_dir(), "new resolved external output directory required")
    baseline_input_raw = regular(D / "unified-baseline/inputs-before.json.gz")
    baseline_inputs = json.loads(gzip.decompress(baseline_input_raw))
    baseline_paths = {Path(path) for path in baseline_inputs}
    require(native_input_paths() == baseline_paths, "native input membership differs from baseline")
    inputs_before = inventory(baseline_paths)
    require(git(C, "rev-parse", "HEAD").decode().strip() == PRODUCER, "producer revision changed")
    require(git(CULTURE, "rev-parse", "HEAD").decode().strip() == CULTURE_REV, "CultureMech revision changed")
    head = git(W, "rev-parse", "HEAD").decode().strip()
    if not args.baseline_only:
        require(args.mim_head == head and not git(W, "status", "--porcelain", "--untracked-files=all"), "clean explicit MIM checkpoint required")
    plan_raw = regular(D / "owner-plan.json")
    require(sha(plan_raw) == PLAN_SHA, "owner plan changed")
    plan = json.loads(plan_raw)
    sys.path[:0] = [str(C), str(C / "src"), str(W), str(W / "src")]
    native, native_raw = load("step7d_native_unified_trace", C / "scripts/build_unified_ingredient_mapping.py", PRODUCER_SHA)
    source, source_raw = load("step7d_source_reference_trace", D / "apply_reviewed_owners.py", SOURCE_SHA)
    exporter_path = W / "scripts/export_lists.py"
    exporter, exporter_raw = load("step7d_native_label_trace", exporter_path)
    checker, checker_raw = load("step7d_native_freshness_trace", W / "scripts/check_unified_freshness.py")
    for path, raw in ((exporter_path, exporter_raw), (W / "scripts/check_unified_freshness.py", checker_raw)):
        require(raw == git(W, "show", BASE + ":" + str(path.relative_to(W))), "native MIM helper changed")
    exporter_contract = regular(W / "scripts/export_individual_records.py")
    require(exporter_contract == git(W, "show", BASE + ":scripts/export_individual_records.py")
            and 'PER_RECORD_AUTHORED_FIELDS: tuple[str, ...] = ("discussions",)' in exporter_contract.decode(), "per-record field contract differs")
    consumed_mim = {Path(path).relative_to(W).as_posix() for path in baseline_inputs if Path(path).is_relative_to(W)}
    allowed = set(plan["owners"]) | {LABEL, LEDGER, TSV, PROVENANCE}
    changed_inputs = []
    for path, current in inputs_before.items():
        prior = baseline_inputs[path]
        if current["sha256"] != prior["sha256"]:
            require(Path(path).is_relative_to(W) and str(Path(path).relative_to(W)) in allowed,
                    "unaccounted changed native input: " + path)
            changed_inputs.append({"path": path, "before_sha256": prior["sha256"], "after_sha256": current["sha256"]})
    occurrences = native.scan_culturemech(CULTURE)
    outputs = {}
    extra_inputs = {D / "owner-plan.json": plan_raw, D / "unified-baseline/inputs-before.json.gz": baseline_input_raw}
    with tempfile.TemporaryDirectory(prefix="mim-step7d-unified-trace-") as directory:
        temp = Path(directory).resolve()
        before_root, after_root = temp / "before", temp / "after"
        before_root.mkdir()
        archive_sha = unpack_base(before_root)
        before_snapshot = regular(before_root / TSV)
        require(sha(before_snapshot) == BEFORE_SHA
                and before_snapshot == regular(D / "unified-baseline/output/unified-diagnostic.tsv"), "native baseline reference changed")
        base_records = direct_paths(before_root)
        require({str(path.relative_to(before_root)) for path in base_records} == set(plan["all_owner_sha256"]), "base owner inventory differs")
        for path in base_records:
            name = str(path.relative_to(before_root))
            require(sha(regular(path)) == plan["all_owner_sha256"][name], "plan/base owner hash mismatch")
        verify_collection_and_labels(before_root, exporter, regular(before_root / LABEL))
        before_replay, before_trace, old_data = replay(native, before_root, occurrences)
        require(before_replay == before_snapshot, "full native baseline replay differs")
        before_columns, before_rows = table(before_snapshot)
        result = {"scientific_approval_added": False, "supervisor_binding": None, "producer_revision": PRODUCER,
                  "producer_sha256": PRODUCER_SHA, "base_revision": BASE, "mim_checkpoint": head,
                  "baseline_archive_sha256": archive_sha, "baseline_tsv_sha256": BEFORE_SHA,
                  "baseline_native_replay_exact": True, "before_native_replay_exact": True, "baseline_drift_changed_cells": 0,
                  "changed_native_inputs": changed_inputs, "plan_sha256": PLAN_SHA,
                  "qualification": "Pinned native functions and complete output replay; exact data paths bind owners. No source, snapshot, sidecar, threshold, owner-selection rule or maintained test was changed."}
        if args.baseline_only:
            result.update(status="BASELINE_REPLAY_PASS_ONLY", after_pair_processed=False, rows=len(before_rows))
        else:
            pair = Path(args.after).absolute()
            require(pair == pair.resolve() and pair.is_dir(), "resolved after-pair directory required")
            after_raw, provenance_raw = regular(pair / TSV), regular(pair / PROVENANCE)
            require(sha(after_raw) == args.tsv_sha256 and sha(provenance_raw) == args.provenance_sha256, "after pair pins differ")
            after_root.mkdir()
            copy_names = {str(path.relative_to(before_root)) for path in base_records} | {LABEL, LEDGER, *COLLECTIONS}
            for name in sorted(copy_names):
                raw = regular(W / name)
                if name in COLLECTIONS:
                    extra_inputs[W / name] = raw
                if name in plan["all_owner_sha256"]:
                    expected = plan["owners"][name]["after_sha256"] if name in plan["owners"] else plan["all_owner_sha256"][name]
                    require(sha(raw) == expected, "current owner outside reviewed endpoint: " + name)
                target = after_root / name
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_bytes(raw)
            verify_collection_and_labels(after_root, exporter, regular(W / LABEL))
            ledger = regular(before_root / LEDGER)
            for stage in plan["auxiliary"][LEDGER]:
                ledger = source.propose_auxiliary(LEDGER, ledger, stage)
            require(ledger == regular(after_root / LEDGER), "planned rejection-ledger replay differs")
            after_replay, after_trace, new_data = replay(native, after_root, occurrences)
            require(after_replay == after_raw, "complete after TSV differs from unchanged native replay")
            columns, after_rows = table(after_raw)
            require(columns == before_columns and [r["ingredient_name"] for r in after_rows] == [r["ingredient_name"] for r in before_rows],
                    "snapshot columns, membership or row order changed")
            for old_row, new_row in zip(before_rows, after_rows, strict=True):
                require(all(old_row[field] == new_row[field] for field in ("ingredient_name", "occurrence_count", "example_media", "mapping_status")),
                        "snapshot membership/count/example/status change")
            provenance = json.loads(provenance_raw)
            require(set(provenance) == {"artifact", "artifact_sha256", "artifact_rows", "mim_inputs_digest", "mim_record_count", "mim_rev", "stamped_at"},
                    "native provenance shape differs")
            digest, count = checker.inputs_digest(after_root / "data/ingredients")
            require((digest, count) == checker.inputs_digest(W / "data/ingredients"), "private/current native freshness inputs differ")
            require(provenance["artifact"] == TSV and provenance["artifact_sha256"] == sha(after_raw)
                    and provenance["artifact_rows"] == len(after_rows) and provenance["mim_inputs_digest"] == digest
                    and provenance["mim_record_count"] == count and provenance["mim_rev"] == checker._git_rev(W),
                    "native provenance pair or input binding differs")
            datetime.strptime(provenance["stamped_at"], "%Y-%m-%dT%H:%M:%SZ")
            cells = []
            for position, (old_row, new_row) in enumerate(zip(before_rows, after_rows, strict=True), 1):
                name = old_row["ingredient_name"]
                for column in columns:
                    if old_row[column] != new_row[column]:
                        cell = trace_cell(name, column, old_row[column], new_row[column], before_trace[name], after_trace[name], old_data, new_data, plan, native)
                        cell.update(row_position=position, before_row=old_row, after_row=new_row)
                        cells.append(cell)
            untraced = [cell for cell in cells if cell["status"] != "TRACED"]
            result.update(status="PASS" if not untraced else "FAIL_UNTRACED_CELLS", after_pair_processed=True,
                          after_tsv_sha256=sha(after_raw), after_provenance_sha256=sha(provenance_raw),
                          after_native_replay_exact=True, native_provenance_verified=True, rows=len(after_rows),
                          changed_cells=len(cells), changed_rows=len({cell["row_position"] for cell in cells}),
                          changed_cell_columns=dict(Counter(cell["column"] for cell in cells)),
                          untraced_cells=len(untraced), all_changed_inputs_accounted_for=True)
            outputs["cell-traces.json"] = enc({"cells": cells, "untraced_cells": untraced})
            flat = io.StringIO(newline="")
            writer = csv.DictWriter(flat, fieldnames=["row_position", "ingredient_name", "column", "before", "after", "status", "owner_path", "source_group", "operation_indices", "reason"], delimiter="\t")
            writer.writeheader()
            for cell in cells:
                writer.writerow({**{key: cell.get(key, "") for key in writer.fieldnames if key != "operation_indices"},
                                 "operation_indices": ",".join(str(item["operation_index"]) for item in cell.get("operations", []))})
            outputs["cell-diff.tsv"] = flat.getvalue().encode()
            changed_names = {cell["ingredient_name"] for cell in cells}
            outputs["resolver-traces.json"] = enc({name: {"before": before_trace[name], "after": after_trace[name]} for name in sorted(changed_names)})
            outputs["native-provenance-verified.json"] = enc(provenance)
            outputs["after-pair-input-hashes.json"] = enc({str(pair / TSV): sha(after_raw), str(pair / PROVENANCE): sha(provenance_raw)})
            extra_inputs.update({pair / TSV: after_raw, pair / PROVENANCE: provenance_raw})
            cas_lookup = []
            for owner in plan["owners"]:
                data = new_data[owner]
                mapping = data.get("ontology_mapping") or {}
                if mapping.get("mapping_quality") != "CAS_RN_LOOKUP":
                    continue
                label = mapping.get("ontology_label") or ""
                surfaces = [data["preferred_term"]] + [native._synonym_text(synonym) for synonym in data.get("synonyms", [])
                                                       if native._is_publishable_mim_synonym(synonym)]
                cas_lookup.append({"owner_path": owner, "identifier": data["identifier"], "ontology_label": label,
                                   "native_identity_ontology_mapping": native._identity_ontology_mapping(data),
                                   "label_independently_present_casefolded": label.casefold() in {text.casefold() for text in surfaces},
                                   "actual_native_rows": [row for row in after_rows if row["mim_id"] == data["identifier"]]})
            outputs["cas-lookup-native-behavior.json"] = enc({"qualification": "Observed current selected-owner behavior; no producer policy edit or approval.",
                                                             "owners": cas_lookup})
            require(regular(pair / TSV) == after_raw and regular(pair / PROVENANCE) == provenance_raw, "after pair changed during tracing")
    require(native_input_paths() == baseline_paths and inventory(baseline_paths) == inputs_before,
            "native input bytes/membership changed during replay")
    require(git(W, "rev-parse", "HEAD").decode().strip() == head and git(C, "rev-parse", "HEAD").decode().strip() == PRODUCER
            and git(CULTURE, "rev-parse", "HEAD").decode().strip() == CULTURE_REV, "repository revision changed during trace")
    from mediaingredientmech.ingredient_bundle_refresh import publish_new_files
    require(regular(Path(__file__).resolve()) == TRACER_RAW, "tracer changed during execution")
    code_inputs = {str(Path(__file__).resolve()): sha(TRACER_RAW),
                   str(C / "scripts/build_unified_ingredient_mapping.py"): sha(native_raw), str(exporter_path): sha(exporter_raw),
                   str(W / "scripts/check_unified_freshness.py"): sha(checker_raw), str(D / "apply_reviewed_owners.py"): sha(source_raw)}
    for name, module in sys.modules.copy().items():
        location = getattr(module, "__file__", None)
        if location and Path(location).suffix == ".py" and Path(location).is_file():
            path = Path(location).resolve()
            if path.is_relative_to(W / "src") or path.is_relative_to(C / "src") or path.is_relative_to(C / "plugins"):
                raw = regular(path)
                root, rev = (W, BASE) if path.is_relative_to(W) else (C, PRODUCER)
                require(raw == git(root, "show", rev + ":" + str(path.relative_to(root))), "imported native module differs from pinned commit")
                code_inputs[str(path)] = sha(raw)
    outputs["trace-receipt.json"] = enc(result)
    outputs["executed-code-inputs.json"] = enc(code_inputs)
    outputs["native-input-inventory.json.gz"] = gzip.compress(enc(inputs_before), mtime=0)
    outputs["additional-proof-inputs.json"] = enc({str(path): sha(raw) for path, raw in extra_inputs.items()})
    out.mkdir(mode=0o700)
    # External evidence only; reserve all leaves before writing any content.
    def recheck():
        require(inventory(baseline_paths) == inputs_before, "inputs changed before evidence publication")
        require(all(regular(path) == raw for path, raw in extra_inputs.items()), "proof input changed before evidence publication")
        require(all(sha(regular(Path(path))) == digest for path, digest in code_inputs.items()), "executed code changed")
    publish_new_files([(out / name, raw) for name, raw in outputs.items()], recheck)
    print(json.dumps(result, indent=2))
    return 0 if result["status"] in {"PASS", "BASELINE_REPLAY_PASS_ONLY"} else 2


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", required=True, type=Path)
    parser.add_argument("--baseline-only", action="store_true")
    parser.add_argument("--after", type=Path, help="Directory containing the exact native snapshot pair")
    parser.add_argument("--tsv-sha256")
    parser.add_argument("--provenance-sha256")
    parser.add_argument("--mim-head")
    args = parser.parse_args()
    require(args.baseline_only or all((args.after, args.tsv_sha256, args.provenance_sha256, args.mim_head)),
            "full trace needs after directory, both hashes and explicit MIM head")
    require(not args.baseline_only or not any((args.after, args.tsv_sha256, args.provenance_sha256, args.mim_head)),
            "baseline-only cannot claim an after pair")
    raise SystemExit(run(args))


if __name__ == "__main__":
    main()
