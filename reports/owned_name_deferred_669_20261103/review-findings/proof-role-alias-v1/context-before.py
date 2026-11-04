"""Prove the bounded #669 export-only suffix without renewing scientific support.

The old manifest's canonical hash is a historical receipt checkpoint. Native
payload replay bridges it to the durable baseline; historical owner attribution
is never rebound. Generation is hash-bound attribution, replayed by the publisher.
"""

from __future__ import annotations

import csv
import hashlib
import io
import json
import os
import re
import stat
import subprocess
from copy import deepcopy
from pathlib import Path

from mediaingredientmech.curie import mim_curie_for_stem
from mediaingredientmech.ingredient_bundle_contract import (
    Draft202012Validator,
    _base_table,
    content_sha256,
    read_json,
    safe_member,
)
from mediaingredientmech.mapping_scope import _load_yaml
from mediaingredientmech.registry_correction_refresh import receipt_inventory
from mediaingredientmech.synonym_policy import preferred_term_owners
from mediaingredientmech.validation.mapping_change_receipts import (
    HISTORICAL_CONTEXT,
    RECEIPTS_DIR,
    SSSOM_SOURCE,
    verify_mapping_chain,
)

MANIFEST = SSSOM_SOURCE + ".manifest.json"
SIDECAR = "mappings/suppressed_aliases.tsv"
BASELINE = "mappings/other_cross_record_baseline.tsv"
ARTIFACTS = (SSSOM_SOURCE, SIDECAR, BASELINE)
UPDATE = "owned_name_suppression_updates"
ISSUE = "https://github.com/CultureBotAI/MediaIngredientMech/issues/669"
SCOPE = "Export-only suppression of the 23 reviewed owned-name alias pairs; no scientific approval"
APPROVAL = "NONE: every touched row is withheld pending mapping-specific review; no prior approval carries across this link."
SCHEMA = "src/mediaingredientmech/profiles/owned_name_suppression_v1.schema.json"
PROTECTED = (
    "UNIFIED_INGREDIENT_MAPPING.tsv",
    "UNIFIED_INGREDIENT_MAPPING.provenance.json",
    "docs/data/label_index.csv",
    "MAPPING_SEMANTICS.md",
    ".github/workflows/qc-evidence.yaml",
    "scripts/.vendored_canon_ref",
    "justfile",
    "pyproject.toml",
    "src/mediaingredientmech/synonym_policy.py",
    "src/mediaingredientmech/curie.py",
    "src/mediaingredientmech/profiles/ingredient_bundle_v1.schema.json",
    "src/mediaingredientmech/profiles/ingredient_scope_v1.yaml",
)
VERIFIERS = tuple(
    "src/mediaingredientmech/" + name
    for name in (
        "owned_name_suppression_refresh.py",
        "ingredient_bundle_refresh.py",
        "ingredient_bundle_contract.py",
        "registry_correction_refresh.py",
        "validation/mapping_change_receipts.py",
        "export/reviewed_sssom.py",
        "curie.py",
        "mapping_scope.py",
        "review_claims.py",
        "synonym_policy.py",
        "sssom_metadata.py",
    )
)
_PACKAGE_DIR = Path(__file__).resolve().parent
_LOADED = {
    name: (_PACKAGE_DIR / name.removeprefix("src/mediaingredientmech/")).read_bytes()
    for name in (*VERIFIERS, SCHEMA)
}
_SCHEMA = read_json(_LOADED[SCHEMA])
_SIDECAR_FIELDS = (
    "subject_id",
    "token_key",
    "token",
    "owner_subject_ids",
    "disposition",
    "input_surfaces",
    "source_refs",
    "evidence_refs",
)


def require(condition, message):
    if not condition:
        raise ValueError("Owned-name suppression: " + message)


def member(root, name):
    path = safe_member(root, name)
    require(path == path.resolve(), "aliased proof path: " + name)
    require(
        all(not p.is_symlink() for p in (path, *path.parents)),
        "symlink proof path: " + name,
    )
    require(path.is_file() and stat.S_ISREG(path.stat().st_mode), "non-regular proof: " + name)
    return path


