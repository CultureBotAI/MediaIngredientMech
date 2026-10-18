# `data/ingredients/mapped/Perillyl_Alcohol.yaml`

## Verdict

Pass. The CultureBotHT import maps exactly to active `CHEBI:15420` perillyl
alcohol, and its final SSSOM synonyms are restricted to a CHEBI exact synonym
and the structured CAS.

## Identity

- Reviewed record: `data/ingredients/mapped/Perillyl_Alcohol.yaml`.
- Identifier and grounding: `identifier: CHEBI:15420` with
  `ontology_mapping.ontology_id: CHEBI:15420`, label `perillyl alcohol`,
  source `CHEBI`, `mapping_quality: EXACT_MATCH`,
  `mapping_status: MAPPED`, and `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: no CultureMech media occurrences.

## Validation

- `uv run --frozen python scripts/validate_strict.py` exited 0 across this
  five-record batch and wrote zero ERROR rows.
- A fresh OLS4 exact search for `CHEBI:15420` resolves `CHEBI:15420`
  `perillyl alcohol` and the exact synonym exported by this record.
- A local CAS checksum calculation confirmed that `536-59-4` has the expected
  check digit.
- The final SSSOM row was inspected directly and maps `MIM:Perillyl_Alcohol`
  exactly to `CHEBI:15420`.

## Evidence

- The CHEBI primary identifier, mapping target, structured formula, InChI, and
  SMILES all describe perillyl alcohol.
- The exported IUPAC synonym appears as an OLS4 exact synonym of `CHEBI:15420`.
- Final SSSOM `other` exports only the exact synonym and `CAS:536-59-4`.

## Completeness

- No consequential gap was found for this single-ingredient exact CHEBI
  mapping.

## Recommended Edits

- None.
