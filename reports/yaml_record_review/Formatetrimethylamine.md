# `data/ingredients/mapped/Formatetrimethylamine.yaml`

## Verdict

Needs curation; minor. The local fallback identity, explicit formate plus
trimethylamine decomposition, MicrobeDecoder occurrence, and final SSSOM row
pass, but stale notes still describe the older unresolved import and
pre-partonomy label-split state.

## Identity

- Reviewed record: `data/ingredients/mapped/Formatetrimethylamine.yaml`.
- Identifier and grounding:
  `identifier: kgmicrobe.ingredient:formate_trimethylamine` with matching
  `ontology_mapping.ontology_id`, source `kgmicrobe.ingredient`,
  `mapping_quality: FALLBACK_REGISTRY`, and `mapping_status: MAPPED`.
- The local identifier denotes the whole `Formate+trimethylamine` source-label
  combination, not either component alone.
- The maintained `UNMAPPED_0747` row in
  `mappings/microbedecoder_residual_research_decomposition.tsv` splits the
  label into `CHEBI:15740:formate` and `CHEBI:18139:trimethylamine`; the active
  YAML carries the same two components under
  `component_assertion.method: LABEL_ENUMERATION`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Formatetrimethylamine.yaml data/ingredients/mapped/Formic_Acid.yaml data/ingredients/mapped/Fortimicin_B.yaml data/ingredients/mapped/Fosfomycin.yaml data/ingredients/mapped/Fosmidomycin_Sodium_Salt_Hydrate.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- LinkML term validation passed for the three CHEBI-primary records in this
  batch and was intentionally skipped for this local `kgmicrobe.ingredient:`
  record because the Engine A/OBO prefix scope does not cover private
  KG-Microbe CURIEs.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed with
  2,951 records, 83 decompositions, 505 components, and 0 violations.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 skipped because the
  sibling kg-microbe ontology transforms are not checked out.

## Evidence

- The matching `data/curated/mapped_ingredients.yaml` entry carries the same
  local identifier, preferred label, component list, typed
  `component_assertion`, source occurrence, final `NAMED_MEDIUM` type, and
  stale notes as the per-record YAML.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:Formatetrimethylamine` to
  `kgmicrobe.ingredient:formate_trimethylamine` with `skos:exactMatch`, object
  source `kgm:ingredient`, and an empty `other` column.
- The source-label evidence and curated decomposition dataset both support
  exactly two top-level parts. No concentration was asserted in either source.
- Minor: top-level `notes` still carry the original MicrobeDecoder import text
  and say curator review is needed even though the record has been decomposed,
  promoted, typed, moved into the mapped collection, and exported.
- Minor: `ontology_mapping.evidence[0].notes` still repeats the older
  label-split text and says `ingredient_type=DEFINED_MEDIUM`; the current
  record uses `ingredient_type: NAMED_MEDIUM`.
- A hidden/ignored-inclusive search over `data`, `src`, `tests`, `mappings`,
  `scripts`, and `reports`, excluding prior per-record review reports and
  historical aggregate backups, found the active YAML, aggregate copy, final
  SSSOM row, MicrobeDecoder residual rows, component-partonomy migration list,
  and related formate-plus-substrate records.

## Completeness

- The local identity, raw MicrobeDecoder source label, two components,
  `component_assertion`, source occurrence, and final SSSOM row are populated.
- Empty concentration, nutritional-role, physicochemical-role, and chemical
  structure slots are acceptable for this source-label combination.

## Recommended Edits

- Minor: refresh `notes` in
  `data/ingredients/mapped/Formatetrimethylamine.yaml` so it describes the
  current reviewed local fallback decomposition.
- Minor: replace `ontology_mapping.evidence[0].notes` with the post-curated
  state: both source-label parts are resolved, both carry component IDs, and
  the current type is `NAMED_MEDIUM`.
