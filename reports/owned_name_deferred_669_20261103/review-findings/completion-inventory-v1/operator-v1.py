"""Bounded deferred-23 export publication; dry-run unless explicitly applied.

This external operator preserves all source records and scientific decisions.
Native producer replay, receipt creation and guarded publication remain separate.
"""
from __future__ import annotations

import argparse
import base64
import csv
import hashlib
import importlib.util
import io
import json
import os
import re
import stat
import subprocess
import sys
import tempfile
from copy import deepcopy
from pathlib import Path

BASE = "0ee56c11a2894ed50a476b331d56297be0a3ee12"
PRODUCER = "3022b8738dcc9e01c7464a8d5c95aa9be2eef141"
SSSOM = "mappings/ingredient_mappings.sssom.tsv"
SIDECAR = "mappings/suppressed_aliases.tsv"
BASELINE = "mappings/other_cross_record_baseline.tsv"
MANIFEST = SSSOM + ".manifest.json"
ARTIFACTS = (SSSOM, SIDECAR, BASELINE)
PLAN = "reports/owned_name_deferred_669_20261103/publication-plan.json"
INVENTORY = "reports/owned_name_deferred_669_20261103/unchanged-inventory.json"
LOG = "reports/owned_name_deferred_669_20261103/application/publication.json"
BATCH = "issue669-deferred-owned-aliases"
RECEIPT = "reports/sssom_completion_20260921/mapping_changes/" + BATCH + ".json"
MAKER = "reports/sssom_completion_20260921/mapping_changes/make_receipt.py"
ISSUE = "https://github.com/CultureBotAI/MediaIngredientMech/issues/669"
SCOPE = "Export-only suppression of the 23 reviewed owned-name alias pairs; no scientific approval"
APPROVAL = "NONE: every touched row is withheld pending mapping-specific review; no prior approval carries across this link."
FIELDS = (
    "subject_id", "subject_label", "predicate_id", "object_id", "object_label",
    "object_source", "mapping_justification", "source", "mapping_date", "confidence",
    "comment", "other", "validation_method",
)
SIDE_FIELDS = (
    "subject_id", "token_key", "token", "owner_subject_ids", "disposition",
    "input_surfaces", "source_refs", "evidence_refs",
)
PAIR_FIELDS = {
    "baseline_row", "token_key", "source_position", "selector", "before_row",
    "after_other", "source_owner", "credited_owners", "source_ref", "input_surfaces",
    "disposition", "review_disposition",
}
_CODE = Path(__file__).read_bytes()


def require(condition, message):
    if not condition:
        raise ValueError("Deferred owned-name publication: " + message)


def digest(data):
    return hashlib.sha256(data).hexdigest()


def encoded(value):
    return (json.dumps(value, indent=2, sort_keys=True, ensure_ascii=False) + "\n").encode()


def read_json(raw):
    def pairs(items):
        result = {}
        for key, value in items:
            require(key not in result, "duplicate JSON key: " + key)
            result[key] = value
        return result
    return json.loads(raw, object_pairs_hook=pairs)


def checked(path):
    path = Path(path).absolute()
    require(path == path.resolve(), "aliased path: " + str(path))
    require(all(not p.is_symlink() for p in (path, *path.parents)), "symlink path: " + str(path))
    return path


def regular(path):
    path = checked(path)
    info = path.lstat()
    require(stat.S_ISREG(info.st_mode) and info.st_nlink == 1, "not a single regular file: " + str(path))
    return path.read_bytes()


def member(root, name, *, exists=True):
    require(isinstance(name, str) and name and "\\" not in name and not name.startswith("/"),
            "unsafe relative member")
    require(all(p not in {"", ".", ".."} for p in name.split("/")), "noncanonical member")
    path = checked(root / name)
    require(path.is_relative_to(root), "member escapes root")
    if exists:
        regular(path)
    return path


def git(root, *args):
    return subprocess.check_output(["git", "-C", str(root), *args])


def bind(inputs, items):
    for path, raw in items.items():
        path = checked(path)
        require(path not in inputs or inputs[path] == raw, "conflicting captured bytes: " + str(path))
        inputs[path] = raw


def table(raw, *, comments=False):
    require(isinstance(raw, bytes), "TSV input must be bytes")
    lines = raw.decode().splitlines(keepends=True)
    body = [line for line in lines if not (comments and line.startswith("#"))]
    reader = csv.DictReader(body, delimiter="\t")
    rows = list(reader)
    require(reader.fieldnames and len(reader.fieldnames) == len(set(reader.fieldnames)), "missing/duplicate TSV columns")
    require(all(None not in row and None not in row.values() for row in rows), "ragged TSV rows")
    return reader.fieldnames, rows


def source_reference(pair, before_sha):
    row = pair["before_row"]
    return (f"{SSSOM}#source_position={pair['source_position']}&subject_id={row['subject_id']}"
            f"&predicate_id={row['predicate_id']}&object_id={row['object_id']}&field=other@sha256={before_sha}")


