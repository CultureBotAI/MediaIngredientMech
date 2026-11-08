Proposed update to [#321](https://github.com/CultureBotAI/MediaIngredientMech/issues/321), with existing #320/#374 history retained; do not file another generic hydrate-collapse issue.

Worker 02 confirms a bounded chemistry-field residual after the earlier nickel hydrate identity corrections:

| Owner and status | Frozen residual | Reviewed proposal |
|---|---|---|
| `Niso4_X_7_H2o.yaml`, MAPPED, CHEBI:53504 | Formula already includes seven waters, but InChI and SMILES still describe anhydrous nickel sulfate; the earlier incorrect six-water CAS was withdrawn without replacement. | `c-proposal-nickel-sulfate-7-water-properties` uses the official seven-water structure and CAS 10101-98-1. |
| `Niso4_X_6_H2o.yaml`, REJECTED, CHEBI:53437 | The merge record retains anhydrous formula/InChI/SMILES despite pointing to the six-water survivor. | `c-proposal-nickel-sulfate-6-water-properties` corrects these archival fields while retaining REJECTED status. The active `Nickel_II_sulfate_hexahydrate.yaml` survivor is already six-water-specific. |

Official [CHEBI:53504](https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_53504) and [CHEBI:53437](https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_53437) capture the distinct form-specific structures. Evidence, exact before/after hashes and independent review are in worker 02's C proposal bundle. These are field corrections, not another promotion to hydrate identities and not permission to merge or reactivate rejected records.

Preserve historical finding `SEM:1971ff4d47b066a4339f` as OPEN until its full scope is resolved: it also covers parent synonyms and provisional role evidence. The separate role finding `SEM:db276e2e3eae5d2442dc` is not resolved by chemical-property replacement. Preserve `SEM:40c78da59752cd7b40cd` as EXCLUDED_REJECTED for the six-water merge record; archival cleanup does not establish an active publication claim.

Recommended tracking action: append this evidence-backed residual to #321 and explicitly reconsider its closure for the active seven-water structure gap; preserve all historical successful identity fixes and count corrections. Do not reopen #374 as though its specific-identity promotion had failed. Complete guarded property integration and changed-owner review before retiring the bounded structural portion; retain other source/publication holds. No proposal has yet been applied by this campaign.
