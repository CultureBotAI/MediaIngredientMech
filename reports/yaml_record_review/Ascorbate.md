# `data/ingredients/mapped/Ascorbate.yaml`

## Verdict

Pass. The record exactly denotes the generic ChEBI `ascorbate` conjugate-base
class and its MicrobeDecoder import, CultureMech recipe memberships, SSSOM row,
and aggregate copy agree.

## Identity

- Reviewed record: `data/ingredients/mapped/Ascorbate.yaml`.
- Identifier and grounding: `identifier: CHEBI:22651` with
  `ontology_mapping.ontology_id: CHEBI:22651`, `ontology_source: CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- OLS resolves `CHEBI:22651` to non-obsolete ChEBI `ascorbate`, defined as a
  ketoaldonate that is the conjugate base of ascorbic acid.
- The generic ascorbate identity is intentionally broader than the separate
  `L-ascorbic_Acid.yaml` and `Na-ascorbate.yaml` records; the ChEBI term has no
  fixed neutral structure to backfill.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Ascorbate.yaml data/ingredients/mapped/Ascorbic_Acid.yaml data/ingredients/mapped/Ascosin.yaml data/ingredients/mapped/Asialofetuin.yaml data/ingredients/mapped/Asiaticoside.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Ascorbate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- OLS4 term lookup for `CHEBI:22651`: resolved the current non-obsolete ChEBI
  label and the generic ascorbate definition.
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

- `data/custom/microbedecoder/unmapped_labels.tsv` contains
  `kgmicrobe.trait:ascorbate` from `BacDive_Metabolite_utilization` with five
  occurrences, matching `occurrence_statistics.source_occurrences`.
- `data/custom/microbedecoder/ingredient_candidates.tsv` contains the exact
  `ascorbate` candidate with the same count and source column.
- `mappings/microbedecoder_auto_mapped_review.tsv` row 65 records the
  `APPROVED` decision that promoted `Ascorbate.yaml` to `MAPPED`.
- `mappings/culturemech_recipe_membership.tsv` carries seven `CHEBI:22651`
  recipe memberships, matching `occurrence_statistics.total_occurrences`.
- `mappings/ingredient_mappings.sssom.tsv` row 484 maps `MIM:Ascorbate` to
  `CHEBI:22651` with `skos:exactMatch`.

## Completeness

- The ChEBI class identity, MicrobeDecoder source occurrence, CultureMech
  occurrence counts, SSSOM row, and aggregate copy are populated.
- Chemical properties, CAS, roles, components, environment, datasets, and
  discussions are correctly absent for this generic ascorbate class.

## Recommended Edits

- None.
