# `data/ingredients/mapped/Resistomycin.yaml`

**Verdict**: pass.

**Identity**: `Resistomycin` is an exact MicrobeDecoder lexical grounding to
defining `CHEBI:29671` / `Resistomycin`. Fresh OLS4 lookup resolved the ChEBI
CURIE, and the detailed ChEBI term annotations match the formula, SMILES, and
InChI stored in YAML.

**Validation**: `uv run --frozen python scripts/validate_strict.py
data/ingredients/mapped/Reducing_Agent.yaml data/ingredients/mapped/Resazurin.yaml
data/ingredients/mapped/Resistomycin.yaml data/ingredients/mapped/Resveratrol.yaml
data/ingredients/mapped/Rhamnogalacturonan_From_Soy_Bean_Pectic_Fibre.yaml` passed
for the 5-file batch with 0 ERROR rows. Direct
`linkml-term-validator validate-data` with `--labels` passed for this CHEBI
record.

**Evidence**: The per-record YAML agrees with the aggregate
`data/curated/mapped_ingredients.yaml` row. Final SSSOM row 2495 maps exactly to
`CHEBI:29671` and has an empty `other` field. The MicrobeDecoder source
occurrence and `manual:review-ingredients|APPROVED|2026-08-04` SSSOM marker
agree with the import and review history.

**Completeness**: The exact identity, structure, source occurrence, and
ingredient type are populated; no roles, components, or extra synonyms are
asserted.

**Recommended Edits**: None.
