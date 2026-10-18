# `data/ingredients/mapped/Fish_peptone.yaml`

## Verdict

Needs curation, with a major unsupported-role issue. The record maps exactly to
the MICRO fish peptone term and its undefined-mixture type is appropriate, but
`nutritional_roles.PROTEIN_SOURCE` is still only a provisional name-pattern
inference.

## Identity

- Reviewed record: `data/ingredients/mapped/Fish_peptone.yaml`.
- Identifier and grounding: `identifier: MICRO:0000462` with matching
  `ontology_mapping.ontology_id`, label `fish peptone`, source `MICRO`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: UNDEFINED_MIXTURE`.
- EBI OLS for MICRO resolves `MICRO:0000462` as `fish peptone`, marks it
  non-obsolete, and defines it as an enzymatic hydrolysate of protein derived
  from fish of unspecified origin.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Fildes_Enrichment.yaml data/ingredients/mapped/Filipin.yaml data/ingredients/mapped/Filtered_Seawater.yaml data/ingredients/mapped/Fish-sperm_Dna.yaml data/ingredients/mapped/Fish_peptone.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Fish_peptone.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  failed in the local MICRO validation path; prefix-specific EBI OLS resolved
  the exact MICRO CURIE and label.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 skipped because the
  sibling kg-microbe ontology transforms are not checked out.

## Evidence

- The matching `data/curated/mapped_ingredients.yaml` entry carries the same
  MICRO identifier, occurrence counts, ingredient type, and provisional role
  evidence as the per-record YAML.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:Fish_peptone` to `MICRO:0000462` with `skos:exactMatch` and an empty
  `other` column.
- `mappings/ingredient_mappings_external_prefix_ols_validation.tsv` resolves
  `MICRO:0000462` exactly through prefix-specific EBI OLS; the older
  `UNKNOWN_TERM` row in `mappings/ingredient_mappings_oak_ols_review.tsv` was
  a validator-prefix coverage gap, not a bad identifier.
- Major: `nutritional_roles.PROTEIN_SOURCE` was created by
  `infer_roles_from_name_lists` and has only `COMPUTATIONAL_PREDICTION`
  evidence with a curator note calling the name-pattern rule provisional.
- A hidden/ignored-inclusive search over `data/ingredients`, `data/curated`,
  `mappings`, `scripts`, `src`, `tests`, and `reports`, excluding prior
  per-record reports, aggregate backups, and the final SSSOM TSV, found the
  active YAML, aggregate copy, MICRO OLS validation rows, row-review
  provenance, occurrence membership, the `Bacto_Peptone` cross-record synonym,
  and ignored historical batch reports.

## Completeness

- The exact MICRO identity, undefined-mixture type, occurrence counts, and empty
  final SSSOM payload are populated.
- The one consequential gap is evidence for the nutritional role.

## Recommended Edits

- Major: either replace `nutritional_roles.PROTEIN_SOURCE` in
  `data/ingredients/mapped/Fish_peptone.yaml` with source-backed role evidence
  or remove the role, sync `data/curated/mapped_ingredients.yaml`, and rerun
  strict validation plus the final SSSOM invariant gates.
