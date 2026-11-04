"""Execute an exact reviewed data plan through existing native MIM writers.

External, single-batch operator. Dry-run by default; it chooses no identities.
Source evidence, preimages, operations, history and output hashes are explicit.
The native validated serializer and reserved transactional publisher are reused.
"""
from __future__ import annotations

import argparse
import copy
import csv
import hashlib
import inspect
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile

HERE = Path(__file__).resolve().parent
RUN = HERE.parent
ROOT = RUN / "step7d"
BASE = "467aa319a06ef992035f509f66fe251082b44ae1"
sys.path[:0] = [str(ROOT), str(ROOT / "src")]

import yaml
from mediaingredientmech.curate.curation_event import record_curation_event
from mediaingredientmech.validation.write_validated import write_validated_ingredient
from scripts import apply_owned_name_policy as policy
from scripts import promote_heptahydrate_ncit as guarded
from scripts import step7a_guarded_publication as publication

LOADED = {Path(m.__file__).resolve(): Path(m.__file__).read_bytes()
          for m in (policy, guarded, publication)}
for function in (record_curation_event, write_validated_ingredient):
    module_path = Path(inspect.getsourcefile(function)).resolve()
    LOADED[module_path] = module_path.read_bytes()
LOADED[Path(__file__).resolve()] = Path(__file__).read_bytes()
PROTECTED_FIELDS = (
    "preferred_term", "mapping_status", "occurrence_statistics", "source_occurrences",
    "representative", "nutritional_roles", "physicochemical_roles", "cellular_roles",
    "community_roles", "environmental_roles", "causal_graphs", "components",
)
ALLOWED_ROOTS = {"identifier", "ontology_mapping", "chemical_properties", "supplied_form", "synonyms", "notes"}
AUXILIARY_PATHS = {"mappings/culturemech_recipe_membership.tsv", "mappings/unified_mapping_rejections.tsv"}
IDENTITY_MIGRATIONS = {
    "cas:6363-53-7": ("NCIT:C80300", "D-Maltose_Monohydrate", "1117-maltose", 20),
    "kgmicrobe.compound:cecl3_x_7_h2o": ("cas:18618-55-8", "Cecl3_X_7_H2o", "901", 4),
    "kgmicrobe.compound:cu_no32_x_3_h2o": ("cas:10031-43-3", "Cu_No32_X_3_H2o", "901", 2),
}


def require(ok, message):
    if not ok:
        raise ValueError(message)


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def regular(path):
    path = Path(path).absolute()
    require(path == path.resolve(), "Aliased path: " + str(path))
    return policy.regular(path)


def render(record):
    with tempfile.TemporaryDirectory(prefix="mim-step7d-owner-render-") as temp:
        path = Path(temp) / "record.yaml"
        write_validated_ingredient(record, path)
        return path.read_bytes()


def propose(raw, item, timestamp):
    require(sha(raw) == item["before_sha256"], "Owner preimage hash differs")
    old = yaml.safe_load(raw)
    require(old["identifier"] == item["before_identifier"], "Owner identity differs")
    record = copy.deepcopy(old)
    for operation in item["operations"]:
        path = operation["path"]
        require(isinstance(path, list) and path and path[0] in ALLOWED_ROOTS,
                "Operation outside reviewed data fields")
        cursor = record
        for key in path[:-1]:
            cursor = cursor[key]
        key = path[-1]
        exists = key in cursor if isinstance(cursor, dict) else isinstance(key, int) and 0 <= key < len(cursor)
        require(exists == operation["before_exists"], "Operation presence differs")
        if exists:
            require(cursor[key] == operation["before"], "Operation preimage differs")
        if operation["op"] == "set":
            cursor[key] = copy.deepcopy(operation["after"])
        elif operation["op"] == "remove":
            require(exists, "Cannot remove absent field")
            del cursor[key]
        else:
            raise ValueError("Unknown reviewed operation")
    require(record != old, "No-op owner must not get a history event")
    for field in PROTECTED_FIELDS:
        require(record.get(field) == old.get(field), "Protected owner field changed: " + field)
    require(record.get("curation_history") == old.get("curation_history"), "History rewritten")
    record_curation_event(record, curator="claude", action="CORRECTED",
                          changes=item["event_changes"], previous_status=old["mapping_status"],
                          new_status=old["mapping_status"], llm_assisted=True,
                          llm_model="gpt-6", timestamp=timestamp)
    result = render(record)
    require(sha(result) == item["after_sha256"], "Reviewed output hash differs")
    return result


