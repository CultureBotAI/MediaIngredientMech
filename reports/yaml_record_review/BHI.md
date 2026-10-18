# `data/ingredients/mapped/BHI.yaml`

## Verdict

Needs curation; severity minor. The record is intentionally retained as a local
`kgmicrobe.ingredient:bhi` registry identity for the BHI named medium, and the
false whole-medium component edge has already been removed, but the top-level
`notes` still repeat stale import-time text saying curator review was needed.

## Identity

- Reviewed record: `data/ingredients/mapped/BHI.yaml`.
- Identifier and grounding: `identifier: kgmicrobe.ingredient:bhi` with
  `ontology_mapping.ontology_id: kgmicrobe.ingredient:bhi`,
  `ontology_label: BHI`, `ontology_source: kgmicrobe.ingredient`,
  `mapping_quality: FALLBACK_REGISTRY`, `ingredient_type: UNDEFINED_MIXTURE`,
  and `mapping_status: MAPPED`.
- The record denotes the named BHI medium as a local mixture/formulation
  identity, not a single CHEBI chemical and not a `has_part` edge to
  `MICRO:0000193` brain heart infusion.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Azureomycin.yaml data/ingredients/mapped/B-Glucan_From_Oat.yaml data/ingredients/mapped/B-Mannan_Borohydrate_Reduced_Carob_Seed.yaml data/ingredients/mapped/BHI.yaml data/ingredients/mapped/Bacillomycin.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- Engine A term validation was intentionally skipped for this record because
  `kgmicrobe.ingredient` is a non-OBO prefix.
- Hidden/ignored-inclusive local searches verified the maintained
  MicrobeDecoder residual decomposition, SSSOM registry row, CultureMech
  reference, and aggregate copy.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed;
  2951 records, 83 decompositions, 505 components, 0 violations.

## Evidence

- Hidden/ignored-inclusive searches over `data/curated`, `mappings`, and
  `data/custom`, excluding `data/curated/backups`, found the authoritative
  SSSOM row at `mappings/ingredient_mappings.sssom.tsv` row 519 and the
  aggregate copy in `data/curated/mapped_ingredients.yaml`.
- `data/custom/microbedecoder/unmapped_labels.tsv` and
  `data/custom/microbedecoder/ingredient_candidates.tsv` record two `BHI`
  occurrences in `bergey:substrates`, matching the record's source occurrence.
- `mappings/microbedecoder_residual_blends.tsv` and
  `mappings/microbedecoder_residual_research_decomposition.tsv` identify `BHI`
  as a named medium rather than a single-compound grounding target.
- The #369 curation event and current ontology evidence both say the prior BHI
  to `MICRO:0000193` component was an identity or alias claim rather than a
  partonomy edge.
- The #447 curation event migrated the prior free-text CultureMech medium name
  into `culturemech_reference.medium_id: CultureMech:015492`.

## Completeness

- The local registry identity, ingredient type, raw synonym, MicrobeDecoder
  source occurrence, exact CultureMech formulation reference, SSSOM row, and
  aggregate copy are populated.
- The intentionally absent `components` list is consistent with the #369
  removal of the false whole-medium component.
- The only active stale field is the top-level note that still describes the
  pre-promotion unmapped state.

## Recommended Edits

- Remove or rewrite the top-level `notes` in `data/ingredients/mapped/BHI.yaml`,
  synchronize `data/curated/mapped_ingredients.yaml`, and rerun focused strict
  validation, SSSOM invariants, component partonomy, and flat-export coverage.
