"""Independent four-successor technical review; reads candidates, writes one receipt."""
import copy
import hashlib
import importlib.util
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

import yaml

W = Path.cwd().resolve()
C = W.parents[2]
D = W / "reports/all_unmatched_20261107/worker-01/successor-1226-1237-v1"
sys.path.insert(0, str(W / "src"))
from mediaingredientmech.curate.publication_guard import FrozenFile
from mediaingredientmech.synonym_policy import is_resolving_synonym, preferred_term_owners
from mediaingredientmech.validation.component_partonomy import validate_component_partonomy
from mediaingredientmech.validation.write_validated import validate_ingredient

EXPECTED = {
    "NSV4-PROP-NBRC_1020_Se_W_Solution": "d6a2c6de6bb04cc2c7ea3fc2c97dc1a0227151caa331af1baed4875dfbe8651f",
    "NSV4-PROP-JCM_317_Se_W_Solution": "7d2da1da0d6d56cd8db3bdffbda87c94fdc2457caa693f9506684472bf0f22e2",
    "CS-PROP-JCM1430_FERROUS_SULFATE_HCL_STOCK": "9ce46ee43a275add8f13d2fcabe353f15829654b6f623cdf4fae26dcf717517a",
    "CS-PROP-NBRC1321_CO2_BICARBONATE_STOCK": "f7aca68cf65299a813290c8831a568126f3f18eb4ecf50dec60c8f178246a61a",
}


def sha(b):
    return hashlib.sha256(b).hexdigest()


def bind(p):
    return {"path": str(p), "sha256": sha(Path(p).read_bytes())}


def diffs(a, b, path=""):
    if type(a) is not type(b):
        return [{"path": path, "before": a, "after": b}]
    if isinstance(a, dict):
        assert a.keys() == b.keys(), (path, "Unexpected key addition/deletion")
        return [d for k in a for d in diffs(a[k], b[k], path + "/" + k)]
    if isinstance(a, list):
        assert len(a) == len(b), (path, "Unexpected list length change")
        return [d for i, (x, y) in enumerate(zip(a, b)) for d in diffs(x, y, path + "/" + str(i))]
    return [] if a == b else [{"path": path, "before": a, "after": b}]


