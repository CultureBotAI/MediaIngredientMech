# `data/ingredients/mapped/Asialofetuin.yaml`

## Verdict

Pass. The record exact-maps the mim-queue source label to MeSH `asialofetuin`,
and the MeSH label, occurrence counts, SSSOM row, and aggregate copy agree.

## Identity

- Reviewed record: `data/ingredients/mapped/Asialofetuin.yaml`.
- Identifier and grounding: `identifier: mesh:C017029` with
  `ontology_mapping.ontology_id: mesh:C017029`, `ontology_source: MESH`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- OLS resolves `mesh:C017029` to non-obsolete MeSH `asialofetuin` with
  synonyms `asialo-fetuin`, `asialogalactofetuin`, and
  `fetuin, asialo derivative`.
- The single raw synonym is the original mim-queue label and does not introduce
  an unsupported alias.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Ascorbate.yaml data/ingredients/mapped/Ascorbic_Acid.yaml data/ingredients/mapped/Ascosin.yaml data/ingredients/mapped/Asialofetuin.yaml data/ingredients/mapped/Asiaticoside.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Asialofetuin.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- OLS4 term lookup for `mesh:C017029`: resolved the current non-obsolete MeSH
  label and synonyms.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed;
  2951 records, 83 decompositions, 505 components, 0 violations.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.
- `uv run --frozen python scripts/check_flat_export_coverage.py`: passed before
  this review batch; docs data were fresh and every curated label was
  resolvable.
- `uv run --frozen python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`:
  passed before this review batch; all id/label pairs corresponded and 104
  non-blocking plausibility warnings were reported.

## Evidence

- `mappings/ingredient_mappings_external_prefix_ols_validation.tsv` has a
  prefix-specific OLS validation row resolving `mesh:C017029` exactly to
  `asialofetuin`.
- `mappings/ingredient_mappings_unknown_term_triage.tsv` row 116 records that
  the old `UNKNOWN_TERM` status was only missing prefix-validator coverage, not
  a bad MeSH CURIE.
- `mappings/culturemech_recipe_membership.tsv` carries two `mesh:C017029`
  recipe memberships, matching `occurrence_statistics`.
- `mappings/ingredient_mappings.sssom.tsv` row 487 maps `MIM:Asialofetuin` to
  `mesh:C017029` with `skos:exactMatch`.

## Completeness

- The exact MeSH identity, occurrence counts, SSSOM row, and aggregate copy are
  populated.
- No CAS, chemical properties, roles, components, environment, datasets, or
  discussion entries are required for this MeSH protein derivative record.

## Recommended Edits

- None.
