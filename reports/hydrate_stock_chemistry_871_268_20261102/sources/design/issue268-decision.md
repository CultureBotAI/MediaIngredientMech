Recording the approved narrow Step7(b) prevention and source-repair scope shared with #871, before implementation. Begin only after the preceding Step7(a) merge is verified. This comment does not turn automated enrichment or diagnostics into scientific approval.

The present chemistry write routes need one shared, positive record/form eligibility decision: `IngredientCurator.enrich_chemical_properties`, the reviewer’s enrichment suggestion/application, `scripts/enrich_from_ols.py`, and `scripts/enrich_chemical_properties.py`. Stop stock/mixture, rejected/incomplete owner, broader-parent and unresolved form routes before provider calls. Preserve curated chemistry and return a reviewable reason when automatic additions are refused. Post-fetch values must be bound to the validated exact source term and compatible form; neither lexical equality nor a matching identifier string proves chemical identity.

Follow MAPPING_SEMANTICS §0: `CAS_RN_LOOKUP` records method provenance. Do not regrade it or blanket-reject it solely because of its grade when independent evidence establishes the same substance/form. Test eligible exact, synonym and CAS-established identities, alongside hydrate-count, salt/stereo, concentration and mixture conflicts. The existing hydrate parser is a contradiction detector, not a universal identity oracle.

The current client’s old mixed cache and first-PubChem-CID fallback do not return adequate exact-form provenance for automatic record authority. The narrow safe writer path uses validated exact-term properties without allowing those results to bypass form/source checks. Preserve raw retrieval capability; do not choose an ambiguous CID, fabricate water components, or broaden this into a new research framework. Regression tests must exercise all four callers, pre-provider refusal, unchanged records, mixed-cache bypass and preservation of curated fields.

The historical classifier cascade is also a regression target, but the current classifier already checks solution/complex names before structural ontology membership, skips explicitly typed records, and does not classify from a populated formula. Protect that behavior without claiming the old implementation is still present.

