# `data/ingredients/mapped/Peptone.yaml`

## Verdict

Needs curation; major. The generic Peptone identity resolves to
`MICRO:0000178`, but the `PROTEIN_SOURCE` role is only a provisional name-list
prediction and final SSSOM exports a concentration-truncated raw synonym.

## Identity

- Reviewed record: `data/ingredients/mapped/Peptone.yaml`.
- Identifier and grounding: `identifier: MICRO:0000178` with
  `ontology_mapping.ontology_id: MICRO:0000178`, label `peptone`, source
  `MICRO`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: UNDEFINED_MIXTURE`.
- Occurrences: 2,255 total occurrences across 2,251 CultureMech recipes, plus
  48 MicrobeDecoder `BacDive_Metabolite_utilization` occurrences.

## Validation

- `uv run --frozen python scripts/validate_strict.py` exited 0 across this
  five-record batch and wrote zero ERROR rows.
- A fresh prefix-specific OLS4 search resolves `MICRO:0000178` to `peptone`.
- `mappings/ingredient_mappings_unknown_term_triage.tsv` classifies the final
  SSSOM `UNKNOWN_TERM` grade as a missing-prefix validator coverage issue, not
  as a bad term.
- The final SSSOM row was inspected directly and maps `MIM:Peptone` exactly to
  `MICRO:0000178`.

## Evidence

- The MICRO primary identifier and mapping target denote peptone.
- `Peptones` is a harmless plural raw synonym from a reviewed MicrobeDecoder
  duplicate merge.
- Major: `Peptone (0.01 %` is a concentration-truncated source string, not a
  real peptone synonym, but final SSSOM exports it in `other`.
- Major: the `PROTEIN_SOURCE` role is supported only by
  `COMPUTATIONAL_PREDICTION` evidence from `infer_roles_from_name_lists`.

## Completeness

- The exact MICRO identity is complete enough.
- Role evidence and the final synonym surface remain incomplete while the
  provisional nutritional role and concentration-truncated `other` token are
  still present.

## Recommended Edits

- Major: in `data/ingredients/mapped/Peptone.yaml`, retype or suppress
  `Peptone (0.01 %` so it remains occurrence provenance only and no longer
  appears in `mappings/ingredient_mappings.sssom.tsv`.
- Major: replace `nutritional_roles.PROTEIN_SOURCE` with source-backed
  evidence or remove the provisional role facet until it is curated.
