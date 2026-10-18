# `data/ingredients/mapped/Rhamnose.yaml`

**Verdict**: pass.

**Identity**: `Rhamnose` is an exact MicrobeDecoder lexical grounding to defining
`CHEBI:26546` / `rhamnose`. Fresh OLS4 lookup resolved the ChEBI CURIE, and the
generic mapping is appropriate for the generic source label.

**Validation**: `uv run --frozen python scripts/validate_strict.py
data/ingredients/mapped/Rhamnogalacturonan_I_From_Potato_Pectic_Fiber.yaml
data/ingredients/mapped/Rhamnolipid.yaml data/ingredients/mapped/Rhamnose.yaml
data/ingredients/mapped/Rhodinyl_Acetate.yaml
data/ingredients/mapped/Rhodocladonic_Acid.yaml` passed for the 5-file batch
with 0 ERROR rows. Direct `linkml-term-validator validate-data` with `--labels`
passed for this CHEBI record.

**Evidence**: The per-record YAML agrees with the aggregate
`data/curated/mapped_ingredients.yaml` row. Final SSSOM row 2500 maps exactly to
`CHEBI:26546` with an empty `other` field, and the `manual:review-ingredients`
validation marker matches the MicrobeDecoder review history.

**Completeness**: The exact ChEBI identity, source occurrence, refreshed 2/2
CultureMech occurrence count, and ingredient type are populated. No roles,
components, or unsafe synonyms are asserted.

**Recommended Edits**: None.
