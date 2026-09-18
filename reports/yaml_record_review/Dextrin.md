# `data/ingredients/mapped/Dextrin.yaml`

## Verdict

Pass. The record exact-matches active `CHEBI:28675` dextrin, final SSSOM
exports only true ChEBI/PubChem synonyms and the CAS RN, and the raw
CultureMech role text remains filtered from the final synonym surface.

## Identity

- Reviewed record: `data/ingredients/mapped/Dextrin.yaml`.
- Identifier and grounding: `identifier: CHEBI:28675` with
  `ontology_mapping.ontology_id: CHEBI:28675`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Local OAK resolves `CHEBI:28675` to active canonical label `dextrin`, CAS
  xref `9004-53-9`, and related synonyms `dextrine`, `dextrines`, and
  `dextrins`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Destomycin.yaml data/ingredients/mapped/Desulfovibrio_Trace_Elements.yaml data/ingredients/mapped/Deuterated_Glucose.yaml data/ingredients/mapped/Dextran.yaml data/ingredients/mapped/Dextrin.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Dextran.yaml data/ingredients/mapped/Dextrin.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed the OBO/CHEBI subset.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:52071 CHEBI:28675`:
  returned the canonical ChEBI label, alternative IDs, CAS xref, and synonym
  metadata for `CHEBI:28675`.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.
- `uv run --frozen python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`:
  passed; all id-label pairs corresponded, with only full-corpus plausibility
  warnings.

## Evidence

- `mappings/ingredient_mappings_oak_ols_review.tsv` and
  `mappings/ingredient_mappings_row_review_manifest.tsv` both record the
  `CHEBI:28675` mapping as confirmed with no row-review action required.
- The hidden/ignored-inclusive exact search over `data/ingredients`,
  `data/curated`, `mappings`, `docs/data`, `src`, `scripts`, and `tests`
  found the expected active record and the historical `Dextrin_2.yaml` merge
  mention, with no live duplicate exact row.
- `mappings/culturemech_recipe_membership.tsv` has five `CHEBI:28675` rows,
  matching `occurrence_statistics.total_occurrences: 5` and `media_count: 5`.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps `MIM:Dextrin`
  to `CHEBI:28675` with `skos:exactMatch`, canonical object label `dextrin`,
  CHEBI object source, related ChEBI synonyms, and `CAS:9004-53-9` in
  `other`.
- The YAML still preserves the raw CultureMech
  `Role: Carbon source; Properties: ...` label as provenance, but
  `src/mediaingredientmech/synonym_policy.py` filters it: neither the final
  SSSOM row nor `docs/data/mapped_ingredients.csv` publishes that text as a
  synonym.
- `nutritional_roles.CARBON_SOURCE` is source-backed by the original
  CultureMech role text through `reference_type: DATABASE_ENTRY`.

## Completeness

- CAS RN, ChEBI identity, ChEBI/PubChem synonyms, occurrence statistics,
  kg-microbe node ID, source-backed carbon-source role, and merge history are
  populated.
- Chemical structure, mixture components, supplied forms, and environmental
  contexts are correctly empty for this generic mixture-of-polymers term.

## Recommended Edits

- None.
