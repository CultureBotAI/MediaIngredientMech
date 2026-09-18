# `data/ingredients/mapped/Butyricin_7423.yaml`

## Verdict

Needs curation, minor. The exact `mesh:C010427` butyricin 7423 mapping, MeSH
prefix validation, SSSOM row, and aggregate copy agree, but one mapping
evidence note still describes the old kg-microbe placeholder as pending
curator promotion after the record was already upgraded to MeSH.

## Identity

- Reviewed record: `data/ingredients/mapped/Butyricin_7423.yaml`.
- Identifier and grounding: `identifier: mesh:C010427` with
  `ontology_mapping.ontology_id: mesh:C010427`,
  `ontology_label: butyricin 7423`, `ontology_source: MESH`,
  `mapping_quality: EXACT_MATCH`, `ingredient_type: SINGLE_INGREDIENT`, and
  `mapping_status: MAPPED`.
- Live OLS exact search for `Butyricin 7423` returns only `mesh:C010427`, and
  the prefix-specific OLS validation table resolves the same exact CURIE.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Butyrate.yaml data/ingredients/mapped/Butyric_Acid.yaml data/ingredients/mapped/Butyricin_7423.yaml data/ingredients/mapped/Butyrolactam.yaml data/ingredients/mapped/CCCP.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Butyrate.yaml data/ingredients/mapped/Butyric_Acid.yaml data/ingredients/mapped/Butyricin_7423.yaml data/ingredients/mapped/Butyrolactam.yaml data/ingredients/mapped/CCCP.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for all 5 files.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K. Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- Hidden/ignored-inclusive search over `data/curated`, `mappings`,
  `data/custom`, and `reports`, excluding `data/curated/backups` and generated
  review directories, found the prefix-specific MeSH OLS validation row, the
  authoritative exact SSSOM row at `mappings/ingredient_mappings.sssom.tsv`
  row 644, the row-review triage explaining the old `UNKNOWN_TERM` result as a
  missing-prefix-validator artifact, and the aggregate copy in
  `data/curated/mapped_ingredients.yaml`.
- The local SSSOM row maps `MIM:Butyricin_7423` to `mesh:C010427` with
  `skos:exactMatch`, matching the primary `identifier` and
  `ontology_mapping`.
- A parsed comparison against `data/curated/mapped_ingredients.yaml` found
  exactly one aggregate record with the same identifier and preferred term, and
  it is identical to this per-record YAML.

## Completeness

- The exact MeSH identifier, kg-microbe placeholder provenance, MeSH promotion
  event, single-ingredient classification, SSSOM row, and aggregate copy are
  populated.
- Minor gap: the first `ontology_mapping.evidence` item still says the
  `kgmicrobe.compound` placeholder is pending curator promotion to a
  CHEBI/NCIT primary identifier, but the record was promoted to
  `mesh:C010427` on 2026-05-01.
- `occurrence_statistics.total_occurrences: 0` and `media_count: 0` are
  consistent with a kg-microbe placeholder import that has no CultureMech
  recipe memberships.

## Recommended Edits

- Minor: update the stale kg-microbe placeholder evidence note in
  `data/ingredients/mapped/Butyricin_7423.yaml` so it points at the accepted
  MeSH promotion instead of saying promotion is pending; then run
  `just sync-curated` and focused strict/term/SSSOM validation.
