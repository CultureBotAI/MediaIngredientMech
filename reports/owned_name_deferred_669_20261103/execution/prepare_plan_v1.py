"""Freeze the exact deferred-23 proposal; writes new evidence only, never maintained outputs."""
from pathlib import Path
import csv
import hashlib
import importlib.util
import io
import json
import os
import subprocess
import sys

import jsonschema
import yaml

D = Path(__file__).resolve().parent
RUN = D.parent
W = RUN / "step8-aliases"
BASE = "0ee56c11a2894ed50a476b331d56297be0a3ee12"
PRODUCER = RUN / "step7c-claw"
PRODUCER_REV = "3022b8738dcc9e01c7464a8d5c95aa9be2eef141"
REPORT = W / "reports/owned_name_deferred_669_20261103"
GEN = W / "output/next23-native-candidate-v1"
SCHEMA_PATH = RUN / "step7d-execution-20261103/next23-context-contract-v2/contract.schema.json"
SCHEMA_SHA = "bff468962fe5e79ec3726005a289138fed8542cb5a02d0574e16e1fdb459326b"
POLICY = "https://github.com/CultureBotAI/MediaIngredientMech/issues/669#issuecomment-6622570751"
SOURCE = "mappings/ingredient_mappings.sssom.tsv"
SIDECAR = "mappings/suppressed_aliases.tsv"
BASELINE = "mappings/other_cross_record_baseline.tsv"

sys.path[:0] = [str(W), str(W / "src")]
from mediaingredientmech.curie import mim_curie_for_stem
from mediaingredientmech.synonym_policy import preferred_term_owners


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def read(path):
    assert path.is_absolute() and path == path.resolve() and path.is_file() and not path.is_symlink(), path
    return path.read_bytes()


def write(path, raw):
    assert path == path.resolve() and not os.path.lexists(path), path
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("xb") as handle:
        handle.write(raw)


def encode(value):
    return (json.dumps(value, indent=2, ensure_ascii=False) + "\n").encode()


def reference(path):
    return {"path": str(path.relative_to(W)), "sha256": sha(read(path))}


def table(raw):
    return list(csv.DictReader(io.StringIO(raw.decode()), delimiter="\t"))


def tree():
    raw = subprocess.check_output(["git", "-C", str(W), "ls-tree", "-r", "-z", BASE])
    result = {}
    for entry in raw.split(b"\0"):
        if entry:
            meta, name = entry.split(b"\t", 1)
            mode, kind, oid = meta.split()
            result[name.decode()] = (mode, kind, oid.decode())
    return result


def inventory(prefix, git_tree):
    found = {}
    for parent, dirs, files in os.walk(W / prefix, followlinks=False):
        for name in dirs + files:
            assert not (Path(parent) / name).is_symlink(), name
        for name in files:
            path = Path(parent) / name
            if path.suffix in {".yaml", ".yml"}:
                found[str(path.relative_to(W))] = sha(read(path))
    expected = {p for p in git_tree if p.startswith(prefix + "/") and Path(p).suffix in {".yaml", ".yml"}}
    assert set(found) == expected, (prefix, set(found) ^ expected)
    return dict(sorted(found.items()))


