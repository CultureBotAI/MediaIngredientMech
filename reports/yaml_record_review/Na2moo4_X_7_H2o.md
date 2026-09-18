# `data/ingredients/mapped/Na2moo4_X_7_H2o.yaml`

## Verdict

Needs curation - major. The exact `CHEBI:86473` sodium molybdate heptahydrate
identity, withdrawn wrong CAS RN, hydrate formula, occurrence count, and final
exact row pass, but the `TRACE_ELEMENT` role is still a provisional
name-pattern prediction.

## Identity

- Reviewed record: `data/ingredients/mapped/Na2moo4_X_7_H2o.yaml`.
- Identifier and grounding: `identifier: CHEBI:86473` with
  `ontology_mapping.ontology_id: CHEBI:86473`, label
  `sodium molybdate heptahydrate`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 6 CultureMech recipe occurrences across 6 media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Na2moo42h2o` through `Na2s2o3`: exited 0 and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.

## Evidence

- A fresh EBI OLS4 lookup resolves `CHEBI:86473` as active
  `sodium molybdate heptahydrate`, with heptahydrate synonyms on the same term.
- `reports/hydrate_grounding.tsv` classifies `CHEBI:86473` as
  `OK_HYDRATE_TERM`; the final SSSOM row maps exactly to the heptahydrate and
  keeps only heptahydrate synonyms in `other`.
- The #320/#334 repair correctly removed CAS `10102-40-6`; that CAS belongs to
  sodium molybdate dihydrate, not the heptahydrate.
- Major: `nutritional_roles.TRACE_ELEMENT` is backed only by
  `COMPUTATIONAL_PREDICTION` evidence from `infer_roles_from_name_lists`, and
  the curator note marks the role provisional.

## Completeness

- The active ChEBI target, no-CAS state, hydrate formula, structure, 6/6
  occurrence count, and final exact row agree.
- The remaining consequential gap is source-backed evidence for the
  `TRACE_ELEMENT` role.

## Recommended Edits

- Major: in `data/ingredients/mapped/Na2moo4_X_7_H2o.yaml`, either remove
  `nutritional_roles.TRACE_ELEMENT` or replace its name-pattern placeholder with
  source-backed evidence from maintained role-text or literature inputs. Rerun
  strict validation and the role/output SSSOM checks after the role facet
  change.
