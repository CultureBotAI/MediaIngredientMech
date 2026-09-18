# `data/ingredients/mapped/Sodium_Pyrophosphate.yaml`

## Verdict

Needs curation - major. The exact `CHEBI:71240` sodium diphosphate identity,
CAS-backed tetrasodium pyrophosphate structure, ChEBI synonyms, occurrence
count, and final SSSOM row pass, but `CHELATOR` is provisional.

## Identity

- Reviewed record: `data/ingredients/mapped/Sodium_Pyrophosphate.yaml`.
- Identifier and grounding: `identifier: CHEBI:71240` with
  `ontology_mapping.ontology_id: CHEBI:71240`, label `sodium diphosphate`,
  source `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 3 source occurrences across 3 CultureMech media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Sodium_Phosphate_Dibasic` through `Sodium_Pyrophosphate_Dibasic`: exited 0
  and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh EBI OLS4 lookup resolves active `CHEBI:71240` with label
  `sodium diphosphate`, CAS `7722-88-5`, and the curated pyrophosphate
  synonyms.
- Fresh PubChem lookup for CAS `7722-88-5` resolves to tetrasodium
  pyrophosphate with the same formula, InChI, and SMILES as the record.
- Final SSSOM publishes only same-substance ChEBI aliases plus `CAS:7722-88-5`
  in `other`.
- Major: `physicochemical_roles.CHELATOR` is backed only by a
  `COMPUTATIONAL_PREDICTION` from ChEBI ancestry with a `review recommended`
  note.

## Completeness

- The ChEBI ID, canonical label, CAS RN, formula, structure, active synonyms,
  3/3 occurrence count, and final SSSOM row agree.
- The only consequential gap is the unsupported role facet.

## Recommended Edits

- Major: in `data/ingredients/mapped/Sodium_Pyrophosphate.yaml`, replace the
  provisional `CHELATOR` evidence with checked source evidence or remove the
  role.