def main():
    assert not os.path.lexists(REPORT), "Preserve prior report; use a new immutable output"
    schema_raw = read(SCHEMA_PATH)
    assert sha(schema_raw) == SCHEMA_SHA
    schema = json.loads(schema_raw)
    assert subprocess.check_output(["git", "-C", str(W), "rev-parse", "HEAD"]).decode().strip() == BASE
    assert subprocess.check_output(["git", "-C", str(PRODUCER), "rev-parse", "HEAD"]).decode().strip() == PRODUCER_REV
    assert not subprocess.check_output(["git", "-C", str(PRODUCER), "status", "--porcelain", "--untracked-files=all"])
    audit = json.loads(read(D / "fresh-scope-v2/preflight-v2.json"))
    assessed = json.loads(read(D / "fresh-scope-v2/pair-preflight-v2.json"))
    for name, digest in audit["input_sha256"].items():
        assert sha(read(Path(name))) == digest, name
    assert audit["mim_head"] == BASE and len(assessed) == 23
    before = {name: read(W / name) for name in (SOURCE, SIDECAR, BASELINE)}
    git_tree = tree()
    protected = schema["$defs"]["inventory"]["properties"]["protected_sha256"]["properties"]
    inv = {"schema_version": 1, "operation": "owned-name-suppression-inventory-v1", "baseline": BASE,
           "ingredient_sha256": inventory("data/ingredients", git_tree),
           "aggregate_sha256": inventory("data/curated", git_tree),
           "protected_sha256": {name: sha(read(W / name)) for name in protected}}
    for name in set(inv["ingredient_sha256"]) | set(inv["aggregate_sha256"]) | set(protected) | set(before):
        raw = read(W / name)
        mode, kind, oid = git_tree[name]
        assert mode in {b"100644", b"100755"} and kind == b"blob"
        assert hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest() == oid, name
    jsonschema.validate(inv, schema)
    mapped = {mim_curie_for_stem(p.stem): p for p in sorted((W / "data/ingredients/mapped").glob("*.yaml"))}
    records = {subject: yaml.safe_load(read(path)) for subject, path in mapped.items()}
    owners = preferred_term_owners(records)
    policy_path = PRODUCER / "src/kg_microbe_utils/owned_name_policy.py"
    spec = importlib.util.spec_from_file_location("deferred23_plan_native_policy", policy_path)
    native = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = native
    exec(compile(read(policy_path), str(policy_path), "exec"), native.__dict__)
    assert native.build_owner_index(records) == owners
    raw_lines = before[SOURCE].decode().splitlines(keepends=True)
    header_position = next(i for i, line in enumerate(raw_lines) if not line.startswith("#"))
    fields = raw_lines[header_position].rstrip("\n").split("\t")
    source_rows = list(csv.DictReader(raw_lines[header_position:], delimiter="\t"))
    assert len(source_rows) == 3014
    baseline_rows = table(before[BASELINE])
    assert baseline_rows == [item["baseline"] for item in assessed]
    baseline_after = before[BASELINE].splitlines(keepends=True)[0]
    projected = list(raw_lines)
    pairs, new_events = [], []
    candidate_rows = list(csv.DictReader([line for line in read(GEN / "candidate.sssom.tsv").decode().splitlines() if not line.startswith("#")], delimiter="\t"))
    candidate_pairs = {(r["subject_id"], r["token_key"]) for r in table(read(GEN / "suppressed_aliases.tsv"))}
    for item in assessed:
        assert len(item["canonical_occurrences"]) == 1 and not item["yaml_aliases"] and item["candidate_suppression"] is None
        occurrence = item["canonical_occurrences"][0]
        position, subject, key = occurrence["position"], item["subject_id"], item["token_key"]
        row = source_rows[position - 1]
        assert row == occurrence["row"] and occurrence["current_disposition"] == "WITHHOLD"
        assert row["subject_id"] == subject and subject not in owners[key]
        assert not any(r["subject_id"] == subject and key in {t.strip().casefold() for t in r["other"].split("|")} for r in candidate_rows)
        assert (subject, key) not in candidate_pairs
        assert not any(str(s.get("synonym_text", "")).strip().casefold() == key for s in records[subject].get("synonyms", []))
        raw_tokens = row["other"].split("|")
        assert sum(t.strip().casefold() == key for t in raw_tokens) == 1
        after_other = "|".join(t for t in raw_tokens if t.strip().casefold() != key)
        index = header_position + position
        raw_cells = raw_lines[index].rstrip("\n").split("\t")
        assert dict(zip(fields, raw_cells, strict=True)) == row
        raw_cells[fields.index("other")] = after_other
        projected[index] = "\t".join(raw_cells) + "\n"
        source_ref = f"{SOURCE}#source_position={position}&subject_id={subject}&predicate_id={row['predicate_id']}&object_id={row['object_id']}&field=other@sha256={sha(before[SOURCE])}"
        kept, events = native.filter_owned_aliases(subject, [native.AliasCandidate(item["token"], "prior_sssom", (source_ref,), (POLICY,))], owners)
        assert not kept and len(events) == 1
        new_events.extend(events)
        pairs.append({"baseline_row": item["baseline"], "token_key": key, "source_position": position,
                      "selector": {**{k: row[k] for k in ("subject_id", "predicate_id", "object_id")}, "field": "other"},
                      "before_row": row, "after_other": after_other, "source_owner": reference(mapped[subject]),
                      "credited_owners": [{"subject_id": owner, **reference(mapped[owner])} for owner in sorted(owners[key])],
                      "source_ref": source_ref, "input_surfaces": ["prior_sssom"], "disposition": "SUPPRESS", "review_disposition": "WITHHOLD"})
    old_rows = table(before[SIDECAR])
    old_events = []
    for row in old_rows:
        for surface in json.loads(row["input_surfaces"]):
            old_events.append(native.Suppression(row["subject_id"], row["token"], frozenset(json.loads(row["owner_subject_ids"])), surface,
                                                tuple(json.loads(row["source_refs"])), tuple(json.loads(row["evidence_refs"]))))
    assert native.render_suppressed_aliases(old_events) == before[SIDECAR]
    sidecar_after = native.render_suppressed_aliases(old_events + new_events)
    new_rows = {(r["subject_id"], r["token_key"]): r for r in table(sidecar_after)}
    assert len(new_rows) == 34 and all(new_rows[(r["subject_id"], r["token_key"])] == r for r in old_rows)
    after = {SOURCE: "".join(projected).encode(), SIDECAR: sidecar_after, BASELINE: baseline_after}
    assert sum(a != b for a, b in zip(raw_lines, projected, strict=True)) == 23
    REPORT.mkdir()
    for path in sorted(GEN.rglob("*")):
        assert not path.is_symlink(), path
        if path.is_file():
            write(REPORT / "generation" / path.relative_to(GEN), read(path))
    write(REPORT / "contract.schema.json", schema_raw)
    write(REPORT / "unchanged-inventory.json", encode(inv))
    generation = {"producer_revision": PRODUCER_REV}
    for key, name in {"candidate": "candidate.sssom.tsv", "sidecar": "suppressed_aliases.tsv", "manifest": "candidate.sssom.tsv.manifest.json", "receipt": "generation-receipt.json"}.items():
        generation[key] = reference(REPORT / "generation" / name)
    plan = {"schema_version": 1, "operation": "owned-name-suppression-plan-v1", "issue": 669,
            "issue_url": "https://github.com/CultureBotAI/MediaIngredientMech/issues/669",
            "scope": schema["$defs"]["plan"]["properties"]["scope"]["const"],
            "approval": schema["$defs"]["plan"]["properties"]["approval"]["const"], "baseline": BASE, "policy_evidence": POLICY,
            "artifacts_before": {p: sha(raw) for p, raw in before.items()}, "artifacts_after": {p: sha(raw) for p, raw in after.items()},
            "unchanged_inventory": reference(REPORT / "unchanged-inventory.json"), "generation": generation, "receipt_sequence": 26, "pairs": pairs}
    jsonschema.validate(plan, schema)
    write(REPORT / "publication-plan.json", encode(plan))
    for name, raw in before.items():
        write(REPORT / "before" / Path(name).name, raw)
    write(REPORT / "before/ingredient_mappings.sssom.tsv.manifest.json", read(W / "mappings/ingredient_mappings.sssom.tsv.manifest.json"))
    for name, raw in after.items():
        write(REPORT / "proposed" / Path(name).name, raw)
    write(REPORT / "execution/prepare_plan_v1.py", read(Path(__file__).resolve()))
    for path in sorted((D / "fresh-scope-v2").iterdir()):
        if path.is_file():
            write(REPORT / "preflight" / path.name, read(path))
    for name in ("issue669-scope-comment-v1.md", "issue669-scope-comment-action-v1.json", "test-empty-baseline-issue-body-v1.md", "test-empty-baseline-issue-create.json"):
        write(REPORT / "preflight" / name, read(D / name))
    (REPORT / "application").mkdir()
    for name, raw in before.items():
        assert read(W / name) == raw
    receipt = {"plan": reference(REPORT / "publication-plan.json"), "inventory": reference(REPORT / "unchanged-inventory.json"),
               "artifacts_before": plan["artifacts_before"], "artifacts_after": plan["artifacts_after"], "scientific_approval_added": False,
               "maintained_data_writes": False, "source_inventory_files": len(inv["ingredient_sha256"])}
    write(D / "prepared-plan-v1.json", encode(receipt))
    print(json.dumps(receipt, indent=2))


if __name__ == "__main__":
    main()
