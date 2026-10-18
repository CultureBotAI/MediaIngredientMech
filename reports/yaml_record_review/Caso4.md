# `data/ingredients/mapped/Caso4.yaml`

## Verdict

Needs curation; major issue. The anhydrous calcium sulfate identity, CAS,
structure fields, SSSOM row, aggregate copy, occurrence count, and malformed
hydrate alias rejection agree, but `MINERAL_SOURCE` has no evidence object.

## Identity

- Reviewed record: `data/ingredients/mapped/Caso4.yaml`.
- Identifier and grounding: `identifier: CHEBI:31346`,
  `ontology_mapping.ontology_id: CHEBI:31346`,
  `ontology_label: calcium sulfate`, `ontology_source: CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Direct OLS lookup for `CHEBI:31346` returns one active ChEBI term labelled
  `calcium sulfate` with CAS `7778-18-9`, formula `Ca.O4S`, and the same
  InChI and SMILES stored in `chemical_properties`.
- The former malformed `CaSO4 x 7 H2O` alias is retained only as a
  `REJECTED_LABEL`, and the active hydrated sibling now owns the fullwidth-dot
  heptahydrate label.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Casein_Peptone.yaml data/ingredients/mapped/Casein_hydrolysate.yaml data/ingredients/mapped/Casitone.yaml data/ingredients/mapped/Casitone_Yeast_Extract_Rumen_Fluid.yaml data/ingredients/mapped/Caso4.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Casein_Peptone.yaml data/ingredients/mapped/Caso4.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed both Engine-A-supported OBO records in this batch.
- MICRO records in this batch were checked by direct prefix-specific OLS lookup
  and by the existing prefix-specific OLS validation TSV, rather than through
  the sqlite-backed Engine A path that the `justfile` intentionally skips for
  MICRO.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed;
  2951 records, 83 decompositions, 505 components, and 0 violations.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip.wqYt47`
  followed by
  `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip.wqYt47`:
  passed; both curated collection files had 0 data differences and only the
  expected scratch `generation_date` metadata differences.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K. Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- Hidden/ignored-inclusive search over `data/curated`, `mappings`,
  `docs/data`, and `reports`, excluding generated review reports and curated
  backups, found the active `MIM:Caso4` SSSOM row with `CHEBI:31346`, the
  `CONFIRMED_NO_ACTION` row-review disposition, matching aggregate/docs rows,
  and the heptahydrate sibling that now carries the malformed hydrate alias.
- The current `mappings/culturemech_recipe_membership.tsv` rows contain 15
  distinct recipes and 15 total occurrences for `CHEBI:31346`, matching
  `occurrence_statistics`.
- `SULFUR_SOURCE` preserves the imported CultureMech `Mineral` role text as a
  `DATABASE_ENTRY` evidence item. `MINERAL_SOURCE` was added by the #128
  residual-role repair but carries an empty `evidence` list.

## Completeness

- The exact ChEBI identifier, CAS, formula, InChI, SMILES, synonyms, 15/15
  occurrence count, SSSOM row, aggregate copy, and docs row are populated.
- No live hydrate synonym is exported from this anhydrous record after the
  #344 repair; the malformed heptahydrate string is non-resolving here.

## Recommended Edits

- Major: add inspected evidence to
  `nutritional_roles.MINERAL_SOURCE` in
  `data/ingredients/mapped/Caso4.yaml`, or remove the role if the bulk-cation
  assertion is not supported for calcium sulfate, then rerun strict
  validation, SSSOM QC, aggregate roundtrip, and `git diff --check`.
