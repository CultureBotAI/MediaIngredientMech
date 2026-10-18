# `data/ingredients/mapped/D-psicose.yaml`

## Verdict

Pass. The record is an exact active ChEBI match for D-psicose, the BacDive
source count is traceable, the CultureMech count is correctly zero, and the
published SSSOM row has an empty `other` payload.

## Identity

- Reviewed record: `data/ingredients/mapped/D-psicose.yaml`.
- Identifier and grounding: `identifier: CHEBI:27605` with
  `ontology_mapping.ontology_id: CHEBI:27605`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Local OAK resolves `CHEBI:27605` to `D-psicose` with formula `C6H12O6`,
  charge `0`, InChI, SMILES, CAS `551-68-8`, and D-psicose synonyms.
- The MicrobeDecoder source label is exactly `D-psicose`, so the lexical match
  preserves D stereochemistry.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/D-ornithine.yaml data/ingredients/mapped/D-psicose.yaml data/ingredients/mapped/D-rhamnose.yaml data/ingredients/mapped/D-sorbitol.yaml data/ingredients/mapped/D-sorbose.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/D-ornithine.yaml data/ingredients/mapped/D-psicose.yaml data/ingredients/mapped/D-rhamnose.yaml data/ingredients/mapped/D-sorbitol.yaml data/ingredients/mapped/D-sorbose.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for all 5 files.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:16176 CHEBI:27605 CHEBI:63150 CHEBI:17924 CHEBI:17317`:
  returned formula, charge, CAS, InChI, SMILES, mass, synonyms, and xrefs for
  `CHEBI:27605`.
- `uv run --frozen python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`:
  passed; all id-label pairs corresponded, with full-corpus plausibility
  warnings only.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- `data/custom/microbedecoder/ingredient_candidates.tsv` and
  `data/custom/microbedecoder/unmapped_labels.tsv` both contain the exact
  `D-psicose` label with 19 BacDive utilization mentions, matching
  `source_occurrences`.
- `mappings/culturemech_recipe_membership.tsv` has no rows for `CHEBI:27605`,
  matching `occurrence_statistics.media_count: 0` and
  `total_occurrences: 0`.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:D-psicose` to `CHEBI:27605` with `skos:exactMatch`, canonical object
  label `D-psicose`, CHEBI object source, and an empty `other` column.
- The record does not assert nutritional roles, environmental contexts,
  synonyms, or mixture components, so there are no unsupported claim-specific
  evidence objects to resolve.

## Completeness

- The hidden/ignored-inclusive exact-identifier search over active `data`
  surfaces found no second primary record or parent-mapping record for
  `CHEBI:27605`.
- The chemical-property block is complete for the active ChEBI small molecule.
- The aggregate copy in `data/curated/mapped_ingredients.yaml` and the
  per-record YAML agree.

## Recommended Edits

- None.
