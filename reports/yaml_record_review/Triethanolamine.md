# `data/ingredients/mapped/Triethanolamine.yaml`

## Verdict

Pass. The exact CHEBI identity, CAS RN, kg-microbe synonyms, occurrence count,
aggregate row, and final SSSOM row pass.

## Identity

- Reviewed record: `data/ingredients/mapped/Triethanolamine.yaml`.
- Identifier and grounding: `identifier: CHEBI:28621` with matching
  `ontology_mapping.ontology_id`, label `triethanolamine`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- CAS RN: `102-71-6`.
- Synonyms: one raw CultureMech role/properties string plus nine
  kg-microbe-provided synonyms.
- Occurrences: 5 CultureMech recipe occurrences in 5 media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Triethanolamine` through `Trimethylamine-N-oxide`: exited 0 and wrote zero
  ERROR rows.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh exact OLS4 search for `triethanolamine` returns `CHEBI:28621` with
  label `triethanolamine`.
- The OLS result also contains the exported kg-microbe labels
  `2,2',2''-NITRILOTRIETHANOL`, `2,2',2''-nitrilotris(ethanol)`, `H3tea`,
  `N(CH2CH2OH)3`, `Trolamine`, `nitrilo-2,2',2''-triethanol`,
  `nitrilotriethanol`, `tris(2-hydroxyethyl)amine`, and
  `tris(beta-hydroxyethyl)amine`.
- The final SSSOM row has
  `MIM:Triethanolamine skos:exactMatch CHEBI:28621`, exports only the
  inspected kg-microbe synonym labels plus `CAS:102-71-6`, and filters the raw
  `Role:`/`Properties:` string out of `other`.

## Issues

None.

## Completeness

- The CHEBI identity, CAS RN, structure fields, occurrence count, aggregate
  copy, synonyms, and final SSSOM row agree.

## Recommended Edits

None.
