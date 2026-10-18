# `data/ingredients/mapped/Das_Vitamin_Cocktail.yaml`

## Verdict

Needs curation, major. The local
`kgmicrobe.ingredient:das_vitamin_cocktail` identity and registry SSSOM row are
appropriate for a named vitamin stock with no OBO exact term, but the record
still has no component transcription and the old complex-media UNMAPPED row for
the same CultureMech label remains in active `data/curated` outputs.

## Identity

- Reviewed record: `data/ingredients/mapped/Das_Vitamin_Cocktail.yaml`.
- Identifier and grounding:
  `identifier: kgmicrobe.ingredient:das_vitamin_cocktail` with the same
  `ontology_mapping.ontology_id`, `ontology_label: DAS Vitamin Cocktail`,
  `ontology_source: kgmicrobe.ingredient`,
  `mapping_quality: FALLBACK_REGISTRY`, `ingredient_type: STOCK_SOLUTION`,
  `solution_type: VITAMIN_MIX`, and `mapping_status: MAPPED`.
- Live OLS exact search across CHEBI, NCIT, MeSH, FOODON, and ENVO for
  `DAS Vitamin Cocktail` returned 0 results on 2026-09-16, preserving the
  local registry identity premise.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Das_Macro_Solution.yaml data/ingredients/mapped/Das_Vitamin_Cocktail.yaml data/ingredients/mapped/Daunorubicin.yaml data/ingredients/mapped/Day_AminoAcid20.yaml data/ingredients/mapped/Decanoate.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- Direct Engine A term validation over the same 5 files exited 1 on the local
  `kgmicrobe.ingredient` records. The documented `just validate-terms` wrapper
  intentionally skips non-OBO prefixes for Engine A; local registry rows are
  covered by strict schema validation, the SSSOM invariant check, and
  product-level id/label validation.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed;
  2951 records, 83 decompositions, 505 components, 0 violations.
- `uv run --frozen python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`:
  passed; all id-label pairs corresponded, with only full-corpus plausibility
  warnings.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.
- `uv run --frozen python scripts/check_flat_export_coverage.py`: passed; all
  generated `docs/data` artifacts matched their producers and every curated
  label was resolvable.

## Evidence

- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:Das_Vitamin_Cocktail` to
  `kgmicrobe.ingredient:das_vitamin_cocktail` with `skos:exactMatch`, object
  source `kgm:ingredient`, empty `other`, and the expected unknown-term
  validation stamp for a local registry target.
- The hidden/ignored-inclusive exact search over active `data/ingredients`,
  `data/curated`, `mappings`, `docs/data`, `src`, `scripts`, and `tests`
  found the mapped per-record YAML, the mapped aggregate copy, generated
  mapped indexes, the final SSSOM row, and no second
  `data/ingredients/unmapped/Das_Vitamin_Cocktail.yaml` file.
- The same hidden/ignored-inclusive search found stale `UNMAPPED_0045`
  `DAS Vitamin Cocktail` rows in
  `data/curated/unmapped_complex_media.yaml` and
  `data/curated/UNMAPPED_COMPLEX_MEDIA.md`.
- The May and August curation history consistently says this is a vitamin
  cocktail stock/pre-mix, but the component-level recipe curation was still
  pending.

## Completeness

- Consequential gap: this vitamin mix has no `components`,
  `component_assertion`, or claim-level evidence for its vitamin constituents.
- Consequential gap: the stale unmapped complex-media collection still
  publishes the same source label as an unmapped record.
- A `VITAMIN_SOURCE` role should be added only with claim-level evidence after
  the vitamin cocktail composition is transcribed from its maintained source.

## Recommended Edits

- Major: transcribe the DAS vitamin stock recipe into `components`, add a
  source-backed `component_assertion`, add a source-backed `VITAMIN_SOURCE`
  role if the transcribed constituents support it, and rerun
  `uv run --frozen python scripts/validate_component_partonomy.py`.
- Major: remove stale `UNMAPPED_0045` `DAS Vitamin Cocktail` rows from
  `data/curated/unmapped_complex_media.yaml` and
  `data/curated/UNMAPPED_COMPLEX_MEDIA.md`, then rerun strict validation,
  round-trip/category checks, and `uv run --frozen python scripts/check_flat_export_coverage.py`.
