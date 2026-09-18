# `data/ingredients/mapped/Flucloxacillin.yaml`

## Verdict

Pass with minor issues. The CultureMech residual label maps exactly to
`CHEBI:5098` and the final SSSOM row has restored CultureMech provenance, but
the new CHEBI-primary record has no `ingredient_type`.

## Identity

- Reviewed record: `data/ingredients/mapped/Flucloxacillin.yaml`.
- Identifier and grounding: `identifier: CHEBI:5098` with matching
  `ontology_mapping.ontology_id`, canonical label `flucloxacillin`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `match_level: EXACT`, and
  `mapping_status: MAPPED`.
- PubChem lookup by name resolved CID 21319 titled `Flucloxacillin`.
- `mappings/culturemech_residual_groundings.tsv` records this as a
  CultureMech residual label grounded to `CHEBI:5098` on a new exact record.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Fleroxacin.yaml data/ingredients/mapped/Flucloxacillin.yaml data/ingredients/mapped/Fluoranthene.yaml data/ingredients/mapped/Fluorene.yaml data/ingredients/mapped/Fluorescein.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Flucloxacillin.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 skipped because the
  sibling kg-microbe ontology transforms are not checked out.

## Evidence

- The matching `data/curated/mapped_ingredients.yaml` entry carries the same
  ChEBI identifier, CultureMech residual evidence, occurrence count, and
  missing `ingredient_type` as the per-record YAML.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:Flucloxacillin` to `CHEBI:5098` with `skos:exactMatch` and an empty
  `other` column.
- The 2026-09-06 curation restored `MIM:culturemech:output/ingredient_occurrences.tsv`
  into the SSSOM `source` payload, so the final row carries provenance from the
  maintained occurrence table.
- Minor: this exact CHEBI chemical is missing `ingredient_type`.
- A hidden/ignored-inclusive search over `data/ingredients`, `data/curated`,
  `mappings`, `scripts`, `src`, `tests`, and `reports`, excluding prior
  per-record reports, aggregate backups, and the final SSSOM TSV, found the
  active YAML, aggregate copy, residual grounding and triage rows, the
  unresolved `100 mg/ml flucloxacillin` concentration residual, and ignored
  historical batch reports.

## Completeness

- The exact ChEBI identity, CultureMech occurrence evidence, occurrence count,
  and empty final SSSOM synonym payload are populated.
- The missing single-ingredient type is the only consequential field gap.

## Recommended Edits

- Minor: set `ingredient_type: SINGLE_INGREDIENT` in
  `data/ingredients/mapped/Flucloxacillin.yaml`, sync
  `data/curated/mapped_ingredients.yaml`, and rerun strict validation plus the
  final SSSOM invariant gates.
