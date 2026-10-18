# `data/ingredients/mapped/Silibinin.yaml`

**Verdict**: pass.

**Identity**: `Silibinin` maps exactly to active, defining `CHEBI:9144` /
`silibinin`. Fresh OLS4 lookup resolved the ChEBI term, its exact synonym list
contains the long systematic synonym stored in the YAML, and PubChem resolves
CAS RN `22888-70-6` to CID 31553 with a formula and InChI matching the record.

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
fields, and reviewed exact synonym pass. The per-record YAML agrees with the
regenerated aggregate row when keyed by `(identifier, preferred_term)`. Final
SSSOM row 2582 maps exactly to `CHEBI:9144` and exports the reviewed exact
synonym plus `CAS:22888-70-6` in `other`.

**Completeness**: The exact CHEBI identity, CAS field, structure fields, exact
synonym, single-ingredient classification, and final SSSOM row agree. No roles
or components are asserted.

**Recommended Edits**: None.
