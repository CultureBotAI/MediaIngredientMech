# `data/ingredients/mapped/Sodium_Carbonate_Monohydrate.yaml`

**Verdict**: needs curation, major issue.

**Identity**: `sodium carbonate monohydrate` is correctly kept distinct from
anhydrous `CHEBI:29377` / `sodium carbonate` with primary identifier
`cas:5968-11-6`. Fresh OLS4 lookup confirmed that `CHEBI:29377` is the
anhydrous parent with CAS RN `497-19-8`, while PubChem resolves hydrate CAS RN
`5968-11-6` to CID `2735133` with the monohydrate formula, SMILES, and InChI
stored in the record. A fresh ChEBI search for `sodium carbonate monohydrate`
did not find a specific carbonate monohydrate term.

**Validation**: `uv run --frozen python scripts/validate_strict.py
data/ingredients/mapped/Sodium_Antimonate.yaml
data/ingredients/mapped/Sodium_Azide.yaml
data/ingredients/mapped/Sodium_Beta-glycerophosphate.yaml
data/ingredients/mapped/Sodium_Bromate.yaml
data/ingredients/mapped/Sodium_Carbonate_Monohydrate.yaml` passed for the
5-file batch with 0 ERROR rows. Direct `linkml-term-validator validate-data`
with `--labels` passed.

**Evidence**: The hydrate CAS identity, PubChem structure, and
`skos:closeMatch` to the anhydrous ChEBI term pass, and the per-record YAML
agrees with the regenerated aggregate row when keyed by `(preferred_term,
mapping_status)`.

The final SSSOM needs repair. `reports/hydrate_grounding.tsv` classifies this
record as `CAS_MISSING_ANCHOR_ROWS`: rows 2624-2625 preserve the exact CAS
identity but omit an exact `kgmicrobe.compound:sodium_carbonate_monohydrate`
anchor. Row 2624 also exports `Sodium carbonate solution` and `disodium
trioxidocarbonate` in `other`; those are a solution label and an exact ChEBI
synonym for anhydrous sodium carbonate, not same-substance synonyms for the
monohydrate.

**Completeness**: The hydrate has enough CAS and structure support, and the
absence of roles and components is expected. The stale `(adjust if required)`
raw label is contained in YAML and filtered from final SSSOM.

**Recommended Edits**: Add the missing exact
`kgmicrobe.compound:sodium_carbonate_monohydrate` anchor for this CAS-primary
hydrate, remove solution and anhydrous-carbonate synonyms from final SSSOM
`other`, then rebuild final SSSOM and confirm the hydrate-grounding row no
longer reports `CAS_MISSING_ANCHOR_ROWS`.
