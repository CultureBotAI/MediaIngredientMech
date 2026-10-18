# `data/ingredients/mapped/Fe_Nh42_So42_X_7_H2o.yaml`

## Verdict

Needs curation, with a major role-evidence issue. The source label maps to the
active ChEBI ferrous ammonium sulfate heptahydrate term and the final SSSOM row
is clean, but the `TRACE_ELEMENT` role is still backed only by a provisional
in-session inference.

## Identity

- Reviewed record: `data/ingredients/mapped/Fe_Nh42_So42_X_7_H2o.yaml`.
- Identifier and grounding: `identifier: CHEBI:131378` with matching
  `ontology_mapping.ontology_id`, canonical label
  `ferrous ammonium sulfate heptahydrate`, source `CHEBI`, `mapping_quality:
  EXACT_MATCH`, `mapping_status: MAPPED`, and `ingredient_type:
  SINGLE_INGREDIENT`.
- The structure fields record formula `Fe.7H2O.2H4N.2O4S` and the
  CHEBI-backed InChI for the heptahydrate.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Fe_Iii_Citrate.yaml data/ingredients/mapped/Fe_Iiipo4_X_4_H2o.yaml data/ingredients/mapped/Fe_Nh42_So42_X_6_H2o.yaml data/ingredients/mapped/Fe_Nh42_So42_X_7_H2o.yaml data/ingredients/mapped/Fecl2.yaml --out /tmp/mim_fe2_batch_strict.tsv`:
  exited 0 for the 5-file batch; the output TSV contained only its header.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Fe_Iii_Citrate.yaml data/ingredients/mapped/Fe_Iiipo4_X_4_H2o.yaml data/ingredients/mapped/Fe_Nh42_So42_X_6_H2o.yaml data/ingredients/mapped/Fe_Nh42_So42_X_7_H2o.yaml data/ingredients/mapped/Fecl2.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.

## Evidence

- The matching `data/curated/mapped_ingredients.yaml` entry carries the same
  ChEBI identifier, structure fields, hydrate-form synonyms, provisional
  `TRACE_ELEMENT` role, and refreshed occurrence counts as the per-record YAML.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:Fe_Nh42_So42_X_7_H2o` to `CHEBI:131378` with `skos:exactMatch`;
  exported `other` tokens are heptahydrate surface forms.
- `mappings/hydrate_review.tsv` marked the heptahydrate mapping correct but
  medium-confidence, with source support still needed for the heptahydrate
  phase.
- Major: `nutritional_roles.TRACE_ELEMENT` is supported only by a
  `COMPUTATIONAL_PREDICTION` reference from an in-session LLM assignment, and
  that evidence explicitly describes the assertion as provisional.
- A hidden/ignored-inclusive search over `data/ingredients`, `data/curated`,
  `mappings`, and `reports/yaml_record_review` for
  `MIM:Fe_Nh42_So42_X_7_H2o`, `CHEBI:131378`, and heptahydrate labels found
  the active YAML, aggregate copy, final SSSOM row, hydrate review row,
  row-review provenance, CultureMech recipe memberships, and ignored aggregate
  backups; it did not expose a contradictory active mapping.

## Completeness

- The heptahydrate identity, structure fields, hydrate-form synonyms,
  ingredient type, occurrence counts, and final SSSOM row are populated.
- The nutritional role needs curator evidence or removal; source support for
  the exact heptahydrate phase should be recorded if available.

## Recommended Edits

- Major: either replace the provisional `TRACE_ELEMENT` inference with
  source-backed evidence or remove the role facet.
- Minor: attach primary source evidence for the exact heptahydrate phase if
  it is available from the 34 CultureMech occurrences.
- Sync `data/curated/mapped_ingredients.yaml`, regenerate downstream artifacts
  if the role changes, and rerun strict validation.
