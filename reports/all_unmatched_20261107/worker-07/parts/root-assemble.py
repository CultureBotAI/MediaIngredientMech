"""2026-11-08 worker07 artifact assembly; no maintained-source writes.

Inputs: three author outcome bundles and exact frozen shard/baseline owners.
Outputs: combined campaign-contract JSON and compatible isolated owner payloads.
Conflicting edits fail instead of selecting an author's after bytes as baseline.
"""
import copy
import datetime
import hashlib
import json
from pathlib import Path

import yaml
from mediaingredientmech.validation.write_validated import write_validated_ingredient

ROOT = Path.cwd()
OUT = ROOT / "reports/all_unmatched_20261107/worker-07"
QUEUE = Path("/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/all-unmatched-20261107/queue/preliminary-v5")
SHARD = QUEUE / "shards/shard-07.json"


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read(path):
    return json.loads(path.read_text())


def union(values):
    result = []
    for value in values:
        if value not in result:
            result.append(value)
    return result


def combine_payloads(before, payloads):
    result = copy.deepcopy(before)
    # Synonyms preserve original positions/provenance; history preserves prefix.
    for field in union([key for value in payloads for key in value] + list(before)):
        old = before.get(field)
        changed = [value.get(field) for value in payloads if value.get(field) != old]
        if not changed:
            continue
        if field == "synonyms":
            base = old or []
            chosen = copy.deepcopy(base)
            edits = {}
            added = []
            for candidate in changed:
                assert isinstance(candidate, list) and len(candidate) >= len(base), "Synonym deletion requires explicit reconciliation"
                for index, original in enumerate(base):
                    proposed = candidate[index]
                    assert proposed.get("synonym_text") == original.get("synonym_text"), "Reordered/replaced source synonym"
                    if proposed != original:
                        assert index not in edits or edits[index] == proposed, "Conflicting synonym edits"
                        edits[index] = proposed
                added.extend(candidate[len(base):])
            for index, value in edits.items():
                chosen[index] = value
            for value in added:
                if value not in chosen:
                    chosen.append(value)
            result[field] = chosen
        elif field == "curation_history":
            base = old or []
            appended = []
            for candidate in changed:
                assert candidate[:len(base)] == base, "Historical event rewrite"
                appended.extend(candidate[len(base):])
            result[field] = base + sorted(union(appended), key=lambda event: event["timestamp"])
        else:
            assert all(value == changed[0] for value in changed), f"Conflicting field: {field}"
            if changed[0] is None and all(field not in value for value in payloads):
                result.pop(field, None)
            else:
                result[field] = changed[0]
    return result


