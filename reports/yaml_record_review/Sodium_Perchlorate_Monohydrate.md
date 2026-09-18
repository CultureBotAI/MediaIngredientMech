# `data/ingredients/mapped/Sodium_Perchlorate_Monohydrate.yaml`

## Verdict

Needs curation - major. The CAS identity, monohydrate structure, close ChEBI
parent row, and exact CAS registry row pass, but `ELECTRON_ACCEPTOR` is still a
provisional in-session prediction.

## Identity

- Reviewed record:
  `data/ingredients/mapped/Sodium_Perchlorate_Monohydrate.yaml`.
- Identifier and grounding: `identifier: cas:7791-07-3` with
  `ontology_mapping.ontology_id: CHEBI:132103`, label `sodium perchlorate`,
  source `CHEBI`, `mapping_quality: CLOSE_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 1 source occurrence in 1 CultureMech medium.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Sodium_Perchlorate` through `Sodium_Phosphate_Buffer`: exited 0 and wrote
  zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-parent
  record.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh EBI OLS4 lookup resolves active `CHEBI:132103` as the anhydrous
  `sodium perchlorate` parent, agreeing with the #342 regrade from
  `NARROW_MATCH` to `CLOSE_MATCH`.
- Fresh PubChem lookup for CAS `7791-07-3` resolves to sodium perchlorate
  monohydrate with the same hydrate formula, InChI, SMILES, and CID as the
  record.
- Final SSSOM preserves the close ChEBI parent row and the exact CAS registry
  row; the only `other` payload is the same-substance `CAS:7791-07-3`.
- Major: `cellular_metabolic_roles.ELECTRON_ACCEPTOR` is backed only by an
  in-session `COMPUTATIONAL_PREDICTION` with no external evidence and a
  `review recommended` note.

## Completeness

- The CAS RN, monohydrate formula, structure, parent mapping, registry row, and
  1/1 occurrence count agree.
- The only consequential gap is the unsupported role facet.

## Recommended Edits

- Major: in `data/ingredients/mapped/Sodium_Perchlorate_Monohydrate.yaml`,
  remove `cellular_metabolic_roles.ELECTRON_ACCEPTOR` unless a checked source
  supports perchlorate monohydrate in the reviewed medium context.
