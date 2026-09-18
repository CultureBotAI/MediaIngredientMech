# `data/ingredients/mapped/Potassium_2-ketogluconate.yaml`

**Verdict**: needs curation, major issue.

**Identity**: `Potassium 2-ketogluconate` is preserved as the local exact salt identity `kgmicrobe.compound:potassium_2-ketogluconate` with a `NARROW_MATCH` parent mapping to `CHEBI:16808` / `2-dehydro-D-gluconate`. The salt-vs-anion row shape is correct on its own, and final SSSOM rows 2381 and 2382 correctly pair the CHEBI parent row with a KG-Microbe exact identity row.

**Validation**: `uv run --frozen python scripts/validate_strict.py ... Potassium_2-ketogluconate.yaml ...` passed for the 5-file batch with 0 ERROR rows. `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Potassium_2-ketogluconate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels` passed.

**Evidence**: The #213 evidence explicitly equates 2-ketogluconate with 2-dehydro-D-gluconate, but the equivalent `Potassium_2-dehydro-D-gluconate` record remains active under a separate local exact ID. An ignored/hidden local search over `data/ingredients`, `data/curated`, `mappings`, `reports`, `scripts`, `src`, `tests`, `docs`, and `UNIFIED_INGREDIENT_MAPPING.tsv` found both exact registry rows and their shared parent rows in the final SSSOM.

**Completeness**: The salt's CHEBI parent and exact KG-Microbe row are complete enough, but the duplicate active local salt identity leaves equivalent MicrobeDecoder source labels split across two MIM subjects.

**Recommended Edits**: Merge or alias `data/ingredients/mapped/Potassium_2-ketogluconate.yaml` and `data/ingredients/mapped/Potassium_2-dehydro-D-gluconate.yaml` under one exact KG-Microbe registry subject, unless a curator can document a stereochemical distinction that makes them different salts. Regenerate SSSOM and re-run `scripts/validate_sssom_invariants.py` to prove one exact identity row remains for this salt.
