# `data/ingredients/mapped/Verapamil_Hydrochloride.yaml`

## Verdict

Pass. The CAS-backed exact CHEBI hydrochloride identity, CAS RN, formula,
synonyms, aggregate row, and final SSSOM row pass.

## Identity

- Reviewed record: `data/ingredients/mapped/Verapamil_Hydrochloride.yaml`.
- Identifier and grounding: `identifier: CHEBI:53188` with matching
  `ontology_mapping.ontology_id`, label `verapamil hydrochloride`, source
  `CHEBI`, `mapping_quality: CAS_RN_LOOKUP`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- CAS RN: `152-11-4`.
- Synonyms: two exact IUPAC synonyms.
- Chemical fields: formula `C27H38N2O4.HCl`.
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

- Fresh OLS4 lookup for `CHEBI:53188` returns active label
  `verapamil hydrochloride`, CAS xref `152-11-4`, formula
  `C27H38N2O4.HCl`, and the same two IUPAC exact synonyms exported in final
  SSSOM.
- The final SSSOM row correctly has
  `MIM:Verapamil_Hydrochloride skos:exactMatch CHEBI:53188`, with the
  hydrochloride-specific synonyms and `CAS:152-11-4` in `other`.

## Issues

None.

## Completeness

- The CAS-backed CHEBI mapping, CAS RN, formula, synonyms, aggregate copy, and
  final SSSOM row agree.

## Recommended Edits

None.
