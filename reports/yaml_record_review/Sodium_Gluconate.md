# `data/ingredients/mapped/Sodium_Gluconate.yaml`

**Verdict**: needs curation, major issue.

**Identity**: `Sodium gluconate` maps exactly to active, defining
`CHEBI:84997` / `sodium gluconate`. Fresh OLS4 lookup confirmed the ChEBI
label, CAS RN `527-07-1`, formula `C6H11O7.Na`, InChI, InChIKey, SMILES, and
same-substance gluconate synonyms. PubChem resolves the CAS RN to CID
`23672301` with the same formula, InChI, InChIKey, and structure.

**Validation**: `uv run --frozen python scripts/validate_strict.py
data/ingredients/mapped/Sodium_Fluorophosphate.yaml
data/ingredients/mapped/Sodium_Gluconate.yaml
data/ingredients/mapped/Sodium_Glutamate_Monohydrate.yaml
data/ingredients/mapped/Sodium_Hypochlorite.yaml
data/ingredients/mapped/Sodium_Hypophosphite_Monohydrate.yaml` passed for the
5-file batch with 0 ERROR rows. Direct `linkml-term-validator validate-data`
with `--labels` passed.

**Evidence**: The exact CHEBI identity, CAS RN, formula, InChI, SMILES, local
Na-gluconate aliases, and kg-microbe exact synonyms pass. The raw
`Properties:` strings are correctly filtered from final SSSOM row 2643, which
exports only same-substance labels plus `CAS:527-07-1`. The per-record YAML
agrees with the regenerated aggregate row when keyed by identifier and
preferred term.

The `CARBON_SOURCE` and `ENERGY_SOURCE` roles still need curation. Both are
`COMPUTATIONAL_PREDICTION` claims with provisional `review recommended`
curator notes, one from the curated name-pattern rule and one added alongside
the carbon-source prediction.

**Completeness**: The record is otherwise complete for exact sodium gluconate
identity and has refreshed 20-occurrence statistics.

**Recommended Edits**: Either replace the provisional `CARBON_SOURCE` and
`ENERGY_SOURCE` roles with sourced database or literature claims, or remove
them.
