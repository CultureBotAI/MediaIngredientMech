# `data/ingredients/mapped/Sodium_Azide.yaml`

**Verdict**: pass.

**Identity**: `Sodium azide` maps exactly to active, defining `CHEBI:278547` /
`sodium azide`. Fresh OLS4 lookup confirmed the ChEBI label, formula `N3.Na`,
CAS RN `26628-22-8`, InChI, InChIKey, and SMILES, and PubChem resolves the CAS
RN to CID `33557` with the same InChI and structure.

**Validation**: `uv run --frozen python scripts/validate_strict.py
data/ingredients/mapped/Sodium_Antimonate.yaml
data/ingredients/mapped/Sodium_Azide.yaml
data/ingredients/mapped/Sodium_Beta-glycerophosphate.yaml
data/ingredients/mapped/Sodium_Bromate.yaml
data/ingredients/mapped/Sodium_Carbonate_Monohydrate.yaml` passed for the
5-file batch with 0 ERROR rows. Direct `linkml-term-validator validate-data`
with `--labels` passed.

**Evidence**: The exact CHEBI identity, CAS, formula, and structure fields all
agree. Final SSSOM row 2621 maps exactly to `CHEBI:278547` and exports only
`CAS:26628-22-8` in `other`. The per-record YAML agrees with the regenerated
aggregate row when keyed by `(preferred_term, mapping_status)`.

**Completeness**: No roles, components, or curated synonyms are asserted, and
none are needed to support this CultureBotHT single-ingredient record.

**Recommended Edits**: None.
