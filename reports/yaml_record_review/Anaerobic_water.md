# `data/ingredients/mapped/Anaerobic_water.yaml`

## Verdict

Pass. The `ENVO:01000173` anoxic-water grounding, exact-synonym evidence for
the CultureMech surface form, 2 residual CultureMech occurrences, restored SSSOM
provenance, and aggregate copy agree.

## Identity

- Reviewed record: `data/ingredients/mapped/Anaerobic_water.yaml`.
- Identifier and grounding: `identifier: ENVO:01000173` with
  `ontology_mapping.ontology_id: ENVO:01000173`, source `ENVO`,
  `mapping_quality: SYNONYM_MATCH`, `match_level: NORMALIZED`, and
  `mapping_status: MAPPED`.
- The active structured evidence records that the surface form was grounded to
  `ENVO:01000173` by exact match against an exact ontology synonym, and the
  #541 history explains why that evidence was restored into the field read by
  the SSSOM builder.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Amylopectin_From_Maize.yaml data/ingredients/mapped/Amylose_From_Potato.yaml data/ingredients/mapped/Anabasine_Hydrochloride.yaml data/ingredients/mapped/Anaerobic_water.yaml data/ingredients/mapped/Andirobin.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Anaerobic_water.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed; 2951
  records, 83 decompositions, 505 components, 0 violations.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- `mappings/culturemech_residual_groundings.tsv` records the 2 mentions across
  2 recipes that created this record from the residual CultureMech surface.
- `mappings/culturemech_residual_triage.tsv` links the exact `Anaerobic water`
  alias back to `ENVO:01000173`.
- `mappings/ingredient_mappings.sssom.tsv` row 423 maps `MIM:Anaerobic_water`
  to `ENVO:01000173` with `skos:exactMatch` and includes
  `MIM:culturemech:output/ingredient_occurrences.tsv` after the #541 evidence
  restoration.
- A hidden/ignored-inclusive search over active YAML records, the curated
  aggregate, CultureMech residual groundings, residual triage, and batch review
  reports found the active YAML, aggregate copy, residual source row, triage
  alias row, and SSSOM row.

## Completeness

- Occurrence count, ENVO grounding, exact synonym evidence, curation history,
  and SSSOM provenance are populated.
- Chemical structure, CAS, component, role, environmental context, discussion,
  and dataset slots are not needed for this environmental water class.
- The aggregate copy in `data/curated/mapped_ingredients.yaml` matches the
  per-record YAML.

## Recommended Edits

None.
