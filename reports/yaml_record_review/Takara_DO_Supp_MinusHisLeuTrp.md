# `data/ingredients/mapped/Takara_DO_Supp_MinusHisLeuTrp.yaml`

## Verdict

Needs curation - major. The local fallback identity, occurrence count,
aggregate row, and final exact registry row pass, but this commercial dropout
supplement is still represented only as an opaque stock solution and lacks its
component-level recipe.

## Identity

- Reviewed record:
  `data/ingredients/mapped/Takara_DO_Supp_MinusHisLeuTrp.yaml`.
- Identifier and grounding:
  `identifier: kgmicrobe.ingredient:takara_do_supp_minushisleutrp` with the
  same `ontology_mapping.ontology_id`, label `Takara_DO_Supp_MinusHisLeuTrp`,
  source `kgmicrobe.ingredient`, `mapping_quality: FALLBACK_REGISTRY`, and
  `mapping_status: MAPPED`.
- Ingredient type: `STOCK_SOLUTION`.
- Occurrences: 2 CultureMech recipe occurrences across 2 media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `TYGVS_Glucose` through `Takara_DO_Supp_MinusHisLeuTrp`: exited 0 and wrote
  zero ERROR rows.
- Direct old Engine A/OBO term validation was skipped for this local
  `kgmicrobe.ingredient` fallback row because that prefix is intentionally
  outside the CHEBI-focused OBO term subset.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh exact OLS4 search for `Takara_DO_Supp_MinusHisLeuTrp` returned zero
  results, and fresh PubChem name lookup found no CID.
- `mappings/culturemech_recipe_membership.tsv` has two
  `kgmicrobe.ingredient:takara_do_supp_minushisleutrp` rows, agreeing with
  `total_occurrences: 2` and `media_count: 2`.
- The final SSSOM has exactly one exact registry row for
  `MIM:Takara_DO_Supp_MinusHisLeuTrp`, points at
  `kgmicrobe.ingredient:takara_do_supp_minushisleutrp`, names
  `kgm:ingredient`, and publishes no unsafe `other` synonyms.
- Major: the curation history says this commercial dropout supplement was left
  as a pre-mix pending component-level curation, but the record still has no
  `components` list and no `component_assertion`.

## Completeness

- The local fallback identity, aggregate row, occurrence count, and final SSSOM
  row agree mechanically.
- The missing component-level representation is still consequential because the
  record is a named commercial dropout supplement rather than an indivisible
  ontology class or an explicitly undefined mixture.
- An ignored/hidden search of local curated, mapping, generated, report,
  source, and documentation paths found the expected CultureMech fallback,
  occurrence-membership, aggregate, final SSSOM, and generated rows but no
  maintained component formula for this stock solution.

## Recommended Edits

- Major: curate the Takara dropout supplement formula in
  `data/ingredients/mapped/Takara_DO_Supp_MinusHisLeuTrp.yaml`, adding a
  supported `components` list and `component_assertion`.
- Major: regenerate generated component and product artifacts after the
  per-record YAML gains a component-level representation.
