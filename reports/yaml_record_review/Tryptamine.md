# `data/ingredients/mapped/Tryptamine.yaml`

## Verdict

Pass. The exact CHEBI identity, CAS RN, exact synonym, structure fields,
aggregate row, and final SSSOM row pass.

## Identity

- Reviewed record: `data/ingredients/mapped/Tryptamine.yaml`.
- Identifier and grounding: `identifier: CHEBI:16765` with matching
  `ontology_mapping.ontology_id`, label `tryptamine`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- CAS RN: `61-54-1`.
- Synonyms: one reviewed exact synonym,
  `2-(1H-INDOL-3-YL)ETHANAMINE`.
- Occurrences: 0 recipe occurrences in 0 media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Triton_X-100` through `Tryptamine`: exited 0 and wrote zero ERROR rows.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh OLS4 term lookup for `CHEBI:16765` returns `tryptamine`, CAS xref
  `cas:61-54-1`, formula `C10H12N2`, the same InChI and SMILES as the YAML,
  and the exported exact synonym.
- The final SSSOM row has `MIM:Tryptamine skos:exactMatch CHEBI:16765` and
  exports only the exact synonym plus `CAS:61-54-1` in `other`.

## Issues

None.

## Completeness

- The CHEBI identity, CAS RN, structure fields, aggregate copy, and final SSSOM
  row agree.

## Recommended Edits

None.
