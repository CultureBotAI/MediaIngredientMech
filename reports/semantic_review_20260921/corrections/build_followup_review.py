"""Bind the identity-correction review to every current record and graph member.

Historical approvals are inherited only for byte-identical records. This batch
reviews chemical identity; it does not certify every remaining biological role.
"""

import csv
import hashlib
import json
from collections import Counter
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
BASE = HERE.parent
BUNDLE = ROOT / "output/mim-kgx-20260921-identity-corrections"


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read_rows(path, kgx=False):
    with path.open() as f:
        return list(
            csv.DictReader(f, delimiter="\t", quoting=csv.QUOTE_NONE if kgx else csv.QUOTE_MINIMAL)
        )


def main():
    plan = json.loads((HERE / "identity-plan.json").read_text())["records"]
    baseline = {r["source_record"]: r for r in read_rows(BASE / "records.tsv")}
    changes = {r["destination_path"]: r for r in plan}
    old_changes = {r["source_path"]: r for r in plan}
    current = {}
    review = []
    for group in ("mapped", "unmapped"):
        for path in sorted((ROOT / "data/ingredients" / group).glob("*.yaml")):
            name = str(path.relative_to(ROOT))
            rec = yaml.load(path.read_text(), Loader=yaml.CSafeLoader)
            current[name] = rec
            if name in changes:
                item = changes[name]
                assert rec == item["after_record"], f"Unreviewed change: {name}"
                if item["before_record"] is not None:
                    assert item["before_sha256"] == baseline[item["source_path"]]["record_sha256"]
                status = {
                    "REJECTED": "merged_and_excluded",
                    "AMBIGUOUS": "unsupported_identity_withdrawn_source_resolution_pending",
                }.get(rec["mapping_status"], "identity_reviewed_other_findings_not_cleared")
                basis = "identity-plan.json"
            else:
                assert (
                    sha(path) == baseline[name]["record_sha256"]
                ), f"Historical approval is stale: {name}"
                status = baseline[name]["verdict"]
                basis = "../records.tsv (byte-identical source)"
            review.append(
                dict(
                    source_record=name,
                    record_sha256=sha(path),
                    identifier=rec["identifier"],
                    preferred_term=rec["preferred_term"],
                    mapping_status=rec["mapping_status"],
                    disposition=status,
                    basis=basis,
                )
            )
    assert set(baseline) - set(current) == {
        i["source_path"] for i in plan if i["source_path"] != i["destination_path"]
    }
    # Explicitly adjudicate just the fourteen blocker findings.
    blockers = [
        f
        for f in read_rows(BASE / "findings.tsv")
        if f["record_scope"] == "active" and f["severity"] == "blocker"
    ]
    assert len(blockers) == 14
    dispositions = []
    for finding in blockers:
        item = old_changes[finding["source_record"]]
        rec = item["after_record"]
        dispositions.append(
            dict(
                finding_id=finding["finding_id"],
                source_record=finding["source_record"],
                current_record=item["destination_path"],
                disposition=(
                    "WITHDRAWN_PENDING_SOURCE"
                    if rec["mapping_status"] == "AMBIGUOUS"
                    else "IDENTITY_CORRECTED"
                ),
                current_identifier=rec.get("representative", rec["identifier"]),
                reason=item["reason"],
                evidence=" ; ".join(item["evidence"]),
            )
        )
    for filename, rows in [
        ("current_records.tsv", review),
        ("blocker_dispositions.tsv", dispositions),
    ]:
        with (HERE / filename).open("w") as f:
            w = csv.DictWriter(f, fieldnames=rows[0], delimiter="\t", lineterminator="\n")
            w.writeheader()
            w.writerows(rows)
    manifest = json.loads((BUNDLE / "manifest.json").read_text())
    nodes = read_rows(BUNDLE / "mim_nodes.tsv", True)
    edges = read_rows(BUNDLE / "mim_edges.tsv", True)
    assert {n["source_record"] for n in nodes if n["node_kind"] == "ingredient"} == {
        p for p, r in current.items() if r["mapping_status"] != "REJECTED"
    }
    provisional = empty = cellular_without_context = 0
    for e in edges:
        if e["assertion_type"] not in {
            "nutritional_roles",
            "physicochemical_roles",
            "cellular_metabolic_roles",
            "community_organism_roles",
        }:
            continue
        assertion = json.loads(e["assertion_json"])
        ev = assertion.get("evidence") or []
        empty += not ev
        provisional += bool(ev) and all(
            x.get("reference_type") == "COMPUTATIONAL_PREDICTION" for x in ev
        )
        cellular_without_context += e[
            "assertion_type"
        ] == "cellular_metabolic_roles" and not assertion.get("metabolic_context")
    member_hashes = {
        str(p.relative_to(ROOT)): sha(p)
        for p in [
            HERE / "identity-plan.json",
            HERE / "current_records.tsv",
            HERE / "blocker_dispositions.tsv",
            BASE / "manifest.json",
            BASE / "findings.tsv",
            ROOT / "mappings/ingredient_mappings.sssom.tsv",
            ROOT / "UNIFIED_INGREDIENT_MAPPING.tsv",
            ROOT / "UNIFIED_INGREDIENT_MAPPING.provenance.json",
            ROOT / "mappings/unified_mapping_rejections.tsv",
            ROOT / "mappings/culturemech_recipe_membership.tsv",
            HERE / "sssom-validation.json",
            HERE / "counts-and-label-check.json",
            HERE / "membership-refresh.json",
            HERE / "unified-build.json",
            HERE / "downstream-remaining-identifiers.json",
            HERE / "validate_followup_review.py",
            Path(__file__),
            BUNDLE / "projection-review.json",
            BUNDLE / "native-kgx-reader.json",
            BUNDLE / "reproducibility.json",
            BUNDLE / "manifest.json",
            BUNDLE / "mim_nodes.tsv",
            BUNDLE / "mim_edges.tsv",
            BUNDLE / "mim-kgx.tar.gz",
        ]
    }
    report = dict(
        release_verdict="FAIL",
        reason="Identity correction batch completed; unresolved source identities and existing role/component evidence findings remain. Historical record reviews are not fresh approval of changed records.",
        record_count=len(current),
        statuses=dict(Counter(r["mapping_status"] for r in current.values())),
        changed_or_added_records=len(plan),
        blocker_dispositions=dict(Counter(r["disposition"] for r in dispositions)),
        graph_counts=manifest["counts"],
        role_evidence=dict(
            prediction_only=provisional,
            empty=empty,
            cellular_without_context=cellular_without_context,
        ),
        inputs=member_hashes,
        record_inputs={r["source_record"]: r["record_sha256"] for r in review},
        all_records_accounted_for=True,
        archive_sha256=sha(BUNDLE / "mim-kgx.tar.gz"),
    )
    (HERE / "current-review.json").write_text(json.dumps(report, indent=2) + "\n")
    (BUNDLE / "semantic-review.json").write_text(
        json.dumps(
            {
                "release_verdict": "FAIL",
                "review": "reports/semantic_review_20260921/corrections/current-review.json",
                "review_sha256": sha(HERE / "current-review.json"),
                "archive_sha256": sha(BUNDLE / "mim-kgx.tar.gz"),
            },
            indent=2,
        )
        + "\n"
    )
    print(
        json.dumps(
            {
                k: v
                for k, v in report.items()
                if k not in {"inputs", "record_inputs", "graph_counts"}
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
