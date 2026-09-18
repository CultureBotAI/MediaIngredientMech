# `data/ingredients/mapped/Sodium_Ferric_EDTA.yaml`

**Verdict**: pass.

**Identity**: `Sodium ferric EDTA` maps to active, defining `CHEBI:78292` /
`sodium feredetate`. Fresh exact OLS4 searches for the CURIE and label resolve
that ChEBI term and confirm the two long IUPAC names retained as exact
synonyms. PubChem resolves CAS RN `15708-41-5` to CID `27461` with formula
`C10H12FeN2NaO8` and the same InChI as the YAML.

**Validation**: `uv run --frozen python scripts/validate_strict.py
data/ingredients/mapped/Sodium_Dodecyl_Sulfate.yaml
data/ingredients/mapped/Sodium_Ethyl_Sulfate.yaml
data/ingredients/mapped/Sodium_Ferric_EDTA.yaml
data/ingredients/mapped/Sodium_Ferulate.yaml
data/ingredients/mapped/Sodium_Fluoroacetate.yaml` passed for the 5-file batch
with 0 ERROR rows. Direct `linkml-term-validator validate-data` with `--labels`
passed.

**Evidence**: The CAS-to-ChEBI identity, formula, and InChI pass. The exported
`FeNa-EDTA`, exact IUPAC synonyms, `FeNa.EDTA` CultureMech surface form, and
`CAS:15708-41-5` all preserve the same sodium ferric EDTA identity in final
SSSOM row 2639. The per-record YAML agrees with the regenerated aggregate row
when keyed by identifier and preferred term.

**Completeness**: The record has no roles needing evidence review, and its
27-occurrence statistics are refreshed from distinct CultureMech recipe ids.
No broader EDTA parent, iron-only, sodium-only, or raw occurrence strings leak
into final SSSOM.

**Recommended Edits**: None.