_RENDER = r'''
import importlib.util,json,sys
from pathlib import Path
p=Path(sys.argv[1]);spec=importlib.util.spec_from_file_location('deferred_native_policy',p)
m=importlib.util.module_from_spec(spec);sys.modules[spec.name]=m
exec(compile(p.read_bytes(),str(p),'exec'),m.__dict__)
items=json.load(sys.stdin)
events=[m.Suppression(x['subject_id'],x['token'],frozenset(x['owners']),x['surface'],tuple(x['sources']),tuple(x['evidence'])) for x in items]
sys.stdout.buffer.write(m.render_suppressed_aliases(events))
'''


def render_events(events, producer):
    producer = checked(producer)
    path = producer / "src/kg_microbe_utils/owned_name_policy.py"
    require(git(producer, "rev-parse", "HEAD").decode().strip() == PRODUCER, "wrong producer revision")
    require(regular(path) == git(producer, "show", PRODUCER + ":src/kg_microbe_utils/owned_name_policy.py"),
            "native sidecar renderer differs from pinned source")
    before = regular(path)
    process = subprocess.run([sys.executable, "-I", "-c", _RENDER, str(path)],
                             input=encoded(events), capture_output=True, check=False)
    require(process.returncode == 0, "native sidecar rendering failed: " + process.stderr.decode()[-3000:])
    require(regular(path) == before and git(producer, "rev-parse", "HEAD").decode().strip() == PRODUCER,
            "native renderer changed while executing")
    return process.stdout


def build_projection(before, oldside, baseline, pairs, policy_evidence, producer):
    """Return exactly three projected byte artifacts, without writing any file."""
    require(isinstance(pairs, list) and len(pairs) == 23, "expected the complete 23-pair scope")
    require(isinstance(policy_evidence, str) and re.fullmatch(
        r"https://github\.com/CultureBotAI/MediaIngredientMech/issues/669#issuecomment-[0-9]+",
        policy_evidence), "policy evidence must be the actual issue669 comment")
    fields, rows = table(before, comments=True)
    require(tuple(fields) == FIELDS, "canonical columns differ")
    basefields, obligations = table(baseline)
    require(basefields == ["subject_id", "token", "owned_by", "disposition"], "baseline columns differ")
    require([p.get("baseline_row") for p in pairs] == obligations and len(obligations) == 23,
            "pairs differ from the complete baseline in order or payload")
    sidefields, oldrows = table(oldside)
    require(tuple(sidefields) == SIDE_FIELDS, "sidecar columns differ")
    oldkeys = set()
    events = []
    for row in oldrows:
        key = (row["subject_id"], row["token_key"])
        require(key not in oldkeys and row["token_key"] == row["token"].strip().casefold()
                and row["disposition"] == "SUPPRESS", "old sidecar pair differs")
        oldkeys.add(key)
        groups = {field: read_json(row[field]) for field in SIDE_FIELDS[3:] if field != "disposition"}
        require(all(isinstance(v, list) and v and all(isinstance(x, str) and x for x in v)
                    for v in groups.values()), "old sidecar lists differ")
        for surface in groups["input_surfaces"]:
            events.append({"subject_id": row["subject_id"], "token": row["token"],
                           "owners": groups["owner_subject_ids"], "surface": surface,
                           "sources": groups["source_refs"], "evidence": groups["evidence_refs"]})
    require(render_events(events, producer) == oldside, "old sidecar is not exactly native-rendered")
    selected = {}
    pairkeys = set()
    for pair in pairs:
        require(set(pair) == PAIR_FIELDS, "pair keys differ from closed contract")
        position = pair["source_position"]
        require(type(position) is int and 1 <= position <= len(rows), "invalid source position")
        subject, token = pair["baseline_row"]["subject_id"], pair["baseline_row"]["token"]
        key = token.strip().casefold()
        require((subject, key) not in pairkeys and position not in selected and (subject, key) not in oldkeys,
                "duplicate selected pair/position or already-suppressed pair")
        pairkeys.add((subject, key))
        row = rows[position - 1]
        require(pair["token_key"] == key and pair["before_row"] == row and row["subject_id"] == subject,
                "stale subject/token/row payload")
        require(pair["selector"] == {**{k: row[k] for k in ("subject_id", "predicate_id", "object_id")}, "field": "other"},
                "stale row selector")
        require(pair["input_surfaces"] == ["prior_sssom"] and pair["disposition"] == "SUPPRESS"
                and pair["review_disposition"] == "WITHHOLD", "extra origin, disposition or approval")
        require(pair["source_ref"] == source_reference(pair, digest(before)), "prior-canonical attribution differs")
        credited = [owner["subject_id"] for owner in pair["credited_owners"]]
        require(credited and credited == sorted(set(credited)) and subject not in credited,
                "invalid complete credited-owner list")
        parts = row["other"].split("|")
        hits = [i for i, value in enumerate(parts) if value.strip().casefold() == key]
        require(len(hits) == 1 and parts[hits[0]] == token, "planned token is not one exact raw element")
        after_other = "|".join(value for i, value in enumerate(parts) if i != hits[0])
        require(after_other == pair["after_other"], "projection changes another raw token")
        require(not any(i != position and other["subject_id"] == subject and
                        any(t.strip().casefold() == key for t in other["other"].split("|"))
                        for i, other in enumerate(rows, 1)), "selected token occurs on another row")
        selected[position] = after_other
        events.append({"subject_id": subject, "token": token, "owners": credited,
                       "surface": "prior_sssom", "sources": [pair["source_ref"]],
                       "evidence": [policy_evidence]})
    result_lines = []
    position = -1
    for line in before.splitlines(keepends=True):
        if line.startswith(b"#"):
            result_lines.append(line)
            continue
        position += 1
        if position not in selected:
            result_lines.append(line)
            continue
        cells = line.rstrip(b"\r\n").split(b"\t")
        require(len(cells) == len(fields), "selected raw row has unexpected quoting")
        cells[fields.index("other")] = selected[position].encode()
        result_lines.append(b"\t".join(cells) + line[len(line.rstrip(b"\r\n")):])
    after = b"".join(result_lines)
    _, afterrows = table(after, comments=True)
    expected = deepcopy(rows)
    for position, other in selected.items():
        expected[position - 1]["other"] = other
    require(afterrows == expected and len(selected) == 23, "projection changes unselected cells")
    side = render_events(events, producer)
    _, siderows = table(side)
    bykey = {(r["subject_id"], r["token_key"]): r for r in siderows}
    require(len(bykey) == len(oldrows) + 23 and len(bykey) == len(siderows), "sidecar membership differs")
    require(all(bykey[(r["subject_id"], r["token_key"])] == r for r in oldrows), "old sidecar payload changed")
    require(side.splitlines(keepends=True)[0] == oldside.splitlines(keepends=True)[0], "sidecar header changed")
    return {SSSOM: after, SIDECAR: side, BASELINE: baseline.splitlines(keepends=True)[0]}


