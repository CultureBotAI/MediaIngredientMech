# `data/ingredients/mapped/Filtered_Seawater.yaml`

## Verdict

Needs curation, with a major final-SSSOM synonym issue. The MICRO identity,
undefined-mixture type, occurrence counts, and sea-water natural-source context
are coherent, but final SSSOM exports natural-seawater labels as exact synonyms
of filtered seawater.

## Identity

- Reviewed record: `data/ingredients/mapped/Filtered_Seawater.yaml`.
- Identifier and grounding: `identifier: MICRO:0001773` with matching
  `ontology_mapping.ontology_id`, label `filtered seawater`, source `MICRO`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: UNDEFINED_MIXTURE`.
- EBI OLS for MICRO resolves `MICRO:0001773` as `filtered seawater`, marks it
  non-obsolete, and defines it as an undefined inorganic mixture derived by
  filtering natural seawater.
- `environmental_context` links the record to `ENVO:00002149` with relevance
  `NATURAL_SOURCE`, which matches the MICRO definition's natural-seawater
  source.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Fildes_Enrichment.yaml data/ingredients/mapped/Filipin.yaml data/ingredients/mapped/Filtered_Seawater.yaml data/ingredients/mapped/Fish-sperm_Dna.yaml data/ingredients/mapped/Fish_peptone.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Filtered_Seawater.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  failed in the local MICRO validation path; prefix-specific EBI OLS resolved
  the exact MICRO CURIE and label.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 skipped because the
  sibling kg-microbe ontology transforms are not checked out.

## Evidence

- The matching `data/curated/mapped_ingredients.yaml` entry carries the same
  MICRO identifier, synonyms, occurrence counts, ingredient type, and
  environmental context as the per-record YAML.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:Filtered_Seawater` to `MICRO:0001773` with `skos:exactMatch`.
- `mappings/ingredient_mappings_external_prefix_ols_validation.tsv` resolves
  `MICRO:0001773` exactly through prefix-specific EBI OLS; the older
  `UNKNOWN_TERM` row in `mappings/ingredient_mappings_oak_ols_review.tsv` was
  a validator-prefix coverage gap, not a bad identifier.
- Major: the final SSSOM `other` column exports `Natural seawater` and
  `Natural seawater (filtered, 95% strength)` as exact synonyms. The first
  token drops the filtering state that defines this MICRO term, and the second
  carries a `95% strength` preparation detail that belongs to the recipe rather
  than to the ingredient identity.
- `mappings/culturemech_residual_triage.tsv` leaves `Natural seawater
  (filtrated)` unresolved, so not every natural-seawater surface has been
  intentionally accepted as a filtered-seawater synonym.
- A hidden/ignored-inclusive search over `data/ingredients`, `data/curated`,
  `mappings`, `scripts`, `src`, `tests`, and `reports`, excluding prior
  per-record reports, aggregate backups, and the final SSSOM TSV, found the
  active YAML, aggregate copy, MICRO OLS validation rows, the #260 gap-label
  rule, natural-seawater residual triage, occurrence membership, and ignored
  historical batch reports.

## Completeness

- The exact MICRO identity, undefined-mixture type, occurrence counts, and
  natural-source environment assertion are populated.
- The final SSSOM synonym payload needs filtering for natural-seawater labels
  that do not exactly denote filtered seawater.

## Recommended Edits

- Major: retype or remove `Natural seawater` and `Natural seawater (filtered,
  95% strength)` in `data/ingredients/mapped/Filtered_Seawater.yaml` so
  generic source-water and strength/dilution text no longer export as exact
  synonyms, sync `data/curated/mapped_ingredients.yaml`, regenerate
  `mappings/ingredient_mappings.sssom.tsv`, and rerun strict validation plus
  the final SSSOM invariant gates.
