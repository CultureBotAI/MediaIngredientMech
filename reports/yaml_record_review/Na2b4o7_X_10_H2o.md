# `data/ingredients/mapped/Na2b4o7_X_10_H2o.yaml`

## Verdict

Needs curation - major. The record exactly denotes
`CHEBI:131366` disodium tetraborate decahydrate and publishes only hydrate-form
surface forms in final SSSOM, but its `BUFFER` role was inferred from ChEBI
ancestry and is still marked provisional.

## Identity

- Reviewed record: `data/ingredients/mapped/Na2b4o7_X_10_H2o.yaml`.
- Identifier and grounding: `identifier: CHEBI:131366` with
  `ontology_mapping.ontology_id: CHEBI:131366`, label
  `disodium tetraborate decahydrate`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 263 CultureMech recipe occurrences across 263 media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Na2_Alpha-ketoglutarate` through `Na2co3`: exited 0 and wrote zero ERROR
  rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.

## Evidence

- A fresh EBI OLS4 lookup resolves `CHEBI:131366` as active
  `disodium tetraborate decahydrate`, with formula `10H2O.H4B4O9.2Na` and the
  stored structure for the decahydrate form.
- `reports/hydrate_grounding.tsv` classifies the `CHEBI:131366` row as
  `OK_HYDRATE_TERM`; the record and final SSSOM preserve the decahydrate
  boundary rather than collapsing to anhydrous `CHEBI:38892`.
- The final SSSOM row for `MIM:Na2b4o7_X_10_H2o` maps exactly to
  `CHEBI:131366`; its `other` values are spelling, spacing, dot, and borax
  aliases for the decahydrate subject.
- Major: `physicochemical_roles.BUFFER` is backed only by
  `COMPUTATIONAL_PREDICTION` evidence from the `CHEBI:35225` ancestry rule, and
  the curator note explicitly marks the role provisional.

## Completeness

- The active ChEBI target, hydrate formula, structure, 263/263 occurrence
  count, hydrate synonyms, and final exact row agree.
- The only consequential gap is source-backed evidence for the `BUFFER` role
  facet.

## Recommended Edits

- Major: in `data/ingredients/mapped/Na2b4o7_X_10_H2o.yaml`, either remove
  `physicochemical_roles.BUFFER` or replace its ChEBI-ancestry placeholder with
  source-backed evidence from maintained role-text or literature inputs. Rerun
  strict validation and the role/output SSSOM checks after the role facet
  change.
