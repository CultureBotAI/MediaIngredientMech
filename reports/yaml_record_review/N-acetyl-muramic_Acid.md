# `data/ingredients/mapped/N-acetyl-muramic_Acid.yaml`

## Verdict

Pass with minor issues. The rejected `n-Acetyl-muramic acid` tombstone was
absorbed into the active `CHEBI:47965` `N-acetylmuramic acid` record and is
correctly absent from the final SSSOM, but it still carries stale pre-merge
type, mapping, and structure fields that now serve only as loser-record
provenance.

## Identity

- Reviewed record: `data/ingredients/mapped/N-acetyl-muramic_Acid.yaml`.
- Identifier and grounding: `identifier: CHEBI:47965` with
  `ontology_mapping.ontology_id: CHEBI:47966`, label
  `aldehydo-N-acetylmuramic acid`, source `CHEBI`,
  `mapping_quality: CAS_RN_LOOKUP`, `mapping_status: REJECTED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: zero occurrences after the #398 merge transferred the ten
  source occurrences into `data/ingredients/mapped/N-acetylmuramic_Acid.yaml`.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `N-acetyl-lysine` through `N-acetylmuramic_Acid`: exited 0 and wrote zero
  ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  rejected tombstone.

## Evidence

- A fresh EBI OLS4 lookup resolves `CHEBI:47966` as active
  `aldehydo-N-acetylmuramic acid`, with `cas:10597-89-4`, formula `C11H19NO8`,
  and synonyms matching the tombstone synonym payload.
- A fresh ignored/hidden-inclusive search of
  `mappings/ingredient_mappings.sssom.tsv` found no final
  `MIM:N-acetyl-muramic_Acid` row, which is the intended publication state for
  this rejected merge loser.
- `docs/data/label_index.csv` still resolves the loser label and aliases to the
  active `CHEBI:47965` winner, so lookups on the old surface are not lost.

## Completeness

- The #398 curation-history event fully documents the merge into
  `CHEBI:47965`, why MIM prefers the class-like ChEBI node for the active KG
  subject, and why the purchasable `10597-89-4` CAS moved to the winner's
  `supplied_form`.
- Minor: the rejected tombstone still carries pre-merge
  `ontology_mapping`, `chemical_properties`, and `ingredient_type` fields,
  which can make the inactive file look like a live aldehydo mapping unless a
  reader first notices `mapping_status: REJECTED`.

## Recommended Edits

- Minor: in `data/ingredients/mapped/N-acetyl-muramic_Acid.yaml`, simplify the
  rejected tombstone during a dedicated tombstone-cleanup pass by preserving
  the old `CHEBI:47966` details as provenance and removing any live-looking
  type or structure fields that are no longer active assertions.
