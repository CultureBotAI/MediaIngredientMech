# `data/ingredients/mapped/Xanthyletin.yaml`

## Verdict

Pass. The exact `CHEBI:10073` Xanthyletin identity, structure fields, CAS RN,
aggregate row, and final SSSOM row pass.

## Identity

- Reviewed record: `data/ingredients/mapped/Xanthyletin.yaml`.
- Identifier and grounding: `identifier: CHEBI:10073` with matching
  `ontology_mapping.ontology_id`, label `Xanthyletin`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- CAS RN: `553-19-5`.
- Chemical fields: formula `C14H12O3` with populated InChI and SMILES strings.
- Synonyms: none.
- Occurrences: zero.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Xanthocidin` through `Xylan_From_Beechwood`: exited 0 and wrote zero ERROR
  rows.
- `uv run --frozen linkml-term-validator validate-data` on the four
  CHEBI-primary records in this batch exited 0.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh OLS4 lookup for `CHEBI:10073` returns active label `Xanthyletin`, CAS
  `553-19-5`, formula `C14H12O3`, and structure strings matching the local
  record.
- The final SSSOM row correctly has
  `MIM:Xanthyletin skos:exactMatch CHEBI:10073`.

## Issues

None.

## Completeness

- The exact CHEBI mapping, CAS RN, structure fields, aggregate copy, and final
  SSSOM row agree.

## Recommended Edits

None.