def propose_auxiliary(name, raw, item):
    """Only the explicitly reviewed same-owner reference migrations."""
    require(name in AUXILIARY_PATHS and sha(raw) == item["before_sha256"], "Auxiliary preimage differs")
    migrations = {m["before_identifier"]: m for m in item["migrations"]}
    require(len(migrations) == len(item["migrations"]) and migrations, "Duplicate/empty auxiliary migration")
    for old, migration in migrations.items():
        require(old in IDENTITY_MIGRATIONS, "Unreviewed auxiliary identity")
        new, stem, group, count = IDENTITY_MIGRATIONS[old]
        require(migration["after_identifier"] == new and item["group"] == group
                and migration["owner_path"] == "data/ingredients/mapped/" + stem + ".yaml",
                "Auxiliary owner/group differs")
    destinations = {m["after_identifier"] for m in migrations.values()}
    lines = raw.splitlines(keepends=True)
    if name.endswith("culturemech_recipe_membership.tsv"):
        header = []
        while lines and lines[0].startswith(b"#"):
            header.append(lines.pop(0))
        require(lines and lines[0] == b"mim_identifier\trecipe_id\toccurrences\n", "Membership columns differ")
        header.append(lines.pop(0))
        rows, selected = [], {old: [] for old in migrations}
        for line in lines:
            fields = line.rstrip(b"\r\n").decode().split("\t")
            require(len(fields) == 3 and all(fields), "Malformed membership")
            identity, recipe, count = fields
            require(identity not in destinations, "Destination membership already exists")
            if identity in migrations:
                selected[identity].append({"recipe_id": recipe, "occurrences": int(count)})
                identity = migrations[identity]["after_identifier"]
                line = identity.encode() + b"\t" + line.split(b"\t", 1)[1]
            rows.append(((identity, recipe), line))
        require(all(selected[old] == migration["memberships"]
                    and len(selected[old]) == IDENTITY_MIGRATIONS[old][3]
                    for old, migration in migrations.items()), "Reviewed membership cohort differs")
        require(len({key for key, _ in rows}) == len(rows), "Duplicate membership key")
        after = b"".join(header) + b"".join(line for _, line in sorted(rows))
    else:
        fields = lines[0].decode().rstrip("\n").split("\t")
        require(fields == ["ingredient_name", "rejected_id", "mim_id", "reason"], "Ledger columns differ")
        matches, output = {old: 0 for old in migrations}, [lines[0]]
        for line in lines[1:]:
            values = next(csv.reader([line.decode()], delimiter="\t"))
            require(len(values) == 4, "Malformed ledger row")
            row = dict(zip(fields, values))
            if row["mim_id"] in migrations:
                old = row["mim_id"]
                migration = migrations[old]
                require(row == migration["before_row"], "Wrong ledger owner/source pair")
                changed = dict(row, mim_id=migration["after_identifier"], reason=migration["after_reason"])
                require(changed["reason"].strip() and migration["after_identifier"] in changed["reason"], "Missing current ledger rationale")
                require(not any(any(c in value for c in "\t\r\n") for value in changed.values()), "Invalid ledger cell")
                line = ("\t".join(changed[k] for k in fields) + "\n").encode()
                matches[old] += 1
            output.append(line)
        require(all(count == 1 for count in matches.values()), "Reviewed ledger cohort differs")
        after = b"".join(output)
    require(sha(after) == item["after_sha256"], "Reviewed auxiliary output hash differs")
    return after


