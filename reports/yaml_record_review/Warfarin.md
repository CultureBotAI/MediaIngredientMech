# `data/ingredients/mapped/Warfarin.yaml`

## Verdict

Pass. The exact `CHEBI:10033` warfarin identity, formula, CAS RN, reviewed
IUPAC synonym, aggregate row, and final SSSOM row pass.

## Identity

- Reviewed record: `data/ingredients/mapped/Warfarin.yaml`.
- Identifier and grounding: `identifier: CHEBI:10033` with matching
  `ontology_mapping.ontology_id`, label `warfarin`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- CAS RN: `81-81-2`.
- Chemical fields: formula `C19H16O4`.
- Synonyms: one reviewed exact IUPAC synonym,
  `rac-4-hydroxy-3-(3-oxo-1-phenylbutyl)-2H-1-benzopyran-2-one`.
- Occurrences: zero.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Voso4_X_N_H2o` through `Washed_agar`: exited 0 and wrote zero ERROR rows.
- `uv run --frozen linkml-term-validator validate-data` on the three
  CHEBI-primary records in this batch exited 0.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh OLS4 lookup for `CHEBI:10033` returns active label `warfarin`, formula
  `C19H16O4`, CAS `81-81-2`, and the reviewed IUPAC synonym.
- The final SSSOM row correctly has
  `MIM:Warfarin skos:exactMatch CHEBI:10033` and exports the reviewed IUPAC
  synonym in `other`.

## Issues

None.

## Completeness

- The exact CHEBI mapping, CAS RN, formula, aggregate copy, and final SSSOM row
  agree.

## Recommended Edits

None.
