# `data/ingredients/mapped/Rosaramicin.yaml`

**Verdict**: pass.

**Identity**: `Rosaramicin` maps exactly to active, defining `CHEBI:87084` /
`rosaramicin`. Fresh OLS4 lookup resolved the ChEBI term with the same formula,
InChI, and SMILES as the record.

**Validation**: `uv run --frozen python scripts/validate_strict.py
data/ingredients/mapped/Rosaramicin.yaml
data/ingredients/mapped/Roseoflavin.yaml
data/ingredients/mapped/Rosmarinic_Acid.yaml
data/ingredients/mapped/Rosuvastatin_Calcium.yaml
data/ingredients/mapped/Rotenone.yaml` passed for the 5-file batch with 0 ERROR
rows. Direct `linkml-term-validator validate-data` with `--labels` passed for
the same 5 files.

**Evidence**: The MicrobeDecoder import, review promotion, and
single-ingredient classification all point at the same exact ChEBI identity.
The per-record YAML agrees with the regenerated aggregate row when keyed by
`(identifier, preferred_term)`. Final SSSOM row 2529 maps exactly to
`CHEBI:87084` and exports an empty `other` field.

**Completeness**: Hidden and ignored inclusive search across `data`, `src`,
`tests`, `mappings`, `scripts`, and `reports` found only expected references to
the Rosaramicin label and `CHEBI:87084`: the live per-record and aggregate
copies, generated indexes, row-review provenance, MicrobeDecoder review row,
and historical backups. No roles, components, or CAS payload are asserted.

**Recommended Edits**: None.
