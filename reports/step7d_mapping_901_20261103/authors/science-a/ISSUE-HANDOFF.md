# Issue-first scope for science-a

These are author findings and proposed dispositions, not posted comments or applied changes. The coordinator must live-deduplicate/update the existing issues before a guarded writer runs. The frozen `decisions.json` carries exact owner hashes and before/after operations; `evidence-index.json` binds the sources.

## Proposed #268 update: supported chemistry and procurement corrections

Three included owners have evidenced structure-scope defects:

- `5-Fluoroorotic_Acid_Hydrate`: historical F5013 and the current supplier describe `xH2O`, whereas formula, SMILES, InChI and CID16212749 fix one water. Withdraw those four unqualified fields; preserve CAS207291-81-4, source metadata and history. This does not assert that a monohydrate is impossible.
- `Beta-Glycerophosphate_Disodium_Salt_Hydrate`: the current SMILES/InChI place negative charge on terminal alcohols, and the formula/structure/CID44828775 impose one water. The source name and supplier comparator concern the disodium phosphate salt with `xH2O`. Withdraw those four fields without guessing a new CID or water count. G9422 is comparison evidence, not actual procurement provenance for the historical owner.
- `Cadmium_Acetate_Dihydrate`: retain the correct `C4H6CdO4.2H2O` formula and CAS5743-04-4, but withdraw the water-free SMILES, InChI and CID10986. Fresh supplier/PubChem dihydrate evidence establishes the mismatch; no automatic replacement structure is proposed.

Two included local hydrate owners need a procurement/substance distinction:

- `Cefsulodin_Sodium_Salt_Hydrate`: the actual C8145 catalogue describes an unspecified hydrate, while CAS52152-93-9 also identifies the water-free sodium salt. Keep local hydrate identity. Move that CAS from unqualified chemical properties to the explicitly qualified C8145 supplied form.
- `Chlorhexidine_Diacetate_Salt_Hydrate`: both historical C6143 and current C6143 identify a diacetate hydrate; current supplier formula is `xH2O`. Historical CAS56-95-1 and current supplier CAS206986-79-0 conflict, and the latter returns mixed PubChem forms. Keep local source-defined hydrate identity, move procurement information to supplied_form, and preserve both CAS observations in notes/history. Do not choose an exact CAS primary or fixed-water structure. If independent review finds the material boundary unresolved, drop this whole owner, including the procurement change.

The dropped alpha-ketoglutarate disodium hydrate and adenine hydrochloride hydrate also carry water-free formula/structures. Their own CAS/material boundaries remain unresolved; record the defects for follow-up but do not partially edit those dropped owners in this batch.

## Proposed #901 update: bounded relation and identity decisions

Eleven of this partition's22 owners are proposed for the data transaction. Their YAML grade becomes `NARROW_MATCH`; supported generation must emit `skos:broadMatch`, never the inverse predicate. Own identity remains separate from ontology grounding and all existing role holds persist.

- Beta-glycerophosphate hydrate uses the closer disodium parent `CHEBI:132089 sodium glycerol 2-phosphate`, replacing the free-acid parent. Keep the separate parent owner and hydrate owner distinct.
- Cerium chloride heptahydrate gains own CAS18618-55-8, corroborated by specific primary supplier/PubChem evidence and raw seven-water source labels.
- Copper nitrate trihydrate gains own CAS10031-43-3, corroborated by current GSRS/PubChem and source/formula evidence. Preserve the existing local registry identities for both CAS promotions. The ignored-inclusive current owner scan found no other record owning either proposed CAS.
- No new exact ontology term was selected. Recorded searches are bounded and do not claim universal absence.

Eleven owners are dropped entirely. Ceftazidime C3809 needs an active-hydrate versus stabilized whole-product ruling; my default recommendation is an active-hydrate owner with C3809 in supplied_form, reserving a whole-product mixture identity for an explicit source-boundary decision. Bathophenanthroline has a real positional-structure conflict among the apparent exact hydrate terms. Alpha-ketoglutarate and adenine HCl have unresolved CAS/hydrate boundaries. Potassium chromium alum needs a whole-substance parent decision. The unusual calcium/copper hydrate source labels remain unresolved. CoCl2·4H2O is an evidentiary drop because the direct primary crystal article could not be inspected; this is not an impossibility claim.

The existing #344 source history and #312 registry/membership work are retained. No source label is corrected by guessing a more familiar hydrate. No owner merge, occurrence transfer, new role approval or extra owner is proposed.

Parent-only exact alias findings are recorded separately with no operations. The coordinator must preserve every one of the23 staged #669 pairs; this batch must not silently complete that later rollout. Existing native WITHHOLDs continue. An inherited support stamp cannot follow a changed owner or assertion without the required qualification/review.

## Execution evidence and handoff

Current strict validation passed22files with0errors. All22 individual `validate-terms` invocations exited0. Their actual receipts are `RUN/logs/science-a-strict-v1.{json,log}` and `RUN/logs/science-a-terms-01.json` through `-22.json`; `terms-summary.json` gives exact absolute paths. These checks cover the current inputs, not a hypothetical applied transaction, scientific approval or a full suite.

`unchanged-source-readback.json` records clean current main467aa319 and exact target hashes at final author handoff. No maintained source, canonical output, workflow, Git ref or GitHub object was changed by this review. The author is not the independent reviewer.
