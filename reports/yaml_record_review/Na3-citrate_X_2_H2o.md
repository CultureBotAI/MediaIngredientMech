# `data/ingredients/mapped/Na3-citrate_X_2_H2o.yaml`

## Verdict

Needs curation - major. The exact `CHEBI:32142` sodium citrate dihydrate
identity, CAS-backed structure, duplicate merges, occurrence count, `BUFFER`
role, and trihydrate rejection pass, but final SSSOM still publishes malformed,
concentration-qualified, and hydrate-erasing labels as dihydrate synonyms.

## Identity

- Reviewed record: `data/ingredients/mapped/Na3-citrate_X_2_H2o.yaml`.
- Identifier and grounding: `identifier: CHEBI:32142` with
  `ontology_mapping.ontology_id: CHEBI:32142`, label
  `sodium citrate dihydrate`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 277 CultureMech recipe occurrences across 277 media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Na3-citrate_X_2_H2o` through `Nabr`: exited 0 and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.

## Evidence

- A fresh EBI OLS4 lookup resolves `CHEBI:32142` as active
  `sodium citrate dihydrate`; the term carries formula `C6H5O7.2H2O.3Na`, CAS
  `6132-04-3`, and the same InChI and SMILES as the record.
- A fresh PubChem CAS lookup for `6132-04-3` resolves to trisodium citrate
  dihydrate with the same InChI, confirming the chemical block.
- The absorbed duplicates keep CAS-selected sodium citrate and the alternative
  trisodium-citrate-dihydrate surface on the hydrate-specific `CHEBI:32142`
  identity.
- The `BUFFER` role is supported by CultureMech `DATABASE_ENTRY` evidence whose
  curator note preserves the original `Buffer` role text.
- The #251 repair correctly marked the trihydrate label as `REJECTED_LABEL`, and
  that rejected label is filtered from final SSSOM.
- Major: final SSSOM `other` publishes malformed `Na2citrate x 2 H2O` and
  `Na2citrate` labels, a concentration-qualified
  `Na3-citrate x 2 H2O (0.6 g/l stock solution)` label, the hydrate-erasing
  `Na3Citrate` label, and typoed `Trisodium citrate dehydrate`.

## Completeness

- The active ChEBI term, CAS RN, formula, structure, 277/277 occurrence count,
  duplicate merges, buffer role, rejected trihydrate label, and exact final row
  otherwise agree.
- The remaining consequential gap is cleanup of malformed and
  hydrate-erasing labels in the final synonym surface.

## Recommended Edits

- Major: in `data/ingredients/mapped/Na3-citrate_X_2_H2o.yaml`, demote or reject
  the malformed `Na2citrate` forms, the stock-solution label, anhydrous/generic
  citrate labels, and the `dehydrate` typo so they no longer publish as exact
  `CHEBI:32142` synonyms. Rebuild final SSSOM and rerun final SSSOM validation
  plus product label validation.
