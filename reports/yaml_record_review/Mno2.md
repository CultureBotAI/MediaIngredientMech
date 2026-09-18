# `data/ingredients/mapped/Mno2.yaml`

## Verdict

Pass. The exact `CHEBI:136511` manganese dioxide identity, CAS, structure,
row-review confirmation, occurrence count, and final SSSOM row pass.

## Identity

- Reviewed record: `data/ingredients/mapped/Mno2.yaml`.
- Identifier and grounding: `identifier: CHEBI:136511` with
  `ontology_mapping.ontology_id: CHEBI:136511`, label `manganese dioxide`,
  source `CHEBI`, `mapping_quality: EXACT_MATCH`,
  `mapping_status: MAPPED`, and `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: four CultureMech recipe occurrences.
- Chemical identity: CAS `1313-13-9`, formula `MnO2`, SMILES, and InChI.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Mncl2` through `Mnso4`: exited 0 and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for all five
  CHEBI-primary records in the same batch.

## Evidence

- `mappings/ingredient_mappings_oak_ols_review.tsv` and
  `mappings/ingredient_mappings_row_review_manifest.tsv` confirm `MIM:Mno2` to
  `CHEBI:136511`.
- A fresh EBI OLS4 lookup resolves `CHEBI:136511` as active
  `manganese dioxide`.
- The final SSSOM publishes one `skos:exactMatch` row from `MIM:Mno2` to
  `CHEBI:136511`.

## Completeness

- The target identity, CAS, formula, 4/4 occurrence count, synonym set, and
  final exact row agree.
- The record does not publish unsupported roles or stale CAS values.

## Recommended Edits

- None.
