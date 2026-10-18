# `data/ingredients/mapped/Rye-bran.yaml`

**Verdict**: pass.

**Identity**: `Rye-bran` maps by normalized synonym match to active, defining
`FOODON:03311582` / `rye bran`. Fresh OLS4 lookup resolved the FOODON term with
the same canonical label.

**Validation**: `uv run --frozen python scripts/validate_strict.py
data/ingredients/mapped/Rutilantinone.yaml
data/ingredients/mapped/Rutin.yaml data/ingredients/mapped/Rye-bran.yaml
data/ingredients/mapped/S-3-hydroxybutyrate.yaml
data/ingredients/mapped/S-adenosyl_Homocysteine.yaml` passed for the 5-file
batch with 0 ERROR rows. Direct `linkml-term-validator validate-data` with
`--labels` crashed on CAS-primary rows in the mixed batch; rerunning it on this
batch's CHEBI/FOODON subset passed.

**Evidence**: The CultureMech residual grounding records two `Rye-bran`
mentions mapped to `FOODON:03311582`, and the later alias backfill records the
raw one-mention `Rye--bran` surface that folds to the same label. The
per-record YAML agrees with the regenerated aggregate row when keyed by
`(identifier, preferred_term)`. Final SSSOM row 2541 maps exactly to
`FOODON:03311582` and exports only the raw CultureMech `Rye--bran` surface.

**Completeness**: The FOODON identity, CultureMech evidence restoration,
occurrence count, raw alias, and final SSSOM row agree. No roles, components, or
chemical properties are asserted.

**Recommended Edits**: None.
