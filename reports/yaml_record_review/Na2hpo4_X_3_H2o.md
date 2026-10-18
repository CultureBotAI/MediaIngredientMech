# `data/ingredients/mapped/Na2hpo4_X_3_H2o.yaml`

## Verdict

Pass. The record is an intentionally local
`kgmicrobe.compound:na2hpo4_x_3_h2o` identity for an unresolved trihydrate
surface, close-matches the anhydrous `CHEBI:34683` parent, carries no
unverified structure, and publishes the required local exact sibling row with
no extra `other` synonyms.

## Identity

- Reviewed record: `data/ingredients/mapped/Na2hpo4_X_3_H2o.yaml`.
- Identifier and grounding: `identifier:
  kgmicrobe.compound:na2hpo4_x_3_h2o` with
  `ontology_mapping.ontology_id: CHEBI:34683`, label
  `disodium hydrogenphosphate`, source `CHEBI`,
  `mapping_quality: CLOSE_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 4 CultureMech recipe occurrences across 4 media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Na2hpo4_X_2_H2o` through `Na2moo4`: exited 0 and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for the
  `CHEBI:34683` parent label.

## Evidence

- A fresh EBI OLS4 lookup resolves parent `CHEBI:34683` as active
  `disodium hydrogenphosphate`, and an exact OLS4 search for
  `disodium hydrogenphosphate trihydrate` returned zero ChEBI documents.
- #344 records that `mediadive.compound:525` still carries the source label for
  the three-water surface but that no exact ontology term or CAS RN has been
  verified; the local `kgmicrobe.compound` identifier and `skos:closeMatch`
  parent row preserve that unresolved state.
- `reports/hydrate_grounding.tsv` classifies the local trihydrate row as
  `OK_LOCAL_REGISTRY_ID`.
- The final SSSOM rows include the close parent row and the exact local
  registry row. Both rows leave `other` empty.
- `physicochemical_roles.BUFFER` is source-backed by CultureMech raw role text
  naming `Buffer`.

## Completeness

- The local identifier, parent ChEBI term, empty chemical-properties block,
  source-backed buffer role, 4/4 occurrence count, rejected sibling hydrate
  labels, and final local registry row agree.

## Recommended Edits

- None.
