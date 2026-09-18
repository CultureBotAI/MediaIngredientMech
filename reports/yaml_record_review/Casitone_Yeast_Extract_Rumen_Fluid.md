# `data/ingredients/mapped/Casitone_Yeast_Extract_Rumen_Fluid.yaml`

## Verdict

Pass. The local fallback-registry identity correctly preserves a
multi-component MicrobeDecoder label that has no single external ontology
term, and its complete has-part assertion resolves all three constituents to
MIM catalog records.

## Identity

- Reviewed record:
  `data/ingredients/mapped/Casitone_Yeast_Extract_Rumen_Fluid.yaml`.
- Identifier and grounding:
  `identifier: kgmicrobe.ingredient:casitone_yeast_extract_rumen_fluid`,
  `ontology_mapping.ontology_id: kgmicrobe.ingredient:casitone_yeast_extract_rumen_fluid`,
  `ontology_source: kgmicrobe.ingredient`,
  `mapping_quality: FALLBACK_REGISTRY`, `mapping_status: MAPPED`, and
  `ingredient_type: UNDEFINED_MIXTURE`.
- Direct exact OLS search for `Casitone + Yeast Extract + Rumen Fluid` returned
  0 hits, matching the curated decision to keep the blend local and decompose
  it instead of forcing it to one component.
- The three components resolve inside the MIM catalog:
  `MICRO:0000606` for `casitone`, `FOODON:03315426` for `yeast extract`, and
  `MICRO:0000520` for `clarified rumen fluid`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Casein_Peptone.yaml data/ingredients/mapped/Casein_hydrolysate.yaml data/ingredients/mapped/Casitone.yaml data/ingredients/mapped/Casitone_Yeast_Extract_Rumen_Fluid.yaml data/ingredients/mapped/Caso4.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Casein_Peptone.yaml data/ingredients/mapped/Caso4.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed both Engine-A-supported OBO records in this batch.
- MICRO records in this batch were checked by direct prefix-specific OLS lookup
  and by the existing prefix-specific OLS validation TSV. This local
  kgmicrobe fallback has no Engine A adapter, like other kgmicrobe local
  identifiers.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed;
  2951 records, 83 decompositions, 505 components, and 0 violations.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip.wqYt47`
  followed by
  `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip.wqYt47`:
  passed; both curated collection files had 0 data differences and only the
  expected scratch `generation_date` metadata differences.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K. Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- Hidden/ignored-inclusive search over `data/curated`, `mappings`,
  `docs/data`, and `reports`, excluding generated review reports and curated
  backups, found the active
  `MIM:Casitone_Yeast_Extract_Rumen_Fluid` SSSOM row, matching aggregate/docs
  rows, and the exact row in
  `mappings/microbedecoder_residual_research_decomposition.tsv` that
  decomposes this source label.
- Hidden/ignored-inclusive search of the decomposition and label-index
  surfaces found all three component identifiers as MIM-catalog entries.
- Direct OLS lookups for `MICRO:0000606`, `FOODON:03315426`, and
  `MICRO:0000520` return active `casitone`, `yeast extract`, and `clarified
  rumen fluid` terms respectively.
- The current `mappings/culturemech_recipe_membership.tsv` table has 0 rows
  for `kgmicrobe.ingredient:casitone_yeast_extract_rumen_fluid`, matching
  `occurrence_statistics` `0/0`; the separate MicrobeDecoder
  `source_occurrences` block records one literature-substrate occurrence.

## Completeness

- The fallback local identifier, source occurrence, complete component list,
  structured component assertion, SSSOM row, aggregate copy, and docs row are
  populated.
- Component concentrations are correctly absent because neither the source
  label nor the curated decomposition records concentrations.
- No role or chemical-property claims are present.

## Recommended Edits

- None for this record.