def combine_hutner(proposals):
    """Explicit reviewed identity reconciliation, never a lexical generic-stock merge."""
    ids = ["A-PROPOSAL-JCM979_Hutner_Basal_Salts", "B-PROPOSAL-jcm_900_modified_hutner_basal_salts"]
    group = [next(p for p in proposals if p["proposal_id"] == pid) for pid in ids]
    payloads = [read_yaml(OUT / p["after_capture"]["path"]) for p in group]
    first, canonical = payloads
    assert all(p["kind"] == "new_owner" and p["before_sha256"] is None for p in group)
    assert len(first["components"]) == len(canonical["components"]) == 9
    assert first["components"][3]["component_name"] == canonical["components"][3]["component_name"] == "(NH4)6MoO24·4H2O"
    assert all(p["component_assertion"]["completeness"] == "COMPLETE" for p in payloads)
    after = copy.deepcopy(canonical)
    after["preferred_term"] = "Hutner basal salts (JCM 900 and JCM 979)"
    after["ontology_mapping"]["ontology_label"] = after["preferred_term"]
    after["ontology_mapping"]["evidence"] = union(canonical["ontology_mapping"]["evidence"] + first["ontology_mapping"]["evidence"])
    note = ("The primary JCM 900 and JCM 979 stock subrecipes specify the same nine named inputs, quantities, "
            "Metals 44 reference to JCM 149 and preparation: dissolve NTA, adjust to pH 7.0 with about 7.3 g KOH, "
            "add the remaining ingredients, and readjust to pH 6.8 with NaOH or H2SO4. Parent media and vitamin "
            "supplements differ outside this stock boundary. The literal malformed (NH4)6MoO24·4H2O remains "
            "unresolved; no heptamolybdate correction or exact chemical-component equivalence is asserted. "
            "Raw source names Hutner's basal salts (see below) and Modified Hutner's basal salts remain "
            "in the frozen case evidence; neither becomes a global stock synonym. The canonical proposed "
            "local registry identifier retains JCM 900 provenance and also covers this verified JCM 979 subrecipe.")
    after["notes"] = note
    after["components"][7].pop("concentration_value", None)
    after["components"][7].pop("concentration_unit", None)
    after["components"][7]["source"] = "About 7.3 g KOH to reach initial pH 7.0; approximate source-batch quantity, not an exact final concentration."
    after["component_assertion"]["evidence"] = union(canonical["component_assertion"]["evidence"] + first["component_assertion"]["evidence"])
    after["component_assertion"]["notes"] += " " + note
    event = {"timestamp": "2026-11-08T05:27:37Z", "curator": "all-unmatched-20261107-worker07-root",
             "action": "RECONCILE_ISOLATED_STOCK_PROPOSALS", "changes": note,
             "new_status": "MAPPED", "llm_assisted": True}
    after["curation_history"] = sorted(union(canonical["curation_history"] + first["curation_history"] + [event]), key=lambda e: e["timestamp"])
    capture = OUT / "proposed_owners/combined-JCM900-JCM979-Hutner.yaml"
    write_validated_ingredient(after, capture)
    proposal = copy.deepcopy(group[1])
    proposal.update({"proposal_id": "W07-COMBINED-JCM900-JCM979-Hutner",
                     "description": "One source-qualified nominal stock for the identical primary JCM 900 and JCM 979 Hutner subrecipes; distinct parent media excluded.",
                     "case_ids": union([c for p in group for c in p["case_ids"]]),
                     "evidence_ids": union([e for p in group for e in p["evidence_ids"]]),
                     "after_capture": {"root": "artifact", "path": str(capture.relative_to(OUT)), "sha256": sha(capture)},
                     "author_proposal_ids": ids, "original_author_payloads": [p["after_capture"] for p in group],
                     "integration_finding": "INTEGRATION-01 in captures/integration-review-initial.json",
                     "limitations": note})
    return [p for p in proposals if p["proposal_id"] not in ids] + [proposal], {pid: proposal["proposal_id"] for pid in ids}


def read_yaml(path):
    return yaml.safe_load(path.read_text())


