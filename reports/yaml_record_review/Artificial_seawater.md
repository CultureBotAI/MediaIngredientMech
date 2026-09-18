# `data/ingredients/mapped/Artificial_seawater.yaml`

## Verdict

Pass. The record exactly denotes MICRO `artificial seawater`, and its raw
CultureMech variants are retained only as source surface forms.

## Identity

- Reviewed record: `data/ingredients/mapped/Artificial_seawater.yaml`.
- Identifier and grounding: `identifier: MICRO:0001715` with
  `ontology_mapping.ontology_id: MICRO:0001715`, `ontology_source: MICRO`,
  `mapping_quality: EXACT_MATCH`, `match_level: EXACT`, and
  `mapping_status: MAPPED`.
- OLS resolves `MICRO:0001715` to non-obsolete `artificial seawater` with a
  definition for an inorganic salts solution that mimics sea water and the
  exact synonym `synthetic seawater`.
- The two synonyms are raw CultureMech labels with parenthetical recipe
  navigation text; they are not asserted as exact ontology aliases.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Arsenate.yaml data/ingredients/mapped/Artepaulin.yaml data/ingredients/mapped/Artificial_Sea_Salt.yaml data/ingredients/mapped/Artificial_seawater.yaml data/ingredients/mapped/Ascomycin.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Artificial_seawater.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  failed in the MICRO sqlite adapter with `sqlite3.OperationalError: no such
  table: rdfs_label_statement`. This matches the repository contract:
  `just validate-terms` skips MICRO and leaves it to Engine B/product
  validation or explicit OLS checks.
- OLS4 lookup for `MICRO:0001715`: resolved the exact stored term and label.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed;
  2951 records, 83 decompositions, 505 components, 0 violations.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.
- `uv run --frozen python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`:
  passed; all id/label pairs corresponded and 104 non-blocking plausibility
  warnings were reported.
- `uv run --frozen python scripts/check_flat_export_coverage.py`: passed; docs
  data were fresh and every curated label was resolvable.

## Evidence

- `mappings/culturemech_residual_groundings.tsv` has the maintained residual
  decisions that folded `Artificial seawater`,
  `Artificial seawater (see below)`, `Artificial Seawater`, and
  `Artificial seawater (see Medium No. 736 )` to `MICRO:0001715`.
- `mappings/ingredient_mappings.sssom.tsv` row 482 maps
  `MIM:Artificial_seawater` to `MICRO:0001715` with `skos:exactMatch` and keeps
  the two parenthetical strings in `other`.
- A hidden, ignored-inclusive search across the active checkout, excluding
  stale `data/curated/backups` and review output, found the same identity in
  the per-record YAML, aggregate YAML, SSSOM, CultureMech residual TSVs, and
  generated docs products.

## Completeness

- Occurrence counts are populated: 19 total mentions across 19 CultureMech
  recipes.
- The record correctly leaves components, roles, environment, datasets, and
  discussions empty; it is only publishing a resolved CultureMech residual
  ingredient and two raw label variants.
- No CAS or chemical structure fields are expected for this MICRO mixture.

## Recommended Edits

- None.
