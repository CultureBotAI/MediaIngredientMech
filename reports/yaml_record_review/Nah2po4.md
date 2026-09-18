# `data/ingredients/mapped/Nah2po4.yaml`

## Verdict

Needs curation - major. The exact `CHEBI:37585` anhydrous sodium
dihydrogenphosphate identity, CAS-backed structure, `BUFFER` role, hidden
hydrate rejection, and final exact SSSOM row mostly agree, but final SSSOM
still publishes a malformed hydrate-like label as an exact synonym.

## Identity

- Reviewed record: `data/ingredients/mapped/Nah2po4.yaml`.
- Identifier and grounding: `identifier: CHEBI:37585` with
  `ontology_mapping.ontology_id: CHEBI:37585`, label
  `sodium dihydrogenphosphate`, source `CHEBI`,
  `mapping_quality: SYNONYM_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 237 CultureMech recipe occurrences across 237 media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Nacl` through `Nah2po4`: exited 0 and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.

## Evidence

- A fresh EBI OLS4 lookup resolves `CHEBI:37585` as active
  `sodium dihydrogenphosphate` with formula `H2O4P.Na`, CAS `7558-80-7`, the
  `NaH2PO4` and anhydrous monobasic-phosphate synonyms, and the same InChI and
  SMILES as the record.
- A fresh PubChem CAS lookup for `7558-80-7` resolves to monosodium phosphate
  with the same InChI, confirming the chemical block.
- `mapping_quality: SYNONYM_MATCH` honestly records that this record's label
  resolves through a synonym rather than the primary ChEBI label; the SSSOM
  `skos:exactMatch` predicate is still correct under Rule D.
- The `BUFFER` role is supported by imported CultureMech `Buffer` source role
  text.
- The middle-dot and explicit monohydrate/dihydrate labels are now
  `REJECTED_LABEL` entries and are filtered out of final SSSOM `other`.
- Major: `NaH PO .2H O` remains an active `EXACT_SYNONYM` and still publishes
  in final SSSOM. It is a malformed formula-style label and resembles the
  rejected hydrate spellings rather than a resolving synonym for anhydrous
  `CHEBI:37585`.

## Completeness

- The active ChEBI term, CAS RN, formula, structure, 237/237 occurrence count,
  role evidence, and final exact row otherwise agree.
- The only consequential gap is the malformed kg-microbe synonym that escaped
  the hidden-hydrate cleanup.

## Recommended Edits

- Major: in `data/ingredients/mapped/Nah2po4.yaml`, reject or delete
  `NaH PO .2H O`, then rebuild final SSSOM so `other` keeps only real
  anhydrous `CHEBI:37585` synonyms plus `CAS:7558-80-7`.
