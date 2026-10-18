# `data/ingredients/mapped/Pipes.yaml`

## Verdict

Pass. The CultureMech import maps exactly to active `CHEBI:39033` PIPES, the
buffer role is source-backed by original CultureMech role text, and the final
SSSOM row exports only the safe CAS synonym.

## Identity

- Reviewed record: `data/ingredients/mapped/Pipes.yaml`.
- Identifier and grounding: `identifier: CHEBI:39033` with
  `ontology_mapping.ontology_id: CHEBI:39033`, label `PIPES`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 103 CultureMech occurrences across 103 recipes.

## Validation

- `uv run --frozen python scripts/validate_strict.py` exited 0 across this
  five-record batch and wrote zero ERROR rows.
- A fresh OLS4 exact search for `CHEBI:39033` resolves `CHEBI:39033` `PIPES`.
- A fresh PubChem lookup for CAS `5625-37-6` resolves to one compound CID.
- The final SSSOM row was inspected directly and maps `MIM:Pipes` exactly to
  `CHEBI:39033`.

## Evidence

- The CHEBI primary identifier, mapping target, and CAS `5625-37-6` all
  describe PIPES.
- The `BUFFER` role was extracted from raw CultureMech `Role: Buffer`
  evidence, so it is not an unsupported name-list inference.
- The raw `Role: Buffer; Properties: ...` synonyms are filtered and do not leak
  into final SSSOM `other`.
- The sibling `PIPES_Buffer` record correctly carries the stock-solution
  surfaces and keeps them out of this pure PIPES row.
- The final SSSOM row exports only `CAS:5625-37-6` in `other`.

## Completeness

- No consequential gap was found for this single-ingredient exact CHEBI
  mapping with source-backed buffer role.

## Recommended Edits

- None.
