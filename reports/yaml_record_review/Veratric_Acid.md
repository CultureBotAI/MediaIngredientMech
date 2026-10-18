# `data/ingredients/mapped/Veratric_Acid.yaml`

## Verdict

Pass. The CAS-backed exact CHEBI identity, CAS RN, structure fields, aggregate
row, and final SSSOM row pass.

## Identity

- Reviewed record: `data/ingredients/mapped/Veratric_Acid.yaml`.
- Identifier and grounding: `identifier: CHEBI:296881` with matching
  `ontology_mapping.ontology_id`, label `3,4-dimethoxybenzoic acid`, source
  `CHEBI`, `mapping_quality: CAS_RN_LOOKUP`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- CAS RN: `93-07-2`.
- Chemical fields: formula `C9H10O4` and ChEBI-backed SMILES/InChI.
- Occurrences: 0.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Vanillyl_Alcohol` through `Veratric_Acid`: exited 0 and wrote zero ERROR
  rows.
- `uv run --frozen linkml-term-validator validate-data` on the CHEBI subset of
  this batch exited 0 for `Vanillyl_Alcohol`, `Vanillylmandelic_Acid`,
  `Verapamil_Hydrochloride`, and `Veratric_Acid`.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh OLS4 lookup for `CHEBI:296881` returns active label
  `3,4-dimethoxybenzoic acid`, CAS xref `93-07-2`, formula `C9H10O4`, the same
  SMILES/InChI as the YAML, and `Veratric acid` as a ChEBI synonym.
- The final SSSOM row correctly has
  `MIM:Veratric_Acid skos:exactMatch CHEBI:296881` with `CAS:93-07-2` in
  `other`.

## Issues

None.

## Completeness

- The CAS-backed CHEBI mapping, CAS RN, structure fields, aggregate copy, and
  final SSSOM row agree.

## Recommended Edits

None.
