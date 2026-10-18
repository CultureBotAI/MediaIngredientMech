# `data/ingredients/mapped/Serotonin.yaml`

**Verdict**: pass.

**Identity**: `Serotonin` maps exactly to active, defining `CHEBI:28790` /
`serotonin`. Fresh OLS4 lookup resolved the ChEBI term with the same CAS RN,
formula, InChI, and SMILES as the record, and PubChem also resolved `50-67-9`.

**Validation**: `uv run --frozen python scripts/validate_strict.py
data/ingredients/mapped/Serine.yaml
data/ingredients/mapped/Serine_Hydroxamate.yaml
data/ingredients/mapped/Serotonin.yaml data/ingredients/mapped/Serum.yaml
data/ingredients/mapped/Setamycin.yaml` passed for the 5-file batch with 0
ERROR rows. Direct `linkml-term-validator validate-data` with `--labels`
passed for the same 5 files.

**Evidence**: The CultureBotHT CAS payload `50-67-9` agrees with the active
CHEBI xref and PubChem lookup. The retained
`3-(2-Aminoethyl)-1H-indol-5-ol` synonym is an exact OLS4 synonym of
`CHEBI:28790`. The per-record YAML agrees with the regenerated aggregate row
when keyed by `(identifier, preferred_term)`. Final SSSOM row 2572 maps exactly
to `CHEBI:28790` and exports `3-(2-Aminoethyl)-1H-indol-5-ol|CAS:50-67-9` in
`other`.

**Completeness**: The exact CHEBI identity, CAS, structure fields,
single-ingredient type, curated synonym, and final SSSOM row agree. No roles or
components are asserted.

**Recommended Edits**: None.
