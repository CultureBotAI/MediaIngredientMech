# `data/ingredients/mapped/Rabbit_Serum.yaml`

**Verdict**: pass.

**Identity**: `Rabbit serum` preserves the specific serum identity locally as
`kgmicrobe.ingredient:rabbit_serum` and correctly anchors it to broader
`UBERON:0001977` / `blood serum` with `mapping_quality: NARROW_MATCH`. Fresh
OLS4 lookup resolved the UBERON parent as a defining term, while an exact MICRO
search for `Rabbit serum` returned only non-defining `MICRO:0002392` under the
malformed `MicrO.owl` IRI repaired in #137.

**Validation**: `uv run --frozen python scripts/validate_strict.py
data/ingredients/mapped/Quinoline.yaml
data/ingredients/mapped/R-3-hydroxybutyrate.yaml
data/ingredients/mapped/R2A_agar.yaml
data/ingredients/mapped/Rabbit_Blood.yaml
data/ingredients/mapped/Rabbit_Serum.yaml` passed for the 5-file batch with 0
ERROR rows. Direct `linkml-term-validator validate-data` with `--labels` passed
for the UBERON parent mapping.

**Evidence**: The per-record YAML agrees with the aggregate
`data/curated/mapped_ingredients.yaml` row. Final SSSOM rows 2483 and 2484
publish the required pair: `MIM:Rabbit_Serum skos:narrowMatch UBERON:0001977`
and sibling `MIM:Rabbit_Serum skos:exactMatch
kgmicrobe.ingredient:rabbit_serum`. The `other` fields are empty, so no parent
serum synonym is being exported as though it named rabbit serum exactly.

**Completeness**: The local registry exact row preserves the rabbit-specific
identity lost in the UBERON parent, the Rule B1 sibling row is present, and no
roles, components, or chemical properties are asserted.

**Recommended Edits**: None.
