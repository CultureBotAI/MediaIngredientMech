# `data/ingredients/mapped/Glucose_Cellobiose_Starch_Trypticase_Yeast_Extract.yaml`

## Verdict

Pass with a minor stale-note issue. The local fallback identity, five-part
component list, undefined-mixture classification, typed component assertion,
MicrobeDecoder occurrence, and final SSSOM row pass, but the top-level note
still describes the original unmapped import.

## Identity

- Reviewed record:
  `data/ingredients/mapped/Glucose_Cellobiose_Starch_Trypticase_Yeast_Extract.yaml`.
- Identifier and grounding:
  `identifier: kgmicrobe.ingredient:glucose_cellobiose_starch_trypticase_yeast_extract`
  with matching `ontology_mapping.ontology_id`, source
  `kgmicrobe.ingredient`, `mapping_quality: FALLBACK_REGISTRY`,
  `mapping_status: MAPPED`, and `ingredient_type: UNDEFINED_MIXTURE`.
- Components: `glucose` / `CHEBI:17234`, `cellobiose` / `CHEBI:17057`,
  `starch` / `CHEBI:28017`, `Trypticase peptone` / `MICRO:0000175`, and
  `yeast extract` / `FOODON:03315426`, all scoped to `MIM_CATALOG`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Glucose_Acetate.yaml data/ingredients/mapped/Glucose_Cellobiose_Starch_Trypticase_Yeast_Extract.yaml data/ingredients/mapped/Glucose_Formate.yaml data/ingredients/mapped/Glucose_Lactate.yaml data/ingredients/mapped/Glucose_Maltose_Cellobiose_Starch_Glycerol.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- LinkML Engine A was intentionally skipped for all five records in this batch
  because their own identity rows use the private `kgmicrobe.ingredient`
  prefix, which the OBO-only term validator cannot resolve.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed;
  2951 records, 83 decompositions, 505 components, 0 violations.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 skipped because the
  sibling kg-microbe ontology transforms are not checked out.

## Evidence

- The matching aggregate `data/curated/mapped_ingredients.yaml` entry carries
  the same local identifier, component list, typed component assertion, source
  occurrence, undefined-mixture type, and stale top-level note as the
  per-record YAML.
- `mappings/microbedecoder_residual_research_decomposition.tsv` is the
  maintained split source for the five retained components and describes the
  label as a high-confidence GSC/M2GSC-type rumen or cellulolytic carbohydrate
  blend.
- The `UNDEFINED_MIXTURE` type is justified because the decomposition includes
  Trypticase peptone and yeast extract, both undefined biological preparations.
- A phrase-constrained OLS4 exact search over `label,synonym` returned zero
  terms for the exact full composite label
  `Glucose + Cellobiose + Starch + Trypticase + Yeast Extract`.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:Glucose_Cellobiose_Starch_Trypticase_Yeast_Extract` to
  `kgmicrobe.ingredient:glucose_cellobiose_starch_trypticase_yeast_extract`
  with `skos:exactMatch` and leaves `other` empty.
- Minor: top-level `notes` still carry the original MicrobeDecoder import text
  and say curator review is needed even though the record has been decomposed,
  promoted, typed, moved into the mapped collection, and exported.
- A hidden/ignored-inclusive search over `data`, `src`, `tests`, `mappings`,
  `reports`, and `.claude` found the active YAML, aggregate copies, final SSSOM
  row, MicrobeDecoder residual rows, generated indexes, old batch validation
  reports, and ignored aggregate backups.

## Completeness

- The local identity, raw MicrobeDecoder source label, five components,
  component assertion, source occurrence, undefined-mixture classification, and
  final SSSOM row are populated.
- Empty concentration, nutritional-role, physicochemical-role, and chemical
  structure slots are acceptable for this source-label combination.

## Recommended Edits

- Minor: refresh `notes` in
  `data/ingredients/mapped/Glucose_Cellobiose_Starch_Trypticase_Yeast_Extract.yaml`
  so it describes the current reviewed local fallback decomposition.
