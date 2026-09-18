# `data/ingredients/mapped/Planctomyces_vitamin_mix.yaml`

**Verdict**: needs curation, major issue.

**Identity**: `Planctomyces_vitamin_mix` is modeled as a named Planctomyces vitamin stock solution with the local exact identifier `kgmicrobe.ingredient:planctomyces_vitamin_mix`. The identifier, preferred term, `STOCK_SOLUTION` / `VITAMIN_MIX` classification, fallback `kgmicrobe.ingredient` mapping, and row-2346 final SSSOM exact row agree. The final SSSOM row has no `other` tokens, so it does not publish the duplicate raw label as an extra synonym.

**Validation**: `uv run --frozen python scripts/validate_strict.py ... Planctomyces_vitamin_mix.yaml ...` passed for the 5-file batch with 0 ERROR rows. Engine A term validation was skipped intentionally because `kgmicrobe.ingredient` is a non-OBO local registry prefix covered by product validation rather than `linkml-term-validator` OAK lookup.

**Evidence**: The `FALLBACK_REGISTRY` evidence and `promote_resolved_unmapped` history support keeping a local registry identity for a named lab preparation that had no exact CHEBI, NCIT, MeSH, FOODON, or ENVO term in the recorded review. The raw CultureBotHT occurrence is traceable to one `Planctomyces_medium_DSMZ1560` use. An ignored/hidden local search over `data/ingredients`, `data/curated`, `mappings`, `reports`, `scripts`, `src`, `tests`, `docs`, and `UNIFIED_INGREDIENT_MAPPING.tsv` found the expected curated, generated, audit, and final SSSOM references for this local identifier.

**Completeness**: The record itself documents that this is a multi-component vitamin stock and that component-level recipe curation was still pending, but it was promoted to `MAPPED` with no `components` block. That leaves the stock solution exact identity incomplete: downstream consumers can recover that the mixture exists, but not the vitamins and concentrations that define it.

**Recommended Edits**: Add a source-backed `components` block for the vitamin-stock recipe in `data/ingredients/mapped/Planctomyces_vitamin_mix.yaml`, then synchronize `data/curated/mapped_ingredients.yaml` from the individual record. Re-run `scripts/validate_strict.py`, `scripts/validate_component_partonomy.py`, the SSSOM invariant check, and the flat export coverage check to prove the component partonomy and generated exports remain consistent.
