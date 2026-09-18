# `data/ingredients/mapped/Salts_Solution.yaml`

**Verdict**: needs curation, major issue.

**Identity**: `Salts solution` is intentionally represented as local
`kgmicrobe.ingredient:salts_solution`. Fresh OLS4 search found only broader or
named salt-solution alternatives, not an exact public ontology term for this
generic stock-solution record, so the #288 fallback-registry grounding remains
appropriate.

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

**Evidence**: The per-record YAML agrees with the regenerated aggregate row
when keyed by `(identifier, preferred_term)`. Final SSSOM row 2556 maps
exactly to `kgmicrobe.ingredient:salts_solution`, but it exports
`Salts solution***` in `other`.

That `other` value is the raw CultureMech occurrence-table surface form with
trailing markup, not a real synonym of the local concept. It should not be in
the final SSSOM `other` column.

**Completeness**: The fallback-registry identity, stock-solution type, and
occurrence count agree. The final SSSOM synonym payload does not: it still
contains a footnote-marked alias.

**Recommended Edits**: Remove or non-publish the `Salts solution***` raw
synonym, or teach `src/mediaingredientmech/synonym_policy.py` to reject
trailing asterisk markup before `ingredient_mappings.sssom.tsv` is generated.
