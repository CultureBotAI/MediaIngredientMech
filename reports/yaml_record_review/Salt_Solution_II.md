# `data/ingredients/mapped/Salt_Solution_II.yaml`

**Verdict**: pass.

**Identity**: `Salt Solution II` is intentionally represented as local
`kgmicrobe.ingredient:salt_solution_ii`. Fresh OLS4 search found no exact
public ontology term for this named stock solution, consistent with the #288
fallback-registry review.

**Validation**: `uv run --frozen python scripts/validate_strict.py
data/ingredients/mapped/Salt_Solution_II.yaml
data/ingredients/mapped/Salt_Water.yaml
data/ingredients/mapped/Salts_Solution.yaml
data/ingredients/mapped/Salvinorin_A.yaml
data/ingredients/mapped/Sandramycin.yaml` passed for the 5-file batch with 0
ERROR rows. Direct `linkml-term-validator validate-data` with `--labels`
passed for the OBO-resolvable subset, `Salt_Water`, `Salvinorin_A`, and
`Sandramycin`; the two `kgmicrobe.ingredient` fallback-registry records in
this batch are outside Engine A coverage.

**Evidence**: The #288 manual curation established this as a named
multi-component preparation that should not narrow to a single compound. The
per-record YAML agrees with the regenerated aggregate row when keyed by
`(identifier, preferred_term)`. Final SSSOM row 2554 maps exactly to
`kgmicrobe.ingredient:salt_solution_ii` and exports an empty `other` field.

**Completeness**: The fallback-registry identity, stock-solution type,
occurrence count, and final SSSOM row agree. No roles, components, CAS, or
chemical structure fields are asserted.

**Recommended Edits**: None.
