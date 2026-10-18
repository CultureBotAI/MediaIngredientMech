# `data/ingredients/mapped/Sebacic_Acid.yaml`

**Verdict**: pass.

**Identity**: `Sebacic acid` maps exactly to active, defining `CHEBI:41865` /
`sebacic acid`. Fresh OLS4 lookup resolved the ChEBI term with the same CAS RN,
formula, InChI, and SMILES as the record, and PubChem also resolved
`111-20-6`.

**Validation**: `uv run --frozen python scripts/validate_strict.py
data/ingredients/mapped/Sea_Water.yaml data/ingredients/mapped/Seawater.yaml
data/ingredients/mapped/Sebacic_Acid.yaml data/ingredients/mapped/Selenate.yaml
data/ingredients/mapped/Selenite.yaml` passed for the 5-file batch with 0
ERROR rows. Direct `linkml-term-validator validate-data` with `--labels`
passed for the same 5 files.

**Evidence**: The CultureBotHT CAS payload `111-20-6` agrees with the active
CHEBI xref and PubChem lookup. The retained `Decanedioic acid` synonym is an
exact OLS4 synonym of `CHEBI:41865`. The per-record YAML agrees with the
regenerated aggregate row when keyed by `(identifier, preferred_term)`. Final
SSSOM row 2567 maps exactly to `CHEBI:41865` and exports
`Decanedioic acid|CAS:111-20-6` in `other`.

**Completeness**: The exact CHEBI identity, CAS, structure fields,
single-ingredient type, curated synonym, and final SSSOM row agree. No roles or
components are asserted.

**Recommended Edits**: None.
