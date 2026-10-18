# `data/ingredients/mapped/Gallate_Formate.yaml`

## Verdict

Pass with minor stale-note issues. The local fallback identity, curated gallate
plus formate component list, typed component assertion, MicrobeDecoder
occurrence, and final SSSOM row pass, but stale prose still describes the old
unresolved import and the pre-curated state where gallate lacked a component
ID.

## Identity

- Reviewed record: `data/ingredients/mapped/Gallate_Formate.yaml`.
- Identifier and grounding: `identifier: kgmicrobe.ingredient:gallate_formate`
  with matching `ontology_mapping.ontology_id`, source
  `kgmicrobe.ingredient`, `mapping_quality: FALLBACK_REGISTRY`,
  `mapping_status: MAPPED`, and `ingredient_type: NAMED_MEDIUM`.
- Components: `gallate` / `CHEBI:16918` scoped to `EXTERNAL_TERM`, and
  `formate` / `CHEBI:15740` scoped to `MIM_CATALOG`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Gallate_Formate.yaml data/ingredients/mapped/Gallic_Acid.yaml data/ingredients/mapped/Gallium_Iiichloride.yaml data/ingredients/mapped/Gambogic_Acid.yaml data/ingredients/mapped/Gamma-aminobutyric_Acid.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- LinkML term validation passed for the three CHEBI-primary records in this
  batch and was intentionally skipped for this local kg-microbe record because
  Engine A/OBO term validation does not cover private KG-Microbe CURIEs.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed;
  2951 records, 83 decompositions, 505 components, 0 violations.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 skipped because the
  sibling kg-microbe ontology transforms are not checked out.

## Evidence

- The matching `data/curated/mapped_ingredients.yaml` entry carries the same
  local identifier, component list, typed component assertion, source
  occurrence, final `NAMED_MEDIUM` type, and stale notes as the per-record YAML.
- `mappings/microbedecoder_residual_research_decomposition.tsv` is the
  maintained split source for `CHEBI:16918:gallate` and `CHEBI:15740:formate`.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:Gallate_Formate` to `kgmicrobe.ingredient:gallate_formate` with
  `skos:exactMatch` and leaves `other` empty.
- Minor: top-level `notes` still carry the original MicrobeDecoder import text
  and say curator review is needed even though the record has been decomposed,
  promoted, typed, moved into the mapped collection, and exported.
- Minor: `ontology_mapping.evidence[0].notes` still repeats the older label-split
  text and says gallate has no component ID; the current curated component list
  resolves both gallate and formate.
- A hidden/ignored-inclusive search over `data`, `src`, `tests`, `mappings`,
  `scripts`, and `reports` found the active YAML, aggregate copy, final SSSOM
  row, MicrobeDecoder residual row, component-partonomy migration list,
  generated indexes, and ignored aggregate backups.

## Completeness

- The local identity, raw MicrobeDecoder source label, two components,
  component assertion, source occurrence, and final SSSOM row are populated.
- Empty concentration, nutritional-role, physicochemical-role, and chemical
  structure slots are acceptable for this source-label combination.

## Recommended Edits

- Minor: refresh `notes` in
  `data/ingredients/mapped/Gallate_Formate.yaml` so it describes the current
  reviewed local fallback decomposition.
- Minor: replace `ontology_mapping.evidence[0].notes` with the post-curated
  state: both source-label parts are resolved, both carry component IDs, and
  the current type is `NAMED_MEDIUM`.
