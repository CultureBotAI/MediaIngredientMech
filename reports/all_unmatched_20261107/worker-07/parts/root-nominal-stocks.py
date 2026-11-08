"""Four explicit source-qualified nominal stock proposals after integration finding03.

Original A primary bundles stay immutable. The assembler applies only these
four explicit decision deltas; the independent integration reviewer reassesses
the final changed decisions and exact new payloads.
"""
import datetime
import hashlib
import json
from pathlib import Path

from mediaingredientmech.validation.write_validated import write_validated_ingredient

OUT = Path("reports/all_unmatched_20261107/worker-07")


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    decisions = json.loads((OUT / "parts/a-decisions.json").read_text())["decisions"]
    entries = [
        (11, "togo_m2570_l_cysteine_hcl_25percent_stock", "L-cysteine hydrochloride 2.5% stock (TOGO M2570)", "L-cysteine hydrochloride (hydrate unspecified)", "2.5", "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2570", "components[1].items[1]; comments paragraph_index=6",
         "TOGO M2570 specifies a 10 mL aliquot of 2.5% L-cysteine hydrochloride stock prepared under nitrogen and autoclaved before addition. Nitrogen is a preparation atmosphere, not an asserted bulk solute. Solvent, percentage basis and reagent hydrate are unreported; L stereochemistry and hydrochloride are explicit. The frozen G_PER_L quantity is preserved as a source normalization conflict, not used as stock composition."),
        (23, "jcm87_lactic_acid_20percent_titrant", "Lactic acid 20% titrant (JCM 87)", "Lactic acid (stereochemistry unspecified)", "20", "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=87", "Final instruction after the JCM87 ingredient table",
         "JCM 87 permits 20% lactic acid OR 1 N to 6 N HCl to adjust the final medium to pH 5.6. This proposal denotes only the lactic acid stock alternative. HCl is not a constituent of it, and pH 5.6 is not the stock pH. Percentage basis, solvent and acid stereochemistry are unreported; the amount is determined by the final-medium pH endpoint."),
        (45, "togo_m2653_sodium_acetate_25percent_stock", "Sodium acetate 25% stock (TOGO M2653)", "Sodium acetate (hydrate unspecified)", "25", "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2653", "components[0].items[2]",
         "TOGO M2653 specifies a 4 mL aliquot of 25% sodium acetate stock. Percentage basis, solvent and hydrate of the weighed starting material are unreported. The frozen normalized amount 4 with a mass concentration unit is not evidence for a mass fraction or final solute concentration."),
        (46, "nbrc989_sodium_lactate_50percent_stock", "Sodium lactate 50% stock (NBRC 989)", "Sodium lactate (stereochemistry unspecified)", "50", "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=989", "Composition table: 50% Sodium lactate, 25 ml",
         "NBRC 989 specifies 25 mL of 50% sodium lactate stock. The two frozen occurrences have conflicting ML_PER_L and G_PER_L units; both remain in the decision with the primary volume as context. Percentage basis, solvent and sodium lactate stereochemistry are unreported. No L or DL pure-salt identity is selected."),
    ]
    now = datetime.datetime.now(datetime.timezone.utc).isoformat()
    proposals, deltas = [], []
    for index, slug, label, component, strength, url, locator, note in entries:
        original = decisions[index]
        pid = f"ROOT-PROPOSAL-NOMINAL-{index}"
        owner = f"data/ingredients/mapped/{slug}.yaml"
        assert not Path(owner).exists()
        identifier = "kgmicrobe.ingredient:" + slug
        limitation = (note + " This is a nominal source-qualified preparation, not a fully resolved chemical formulation. "
                      "PERCENT preserves the unspecified source percent basis; it is not PERCENT_WV or PERCENT_WW. "
                      "UNKNOWN component-list completeness records the unreported solvent/preparation inputs. "
                      "No generic raw source label is made a global resolving synonym and no inherited hold is removed.")
        evidence = {"evidence_type": "RECIPE_SOURCE", "source": url, "source_record": locator, "notes": limitation}
        record = {"identifier": identifier, "preferred_term": label, "mapping_status": "MAPPED", "ingredient_type": "STOCK_SOLUTION",
                  "ontology_mapping": {"ontology_id": identifier, "ontology_label": label, "ontology_source": "kgmicrobe.ingredient", "mapping_quality": "FALLBACK_REGISTRY", "evidence": [{"evidence_type": "MANUAL_CURATION", "source": url, "notes": "Nominal source-qualified preparation registry identity only. No exact pure-solute ontology equivalence is asserted."}]},
                  "components": [{"component_name": component, "reference_scope": "UNMAPPED", "concentration_value": strength, "concentration_unit": "PERCENT", "source": "Literal stock-strength label; percentage basis unspecified in this source."}],
                  "component_assertion": {"method": "RECIPE_TRANSCRIPTION", "completeness": "UNKNOWN", "evidence": [evidence]}, "notes": limitation,
                  "curation_history": [{"timestamp": now, "curator": "all-unmatched-20261107-worker07-root", "action": "SOURCE_QUALIFIED_NOMINAL_STOCK_PROPOSED", "changes": "Address independent integration finding INTEGRATION-03 with an isolated nominal stock proposal while retaining chemical and quantity uncertainty. " + note, "new_status": "MAPPED", "llm_assisted": True}]}
        capture = OUT / f"proposed_owners/root-nominal-{index}.yaml"
        write_validated_ingredient(record, capture)
        proposals.append({"proposal_id": pid, "kind": "new_owner", "owner_path": owner, "before_sha256": None,
                          "after_capture": {"root": "artifact", "path": str(capture.relative_to(OUT)), "sha256": sha(capture)},
                          "case_ids": [original["case_id"]], "evidence_ids": original["evidence_ids"], "description": "Propose " + label + " with explicit unresolved percentage basis and component forms.",
                          "identity_predicate_consequences": "Own local registry identity; no asserted exact equivalence to pure solute or any other stock.",
                          "publication_review_obligation": "Coordinator must compare source-qualified stock equivalence/cross-shard proposals, apply via guarded writers only after full owner review, and preserve all source and publication holds.", "limitations": limitation})
        deltas.append({"case_id": original["case_id"], "case_index": index,
                       "author_decision_sha256": hashlib.sha256(json.dumps(original, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest(),
                       "reasoning_append": " A bounded nominal stock proposal now preserves the declared source strength without selecting unreported solvent, percent basis or molecular form.",
                       "applicability_append": " Proposal " + pid + " applies only to the listed frozen occurrence context(s). " + note,
                       "proposal_ids": [pid], "no_change_reason": None, "missing_requirement": original["missing_requirement"].replace("before mapping the stock", "before fully specifying the stock and any supplied-form identity"),
                       "review_requirement": "Independent integration reviewer must review this final decision delta and exact new payload; original C review alone does not approve this later root-authored change."})
    (OUT / "parts/root-nominal-stock-proposals.json").write_text(json.dumps({"schema_version": 1, "proposals": proposals}, indent=2) + "\n")
    (OUT / "parts/root-decision-deltas.json").write_text(json.dumps({"authored_at": now, "author": "/root", "trigger": "INTEGRATION-03", "preflight": "Ignored-inclusive rg over all maintained individual YAMLs for the four exact strength/name patterns found no literal match; this is a bounded lexical check, not absence of chemically equivalent stocks. Final catalogue validator checks proposed IDs and paths.", "deltas": deltas}, indent=2) + "\n")
    print(f"Wrote {len(proposals)} isolated nominal stocks and explicit case deltas; original primary bundles unchanged.")


if __name__ == "__main__":
    main()
