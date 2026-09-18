# `data/ingredients/mapped/D-threonine.yaml`

## Verdict

Pass. The record is an exact active ChEBI match for D-threonine, the single
BacDive source occurrence is traceable, and the published SSSOM row has an
empty `other` payload.

## Identity

- Reviewed record: `data/ingredients/mapped/D-threonine.yaml`.
- Identifier and grounding: `identifier: CHEBI:16398` with
  `ontology_mapping.ontology_id: CHEBI:16398`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Local OAK resolves `CHEBI:16398` to `D-threonine` with formula `C4H9NO3`,
  charge `0`, InChI, SMILES, CAS `632-20-2`, and exact D-threonine synonyms.
- The MicrobeDecoder source label is exactly `D-threonine`, so the lexical
  match preserves D stereochemistry.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/D-tagatose.yaml data/ingredients/mapped/D-threonine.yaml data/ingredients/mapped/D-trehalose_Dihydrate.yaml data/ingredients/mapped/D-tryptophan.yaml data/ingredients/mapped/D-valine.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/D-tagatose.yaml data/ingredients/mapped/D-threonine.yaml data/ingredients/mapped/D-trehalose_Dihydrate.yaml data/ingredients/mapped/D-tryptophan.yaml data/ingredients/mapped/D-valine.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for all 5 files.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:16443 CHEBI:16398 CHEBI:232797 CHEBI:16296 CHEBI:27477`:
  returned formula, charge, CAS, InChI, SMILES, mass, synonyms, and xrefs for
  `CHEBI:16398`.
- `uv run --frozen python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`:
  passed; all id-label pairs corresponded, with full-corpus plausibility
  warnings only.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- `data/custom/microbedecoder/ingredient_candidates.tsv` and
  `data/custom/microbedecoder/unmapped_labels.tsv` both contain the exact
  `D-threonine` label with 1 BacDive utilization mention, matching
  `source_occurrences`.
- `mappings/culturemech_recipe_membership.tsv` has no rows for `CHEBI:16398`,
  matching `occurrence_statistics.media_count: 0` and
  `total_occurrences: 0`.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:D-threonine` to `CHEBI:16398` with `skos:exactMatch`, canonical object
  label `D-threonine`, CHEBI object source, and an empty `other` column.
- The record does not assert nutritional roles, environmental contexts,
  synonyms, or mixture components, so there are no unsupported claim-specific
  evidence objects to resolve.

## Completeness

- The hidden/ignored-inclusive exact-identifier search over active `data`
  surfaces found no second primary record or parent-mapping record for
  `CHEBI:16398`.
- The chemical-property block is complete for the active ChEBI small molecule.
- The aggregate copy in `data/curated/mapped_ingredients.yaml` and the
  per-record YAML agree.

## Recommended Edits

- None.
