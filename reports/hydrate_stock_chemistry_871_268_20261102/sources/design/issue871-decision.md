Recording the approved narrow Step7(b) implementation scope for #871/#268 before source edits. Work begins from verified current main after Step7(a) merges. This is a source/guard decision, not a completed scientific review.

Primary evidence supports two exact replacements: [CHEBI:91258 through EBI OLS](https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:91258) supplies the dihydrate structures; [PubChem CID6096963](https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/6096963/property/MolecularFormula,InChI,CanonicalSMILES,IUPACName/JSON) supplies seven-water structures and its [same-CID synonym response](https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/6096963/synonyms/JSON) agrees with the committed NCIT:C61946 CAS/formula/UNII evidence. Preserve original capture times and exact response hashes.

The remaining inherited structures match the archived anhydrous parent ChEBI annotations. For unspecified hydrates, [Sigma B1375](https://www.sigmaaldrich.com/US/en/product/sigma/b1375) and [C8145](https://www.sigmaaldrich.com/US/en/product/sigma/c8145) describe variable hydration/anhydrous-basis mass; the [Thermo DL-isocitrate specification](https://assets.thermofisher.com/chem-specs-pdf/retrievePdf?countryCode=cn&erp_type=CN_E1_LCD&rootSku=20501&sku=205010050) describes dry-substance assay and variable water; [Sigma C6143](https://www.sigmaaldrich.com/deepweb/assets/sigmaaldrich/product/documents/199/546/c6143pis.pdf) names a hydrate without resolving the water count. These suppliers’ descriptors are not proof of fixed whole-hydrate chemistry or of the original MIM supplier.

The thiamine stock’s own #288/#320 history identifies CAS154-87-0 as the pure chloride’s. The [Cayman20254 primary specification](https://cdn.caymanchem.com/cdn/insert/20254.pdf) independently identifies that CAS with the chloride solid, with solution preparation described separately. Its old NCI name lookup does not establish a stock-level CAS. Remove the active block and the corresponding `CAS:154-87-0` token from current canonical row9’s `other`, preserving the original lookup/history. No replacement CAS is inferred.

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

Local preparatory evidence is `step7b-source-design-20261102`: field matrix SHA256 `9cd413c4e81e9979645c4a6ebd9a4aa75d1a9758d08f38a097eb1dfd74a402dd`; original evidence index `b6469d588ea3c487b4b86deb26de914980a63f50115f70477017eaca5df8ab69`. The implementation PR must make the bounded source evidence durable. Five direct Sigma HTTP timeouts are preserved; inspected official web-tool extracts are identified separately from successful raw PDF/JSON captures.

