# `data/ingredients/mapped/Salicylic_Acid.yaml`

**Verdict**: pass.

**Identity**: `Salicylic acid` maps exactly to active, defining `CHEBI:16914`
/ `salicylic acid`. Fresh OLS4 lookup resolved the ChEBI term with the same
CAS RN, formula, InChI, and SMILES as the record.

**Validation**: `uv run --frozen python scripts/validate_strict.py
data/ingredients/mapped/Salicylate.yaml
data/ingredients/mapped/Salicylic_Acid.yaml
data/ingredients/mapped/Salidroside.yaml
data/ingredients/mapped/Salinomycin.yaml
data/ingredients/mapped/Salsoline.yaml` passed for the 5-file batch with 0
ERROR rows. Direct `linkml-term-validator validate-data` with `--labels`
passed for the same 5 files.

**Evidence**: The CultureBotHT CAS payload `69-72-7` agrees with the active
ChEBI xref and PubChem lookup. The retained exact synonym
`2-HYDROXYBENZOIC ACID` is an exact OLS4 synonym of `CHEBI:16914`, and the
per-record YAML agrees with the regenerated aggregate row when keyed by
`(identifier, preferred_term)`. Final SSSOM row 2550 maps exactly to
`CHEBI:16914` and exports `2-HYDROXYBENZOIC ACID|CAS:69-72-7` in `other`.

**Completeness**: The exact CHEBI identity, CAS, structure fields,
single-ingredient type, and final SSSOM row agree. No roles or components are
asserted.

**Recommended Edits**: None.
