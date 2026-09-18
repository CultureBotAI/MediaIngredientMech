# `data/ingredients/mapped/Peroxynitrite.yaml`

## Verdict

Pass. The CultureBotHT import maps exactly to active `CHEBI:25941`
peroxynitrite, and its final SSSOM synonyms are real exact synonyms or the
structured CAS.

## Identity

- Reviewed record: `data/ingredients/mapped/Peroxynitrite.yaml`.
- Identifier and grounding: `identifier: CHEBI:25941` with
  `ontology_mapping.ontology_id: CHEBI:25941`, label `peroxynitrite`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: no CultureMech media occurrences.

## Validation

- `uv run --frozen python scripts/validate_strict.py` exited 0 across this
  five-record batch and wrote zero ERROR rows.
- A fresh OLS4 exact search for `CHEBI:25941` resolves `CHEBI:25941`
  `peroxynitrite` and the two exact synonyms exported by this record.
- A local CAS checksum calculation confirmed that `14042-01-4` has the
  expected check digit.
- The final SSSOM row was inspected directly and maps `MIM:Peroxynitrite`
  exactly to `CHEBI:25941`.

## Evidence

- The CHEBI primary identifier, mapping target, structured formula, InChI, and
  SMILES all describe peroxynitrite.
- `azoperoxoite` and `oxidoperoxidonitrate(1-)` appear as OLS4 exact synonyms
  of `CHEBI:25941`.
- Final SSSOM `other` exports only those exact synonyms and `CAS:14042-01-4`.

## Completeness

- No consequential gap was found for this single-ingredient exact CHEBI
  mapping.

## Recommended Edits

- None.
