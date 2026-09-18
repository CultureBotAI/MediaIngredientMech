# `data/ingredients/mapped/Reducing_Agent.yaml`

**Verdict**: needs curation, major issue.

**Identity**: `Reducing Agent` is exact-mapped to defining `CHEBI:63247` /
`reducing agent`, but that ChEBI term denotes the generic class of electron
donors in redox reactions. It is a role-like class of possible chemicals, not a
single distinct supplied substance, salt, mixture, or stock solution.

**Validation**: `uv run --frozen python scripts/validate_strict.py
data/ingredients/mapped/Reducing_Agent.yaml data/ingredients/mapped/Resazurin.yaml
data/ingredients/mapped/Resistomycin.yaml data/ingredients/mapped/Resveratrol.yaml
data/ingredients/mapped/Rhamnogalacturonan_From_Soy_Bean_Pectic_Fibre.yaml` passed
for the 5-file batch with 0 ERROR rows. Direct
`linkml-term-validator validate-data` with `--labels` passed for the ChEBI id
and label, but that validates label correspondence rather than ingredient-level
specificity.

**Evidence**: The per-record YAML agrees with the aggregate
`data/curated/mapped_ingredients.yaml` row. Final SSSOM row 2493 publishes a
`skos:exactMatch` from `MIM:Reducing_Agent` to `CHEBI:63247` with empty `other`.
The structured evidence only proves that a CultureMech residual used the generic
surface form `reducing agent`; it does not prove a concrete reducing compound
or solution identity.

**Completeness**: No roles, components, supplied forms, or chemical properties
are present that would make the generic residual reproducible as a medium
component.

**Recommended Edits**: Replace the exact ChEBI role-class grounding with a local
stock or unresolved placeholder that preserves the vague CultureMech label, then
keep `CHEBI:63247` only as role semantics if later evidence identifies an
actual reducing-agent component.
