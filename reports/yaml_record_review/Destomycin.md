# `data/ingredients/mapped/Destomycin.yaml`

## Verdict

Needs curation. The local kg-microbe placeholder is still the right primary
identity for the unqualified label `Destomycin`, but its only
`SELECTIVE_AGENT` support is a provisional name-pattern prediction.

## Identity

- Reviewed record: `data/ingredients/mapped/Destomycin.yaml`.
- Identifier and grounding: `identifier: kgmicrobe.compound:destomycin` with
  `ontology_mapping.ontology_id: kgmicrobe.compound:destomycin`, source
  `kgmicrobe.compound`, `mapping_quality: PLACEHOLDER`,
  `mapping_status: MAPPED`, and `ingredient_type: SINGLE_INGREDIENT`.
- The live EBI OLS CHEBI/NCIT query for `Destomycin` still returned the same
  adjacent ChEBI candidates, `CHEBI:224010` Destomycin C and `CHEBI:4454`
  Destomysin, but no exact unqualified `Destomycin` class. That agrees with
  the 2026-05-10 review decision to keep a local placeholder.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Destomycin.yaml data/ingredients/mapped/Desulfovibrio_Trace_Elements.yaml data/ingredients/mapped/Deuterated_Glucose.yaml data/ingredients/mapped/Dextran.yaml data/ingredients/mapped/Dextrin.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data ...` over the mixed
  five-record batch aborted at `kgmicrobe.compound:destomycin` because local
  kg-microbe registry IDs are outside the OAK SQL label database.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Dextran.yaml data/ingredients/mapped/Dextrin.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed the OBO/CHEBI subset; `Destomycin` was intentionally skipped as a
  local registry record.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.
- `uv run --frozen python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`:
  passed; all id-label pairs corresponded, with only full-corpus plausibility
  warnings.

## Evidence

- `mappings/ingredient_mappings_unknown_term_manual_candidate_review.tsv`,
  `mappings/ingredient_mappings_unknown_term_placeholder_ols_candidates.tsv`,
  and `mappings/ingredient_mappings_row_review_manifest.tsv` all document that
  the external candidates were reviewed without an exact-identity promotion.
- The hidden/ignored-inclusive exact search over `data/ingredients`,
  `data/curated`, `mappings`, `docs/data`, `src`, `scripts`, and `tests`
  found no stronger active CHEBI, NCIT, or MeSH exact mapping for the local
  `Destomycin` record.
- The same hidden/ignored-inclusive search found no
  `mappings/culturemech_recipe_membership.tsv` row for
  `kgmicrobe.compound:destomycin`, matching
  `occurrence_statistics.total_occurrences: 0` and `media_count: 0`.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:Destomycin` to `kgmicrobe.compound:destomycin` with
  `skos:exactMatch`, a kg-microbe compound source, and empty `other`.
- Major: `physicochemical_roles.SELECTIVE_AGENT` is supported only by a
  `COMPUTATIONAL_PREDICTION` from `infer_roles_from_name_lists`, with a
  curator note that explicitly calls the role provisional and recommends
  review.

## Completeness

- The unqualified local identity, explicit rejected OLS candidates, row-review
  disposition, occurrence statistics, and empty final SSSOM synonym payload are
  complete enough for this placeholder record.
- CAS RN, chemical structure, mixture components, supplied forms, and
  environmental contexts are correctly empty while no exact external identity
  has been curated.

## Recommended Edits

- Major: remove or source-back `physicochemical_roles.SELECTIVE_AGENT` in
  `data/ingredients/mapped/Destomycin.yaml`, then synchronize
  `data/curated/mapped_ingredients.yaml` and regenerate final SSSOM if the YAML
  change affects emitted rows.
