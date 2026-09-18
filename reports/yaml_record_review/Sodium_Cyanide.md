# `data/ingredients/mapped/Sodium_Cyanide.yaml`

**Verdict**: pass.

**Identity**: `Sodium cyanide` maps exactly to active, defining
`CHEBI:33192` / `sodium cyanide`. Fresh OLS4 lookup confirmed the ChEBI label,
formula `CN.Na`, CAS RN `143-33-9`, InChI, InChIKey, and SMILES, and PubChem
resolves the CAS RN to CID `8929` with the same InChI and structure.

**Validation**: `uv run --frozen python scripts/validate_strict.py
data/ingredients/mapped/Sodium_Cyanide.yaml
data/ingredients/mapped/Sodium_D-Lactate.yaml
data/ingredients/mapped/Sodium_Deoxycholate.yaml
data/ingredients/mapped/Sodium_Deoxycholate_Monohydrate.yaml
data/ingredients/mapped/Sodium_Dithionite.yaml` passed for the 5-file batch
with 0 ERROR rows. Direct `linkml-term-validator validate-data` with `--labels`
passed for the four CHEBI-grounded records; `Sodium_D-Lactate` was skipped
because its fallback `cas` grounding is outside the Engine A OBO subset.

**Evidence**: The exact CHEBI identity, CultureBotHT CAS, formula, and
structure fields all agree. Final SSSOM row 2631 maps exactly to `CHEBI:33192`
and exports only `CAS:143-33-9` in `other`. The per-record YAML agrees with the
regenerated aggregate row when keyed by `(preferred_term, mapping_status)`.

**Completeness**: No roles, components, or curated synonyms are asserted, and
none are needed to support this CultureBotHT single-ingredient record.

**Recommended Edits**: None.