def files(directory):
    """Ignored-inclusive regular-file inventory; aliases anywhere are rejected."""
    directory = checked(directory)
    require(directory.is_dir(), "missing evidence directory")
    result = set()
    for parent, dirs, names in os.walk(directory, followlinks=False):
        for name in (*dirs, *names):
            checked(Path(parent) / name)
        for name in names:
            path = Path(parent) / name
            regular(path)
            result.add(path)
    return result


def modules(root):
    """Load the repository's native validators and writer, not the old owner mutator."""
    sys.path[:0] = [str(root), str(root / "src")]
    from scripts import promote_owned_name_policy as native
    from scripts import step7a_guarded_publication as publication
    from mediaingredientmech import owned_name_suppression_refresh as context
    from mediaingredientmech.validation import mapping_change_receipts as chain
    require(Path(native.__file__).resolve() == root / "scripts/promote_owned_name_policy.py"
            and Path(publication.__file__).resolve() == root / "scripts/step7a_guarded_publication.py"
            and Path(context.__file__).resolve() == root / "src/mediaingredientmech/owned_name_suppression_refresh.py",
            "native modules came from another checkout")
    return native, publication, context, chain


def inventory_inputs(root, plan, tree, context, inputs):
    raw = regular(member(root, INVENTORY))
    require(plan["unchanged_inventory"] == {"path": INVENTORY, "sha256": digest(raw)}, "inventory reference differs")
    inventory = read_json(raw)
    context._shape(inventory, "inventory")
    require(inventory["baseline"] == BASE, "inventory baseline differs")
    bind(inputs, {root / INVENTORY: raw})
    paths = context.source_inventory(root)
    source = {}
    for folder, field in (("data/ingredients", "ingredient_sha256"), ("data/curated", "aggregate_sha256")):
        expected = sorted(name for name in tree if name.startswith(folder + "/") and Path(name).suffix in {".yaml", ".yml"})
        require(paths[folder] == expected == sorted(inventory[field]), "complete source inventory differs")
        for name, expected_sha in inventory[field].items():
            data = regular(member(root, name))
            context._historical_equal(tree, name, data)
            require(digest(data) == expected_sha, "unchanged source hash differs: " + name)
            source[name] = data
            bind(inputs, {root / name: data})
    require(set(inventory["protected_sha256"]) == set(context.PROTECTED), "protected membership differs")
    for name, expected_sha in inventory["protected_sha256"].items():
        data = regular(member(root, name))
        context._historical_equal(tree, name, data)
        require(digest(data) == expected_sha, "protected bytes differ: " + name)
        source[name] = data
        bind(inputs, {root / name: data})
    return source, paths


