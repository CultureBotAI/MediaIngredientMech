# `data/ingredients/mapped/DL-Tyrosine.yaml`

## Verdict

Needs curation. The record correctly documents that DL-Tyrosine should only be
close to the stereo-unspecified ChEBI tyrosine parent, the 18/18 occurrence
count is traceable, and live OLS still has no exact DL-tyrosine class, but the
record uses `CHEBI:18186` as its own identifier, so final SSSOM emits an
identity-preserving `skos:exactMatch` row to a parent that the YAML grades as
`CLOSE_MATCH`.

## Identity

- Reviewed record: `data/ingredients/mapped/DL-Tyrosine.yaml`.
- Current identifier and grounding: `identifier: CHEBI:18186` with
  `ontology_mapping.ontology_id: CHEBI:18186`, source `CHEBI`,
  `mapping_quality: CLOSE_MATCH`, and `mapping_status: MAPPED`.
- Local OAK resolves `CHEBI:18186` to active stereo-unspecified `tyrosine` with
  formula `C9H11NO3`, charge `0`, non-isomeric InChI, SMILES, KEGG xref
  `C01536`, and exact synonym `Tyrosine`.
- Live OLS exact search for `DL-Tyrosine` still returns only derivatives such
  as `DL-tyrosine betaine` and `thyronine`, not a class for the DL racemate.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/DL-Tyrosine.yaml data/ingredients/mapped/DL-glyceraldehyde.yaml data/ingredients/mapped/DL_Vitamins.yaml data/ingredients/mapped/DNA_From_Salmon.yaml data/ingredients/mapped/D_-carvone.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/DL-Tyrosine.yaml data/ingredients/mapped/DL-glyceraldehyde.yaml data/ingredients/mapped/DL_Vitamins.yaml data/ingredients/mapped/DNA_From_Salmon.yaml data/ingredients/mapped/D_-carvone.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  failed when non-OBO fallback targets were included.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/DL-Tyrosine.yaml data/ingredients/mapped/DL-glyceraldehyde.yaml data/ingredients/mapped/D_-carvone.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed the 3-file ChEBI subset after skipping the `kgmicrobe.ingredient:` and
  `cas:` fallback records.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:18186 CHEBI:5445 CHEBI:15399`:
  returned formula, charge, InChI, InChIKey, SMILES, mass, synonyms, and xrefs
  for `CHEBI:18186`.
- `curl -L ... q=DL-Tyrosine&ontology=chebi&exact=true`: live OLS returned two
  derivative classes and no exact ChEBI class for the DL racemate.
- `uv run --frozen python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`:
  passed; all id-label pairs corresponded, with full-corpus plausibility
  warnings only. This self-identifier/close-match semantic conflict is outside
  that lexical validator.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- `mappings/culturemech_recipe_membership.tsv` contains 18 rows for
  `CHEBI:18186`, matching `occurrence_statistics.media_count: 18` and
  `total_occurrences: 18`.
- The curation history explicitly says `CLOSE_MATCH` was chosen because the
  CultureMech label names the DL racemate while `CHEBI:18186` does not
  distinguish stereochemistry.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:DL-Tyrosine` to `CHEBI:18186` with `skos:exactMatch`, because the
  record's own identifier is also `CHEBI:18186`.
- That exact SSSOM row contradicts the record-level `CLOSE_MATCH` decision and
  collapses a DL subject onto a stereo-unspecified parent that should only be a
  close match.

## Completeness

- The hidden/ignored-inclusive exact-identifier search over active `data`,
  `mappings`, `docs`, `scripts`, and `tests` found no second primary record for
  `CHEBI:18186`.
- The record has source occurrences and occurrence statistics, but it lacks a
  local `kgmicrobe.compound:` identity row to preserve the DL racemate
  separately from `CHEBI:18186`.
- The record does not assert nutritional roles, components, or environmental
  contexts.

## Recommended Edits

- In `data/ingredients/mapped/DL-Tyrosine.yaml`, mint a local
  `kgmicrobe.compound:dl-tyrosine` identifier, retain `CHEBI:18186` as the
  `CLOSE_MATCH` parent, and regenerate SSSOM so the final output has a close
  parent row plus a kg-microbe exact identity row rather than an exact
  `CHEBI:18186` row.
- Regenerate synchronized curated and SSSOM products, then rerun
  `uv run --frozen python scripts/validate_strict.py`,
  `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/DL-Tyrosine.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`,
  `uv run --frozen python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`,
  and `uv run --frozen python scripts/validate_sssom_invariants.py`.
