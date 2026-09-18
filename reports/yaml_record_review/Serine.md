# `data/ingredients/mapped/Serine.yaml`

**Verdict**: pass.

**Identity**: `Serine` maps exactly to active, defining `CHEBI:17822` /
`serine`. Fresh OLS4 lookup resolved the ChEBI term with the same formula,
InChI, and SMILES as the record.

**Validation**: `uv run --frozen python scripts/validate_strict.py
data/ingredients/mapped/Serine.yaml
data/ingredients/mapped/Serine_Hydroxamate.yaml
data/ingredients/mapped/Serotonin.yaml data/ingredients/mapped/Serum.yaml
data/ingredients/mapped/Setamycin.yaml` passed for the 5-file batch with 0
ERROR rows. Direct `linkml-term-validator validate-data` with `--labels`
passed for the same 5 files.

**Evidence**: The MicrobeDecoder exact-label import, review promotion,
single-ingredient classification, and CultureMech occurrence refresh all point
at the same exact CHEBI identity. The per-record YAML agrees with the
regenerated aggregate row when keyed by `(identifier, preferred_term)`. Final
SSSOM row 2570 maps exactly to `CHEBI:17822` and exports an empty `other`
field.

**Completeness**: The exact CHEBI identity, structure, MicrobeDecoder source
occurrence count, CultureMech occurrence count, and final SSSOM row agree. No
roles, components, CAS, or curated synonyms are asserted.

**Recommended Edits**: None.
