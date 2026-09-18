# `data/ingredients/mapped/D-glucuronic_Acid.yaml`

## Verdict

Needs curation. The exact `CHEBI:4178` identity, CAS value, German ChEBI
synonyms, CultureMech occurrence count, and final SSSOM payload pass, but the
record still asserts `CARBON_SOURCE` from a provisional ChEBI-ancestry
prediction.

## Identity

- Reviewed record: `data/ingredients/mapped/D-glucuronic_Acid.yaml`.
- Identifier and grounding: `identifier: CHEBI:4178` with
  `ontology_mapping.ontology_id: CHEBI:4178`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Local OAK resolves `CHEBI:4178` to `D-glucuronic acid` with formula
  `C6H10O7`, charge `0`, and CAS `6556-12-3`, matching
  `chemical_properties.cas_rn`.
- The exact match is to the neutral acid. The separate
  `D-Glucuronic_Acid_Sodium_Salt_Monohydrate` record intentionally preserves
  its CAS identity and only close-matches the `CHEBI:4178` parent.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/D-glucose_6-phosphate.yaml data/ingredients/mapped/D-glucuronate.yaml data/ingredients/mapped/D-glucuronic_Acid.yaml data/ingredients/mapped/D-glutamine.yaml data/ingredients/mapped/D-glycerate.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/D-glucose_6-phosphate.yaml data/ingredients/mapped/D-glucuronate.yaml data/ingredients/mapped/D-glucuronic_Acid.yaml data/ingredients/mapped/D-glutamine.yaml data/ingredients/mapped/D-glycerate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for all 5 files.
- `uv run --frozen runoak -i sqlite:obo:chebi aliases CHEBI:14314 CHEBI:15748 CHEBI:4178 CHEBI:17061 CHEBI:16659`:
  returned `D-Glucuronsaeure` and `D-Glukuronsaeure` as related synonyms on
  `CHEBI:4178`.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:14314 CHEBI:15748 CHEBI:4178 CHEBI:17061 CHEBI:16659`:
  returned formula, charge, CAS, mass, synonyms, and xrefs for `CHEBI:4178`.
- `uv run --frozen python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`:
  passed; all id-label pairs corresponded, with full-corpus plausibility
  warnings only.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- `mappings/culturemech_recipe_membership.tsv` contains two rows for
  `CHEBI:4178`, matching `occurrence_statistics.media_count: 2` and
  `total_occurrences: 2`.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:D-glucuronic_Acid` to `CHEBI:4178` with `skos:exactMatch`, canonical
  object label `D-glucuronic acid`, CHEBI object source, and only
  OAK-confirmed terms in `other`: `D-Glucuronsaeure`,
  `D-Glukuronsaeure`, and `CAS:6556-12-3`.
- The raw CultureMech `(sodium salt)` synonym is filtered by
  `src/mediaingredientmech/synonym_policy.py` and does not leak into the final
  SSSOM `other` column.
- The `CARBON_SOURCE` role is supported only by a
  `COMPUTATIONAL_PREDICTION` evidence object whose curator note says the role
  was inferred from ChEBI ancestry and recommends review.

## Completeness

- The hidden/ignored-inclusive exact-identifier search over active `data`
  surfaces found no second primary record for `CHEBI:4178`.
  `D-Glucuronic_Acid_Sodium_Salt_Monohydrate` separately close-matches this
  parent term and keeps a distinct CAS primary identifier.
- CAS, molecular formula, occurrence statistics, ChEBI synonym payloads, and
  ingredient type are populated.
- No mixture decomposition is required for the neutral D-glucuronic acid
  record.

## Recommended Edits

- In `data/ingredients/mapped/D-glucuronic_Acid.yaml`, remove the provisional
  `CARBON_SOURCE` role or replace its `COMPUTATIONAL_PREDICTION` evidence with
  inspected claim-level evidence.
- Regenerate synchronized curated and SSSOM products, then rerun
  `uv run --frozen python scripts/validate_strict.py`,
  `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/D-glucuronic_Acid.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`,
  `uv run --frozen python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`,
  and `uv run --frozen python scripts/validate_sssom_invariants.py`.
