"""Hash read-only repositories/inputs, run native diagnostic and compare TSVs."""
from pathlib import Path
from collections import Counter
from datetime import datetime, timezone
import csv
import gzip
import hashlib
import io
import json
import os
import stat
import subprocess
import sys

HERE = Path(__file__).resolve().parent
RUN = HERE.parents[1]
W = RUN / "step7d"
CLAW = RUN / "step7c-claw"
CULTURE = Path("/Users/marcin/Documents/VIMSS/ontology/Mechs/CultureMech")
REPOS = {"mim": W, "claw": CLAW, "culture": CULTURE}
EXPECTED = {"mim": sys.argv[1], "claw": "3022b8738dcc9e01c7464a8d5c95aa9be2eef141", "culture": "a74dd489720c9df96cc073ffd11568d407d3c06c"}


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def file_info(path):
    info = path.lstat()
    if stat.S_ISLNK(info.st_mode):
        raw = os.fsencode(os.readlink(path))
        return {"mode": "symlink", "bytes": len(raw), "sha256": digest(raw)}
    assert stat.S_ISREG(info.st_mode), path
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            h.update(chunk)
    return {"mode": oct(stat.S_IMODE(info.st_mode)), "bytes": info.st_size, "sha256": h.hexdigest()}


def git(root, *args):
    return subprocess.check_output(["git", *args], cwd=root, env={**os.environ, "GIT_OPTIONAL_LOCKS": "0"})


def repository_inventory():
    result = {}
    for name, root in REPOS.items():
        assert git(root, "rev-parse", "HEAD").decode().strip() == EXPECTED[name]
        assert not git(root, "status", "--porcelain=v1", "--untracked-files=all").strip(), name
        names = [os.fsdecode(value) for value in git(root, "ls-files", "-z").split(b"\0") if value]
        result[name] = {n: file_info(root / n) for n in names}
    return result


def input_inventory():
    paths = set((CULTURE / "data/normalized_yaml").rglob("*.yaml"))
    for category in ("mapped", "unmapped"):
        paths.update((W / "data/ingredients" / category).glob("*.yaml"))
    paths.update(W / n for n in ("docs/data/label_index.csv", "mappings/unified_mapping_rejections.tsv", "UNIFIED_INGREDIENT_MAPPING.tsv", "UNIFIED_INGREDIENT_MAPPING.provenance.json"))
    paths.add(CLAW / "scripts/build_unified_ingredient_mapping.py")
    paths.add(CLAW / "plugins/ingredient_name_normalizer.py")
    paths.add(CLAW / "plugins/__init__.py")
    paths.update((CLAW / "src/kg_microbe_fleet").rglob("*.py"))
    paths.add(CLAW / "src/kg_microbe_fleet/fleet.yaml")
    for path in paths:
        assert not any(parent.is_symlink() for parent in (path, *path.parents)), path
    return {str(path): file_info(path) for path in sorted(paths)}


def save(name, value):
    raw = (json.dumps(value, indent=2, sort_keys=True) + "\n").encode()
    with (HERE / name).open("xb") as stream:
        stream.write(gzip.compress(raw, compresslevel=3, mtime=0) if name.endswith(".gz") else raw)
    return digest(raw)


start = datetime.now(timezone.utc).isoformat()
print("Capturing complete tracked-file and native-input inventories", flush=True)
before = repository_inventory()
inputs = input_inventory()
before_hash = save("tracked-before.json.gz", before)
inputs_hash = save("inputs-before.json.gz", inputs)
producer = CLAW / "scripts/build_unified_ingredient_mapping.py"
with (HERE / "executed-producer.py").open("xb") as stream:
    stream.write(producer.read_bytes())
(HERE / "output").mkdir(mode=0o700)
env = dict(os.environ)
for key in ("PYTHONPATH", "KG_MICROBE_FLEET_MANIFEST", "KGMICROBE_ROOT", "COMMUNITYMECH_ROOT"):
    env.pop(key, None)
env.update(GIT_PYTHON_GIT_EXECUTABLE="/usr/bin/git", PYTHONDONTWRITEBYTECODE="1", CULTUREMECH_ROOT=str(CULTURE), MEDIAINGREDIENTMECH_ROOT=str(W), CLAW_ROOT=str(CLAW), GIT_OPTIONAL_LOCKS="0")
argv = [sys.executable, "-B", str(HERE / "execute_native.py")]
print("Running unchanged native CLI in audit-constrained child", flush=True)
with (HERE / "native.log").open("x") as log:
    process = subprocess.run(argv, cwd=CLAW, env=env, stdout=log, stderr=subprocess.STDOUT)
