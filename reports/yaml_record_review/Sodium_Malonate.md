# `data/ingredients/mapped/Sodium_Malonate.yaml`

**Verdict**: pass.

**Identity**: `Sodium Malonate` maps exactly to active, defining
`CHEBI:62983` / `sodium malonate`. Fresh OLS4 lookup confirmed the ChEBI label,
formula `C3H2O4.2Na`, InChI, InChIKey, SMILES, and disodium-malonate synonym
set.

**Validation**: `uv run --frozen python scripts/validate_strict.py
data/ingredients/mapped/Sodium_Malonate.yaml
data/ingredients/mapped/Sodium_Metasilicate.yaml
data/ingredients/mapped/Sodium_Metasilicate_Silicate_For_Diatom_Frustules.yaml
data/ingredients/mapped/Sodium_Methanesulfonate.yaml
data/ingredients/mapped/Sodium_Nitrate_070_M_Stock.yaml` passed for the
5-file batch with 0 ERROR rows. Direct `linkml-term-validator validate-data`
with `--labels` passed.

**Evidence**: The MicrobeDecoder exact ChEBI import, reviewed promotion,
formula, InChI, and SMILES pass. Final SSSOM row 2657 exports no local `other`
tokens, so there are no unsupported synonyms to review. The per-record YAML
agrees with the regenerated aggregate row when keyed by identifier and
preferred term.

**Completeness**: The record has no roles needing evidence review and no
unsafe synonyms in final SSSOM.

**Recommended Edits**: None.
