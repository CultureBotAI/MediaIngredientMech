# `data/ingredients/mapped/Proteose_Peptone_No_2.yaml`

**Verdict**: needs curation, major issue.

**Identity**: `Proteose peptone no. 2` is preserved as local `kgmicrobe.ingredient:proteose_peptone_no_2` with a `NARROW_MATCH` parent to defining `MICRO:0000180` / `proteose peptone`. That shape matches the #137 repair: OLS4 still exposes `MICRO:0002393`, but as a non-defining MicrO.owl IRI, while No. 2 remains a distinct catalog-specific peptone.

**Validation**: `uv run --frozen python scripts/validate_strict.py ... Proteose_Peptone_No_2.yaml ...` passed for the 5-file batch with 0 ERROR rows. Direct Engine A term validation was skipped because `MICRO` is intentionally outside the OBO-prefix subset used by `just validate-terms`; OLS4 search confirmed the `MICRO:0000180` parent.

**Evidence**: Final SSSOM rows 2432 and 2433 preserve both sides of the intended mapping: a parent `skos:narrowMatch` to generic proteose peptone and an exact `kgmicrobe.ingredient` identity row for Proteose peptone no. 2. The final `Proteose peptone No 2 (DIFCO 0121-01-3)` token is a curated catalog variant for the same local subject. The active `PROTEIN_SOURCE` role is still only a `COMPUTATIONAL_PREDICTION` from the peptone name pattern with a provisional curator note.

**Completeness**: The identity, parent row, exact local registry row, and seven occurrence counts are complete enough. The remaining gap is the provisional nutritional role.

**Recommended Edits**: In `data/ingredients/mapped/Proteose_Peptone_No_2.yaml`, replace `nutritional_roles.PROTEIN_SOURCE` with source-backed evidence or remove the role. Synchronize `data/curated/mapped_ingredients.yaml`, regenerate any affected products, and rerun strict validation plus `scripts/validate_sssom_invariants.py`.
