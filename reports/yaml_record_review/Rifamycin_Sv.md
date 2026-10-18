# `data/ingredients/mapped/Rifamycin_Sv.yaml`

**Verdict**: pass.

**Identity**: `Rifamycin Sv` maps exactly to active, defining `CHEBI:29673` /
`rifamycin SV`. Fresh OLS4 lookup resolved the ChEBI term and matched the YAML
formula, SMILES, and InChI.

**Validation**: `uv run --frozen python scripts/validate_strict.py
data/ingredients/mapped/Rifamycin_B.yaml
data/ingredients/mapped/Rifamycin_O.yaml
data/ingredients/mapped/Rifamycin_S.yaml
data/ingredients/mapped/Rifamycin_Sv.yaml
data/ingredients/mapped/Ristocetin_A.yaml` passed for the 5-file batch with 0
ERROR rows. Direct `linkml-term-validator validate-data` with `--labels` passed
for the same 5 files.

**Evidence**: The per-record YAML agrees with the regenerated aggregate row
when keyed by `(identifier, preferred_term)`. Final SSSOM row 2519 maps exactly
to `CHEBI:29673`, exports an empty `other` field, and carries the
MicrobeDecoder provenance plus `review-ingredients` approval.

**Completeness**: The MicrobeDecoder occurrence provenance, reviewed ChEBI
identity, ingredient type, ChEBI/PubChem structure fields, and final SSSOM row
agree.

**Recommended Edits**: None.
