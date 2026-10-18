# `data/ingredients/mapped/Spir_Solution.yaml`

## Verdict

Pass. The record intentionally models a named SPIR solution stock as a local
`kgmicrobe.ingredient` identity, preserves its two raw CultureMech labels, and
publishes only those same labels in final SSSOM `other`.

## Identity

- Reviewed record: `data/ingredients/mapped/Spir_Solution.yaml`.
- Identifier and grounding: `identifier: kgmicrobe.ingredient:spir_solution`
  with `ontology_mapping.ontology_id: kgmicrobe.ingredient:spir_solution`,
  label `Spir solution`, source `kgmicrobe.ingredient`,
  `mapping_quality: FALLBACK_REGISTRY`, `mapping_status: MAPPED`,
  `ingredient_type: STOCK_SOLUTION`, and `solution_type: OTHER`.
- Synonyms: `Spir solution 1` and `Spir solution 2` as CultureMech raw text.
- Occurrences: 2 source occurrences across 2 CultureMech media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Sphondin` through `Spiramycin_II`: exited 0 and wrote zero ERROR rows.
- Engine A term validation was skipped for this local `kgmicrobe.ingredient`
  target; the non-OBO CURIE is covered by the product validator rather than
  OAK.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh exact OLS4 searches for `Spir solution`, `Spir solution 1`, and
  `Spir solution 2` returned zero documents, matching the local fallback
  decision in `MIM curation (#114)`.
- A gitignore-independent `find data -name '*Spir*'` found only the three live
  mapped per-record files for `Spiramycin`, `Spiramycin_II`, and
  `Spir_Solution`; there is no live unmapped per-record duplicate.
- The residual `data/curated/unmapped_complex_media.yaml` entry is in a legacy
  generated category YAML described by `data/curated/UNMAPPED_FINAL_REPORT.md`,
  not a synchronized `data/ingredients/unmapped` record.
- The final SSSOM row is a local identity row with
  `Spir solution 1|Spir solution 2` in `other`, exactly matching the two
  CultureMech raw labels retained in YAML.

## Completeness

- The local identifier, stock-solution type, raw labels, occurrence count,
  aggregate copy, and final SSSOM row agree.
- The component formula for this named SPIR stock remains unresolved, but that
  is explicitly recorded in the May 2026 curation note.

## Recommended Edits

- None.
