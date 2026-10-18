# `data/ingredients/mapped/Dextran.yaml`

## Verdict

Needs curation. The exact `CHEBI:52071` dextran identity, CAS payload, ChEBI
synonyms, occurrence rows, and final SSSOM `other` column pass, but the
carbon-source role is still inferred only from ChEBI ancestry.

## Identity

- Reviewed record: `data/ingredients/mapped/Dextran.yaml`.
- Identifier and grounding: `identifier: CHEBI:52071` with
  `ontology_mapping.ontology_id: CHEBI:52071`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Local OAK resolves `CHEBI:52071` to active canonical label `dextran`, CAS
  xref `9004-54-0`, and related synonyms including the stored glucosyl
  polymer labels, `Dextran 40`, `Dextran 70`, `Dextran 75`, `dextrane`,
  `dextrano`, `dextrans`, and `dextranum`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Destomycin.yaml data/ingredients/mapped/Desulfovibrio_Trace_Elements.yaml data/ingredients/mapped/Deuterated_Glucose.yaml data/ingredients/mapped/Dextran.yaml data/ingredients/mapped/Dextrin.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Dextran.yaml data/ingredients/mapped/Dextrin.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed the OBO/CHEBI subset.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:52071 CHEBI:28675`:
  returned the canonical ChEBI label, CAS xref, and synonym metadata for
  `CHEBI:52071`.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.
- `uv run --frozen python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`:
  passed; all id-label pairs corresponded, with only full-corpus plausibility
  warnings.

## Evidence

- `mappings/ingredient_mappings_oak_ols_review.tsv` and
  `mappings/ingredient_mappings_row_review_manifest.tsv` both record the
  `CHEBI:52071` mapping as confirmed with no row-review action required.
- The hidden/ignored-inclusive exact search over `data/ingredients`,
  `data/curated`, `mappings`, `docs/data`, `src`, `scripts`, and `tests`
  found the expected active `Dextran` row and the separate unresolved
  `Dextran_Mw_1270` and `Dextran_Mw_200000` records, with no stale exact
  parent row collapsing those molecular-weight-specific forms into generic
  dextran.
- `mappings/culturemech_recipe_membership.tsv` has three `CHEBI:52071` rows,
  matching `occurrence_statistics.total_occurrences: 3` and `media_count: 3`.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps `MIM:Dextran`
  to `CHEBI:52071` with `skos:exactMatch`, canonical object label `dextran`,
  CHEBI object source, ChEBI synonyms, and `CAS:9004-54-0` in `other`.
- Major: `nutritional_roles.CARBON_SOURCE` is supported only by an
  `infer_roles_from_chebi_ancestry` `COMPUTATIONAL_PREDICTION` whose curator
  note explicitly calls the assignment provisional.

## Completeness

- The ChEBI identity, CAS RN, occurrence statistics, kg-microbe node ID,
  synonyms, and curation history are populated.
- Chemical structure, mixture components, supplied forms, and environmental
  contexts are correctly empty for this generic polymer class record.

## Recommended Edits

- Major: source or remove `nutritional_roles.CARBON_SOURCE` in
  `data/ingredients/mapped/Dextran.yaml`, then synchronize
  `data/curated/mapped_ingredients.yaml`.
