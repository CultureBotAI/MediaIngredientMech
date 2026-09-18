# `data/ingredients/mapped/Fetal_Bovine_Serum.yaml`

## Verdict

Needs curation, with major unsupported-role and ingredient-type issues. The
NCIT grounding correctly expands `FBS` to fetal bovine serum in the media
context and the final SSSOM synonyms are safe, but the record still asserts an
LLM-only `PROTEIN_SOURCE` role and an old `SINGLE_INGREDIENT` type for a serum
mixture.

## Identity

- Reviewed record: `data/ingredients/mapped/Fetal_Bovine_Serum.yaml`.
- Identifier and grounding: `identifier: NCIT:C113696` with matching
  `ontology_mapping.ontology_id`, label `Fetal Bovine Serum`, source `NCIT`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- EBI OLS for NCIT resolves `NCIT:C113696` as `Fetal Bovine Serum`, marks it
  non-obsolete, defines it as a cow-fetus serum fraction used as a growth-medium
  component, and lists `FBS` as an exact synonym.
- The prior `FBS` ambiguity was already resolved in favor of fetal bovine serum:
  `mappings/unmapped_ingredients_ols_exact_audit.tsv` listed `FBS` as an exact
  synonym hit for `NCIT:C113696`, and the active record absorbed the
  `FBS.yaml` duplicate on 2026-05-11.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Feso4_X_H2o.yaml data/ingredients/mapped/Fetal_Bovine_Serum.yaml data/ingredients/mapped/Fibrin.yaml data/ingredients/mapped/Fidaxomicin.yaml data/ingredients/mapped/Fig.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Fetal_Bovine_Serum.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 skipped because the
  sibling kg-microbe ontology transforms are not checked out.

## Evidence

- The matching `data/curated/mapped_ingredients.yaml` entry carries the same
  NCIT identifier, aliases, occurrence counts, stale `SINGLE_INGREDIENT` type,
  and provisional role evidence as the per-record YAML.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:Fetal_Bovine_Serum` to `NCIT:C113696` with `skos:exactMatch`.
- The final SSSOM `other` tokens are `FBS` and the CultureMech
  `Fetal Bovine Serum (ATCC 30-2020)` supplier surface that was backfilled as a
  raw exact alias for this same serum identity.
- `mappings/ingredient_mappings_external_prefix_ols_validation.tsv` resolves
  `NCIT:C113696` exactly through prefix-specific EBI OLS; the older
  `UNKNOWN_TERM` row in `mappings/ingredient_mappings_oak_ols_review.tsv` was
  a validator-prefix coverage gap, not a bad identifier.
- Major: `nutritional_roles.PROTEIN_SOURCE` was added by
  `claude_in_session_curation` and is supported only by
  `COMPUTATIONAL_PREDICTION` evidence whose curator note calls it a provisional
  in-session LLM assignment.
- Major: `ingredient_type: SINGLE_INGREDIENT` came from the retired
  `auto_classify_ingredient_type` NCIT-primary heuristic. The maintained
  `scripts/classify_ingredient_type.py` intentionally treats NCIT-primary
  records as ambiguous unless their names independently match a complex-material
  pattern; the record should be curator-reviewed as a serum mixture rather than
  kept as a single pure ingredient.
- A hidden/ignored-inclusive search over `data/ingredients`, `data/curated`,
  `mappings`, `scripts`, `src`, `tests`, and `reports`, excluding prior
  per-record reports, aggregate backups, and the final SSSOM TSV, found the
  active YAML, aggregate copy, NCIT OLS validation rows, the FBS
  duplicate-resolution row, the CultureMech ATCC alias and separate
  heat-inactivated FBS residuals, occurrence membership, and ignored historical
  batch reports.

## Completeness

- The media-context expansion of `FBS`, the exact NCIT identity, occurrence
  counts, and final SSSOM aliases are populated.
- The role evidence and ingredient-type classification remain the consequential
  gaps.
- The unresolved heat-inactivated and supplier-specific FBS labels in
  `mappings/culturemech_residual_triage.tsv` are correctly absent from this
  record's synonyms.

## Recommended Edits

- Major: replace or remove `nutritional_roles.PROTEIN_SOURCE` in
  `data/ingredients/mapped/Fetal_Bovine_Serum.yaml`; keep the role only if a
  source explicitly supports fetal bovine serum as a protein source.
- Major: change `ingredient_type` on the same record from `SINGLE_INGREDIENT`
  to the curator-confirmed mixture type, likely `UNDEFINED_MIXTURE`, then sync
  `data/curated/mapped_ingredients.yaml` and rerun strict validation plus the
  final SSSOM invariant gates.
