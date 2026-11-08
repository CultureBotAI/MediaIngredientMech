Four concentration-qualified labels resolve uniquely to pure-compound owners in the frozen worker08 label index. The same owner bytes remain on live `main`, checked through the GitHub contents API on 2026-11-08 UTC.

| Owner | Resolving labels | Frozen owner SHA256 |
|---|---|---|
| `data/ingredients/mapped/Kh2po4.yaml` (`CHEBI:63036`) | `KH2PO4 (0.4 g/l)`, `KH2PO4 (7% w/v)` | `e721979cb20e8dcac144900643442d9d9e1f01e4d69b2073de8266120419f1c4` |
| `data/ingredients/mapped/Na2s_X_9_H2o.yaml` (`CHEBI:76209`) | `Na2S x 9 H2O (3% w/v)`, `Na2S x 9 H2O(24% w/v)` | `e849eb5c8d5a8d977c572ee249927b7fb71b40506e23ed6fb4c30d089b5c8219` |

The phosphate labels are `RAW_TEXT`; the sulfide labels are `HYDRATE_FORM`. All four appear as `synonym`, `MAPPED`, `unique` rows targeting the pure compound in [the exact frozen label index](https://github.com/CultureBotAI/MediaIngredientMech/blob/7efd3f8b98f9e822431dcb510c2c242a2569cfc7/docs/data/label_index.csv). This is a direct index observation, not a claim that a new downstream rebuild was performed.

[ChEBI:63036](https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:63036) denotes potassium dihydrogen phosphate and [ChEBI:76209](https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:76209) denotes sodium sulfide nonahydrate. A concentration-qualified preparation or receiving-dose instruction is not an exact global synonym for either pure substance. Missing stock carrier or percentage-basis evidence must remain explicit; neither quantity nor solvent should be invented.

Worker08's authorship-separated issue1201 review identified this as IF1201-R2. Isolated proposals `if1201-edit-kh2po4-alias-scope` and `if1201-edit-nonahydrate-stock-aliases` retain the exact labels and provenance as `REJECTED_LABEL`, preserving identity, roles, counts and source holds. The same phosphate proposal also rejects the orphan `(dibasic)` owner token, but that bare token was not found as an exact row in the frozen label index, so no consumer-resolution claim is made for it. Maintained data are unchanged.

Integration follow-up:

- Reconcile these exact preimages with other campaign proposals and apply the separately reviewed owner deltas through the guarded writer.
- Synchronize maintained surfaces and regenerate/check the label index and SSSOM through the coordinator's authorized integration workflow.
- Verify these four full labels no longer resolve globally to the pure owners; retain source-specific stock and receiving-dose context.
- Preserve all existing source/role/export holds. This finding does not approve a stock formulation, source membership, owner-wide payload or release.

Deduplication: read #811, #868, #758, #464, #899 and #901 context, and searched all issue states for `sulfide`, `Kh2po4`, `dibasic` and the exact concentration-qualified labels. The earlier calcium-sulfate/potassium-phosphate issue and the generic phosphate-label issue are different defects. Tris stock/nitrilotriacetate alias work is already tracked in #1157 and is intentionally excluded here. The source-review completion work remains under #1201.

Exact live-main hashes, frozen-index rows, search results and immutable proposal/review bindings are retained in `reports/all_unmatched_20261107/worker-08/successors/issue-1201-v1/`. No PR, merge, rebuild or publication was performed by this finding.
