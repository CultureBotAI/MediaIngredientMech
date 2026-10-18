# `data/ingredients/mapped/Myristic_Acid.yaml`

## Verdict

Pass. The CAS-backed `CHEBI:28875` tetradecanoic acid identity, myristic-acid
synonym, structure, CAS provenance, and final exact row pass.

## Identity

- Reviewed record: `data/ingredients/mapped/Myristic_Acid.yaml`.
- Identifier and grounding: `identifier: CHEBI:28875` with
  `ontology_mapping.ontology_id: CHEBI:28875`, label `tetradecanoic acid`,
  source `CHEBI`, `mapping_quality: CAS_RN_LOOKUP`,
  `mapping_status: MAPPED`, and `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: no direct CultureMech recipe occurrences.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Myo-inositol` through `N-Acetyl-D-glucosamine_6-phosphate_Sodium_Salt`:
  exited 0 and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.

## Evidence

- A fresh EBI OLS4 lookup resolves `CHEBI:28875` as active `tetradecanoic acid`
  with `MYRISTIC ACID`, `Myristic acid`, and `myristic acid` as exact synonyms.
- A fresh PubChem lookup for CAS `544-63-8` returns formula `C14H28O2` and the
  same InChI stored on the record.
- The final SSSOM publishes one `skos:exactMatch` row from
  `MIM:Myristic_Acid` to `CHEBI:28875` with `CAS:544-63-8` in `other`.

## Completeness

- The active ChEBI target, CAS RN, synonym-grade history, structure, and final
  row agree.
- The record does not assert components, roles, or non-synonym final `other`
  text.

## Recommended Edits

- None.
