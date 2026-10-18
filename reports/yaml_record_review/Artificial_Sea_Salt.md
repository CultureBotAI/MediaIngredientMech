# `data/ingredients/mapped/Artificial_Sea_Salt.yaml`

## Verdict

Needs curation; severity blocker. The exact MICRO mapping is a lexical
stem-match from `Artificial Sea Salt` to generic `sea salt`, not an identity
mapping for the artificial product/formulation named by the source label.

## Identity

- Reviewed record: `data/ingredients/mapped/Artificial_Sea_Salt.yaml`.
- Identifier and grounding: `identifier: MICRO:0001647` with
  `ontology_mapping.ontology_id: MICRO:0001647`, `ontology_source: MICRO`,
  `mapping_quality: LEXICAL_MATCH`, and `mapping_status: MAPPED`.
- OLS resolves `MICRO:0001647` to `sea salt` with the definition "An undefined
  inorganic chemical mixture comprised of a mixture of salts derived from the
  evaporation of seawater."
- The source label is `Artificial Sea Salt`, and the creation history records a
  stem-substring upgrade from the old unmapped identity. That stem match drops
  the explicit artificial/synthetic qualifier.
- OLS resolves the neighboring term `MICRO:0001715` to `artificial seawater`,
  defined as an inorganic salts solution that mimics sea water. That confirms
  that MICRO distinguishes generic evaporated `sea salt` from artificial sea
  water formulations, but dry artificial sea salt should not be merged into
  `MICRO:0001715` without source support that the source label denotes the
  finished aqueous solution.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Arsenate.yaml data/ingredients/mapped/Artepaulin.yaml data/ingredients/mapped/Artificial_Sea_Salt.yaml data/ingredients/mapped/Artificial_seawater.yaml data/ingredients/mapped/Ascomycin.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Artificial_Sea_Salt.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  failed after OAK downloaded the empty MICRO sqlite stub, with
  `sqlite3.OperationalError: no such table: rdfs_label_statement`. This matches
  the repository contract: `just validate-terms` skips MICRO and leaves it to
  Engine B/product validation or explicit OLS checks.
- OLS4 lookup for `MICRO:0001647`: resolved the stored `sea salt` label exactly
  and returned the evaporated-seawater definition.
- OLS4 lookup for `MICRO:0001715`: resolved the distinct `artificial seawater`
  term.
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

- `mappings/ingredient_mappings.sssom.tsv` row 481 publishes
  `MIM:Artificial_Sea_Salt skos:exactMatch MICRO:0001647`, so the output
  currently collapses artificial sea salt into generic evaporated sea salt.
- `mappings/ingredient_mappings_unknown_term_triage.tsv` row 113 only proves
  the MICRO CURIE resolves in OLS; it does not prove exact identity between
  `Artificial Sea Salt` and `sea salt`.
- `reports/causal_graph_readiness.tsv` flags this record for weak lexical
  mapping quality, no roles, and no components. The missing components are
  secondary to the wrong exact identity.
- The only synonym is a duplicate raw copy of `Artificial Sea Salt`, so the
  record has no additional evidence narrowing it to natural evaporated sea salt.

## Completeness

- Occurrence counts are populated: 12 total mentions across 12 CultureMech
  recipes.
- `ingredient_type: UNDEFINED_MIXTURE` fits a sea-salt mixture, but the record
  has no `components` decomposition for the artificial formulation and no
  discussion explaining which product or recipe text this label came from.
- A hidden, ignored-inclusive search across the checkout, excluding stale
  `data/curated/backups` and review output, found no maintained source artifact
  that justifies dropping the `Artificial` qualifier.

## Recommended Edits

- In `data/ingredients/mapped/Artificial_Sea_Salt.yaml`, break the exact
  mapping to `MICRO:0001647`.
- Preserve a kg-microbe primary identity for the artificial sea salt mixture
  unless an exact external ontology term is found; if the best external anchor
  remains `sea salt`, record it as a non-identity parent or close mapping
  according to `MAPPING_SEMANTICS.md`.
- Add a discussion or component evidence entry that explains whether the source
  label denotes dry artificial sea salt, an artificial seawater solution, or a
  named commercial mixture.
- Synchronize `data/curated/mapped_ingredients.yaml` and
  `mappings/ingredient_mappings.sssom.tsv`, then rerun strict validation, MICRO
  OLS/product label checks, component partonomy, and SSSOM invariants.
