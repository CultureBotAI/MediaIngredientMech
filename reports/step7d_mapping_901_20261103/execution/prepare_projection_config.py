"""Freeze an explicit Step7d proposal from an actual captured native candidate.

Creates new external proposal files only. No source, canonical, receipt or
approval is applied. Full source-log verification remains the promotion gate.
"""
from pathlib import Path
from collections import Counter
import argparse
import csv
import difflib
import hashlib
import importlib.util
import io
import json
import os
import sys

D = Path(__file__).resolve().parent
R = D.parent
W = R / "step7d"
sys.path[:0] = [str(W), str(W / "src")]
from mediaingredientmech import ingredient_bundle_refresh as refresh

OPERATOR_SHA = "9c26101166b25f88f7e0aed8a43c8040b912c2fdb76489cb1a0ffa0911d198e6"
SOURCE_SHA = "965f29ff2c35e789be007f2177a12b0c463c7a2ec4c5671b71433ef8038c99d0"
PLAN_SHA = "a82bc6d32e750f16fc7ecfa4c0a5e172a5930c849d7dc3ec5a6ca106ed60fca4"
SHAPES_SHA = "30d7250207a898695d19611c7a52db60f6533869a6a7e21d142988d670d9a301"
OPERATOR = D / "promote_step7d_mapping.py"
sha = lambda raw: hashlib.sha256(raw).hexdigest()
assert sha(OPERATOR.read_bytes()) == OPERATOR_SHA
spec = importlib.util.spec_from_file_location("step7d_projection_builder_operator", OPERATOR)
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)
enc = m.encoded
require = m.require


def triple(row):
    return {key: row[key] for key in ("subject_id", "object_id", "predicate_id")}


def basis(owner, item, source, prior):
    if prior is None:
        kind = ("New native Rule B1 local-compound identity handle for the asymmetric parent"
                if source["object_id"].startswith("kgmicrobe.compound:")
                else "New native exact CAS registry row from this owner's reviewed primary identifier")
    elif source["object_id"] != prior["object_id"]:
        if source["object_id"].startswith("NCIT:") and source["predicate_id"] == "skos:exactMatch":
            kind = "Existing ontology slot regrounded to the reviewed exact form-specific NCIt identity"
        elif source["object_id"].startswith("CHEBI:") and source["predicate_id"] == "skos:broadMatch":
            kind = ("Existing ontology slot corrected from " + prior["object_id"] + " to the reviewed nearest CHEBI parent "
                    + source["object_id"] + " with broadMatch under NARROW_MATCH; the supplied-form identity remains distinct")
        else:
            raise ValueError("Unreviewed changed ontology-object class: " + source["object_id"])
    elif source["predicate_id"] != prior["predicate_id"]:
        kind = "Existing nearest-parent row changed from closeMatch to broadMatch under reviewed NARROW_MATCH"
    else:
        kind = "Existing exact registry identity retained with current native provenance, date and CAS/alias payload"
    paths = ["/" + "/".join(map(str, operation["path"])) for operation in item["operations"]]
    return (kind + ". Owner " + owner + "; source group " + item["group"]
            + "; before SHA256 " + item["before_sha256"] + "; after SHA256 " + item["after_sha256"]
            + "; exact reviewed operation paths " + json.dumps(paths, ensure_ascii=False)
            + ". Native scientific cells are unchanged by projection. Historical source/comment provenance is carried;"
            + " validation stamps survive only identical object/predicate. Existing deferred23 tokens are restored"
            + " only on their original row. No new approval. " + item["verification"])