def generation_inputs(root, bundle, producer, plan, before, inputs, native):
    """Bind the complete original/archive pair, actual inputs, then replay offline."""
    archive = root / Path(plan["generation"]["candidate"]["path"]).parent
    original_files, archive_files = files(bundle), files(archive)
    require({str(p.relative_to(bundle)) for p in original_files}
            == {str(p.relative_to(archive)) for p in archive_files}, "generation archive membership differs")
    for path in sorted(original_files):
        archived = archive / path.relative_to(bundle)
        data = regular(path)
        require(data == regular(archived), "generation archive differs from original")
        bind(inputs, {path: data, archived: data})
    for key, name in (("candidate", "candidate.sssom.tsv"), ("sidecar", "suppressed_aliases.tsv"),
                      ("manifest", "candidate.sssom.tsv.manifest.json"), ("receipt", "generation-receipt.json")):
        require(plan["generation"][key] == {"path": str((archive / name).relative_to(root)),
                                           "sha256": digest(inputs[bundle / name])}, "generation reference differs")
    manifest = read_json(inputs[bundle / "candidate.sssom.tsv.manifest.json"])
    receipt = read_json(inputs[bundle / "generation-receipt.json"])
    prior_inventory, after_inventory = (read_json(inputs[bundle / n]) for n in ("inputs-before.json", "inputs-after.json"))
    repositories = read_json(inputs[bundle / "repository-context.json"])
    require(prior_inventory == after_inventory and receipt["input_bytes_unchanged"] is True,
            "native generation input bytes changed")
    require(receipt["scientific_approval_added"] is False and receipt["supervisor_binding"] is None,
            "generation invented scientific approval or supervisor binding")
    require(manifest["schema_version"] == 1 and manifest["policy_version"] == "owned-name-policy-v1"
            and manifest["external_sssom_validation"] == "passed", "native generation contract differs")
    require(plan["generation"]["producer_revision"] == manifest["source_revisions"]["claw"]
            == receipt["producer_revision"] == PRODUCER, "generation producer pin differs")
    require(git(producer, "rev-parse", "HEAD").decode().strip() == PRODUCER
            and not git(producer, "status", "--porcelain", "--untracked-files=all"), "producer checkout changed")
    for key, path, revision in (("mim", root, BASE), ("claw", producer, PRODUCER)):
        require(repositories[key]["path"] == str(path) and repositories[key]["revision"] == revision
                == manifest["source_revisions"][key] and not repositories[key]["status"],
                "generation repository checkpoint differs: " + key)
    for name, field in (("candidate.sssom.tsv", "candidate_sha256"), ("suppressed_aliases.tsv", "sidecar_sha256"),
                        ("candidate.sssom.tsv.manifest.json", "native_generation_manifest_sha256"),
                        ("inputs-before.json", "input_manifest_sha256")):
        require(digest(inputs[bundle / name]) == receipt[field], "native generation receipt differs: " + name)
    require(receipt["candidate"] == str(bundle / "candidate.sssom.tsv"), "original candidate path differs")
    require(manifest["artifacts"] == [
        {"path": str(bundle / "candidate.sssom.tsv"), "role": "sssom", "sha256": receipt["candidate_sha256"]},
        {"path": str(bundle / "suppressed_aliases.tsv"), "role": "suppressed_aliases", "sha256": receipt["sidecar_sha256"]}],
        "native paired artifacts differ")
    producer_files = native.producer_paths(producer)
    declared_code = {checked(p): h for p, h in manifest["producer_import_snapshot"].items()}
    require(set(declared_code) == producer_files, "complete producer dependency inventory differs")
    blobs = native.git_blobs(producer, PRODUCER, "src") | native.git_blobs(producer, PRODUCER, "scripts") | native.git_blobs(producer, PRODUCER, "plugins")
    for path in producer_files:
        data = regular(path)
        require(path in blobs and native.matches_blob(data, blobs[path]) and digest(data) == declared_code[path],
                "producer source differs from reviewed commit: " + str(path))
        bind(inputs, {path: data})
    entry = producer / "scripts/build_mim_ingredient_sssom.py"
    require(receipt["executed_entry_source_sha256"] == receipt["producer_sha256"] == declared_code[entry],
            "executed entry source binding differs")
    label_paths = {bundle / name for name in receipt["label_maps"]}
    require(label_paths == set(bundle.glob("label-input-*.json")), "label map membership differs")
    labels = {}
    for path in sorted(label_paths):
        require(path.parent == bundle and digest(inputs[path]) == receipt["label_maps"][path.name], "label map pin differs")
        labels.update(read_json(inputs[path])["labels"])
    require(labels == manifest["canonical_label_resolution"], "captured native labels differ")
    mapped = {p for p in inputs if p.parent == root / "data/ingredients/mapped" and p.suffix in {".yaml", ".yml"}}
    require(list(map(str, sorted(mapped))) == manifest["mapped_record_paths"], "native mapped membership differs")
    declared = {checked(item["path"]): item["sha256"] for item in manifest["source_inputs"]}
    require(len(declared) == len(manifest["source_inputs"]), "duplicate native input path")
    kgroot = checked(repositories["kg_microbe"]["path"])
    kg = kgroot / "mappings/kgmicrobe_unified_entity_mappings.sssom.tsv.gz"
    residual = producer / "workspace/reports/kg_microbe_residual_p25_categorized.json"
    require(receipt["prior_stamps"] == str(root / SSSOM) and manifest["prior_stamp_sources"] == [str(root / SSSOM)]
            and receipt["prior_sha256"] == digest(before[SSSOM]), "native prior canonical attribution differs")
    require(set(declared) == mapped | producer_files | {kg, residual, root / SSSOM}, "native declared input membership differs")
    absent = set()
    for path, expected in declared.items():
        if expected is None:
            require(not os.path.lexists(path), "absent native input appeared")
            absent.add(path)
            continue
        data = before[SSSOM] if path == root / SSSOM else regular(path)
        require(digest(data) == expected, "native consumed input changed: " + str(path))
        if path != root / SSSOM:
            bind(inputs, {path: data})
        if path not in producer_files:
            require(prior_inventory.get(str(path)) == {"sha256": expected, "bytes": len(data)},
                    "native harness input attribution differs")
    require(manifest["source_revisions"]["kg_microbe"] == repositories["kg_microbe"]["revision"], "KG historical revision differs")
    # Original ontology database hashes remain historical capture evidence.
    # Replay uses the exact captured label responses, not mutable database queries.
    with tempfile.TemporaryDirectory(prefix="deferred23-native-replay-") as temporary:
        prior = Path(temporary).resolve() / "before.tsv"
        prior.write_bytes(before[SSSOM])
        replay = subprocess.run([sys.executable, "-I", "-c", native._REPLAY, str(producer), str(bundle), str(prior)],
                                capture_output=True, text=True, check=False)
    require(replay.returncode == 0, "native offline replay failed: " + replay.stderr[-4000:])
    proof = read_json(replay.stdout)
    require(proof["rows"] == manifest["emitted_rows"], "native replay row count differs")
    candidate_rows = table(inputs[bundle / "candidate.sssom.tsv"], comments=True)[1]
    diagnostic_rows = table(inputs[bundle / "suppressed_aliases.tsv"])[1]
    for pair in plan["pairs"]:
        subject, key = pair["before_row"]["subject_id"], pair["token_key"]
        require(not any(row["subject_id"] == subject and row["token_key"] == key for row in diagnostic_rows)
                and not any(row["subject_id"] == subject and any(t.strip().casefold() == key for t in row["other"].split("|"))
                            for row in candidate_rows), "selected token has fresh candidate origin")
    return {"original_files": original_files, "archive": archive, "archive_files": archive_files,
            "producer_files": producer_files, "label_paths": label_paths, "absent": absent, "replay": proof}


