# `data/ingredients/mapped/Digested_Serum.yaml`

## Verdict

Needs curation. The record now exact-matches live `MICRO:0001362` digested
serum and is correctly typed as an undefined mixture, but its
`PROTEIN_SOURCE` role is still only an in-session computational assertion.
The record also retains stale import-review notes and an obsolete
`UNKNOWN_TERM` validation stamp in final SSSOM.

## Identity

- Reviewed record: `data/ingredients/mapped/Digested_Serum.yaml`.
- Identifier and grounding: `identifier: MICRO:0001362` with
  `ontology_mapping.ontology_id: MICRO:0001362`, source `MICRO`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`,
  `ingredient_type: UNDEFINED_MIXTURE`, and two CultureMech occurrences.
- Live EBI OLS exact searches for `MICRO:0001362` and `digested serum` both
  resolve to the MICRO class `MICRO:0001362` with label `digested serum`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Dicloxacillin_Sodium_Salt_Monohydrate.yaml data/ingredients/mapped/Diethyl_Ether.yaml data/ingredients/mapped/Diethyl_phosphonate.yaml data/ingredients/mapped/Difucosyllactose.yaml data/ingredients/mapped/Digested_Serum.yaml`:
  exited 0 for the 5-file batch.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Dicloxacillin_Sodium_Salt_Monohydrate.yaml data/ingredients/mapped/Diethyl_Ether.yaml data/ingredients/mapped/Diethyl_phosphonate.yaml data/ingredients/mapped/Difucosyllactose.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed the 4-record CHEBI subset.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Dicloxacillin_Sodium_Salt_Monohydrate.yaml data/ingredients/mapped/Diethyl_Ether.yaml data/ingredients/mapped/Diethyl_phosphonate.yaml data/ingredients/mapped/Difucosyllactose.yaml data/ingredients/mapped/Digested_Serum.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  failed after the four CHEBI records when the local `sqlite:obo:micro`
  adapter hit an incomplete cache with no `rdfs_label_statement` table.
- `curl -L -sS --max-time 20 "https://www.ebi.ac.uk/ols/api/search?q=MICRO%3A0001362&ontology=micro&exact=true"`:
  returned one defining MICRO class with `obo_id: MICRO:0001362` and label
  `digested serum`.
- `curl -L -sS --max-time 20 "https://www.ebi.ac.uk/ols/api/search?q=digested%20serum&ontology=micro&exact=true"`:
  returned the same `MICRO:0001362` class.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.
- `uv run --frozen python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`:
  passed; all id-label pairs corresponded, with only full-corpus
  plausibility warnings.

## Evidence

- `data/curated/mapped_ingredients.yaml` contains the same maintained record
  body as the per-record YAML.
- The hidden/ignored-inclusive exact search over `data/ingredients`,
  `data/curated`, `mappings`, `docs/data`, `src`, `scripts`, and `tests`
  found the expected active record, generated/indexed copies, row-review
  rows, and the local in-session role curation script reference.
- A focused hidden/ignored-inclusive search of `data/ingredients` for
  `MICRO:0001362` found only `data/ingredients/mapped/Digested_Serum.yaml`.
- `mappings/ingredient_mappings_external_prefix_ols_validation.tsv`,
  `mappings/ingredient_mappings_unknown_term_triage.tsv`, and
  `mappings/ingredient_mappings_row_review_manifest.tsv` record the MICRO row
  as a prefix-coverage limitation, not a bad identity:
  prefix-specific EBI OLS resolved the exact CURIE and label.
- `mappings/culturemech_recipe_membership.tsv` has two `MICRO:0001362` rows,
  matching `occurrence_statistics.total_occurrences: 2` and
  `media_count: 2`.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:Digested_Serum` to `MICRO:0001362` with `skos:exactMatch`, canonical
  object label `digested serum`, MICRO object source, and no `other` tokens.
- Major: `nutritional_roles.PROTEIN_SOURCE` has only
  `COMPUTATIONAL_PREDICTION` evidence from in-session Claude reasoning. It is
  unsupported by claim-level source evidence.

## Completeness

- The MICRO identity, undefined-mixture classification, occurrence statistics,
  and source raw label are populated.
- Minor: top-level `notes` still repeat the original no-CAS import state,
  stale 3-media count, and curator-review request even though the record is
  now mapped to MICRO and has refreshed 2/2 occurrence statistics.
- Minor: the final SSSOM `validation_method` still ends with
  `none|UNKNOWN_TERM|2026-07-07`; the row-review manifest documents this as a
  prefix-coverage artifact after prefix-specific OLS resolution.

## Recommended Edits

- Major: replace the `PROTEIN_SOURCE` computational role in
  `data/ingredients/mapped/Digested_Serum.yaml` with source-backed role
  evidence scoped to digested serum, or remove the role if no support is
  available; then synchronize `data/curated/mapped_ingredients.yaml`.
- Minor: refresh the stale top-level `notes` so they no longer contradict the
  current mapped `MICRO:0001362` identity and 2/2 occurrence statistics.
- Minor: after the MICRO SSSOM validator dispatch is repaired, regenerate the
  final SSSOM row so `validation_method` no longer carries the obsolete
  `UNKNOWN_TERM` stamp.
