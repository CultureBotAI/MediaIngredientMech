# `data/ingredients/mapped/Ascorbic_Acid.yaml`

## Verdict

Needs curation; severity major. The record still exact-maps `Ascorbic acid` to
generic `CHEBI:22652`, but its CAS and PubChem provenance identify
stereospecific `L-ascorbic acid`, and old CultureMech role/property text remains
in `synonyms`.

## Identity

- Reviewed record: `data/ingredients/mapped/Ascorbic_Acid.yaml`.
- Identifier and grounding: `identifier: CHEBI:22652` with
  `ontology_mapping.ontology_id: CHEBI:22652`, `ontology_source: CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- OLS resolves `CHEBI:22652` to non-obsolete generic `ascorbic acid`; that term
  has no CAS, formula, InChI, or SMILES annotation in ChEBI.
- OLS resolves `CHEBI:29073` to `L-ascorbic acid`; that narrower term carries
  CAS xref `50-81-7`, formula `C6H8O6`, the full InChI present in PubChem for
  CAS `50-81-7`, and synonyms including `Ascorbic acid` and `Vitamin C`.
- PubChem resolves CAS `50-81-7` to the same stereospecific L-ascorbic-acid
  InChI, so `chemical_properties.cas_rn: 50-81-7` does not support the current
  generic `CHEBI:22652` identity.
- A separate `data/ingredients/mapped/L-ascorbic_Acid.yaml` record already
  denotes `CHEBI:29073` and carries the same CAS with matching structure.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Ascorbate.yaml data/ingredients/mapped/Ascorbic_Acid.yaml data/ingredients/mapped/Ascosin.yaml data/ingredients/mapped/Asialofetuin.yaml data/ingredients/mapped/Asiaticoside.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Ascorbic_Acid.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed; this only proves `CHEBI:22652` is canonically labelled
  `ascorbic acid`, not that the CAS-bearing CultureMech record was grounded to
  the most specific term.
- OLS4 lookups for `CHEBI:22652` and `CHEBI:29073` resolved the parent/child
  distinction and showed that CAS `50-81-7` belongs to `CHEBI:29073`.
- PubChem lookup for `50-81-7` resolved the L-ascorbic-acid formula and InChI.
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

- `mappings/ingredient_mappings.sssom.tsv` row 485 publishes
  `MIM:Ascorbic_Acid skos:exactMatch CHEBI:22652` while also exporting
  `CAS:50-81-7`, so the published row mixes a generic parent with the
  L-ascorbic-acid registry number.
- `mappings/ingredient_mappings_oak_ols_review.tsv` row 326 and
  `mappings/ingredient_mappings_row_review_manifest.tsv` row 326 are stale:
  they describe `MIM:Ascorbic_Acid` as confirmed against `CHEBI:29073`, but the
  active SSSOM row and YAML both still use `CHEBI:22652`.
- Five `Role: Vitamin; Properties: ...` strings remain in `synonyms` as
  CultureMech `RAW_TEXT`. They are role/property metadata, not names of
  ascorbic acid.
- `Ascorbic acid (Sigma)` is a supported raw/catalog surface from
  `culturemech:output/ingredient_occurrences.tsv`.

## Completeness

- Occurrence counts are populated for 65 distinct CultureMech recipes and are
  traceable through `mappings/culturemech_recipe_membership.tsv`.
- The vitamin-source nutritional role records the original CultureMech
  `Vitamin Source` role text narrowly enough.
- Chemical formula, InChI, and SMILES are absent because the current ChEBI
  parent is generic; after regrounding to `CHEBI:29073`, those fields should be
  synchronized from ChEBI/PubChem just as they are in `L-ascorbic_Acid.yaml`.

## Recommended Edits

- Reground `data/ingredients/mapped/Ascorbic_Acid.yaml` from `CHEBI:22652` to
  the form-specific `CHEBI:29073` when the source label and CAS `50-81-7`
  denote ordinary L-ascorbic acid.
- Decide whether this record should merge with `L-ascorbic_Acid.yaml` or retain
  a separate source-surface record; do not leave two exact records for the same
  CAS-backed chemical unless the duplicate-identifier baseline intentionally
  tracks that family.
- Remove the five `Role: Vitamin; Properties: ...` strings from `synonyms`.
- Synchronize the aggregate and SSSOM rows, then rerun focused strict and term
  validation, SSSOM invariants, flat-export coverage, and the id/label product
  check.
