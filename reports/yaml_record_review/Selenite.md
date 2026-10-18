# `data/ingredients/mapped/Selenite.yaml`

**Verdict**: pass.

**Identity**: `Selenite` maps by exact synonym to active, defining
`CHEBI:18212` / `selenite(2-)`. Fresh OLS4 lookup resolved the ChEBI term with
the same formula, InChI, and SMILES as the record, and still lists `Selenite`
as an exact synonym.

**Validation**: `uv run --frozen python scripts/validate_strict.py
data/ingredients/mapped/Sea_Water.yaml data/ingredients/mapped/Seawater.yaml
data/ingredients/mapped/Sebacic_Acid.yaml data/ingredients/mapped/Selenate.yaml
data/ingredients/mapped/Selenite.yaml` passed for the 5-file batch with 0
ERROR rows. Direct `linkml-term-validator validate-data` with `--labels`
passed for the same 5 files.

**Evidence**: The MicrobeDecoder residual promotion records the exact
selenite-to-`CHEBI:18212` synonym match that the fresh OLS4 lookup still
confirms. The per-record YAML agrees with the regenerated aggregate row when
keyed by `(identifier, preferred_term)`. Final SSSOM row 2569 maps exactly to
`CHEBI:18212` and exports an empty `other` field.

**Completeness**: The exact-synonym CHEBI identity, structure, MicrobeDecoder
source occurrence count, and final SSSOM row agree. No roles, components, CAS,
or curated synonyms are asserted.

**Recommended Edits**: None.
