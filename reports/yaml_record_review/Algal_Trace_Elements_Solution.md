# `data/ingredients/mapped/Algal_Trace_Elements_Solution.yaml`

## Verdict

Needs curation. `MICRO:0000455` resolves as generic `trace elements solution`,
but `Algal Trace Elements Solution` is a specific stock solution that shares the
same MICRO ID with `WC Trace Elements Solution`; the record needs its own exact
identity and should keep `MICRO:0000455` only as a broader parent if useful.

## Identity

- Reviewed record:
  `data/ingredients/mapped/Algal_Trace_Elements_Solution.yaml`.
- Identifier and grounding: `identifier: MICRO:0000455` with
  `ontology_mapping.ontology_id: MICRO:0000455`, source `MICRO`,
  `mapping_quality: LEXICAL_MATCH`, and `mapping_status: MAPPED`.
- `mappings/ingredient_mappings_external_prefix_ols_validation.tsv` confirms
  `MICRO:0000455` resolves through prefix-specific OLS as `trace elements solution`.
- `ingredient_type: STOCK_SOLUTION` is present.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Alazopeptin.yaml data/ingredients/mapped/Alboverticillin.yaml data/ingredients/mapped/Alcl3.yaml data/ingredients/mapped/Alcl3_X_6_H2o.yaml data/ingredients/mapped/Algal_Trace_Elements_Solution.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `scripts/_engine_a_obo_safe.sh data/ingredients/mapped/Algal_Trace_Elements_Solution.yaml "CHEBI FOODON NCIT MESH UBERON ENVO BTO PATO"`:
  exited 1, so `just validate-terms` would skip Engine A for this unsupported
  `MICRO` prefix.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed; 2951
  records, 83 decompositions, 505 components, 0 violations.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- `mappings/duplicate_identifier_baseline.tsv` already classifies the
  `MICRO:0000455` pair `Algal Trace Elements Solution | WC Trace Elements Solution`
  as `NEEDS_OWN_ID`; both records currently point at the same generic MICRO
  class.
- `mappings/ingredient_mappings.sssom.tsv` row 365 publishes
  `MIM:Algal_Trace_Elements_Solution` as `skos:exactMatch` to
  `MICRO:0000455`, which loses the algal-specific stock-solution identity.
- A hidden/ignored-inclusive search of `mappings/culturemech_recipe_membership.tsv`
  found no `MICRO:0000455` row, so the single stored occurrence is not
  represented in the refreshed occurrence membership table.
- The `TRACE_ELEMENT` role is still only a provisional in-session LLM role
  assignment and says review is recommended.
- Older unmapped-category artifacts under `data/curated/unmapped_complex_media.yaml`
  and `data/ingredient_category_summaries/unmapped/complex_mixture.yaml` still
  carry historical `Algal Trace Elements Solution` UNMAPPED entries.
- The hidden/ignored-inclusive search over `data`, `mappings`, `reports`,
  `src`, `tests`, `scripts`, `.claude`, `justfile`, and `CLAUDE.md` found the
  active YAML, aggregate copy, SSSOM row, external-prefix OLS validation row,
  duplicate-identifier rows, stale unmapped-category artifacts, generated
  indexes, and ignored aggregate backups.

## Completeness

- Mapping evidence, occurrence statistics, curation history, provisional role,
  and `ingredient_type` are populated.
- The stock solution lacks a distinct exact identifier, component composition,
  refreshed occurrence edge, and claim-level evidence for the trace-element
  role.
- The aggregate copy in `data/curated/mapped_ingredients.yaml` matches the
  per-record YAML.

## Recommended Edits

- Mint or assign a distinct exact identity for
  `data/ingredients/mapped/Algal_Trace_Elements_Solution.yaml`, demoting
  `MICRO:0000455` to a parent mapping if generic `trace elements solution`
  remains useful.
- Add component rows for the stock solution when the source recipe defines them,
  and remove the stale duplicate with `WC Trace Elements Solution`.
- Recompute CultureMech membership/occurrence outputs and either curate
  claim-level evidence for `nutritional_roles.TRACE_ELEMENT` or remove the
  provisional role.
- Regenerate synchronized products, then rerun
  `uv run --frozen python scripts/validate_strict.py`,
  `uv run --frozen python scripts/validate_component_partonomy.py`, and
  `uv run --frozen python scripts/validate_sssom_invariants.py`.
