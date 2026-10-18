# `data/ingredients/mapped/GYPS.yaml`

## Verdict

Pass with a minor stale-note issue. `GYPS` is intentionally a local registry
ingredient for a recipe-variable glucose, yeast-extract, peptone, and starch
blend; its curated component partonomy and similar-composition CultureMech link
validate, but the top-level import note still says curator review is needed.

## Identity

- Reviewed record: `data/ingredients/mapped/GYPS.yaml`.
- Identifier and grounding: `identifier: kgmicrobe.ingredient:gyps` with
  matching `ontology_mapping.ontology_id`, source `kgmicrobe.ingredient`,
  `mapping_quality: FALLBACK_REGISTRY`, `mapping_status: MAPPED`, and
  `ingredient_type: UNDEFINED_MIXTURE`.
- Components: `glucose` / `CHEBI:17234`, `yeast extract` /
  `FOODON:03315426`, `peptone` / `MICRO:0000178`, and `starch` /
  `CHEBI:28017`, all scoped to `MIM_CATALOG`.

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
  local identifier, MicrobeDecoder source occurrence, four components,
  component assertion, CultureMech reference, and ingredient type as the
  per-record YAML.
- `mappings/microbedecoder_residual_research_decomposition.tsv` is the
  maintained split source for the four current MIM-catalog components.
- The `culturemech_reference` is deliberately
  `CultureMech:002799` / `SIMILAR_COMPOSITION`: the record states that three of
  four curated constituents agree and the CultureMech medium additionally lists
  MES and sea salt but no starch, and `tests/test_cross_reference_culturemech.py`
  asserts this link must not be upgraded to `EXACT_FORMULATION`.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps `MIM:GYPS` to
  `kgmicrobe.ingredient:gyps` with `skos:exactMatch` and leaves `other` empty.
- Minor: the top-level `notes` field still contains the original import text
  saying no CAS or CHEBI/NCIT match was found and curator review was needed,
  even though the record is now mapped and decomposed.
- A hidden/ignored-inclusive search over `data`, `src`, `tests`, `mappings`,
  `scripts`, and `reports` found the active YAML, aggregate copy, final SSSOM
  row, residual decomposition row, CultureMech cross-reference tests, generated
  indexes, and ignored aggregate backups.

## Completeness

- The local mixture identity, source occurrence, curated MIM-catalog component
  list, component assertion, similar-composition CultureMech link, and final
  SSSOM row are populated.
- Concentrations are correctly absent because the curated decomposition row did
  not record any.

## Recommended Edits

- Minor: refresh the top-level `notes` in
  `data/ingredients/mapped/GYPS.yaml` and
  `data/curated/mapped_ingredients.yaml` so it summarizes the mapped
  local-registry identity rather than the old unresolved-import state.