def native_receipt(root, plan, plan_ref, before, outputs, tree, inputs, context, chain):
    """Execute the actual maker in private staging and replay both complete chains."""
    names = sorted(name for name in tree if name.startswith(chain.RECEIPTS_DIR + "/") and name.endswith(".json"))
    for name in (*names, *chain.HISTORICAL_CONTEXT, MAKER):
        data = regular(member(root, name))
        context._historical_equal(tree, name, data)
        bind(inputs, {root / name: data})
    spec = importlib.util.spec_from_file_location("deferred23_native_maker", root / MAKER)
    maker = importlib.util.module_from_spec(spec)
    exec(compile(inputs[root / MAKER], str(root / MAKER), "exec"), maker.__dict__)
    records = [context.expected_record(pair, plan_ref) for pair in plan["pairs"]]
    from contextlib import redirect_stdout
    with tempfile.TemporaryDirectory(prefix="deferred23-native-receipt-") as directory:
        temp = Path(directory).resolve()
        for name in (*names, *chain.HISTORICAL_CONTEXT):
            path = temp / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(inputs[root / name])
        canonical = temp / SSSOM
        canonical.parent.mkdir(parents=True, exist_ok=True)
        canonical.write_bytes(before[SSSOM])
        prefix = chain.verify_mapping_chain(temp)
        old_paths = prefix["receipt_paths"]
        require(set(old_paths) == set(names) and prefix["reviewed_sha256"] == digest(before[SSSOM]), "native prefix endpoint differs")
        require(type(plan["receipt_sequence"]) is int and plan["receipt_sequence"] == len(old_paths) + 1,
                "next receipt sequence differs")
        for item in records:
            path = temp / item["source_record"]
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(inputs[root / item["source_record"]])
        before_path, apply_log = temp / "before.tsv", temp / "source.json"
        before_path.write_bytes(before[SSSOM])
        apply_log.write_bytes(encoded({"records": records, "approval": APPROVAL}))
        canonical.write_bytes(outputs[SSSOM])
        maker.ROOT, maker.SOURCE, maker.HERE = temp, canonical, temp / chain.RECEIPTS_DIR
        argv = sys.argv
        sys.argv = [str(root / MAKER), "--batch", BATCH, "--sequence", str(plan["receipt_sequence"]),
                    "--issue", ISSUE, "--scope", SCOPE, "--before-sssom", str(before_path), "--apply-log", str(apply_log)]
        maker_stdout = io.StringIO()
        try:
            with redirect_stdout(maker_stdout):
                maker.main()
        finally:
            sys.argv = argv
        raw = regular(temp / RECEIPT)
        receipt = read_json(raw)
        old_rows, new_rows = maker.rows_of(before[SSSOM]), maker.rows_of(outputs[SSSOM])
        require(receipt["issue"] == ISSUE and receipt["scope"] == SCOPE and receipt["approval"] == APPROVAL
                and receipt["batch"] == BATCH and receipt["records"] == records
                and receipt["before_sha256"] == digest(before[SSSOM]) and receipt["after_sha256"] == digest(outputs[SSSOM])
                and receipt["sequence"] == plan["receipt_sequence"] and receipt["changed_rows"] == 23
                and receipt["added_rows"] == receipt["removed_rows"] == 0
                and receipt["position_map"] == list(range(1, len(old_rows) + 1))
                and receipt["changes"] == maker.align(old_rows, new_rows)[0]
                and receipt["touched_subjects"] == sorted(p["before_row"]["subject_id"] for p in plan["pairs"]),
                "native maker exceeds bounded export-only transition")
        full = chain.verify_mapping_chain(temp)
        require(full["state"] == new_rows and full["receipt_paths"] == old_paths + [RECEIPT], "native full chain differs")
    return raw, prefix, {"prefix_receipts": len(old_paths), "full_receipts": len(old_paths) + 1,
                         "maker_stdout": maker_stdout.getvalue(), "before_sha256": digest(before[SSSOM]),
                         "after_sha256": digest(outputs[SSSOM]), "changed_rows": 23, "added_rows": 0, "removed_rows": 0}