def construct(before, candidate, plan, shapes, manifest_sha):
    """Pure assembly checked by the frozen promotion projection implementation."""
    require(sha(before) == m.BEFORE_SHA, "wrong canonical baseline")
    names = m.owner_names(plan)
    require(len(names) == 38 and shapes["owner_count"] == 38, "wrong reviewed owner count")
    by_subject = {"MIM:" + Path(name).stem: name for name in names}
    shape_by_owner = {item["owner_path"]: item for item in shapes["owners"]}
    require(set(shape_by_owner) == set(names), "shape owner membership differs")
    header, fields, old = m.table(before)
    _, candidate_fields, generated = m.table(candidate)
    require(fields == candidate_fields, "candidate fields differ")
    selected = [(i, row) for i, (row, _) in enumerate(generated, 1) if row["subject_id"] in by_subject]
    old_selected = [(i, row) for i, (row, _) in enumerate(old, 1) if row["subject_id"] in by_subject]
    require(len(selected) == 105 and len(old_selected) == 76, "candidate/baseline selected row count differs")
    by_old = {m.slot(row): (i, row) for i, row in old_selected}
    by_new = {m.slot(row): (i, row) for i, row in selected}
    require(len(by_old) == len(old_selected) and len(by_new) == len(selected), "duplicate selected slot")
    for subject, owner in by_subject.items():
        shape = shape_by_owner[owner]
        require(shape["before_sha256"] == plan["owners"][owner]["before_sha256"]
                and shape["after_sha256"] == plan["owners"][owner]["after_sha256"], "shape owner hashes differ")
        actual_old = [{"position": i, "slot": m.slot(row)[1], **triple(row)}
                      for i, row in old_selected if row["subject_id"] == subject]
        actual_new = {m.slot(row)[1]: triple(row) for _, row in selected if row["subject_id"] == subject}
        expected_new = {row["slot"]: triple(row) for row in shape["after"]}
        require(actual_old == shape["before"] and actual_new == expected_new,
                "native candidate scientific slots differ from reviewed preview prediction: " + owner)
    deferred_raw = m.regular(W / "mappings/other_cross_record_baseline.tsv")
    require(sha(deferred_raw) == plan["protected_sha256"]["mappings/other_cross_record_baseline.tsv"],
            "deferred baseline differs from frozen plan")
    deferred = m.deferred_pairs(deferred_raw)
    items, removals, output, insertions = [], [], {}, {}
    for position, source in selected:
        owner = by_subject[source["subject_id"]]
        item = plan["owners"][owner]
        prior_item = by_old.get(m.slot(source))
        prior = prior_item[1] if prior_item else None
        after = m.output_from_candidate(source, prior, deferred)
        insertion = None if prior_item else max(i for i, row in old_selected if row["subject_id"] == source["subject_id"])
        declared = {"candidate_position": position, "candidate": source, "output": after,
                    "before_position": prior_item[0] if prior_item else None,
                    "insert_after_position": insertion, "output_position": None,
                    "basis": basis(owner, item, source, prior)}
        items.append(declared)
        output[m.slot(source)] = after
        if insertion is not None:
            insertions.setdefault(insertion, []).append(after)
    for key in sorted(set(by_old) - set(by_new)):
        position, row = by_old[key]
        owner = by_subject[row["subject_id"]]
        item = plan["owners"][owner]
        removals.append({"before_position": position, "before": row,
                         "basis": "The exact form-specific NCIt primary supersedes this owner's previous CAS-only fallback; "
                         "the pinned native generator emits one exact ontology identity and no separate registry row. "
                         "Owner " + owner + "; group " + item["group"] + "; reviewed plan " + PLAN_SHA
                         + ". Removed row and historical comment remain preserved in native receipt25/preimage; "
                         "no provenance is reassigned to another row. " + item["verification"]})
    require(len(removals) == 2 and all(m.slot(item["before"])[1] == "cas" for item in removals),
            "unexpected removed row class")
    require(Counter(m.slot(item["output"])[1] for item in items if item["before_position"] is None)
            == {"kgmicrobe.compound": 29, "cas": 2}, "unexpected new row classes")
    render = lambda row: "\t".join(row[field] for field in fields) + "\n"
    body = []
    for position, (row, raw) in enumerate(old, 1):
        if row["subject_id"] not in by_subject:
            body.append(raw)
        elif m.slot(row) in output:
            body.append(render(output[m.slot(row)]))
        body.extend(render(row) for row in insertions.get(position, []))
    lines = ("".join(header) + "".join(body)).splitlines(keepends=True)
    date = m.newest_row_date(lines)
    require(date is not None, "missing mapping date")
    after = "".join(m.rewrite(lines, date)[0]).encode()
    _, _, final_rows = m.table(after)
    final_positions = {m.slot(row): i for i, (row, _) in enumerate(final_rows, 1) if row["subject_id"] in by_subject}
    for item in items:
        item["output_position"] = final_positions[m.slot(item["output"])]
    config = {"schema_version": 2, "base_revision": m.BASE, "producer_revision": m.PRODUCER,
              "candidate_sha256": sha(candidate), "generation_manifest_sha256": manifest_sha,
              "canonical_after_sha256": sha(after), "owner_plan_sha256": PLAN_SHA,
              "source_operator_sha256": SOURCE_SHA, "scientific_approval_added": False,
              "supervisor_binding": None, "rows": items, "removed": removals}
    require(m.projection(before, candidate, config, plan, deferred) == after, "frozen projection replay differs")
    return config, after


