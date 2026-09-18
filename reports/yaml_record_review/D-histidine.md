# `data/ingredients/mapped/D-histidine.yaml`

## Verdict

Pass. The record is an exact active ChEBI match for D-histidine, the single
BacDive source occurrence is traceable, no unsupported roles are asserted, and
the final SSSOM row has an empty `other` payload.

## Identity

- Reviewed record: `data/ingredients/mapped/D-histidine.yaml`.
- Identifier and grounding: `identifier: CHEBI:27947` with
  `ontology_mapping.ontology_id: CHEBI:27947`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Local OAK resolves `CHEBI:27947` to active `D-histidine` with formula
  `C6H9N3O2`, charge `0`, InChI, SMILES, CAS `351-50-8`, and exact
  D-histidine synonyms.
- The MicrobeDecoder source label is exactly `D-histidine`, so the lexical
  match preserves D stereochemistry.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/D-histidine.yaml data/ingredients/mapped/D-limonene.yaml data/ingredients/mapped/D-malate.yaml data/ingredients/mapped/D-mannitol.yaml data/ingredients/mapped/D-mannose.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/D-histidine.yaml data/ingredients/mapped/D-malate.yaml data/ingredients/mapped/D-mannitol.yaml data/ingredients/mapped/D-mannose.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed the 4-file CHEBI subset. `D-limonene` was skipped because its `cas:`
  fallback crashes the OAK SQL label lookup with
  `sqlite3.OperationalError: no such table: rdfs_label_statement`.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:27947 CHEBI:15588 CHEBI:16899 CHEBI:16024`:
  returned formula, charge, CAS, InChI, SMILES, mass, synonyms, and xrefs for
  `CHEBI:27947`.
- `uv run --frozen python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`:
  passed; all id-label pairs corresponded, with full-corpus plausibility
  warnings only.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- `data/custom/microbedecoder/ingredient_candidates.tsv` and
  `data/custom/microbedecoder/unmapped_labels.tsv` both contain the exact
  `D-histidine` label with 1 BacDive utilization mention, matching
  `source_occurrences`.
- `mappings/culturemech_recipe_membership.tsv` has no rows for `CHEBI:27947`,
  matching `occurrence_statistics.media_count: 0` and
  `total_occurrences: 0`.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:D-histidine` to `CHEBI:27947` with `skos:exactMatch`, canonical object
  label `D-histidine`, CHEBI object source, and an empty `other` column.
- The record does not assert nutritional roles, environmental contexts,
  synonyms, or mixture components, so there are no unsupported claim-specific
  evidence objects to resolve.

## Completeness

- The hidden/ignored-inclusive exact-identifier search over active `data`
  surfaces found no second primary record or parent-mapping record for
  `CHEBI:27947`.
- The chemical-property block is complete for the active ChEBI small molecule.
- The aggregate copy in `data/curated/mapped_ingredients.yaml` and the
  per-record YAML agree.

## Recommended Edits

- None.