def _shape(value, kind):
    schema = {"$ref": "#/$defs/" + kind, "$defs": _SCHEMA["$defs"]}
    errors = sorted(Draft202012Validator(schema).iter_errors(value), key=lambda e: str(e.path))
    require(not errors, "invalid " + kind + " shape" + (": " + errors[0].message if errors else ""))
    require(type(value["schema_version"]) is int, "schema version must be an integer")
    if "issue" in value:
        require(type(value["issue"]) is int, "issue must be an integer")
    if kind == "plan":
        require(type(value["receipt_sequence"]) is int, "receipt sequence must be an integer")
    if kind == "update":
        require(
            type(value["mapping_receipt"]["sequence"]) is int
            and type(value["historical_checkpoint"]["sequence"]) is int
            and all(type(n) is int for n in value["historical_checkpoint"]["bridge_sequences"]),
            "receipt/checkpoint sequence must be an integer",
        )


def _tree(root, baseline):
    raw = subprocess.check_output(["git", "ls-tree", "-r", "-z", baseline], cwd=root)
    result = {}
    for item in raw.split(b"\0"):
        if not item:
            continue
        metadata, name = item.split(b"\t", 1)
        mode, kind, oid = metadata.decode().split()
        result[name.decode()] = (mode, kind, oid)
    return result


def _historical_equal(tree, name, raw):
    expected = hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()
    require(
        name in tree
        and tree[name][0] in {"100644", "100755"}
        and tree[name][1] == "blob"
        and tree[name][2] == expected,
        "durable baseline bytes differ: " + name,
    )


def source_inventory(root):
    """Ignored-inclusive YAML membership; reject directory aliases before walking."""
    result = {}
    for folder in ("data/ingredients", "data/curated"):
        base = root / folder
        require(base.is_dir() and base == base.resolve(), "aliased source directory")
        found: list[str] = []
        for directory, dirs, files in os.walk(base, followlinks=False):
            for name in (*dirs, *files):
                path = Path(directory) / name
                require(not path.is_symlink(), "aliased source inventory member")
            found.extend(
                (Path(directory) / name).relative_to(root).as_posix()
                for name in files
                if Path(name).suffix in {".yaml", ".yml"}
            )
        result[folder] = sorted(found)
    return result


def recheck_inventory(root, proof):
    """Repeat both exhaustive memberships after publication has reserved outputs."""
    require(
        source_inventory(root) == proof["source_paths"],
        "source inventory changed during verification",
    )
    require(
        receipt_inventory(root) == set(proof["receipt_paths"]),
        "receipt inventory changed during verification",
    )


def _table(raw):
    stream = io.StringIO(raw.decode(), newline="")
    reader = csv.DictReader(stream, delimiter="\t")
    rows = list(reader)
    require(reader.fieldnames is not None, "missing TSV header")
    require(all(None not in r and None not in r.values() for r in rows), "ragged TSV")
    return reader.fieldnames, rows


def source_reference(pair, before_sha):
    row = pair["before_row"]
    return (
        f"{SSSOM_SOURCE}#source_position={pair['source_position']}"
        f"&subject_id={row['subject_id']}&predicate_id={row['predicate_id']}"
        f"&object_id={row['object_id']}&field=other@sha256={before_sha}"
    )


def expected_record(pair, plan_ref):
    """Truthful export-only maker input; it asserts no fabricated YAML event."""
    return {
        "source_record": pair["source_owner"]["path"],
        "shape": "export_only_owned_name_suppression",
        "before_yaml_sha256": pair["source_owner"]["sha256"],
        "after_yaml_sha256": pair["source_owner"]["sha256"],
        "change": f"SUPPRESS {pair['baseline_row']['token']} from SSSOM other only; source YAML unchanged; no identity, role or release approval.",
        "verification": f"Owned-name export policy #669; preferred-name credits and prior-only provenance are frozen in {plan_ref['path']} sha256={plan_ref['sha256']}.",
    }


