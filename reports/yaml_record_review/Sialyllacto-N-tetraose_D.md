# `data/ingredients/mapped/Sialyllacto-N-tetraose_D.yaml`

**Verdict**: needs curation, major issue.

**Identity**: `Sialyllacto-N-tetraose d` maps to local fallback registry
identifier `cas:100789-83-1`. Fresh PubChem lookup resolves CAS RN
`100789-83-1` to CID 9963175, and PubChem's formula and InChI agree with the
record. Fresh OLS4 searches by the CAS RN and label found no exact ChEBI term
for the d isomer; the row-review `UNKNOWN_TERM` result is therefore expected
CAS registry coverage, not a missing ChEBI repair.

**Validation**: `uv run --frozen python scripts/validate_strict.py
data/ingredients/mapped/Sialyllacto-N-tetraose_D.yaml
data/ingredients/mapped/Siderophore.yaml
data/ingredients/mapped/Silibinin.yaml
data/ingredients/mapped/Silver_Chloride.yaml
data/ingredients/mapped/Silver_Sulfate.yaml` passed for the 5-file batch with 0
ERROR rows. Direct `linkml-term-validator validate-data` with `--labels`
passed for the 3 CHEBI files; `Sialyllacto-N-tetraose_D` and `Silver_Sulfate`
were skipped because `cas` is outside the Engine A OBO term-validation subset.

**Evidence**: The CultureBotHT CAS source, CAS fallback identity, PubChem
structure fields, expected row-review `UNKNOWN_TERM` classification, and final
SSSOM row pass. The per-record YAML agrees with the regenerated aggregate row
when keyed by `(identifier, preferred_term)`. Final SSSOM row 2580 maps exactly
to `cas:100789-83-1` and exports only `CAS:100789-83-1` in `other`.

The remaining issue is the `CARBON_SOURCE` role. It was inferred from a name
pattern, its only evidence is `COMPUTATIONAL_PREDICTION`, and its curator note
explicitly says the assertion is provisional and needs review. That is not
enough source support for a nutritional role.

**Completeness**: The CAS fallback identity, PubChem structure fields, and
final SSSOM row agree. The carbon-source role needs source-backed curation or
removal.

**Recommended Edits**: Replace the provisional `CARBON_SOURCE` role with
source-backed evidence, or remove it if no MediaIngredientMech source supports
using sialyllacto-N-tetraose d as a carbon source.
