# `data/ingredients/mapped/Na2so3_X_5_H2o.yaml`

## Verdict

Needs curation - major. The record preserves the sodium sulfite pentahydrate
surface, but it still asserts an exact final SSSOM row to anhydrous
`CHEBI:86477`, keeps anhydrous synonyms, and stores an anhydrous InChI/SMILES
next to a manually hydrated formula.

## Identity

- Reviewed record: `data/ingredients/mapped/Na2so3_X_5_H2o.yaml`.
- Identifier and grounding: `identifier: CHEBI:86477` with
  `ontology_mapping.ontology_id: CHEBI:86477`, label `sodium sulfite`, source
  `CHEBI`, `mapping_quality: SYNONYM_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 26 CultureMech recipe occurrences across 26 media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Na2so3_X_5_H2o` through `Na2wo4_X_2_H2o`: exited 0 and wrote zero ERROR
  rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.

## Evidence

- A fresh EBI OLS4 lookup resolves `CHEBI:86477` as active `sodium sulfite`,
  formula `2Na.O3S`, and CAS `7757-83-7`; those are the anhydrous identity.
- Major: the preferred term names a pentahydrate, but no exact ChEBI
  pentahydrate target was verified and the record still maps exactly to the
  anhydrous `CHEBI:86477` term in final SSSOM.
- Major: the #334 CAS repair removed the anhydrous CAS without replacing it,
  but the `chemical_properties` block still carries the anhydrous InChI and
  SMILES from `CHEBI:86477` next to a manually appended `5H2O` formula.
- Major: the only published final `other` tokens are anhydrous sodium sulfite
  synonyms from `CHEBI:86477`, not pentahydrate synonyms.

## Completeness

- The CAS field is correctly empty after the #334 repair.
- The remaining consequential gaps are the anhydrous exact grounding,
  anhydrous final synonyms, and mixed hydrate/anhydrous structure fields.

## Recommended Edits

- Major: mint or assign a hydrate-specific local identity for
  `data/ingredients/mapped/Na2so3_X_5_H2o.yaml`; keep `CHEBI:86477` only as an
  anhydrous parent row under the mapping semantics, then rebuild final SSSOM and
  rerun final SSSOM validation.
- Major: remove the anhydrous InChI/SMILES unless hydrate-specific structure
  evidence is curated, and drop the anhydrous synonyms from this hydrate record.
  Rerun strict validation and product label validation after the cleanup.