def _pairs(plan, old, new, source_bytes):
    baseline_fields, obligations = _table(old[BASELINE])
    require(
        baseline_fields == ["subject_id", "token", "owned_by", "disposition"],
        "baseline columns differ",
    )
    require(
        [p["baseline_row"] for p in plan["pairs"]] == obligations,
        "plan differs from complete baseline",
    )
    require(
        new[BASELINE] == old[BASELINE].splitlines(keepends=True)[0], "baseline retirement differs"
    )
    _, fields, old_rows = _base_table(old[SSSOM_SOURCE])
    _, new_fields, new_rows = _base_table(new[SSSOM_SOURCE])
    require(
        fields == new_fields and len(old_rows) == len(new_rows),
        "canonical row/column count differs",
    )
    records = {
        mim_curie_for_stem(Path(name).stem): _load_yaml(raw.decode())
        for name, raw in source_bytes.items()
        if Path(name).parent.as_posix() == "data/ingredients/mapped" and name.endswith(".yaml")
    }
    paths = {
        mim_curie_for_stem(Path(name).stem): name
        for name in source_bytes
        if Path(name).parent.as_posix() == "data/ingredients/mapped" and name.endswith(".yaml")
    }
    require(
        len(records)
        == sum(
            Path(name).parent.as_posix() == "data/ingredients/mapped" and name.endswith(".yaml")
            for name in source_bytes
        ),
        "ambiguous mapped source subjects",
    )
    owners = preferred_term_owners(records)
    label_rows = list(
        csv.DictReader(io.StringIO(source_bytes["docs/data/label_index.csv"].decode()))
    )
    selected = {}
    pair_keys = set()
    for pair in plan["pairs"]:
        position = pair["source_position"]
        require(type(position) is int and 1 <= position <= len(old_rows), "invalid source position")
        row = old_rows[position - 1]
        subject, token = pair["baseline_row"]["subject_id"], pair["baseline_row"]["token"]
        key = token.strip().casefold()
        require(
            (subject, key) not in pair_keys and position not in selected,
            "duplicate planned pair/position",
        )
        pair_keys.add((subject, key))
        require(
            pair["token_key"] == key and row == pair["before_row"] and row["subject_id"] == subject,
            "stale pair payload",
        )
        require(
            pair["selector"]
            == {
                **{k: row[k] for k in ("subject_id", "predicate_id", "object_id")},
                "field": "other",
            },
            "pair selector differs",
        )
        require(subject in paths, "unresolved subject owner")
        require(
            pair["source_owner"]
            == {"path": paths[subject], "sha256": content_sha256(source_bytes[paths[subject]])},
            "source owner differs",
        )
        credited = owners.get(key, frozenset())
        require(credited and subject not in credited, "token is not owned by another record")
        require(all(owner in paths for owner in credited), "unresolved credited owner")
        expected = [
            {
                "subject_id": owner,
                "path": paths[owner],
                "sha256": content_sha256(source_bytes[paths[owner]]),
            }
            for owner in sorted(credited)
        ]
        require(pair["credited_owners"] == expected, "native credited owner set differs")
        # owned_by is historical display text only: it neither selects nor parses credits.
        hits = [r for r in label_rows if r["label"].strip().casefold() == key]
        credited_ids = {str(records[owner].get("identifier", "")) for owner in credited}
        require(
            hits
            and hits[0]["match_type"] == "preferred_term"
            and hits[0]["identifier"] in credited_ids,
            "preferred owner is not first in label index",
        )
        aliases = records[subject].get("synonyms", []) or []
        require(
            not any(str(x.get("synonym_text") or "").strip().casefold() == key for x in aliases),
            "fresh YAML origin requires new scope",
        )
        matches = [
            (i, value)
            for i, value in enumerate(row["other"].split("|"))
            if value.strip().casefold() == key
        ]
        require(len(matches) == 1 and matches[0][1] == token, "planned raw token differs")
        result = "|".join(
            value for i, value in enumerate(row["other"].split("|")) if i != matches[0][0]
        )
        require(result == pair["after_other"], "other projection differs")
        require(
            pair["source_ref"] == source_reference(pair, plan["artifacts_before"][SSSOM_SOURCE]),
            "prior-only provenance differs",
        )
        for i, other in enumerate(old_rows, 1):
            require(
                i == position
                or other["subject_id"] != subject
                or not any(t.strip().casefold() == key for t in other["other"].split("|")),
                "selected alias occurs on another old row",
            )
        for other in new_rows:
            require(
                other["subject_id"] != subject
                or not any(t.strip().casefold() == key for t in other["other"].split("|")),
                "selected alias remains published",
            )
        selected[position] = pair
    expected_rows = deepcopy(old_rows)
    for position, pair in selected.items():
        expected_rows[position - 1]["other"] = pair["after_other"]
    require(expected_rows == new_rows, "unrelated canonical cell changed")
    old_lines, new_lines = old[SSSOM_SOURCE].splitlines(keepends=True), new[
        SSSOM_SOURCE
    ].splitlines(keepends=True)
    require(len(old_lines) == len(new_lines), "raw canonical layout differs")
    data_position = -1
    for before_line, after_line in zip(old_lines, new_lines, strict=True):
        if before_line.startswith(b"#"):
            require(before_line == after_line, "canonical header changed")
            continue
        data_position += 1
        if data_position not in selected:
            require(before_line == after_line, "unselected raw row changed")
        else:
            cells = before_line.rstrip(b"\r\n").split(b"\t")
            require(len(cells) == len(fields), "unexpected quoting in planned raw row")
            cells[fields.index("other")] = selected[data_position]["after_other"].encode()
            ending = before_line[len(before_line.rstrip(b"\r\n")) :]
            require(b"\t".join(cells) + ending == after_line, "raw row exceeds exact other cell")
    return old_rows, new_rows, selected


