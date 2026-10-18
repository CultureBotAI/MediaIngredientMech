# `data/ingredients/mapped/Glucose_Formate.yaml`

## Verdict

Pass with minor stale-note issues. The local fallback identity, glucose plus
formate component list, typed component assertion, MicrobeDecoder occurrence,
and final SSSOM row pass, but old explanatory text still describes the original
unmapped import and the retired `DEFINED_MEDIUM` ingredient-type name.

## Identity

- Reviewed record: `data/ingredients/mapped/Glucose_Formate.yaml`.
- Identifier and grounding: `identifier: kgmicrobe.ingredient:glucose_formate`
  with matching `ontology_mapping.ontology_id`, source
  `kgmicrobe.ingredient`, `mapping_quality: FALLBACK_REGISTRY`,
  `mapping_status: MAPPED`, and `ingredient_type: NAMED_MEDIUM`.
- Components: `glucose` / `CHEBI:17234` and `formate` / `CHEBI:15740`, both
  scoped to `MIM_CATALOG`.

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
  occurrence, final `NAMED_MEDIUM` type, and stale notes as the per-record YAML.
- `mappings/microbedecoder_residual_research_decomposition.tsv` is the
  maintained split source for `CHEBI:17234:glucose` and
  `CHEBI:15740:formate`, with high confidence and the note that the source
  label names two substrates.
- A phrase-constrained OLS4 exact search over `label,synonym` returned zero
  terms for the exact full composite label `Glucose + Formate`.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:Glucose_Formate` to `kgmicrobe.ingredient:glucose_formate` with
  `skos:exactMatch` and leaves `other` empty.
- Minor: top-level `notes` still carry the original MicrobeDecoder import text
  and say curator review is needed even though the record has been decomposed,
  promoted, typed, moved into the mapped collection, and exported.
- Minor: `ontology_mapping.evidence[0].notes` still says
  `ingredient_type=DEFINED_MEDIUM`; that was a transient pre-#222
  classification name and should not remain in current identity evidence.
- A hidden/ignored-inclusive search over `data`, `src`, `tests`, `mappings`,
  `reports`, and `.claude` found the active YAML, aggregate copies, final SSSOM
  row, MicrobeDecoder residual rows, generated indexes, old batch validation
  reports, and ignored aggregate backups.

## Completeness

- The local identity, raw MicrobeDecoder source label, two components,
  component assertion, source occurrence, and final SSSOM row are populated.
- Empty concentration, nutritional-role, physicochemical-role, and chemical
  structure slots are acceptable for this source-label combination.

## Recommended Edits

- Minor: refresh `notes` in
  `data/ingredients/mapped/Glucose_Formate.yaml` so it describes the current
  reviewed local fallback decomposition.
- Minor: replace the legacy `ingredient_type=DEFINED_MEDIUM` prose in
  `ontology_mapping.evidence[0].notes` with wording that either names the
  current type or simply describes the two defined components.