def loaded_code(root, tree, inputs, context, native, publication):
    require(regular(Path(__file__)) == _CODE, "executed external operator changed")
    bind(inputs, {Path(__file__).resolve(): _CODE})
    for name, data in context._LOADED.items():
        require(regular(root / name) == data, "executed native verifier changed: " + name)
        bind(inputs, {root / name: data})
    for module in (native, publication):
        path = Path(module.__file__).resolve()
        require(regular(path) == module._CODE, "executed helper changed")
    for module in tuple(sys.modules.values()):
        name = getattr(module, "__file__", None)
        if not name or not str(name).endswith(".py"):
            continue
        path = Path(name).resolve()
        if path.is_relative_to(root / "scripts") or path.is_relative_to(root / "src"):
            data = regular(path)
            # The new context and refresh integration are separately reviewed code.
            # All other native source is unchanged from the durable baseline.
            relative = str(path.relative_to(root))
            if relative not in {"src/mediaingredientmech/owned_name_suppression_refresh.py",
                                "src/mediaingredientmech/ingredient_bundle_refresh.py"}:
                context._historical_equal(tree, relative, data)
            bind(inputs, {path: data})
        elif any(part in {"kg_microbe_write", "kg_microbe_utils"} for part in path.parts):
            bind(inputs, {path: regular(path)})


