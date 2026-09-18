# `data/ingredients/mapped/D-sorbitol.yaml`

## Verdict

Needs curation. The `CHEBI:17924` D-glucitol identity, CAS, formula,
structure, 3/3 CultureMech count, and final SSSOM synonym payload pass, but the
record still asserts `CARBON_SOURCE` from a provisional ChEBI-ancestry
prediction.

## Identity

- Reviewed record: `data/ingredients/mapped/D-sorbitol.yaml`.
- Identifier and grounding: `identifier: CHEBI:17924` with
  `ontology_mapping.ontology_id: CHEBI:17924`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Local OAK resolves `CHEBI:17924` to `D-glucitol` with formula `C6H14O6`,
  charge `0`, InChI, SMILES, CAS `50-70-4`, and D-sorbitol / D-glucitol
  synonyms, matching the stored `kg_microbe_node_id` and chemistry block.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/D-ornithine.yaml data/ingredients/mapped/D-psicose.yaml data/ingredients/mapped/D-rhamnose.yaml data/ingredients/mapped/D-sorbitol.yaml data/ingredients/mapped/D-sorbose.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/D-ornithine.yaml data/ingredients/mapped/D-psicose.yaml data/ingredients/mapped/D-rhamnose.yaml data/ingredients/mapped/D-sorbitol.yaml data/ingredients/mapped/D-sorbose.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for all 5 files.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:16176 CHEBI:27605 CHEBI:63150 CHEBI:17924 CHEBI:17317`:
  returned formula, charge, CAS, InChI, SMILES, mass, synonyms, and xrefs for
  `CHEBI:17924`.
- `uv run --frozen python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`:
  passed; all id-label pairs corresponded, with full-corpus plausibility
  warnings only.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- `mappings/culturemech_recipe_membership.tsv` contains 3 rows for
  `CHEBI:17924`, matching `occurrence_statistics.media_count: 3` and
  `total_occurrences: 3`.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:D-sorbitol` to `CHEBI:17924` with `skos:exactMatch`, canonical object
  label `D-glucitol`, CHEBI object source, CAS `50-70-4`, and only
  ChEBI-backed D-sorbitol / D-glucitol tokens in `other`.
- The `CARBON_SOURCE` role is supported only by a
  `COMPUTATIONAL_PREDICTION` evidence object whose curator note says the role
  was inferred from ChEBI ancestry and recommends review.

## Completeness

- The hidden/ignored-inclusive exact-identifier search over active `data`
  surfaces found no second primary record or parent-mapping record for
  `CHEBI:17924`.
- CAS, formula, InChI, SMILES, occurrence statistics, and kg-microbe node id are
  populated.
- No mixture decomposition is required for the free D-sorbitol record.

## Recommended Edits

- In `data/ingredients/mapped/D-sorbitol.yaml`, remove the provisional
  `CARBON_SOURCE` role or replace its `COMPUTATIONAL_PREDICTION` evidence with
  inspected claim-level evidence.
- Regenerate synchronized curated and SSSOM products, then rerun
  `uv run --frozen python scripts/validate_strict.py`,
  `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/D-sorbitol.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`,
  `uv run --frozen python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`,
  and `uv run --frozen python scripts/validate_sssom_invariants.py`.
