# `data/ingredients/mapped/Sodium_phosphate_monobasic_monohydrate.yaml`

## Verdict

Needs curation - major. The exact `CHEBI:114249` monosodium phosphate
monohydrate identity, CAS-backed structure, ChEBI synonyms, occurrence count,
and final SSSOM row pass, but `BUFFER` is provisional.

## Identity

- Reviewed record:
  `data/ingredients/mapped/Sodium_phosphate_monobasic_monohydrate.yaml`.
- Identifier and grounding: `identifier: CHEBI:114249` with
  `ontology_mapping.ontology_id: CHEBI:114249`, label
  `sodium dihydrogenphosphate monohydrate`, source `CHEBI`,
  `mapping_quality: CAS_RN_LOOKUP`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 46 source occurrences across 46 FEBA media formulations.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Sodium_Thiosulfate_Pentahydrate` through `Soil`: exited 0 and wrote zero
  ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh EBI OLS4 lookup resolves active `CHEBI:114249` with label
  `sodium dihydrogenphosphate monohydrate`, CAS `10049-21-5`, and the curated
  monohydrate synonyms.
- Fresh PubChem lookup for CAS `10049-21-5` resolves to sodium phosphate
  monobasic monohydrate with the same hydrate formula, InChI, and SMILES as the
  record.
- Final SSSOM publishes same-substance monohydrate aliases plus
  `CAS:10049-21-5` in `other`.
- Major: `physicochemical_roles.BUFFER` is backed only by an in-session
  `COMPUTATIONAL_PREDICTION` with no external evidence and a
  `review recommended` note.

## Completeness

- The ChEBI ID, CAS RN, hydrate formula, structure, 46/46 occurrence count,
  active synonyms, and final exact row agree.
- The only consequential gap is the unsupported role facet.

## Recommended Edits

- Major: in
  `data/ingredients/mapped/Sodium_phosphate_monobasic_monohydrate.yaml`, replace
  the provisional `BUFFER` evidence with checked source evidence or remove the
  role.
