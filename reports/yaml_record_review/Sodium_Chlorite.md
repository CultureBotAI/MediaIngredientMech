# `data/ingredients/mapped/Sodium_Chlorite.yaml`

**Verdict**: pass.

**Identity**: `Sodium Chlorite` maps exactly to active, defining
`CHEBI:78667` / `sodium chlorite`. Fresh OLS4 lookup confirmed the ChEBI
label, formula `ClO2.Na`, CAS RN `7758-19-2`, InChI, InChIKey, and SMILES,
and PubChem resolves the CAS RN to CID `23668197` with the same InChI and
structure.

**Validation**: `uv run --frozen python scripts/validate_strict.py
data/ingredients/mapped/Sodium_Carbonate_Solution.yaml
data/ingredients/mapped/Sodium_Chlorite.yaml
data/ingredients/mapped/Sodium_Cholate_Hydrate.yaml
data/ingredients/mapped/Sodium_Chromate.yaml
data/ingredients/mapped/Sodium_Citrate.yaml` passed for the 5-file batch with
0 ERROR rows. Direct `linkml-term-validator validate-data` with `--labels`
passed.

**Evidence**: The exact CHEBI identity, CultureBotHT CAS, formula, and
structure fields all agree. Final SSSOM row 2627 maps exactly to `CHEBI:78667`
and exports only `CAS:7758-19-2` in `other`. The per-record YAML agrees with
the regenerated aggregate row when keyed by `(preferred_term, mapping_status)`.

**Completeness**: No roles, components, or curated synonyms are asserted, and
none are needed to support this CultureBotHT single-ingredient record.

**Recommended Edits**: None.
