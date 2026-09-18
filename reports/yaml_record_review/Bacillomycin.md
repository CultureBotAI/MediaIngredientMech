# `data/ingredients/mapped/Bacillomycin.yaml`

## Verdict

Needs curation; severity major. The bare Bacillomycin label still has no exact
bare `CHEBI`, `MESH`, or `NCIT` term and is reasonably held as a local
`kgmicrobe.compound` fallback, but its active ontology evidence says only
`test canary`, and its top-level `notes` still repeat stale pre-promotion text.

## Identity

- Reviewed record: `data/ingredients/mapped/Bacillomycin.yaml`.
- Identifier and grounding: `identifier: kgmicrobe.compound:bacillomycin` with
  `ontology_mapping.ontology_id: kgmicrobe.compound:bacillomycin`,
  `ontology_label: Bacillomycin`, `ontology_source: kgmicrobe.compound`,
  `mapping_quality: FALLBACK_REGISTRY`, and `mapping_status: MAPPED`.
- OLS4 exact search across `CHEBI`, `MESH`, and `NCIT` returned more specific
  bacillomycin terms such as `Bacillomycin D`, `bacillomycin L`, and
  `bacillomycin F`, but no exact bare `Bacillomycin` term.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Azureomycin.yaml data/ingredients/mapped/B-Glucan_From_Oat.yaml data/ingredients/mapped/B-Mannan_Borohydrate_Reduced_Carob_Seed.yaml data/ingredients/mapped/BHI.yaml data/ingredients/mapped/Bacillomycin.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- Engine A term validation was intentionally skipped for this record because
  `kgmicrobe.compound` is a non-OBO prefix.
- OLS4 exact lookup for `Bacillomycin` in `CHEBI`, `MESH`, and `NCIT` found
  several narrower terms but no exact bare term.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed;
  2951 records, 83 decompositions, 505 components, 0 violations.

## Evidence

- Hidden/ignored-inclusive searches over `data/curated`, `mappings`, and
  `data/custom`, excluding `data/curated/backups`, found the authoritative
  SSSOM row at `mappings/ingredient_mappings.sssom.tsv` row 520 and the
  aggregate copy in `data/curated/mapped_ingredients.yaml`.
- The 2026-08-06 curation event records the promotion from `UNMAPPED_0799` to
  `kgmicrobe.compound:bacillomycin` and the `FALLBACK_REGISTRY` decision.
- `data/custom/microbedecoder/unmapped_labels.tsv` and
  `data/custom/microbedecoder/ingredient_candidates.tsv` record one
  `bacillomycin` occurrence in `BacDive_Antibiotic_sensitivity`, matching
  `occurrence_statistics.source_occurrences`.
- The current `ontology_mapping.evidence.notes` value, `test canary`, is a
  placeholder and does not explain or support the fallback registry decision.

## Completeness

- The local fallback identifier, raw synonym, MicrobeDecoder source occurrence,
  SSSOM row, and aggregate copy are populated.
- The top-level `notes` field is stale and still says no match was found and
  curator review was needed even though the record was promoted on 2026-08-06.
- The active mapping evidence needs a real review note describing the no-exact
  external-term decision.

## Recommended Edits

- Replace `ontology_mapping.evidence.notes: test canary` in
  `data/ingredients/mapped/Bacillomycin.yaml` with the maintained #213
  fallback-registry rationale, remove or rewrite the stale top-level `notes`,
  synchronize `data/curated/mapped_ingredients.yaml`, and rerun focused strict
  validation, SSSOM invariants, product id/label correspondence, and flat-export
  coverage.
