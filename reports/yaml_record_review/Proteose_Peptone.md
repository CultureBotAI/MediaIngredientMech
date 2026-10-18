# `data/ingredients/mapped/Proteose_Peptone.yaml`

**Verdict**: needs curation, major issue.

**Identity**: `Proteose Peptone` is mapped exactly to defining `MICRO:0000180` / `proteose peptone`, and live OLS4 search resolves that well-formed OBO IRI. The September #137 split correctly removed Proteose Peptone No. 2 surface forms from this generic Proteose Peptone record.

**Validation**: `uv run --frozen python scripts/validate_strict.py ... Proteose_Peptone.yaml ...` passed for the 5-file batch with 0 ERROR rows. Direct Engine A term validation was skipped because `MICRO` is intentionally outside the OBO-prefix subset used by `just validate-terms`; prefix-specific OLS4 search still resolved `MICRO:0000180`.

**Evidence**: Final SSSOM row 2431 keeps the exact MICRO row and the Proteose Peptone No. 3 catalog variants that remain curated on the generic record. It also still exports `Peptic digest of animal tissue` as `other`; live OLS4 reports that phrase as a broad synonym of `MICRO:0000180`, and an ignored/hidden local search over `data/ingredients`, `data/curated`, `mappings`, `reports`, `src`, `tests`, `docs`, and `UNIFIED_INGREDIENT_MAPPING.tsv` found the cross-repo unified snapshot mapping the same surface to the separate generic peptone term `MICRO:0000178`. The active `PROTEIN_SOURCE` role is also only a `COMPUTATIONAL_PREDICTION` from the peptone name pattern with a provisional curator note.

**Completeness**: The exact MICRO grounding and occurrence refresh are complete enough, but the broad peptic-digest label should not be published as an exact synonym for Proteose Peptone and the protein-source role still needs source-backed evidence.

**Recommended Edits**: In `data/ingredients/mapped/Proteose_Peptone.yaml`, either demote `Peptic digest of animal tissue` to non-published provenance or re-evaluate that absorbed source surface against generic peptone `MICRO:0000178`. Replace the provisional `PROTEIN_SOURCE` role with source-backed evidence or remove it. Synchronize `data/curated/mapped_ingredients.yaml`, regenerate SSSOM, and rerun strict validation plus `scripts/validate_sssom_invariants.py`.
