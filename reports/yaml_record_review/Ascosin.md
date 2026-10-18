# `data/ingredients/mapped/Ascosin.yaml`

## Verdict

Pass. `Ascosin` is intentionally retained as a `kgmicrobe.compound` placeholder
after exact OLS promotion searches failed to find a CHEBI, NCIT, MeSH, MICRO,
BTO, or FoodOn identity.

## Identity

- Reviewed record: `data/ingredients/mapped/Ascosin.yaml`.
- Identifier and grounding: `identifier: kgmicrobe.compound:ascosin` with
  `ontology_mapping.ontology_id: kgmicrobe.compound:ascosin`,
  `ontology_source: kgmicrobe.compound`, `mapping_quality: PLACEHOLDER`, and
  `mapping_status: MAPPED`.
- The current OLS4 exact and broad searches for `Ascosin` across CHEBI, NCIT,
  MeSH, MICRO, BTO, and FoodOn returned zero candidates.
- The record's local placeholder identity is consistent with
  `mappings/ingredient_mappings_unknown_term_nohit_review.tsv` and the
  2026-05-09 curation note, both of which found no exact OLS candidate and no
  normalized local duplicate.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Ascorbate.yaml data/ingredients/mapped/Ascorbic_Acid.yaml data/ingredients/mapped/Ascosin.yaml data/ingredients/mapped/Asialofetuin.yaml data/ingredients/mapped/Asiaticoside.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Ascosin.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  failed in the kg-microbe sqlite adapter with
  `sqlite3.OperationalError: no such table: rdfs_label_statement`. This matches
  the repository contract: kg-microbe registry CURIEs are skipped by
  `just validate-terms` and reviewed as local identifiers.
- Current exact and broad OLS4 searches for `Ascosin`: no candidates.
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

- `mappings/ingredient_mappings.sssom.tsv` row 486 maps `MIM:Ascosin` exactly
  to `kgmicrobe.compound:ascosin`, which is the record's own retained primary
  identifier rather than a lossy external match.
- `mappings/ingredient_mappings_unknown_term_triage.tsv` row 115 marks the
  placeholder as an expected local registry identifier pending curator
  promotion to an external term.
- `mappings/ingredient_mappings_unknown_term_nohit_review.tsv` row 6 records
  the no-exact-candidate and no-local-duplicate review for the same YAML file.

## Completeness

- The placeholder provenance, curation note, `ingredient_type`, SSSOM row, and
  aggregate copy are populated.
- Occurrence counts are correctly zero, and no CAS, chemical structure, roles,
  components, environment, or datasets are needed while no external identity is
  known.

## Recommended Edits

- None.
