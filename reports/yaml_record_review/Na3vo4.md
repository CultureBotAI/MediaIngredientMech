# `data/ingredients/mapped/Na3vo4.yaml`

## Verdict

Pass. The exact `CHEBI:35607` trisodium vanadate identity, CAS-backed
structure, occurrence count, ChEBI synonyms, and final exact row agree.

## Identity

- Reviewed record: `data/ingredients/mapped/Na3vo4.yaml`.
- Identifier and grounding: `identifier: CHEBI:35607` with
  `ontology_mapping.ontology_id: CHEBI:35607`, label `trisodium vanadate`,
  source `CHEBI`, `mapping_quality: EXACT_MATCH`,
  `mapping_status: MAPPED`, and `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 2 CultureMech recipe occurrences across 2 media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Na3-citrate_X_2_H2o` through `Nabr`: exited 0 and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.

## Evidence

- A fresh EBI OLS4 lookup resolves `CHEBI:35607` as active
  `trisodium vanadate`; the term carries `Na3VO4`, the stored vanadate
  synonyms, formula `3Na.O4V`, CAS `13721-39-6`, and the same InChI and SMILES
  as the record.
- A fresh PubChem CAS lookup for `13721-39-6` resolves to trisodium vanadate
  with the same formula and InChI, confirming the chemical block.
- The final SSSOM row maps `MIM:Na3vo4` exactly to `CHEBI:35607`, uses the
  canonical object label, and keeps only ChEBI same-substance aliases plus
  `CAS:13721-39-6` in `other`.

## Completeness

- The active ChEBI term, CAS RN, formula, structure, 2/2 occurrence count, and
  final exact row agree.
- No role, component, or environment assertions are present; those optional
  slots are appropriately empty for the current record.

## Recommended Edits

- None.
