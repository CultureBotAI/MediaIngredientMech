# `data/ingredients/mapped/Resveratrol.yaml`

**Verdict**: pass.

**Identity**: `Resveratrol` maps exactly to defining `CHEBI:27881` /
`resveratrol`. Fresh OLS4 lookup resolved the ChEBI CURIE, the detailed ChEBI
term annotations match the formula, SMILES, and InChI stored in YAML, and ChEBI
itself cross-references the stored CAS `501-36-0`.

**Validation**: `uv run --frozen python scripts/validate_strict.py
data/ingredients/mapped/Reducing_Agent.yaml data/ingredients/mapped/Resazurin.yaml
data/ingredients/mapped/Resistomycin.yaml data/ingredients/mapped/Resveratrol.yaml
data/ingredients/mapped/Rhamnogalacturonan_From_Soy_Bean_Pectic_Fibre.yaml` passed
for the 5-file batch with 0 ERROR rows. Direct
`linkml-term-validator validate-data` with `--labels` passed for this CHEBI
record.

**Evidence**: The per-record YAML agrees with the aggregate
`data/curated/mapped_ingredients.yaml` row. Final SSSOM row 2496 maps exactly to
`CHEBI:27881` and exports only the ChEBI exact synonym
`5-[2-(4-hydroxyphenyl)ethenyl]benzene-1,3-diol` plus `CAS:501-36-0`.

**Completeness**: The exact ChEBI identity, structure, CAS, ingredient type, and
final SSSOM row agree. No roles or components are asserted.

**Recommended Edits**: None.
