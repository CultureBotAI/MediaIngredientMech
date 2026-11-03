"""Bounded Step7d projection + native receipt25; dry-run unless --apply.

An externally reviewed, hash-pinned config freezes the actual native candidate
and complete output rows. This operator grants no mapping/release approval.
Canonical and receipt are one native guarded transaction. Policy artifacts stay
historical through receipt24. CLI owns the native lock; callers must do likewise.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import importlib.util
import io
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile

HERE = Path(__file__).resolve().parent
RUN = HERE.parent
ROOT = RUN / "step7d"
sys.path[:0] = [str(ROOT), str(ROOT / "src")]
from scripts import apply_owned_name_policy as policy
from scripts import promote_owned_name_policy as native
from scripts import promote_heptahydrate_ncit as guarded
from scripts import step7a_guarded_publication as publication
from scripts import bump_sssom_header as header_module
from scripts.bump_sssom_header import newest_row_date, rewrite
from mediaingredientmech.validation import mapping_change_receipts as chain

BASE = "467aa319a06ef992035f509f66fe251082b44ae1"
PRODUCER = "3022b8738dcc9e01c7464a8d5c95aa9be2eef141"
BEFORE_SHA = "62fd37c2ed8ace9b9295618d44e251d11fc35feb711053b66d322e5a7bce14f1"
SSSOM = Path(chain.SSSOM_SOURCE)
BATCH = "issue901-step7d-reviewed-owner-forms"
RECEIPT = Path(chain.RECEIPTS_DIR) / (BATCH + ".json")
MAKER = Path(chain.RECEIPTS_DIR) / "make_receipt.py"
ISSUE = "https://github.com/CultureBotAI/MediaIngredientMech/issues/901"
SCOPE = "Step7d supported owner subset: exact form identity, closest-parent broadMatch and evidenced chemistry/alias corrections; deferred23 alias obligations and native holds retained."
APPROVAL = "NONE: source and mapping changes only; receipt25 withdraws prior approval from touched rows."
FORM = tuple("reports/sssom_completion_20260921/mapping_review/form_reviews/901-" + n + "-v1.json"
             for n in ("melezitose", "sodium-perchlorate"))
PROTECTED = tuple(map(Path, (
    "mappings/ingredient_mappings.sssom.tsv.manifest.json", "mappings/suppressed_aliases.tsv",
    "mappings/other_cross_record_baseline.tsv", "mappings/culturemech_recipe_membership.tsv",
    "mappings/unified_mapping_rejections.tsv", "UNIFIED_INGREDIENT_MAPPING.tsv",
    "UNIFIED_INGREDIENT_MAPPING.provenance.json", ".github/workflows/qc-evidence.yaml",
)))
SOURCE_GROUPS = ("1117-carbonate", "1117-maltose", "901")
SOURCE_OPERATOR = HERE / "apply_reviewed_owners.py"
_spec = importlib.util.spec_from_file_location("step7d_reviewed_owner_operator", SOURCE_OPERATOR)
owner_operator = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(owner_operator)
_CODE = Path(__file__).read_bytes()
_EXECUTED = {Path(m.__file__).resolve(): Path(m.__file__).read_bytes()
             for m in (policy, native, guarded, publication, chain, header_module)}
_EXECUTED.update(owner_operator.LOADED)
_EXECUTED[Path(__file__).resolve()] = _CODE
digest = guarded.digest
regular = policy.regular


def require(ok, message):
    if not ok:
        raise ValueError("Step7d promotion: " + message)


def encoded(value):
    return (json.dumps(value, indent=2, ensure_ascii=False) + "\n").encode()


def checked(path):
    path = Path(path).absolute()
    require(path == path.resolve() and ".." not in path.parts, "aliased or traversing path")
    return path


def bind(inputs, additions):
    for path, raw in additions.items():
        path = checked(path)
        require(path not in inputs or inputs[path] == raw, "conflicting input bytes: " + str(path))
        inputs[path] = raw


def table(raw):
    lines = raw.decode().splitlines(keepends=True)
    start = next(i for i, line in enumerate(lines) if not line.startswith("#"))
    fields = next(csv.reader([lines[start]], delimiter="\t"))
    rows = list(csv.DictReader(lines[start:], delimiter="\t"))
    require(len(fields) == len(set(fields)) and len(rows) == len(lines[start + 1:])
            and all(None not in r and None not in r.values() for r in rows), "malformed SSSOM")
    return lines[:start + 1], fields, list(zip(rows, lines[start + 1:], strict=True))


def slot(row):
    prefix = row["object_id"].split(":", 1)[0]
    return (row["subject_id"], prefix if prefix in {"cas", "kgmicrobe.ingredient", "kgmicrobe.compound"} else "ontology")


def owner_names(plan):
    require(isinstance(plan.get("owners"), dict) and plan["owners"], "empty owner plan")
    names = tuple(sorted(plan["owners"]))
    for name in names:
        path = Path(name)
        require(path.parts[:3] == ("data", "ingredients", "mapped") and len(path.parts) == 4
                and path.suffix == ".yaml" and str(path) == name, "unsafe/nonmapped owner path")
    require({item["group"] for item in plan["owners"].values()} == set(SOURCE_GROUPS),
            "owner groups must be exactly1117-carbonate,1117-maltose,901")
    return names


def deferred_pairs(raw):
    reader = csv.DictReader(io.StringIO(raw.decode()), delimiter="\t")
    require(reader.fieldnames == ["subject_id", "token", "owned_by", "disposition"], "baseline columns differ")
    rows = list(reader)
    require(len(rows) == 23 and all(None not in row and None not in row.values() for row in rows),
            "deferred23 baseline differs")
    pairs = {(r["subject_id"], r["token"]) for r in rows}
    require(len(pairs) == 23, "duplicate deferred pair")
    return pairs


def tokens(value):
    return list(filter(None, value.split("|")))


def output_from_candidate(src, prior, deferred):
    """Deterministic, narrow provenance carry; no scientific-field synthesis."""
    out = dict(src)
    out["validation_method"] = ""
    if prior is None:
        return out
    out["source"] = "|".join(dict.fromkeys(tokens(prior["source"]) +
                                           [t for t in tokens(src["source"]) if t.startswith("MIM:")]))
    out["comment"] = " ".join(dict.fromkeys(filter(None, (prior["comment"], src["comment"]))))
    if all(prior[k] == src[k] for k in ("object_id", "predicate_id")):
        out["validation_method"] = prior["validation_method"]
    restored = [t for t in tokens(prior["other"])
                if (src["subject_id"], t) in deferred and t not in tokens(src["other"])]
    out["other"] = "|".join(tokens(src["other"]) + restored)
    return out


def projection(before, candidate, config, plan, deferred):
    """Every selected candidate row/output/position and removed slot is explicit."""
    subjects = {"MIM:" + Path(n).stem for n in owner_names(plan)}
    header, fields, old = table(before)
    _, candidate_fields, generated = table(candidate)
    require(fields == candidate_fields, "candidate fields differ")
    selected = [(i, r) for i, (r, _) in enumerate(generated, 1) if r["subject_id"] in subjects]
    old_selected = [(i, r) for i, (r, _) in enumerate(old, 1) if r["subject_id"] in subjects]
    require(selected and {r["subject_id"] for _, r in selected} == subjects
            and {r["subject_id"] for _, r in old_selected} == subjects, "selected subject membership differs")
    by_old = {slot(r): (i, r) for i, r in old_selected}
    by_candidate = {slot(r): (i, r) for i, r in selected}
    require(len(by_old) == len(old_selected) and len(by_candidate) == len(selected), "duplicate selected row slot")
    require(len(config["rows"]) == len(selected), "projection must declare every complete selected row")
    output, insertions, declared_positions = {}, {}, {}
    for item in config["rows"]:
        require(set(item) == {"candidate_position", "candidate", "output", "before_position",
                              "insert_after_position", "output_position", "basis"}
                and isinstance(item["basis"], str) and item["basis"].strip(), "invalid projection item")
        require(type(item["candidate_position"]) is int and item["candidate_position"] > 0, "invalid candidate position")
        src, out = item["candidate"], item["output"]
        require(set(src) == set(out) == set(fields), "projection row fields differ")
        require(all(isinstance(v, str) and not any(c in v for c in "\t\r\n") for v in out.values()),
                "invalid output cell")
        key = slot(src)
        require(key not in output and by_candidate.get(key) == (item["candidate_position"], src)
                and slot(out) == key, "candidate row mismatch or duplicate")
        prior_item = by_old.get(key)
        prior = prior_item[1] if prior_item else None
        require(out == output_from_candidate(src, prior, deferred),
                "output differs from native science/provenance/deferred-token contract")
        require(type(item["output_position"]) is int and item["output_position"] > 0, "invalid final position")
        declared_positions[key] = item["output_position"]
        if prior is None:
            require(item["before_position"] is None, "new slot cannot claim old position")
            position = item["insert_after_position"]
            require(type(position) is int and position == max(i for i, r in old_selected if r["subject_id"] == key[0]),
                    "new row must follow last existing row of its subject")
            insertions.setdefault(position, []).append(out)
        else:
            require(type(item["before_position"]) is int and item["before_position"] == prior_item[0]
                    and item["insert_after_position"] is None,
                    "existing row cannot move or be reinserted")
        output[key] = out
    require(set(output) == set(by_candidate), "selected candidate slot omitted")
    removed = set(by_old) - set(output)
    declared_removed = set()
    for item in config["removed"]:
        require(set(item) == {"before_position", "before", "basis"} and isinstance(item["basis"], str)
                and item["basis"].strip(), "invalid removed-row declaration")
        require(type(item["before_position"]) is int and item["before_position"] > 0, "invalid removed position")
        key = slot(item["before"])
        require(key in removed and key not in declared_removed
                and by_old[key] == (item["before_position"], item["before"]), "wrong/duplicate removed slot")
        require(key[1] in {"cas", "kgmicrobe.compound", "kgmicrobe.ingredient"},
                "only obsolete registry slots may be removed")
        replacement = [r for _, r in selected if r["subject_id"] == key[0]]
        require(len(replacement) == 1 and slot(replacement[0])[1] == "ontology"
                and replacement[0]["predicate_id"] == "skos:exactMatch", "slot removal requires exact ontology route")
        require(not any((key[0], t) in deferred for t in tokens(item["before"]["other"])),
                "removal would discard a staged deferred-token occurrence")
        declared_removed.add(key)
    require(declared_removed == removed, "undeclared selected slot removal")
    render = lambda row: "\t".join(row[k] for k in fields) + "\n"
    body = []
    for position, (row, raw) in enumerate(old, 1):
        if row["subject_id"] not in subjects:
            body.append(raw)
        elif slot(row) in output:
            body.append(render(output[slot(row)]))
        body.extend(render(r) for r in insertions.get(position, []))
    lines = ("".join(header) + "".join(body)).splitlines(keepends=True)
    date = newest_row_date(lines)
    require(date is not None, "missing projected mapping date")
    result = "".join(rewrite(lines, date)[0]).encode()
    _, _, projected = table(result)
    require(len(projected) == len(old) + len(set(output) - set(by_old)) - len(removed), "row count differs")
    actual_positions = {slot(row): i for i, (row, _) in enumerate(projected, 1) if row["subject_id"] in subjects}
    require(actual_positions == declared_positions, "explicit final positions differ")
    require([raw for row, raw in projected if row["subject_id"] not in subjects]
            == [raw for row, raw in old if row["subject_id"] not in subjects], "unrelated row bytes/order changed")
    before_occurrences = {(slot(row), token) for row, _ in old for token in tokens(row["other"])
                          if (row["subject_id"], token) in deferred}
    after_occurrences = {(slot(row), token) for row, _ in projected for token in tokens(row["other"])
                         if (row["subject_id"], token) in deferred}
    require(before_occurrences == after_occurrences, "deferred23 baseline occurrences changed")
    require(digest(result) == config["canonical_after_sha256"], "reviewed projection output hash differs")
    return result


def baseline(root):
    """Capture regular base blobs once; owner absence and prefix are durable pins."""
    entries = native.git(root, "ls-tree", "-r", "-z", BASE)
    tree = {}
    native_code = {str(path.relative_to(root)) for path in _EXECUTED if path.is_relative_to(root)}
    for entry in entries.split(b"\0"):
        if not entry:
            continue
        meta, name = entry.split(b"\t", 1)
        mode, kind, oid = meta.decode().split()
        name = name.decode()
        if (name.startswith("data/ingredients/") and name.endswith(".yaml")
                or name.startswith(chain.RECEIPTS_DIR + "/") and name.endswith(".json")
                or name in (*chain.HISTORICAL_CONTEXT, *FORM, str(SSSOM), str(MAKER), *map(str, PROTECTED))
                or name in native_code):
            require(mode in {"100644", "100755"} and kind == "blob", "nonregular base object")
            tree[name] = oid
    ids = sorted(set(tree.values()))
    raw = subprocess.check_output(["git", "cat-file", "--batch"], cwd=root,
                                  input="".join(x + "\n" for x in ids).encode())
    offset, blobs = 0, {}
    for oid in ids:
        end = raw.index(b"\n", offset)
        actual, kind, size = raw[offset:end].decode().split()
        require(actual == oid and kind == "blob", "base object framing differs")
        length = int(size)
        blobs[oid] = raw[end + 1:end + 1 + length]
        require(raw[end + 1 + length:end + 2 + length] == b"\n", "base object length differs")
        offset = end + 2 + length
    require(offset == len(raw), "base object suffix differs")
    result = {name: blobs[oid] for name, oid in tree.items()}
    require(digest(result[str(SSSOM)]) == BEFORE_SHA, "wrong base canonical")
    return result


def verify_identity_promotions(names, old_ids, new_ids):
    """No identity takeover/merge, including a displaced base owner."""
    for name in names:
        identity = new_ids[name]
        if identity != old_ids[name]:
            require(isinstance(identity, str) and identity, "invalid promoted identifier")
            require(not any(other != name and isinstance(value, str) and value.casefold() == identity.casefold()
                            for inventory in (old_ids, new_ids) for other, value in inventory.items()),
                    "new primary identity collides with another owner: " + identity)


def source_inputs(root, plan_path, plan_sha256, source_logs, base):
    """Replay actual1117-carbonate,1117-maltose then901 source phases and verify native recovery evidence."""
    plan_path = checked(plan_path)
    plan_raw = regular(plan_path)
    require(digest(plan_raw) == plan_sha256, "owner plan hash differs")
    plan = json.loads(plan_raw)
    names = owner_names(plan)
    require(plan["base_revision"] == BASE and plan["scientific_approval_added"] is False,
            "owner plan base/approval differs")
    require(owner_operator.ROOT == root and owner_operator.BASE == BASE, "source operator binding differs")
    require(native.git(root, "merge-base", BASE, "HEAD").decode().strip() == BASE,
            "current branch not based on pinned main")
    owner_paths = policy.ingredient_paths(root)
    old_paths = {root / name for name in base if name.startswith("data/ingredients/")}
    require(owner_paths == old_paths and set(plan["all_owner_sha256"]) == {str(p.relative_to(root)) for p in owner_paths},
            "owner inventory differs from base/plan")
    require(set(names) <= set(plan["all_owner_sha256"]), "selected owner absent from inventory")
    current = {p: regular(p) for p in owner_paths}
    initial = {root / name: raw for name, raw in base.items() if name.startswith("data/ingredients/")}
    for path, raw in initial.items():
        name = str(path.relative_to(root))
        require(digest(raw) == plan["all_owner_sha256"][name], "plan inventory differs from base")
        expected = plan["owners"][name]["after_sha256"] if name in names else digest(raw)
        require(digest(current[path]) == expected, "current owner differs from reviewed endpoint: " + name)
    auxiliary = plan.get("auxiliary", {})
    require(set(auxiliary) <= owner_operator.AUXILIARY_PATHS,
            "unreviewed auxiliary destination")
    require(not (set(auxiliary) & (set(plan["protected_sha256"]) | set(plan["evidence_sha256"]))),
            "phase-varying auxiliary must not also be a constant input")
    for name, stages in auxiliary.items():
        require(isinstance(stages, list) and stages
                and len({stage["group"] for stage in stages}) == len(stages), "invalid auxiliary stages")
        require([stage["group"] for stage in stages] == sorted(
                    (stage["group"] for stage in stages), key=SOURCE_GROUPS.index), "auxiliary phase order differs")
        require(all(a["after_sha256"] == b["before_sha256"] for a, b in zip(stages, stages[1:])),
                "auxiliary phase chain differs")
        require(digest(base[name]) == stages[0]["before_sha256"], "auxiliary base hash differs")
        current[root / name] = regular(root / name)
        initial[root / name] = base[name]
        require(digest(current[root / name]) == stages[-1]["after_sha256"], "auxiliary final hash differs")
        for stage in stages:
            for migration in stage["migrations"]:
                owner = migration["owner_path"]
                require(owner in plan["owners"] and plan["owners"][owner]["group"] == stage["group"]
                        and plan["owners"][owner]["before_identifier"] == migration["before_identifier"]
                        and owner_operator.yaml.safe_load(current[root / owner])["identifier"] == migration["after_identifier"],
                        "auxiliary migration not bound to this exact selected owner")
    # A newly selected identity cannot silently take another current/base owner's id.
    old_ids = {str(path.relative_to(root)): owner_operator.yaml.safe_load(raw).get("identifier")
               for path, raw in initial.items() if path in owner_paths}
    new_ids = {str(path.relative_to(root)): owner_operator.yaml.safe_load(raw).get("identifier")
               for path, raw in current.items() if path in owner_paths}
    verify_identity_promotions(names, old_ids, new_ids)
    common = {plan_path: plan_raw}
    for path, raw in owner_operator.LOADED.items():
        require(regular(path) == raw, "source operator/helper changed")
        bind(common, {path: raw})
    for section in ("evidence_sha256", "protected_sha256"):
        for name, expected in plan[section].items():
            path = checked(root / name)
            require(path.is_relative_to(root), "unsafe plan evidence/protected path")
            raw = regular(path)
            require(digest(raw) == expected, "planned evidence/protected input differs: " + name)
            bind(common, {path: raw})
    inputs = dict(current)
    bind(inputs, common)
    records, phase_state = [], dict(initial)
    require(len(source_logs) == len(SOURCE_GROUPS) and len(set(map(checked, source_logs))) == len(SOURCE_GROUPS),
            "source logs must be distinct and follow the three declared groups")
    for group, log in zip(SOURCE_GROUPS, map(checked, source_logs), strict=True):
        selected = {name: plan["owners"][name] for name in names if plan["owners"][name]["group"] == group}
        phase_inputs = dict(phase_state)
        bind(phase_inputs, common)
        phase_records, outputs, previous = [], {}, {}
        for name, item in sorted(selected.items()):
            old = phase_state[root / name]
            require(digest(old) == item["before_sha256"] == digest(base[name]), "source preimage differs")
            new = owner_operator.propose(old, item, plan["timestamp"])
            require(new == current[root / name], "source operator replay differs from final owner")
            outputs[Path(name)] = new
            previous[Path(name)] = old
            phase_records.append({"source_record": name, "shape": item["shape"],
                                  "before_yaml_sha256": digest(old), "after_yaml_sha256": digest(new),
                                  "change": item["event_changes"], "verification": item["verification"]})
            backup = log.with_name(log.stem + ".before-" + Path(name).name)
            require(regular(backup) == old, "source backup differs from base")
            bind(inputs, {backup: old})
        auxiliary_receipt = {}
        for name, stages in auxiliary.items():
            for item in stages:
                if item["group"] != group:
                    continue
                old = phase_state[root / name]
                new = owner_operator.propose_auxiliary(name, old, item)
                outputs[Path(name)] = new
                previous[Path(name)] = old
                auxiliary_receipt[name] = item
                backup = log.with_name(log.stem + ".before-" + Path(name).name)
                require(regular(backup) == old, "auxiliary phase backup differs")
                bind(inputs, {backup: old})
        expected = {"phase": "step7d-reviewed-owner-" + group, "base_revision": BASE,
                    "plan_sha256": plan_sha256,
                    "approval": "NONE: source correction; changed owner bytes withdraw inherited support.",
                    "scientific_approval_added": False, "supervisor_binding": None, "records": phase_records,
                    "auxiliary": auxiliary_receipt,
                    "input_sha256": {str(p): digest(b) for p, b in phase_inputs.items()},
                    "output_sha256": {str(p): digest(b) for p, b in outputs.items()}}
        raw = policy.completed_receipt(log, expected, root, changed=set(outputs))
        bind(inputs, {log: raw})
        bind(inputs, publication.completed_journal(root, log, json.loads(raw), previous=previous))
        records.extend(phase_records)
        phase_state.update({root / p: raw for p, raw in outputs.items()})
    require(phase_state == current and len(records) == len(names), "source phases do not close exact selected owner set")
    return inputs, records, owner_paths, plan


def generation_inputs(root, bundle, producer, inputs, manifest_sha256):
    """Verify native input/capture contracts and replay without network calls."""
    bundle, producer = checked(bundle), checked(producer)
    names = ("candidate.sssom.tsv", "suppressed_aliases.tsv", "candidate.sssom.tsv.manifest.json",
             "generation-receipt.json", "inputs-before.json", "inputs-after.json", "repository-context.json")
    bind(inputs, {bundle / n: regular(bundle / n) for n in names})
    manifest = json.loads(inputs[bundle / names[2]])
    receipt = json.loads(inputs[bundle / names[3]])
    before, after = (json.loads(inputs[bundle / n]) for n in names[4:6])
    context = json.loads(inputs[bundle / names[6]])
    require(digest(inputs[bundle / names[2]]) == manifest_sha256, "native manifest pin differs")
    require(before == after and receipt["input_bytes_unchanged"] is True, "generation inputs changed")
    require(receipt.get("scientific_approval_added") is False and receipt.get("supervisor_binding") is None,
            "generation cannot confer approval/binding")
    require(manifest.get("schema_version") == 1 and manifest.get("policy_version") == "owned-name-policy-v1"
            and manifest.get("external_sssom_validation") == "passed", "native generation contract differs")
    require(manifest["source_revisions"]["claw"] == receipt["producer_revision"] == PRODUCER
            and native.git(producer, "rev-parse", "HEAD").decode().strip() == PRODUCER
            and not native.git(producer, "status", "--porcelain", "--untracked-files=all"), "producer is not clean and pinned")
    for key, path in (("mim", root), ("claw", producer)):
        require(context[key]["path"] == str(path) and not context[key]["status"]
                and context[key]["revision"] == manifest["source_revisions"][key], "generation checkpoint differs")
    for name, field in zip(names[:3], ("candidate_sha256", "sidecar_sha256", "native_generation_manifest_sha256"), strict=True):
        require(digest(inputs[bundle / name]) == receipt[field], "generation artifact receipt differs")
    require(receipt["input_manifest_sha256"] == digest(inputs[bundle / names[4]]), "generation inventory receipt differs")
    require(manifest["artifacts"] == [{"path": str(bundle / names[0]), "role": "sssom", "sha256": receipt["candidate_sha256"]},
                                     {"path": str(bundle / names[1]), "role": "suppressed_aliases", "sha256": receipt["sidecar_sha256"]}],
            "native artifact pair differs")
    producers = native.producer_paths(producer)
    code = {Path(p): h for p, h in manifest["producer_import_snapshot"].items()}
    require(set(code) == producers, "producer dependency membership differs")
    blobs = {}
    for prefix in ("src", "scripts", "plugins"):
        blobs.update(native.git_blobs(producer, PRODUCER, prefix))
    for path in producers:
        raw = regular(path)
        require(path in blobs and native.matches_blob(raw, blobs[path]) and digest(raw) == code[path], "producer source changed")
        bind(inputs, {path: raw})
    entry = producer / "scripts/build_mim_ingredient_sssom.py"
    require(receipt["executed_entry_source_sha256"] == receipt["producer_sha256"] == code[entry], "executed entrypoint differs")
    label_paths = {bundle / name for name in receipt["label_maps"]}
    require(label_paths == set(bundle.glob("label-input-*.json")), "label capture inventory differs")
    labels = {}
    for path in sorted(label_paths):
        require(path.parent == bundle, "unsafe label capture path")
        raw = regular(path)
        require(digest(raw) == receipt["label_maps"][path.name], "captured labels changed")
        bind(inputs, {path: raw})
        labels.update(json.loads(raw)["labels"])
    require(labels == manifest["canonical_label_resolution"], "native labels differ from captures")
    mapped = {p for p in policy.ingredient_paths(root) if p.parent == root / "data/ingredients/mapped"}
    require(list(map(str, sorted(mapped))) == manifest["mapped_record_paths"], "mapped inventory differs")
    checkpoint = native.git_blobs(root, manifest["source_revisions"]["mim"], "data/ingredients/mapped")
    require(set(checkpoint) == mapped and all(native.matches_blob(inputs[p], checkpoint[p]) for p in mapped), "source checkpoint differs")
    declared = {Path(item["path"]): item["sha256"] for item in manifest["source_inputs"]}
    require(len(declared) == len(manifest["source_inputs"]), "duplicate generation input")
    kgroot = checked(context["kg_microbe"]["path"])
    kg = kgroot / "mappings/kgmicrobe_unified_entity_mappings.sssom.tsv.gz"
    residual = producer / "workspace/reports/kg_microbe_residual_p25_categorized.json"
    prior = checked(receipt["prior_stamps"])
    require(manifest["prior_stamp_sources"] == [str(prior)] and prior == root / SSSOM
            and receipt["prior_sha256"] == BEFORE_SHA, "prior stamp source differs")
    require(set(declared) == mapped | producers | {kg, residual, root / SSSOM}, "native input inventory differs")
    absent = set()
    for path, expected in declared.items():
        if expected is None:
            require(not os.path.lexists(path), "absent native input appeared")
            absent.add(path)
            continue
        raw = regular(path)
        require(digest(raw) == expected, "native input bytes changed")
        bind(inputs, {path: raw})
        if path not in producers:
            require(before[str(path)] == {"sha256": expected, "bytes": len(raw)}, "harness input binding differs")
    require(manifest["source_revisions"]["kg_microbe"] == context["kg_microbe"]["revision"], "KG revision receipt differs")
    replay = subprocess.run([sys.executable, "-I", "-c", native._REPLAY, str(producer), str(bundle), str(prior)],
                            capture_output=True, text=True, check=False)
    require(replay.returncode == 0, "native offline replay failed: " + replay.stderr[-4000:])
    replay_result = json.loads(replay.stdout)
    require(replay_result["rows"] == manifest["emitted_rows"], "native replay count differs")
    return absent, label_paths, producers, replay_result


def native_receipt(root, base, inputs, records, after, plan):
    """Execute the exact native maker only inside a private temporary tree."""
    old_paths = chain.receipt_paths(root)
    expected = {n for n in base if n.startswith(chain.RECEIPTS_DIR + "/") and n.endswith(".json")}
    require(len(old_paths) == 24 and set(old_paths) == expected, "native receipt prefix differs")
    for name in (*old_paths, *chain.HISTORICAL_CONTEXT, *FORM, str(MAKER)):
        raw = regular(root / name)
        require(raw == base[name], "historical receipt/context/FORM/maker differs")
        bind(inputs, {root / name: raw})
    spec = importlib.util.spec_from_file_location("step7d_native_maker", root / MAKER)
    maker = importlib.util.module_from_spec(spec)
    exec(compile(inputs[root / MAKER], str(root / MAKER), "exec"), maker.__dict__)
    with tempfile.TemporaryDirectory(prefix="mim-step7d-native-receipt-") as directory:
        temp = Path(directory).resolve()
        for name in (*old_paths, *chain.HISTORICAL_CONTEXT):
            path = temp / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(inputs[root / name])
        canonical = temp / SSSOM
        canonical.parent.mkdir(parents=True, exist_ok=True)
        canonical.write_bytes(base[str(SSSOM)])
        prefix = chain.verify_mapping_chain(temp)
        require(prefix["reviewed_sha256"] == BEFORE_SHA, "native prefix endpoint differs")
        before = temp / "before.tsv"
        before.write_bytes(base[str(SSSOM)])
        source = temp / "source.json"
        source.write_bytes(encoded({"records": records, "approval": APPROVAL}))
        for item in records:
            path = temp / item["source_record"]
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(inputs[root / item["source_record"]])
        canonical.write_bytes(after)
        maker.ROOT, maker.SOURCE, maker.HERE = temp, canonical, temp / chain.RECEIPTS_DIR
        argv = sys.argv
        sys.argv = [str(root / MAKER), "--batch", BATCH, "--sequence", "25", "--issue", ISSUE,
                    "--scope", SCOPE, "--before-sssom", str(before), "--apply-log", str(source)]
        try:
            maker.main()
        finally:
            sys.argv = argv
        raw = regular(temp / RECEIPT)
        receipt = json.loads(raw)
        require(receipt["records"] == records and receipt["before_sha256"] == BEFORE_SHA
                and receipt["after_sha256"] == digest(after) and receipt["sequence"] == 25
                and receipt["issue"] == ISSUE and receipt["batch"] == BATCH
                and receipt["approval"].startswith("NONE:")
                and receipt["changes"] == maker.align(maker.rows_of(base[str(SSSOM)]), maker.rows_of(after))[0]
                and set(receipt["touched_subjects"]) == {"MIM:" + Path(n).stem for n in owner_names(plan)}, "native receipt endpoints or scope differ")
        full = chain.verify_mapping_chain(temp)
        require(full["state"] == maker.rows_of(after) and full["receipt_paths"] == old_paths + [str(RECEIPT)],
                "native full-chain replay differs")
    return raw, old_paths


def promote(root, bundle, producer, plan_path, plan_sha256, source_logs, config_path, config_sha256, log, *, apply=False):
    root, bundle, producer, log, config_path = map(checked, (root, bundle, producer, log, config_path))
    require(root == ROOT.resolve(), "operator is bound to owned Step7d checkout")
    require(not os.path.lexists(root / RECEIPT), "receipt25 already exists")
    raw = regular(config_path)
    require(digest(raw) == config_sha256, "projection config pin differs")
    config = json.loads(raw)
    require(set(config) == {"schema_version", "base_revision", "producer_revision", "candidate_sha256",
            "generation_manifest_sha256", "canonical_after_sha256", "rows", "removed", "owner_plan_sha256",
            "source_operator_sha256", "scientific_approval_added", "supervisor_binding"}
            and config["schema_version"] == 2 and config["base_revision"] == BASE
            and config["producer_revision"] == PRODUCER and config["scientific_approval_added"] is False
            and config["supervisor_binding"] is None, "projection config contract differs")
    require(config["owner_plan_sha256"] == plan_sha256
            and config["source_operator_sha256"] == digest(regular(SOURCE_OPERATOR)), "source plan/operator pin differs")
    base = baseline(root)
    inputs, records, owner_paths, plan = source_inputs(root, plan_path, plan_sha256, source_logs, base)
    bind(inputs, {config_path: raw})
    for p in PROTECTED:
        raw = regular(root / p)
        if str(p) in plan.get("auxiliary", {}):
            require(digest(raw) == plan["auxiliary"][str(p)][-1]["after_sha256"],
                    "reviewed auxiliary final endpoint changed")
        else:
            require(raw == base[str(p)], "historical policy/unified/membership anchor changed")
        bind(inputs, {root / p: raw})
    absent, label_paths, producer_paths, replay = generation_inputs(
        root, bundle, producer, inputs, config["generation_manifest_sha256"])
    candidate = inputs[bundle / "candidate.sssom.tsv"]
    require(digest(candidate) == config["candidate_sha256"], "reviewed candidate pin differs")
    require(inputs[root / SSSOM] == base[str(SSSOM)], "canonical preimage differs")
    deferred = deferred_pairs(base["mappings/other_cross_record_baseline.tsv"])
    after = projection(base[str(SSSOM)], candidate, config, plan, deferred)
    receipt, old_paths = native_receipt(root, base, inputs, records, after, plan)
    code_paths = {Path(__file__), Path(native.__file__), Path(policy.__file__), Path(guarded.__file__),
                  Path(publication.__file__), Path(chain.__file__), root / MAKER,
                  root / "scripts/bump_sssom_header.py"}
    require(regular(Path(__file__)) == _CODE and regular(Path(native.__file__)) == native._CODE
            and regular(Path(publication.__file__)) == publication._CODE, "executed operator/helper changed")
    for path, loaded in _EXECUTED.items():
        require(regular(path) == loaded, "executed module bytes changed")
        if path.is_relative_to(root):
            require(loaded == base[str(path.relative_to(root))], "native module differs from approved base")
        bind(inputs, {path: loaded})
    for path in code_paths:
        bind(inputs, {path: regular(path)})
    code_paths.update(p for p in inputs if p.suffix == ".py" and p not in producer_paths)
    execution_code = {str(p): {"sha256": digest(inputs[p]), "source_utf8": inputs[p].decode()} for p in sorted(code_paths)}
    result = {"schema_version": 1, "phase": "canonical-and-receipt25", "approval": APPROVAL,
              "scientific_approval_added": False, "supervisor_binding": None,
              "source_logs": [str(checked(p)) for p in source_logs], "records": records,
              "auxiliary_reference_migrations": plan.get("auxiliary", {}),
              "base_revision": BASE, "producer_revision": PRODUCER,
              "projection_config": str(config_path), "projection_config_sha256": config_sha256,
              "generation_manifest_sha256": config["generation_manifest_sha256"],
              "sssom_before_sha256": BEFORE_SHA, "sssom_after_sha256": digest(after),
              "receipt_path": str(RECEIPT), "receipt_sha256": digest(receipt),
              "native_replay": replay,
              "historical_policy": "unchanged through receipt24; receipt25 binds this batch; deferred23 preserved",
              "input_sha256": {str(p): digest(b) for p, b in inputs.items()},
              "executed_code": execution_code}
    outputs = {SSSOM: after, RECEIPT: receipt}
    def recheck():
        require(policy.ingredient_paths(root) == owner_paths, "owner inventory changed")
        require(set(chain._names(root)) == set(old_paths), "receipt inventory changed")
        require(set(bundle.glob("label-input-*.json")) == label_paths and native.producer_paths(producer) == producer_paths,
                "producer/label inventory changed")
        require(all(not os.path.lexists(p) for p in absent), "absent generation input appeared")
        require(native.git(producer, "rev-parse", "HEAD").decode().strip() == PRODUCER
                and not native.git(producer, "status", "--porcelain", "--untracked-files=all"), "producer context changed")
        guarded.recheck(inputs)
    backups = {log.with_name(log.stem + ".before-canonical.tsv"): base[str(SSSOM)]}
    recheck()
    answer = publication.publish(root, outputs, inputs, log, backups, result, apply=apply, validate_scope=recheck)
    if apply:
        saved = json.loads(regular(log))
        require(saved.get("applied") is True and saved.get("state") == "complete", "promotion completion absent")
        require(all(regular(root / p) == b for p, b in outputs.items()), "published outputs differ")
        require(all(regular(p) == b for p, b in inputs.items() if p != root / SSSOM), "input changed after publication")
        from kg_microbe_write.transaction import JOURNAL_VERSION
        journal = checked(saved["transaction"]["journal"])
        directory = publication._journal_path(log)
        require(journal.parent == directory and sorted(directory.iterdir()) == [journal], "promotion journal membership differs")
        raw = regular(journal)
        require(digest(raw) == saved["journal_sha256"] and json.loads(raw) == {
            "version": JOURNAL_VERSION, "root": str(root), "status": "complete",
            "changed": [str(root / SSSOM)], "created": [str(root / RECEIPT)],
            "previous": {str(root / SSSOM): base[str(SSSOM)].decode()}}, "promotion journal differs")
        full = chain.verify_mapping_chain(root)
        require(full["reviewed_sha256"] == digest(after) and full["receipt_paths"] == old_paths + [str(RECEIPT)],
                "published native chain differs")
    return answer


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    for name in ("bundle", "producer", "plan", "config", "log"):
        parser.add_argument("--" + name, type=Path, required=True)
    parser.add_argument("--source-log", type=Path, action="append", required=True,
                        help="repeat in order:1117-carbonate,1117-maltose,901")
    parser.add_argument("--config-sha256", required=True)
    parser.add_argument("--plan-sha256", required=True)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--apply", action="store_true")
    mode.add_argument("--dry-run", action="store_true")
    args = parser.parse_args(argv)
    from plugins.lock_manager import LockManager
    from plugins.repository_settings import RepositorySettings
    root = checked(args.root)
    target = RepositorySettings.from_environment().get_target("mediaingredientmech")
    require(target.path.resolve() == root, "configured MIM root differs")
    target.open()
    with LockManager().lock("mediaingredientmech", "Step7d canonical plus native receipt25"):
        result = promote(root, args.bundle, args.producer, args.plan, args.plan_sha256,
                         args.source_log, args.config, args.config_sha256,
                         args.log, apply=args.apply)
    print(json.dumps({k: v for k, v in result.items() if k not in {"input_sha256", "executed_code"}}, indent=2))


if __name__ == "__main__":
    main()
