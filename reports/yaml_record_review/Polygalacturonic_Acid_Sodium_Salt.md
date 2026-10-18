# `data/ingredients/mapped/Polygalacturonic_Acid_Sodium_Salt.yaml`

**Verdict**: needs curation, major issue.

**Identity**: `Polygalacturonic acid sodium salt` is preserved as `cas:9049-37-0` with a parent `NARROW_MATCH` to `CHEBI:62969` / `polygalacturonic acid`. A fresh exact CHEBI OLS lookup found no sodium-salt term, so the CAS identity plus parent mapping remains the right shape, and final SSSOM rows 2366 and 2367 correctly preserve exact CAS and KG-Microbe registry rows alongside the parent row.

**Validation**: `uv run --frozen python scripts/validate_strict.py ... Polygalacturonic_Acid_Sodium_Salt.yaml ...` passed for the 5-file batch with 0 ERROR rows. `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Polygalacturonic_Acid_Sodium_Salt.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels` passed, confirming the stored CHEBI parent label.

**Evidence**: `Sodium pectate` is a valid same-form synonym for the CAS sodium-salt subject, and `CAS:9049-37-0` is allowed on the registry exact rows because it matches `chemical_properties.cas_rn`. The bare `autoclaved` synonym recovered from previous SSSOM `other` content is only process text, not a substance label, and it is still exported in row 2365. The stored formula, InChI, and SMILES were copied from the neutral `CHEBI:62969` parent and do not include sodium; a PubChem lookup by CAS `9049-37-0` returned no CID to corroborate those structure fields for the sodium salt. An ignored/hidden local search over `data/ingredients`, `data/curated`, `mappings`, `reports`, `scripts`, `src`, `tests`, `docs`, and `UNIFIED_INGREDIENT_MAPPING.tsv` found the expected parent, registry sibling, row-review, and final SSSOM rows.

**Completeness**: The salt-specific identity is represented in registry rows, but the active chemical properties describe the parent acid rather than a sodium-salt structure.

**Recommended Edits**: In `data/ingredients/mapped/Polygalacturonic_Acid_Sodium_Salt.yaml`, remove or replace the inherited acid formula, InChI, and SMILES with source-backed sodium-salt chemistry; remove `autoclaved` from active synonyms or move it to filtered provenance. Synchronize `data/curated/mapped_ingredients.yaml`, regenerate SSSOM, and rerun strict validation plus `scripts/validate_sssom_invariants.py`.
