# Step 7d author review: owners 46–67

Baseline: `467aa319a06ef992035f509f66fe251082b44ae1`. This is a complete author assessment of 22 current owners, not an independent final review, native saved review, or approval. No maintained file or GitHub object was edited.

**Result: 12 include, 10 drop.** Exact preimages, proposed operations, full rubric and source claims are in `assessments-v2.json`; `evidence-manifest.json` records all reused or newly captured evidence with exact hashes. The v2 supplement changes metadata only: dispositions and field operations are unchanged from `assessments.json`.

| Owner | Decision | Scope or remaining decision |
|---|---|---|
| Maltose_Hydrate | INCLUDE | Retain local generic-hydrate identity; change parent relation to NARROW_MATCH without assigning water count or anomer. |
| Maltotriose_Hydrate | INCLUDE | Correct open-chain parent CHEBI:61993 to cyclic reducing-end-unspecified CHEBI:140999; NARROW_MATCH. File finding first. |
| Mgcl2_X_7_H2o | DROP | Unresolved source hydration; do not substitute a familiar hydrate. |
| Na2hpo4_X_3_H2o | DROP | Unresolved source hydration; retain local identity and hold. |
| Na2hpo4_X_6_H2o | DROP | Unresolved source hydration; retain local identity and hold. |
| Nah2po4_X_2_H2o | DROP | Exact candidate NCIT:C66551 exists, but coupled alias/membership correction remains on #758/#740. |
| Neomycin_Trisulfate_Salt_Hydrate | DROP | N1142 is a supplied saline solution; active substance versus formulation requires a decision. |
| Nicl2_X_2_H2o | INCLUDE | Literal source dihydrate and primary experimental evidence support NARROW_MATCH; retain local identity and formula. |
| Nicl2_X_5_H2o | DROP | Unresolved source hydration; retain local identity and hold. |
| Palatinose_Hydrate | INCLUDE | NARROW_MATCH; remove four over-specific one-water chemistry assertions. |
| Potassium_Citramalate_Monohydrate | INCLUDE | NARROW_MATCH; remove four dry-salt chemistry assertions; no enantiomer or supplier assignment. |
| Potassium_Tellurate_Hydrate | INCLUDE | NARROW_MATCH; remove four over-specific one-water chemistry assertions. |
| Potassium_Tellurite_Hydrate | DROP | Archived hydrate and current P0677 dry-salt certificate conflict; historical product identity needed. |
| Sodium_Carbonate_Monohydrate | INCLUDE | Promote to NCIT:C80911 with CAS_RN_LOOKUP; reject process-only token; keep pending solution alias unchanged. |
| Sodium_Cholate_Hydrate | INCLUDE | NARROW_MATCH; remove four over-specific one-water chemistry assertions and reject dry-parent synonym. |
| Sodium_Deoxycholate_Monohydrate | INCLUDE | NARROW_MATCH; retain verified one-water chemistry and source spelling variants. |
| Sodium_Hypophosphite_Monohydrate | DROP | Current parent and chemistry lose two phosphorus-bound hydrogens; resolve ontology parent first. |
| Sodium_Phosphite_Dibasic_Pentahydrate | INCLUDE | NARROW_MATCH only; source formula and prior #320 decision support current parent convention. Do not import erroneous PubChem properties. |
| Sodium_Thiophosphate_Tribasic_Hydrate | INCLUDE | NARROW_MATCH; remove four over-specific one-water chemistry assertions. |
| Stachyose_Hydrate | INCLUDE | NARROW_MATCH; remove four water-free chemistry assertions. A tetrahydrate term exists but is too specific for the supplied n-hydrate. |
| Terpene_Hydrate | DROP | Unresolved cis/stereo scope among source CAS, ChEBI, NCIt and GSRS; leave on #901. |
| Vancomycin_Hydrochloride_Hydrate | DROP | Archived SKU does not match inspected MP certificate; hydration/product scope requires a decision. |

The carbonate conclusion is ready for a sourced update on #1117 and its own record commit. The pending “Sodium carbonate solution” alias pair remains untouched for the later #669 step. The six chemistry withdrawals and maltotriose parent correction require their issue updates before writes. `findings-handoff.json` gives the deduplication and suggested issue scopes.

Native checks: strict validation passed for all 22 current owners with zero findings. Each of 22 individual term validations passed. The carbonate and maltotriose candidate files passed individual term validation. An initial directory-form candidate invocation failed before validation; its receipt remains preserved. No full suite or final-batch QC was run by this author.

Evidence limits: supplier page inspection notes are identified as notes and their hashes are not claimed to be raw HTTP page hashes. Failed/blocked requests remain preserved and are not treated as evidence. CAS Common Chemistry returned a JavaScript shell, so no direct registry-content verification is claimed. Historical source CSV evidence is explicitly an archived untracked input, not a Git blob. Other manufacturers’ matching catalog compounds corroborate chemistry but do not establish the original purchase or lot.

No role approvals, owner merges, occurrence transfers, guessed hydration, maintained edits, GitHub mutations, or provider credits were used. All changed owner bytes must receive fresh native companion support and the independent final review required by the plan.