def prepare(bundle, producer, out):
    bundle, producer, out = map(m.checked, (bundle, producer, out))
    require(bundle.is_relative_to(W / "output") and producer == R / "step7c-claw", "unreviewed bundle/producer path")
    require(out.is_relative_to(D) and out != D and not os.path.lexists(out) and out.parent.is_dir(),
            "new external output directory under D required")
    bound = {}
    for path in (Path(__file__).resolve(), OPERATOR, D / "apply_reviewed_owners.py", D / "owner-plan.json",
                 D / "expected-projection-shapes.json", W / m.SSSOM, W / "mappings/other_cross_record_baseline.tsv",
                 Path(refresh.__file__).resolve()):
        m.bind(bound, {path: m.regular(path)})
    require(sha(bound[OPERATOR]) == OPERATOR_SHA and sha(bound[D / "apply_reviewed_owners.py"]) == SOURCE_SHA
            and sha(bound[D / "owner-plan.json"]) == PLAN_SHA
            and sha(bound[D / "expected-projection-shapes.json"]) == SHAPES_SHA, "frozen builder input changed")
    plan = json.loads(bound[D / "owner-plan.json"])
    shapes = json.loads(bound[D / "expected-projection-shapes.json"])
    base = m.baseline(W)
    inventory = m.policy.ingredient_paths(W)
    require({str(path.relative_to(W)) for path in inventory} == set(plan["all_owner_sha256"]), "owner inventory differs")
    for path in inventory:
        name = str(path.relative_to(W))
        raw = m.regular(path)
        expected = plan["owners"][name]["after_sha256"] if name in plan["owners"] else plan["all_owner_sha256"][name]
        require(sha(raw) == expected, "current owner not at reviewed endpoint: " + name)
        m.bind(bound, {path: raw})
    for name, stages in plan["auxiliary"].items():
        raw = m.regular(W / name)
        require(sha(raw) == stages[-1]["after_sha256"], "auxiliary endpoint differs")
        m.bind(bound, {W / name: raw})
    for name in ("MAPPING_SEMANTICS.md", "src/mediaingredientmech/schema/mediaingredientmech.yaml"):
        raw = m.regular(W / name)
        require(sha(raw) == plan["protected_sha256"][name], "semantic/schema input differs")
        m.bind(bound, {W / name: raw})
    manifest_path = bundle / "candidate.sssom.tsv.manifest.json"
    manifest_sha = sha(m.regular(manifest_path))
    absent, label_paths, producer_paths, replay = m.generation_inputs(W, bundle, producer, bound, manifest_sha)
    manifest = json.loads(bound[manifest_path])
    checkpoint = manifest["source_revisions"]["mim"]
    require(m.native.git(W, "rev-parse", "HEAD").decode().strip() == checkpoint
            and not m.native.git(W, "status", "--porcelain", "--untracked-files=all"),
            "current MIM is not the clean native generation checkpoint")
    for path, loaded in m._EXECUTED.items():
        require(m.regular(path) == loaded, "promotion module changed")
        if path.is_relative_to(W):
            require(loaded == base[str(path.relative_to(W))], "native module differs from base")
        m.bind(bound, {path: loaded})
    require(bound[Path(refresh.__file__).resolve()] == m.native.git(W, "show", m.BASE + ":src/mediaingredientmech/ingredient_bundle_refresh.py"),
            "exclusive publisher differs from base")
    before, candidate = bound[W / m.SSSOM], bound[bundle / "candidate.sssom.tsv"]
    config, after = construct(before, candidate, plan, shapes, manifest_sha)
    maker_path = W / m.MAKER
    maker_raw = m.regular(maker_path)
    require(maker_raw == base[str(m.MAKER)], "native alignment maker differs from base")
    m.bind(bound, {maker_path: maker_raw})
    spec = importlib.util.spec_from_file_location("step7d_projection_native_alignment", maker_path)
    maker = importlib.util.module_from_spec(spec)
    exec(compile(maker_raw, str(maker_path), "exec"), maker.__dict__)
    changes, position_map = maker.align(maker.rows_of(before), maker.rows_of(after))
    fields = m.table(before)[1]
    for change in changes:
        change["changed_cells"] = ({field: {"before": change["before"].get(field), "after": change["after"].get(field)}
                                     for field in fields if change["before"].get(field) != change["after"].get(field)}
                                    if change["kind"] == "changed" else None)
    require(Counter(c["kind"] for c in changes)["added"] == 31
            and Counter(c["kind"] for c in changes)["removed"] == 2, "native alignment row classes differ")
    config_raw = enc(config)
    scope = {"state": "FROZEN_PROPOSAL_NOT_APPLIED", "scientific_approval_added": False, "supervisor_binding": None,
             "base_revision": m.BASE, "generation_checkpoint": checkpoint, "producer_revision": m.PRODUCER,
             "generation_bundle": str(bundle), "native_offline_replay": replay,
             "owner_count": 38, "selected_rows_before": 76, "selected_rows_after": 105,
             "changed_row_counts": dict(Counter(c["kind"] for c in changes)),
             "changed_existing_cells": sum(len(c["changed_cells"]) for c in changes if c["changed_cells"] is not None),
             "before_sha256": sha(before), "after_sha256": sha(after), "config_sha256": sha(config_raw),
             "projection_operator_sha256": OPERATOR_SHA, "source_operator_sha256": SOURCE_SHA,
             "owner_plan_sha256": PLAN_SHA, "expected_shapes_sha256": SHAPES_SHA,
             "unrelated_raw_rows_identical_and_in_order": True, "deferred23_occurrences_preserved": True,
             "source_log_replay_and_guarded_promotion_dry_run": "Still required; not claimed by config construction",
             "input_sha256": {str(path): sha(raw) for path, raw in bound.items()}}
    cells = [{"subject_id": c["after"]["subject_id"], "object_id": c["after"]["object_id"],
              "column": field, **values} for c in changes if c["changed_cells"] is not None
             for field, values in c["changed_cells"].items()]
    stream = io.StringIO(newline="")
    writer = csv.DictWriter(stream, fieldnames=["subject_id", "object_id", "column", "before", "after"], delimiter="\t")
    writer.writeheader()
    writer.writerows(cells)
    outputs = {out / "projection-config.json": config_raw, out / "canonical-proposal.sssom.tsv": after,
               out / "row-diff.json": enc({"approval": "NONE: explanatory projection, not receipt25", "changes": changes, "position_map": position_map}),
               out / "cell-diff.tsv": stream.getvalue().encode(), out / "scope-receipt.json": enc(scope),
               out / "canonical-proposal.diff": "".join(difflib.unified_diff(before.decode().splitlines(keepends=True),
                   after.decode().splitlines(keepends=True), fromfile="canonical-before", tofile="canonical-proposal")).encode()}

    def recheck():
        require(all(m.regular(path) == raw for path, raw in bound.items()), "proposal input changed")
        require(m.policy.ingredient_paths(W) == inventory and m.native.producer_paths(producer) == producer_paths,
                "owner/producer membership changed")
        require(set(bundle.glob("label-input-*.json")) == label_paths and all(not os.path.lexists(path) for path in absent),
                "captured label or absent input membership changed")
        require(m.native.git(W, "rev-parse", "HEAD").decode().strip() == checkpoint
                and not m.native.git(W, "status", "--porcelain", "--untracked-files=all"), "MIM generation checkpoint changed")

    recheck()
    out.mkdir(mode=0o700)
    refresh.publish_new_files(list(outputs.items()), recheck)
    require(all(m.regular(path) == raw for path, raw in outputs.items()), "external proposal output differs")
    return {"state": scope["state"], "config_sha256": sha(config_raw), "canonical_after_sha256": sha(after),
            "row_change_counts": scope["changed_row_counts"], "changed_existing_cells": scope["changed_existing_cells"],
            "outputs": {str(path): sha(raw) for path, raw in outputs.items()}}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--bundle", type=Path, required=True)
    parser.add_argument("--producer", type=Path, default=R / "step7c-claw")
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    print(json.dumps(prepare(args.bundle, args.producer, args.out), indent=2))


if __name__ == "__main__":
    main()
