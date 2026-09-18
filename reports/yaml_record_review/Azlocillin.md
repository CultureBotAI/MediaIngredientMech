# `data/ingredients/mapped/Azlocillin.yaml`

## Verdict

Needs curation; severity minor. The CultureMech residual label is
exact-mapped to non-obsolete `CHEBI:2956` `azlocillin` and the SSSOM plus
aggregate copies are synchronized, but this exact structural ChEBI record is
missing `ingredient_type: SINGLE_INGREDIENT` and the available ChEBI chemical
properties.

## Identity

- Reviewed record: `data/ingredients/mapped/Azlocillin.yaml`.
- Identifier and grounding: `identifier: CHEBI:2956` with
  `ontology_mapping.ontology_id: CHEBI:2956`,
  `ontology_label: azlocillin`, `ontology_source: CHEBI`,
  `mapping_quality: EXACT_MATCH`, `match_level: EXACT`, and
  `mapping_status: MAPPED`.
- OLS resolves `CHEBI:2956` to non-obsolete `azlocillin` with CAS
  `37091-66-0`, formula `C20H23N5O6S`, and full InChI/SMILES annotations.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Azithromycin.yaml data/ingredients/mapped/Azlocillin.yaml data/ingredients/mapped/Azlocillin_Sodium_Salt.yaml data/ingredients/mapped/Azomycin.yaml data/ingredients/mapped/Aztreonam.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Azlocillin.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- OLS4 lookup for `CHEBI:2956` confirmed the exact acid identity and available
  ChEBI structure fields.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed;
  2951 records, 83 decompositions, 505 components, 0 violations.

## Evidence

- Hidden/ignored-inclusive searches over `data/curated`, `mappings`, and
  `data/custom`, excluding `data/curated/backups`, found the authoritative
  SSSOM row at `mappings/ingredient_mappings.sssom.tsv` row 512 and the
  aggregate copy in `data/curated/mapped_ingredients.yaml`.
- `mappings/culturemech_residual_groundings.tsv` and
  `mappings/culturemech_residual_triage.tsv` show the residual
  `azlocillin` label had one mention in one CultureMech recipe and was promoted
  to `CHEBI:2956`.
- The 2026-09-06 curation event restored the structured
  `ontology_mapping.evidence` needed by the SSSOM builder, and the current
  SSSOM `source` field includes
  `MIM:culturemech:output/ingredient_occurrences.tsv`.

## Completeness

- The exact identifier, CultureMech occurrence count, evidence, SSSOM row, and
  aggregate copy are populated.
- The record is still missing the ChEBI-backed `ingredient_type` and
  `chemical_properties` that adjacent exact ChEBI structural records carry.

## Recommended Edits

- Add `ingredient_type: SINGLE_INGREDIENT` and ChEBI-derived
  `chemical_properties` for `CHEBI:2956` to
  `data/ingredients/mapped/Azlocillin.yaml`, synchronize
  `data/curated/mapped_ingredients.yaml`, and rerun focused strict and term
  validation, product id/label correspondence, SSSOM invariants, and
  flat-export coverage.