def prepare(root, bundle, producer, plan_sha256):
    """Read/reproduce every output; do not publish or reserve any real path."""
    root, bundle, producer = map(checked, (root, bundle, producer))
    require(re.fullmatch(r"[0-9a-f]{64}", plan_sha256), "invalid caller plan pin")
    native, publication, context, chain = modules(root)
    tree = context._tree(root, BASE)
    require(git(root, "merge-base", "--is-ancestor", BASE, "HEAD") == b"", "checkout does not descend from approved base")
    inputs = {}
    plan_raw = regular(member(root, PLAN))
    require(digest(plan_raw) == plan_sha256, "caller plan hash differs")
    plan = read_json(plan_raw)
    context._shape(plan, "plan")
    require(plan["baseline"] == BASE and plan["generation"]["producer_revision"] == PRODUCER, "plan base/producer differs")
    bind(inputs, {root / PLAN: plan_raw})
    before = {name: git(root, "show", BASE + ":" + name) for name in (*ARTIFACTS, MANIFEST)}
    require(plan["artifacts_before"] == {name: digest(before[name]) for name in ARTIFACTS}, "plan artifact preimages differ")
    source, source_paths = inventory_inputs(root, plan, tree, context, inputs)
    projected = build_projection(before[SSSOM], before[SIDECAR], before[BASELINE], plan["pairs"], plan["policy_evidence"], producer)
    require(plan["artifacts_after"] == {name: digest(projected[name]) for name in ARTIFACTS}, "plan artifact postimages differ")
    context._pairs(plan, before, projected, source)
    context._sidecar(plan, before, projected)
    # The prior native review provides explicit positions and WITHHOLD decisions.
    review_name = "reports/sssom_completion_20260921/review.json"
    review_raw = regular(member(root, review_name))
    context._historical_equal(tree, review_name, review_raw)
    bind(inputs, {root / review_name: review_raw})
    decisions = {row["source_position"]: row for row in read_json(review_raw)["decisions"]}
    require(all(decisions[p["source_position"]]["disposition"] == "WITHHOLD" for p in plan["pairs"]),
            "a selected row carries scientific approval")
    generation = generation_inputs(root, bundle, producer, plan, before, inputs, native)
    plan_ref = {"path": PLAN, "sha256": plan_sha256}
    receipt, prefix, receipt_proof = native_receipt(root, plan, plan_ref, before, projected, tree, inputs, context, chain)
    old_manifest = read_json(before[MANIFEST])
    require(set(old_manifest["artifacts"]) == set(ARTIFACTS), "old manifest artifact membership differs")
    require(all(old_manifest["artifacts"][name] == plan["artifacts_before"][name] for name in (SIDECAR, BASELINE)),
            "old policy sidecar/baseline endpoint differs")
    checkpoints = [r["sequence"] for r in prefix["receipts"] if r["after_sha256"] == old_manifest["artifacts"][SSSOM]]
    require(len(checkpoints) == 1, "old manifest canonical checkpoint not unique/reachable")
    checkpoint = checkpoints[0]
    update = {"schema_version": 1, "operation": "owned-name-suppression-update-v1", "issue": 669,
              "scope": SCOPE, "approval": APPROVAL, "baseline": BASE,
              "prior_manifest_sha256": digest(before[MANIFEST]), "plan": plan_ref,
              **{key: plan[key] for key in ("unchanged_inventory", "artifacts_before", "artifacts_after", "generation")},
              "historical_checkpoint": {"sequence": checkpoint, "sssom_sha256": old_manifest["artifacts"][SSSOM],
                                        "bridge_sequences": list(range(checkpoint + 1, plan["receipt_sequence"]))},
              "mapping_receipt": {"path": RECEIPT, "sha256": digest(receipt), "sequence": plan["receipt_sequence"]},
              "publication_log": LOG}
    context._shape(update, "update")
    manifest = deepcopy(old_manifest)
    require(isinstance(manifest.get("owned_name_suppression_updates", []), list), "old update history malformed")
    manifest.setdefault("owned_name_suppression_updates", []).append(update)
    manifest["artifacts"] = dict(plan["artifacts_after"])
    projected[MANIFEST] = encoded(manifest)
    projected[RECEIPT] = receipt
    loaded_code(root, tree, inputs, context, native, publication)
    require(set(projected) == {*ARTIFACTS, MANIFEST, RECEIPT}, "publication output scope differs")
    return {"root": root, "bundle": bundle, "producer": producer, "plan": plan, "before": before,
            "outputs": {Path(name): raw for name, raw in projected.items()}, "inputs": inputs,
            "source_paths": source_paths, "generation": generation, "prefix": prefix,
            "receipt_proof": receipt_proof, "update": update,
            "modules": (native, publication, context, chain)}


def backups(log, before):
    return {log.with_name(log.stem + ".before-" + Path(name).name): data for name, data in before.items()}


def verify_completed(prepared, log):
    """Verify all five outputs and the exact native four-change/one-create journal."""
    root, before, outputs, inputs = (prepared[k] for k in ("root", "before", "outputs", "inputs"))
    native, publication, context, chain = prepared["modules"]
    log = checked(log)
    require(log == root / LOG, "completion log path differs")
    saved = read_json(regular(log))
    require(saved.get("operation") == "deferred-owned-name-publication-v1" and saved.get("state") == "complete"
            and saved.get("applied") is True and saved.get("approval") == APPROVAL
            and saved.get("plan_sha256") == digest(inputs[root / PLAN]), "completed publication attribution differs")
    expected_inputs = {str(path): digest(data) for path, data in inputs.items()}
    expected_inputs.update({str(root / name): digest(data) for name, data in before.items()})
    require(saved.get("input_sha256") == expected_inputs, "completed publication input bindings differ")
    require(saved.get("output_sha256") == {str(name): digest(data) for name, data in outputs.items()},
            "completed publication output bindings differ")
    require(all(regular(root / name) == data for name, data in outputs.items()), "completed output differs")
    require(all(regular(path) == data for path, data in inputs.items()), "completed immutable input differs")
    for path, data in backups(log, before).items():
        require(regular(path) == data, "completed preimage backup differs")
    from kg_microbe_write.transaction import JOURNAL_VERSION
    directory = checked(publication._journal_path(log))
    journal = checked(saved["transaction"]["journal"])
    require(journal.parent == directory and files(directory) == {journal}, "native journal membership differs")
    expected = {"version": JOURNAL_VERSION, "root": str(root), "status": "complete",
                "changed": sorted(str(root / name) for name in before), "created": [str(root / RECEIPT)],
                "previous": {str(root / name): data.decode() for name, data in before.items()}}
    raw = regular(journal)
    require(raw == json.dumps(expected, indent=2, sort_keys=True).encode() and digest(raw) == saved["journal_sha256"],
            "native completed journal differs")
    full = chain.verify_mapping_chain(root)
    require(context.receipt_inventory(root) == set(prepared["prefix"]["receipt_paths"]) | {RECEIPT}
            and full["receipt_paths"] == prepared["prefix"]["receipt_paths"] + [RECEIPT]
            and full["reviewed_sha256"] == digest(outputs[Path(SSSOM)]), "completed native chain differs")
    return {"applied": False, "changed": False, "state": "verified-complete", "receipt_count": len(full["receipt_paths"]),
            "journal_sha256": digest(raw), "canonical_sha256": full["reviewed_sha256"]}


