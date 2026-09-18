# `data/ingredients/mapped/G9_Trace_Metals_For_J_Medium.yaml`

## Verdict

Pass with a minor stale-artifact issue. The active record is a deliberate local
stock-solution registry mint for a named CultureMech preparation with no exact
ontology parent, and the final SSSOM row is clean, but older unmapped-category
artifacts still carry the pre-promotion placeholder.

## Identity

- Reviewed record:
  `data/ingredients/mapped/G9_Trace_Metals_For_J_Medium.yaml`.
- Identifier and grounding:
  `identifier: kgmicrobe.ingredient:g9_trace_metals_for_j_medium` with
  matching `ontology_mapping.ontology_id`, source `kgmicrobe.ingredient`,
  `mapping_quality: FALLBACK_REGISTRY`, `mapping_status: MAPPED`,
  `ingredient_type: STOCK_SOLUTION`, and `solution_type: TRACE_METAL_MIX`.
- The mapping evidence records that ChEBI, NCIT, MeSH, FOODON, and ENVO were
  searched by label and synonym, no exact term denoted this lab preparation,
  and the local stock-solution mint follows the convention for named
  multi-component preparations that do not narrow to one compound.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/G418_Disulfate_Salt_Solution.yaml data/ingredients/mapped/G9_Trace_Metals_For_J_Medium.yaml data/ingredients/mapped/GYPS.yaml data/ingredients/mapped/Galactarate.yaml data/ingredients/mapped/Galactitol.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- LinkML term validation passed for the two CHEBI-primary files in this batch
  and was intentionally skipped for this local kg-microbe record because Engine
  A/OBO term validation does not cover local registry CURIEs.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed;
  2951 records, 83 decompositions, 505 components, 0 violations.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 skipped because the
  sibling kg-microbe ontology transforms are not checked out.

## Evidence

- The matching `data/curated/mapped_ingredients.yaml` entry carries the same
  local identifier, mapping evidence, occurrence statistics, raw CultureMech
  synonym, stock-solution type, and trace-metal-mix type as the per-record YAML.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:G9_Trace_Metals_For_J_Medium` to
  `kgmicrobe.ingredient:g9_trace_metals_for_j_medium` with `skos:exactMatch`
  and leaves `other` empty.
- `mappings/mim_curie_aliases.tsv` preserves the earlier
  `MIM:G9_Trace_Metals_for_J_medium` subject spelling as an alias of the
  published `MIM:G9_Trace_Metals_For_J_Medium` spelling.
- Minor: a hidden/ignored-inclusive search found historical UNMAPPED copies in
  `data/ingredient_category_summaries/unmapped/complex_mixture.yaml`,
  `data/curated/unmapped_complex_media.yaml`, and
  `data/curated/UNMAPPED_COMPLEX_MEDIA.md`.
- The active record asserts no component list, nutritional role,
  physicochemical role, source occurrence, or environment claim that would need
  independent support.
- A hidden/ignored-inclusive search over `data`, `src`, `tests`, `mappings`,
  `scripts`, and `reports` found the active YAML, aggregate copy, final SSSOM
  row, MIM subject alias row, old unmapped-category artifacts, and ignored
  aggregate backups.

## Completeness

- The local stock-solution identity, fallback registry row, one CultureMech
  occurrence, raw source label, and trace-metal-mix classification are
  populated.
- No component composition is asserted yet; no current claim depends on one.

## Recommended Edits

- Minor: regenerate or retire the stale unmapped-category artifacts that still
  list `G9 Trace Metals for J medium` under its pre-promotion placeholder.