def main():
    decisions, evidence, proposals = [], [], []
    author_hashes = {}
    for part in "abc":
        for kind, destination in [("decisions", decisions), ("evidence", evidence), ("proposals", proposals)]:
            path = OUT / f"parts/{part}-{kind}.json"
            destination.extend(read(path)[kind])
            author_hashes[str(path.relative_to(OUT))] = sha(path)
    root_proposals = OUT / "parts/root-nominal-stock-proposals.json"
    root_deltas = OUT / "parts/root-decision-deltas.json"
    proposals.extend(read(root_proposals)["proposals"])
    author_hashes[str(root_proposals.relative_to(OUT))] = sha(root_proposals)
    author_hashes[str(root_deltas.relative_to(OUT))] = sha(root_deltas)
    expected = [case["case_id"] for case in read(SHARD)["cases"]]
    assert len(decisions) == len(expected) == 188
    assert {row["case_id"] for row in decisions} == set(expected)
    by_case = {row["case_id"]: row for row in decisions}
    for delta in read(root_deltas)["deltas"]:
        decision = by_case[delta["case_id"]]
        digest = hashlib.sha256(json.dumps(decision, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()
        assert digest == delta["author_decision_sha256"], "Root decision delta applied to unexpected primary bytes"
        decision["reasoning"] += delta["reasoning_append"]
        decision["applicability"] += delta["applicability_append"]
        decision["proposal_ids"] = delta["proposal_ids"]
        decision["no_change_reason"] = delta["no_change_reason"]
        decision["missing_requirement"] = delta["missing_requirement"]
        decision["root_integration_delta"] = {"path": "parts/root-decision-deltas.json", "author_decision_sha256": digest, "review_requirement": delta["review_requirement"]}
    decisions = [by_case[key] for key in expected]
    for field, rows in [("evidence_id", evidence), ("proposal_id", proposals)]:
        assert len({row[field] for row in rows}) == len(rows), f"Duplicate {field}"
    by_proposal = {row["proposal_id"]: row for row in proposals}
    for decision in decisions:
        for pid in decision["proposal_ids"]:
            assert pid in by_proposal, f"Missing cross-part proposal {pid}"
            if decision["case_id"] not in by_proposal[pid]["case_ids"]:
                by_proposal[pid]["case_ids"].append(decision["case_id"])
    proposals, stock_substitutions = combine_hutner(proposals)
    groups = {}
    for proposal in proposals:
        groups.setdefault(proposal["owner_path"], []).append(proposal)
    merged, substitutions = [], dict(stock_substitutions)
    for owner, group in groups.items():
        path = ROOT / owner
        if group[0]["kind"] == "edit_existing_owner":
            assert all(p["before_sha256"] == sha(path) for p in group), f"Before hash mismatch {owner}"
        else:
            assert not path.exists(), f"New owner already exists {owner}"
        if len(group) == 1:
            merged.append(group[0])
            continue
        assert all(p["kind"] == "edit_existing_owner" for p in group), f"New owner collision {owner}"
        before = yaml.safe_load(path.read_text())
        payloads = []
        for p in group:
            capture = OUT / p["after_capture"]["path"]
            assert sha(capture) == p["after_capture"]["sha256"]
            payloads.append(yaml.safe_load(capture.read_text()))
        after = combine_payloads(before, payloads)
        pid = "W07-COMBINED-" + Path(owner).stem
        capture = OUT / "proposed_owners" / ("combined-" + Path(owner).name)
        write_validated_ingredient(after, capture)
        entry = {
            "proposal_id": pid, "kind": "edit_existing_owner", "owner_path": owner,
            "before_sha256": sha(path),
            "after_capture": {"root": "artifact", "path": str(capture.relative_to(OUT)), "sha256": sha(capture)},
            "case_ids": union([c for p in group for c in p["case_ids"]]),
            "evidence_ids": union([e for p in group for e in p["evidence_ids"]]),
            "description": "Compatible baseline-relative author proposals combined: " + " ".join(p["description"] for p in group),
            "author_proposal_ids": [p["proposal_id"] for p in group],
            "original_author_payloads": [p["after_capture"] for p in group],
            "identity_predicate_consequences": "Compatible synonym/history edits and source evidence additions only; identity, parent, mapping grade and chemical properties unchanged.",
            "publication_review_obligation": "No source edits applied. Withdraw inherited support for changed owner bytes; coordinator must reconcile cross-shard owners, use guarded writers, synchronize and generate native surfaces, and review the complete new published payload. Roles and unrelated source claims remain unapproved.",
        }
        assert all(before.get(k) == after.get(k) for k in set(before) | set(after) if k not in {"synonyms", "curation_history", "ontology_mapping"}), "Composite widened beyond alias/history/evidence scope"
        old_mapping, new_mapping = before.get("ontology_mapping", {}), after.get("ontology_mapping", {})
        assert all(old_mapping.get(k) == new_mapping.get(k) for k in set(old_mapping) | set(new_mapping) if k != "evidence"), "Composite changes identity/parent/grade"
        old_evidence, new_evidence = old_mapping.get("evidence", []), new_mapping.get("evidence", [])
        assert new_evidence[:len(old_evidence)] == old_evidence, "Composite rewrites existing mapping evidence"
        merged.append(entry)
        substitutions.update({p["proposal_id"]: pid for p in group})
    for decision in decisions:
        decision["proposal_ids"] = union([substitutions.get(pid, pid) for pid in decision["proposal_ids"]])
        decision["evidence_ids"] = union(decision["evidence_ids"])
        decision["issue_refs"] = union(decision["issue_refs"])
    final = {"decisions": {"schema_version": 1, "worker_slot": 7, "phase": "shard", "shard_sha256": sha(SHARD), "decisions": decisions},
             "evidence": {"schema_version": 1, "evidence": evidence},
             "proposals": {"schema_version": 1, "proposals": merged}}
    for kind, data in final.items():
        (OUT / f"{kind}.json").write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
    receipt = {"assembled_at": datetime.datetime.now(datetime.timezone.utc).isoformat(), "author_input_hashes": author_hashes,
               "decision_count": len(decisions), "evidence_count": len(evidence), "author_proposal_count": sum(len(read(OUT / f"parts/{part}-proposals.json")["proposals"]) for part in "abc") + len(read(root_proposals)["proposals"]),
               "combined_proposal_count": len(merged), "substitutions": substitutions,
               "maintained_sources_changed": False, "scientific_approval": False}
    (OUT / "logs/assembly-receipt.json").write_text(json.dumps(receipt, indent=2) + "\n")
    print(json.dumps(receipt, indent=2))


if __name__ == "__main__":
    main()
