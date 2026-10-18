# `data/ingredients/mapped/Sisomicin_Sulfate_Salt.yaml`

**Verdict**: needs curation, major issues.

**Identity**: `Sisomicin sulfate salt` is a CAS-primary salt record that
currently maps to broad parent `CHEBI:35175` / `sulfate salt`. Fresh PubChem
lookup resolves CAS RN `53179-09-2` to CID 439243 with a formula and InChI
matching the record. Fresh OLS4 lookup by exact CAS RN found no ChEBI xref, but
a label search found active, defining `CHEBI:756083` / `sisomicin sulfate`,
which now supersedes the stale generic sulfate-salt parent.

**Validation**: `uv run --frozen python scripts/validate_strict.py
data/ingredients/mapped/Sio2.yaml
data/ingredients/mapped/Sisomicin_Sulfate_Salt.yaml
data/ingredients/mapped/Skim_milk_powder.yaml
data/ingredients/mapped/Skimmed_Milk.yaml
data/ingredients/mapped/Skirrow_Supplement.yaml` passed for the 5-file batch
with 0 ERROR rows. Direct `linkml-term-validator validate-data` with `--labels`
passed for `Sio2`, `Sisomicin_Sulfate_Salt`, and `Skimmed_Milk`; the MICRO and
kgmicrobe.ingredient records were skipped because those prefixes are outside the
Engine A OBO term-validation subset.

**Evidence**: The exact CAS and kg-microbe registry identity rows and expected
row-review `UNKNOWN_TERM` classifications pass. The per-record YAML agrees with
the regenerated aggregate row when keyed by `(identifier, preferred_term)`.

Two assertions need curation. Final SSSOM row 2593 maps to the generic
`sulfate salt` parent even though current ChEBI now has exact term
`CHEBI:756083` / `sisomicin sulfate`. The `SELECTIVE_AGENT` role is also only a
`COMPUTATIONAL_PREDICTION` from a name pattern, and its curator note explicitly
says the assertion is provisional and needs review.

**Completeness**: Final SSSOM rows 2594-2595 preserve the exact CAS and
kg-microbe registry rows. The ChEBI parent should be promoted to the current
exact sisomicin sulfate term, and the selective-agent role needs source-backed
curation or removal.

**Recommended Edits**: Replace `CHEBI:35175` with exact `CHEBI:756083` in
`data/ingredients/mapped/Sisomicin_Sulfate_Salt.yaml`, update the mapping grade
accordingly, rebuild final SSSOM, and confirm the generic `sulfate salt`
narrow row is gone. Replace the provisional `SELECTIVE_AGENT` role with
source-backed evidence, or remove it if no MediaIngredientMech source supports
using sisomicin sulfate salt as a selective agent.
