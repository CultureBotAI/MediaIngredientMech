# `data/ingredients/mapped/Sodium_Chromate.yaml`

**Verdict**: pass.

**Identity**: `Sodium Chromate` maps exactly to active, defining
`CHEBI:78671` / `sodium chromate`. Fresh OLS4 lookup confirmed the ChEBI
label, formula `CrO4.2Na`, CAS RN `7775-11-3`, InChI, InChIKey, SMILES, and
the curated IUPAC synonym, and PubChem resolves the CAS RN to CID `24488` with
the same InChI and structure.

**Validation**: `uv run --frozen python scripts/validate_strict.py
data/ingredients/mapped/Sodium_Carbonate_Solution.yaml
data/ingredients/mapped/Sodium_Chlorite.yaml
data/ingredients/mapped/Sodium_Cholate_Hydrate.yaml
data/ingredients/mapped/Sodium_Chromate.yaml
data/ingredients/mapped/Sodium_Citrate.yaml` passed for the 5-file batch with
0 ERROR rows. Direct `linkml-term-validator validate-data` with `--labels`
passed.

**Evidence**: The exact CHEBI identity, CultureBotHT CAS, formula, structure
fields, IUPAC synonym, and final SSSOM row 2630 pass. The per-record YAML
agrees with the regenerated aggregate row when keyed by `(preferred_term,
mapping_status)`.

**Completeness**: No roles or components are asserted, and none are needed to
support this CultureBotHT single-ingredient record.

**Recommended Edits**: None.
