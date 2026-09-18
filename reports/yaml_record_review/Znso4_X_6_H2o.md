# `data/ingredients/mapped/Znso4_X_6_H2o.yaml`

## Verdict

Needs curation. The exact `CHEBI:132762` zinc sulfate hexahydrate identity,
CAS, structure, hydrate-preserving synonyms, aggregate row, and final SSSOM row
pass, but the `TRACE_ELEMENT` role is only a provisional name-pattern
inference.

## Identity

- Reviewed record: `data/ingredients/mapped/Znso4_X_6_H2o.yaml`.
- Identifier and grounding: `identifier: CHEBI:132762` with matching
  `ontology_mapping.ontology_id`, canonical label
  `zinc sulfate hexahydrate`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- CAS RN: `13986-24-8`.
- Structure: formula `6H2O.O4S.Zn` with populated InChI and SMILES for the
  hexahydrate.
- Synonyms: one formulaic hydrate form, `zinc sulfate hexahydrate`, and the
  ChEBI exact synonym `zinc sulfate--water (1/6)`.
- Role: `TRACE_ELEMENT` with `COMPUTATIONAL_PREDICTION` evidence from a
  provisional curated name-pattern rule.
- Occurrences: three CultureMech occurrences across three media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on this 5-file batch:
  exited 0 and wrote zero ERROR rows.
- `uv run linkml-term-validator validate-data` passed for this CHEBI-primary
  record with `--labels`.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.
- Fresh OLS4 exact search for `zinc sulfate hexahydrate` in CHEBI returned the
  active `CHEBI:132762` label `zinc sulfate hexahydrate`.

## Evidence

- The final SSSOM row correctly exports
  `MIM:Znso4_X_6_H2o skos:exactMatch CHEBI:132762`.
- The final `other` field preserves only the formulaic hexahydrate synonym, the
  ChEBI exact synonym, and matching `CAS:13986-24-8`.
- The nutritional role came from `infer_roles_from_name_lists` rather than the
  original CultureMech role text.

## Issues

- Major: `nutritional_roles.TRACE_ELEMENT` rests on
  `COMPUTATIONAL_PREDICTION` evidence whose note says the curated name-pattern
  rule is provisional and still needs review.

## Completeness

- The exact CHEBI identifier, CAS, structure fields, single-ingredient type,
  aggregate copy, and final SSSOM row agree.
- The trace-element role should be replaced with source-backed evidence or
  removed.

## Recommended Edits

- Replace or remove `nutritional_roles.TRACE_ELEMENT`; keep it only if a
  maintained source supports zinc sulfate hexahydrate as a trace element in
  media.
- Rerun strict validation, SSSOM invariant validation, and any role-focused
  audits after editing.
