# `data/ingredients/mapped/Potassium_5-dehydro-D-gluconate.yaml`

**Verdict**: needs curation, major issue.

**Identity**: `Potassium 5-dehydro-D-gluconate` is preserved as the local exact salt identity `kgmicrobe.compound:potassium_5-dehydro-d-gluconate` with a `NARROW_MATCH` parent mapping to `CHEBI:58143` / `5-dehydro-D-gluconate`. The salt-vs-anion row shape is correct on its own, and final SSSOM rows 2384 and 2385 correctly pair the CHEBI parent row with a KG-Microbe exact identity row.

**Validation**: `uv run --frozen python scripts/validate_strict.py ... Potassium_5-dehydro-D-gluconate.yaml ...` passed for the 5-file batch with 0 ERROR rows. `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Potassium_5-dehydro-D-gluconate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels` passed.

**Evidence**: The #213 evidence supports keeping a local registry identity because CHEBI has the anion but not the potassium salt. The immediately adjacent active `data/ingredients/mapped/Potassium_5-ketogluconate.yaml` record asserts the same potassium salt of `5-dehydro-D-gluconate` under a second local exact ID. An ignored/hidden local search over `data/ingredients`, `data/curated`, `mappings`, `reports`, `scripts`, `src`, `tests`, `docs`, and `UNIFIED_INGREDIENT_MAPPING.tsv` found both exact registry rows and their shared parent rows in the final SSSOM.

**Completeness**: The salt's CHEBI parent and exact KG-Microbe row are complete enough, but the duplicate active local salt identity leaves equivalent MicrobeDecoder source labels split across two MIM subjects.

**Recommended Edits**: Merge or alias `data/ingredients/mapped/Potassium_5-dehydro-D-gluconate.yaml` and `data/ingredients/mapped/Potassium_5-ketogluconate.yaml` under one exact KG-Microbe registry subject, unless a curator can document a stereochemical distinction that makes them different salts. Regenerate SSSOM and re-run `scripts/validate_sssom_invariants.py` to prove one exact identity row remains for this salt.
