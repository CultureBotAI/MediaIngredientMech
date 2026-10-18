# `data/ingredients/mapped/Sialyllacto-N-tetraose_C.yaml`

**Verdict**: needs curation, major issue.

**Identity**: `Sialyllacto-N-tetraose c` maps exactly to active, defining
`CHEBI:89905` / `Sialyllacto-N-neotetraose c`. Fresh OLS4 lookup resolved the
ChEBI term, and its CAS RN `64003-55-0`, formula, InChI, and PubChem CID
131882577 all agree with the record.

**Validation**: `uv run --frozen python scripts/validate_strict.py
data/ingredients/mapped/Sheep_blood.yaml
data/ingredients/mapped/Shikimic_Acid.yaml
data/ingredients/mapped/Showdomycin.yaml
data/ingredients/mapped/Sialyllacto-N-tetraose_A.yaml
data/ingredients/mapped/Sialyllacto-N-tetraose_C.yaml` passed for the 5-file
batch with 0 ERROR rows. Direct `linkml-term-validator validate-data` with
`--labels` passed for the 4 CHEBI files; `Sheep_blood` was skipped because
`MICRO` is outside the Engine A CHEBI/OBO term-validation subset.

**Evidence**: The CultureBotHT CAS source, exact CHEBI identity, CAS field, and
structure fields pass. The per-record YAML agrees with the regenerated
aggregate row when keyed by `(identifier, preferred_term)`. Final SSSOM row
2579 maps exactly to `CHEBI:89905` and exports only `CAS:64003-55-0` in
`other`.

The remaining issue is the `CARBON_SOURCE` role. It was inferred from ChEBI
ancestry, its only evidence is `COMPUTATIONAL_PREDICTION`, and its curator note
explicitly says the assertion is provisional and needs review. That is not
enough source support for a nutritional role.

**Completeness**: The exact CAS-to-ChEBI identity, CAS field, structure fields,
and final SSSOM row agree. The carbon-source role needs source-backed curation
or removal.

**Recommended Edits**: Replace the provisional `CARBON_SOURCE` role with
source-backed evidence, or remove it if no MediaIngredientMech source supports
using sialyllacto-N-tetraose c as a carbon source.
