# `data/ingredients/mapped/Silver_Chloride.yaml`

**Verdict**: pass.

**Identity**: `silver chloride` maps exactly to active, defining `CHEBI:30341`
/ `silver monochloride`. Fresh OLS4 lookup resolved the ChEBI term, ChEBI lists
`silver(1+) chloride` and `silver(I) chloride` as exact synonyms, and PubChem
resolves CAS RN `7783-90-6` to CID 24561 with an InChI matching the record.

**Validation**: `uv run --frozen python scripts/validate_strict.py
data/ingredients/mapped/Sialyllacto-N-tetraose_D.yaml
data/ingredients/mapped/Siderophore.yaml
data/ingredients/mapped/Silibinin.yaml
data/ingredients/mapped/Silver_Chloride.yaml
data/ingredients/mapped/Silver_Sulfate.yaml` passed for the 5-file batch with 0
ERROR rows. Direct `linkml-term-validator validate-data` with `--labels`
passed for the 3 CHEBI files; `Sialyllacto-N-tetraose_D` and `Silver_Sulfate`
were skipped because `cas` is outside the Engine A OBO term-validation subset.

**Evidence**: The CultureBotHT CAS source, exact CHEBI identity, structure
fields, and reviewed exact synonyms pass. The per-record YAML agrees with the
regenerated aggregate row when keyed by `(identifier, preferred_term)`. Final
SSSOM row 2583 maps exactly to `CHEBI:30341` and exports only the two reviewed
exact synonyms plus `CAS:7783-90-6` in `other`.

**Completeness**: The exact CAS-to-ChEBI identity, CAS field, structure fields,
single-ingredient classification, exact synonyms, and final SSSOM row agree. No
roles or components are asserted.

**Recommended Edits**: None.