def main():
    allow = json.loads((D / "inputs/w01-full-provenance-allowlist-v2.json").read_text())
    rows = [r for r in allow["rows"] if r["also_science_scope"]]
    assert len(rows) == 5 and {r["proposal_id"] for r in rows} == set(EXPECTED)
    author = json.loads((D / "science/author-payload-receipt-v1.json").read_text())
    lineage = {r["proposal_id"]: r for r in json.loads((D / "science/qualifier-negative-audit-lineage-v1.json").read_text())["records"]}
    capture_receipt = json.loads((D / "science/input-bindings-and-owned-name-check-v1.json").read_text())
    primary = []
    seen = set()
    for r in capture_receipt["primary_receipts_original_access_times"]:
        p = Path(r["frozen_absolute_path"])
        assert sha(p.read_bytes()) == r["capture"]["sha256"]
        if r["capture"]["sha256"] not in seen:
            seen.add(r["capture"]["sha256"])
            primary.append({"capture": bind(p), "url": r["url"], "original_accessed_at": r["accessed_at"], "read_scope": "Complete original HTML body read for the eight relevant source recipes; not a fresh retrieval."})
    holds, checks, parsed, pins = [], [], {}, []
    for pid, expected in EXPECTED.items():
        rs = [r for r in rows if r["proposal_id"] == pid]
        r = rs[0]
        pf = FrozenFile.capture(Path(r["current_payload_path"]))
        af = FrozenFile.capture(D / "payloads" / (pid + ".yaml"))
        pins += [pf, af]
        assert sha(pf.content) == r["payload_sha256"] and sha(af.content) == expected
        before, after = yaml.safe_load(pf.content), yaml.safe_load(af.content)
        assert before == r["origin"]["record"]
        assert r["proposal_kind"] == "new_owner" and r["baseline_path"] is None
        assert not validate_ingredient(after)
        oldh = before["curation_history"]
        assert after["curation_history"][:-1] == oldh
        assert len(after["curation_history"]) == len(oldh) + 1
        event = after["curation_history"][-1]
        assert event["curator"] == "Codex /root/primary_context (worker01)" and event["llm_assisted"] is True
        assert "#1226" in event["changes"] and "#1237" in event["changes"]
        assert lineage[pid]["original_synonyms"] == before["synonyms"]
        assert lineage[pid]["original_curation_history"] == oldh
        assert lineage[pid]["successor_synonyms"] == after["synonyms"]
        reverted = copy.deepcopy(after)
        reverted["curation_history"] = copy.deepcopy(oldh)
        type_changes = []
        for row in rs:
            i = int(re.fullmatch(r"ontology_mapping\.evidence\[(\d+)\]", row["field"]).group(1))
            assert before["ontology_mapping"]["evidence"][i] == row["full_value"]
            assert after["ontology_mapping"]["evidence"][i] == {**row["full_value"], "evidence_type": "LLM_SUGGESTION"}
            reverted["ontology_mapping"]["evidence"][i]["evidence_type"] = "MANUAL_CURATION"
            type_changes.append({"audit_row_id": row["audit_row_id"], "field": row["field"], "source_and_notes_unchanged": True})
        changes = diffs(before, reverted)
        common = {"/notes"}
        if "Se_W" in pid:
            allowed = common | {"/component_assertion/notes", "/component_assertion/evidence/0/notes"}
        elif "FERROUS" in pid:
            allowed = common | {"/synonyms/0/synonym_type", "/synonyms/0/source"}
        else:
            allowed = common
        assert {x["path"] for x in changes} == allowed
        for key in ["identifier", "preferred_term", "mapping_status", "components", "ingredient_type", "solution_type"]:
            assert before[key] == after[key]
        assert {k: v for k, v in before["ontology_mapping"].items() if k != "evidence"} == {k: v for k, v in after["ontology_mapping"].items() if k != "evidence"}
        parsed[pid] = (before, after)
        checks.append({"proposal_id": pid, "predecessor": bind(pf.path), "successor": bind(af.path), "authentic_owner_before": None, "source_kind": "new_owner proposal; no maintained beforeimage is invented", "native_closed_schema": "pass", "exact_old_history_prefix": True, "one_new_event": event, "all_components_and_quantities_equal": True, "identifier_and_mapping_identity_equal": True, "mapping_evidence_changes": type_changes, "complete_scientific_leaf_deltas": changes, "original_case_bindings": r["origin"]["case_bindings"], "negative_lineage": {"exact_original_synonyms_preserved": True, "exact_original_history_preserved": True}})
    # Only native reference closure for these four, rather than a repeated whole-cohort test.
    mapped, maintained, inventory = {}, {}, []
    for p in sorted((W / "data/ingredients").rglob("*.yaml")):
        record = yaml.safe_load(p.read_bytes())
        maintained[str(p)] = record
        inventory.append(bind(p))
        if p.parent.name == "mapped":
            mapped[p.stem] = record
    needed = {c["component_id"] for _, a in parsed.values() for c in a.get("components", []) if c.get("reference_scope") == "MIM_CATALOG"}
    owners = [(p, r) for p, r in maintained.items() if r.get("identifier") in needed]
    errors = validate_component_partonomy([a for _, a in parsed.values()] + [r for _, r in owners])
    assert not errors, [str(e) for e in errors]
    tokens = ["0.01 M FeSO4·7H2O solution (in 0.02 N HCl)", "Bicarbonate solution (1.0 M)***", "Bicarbonate solution***"]
    owner_index = preferred_term_owners(mapped)
    owner_hits = {t: sorted(owner_index.get(t.casefold().strip(), [])) for t in tokens}
    assert all(not x for x in owner_hits.values())
    proposal_inventory = []
    props = json.loads((W / "reports/all_unmatched_20261107/worker-01/shard/proposals.json").read_text())["proposals"]
    for p in props:
        path = W / "reports/all_unmatched_20261107/worker-01" / p["after_capture"]["path"]
        record = yaml.safe_load(path.read_bytes())
        assert sha(path.read_bytes()) == p["after_capture"]["sha256"]
        proposal_inventory.append({"proposal_id": p["proposal_id"], "capture": bind(path), "preferred_term": record["preferred_term"]})
    assert all(r["preferred_term"].strip().casefold() not in {t.casefold() for t in tokens} for r in proposal_inventory)
    producer = C.parent / "kgm-unmapped-20261107/claw/scripts/build_mim_ingredient_sssom.py"
    spec = importlib.util.spec_from_file_location("science4_native_sssom", producer)
    module = importlib.util.module_from_spec(spec); sys.modules[spec.name] = module; spec.loader.exec_module(module)
    projections = []
    for pid, (before, after) in parsed.items():
        rb = module._row_from_yaml(Path(pid + ".yaml"), {}, {}, {}, {}, record=before, owners={})
        ra = module._row_from_yaml(Path(pid + ".yaml"), {}, {}, {}, {}, record=after, owners={})
        flags = [{"text": s["synonym_text"], "before": is_resolving_synonym(before["synonyms"][i]), "after": is_resolving_synonym(s)} for i, s in enumerate(after["synonyms"])]
        assert all(f["after"] == ("FERROUS" in pid) for f in flags)
        if "FERROUS" in pid:
            assert tokens[0] in {t for row in ra for t in row.get("other", "").split("|")}
        if "BICARBONATE" in pid:
            assert not set(tokens[1:]).intersection({t for row in ra for t in row.get("other", "").split("|")})
        assert [(r["subject_id"], r["predicate_id"], r["object_id"]) for r in rb] == [(r["subject_id"], r["predicate_id"], r["object_id"]) for r in ra]
        projections.append({"proposal_id": pid, "resolver_behavior": flags, "before_rows": rb, "after_rows": ra})
    for f in pins:
        f.verify()
    report = {
        "reviewed_at": datetime.now(timezone.utc).isoformat(),
        "reviewer": "Codex /root/issue_context (worker01)",
        "independence": "Did not author or edit these four successor payloads or their science dispositions. Authored the disjoint 62 typing-only successors; no independent claim is made for that lane. This same persistent session authored some historical CS predecessors, so this review is independent of the current four-candidate author, not an assertion of independence from all historical formulation work. Root and skeptical reviews remain separately required.",
        "verdict": "pass_with_limitations",
        "scope": "Exactly four complete primary_context successors at the declared hashes: technical schema, complete semantic deltas, five evidence objects, old history/negative lineage, identity, components, scoped resolver/native SSSOM and reference closure. Bounded primary reassessment supports the authorized #1237 correction only; not a new whole-owner or release approval.",
        "findings": [],
        "assignment": bind(D / "inputs/w01-author-task-DRAFT-v2.md"),
        "allowlist": bind(D / "inputs/w01-full-provenance-allowlist-v2.json"),
        "author_receipt": bind(D / "science/author-payload-receipt-v1.json"),
        "negative_lineage_receipt": bind(D / "science/qualifier-negative-audit-lineage-v1.json"),
        "author_input_receipt": bind(D / "science/input-bindings-and-owned-name-check-v1.json"),
        "program": bind(__file__),
        "candidate_checks": checks,
        "primary_source_captures": primary,
        "source_assessments": [
            {"finding": "CHEM-COMP-002", "targets": list(EXPECTED)[:2], "assessment": "NBRC1020 prints Na2SeO3 4 mg and Na2WO4 4 mg plus 1 L distilled water; neither omitted hydrate qualifier establishes anhydrous reagent. JCM317 positively prints Na2WO4·2H2O at 4 mg with 4 mg Na2SeO3 and 1 L water. Both unchanged literal component tables preserve these facts. New notes withdraw unsupported difference/equality, preserve source-bound partial proposals and explicitly withhold merge/co-installation as proved-distinct owners. No arbitrary winning identifier or new component assignment.", "limits": "NBRC824 lists the two 4 mg salt entries but no stock water/denominator; its occurrence remains excluded from the quantified NBRC1020 proposal. JCM1425 explicitly points to JCM317. Unchanged comparisons to other recipes are inherited scope, not newly reapproved here."},
            {"finding": "CHEM-COMP-006", "targets": ["CS-PROP-JCM1430_FERROUS_SULFATE_HCL_STOCK"], "assessment": "JCM1430 and JCM1431 both print the exact complete 0.01 M FeSO4·7H2O solution (in 0.02 N HCl) name. The fully qualified label identifies the stated operational stock, and the 3.0 mL is the receiving dose. Its sole EXACT_SYNONYM reclassification is claim-specific and supported; exact predecessor rejection/source/history remain in the immutable lineage. Components, normality, hydrate and stock identity are unchanged. Native resolver and in-memory SSSOM now expose this exact token only; no shortened-name equivalence or N-to-M conversion is added."},
            {"finding": "CHEM-COMP-006", "targets": ["CS-PROP-NBRC1321_CO2_BICARBONATE_STOCK"], "assessment": "Both exact bicarbonate strings are receiving-table footnote pointers. The new per-string rationale distinguishes their standalone scope from the footnote-defined NaHCO3/CO2 preparation, while preserving their actual sourced REJECTED_LABEL objects and positive occurrence assignments. Both full NBRC footnotes support the same 8.4 g NaHCO3 plus 100 mL distilled-water preparation, CO2 saturation and sealed autoclaving. The union and literal components remain unchanged; no final-volume or amount-of-dissolved-CO2 assertion is added. CO2 is a material input here because saturation is explicit, separately from headspace handling. Owned-name suppression is not invoked without an established preferred owner."},
        ],
        "native_partonomy": {"scope": "Only the four successors plus actual maintained owners needed to resolve their explicit MIM_CATALOG parts", "candidate_count": 4, "reference_owner_count": len(owners), "owner_inputs": [bind(p) for p, _ in owners], "errors": [], "limits": "No repeated full-catalog test; root owns final all-76 overlay validation. This pass does not approve unrelated fields on referenced owners."},
        "owned_name_search": {"ignored_files_included": True, "method": "Path.rglob over complete current data/ingredients, native preferred_term_owners for mapped records, exact stripped casefold tokens; all 76 original selected proposal preferred names checked separately", "mapped_count": len(mapped), "maintained_inventory": inventory, "native_preferred_hits": owner_hits, "selected_proposal_inventory": proposal_inventory, "limits": "No exact owner found in this declared scope; other workers/current remote proposals were not searched. Absence does not establish chemical identity."},
        "native_projections": {"producer": bind(producer), "rows": projections, "limits": "Actual native producer called in memory with empty ancillary maps; no canonical export, full downstream gate or source admission approval."},
        "native_sources": [bind(W / f) for f in ["src/mediaingredientmech/validation/write_validated.py", "src/mediaingredientmech/validation/component_partonomy.py", "src/mediaingredientmech/synonym_policy.py", "src/mediaingredientmech/schema/mediaingredientmech.yaml", "MAPPING_SEMANTICS.md"]],
        "retained_limits": ["Five original source cases contain seven occurrence IDs; only six support these positive proposals, with NBRC824 retained as the explicit missing-denominator hold.", "Scientific applicability beyond the exact #1237 deltas, original component-owner/release holds and ambiguous Se/W co-installation remain unresolved where stated.", "No candidate, predecessor, maintained data, Git or GitHub mutation by this review; independent exact-byte review does not itself apply candidates."]
    }
    out = D / "reviews/science-technical-by-issue-context-v1.json"
    with out.open("x") as f:
        json.dump(report, f, indent=2, ensure_ascii=False); f.write("\n")
    print(json.dumps({"review": bind(out), "candidate_count": 4, "evidence_type_changes": 5, "partonomy_errors": 0}))


if __name__ == "__main__":
    main()
