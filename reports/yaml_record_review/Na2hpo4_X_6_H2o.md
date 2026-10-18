# `data/ingredients/mapped/Na2hpo4_X_6_H2o.yaml`

## Verdict

Needs curation - major. The record is an intentionally local
`kgmicrobe.compound` identity for an unresolved hexahydrate surface and the
final local/parent SSSOM rows pass, but its `BUFFER` role is still backed only
by an in-session LLM assignment.

## Identity

- Reviewed record: `data/ingredients/mapped/Na2hpo4_X_6_H2o.yaml`.
- Identifier and grounding: `identifier:
  kgmicrobe.compound:na2hpo4_x_6_h2o` with
  `ontology_mapping.ontology_id: CHEBI:34683`, label
  `disodium hydrogenphosphate`, source `CHEBI`,
  `mapping_quality: CLOSE_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 5 CultureMech recipe occurrences across 5 media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Na2hpo4_X_2_H2o` through `Na2moo4`: exited 0 and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for the
  `CHEBI:34683` parent label.

## Evidence

- A fresh EBI OLS4 lookup resolves parent `CHEBI:34683` as active
  `disodium hydrogenphosphate`, and an exact OLS4 search for
  `disodium hydrogenphosphate hexahydrate` returned zero ChEBI documents.
- #344 records that `mediadive.compound:1580` still carries the source label for
  the six-water surface but that no exact ontology term or CAS RN has been
  verified; the local `kgmicrobe.compound` identifier and `skos:closeMatch`
  parent row preserve that unresolved state.
- `reports/hydrate_grounding.tsv` classifies the local hexahydrate row as
  `OK_LOCAL_REGISTRY_ID`.
- The final SSSOM rows include the close parent row and the exact local
  registry row, and the only `other` token is a six-water hydrate spelling.
- Major: `physicochemical_roles.BUFFER` is backed only by a
  `COMPUTATIONAL_PREDICTION` evidence object from in-session LLM reasoning, and
  the curator note explicitly marks it provisional.

## Completeness

- The local identifier, parent ChEBI term, empty chemical-properties block, 5/5
  occurrence count, rejected sibling hydrate labels, and final local registry
  row agree.
- The remaining consequential gap is source-backed evidence for the `BUFFER`
  role.

## Recommended Edits

- Major: in `data/ingredients/mapped/Na2hpo4_X_6_H2o.yaml`, either remove
  `physicochemical_roles.BUFFER` or replace its LLM placeholder with
  source-backed evidence from maintained role-text or literature inputs. Rerun
  strict validation and the role/output SSSOM checks after the role facet
  change.
