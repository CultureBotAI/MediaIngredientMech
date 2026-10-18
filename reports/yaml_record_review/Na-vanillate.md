# `data/ingredients/mapped/Na-vanillate.yaml`

## Verdict

Needs curation - major. The exact `CHEBI:132748` sodium vanillate identity,
structure, occurrence count, synonyms, and final SSSOM row pass, but the
`CARBON_SOURCE` facet is still an unsupported provisional LLM assignment.

## Identity

- Reviewed record: `data/ingredients/mapped/Na-vanillate.yaml`.
- Identifier and grounding: `identifier: CHEBI:132748` with
  `ontology_mapping.ontology_id: CHEBI:132748`, label `sodium vanillate`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 3 CultureMech recipe occurrences across 3 media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Na-stearate` through `Na2-edta`: exited 0 and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.

## Evidence

- A fresh EBI OLS4 lookup resolves `CHEBI:132748` as active
  `sodium vanillate`, with formula `C8H7O4.Na`, the stored structure, and the
  accepted IUPAC synonym.
- The final SSSOM exact row for `MIM:Na-vanillate` keeps only the accepted
  IUPAC synonym and `CAS:28508-48-7` in `other`.
- Major: `nutritional_roles.CARBON_SOURCE` is backed only by a
  `COMPUTATIONAL_PREDICTION` whose curator note calls it a provisional
  in-session LLM assignment. No inspected source in this record supports sodium
  vanillate's use as a carbon source.

## Completeness

- The active ChEBI target, formula, structure, exact synonym, 3/3 occurrence
  count, and final exact mapping row agree.
- The only consequential gap is the unsupported `CARBON_SOURCE` role facet.

## Recommended Edits

- Major: in `data/ingredients/mapped/Na-vanillate.yaml`, either remove
  `nutritional_roles.CARBON_SOURCE` or replace its computational placeholder
  with source-backed evidence from maintained occurrence, role-text, or
  literature inputs. Rerun strict validation and the role/output SSSOM checks
  after the role facet changes.
