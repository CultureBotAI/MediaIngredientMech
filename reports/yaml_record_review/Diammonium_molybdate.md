# `data/ingredients/mapped/Diammonium_molybdate.yaml`

## Verdict

Needs curation. The CAS-to-ChEBI identity, structure fields, source-backed
trace-element role, tetrahydrate label rejections, and occurrence count pass.
One anhydrous heptamolybdate formula remains typed as an exact synonym and
still leaks to final SSSOM `other`.

## Identity

- Reviewed record: `data/ingredients/mapped/Diammonium_molybdate.yaml`.
- Identifier and grounding: `identifier: CHEBI:91249` with
  `ontology_mapping.ontology_id: CHEBI:91249`, source `CHEBI`,
  `mapping_quality: CAS_RN_LOOKUP`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Local OAK resolves `CHEBI:91249` to active `ammonium molybdate`, an
  ammonium salt composed of two ammonium ions per molybdate ion, CAS xref
  `13106-76-8`, formula `2H4N.MoO4`, InChI, SMILES, and the stored
  kg-microbe synonyms except the heptamolybdate formula.
- The sibling `Ammonium_Molybdate_Tetrahydrate` is correctly modeled as its own
  `cas:12054-85-2` identity with only a closeMatch to anhydrous
  `CHEBI:91249`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Dextrose.yaml data/ingredients/mapped/Diacetyl.yaml data/ingredients/mapped/Diallyl_Sulfide.yaml data/ingredients/mapped/Diaminopimelic_Acid.yaml data/ingredients/mapped/Diammonium_molybdate.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Dextrose.yaml data/ingredients/mapped/Diacetyl.yaml data/ingredients/mapped/Diallyl_Sulfide.yaml data/ingredients/mapped/Diaminopimelic_Acid.yaml data/ingredients/mapped/Diammonium_molybdate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed all 5 records.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:91249`:
  returned the canonical label, synonyms, CAS xref, formula, InChI, SMILES,
  charge, and mass for `CHEBI:91249`.
- `curl -L ... q=(NH4)6Mo7O24`: live OLS returned 0 rows.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- The hidden/ignored-inclusive exact search over `data/ingredients`,
  `data/curated`, `mappings`, `docs/data`, `src`, `scripts`, and `tests`
  found the expected anhydrous ammonium molybdate record, the separate
  ammonium molybdate tetrahydrate record, hydrate-review rows for rejected
  tetrahydrate labels, and `other_cross_record_baseline.tsv` row 10 for the
  unresolved sibling formula.
- The 2026-09-12 `reject_hidden_hydrate_synonym_collapses` event correctly
  converted `(NH4)6Mo7O24 x 4 H2O`, `Molybdic acid ammonium salt
  tetrahydrate`, `Ammonium heptamolybdate tetrahydrate`, and
  `(NH4)6Mo7O24.4H2O` to `REJECTED_LABEL`.
- Major: `(NH4)6Mo7O24` is still typed as an exact synonym in YAML and still
  appears in final SSSOM `other`. It is a heptamolybdate formula and is not a
  synonym of two-ammonium-per-molybdate `CHEBI:91249`.
- `mappings/culturemech_recipe_membership.tsv` has 239 `CHEBI:91249` rows,
  matching `occurrence_statistics.total_occurrences: 239` and
  `media_count: 239`.
- `nutritional_roles.TRACE_ELEMENT` is source-backed by the original
  CultureMech `Role: Mineral` text; the raw role/property label is correctly
  filtered from final SSSOM.

## Completeness

- CAS RN, formula, InChI, SMILES, kg-microbe node ID, occurrence statistics,
  source-backed trace-element role, and hydrate-rejection history are
  populated.
- Mixture components, supplied forms, and environmental contexts are correctly
  empty for this single salt record.

## Recommended Edits

- Major: change the `(NH4)6Mo7O24` synonym in
  `data/ingredients/mapped/Diammonium_molybdate.yaml` from active synonym
  export to `REJECTED_LABEL`, then synchronize
  `data/curated/mapped_ingredients.yaml` and regenerate final SSSOM so the
  anhydrous heptamolybdate token is removed from `other`.
- Minor: resolve or retire
  `mappings/other_cross_record_baseline.tsv` row 10 after the heptamolybdate
  formula is no longer an active synonym on `MIM:Diammonium_molybdate`.