def _sidecar(plan, old, new):
    old_fields, old_rows = _table(old[SIDECAR])
    fields, rows = _table(new[SIDECAR])
    require(tuple(fields) == tuple(old_fields) == _SIDECAR_FIELDS, "sidecar header differs")
    require(
        old[SIDECAR].splitlines(keepends=True)[0] == new[SIDECAR].splitlines(keepends=True)[0],
        "sidecar raw header changed",
    )

    def keyed(values):
        result = {(r["subject_id"], r["token_key"]): r for r in values}
        require(len(result) == len(values), "duplicate sidecar pair")
        return result

    expected = keyed(old_rows)
    for pair in plan["pairs"]:
        row = {
            "subject_id": pair["before_row"]["subject_id"],
            "token_key": pair["token_key"],
            "token": pair["baseline_row"]["token"],
            "disposition": "SUPPRESS",
        }
        for name, value in {
            "owner_subject_ids": [o["subject_id"] for o in pair["credited_owners"]],
            "input_surfaces": ["prior_sssom"],
            "source_refs": [pair["source_ref"]],
            "evidence_refs": [plan["policy_evidence"]],
        }.items():
            row[name] = json.dumps(value, ensure_ascii=False, separators=(",", ":"))
        key = (row["subject_id"], row["token_key"])
        require(key not in expected, "selected pair already suppressed")
        expected[key] = row
    require(keyed(rows) == expected, "sidecar changed historical rows or scoped additions")
    # Native rendering may interleave the entries, but not rewrite their raw bytes.
    old_raw, new_raw = (
        old[SIDECAR].splitlines(keepends=True)[1:],
        new[SIDECAR].splitlines(keepends=True)[1:],
    )
    require(all(new_raw.count(line) == 1 for line in old_raw), "historical raw sidecar row changed")