def publish_prepared(prepared, *, apply=False):
    root, before, outputs, inputs = (prepared[k] for k in ("root", "before", "outputs", "inputs"))
    native, publication, context, chain = prepared["modules"]
    generation = prepared["generation"]
    log = checked(root / LOG)
    require(log.parent.is_dir(), "application parent must exist before publication")
    expected_backups = backups(log, before)
    for path in (log, publication._journal_path(log), *expected_backups, root / RECEIPT):
        checked(path)
        require(not os.path.lexists(path), "publication output already occupied: " + str(path))
    for name, data in before.items():
        require(regular(root / name) == data, "real publication preimage differs: " + name)
    bound = dict(inputs)
    bind(bound, {root / name: data for name, data in before.items()})
    def recheck():
        require(context.source_inventory(root) == prepared["source_paths"], "source membership changed")
        require(context.receipt_inventory(root) == set(prepared["prefix"]["receipt_paths"]), "receipt inventory changed")
        require(native.producer_paths(prepared["producer"]) == generation["producer_files"], "producer membership changed")
        require(files(prepared["bundle"]) == generation["original_files"]
                and files(generation["archive"]) == generation["archive_files"], "generation membership changed")
        require(set(prepared["bundle"].glob("label-input-*.json")) == generation["label_paths"], "label membership changed")
        require(all(not os.path.lexists(path) for path in generation["absent"]), "absent generation input appeared")
        require(git(prepared["producer"], "rev-parse", "HEAD").decode().strip() == PRODUCER
                and not git(prepared["producer"], "status", "--porcelain", "--untracked-files=all"), "producer revision/context changed")
        require(not os.path.lexists(root / RECEIPT), "new receipt appeared before publication")
        for path in bound:
            regular(path)  # reject symbolic/hardlink aliases, including parent-directory aliases
        publication.guarded.recheck(bound)
    recheck()
    result = {"schema_version": 1, "operation": "deferred-owned-name-publication-v1", "scope": SCOPE,
              "approval": APPROVAL, "scientific_approval_added": False, "supervisor_binding": None,
              "base_revision": BASE, "producer_revision": PRODUCER, "plan": PLAN,
              "plan_sha256": digest(inputs[root / PLAN]), "bundle": str(prepared["bundle"]),
              "producer": str(prepared["producer"]), "native_replay": generation["replay"],
              "native_receipt": prepared["receipt_proof"], "historical_checkpoint": prepared["update"]["historical_checkpoint"],
              "input_sha256": {str(path): digest(data) for path, data in bound.items()},
              "output_sha256": {str(path): digest(data) for path, data in outputs.items()},
              "executed_code": {str(path): {"sha256": digest(data), "source_utf8": data.decode()}
                                for path, data in inputs.items() if path.suffix == ".py"},
              "preserved_source_files": len(prepared["source_paths"]["data/ingredients"]),
              "selected_pairs": 23, "changed_cells": 23, "changed_field": "other"}
    answer = publication.publish(root, outputs, bound, log, expected_backups, result,
                                 apply=apply, validate_scope=recheck)
    if apply:
        answer["completed_verification"] = verify_completed(prepared, log)
    return answer


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ("root", "bundle", "producer"):
        parser.add_argument("--" + name, type=Path, required=True)
    parser.add_argument("--plan-sha256", required=True)
    modes = parser.add_mutually_exclusive_group()
    modes.add_argument("--apply", action="store_true")
    modes.add_argument("--dry-run", action="store_true")
    modes.add_argument("--verify-completed", action="store_true")
    args = parser.parse_args(argv)
    root = checked(args.root)
    sys.path[:0] = [str(root), str(root / "src")]
    from plugins.lock_manager import LockManager
    from plugins.repository_settings import RepositorySettings
    target = RepositorySettings.from_environment().get_target("mediaingredientmech")
    require(target.path.resolve() == root, "configured repository differs from requested root")
    target.open()
    with LockManager().lock("mediaingredientmech", "deferred23 export-only policy publication"):
        prepared = prepare(root, args.bundle, args.producer, args.plan_sha256)
        result = (verify_completed(prepared, root / LOG) if args.verify_completed
                  else publish_prepared(prepared, apply=args.apply))
    print(json.dumps({key: value for key, value in result.items() if key not in {"input_sha256", "executed_code"}}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