The concrete residual stock defect is `02_Thiamine_Pyrophosphate.yaml`: its existing stock-identity ruling and [Cayman’s primary chloride specification](https://cdn.caymanchem.com/cdn/insert/20254.pdf) show why CAS154-87-0 and the pure-compound chemistry cannot remain active whole-stock properties. Set `STOCK_SOLUTION`, remove the whole block, and remove the single generated `CAS:154-87-0` display token from canonical row9. Preserve all original evidence/history; do not guess the actual stock’s solute salt or formulation.

The two phosphate replacements are supported by [exact dihydrate CHEBI:91258 annotations](https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:91258) and [heptahydrate PubChem CID6096963 properties](https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/6096963/property/MolecularFormula,InChI,CanonicalSMILES,IUPACName/JSON), cross-checked with the committed NCIT:C61946 CAS/formula/UNII evidence. The unspecified-hydrate decisions retain the supplier limitations recorded in the shared source packet.

The full batch includes all 14 owners named in #871 and the thiamine stock associated with #268. The heptahydrate exclusion in the approved plan applies to Step7(d), not this Step7(b) chemistry batch.

| Owner under `data/ingredients/mapped/` | Narrow source operation |
|---|---|
| `Cocl2_X_2_H2o.yaml` | Remove inherited anhydrous InChI/SMILES and parent attribution; retain existing stated-hydrate formula. |
| `Cocl2_X_4_H2o.yaml` | Same bounded removal for the tetrahydrate. |
| `K2hpo4_X_3_H2o.yaml` | Same bounded removal for the trihydrate. |
| `Nah2po4_X_2_H2o.yaml` | Same bounded removal for the dihydrate. |
| `Nicl2_X_2_H2o.yaml` | Remove inherited structures and ambiguous block attribution; retain existing stated-hydrate formula. |
| `Cecl3_X_7_H2o.yaml` | Remove inherited structures and parent attribution; retain existing stated-hydrate formula. |
| `Cu_No32_X_3_H2o.yaml` | Remove inherited structures; retain existing trihydrate CAS/formula/import provenance. Its #901 identity decision remains open. |
| `Na2hpo4_X_2_H2o.yaml` | Replace InChI/SMILES with the exact two-water CHEBI:91258 annotations; retain CAS/formula. |
| `Na2hpo4_X_7_H2o.yaml` | Replace InChI/SMILES with exact seven-water PubChem CID6096963 values cross-checked against NCIT:C61946; retain NCIT identity/CAS/formula. |
| `Bathophenanthrolinedisulfonic_Acid_Disodium_Salt_Hydrate.yaml` | Remove unqualified parent formula/InChI/SMILES; retain existing CAS/import provenance without asserting a fixed hydration number. |
| `Cefsulodin_Sodium_Salt_Hydrate.yaml` | Same bounded unspecified-hydrate cleanup. |
| `Chlorhexidine_Diacetate_Salt_Hydrate.yaml` | Same cleanup; supplier formula/water-stoichiometry ambiguity remains explicit. |
| `DL-Isocitric_Acid_Trisodium_Salt_Hydrate.yaml` | Same cleanup; dry-substance descriptors do not establish fixed whole-hydrate chemistry. |
| `Disodium_Phosphate_Heptahydrate_002_M_Stock.yaml` | Remove the entire inherited solute chemistry block, including anhydrous molecular weight. |
| `02_Thiamine_Pyrophosphate.yaml` | Remove the entire pure-solute chemistry block, including CAS154-87-0; set `STOCK_SOLUTION`; synchronize its one generated CAS display token. |

Preserve every primary identifier, ontology mapping/grade, role, occurrence count, existing history and unrelated field. Append an actual-time curation event with exact source/preimage evidence. Retained formulas/CAS values are not blanket revalidated by removing incompatible structures. Do not invent hydration stoichiometry, supplier assignments, stock solvent, percentage basis, solute salt, components or new identities.

At the inspected feature head `83d0375c6abc9eee97039315ba9b7d496aff8391`, all 27 scoped mapping rows are `WITHHOLD`. Chemistry cleanup does not approve them or any role. Preserve existing aliases, including the thiamine stock’s six unresolved pure-solute aliases; this batch removes only the CAS display token generated from the mis-scoped active CAS field. Alias cleanup and remaining identity/BUFFER/formulation questions stay explicit follow-up work.

Use guarded, exact-preimage source writes, supported synchronization/generation and an approval-free native receipt. Preserve historical receipts and both existing FORM authorities. Inspect actual generation differences before bounded canonical promotion; the stock CAS removal does not authorize unrelated row/date/source-vocabulary changes. The canonical hash changes if that token is removed, so do not reuse the conditional zero-row/unchanged-manifest shortcut. A narrowly reviewed native companion transition must account for that manifest change.

Run focused regressions, required native data/export checks and `just qc`, then the full relevant suite and independent adversarial review with findings fixed and re-reviewed. No completed checks or scientific clearance are asserted by this decision comment.

The plan literally prohibits touching the unified snapshot. It does not separately name provenance as forbidden. Nevertheless a provenance-only restamp is not a valid workaround: the native stamp follows a successful rebuild, and the current Casein projection already differs from the protected snapshot. At the audited base the complete batch conditionally yields 26 distinct changed owners against the native limit of25. Recheck after the real Step7(a) merge; the pending snapshot exception is not approval. Prepare the authorized source/guard work without omitting an owner, weakening the gate, or manufacturing a fresh stamp; resolve the publication constraint before claiming gate-complete publication.

Writer regressions must use evidence-pinned pre-correction fixtures, preserve all existing history and enforce exact allowed fields. Pure tests must collect without optional Claw dependencies; real native transaction tests must retain receipt reservation, descriptor-bound journal ownership, late-alias refusal and partial-I/O recovery coverage. The local field matrix is SHA256 `9cd413c4e81e9979645c4a6ebd9a4aa75d1a9758d08f38a097eb1dfd74a402dd`; preparatory source index is `b6469d588ea3c487b4b86deb26de914980a63f50115f70477017eaca5df8ab69`. Durable evidence and actual check results belong in the eventual implementation PR.

