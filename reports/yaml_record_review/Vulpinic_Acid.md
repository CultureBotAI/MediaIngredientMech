# `data/ingredients/mapped/Vulpinic_Acid.yaml`

## Verdict

Pass. The exact `CHEBI:144250` Vulpinic acid identity, structure fields, CAS
RN, aggregate row, and final SSSOM row pass.

## Identity

- Reviewed record: `data/ingredients/mapped/Vulpinic_Acid.yaml`.
- Identifier and grounding: `identifier: CHEBI:144250` with matching
  `ontology_mapping.ontology_id`, label `Vulpinic acid`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- CAS RN: `521-52-8`.
- Chemical fields: formula `C19H14O5` with populated InChI and SMILES strings.
- Synonyms: none.
- Occurrences: zero.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Voso4_X_N_H2o` through `Washed_agar`: exited 0 and wrote zero ERROR rows.
- `uv run --frozen linkml-term-validator validate-data` on the three
  CHEBI-primary records in this batch exited 0.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh OLS4 lookup for `CHEBI:144250` returns active label `Vulpinic acid`,
  formula `C19H14O5`, and structure strings matching the local record.
- The final SSSOM row correctly has
  `MIM:Vulpinic_Acid skos:exactMatch CHEBI:144250`.

## Issues

None.

## Completeness

- The exact CHEBI mapping, CAS RN, structure fields, aggregate copy, and final
  SSSOM row agree.

## Recommended Edits

None.