save("command.json", {"argv": argv, "cwd": str(CLAW), "started_at": start, "completed_at": datetime.now(timezone.utc).isoformat(), "exit_code": process.returncode, "log_sha256": digest((HERE / "native.log").read_bytes()), "roots": {name: str(root) for name, root in REPOS.items()}, "revisions": EXPECTED, "stamping_or_promotion": False})
print("Rechecking all tracked bytes, native input membership, revisions and clean status", flush=True)
after = repository_inventory()
after_inputs = input_inventory()
save("tracked-after.json.gz", after)
save("inputs-after.json.gz", after_inputs)
assert before == after, "Tracked repository changed during diagnostic"
assert inputs == after_inputs, "Native input bytes/membership changed during diagnostic"
save("stability.json", {"status": "PASS", "tracked_inventory_sha256": before_hash, "native_input_inventory_sha256": inputs_hash, "tracked_counts": {name: len(values) for name, values in before.items()}, "input_count": len(inputs), "unchanged_all_tracked_files": True, "unchanged_all_inputs_and_membership": True, "unchanged_heads_and_clean_worktrees": True, "after_tracked_inventory_sha256": digest((json.dumps(after, indent=2, sort_keys=True) + "\n").encode()), "after_input_inventory_sha256": digest((json.dumps(after_inputs, indent=2, sort_keys=True) + "\n").encode())})
assert process.returncode == 0, "Native build failed; retained command/log/stability"
audit = json.loads((HERE / "worker-audit.json").read_bytes())
assert audit["status"] == "PASS" and not audit["refused_events"]
published_raw = (W / "UNIFIED_INGREDIENT_MAPPING.tsv").read_bytes()
diagnostic_raw = (HERE / "output/UNIFIED_INGREDIENT_MAPPING.tsv").read_bytes()


def table(raw):
    reader = csv.DictReader(io.StringIO(raw.decode(), newline=""), delimiter="\t")
    rows = list(reader)
    assert all(None not in row and None not in row.values() for row in rows)
    assert len({row["ingredient_name"] for row in rows}) == len(rows)
    return reader.fieldnames, rows


old_columns, old_rows = table(published_raw)
new_columns, new_rows = table(diagnostic_raw)
assert old_columns == new_columns
old = {row["ingredient_name"]: row for row in old_rows}
new = {row["ingredient_name"]: row for row in new_rows}
common = set(old) & set(new)
changed = []
for name in sorted(common):
    fields = [key for key in old_columns if old[name][key] != new[name][key]]
    if fields:
        changed.append({"ingredient_name": name, "changed_fields": fields, "before": old[name], "after": new[name]})
save("row-diff.json", {"changed": changed, "added": [new[n] for n in sorted(set(new)-set(old))], "removed": [old[n] for n in sorted(set(old)-set(new))]})
comparison = {
    "status": "PASS_FULL_NATIVE_DIAGNOSTIC_COMPARISON", "published_sha256": digest(published_raw), "diagnostic_sha256": digest(diagnostic_raw),
    "bytes_identical": published_raw == diagnostic_raw, "rows_before": len(old_rows), "rows_after": len(new_rows),
    "added_names": len(set(new)-set(old)), "removed_names": len(set(old)-set(new)), "changed_rows": len(changed), "unchanged_rows": len(common)-len(changed),
    "same_row_order": [r["ingredient_name"] for r in old_rows] == [r["ingredient_name"] for r in new_rows],
    "occurrences_before": sum(int(row["occurrence_count"]) for row in old_rows), "occurrences_after": sum(int(row["occurrence_count"]) for row in new_rows),
    "changed_field_counts": dict(Counter(field for row in changed for field in row["changed_fields"])),
    "row_change_classes": dict(Counter(" + ".join(row["changed_fields"]) for row in changed)),
    "status_counts_before": dict(Counter(row["mapping_status"] for row in old_rows)), "status_counts_after": dict(Counter(row["mapping_status"] for row in new_rows)),
    "changed_names": [row["ingredient_name"] for row in changed], "producer_revision": EXPECTED["claw"], "mim_revision": EXPECTED["mim"], "culturemech_revision": EXPECTED["culture"],
    "qualification": "Authorized Step7d native rebuild candidate from the explicit clean current source checkpoint; all cells require exact reviewed owner-operation traces before publication. Only /usr/bin/git version subprocess allowed for native import initialization. No provider/network, canonical write, provenance stamp, permission inference, promotion or scientific approval. Native CLI does not consume KG/CommunityMech in this path.",
    "scientific_approval_added": False,
}
save("comparison.json", comparison)
cell_changes = [{"ingredient_name": row["ingredient_name"], "column": field, "before": row["before"][field], "after": row["after"][field], "before_mim_id": row["before"]["mim_id"], "after_mim_id": row["after"]["mim_id"]} for row in changed for field in row["changed_fields"]]
save("cell-diff.json", {"count": len(cell_changes), "cells": cell_changes, "added_rows": len(set(new)-set(old)), "removed_rows": len(set(old)-set(new)), "scientific_approval_added": False})
with (HERE / "cell-diff.tsv").open("x", newline="") as stream:
    writer = csv.DictWriter(stream, fieldnames=["ingredient_name", "column", "before", "after", "before_mim_id", "after_mim_id"], delimiter="\t")
    writer.writeheader(); writer.writerows(cell_changes)
print(json.dumps(comparison, indent=2), flush=True)