def verify_owned_name_suppression(prior, before, current, context):
    """Return a captured transition proof; no caller-supplied replay is accepted."""
    from mediaingredientmech.ingredient_bundle_refresh import OwnedNameSuppressionContext

    require(type(context) is OwnedNameSuppressionContext, "explicit exact context required")
    require(context.root.absolute() == context.root.resolve(), "aliased context root")
    root = context.root.resolve()
    require(re.fullmatch(r"[0-9a-f]{40}", context.baseline), "durable baseline required")
    require(re.fullmatch(r"[0-9a-f]{64}", context.manifest_sha256), "invalid caller manifest pin")
    tree = _tree(root, context.baseline)
    inputs: dict[str, str] = {}

    def bind(name, raw):
        digest = content_sha256(raw)
        require(
            name not in inputs or inputs[name] == digest, "conflicting proof input hash: " + name
        )
        inputs[name] = digest
        return raw

    def read(name):
        return bind(name, member(root, name).read_bytes())

    def ref(value):
        raw = read(value["path"])
        require(
            content_sha256(raw) == value["sha256"], "pinned reference differs: " + value["path"]
        )
        return raw

    for name, loaded in _LOADED.items():
        require(read(name) == loaded, "loaded verifier differs: " + name)
    for name, raw in before.items():
        _historical_equal(tree, name, raw)
    for name, raw in current.items():
        require(read(name) == raw, "current snapshot differs: " + name)
    require(
        content_sha256(current[MANIFEST]) == context.manifest_sha256, "caller manifest pin differs"
    )
    old_manifest, manifest = read_json(before[MANIFEST]), read_json(current[MANIFEST])
    prefix, updates = old_manifest.get(UPDATE, []), manifest.get(UPDATE)
    require(
        isinstance(prefix, list)
        and isinstance(updates, list)
        and len(updates) == len(prefix) + 1
        and updates[:-1] == prefix,
        "expected one manifest history append",
    )
    immutable_old = {k: v for k, v in old_manifest.items() if k not in {"artifacts", UPDATE}}
    require(
        immutable_old == {k: v for k, v in manifest.items() if k not in {"artifacts", UPDATE}},
        "historical manifest attribution changed",
    )
    update = updates[-1]
    _shape(update, "update")
    require(
        update["prior_manifest_sha256"] == content_sha256(before[MANIFEST])
        and update["baseline"] == context.baseline,
        "manifest predecessor differs",
    )
    plan = read_json(ref(update["plan"]))
    inventory = read_json(ref(update["unchanged_inventory"]))
    _shape(plan, "plan")
    _shape(inventory, "inventory")
    for field in (
        "baseline",
        "unchanged_inventory",
        "artifacts_before",
        "artifacts_after",
        "generation",
    ):
        require(update[field] == plan[field], "manifest/plan field differs: " + field)
    require(inventory["baseline"] == context.baseline, "inventory baseline differs")
    require(
        set(old_manifest["artifacts"]) == set(manifest["artifacts"]) == set(ARTIFACTS),
        "artifact membership differs",
    )
    for name in ARTIFACTS:
        require(
            plan["artifacts_before"][name] == content_sha256(before[name])
            and plan["artifacts_after"][name]
            == content_sha256(current[name])
            == manifest["artifacts"][name],
            "artifact endpoint differs",
        )
    for name in (SIDECAR, BASELINE):
        require(
            old_manifest["artifacts"][name] == plan["artifacts_before"][name],
            "historical policy endpoint differs",
        )
    actual_inventory = source_inventory(root)
    source_bytes = {}
    for folder, key in (
        ("data/ingredients", "ingredient_sha256"),
        ("data/curated", "aggregate_sha256"),
    ):
        expected_paths = sorted(
            name
            for name in tree
            if name.startswith(folder + "/") and Path(name).suffix in {".yaml", ".yml"}
        )
        require(
            actual_inventory[folder] == expected_paths == sorted(inventory[key]),
            "source path inventory differs",
        )
        for name, expected in inventory[key].items():
            raw = read(name)
            require(content_sha256(raw) == expected, "unchanged source hash differs")
            _historical_equal(tree, name, raw)
            source_bytes[name] = raw
    require(set(inventory["protected_sha256"]) == set(PROTECTED), "protected membership differs")
    for name, expected in inventory["protected_sha256"].items():
        raw = read(name)
        require(content_sha256(raw) == expected, "protected source hash differs")
        _historical_equal(tree, name, raw)
        source_bytes[name] = raw
    old_rows, rows, selected = _pairs(plan, before, current, source_bytes)
    _sidecar(plan, before, current)
    generation = plan["generation"]
    generated = {k: ref(generation[k]) for k in ("candidate", "sidecar", "manifest", "receipt")}
    generated_manifest, generated_receipt = read_json(generated["manifest"]), read_json(
        generated["receipt"]
    )
    expected_generated = {
        "sssom": content_sha256(generated["candidate"]),
        "suppressed_aliases": content_sha256(generated["sidecar"]),
    }
    artifacts = generated_manifest.get("artifacts", [])
    require(
        len(artifacts) == 2
        and {item["role"]: item["sha256"] for item in artifacts} == expected_generated,
        "native generation pair attribution differs",
    )
    require(
        generated_manifest.get("external_sssom_validation") == "passed",
        "native generation validation is absent",
    )
    require(
        generated_receipt["producer_revision"]
        == generation["producer_revision"]
        == generated_manifest["source_revisions"]["claw"],
        "generation producer differs",
    )
    for key, field in (
        ("candidate", "candidate_sha256"),
        ("sidecar", "sidecar_sha256"),
        ("manifest", "native_generation_manifest_sha256"),
    ):
        require(
            generated_receipt[field] == content_sha256(generated[key]),
            "generation artifact attribution differs",
        )
    require(
        generated_receipt["prior_sha256"] == plan["artifacts_before"][SSSOM_SOURCE]
        and generated_receipt["input_bytes_unchanged"] is True
        and generated_receipt["scientific_approval_added"] is False,
        "generation preimage/scope differs",
    )
    _, candidate_rows = _table(
        b"".join(
            line
            for line in generated["candidate"].splitlines(keepends=True)
            if not line.startswith(b"#")
        )
    )
    _, diagnostic_rows = _table(generated["sidecar"])
    for pair in plan["pairs"]:
        subject, key = pair["before_row"]["subject_id"], pair["token_key"]
        require(
            not any(r["subject_id"] == subject and r["token_key"] == key for r in diagnostic_rows),
            "fresh candidate origin requires new scope",
        )
        require(
            not any(
                r["subject_id"] == subject
                and any(t.strip().casefold() == key for t in r["other"].split("|"))
                for r in candidate_rows
            ),
            "candidate still publishes selected token",
        )
    proof = verify_mapping_chain(root)
    for name, expected in proof["input_hashes"].items():
        require(
            name not in inputs or inputs[name] == expected,
            "conflicting native replay input: " + name,
        )
        inputs[name] = expected
        require(content_sha256(read(name)) == expected, "native replay input changed")
    old_receipts = {
        name for name in tree if name.startswith(RECEIPTS_DIR + "/") and name.endswith(".json")
    }
    require(
        receipt_inventory(root) == set(proof["receipt_paths"]), "complete receipt inventory differs"
    )
    require(
        set(proof["receipt_paths"][:-1]) == old_receipts
        and len(proof["receipt_paths"]) == len(old_receipts) + 1,
        "expected exact old receipt prefix plus one suffix",
    )
    for name in (*proof["receipt_paths"][:-1], *HISTORICAL_CONTEXT):
        _historical_equal(tree, name, read(name))
    receipt = proof["receipts"][-1]
    sequence = len(proof["receipts"])
    require(
        type(plan["receipt_sequence"]) is int and plan["receipt_sequence"] == sequence,
        "receipt sequence differs",
    )
    require(
        update["mapping_receipt"]
        == {
            "path": proof["receipt_paths"][-1],
            "sha256": proof["receipt_inputs"][proof["receipt_paths"][-1]],
            "sequence": sequence,
        },
        "final receipt reference differs",
    )
    require(
        receipt["issue"] == ISSUE and receipt["scope"] == SCOPE and receipt["approval"] == APPROVAL,
        "receipt attribution differs",
    )
    require(
        receipt["before_sha256"] == plan["artifacts_before"][SSSOM_SOURCE]
        and receipt["after_sha256"] == plan["artifacts_after"][SSSOM_SOURCE],
        "receipt endpoints differ",
    )
    require(
        proof["states_after_sequence"][sequence - 1] == old_rows and proof["state"] == rows,
        "native before/after payload differs",
    )
    require(
        receipt["changed_rows"] == 23
        and receipt["added_rows"] == receipt["removed_rows"] == 0
        and receipt["position_map"] == list(range(1, len(rows) + 1)),
        "receipt exceeds exact 23-cell transition",
    )
    changes = [
        {
            "kind": "changed",
            "before_position": pos,
            "after_position": pos,
            "before": old_rows[pos - 1],
            "after": rows[pos - 1],
        }
        for pos in sorted(selected)
    ]
    require(receipt["changes"] == changes, "native change payload differs")
    expected_records = [expected_record(p, update["plan"]) for p in plan["pairs"]]
    require(
        sorted(receipt["records"], key=lambda r: r["source_record"])
        == sorted(expected_records, key=lambda r: r["source_record"]),
        "export-only owner records differ",
    )
    require(
        receipt["touched_subjects"] == sorted(p["before_row"]["subject_id"] for p in plan["pairs"]),
        "receipt touched subjects differ",
    )
    checkpoints = [
        r["sequence"]
        for r in proof["receipts"][:-1]
        if r["after_sha256"] == old_manifest["artifacts"][SSSOM_SOURCE]
    ]
    require(len(checkpoints) == 1, "historical manifest checkpoint is not unique/reachable")
    checkpoint = checkpoints[0]
    require(
        update["historical_checkpoint"]
        == {
            "sequence": checkpoint,
            "sssom_sha256": old_manifest["artifacts"][SSSOM_SOURCE],
            "bridge_sequences": list(range(checkpoint + 1, sequence)),
        },
        "historical checkpoint bridge differs",
    )
    base_old, base_new = (read_json(values[prior["base_review"]]) for values in (before, current))
    old_decisions = {d["source_position"]: d for d in base_old["decisions"]}
    new_decisions = {d["source_position"]: d for d in base_new["decisions"]}
    require(
        set(old_decisions) == set(new_decisions) == set(range(1, len(rows) + 1)),
        "base decision coverage differs",
    )
    require(
        all(
            old_decisions[p]["disposition"] == new_decisions[p]["disposition"]
            for p in old_decisions
        ),
        "scientific disposition changed",
    )
    require(
        all(
            old_decisions[p]["disposition"] == new_decisions[p]["disposition"] == "WITHHOLD"
            for p in selected
        ),
        "affected mapping is not withheld",
    )
    evidence_documents = {
        label: {
            name: read_json(values[name])
            for name in {d["review_evidence"] for d in decisions.values()}
        }
        for label, values, decisions in (
            ("before", before, old_decisions),
            ("current", current, new_decisions),
        )
    }
    for p in old_decisions.keys() - selected.keys():
        require(old_decisions[p] == new_decisions[p], "unrelated base decision changed")
        a, b = old_decisions[p], new_decisions[p]
        require(
            evidence_documents["before"][a["review_evidence"]]["entries"][a["evidence_key"]]
            == evidence_documents["current"][b["review_evidence"]]["entries"][b["evidence_key"]],
            "unrelated base evidence changed",
        )
    # The completed external log is attribution, not a result to trust for transition proof.
    read(update["publication_log"])
    require(source_inventory(root) == actual_inventory, "source inventory changed during proof")
    return {
        "baseline": context.baseline,
        "caller_pinned_manifest_sha256": context.manifest_sha256,
        "manifest_before_sha256": content_sha256(before[MANIFEST]),
        "appended_update": update,
        "native_receipt": proof["receipt_paths"][-1],
        "native_receipt_sha256": proof["receipt_inputs"][proof["receipt_paths"][-1]],
        "receipt_paths": proof["receipt_paths"],
        "source_paths": actual_inventory,
        "input_sha256": inputs,
        "scientific_approval_added": False,
        "attribution_contract": "Generation bytes and producer attribution are pinned; generation replay belongs to the guarded publisher.",
        "native_transition_contract": "Full native receipt payload replay, immutable durable prefix/source inventories, exact23 other cells, and unchanged dispositions verified.",
    }
