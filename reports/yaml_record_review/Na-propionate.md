# `data/ingredients/mapped/Na-propionate.yaml`

## Verdict

Needs curation - major. The exact `CHEBI:132106` sodium propionate identity,
CAS-backed structure, source-backed carbon role, duplicate merge, occurrence
count, and final SSSOM row pass, but the `ENERGY_SOURCE` facet is still
provisional.

## Identity

- Reviewed record: `data/ingredients/mapped/Na-propionate.yaml`.
- Identifier and grounding: `identifier: CHEBI:132106` with
  `ontology_mapping.ontology_id: CHEBI:132106`, label `sodium propionate`,
  source `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 49 CultureMech recipe occurrences across 49 media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Na-orotate` through `Na-silicate`: exited 0 and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.

## Evidence

- A fresh EBI OLS4 lookup resolves `CHEBI:132106` as active
  `sodium propionate`, with `cas:137-40-6`, formula `C3H5O2.Na`, the stored
  structure, and the accepted propionate synonyms.
- The `CARBON_SOURCE` facet is source-backed by CultureMech original role text
  that explicitly says `Carbon Source`; the raw role/property strings are
  correctly absent from final SSSOM `other`.
- The #505 merge correctly folded the duplicate live `Propionate (sodium salt)`
  record into this sodium propionate record.
- Major: `nutritional_roles.ENERGY_SOURCE` is backed only by automatic
  `COMPUTATIONAL_PREDICTION` evidence, and its curator note explicitly marks it
  provisional.

## Completeness

- The active ChEBI target, CAS RN, formula, structure, exact synonyms, 49/49
  occurrence count, duplicate merge, source-backed `CARBON_SOURCE` role, and
  final exact mapping row agree.
- The only consequential gap is the unsupported inferred energy role.

## Recommended Edits

- Major: in `data/ingredients/mapped/Na-propionate.yaml`, either remove
  `nutritional_roles.ENERGY_SOURCE` or replace its computational placeholder
  with source-backed evidence from maintained occurrence, role-text, or
  literature inputs. Rerun strict validation and the role/output SSSOM checks
  after the role facet changes.
