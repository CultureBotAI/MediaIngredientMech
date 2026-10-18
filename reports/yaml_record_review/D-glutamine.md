# `data/ingredients/mapped/D-glutamine.yaml`

## Verdict

Needs curation. The record is an exact active ChEBI/CAS match for D-glutamine
and its final SSSOM row is clean, but the `AMINO_ACID_SOURCE` role is still a
provisional ChEBI-ancestry prediction.

## Identity

- Reviewed record: `data/ingredients/mapped/D-glutamine.yaml`.
- Identifier and grounding: `identifier: CHEBI:17061` with
  `ontology_mapping.ontology_id: CHEBI:17061`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Local OAK resolves `CHEBI:17061` to `D-glutamine` with formula `C5H10N2O3`,
  charge `0`, InChI, SMILES, CAS `5959-95-5`, and exact D-glutamine synonyms.
- The record came from CultureBotHT with the same CAS-RN, so the exact match
  preserves D stereochemistry.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/D-glucose_6-phosphate.yaml data/ingredients/mapped/D-glucuronate.yaml data/ingredients/mapped/D-glucuronic_Acid.yaml data/ingredients/mapped/D-glutamine.yaml data/ingredients/mapped/D-glycerate.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/D-glucose_6-phosphate.yaml data/ingredients/mapped/D-glucuronate.yaml data/ingredients/mapped/D-glucuronic_Acid.yaml data/ingredients/mapped/D-glutamine.yaml data/ingredients/mapped/D-glycerate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for all 5 files.
- `uv run --frozen runoak -i sqlite:obo:chebi aliases CHEBI:14314 CHEBI:15748 CHEBI:4178 CHEBI:17061 CHEBI:16659`:
  returned the expected `D-glutamine` label for `CHEBI:17061`.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:14314 CHEBI:15748 CHEBI:4178 CHEBI:17061 CHEBI:16659`:
  returned formula, charge, CAS, InChI, SMILES, mass, synonyms, and xrefs for
  `CHEBI:17061`.
- `uv run --frozen python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`:
  passed; all id-label pairs corresponded, with full-corpus plausibility
  warnings only.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- `mappings/culturemech_recipe_membership.tsv` has no rows for `CHEBI:17061`,
  matching `occurrence_statistics.media_count: 0` and
  `total_occurrences: 0`.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:D-glutamine` to `CHEBI:17061` with `skos:exactMatch`, canonical object
  label `D-glutamine`, CHEBI object source, and the same-subject
  `CAS:5959-95-5` token in `other`.
- The `AMINO_ACID_SOURCE` role is supported only by a
  `COMPUTATIONAL_PREDICTION` evidence object whose curator note says the role
  was inferred from ChEBI ancestry and recommends review.
- The record does not assert synonyms, environmental contexts, or mixture
  components, so there are no other claim-specific evidence objects to resolve.

## Completeness

- The hidden/ignored-inclusive exact-identifier search over active `data`
  surfaces found no second primary record or parent-mapping record for
  `CHEBI:17061`.
- CAS, formula, InChI, SMILES, and ingredient type are populated.
- The aggregate copy in `data/curated/mapped_ingredients.yaml` and the
  per-record YAML agree.

## Recommended Edits

- In `data/ingredients/mapped/D-glutamine.yaml`, remove the provisional
  `AMINO_ACID_SOURCE` role or replace its `COMPUTATIONAL_PREDICTION` evidence
  with inspected claim-level evidence.
- Regenerate synchronized curated and SSSOM products, then rerun
  `uv run --frozen python scripts/validate_strict.py`,
  `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/D-glutamine.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`,
  `uv run --frozen python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`,
  and `uv run --frozen python scripts/validate_sssom_invariants.py`.