def execute(plan_path, expected_sha, group, log, *, apply):
    raw = regular(plan_path)
    require(sha(raw) == expected_sha, "Reviewed plan hash differs")
    plan = json.loads(raw)
    require(plan["base_revision"] == BASE and plan["scientific_approval_added"] is False,
            "Wrong base or approval contract")
    require(subprocess.check_output(["git", "merge-base", BASE, "HEAD"], cwd=ROOT).decode().strip() == BASE,
            "Branch is not based on reviewed main")
    names = policy.ingredient_paths(ROOT)
    inputs = {p: regular(p) for p in names}
    require({str(p.relative_to(ROOT)) for p in names} == set(plan["all_owner_sha256"]),
            "Owner inventory changed")
    inputs[Path(plan_path).resolve()] = raw
    for path, content in LOADED.items():
        require(regular(path) == content, "Executed operator/helper changed")
        inputs[path] = content
    for name, expected in plan["evidence_sha256"].items():
        path = ROOT / name
        content = regular(path)
        require(sha(content) == expected, "Evidence changed: " + name)
        inputs[path] = content
    for name, expected in plan["protected_sha256"].items():
        path = ROOT / name
        content = regular(path)
        require(sha(content) == expected, "Protected input changed: " + name)
        inputs[path] = content
    for name, stages in plan.get("auxiliary", {}).items():
        require(name in AUXILIARY_PATHS, "Unreviewed auxiliary destination")
        content = regular(ROOT / name)
        require(stages and len({s["group"] for s in stages}) == len(stages), "Invalid auxiliary stages")
        require(all(a["after_sha256"] == b["before_sha256"] for a, b in zip(stages, stages[1:])), "Auxiliary chain differs")
        selected_stages = [s for s in stages if s["group"] == group]
        allowed = ({selected_stages[0]["before_sha256"]} if selected_stages
                   else {stages[0]["before_sha256"], *(s["after_sha256"] for s in stages)})
        require(sha(content) in allowed, "Unexpected auxiliary reference change")
        inputs[ROOT / name] = content
    selected = {name: item for name, item in plan["owners"].items() if item["group"] == group}
    require(selected, "No reviewed owners in this group")
    for path in names:
        name = str(path.relative_to(ROOT))
        item = plan["owners"].get(name)
        allowed = {plan["all_owner_sha256"][name]}
        if item and item["group"] != group:
            allowed.add(item["after_sha256"])
        require(sha(inputs[path]) in allowed, "Unrelated or unexpected owner change: " + name)
    outputs = {}
    records = []
    backups = {}
    for name, item in sorted(selected.items()):
        before = inputs[ROOT / name]
        after = propose(before, item, plan["timestamp"])
        outputs[Path(name)] = after
        backups[log.with_name(log.stem + ".before-" + Path(name).name)] = before
        records.append({"source_record": name, "shape": item["shape"],
                        "before_yaml_sha256": sha(before), "after_yaml_sha256": sha(after),
                        "change": item["event_changes"], "verification": item["verification"]})
    auxiliary_receipt = {}
    for name, stages in plan.get("auxiliary", {}).items():
        for item in stages:
            if item["group"] != group:
                continue
            outputs[Path(name)] = propose_auxiliary(name, inputs[ROOT / name], item)
            backups[log.with_name(log.stem + ".before-" + Path(name).name)] = inputs[ROOT / name]
            auxiliary_receipt[name] = item

    def scope():
        require(policy.ingredient_paths(ROOT) == names, "Owner inventory changed during publication")

    result = {"phase": "step7d-reviewed-owner-" + group,
              "base_revision": BASE, "plan_sha256": expected_sha,
              "approval": "NONE: source correction; changed owner bytes withdraw inherited support.",
              "scientific_approval_added": False, "supervisor_binding": None,
              "records": records,
              "auxiliary": auxiliary_receipt,
              "input_sha256": {str(p): sha(b) for p, b in inputs.items()},
              "output_sha256": {str(p): sha(b) for p, b in outputs.items()}}
    return publication.publish(ROOT, outputs, inputs, log, backups, result,
                               apply=apply, validate_scope=scope)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--plan", type=Path, required=True)
    parser.add_argument("--plan-sha256", required=True)
    parser.add_argument("--group", required=True)
    parser.add_argument("--log", type=Path, required=True)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    require(args.log.parent.is_dir() and args.log.absolute() == args.log.resolve(), "Resolved receipt parent required")
    from plugins.lock_manager import LockManager
    from plugins.repository_settings import RepositorySettings
    require(RepositorySettings.from_environment().get_target("mediaingredientmech").path.resolve() == ROOT,
            "Configured MIM root differs")
    with LockManager().lock("mediaingredientmech", "Step7d reviewed owner corrections"):
        result = execute(args.plan, args.plan_sha256, args.group, args.log, apply=args.apply)
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
