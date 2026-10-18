# `data/ingredients/mapped/DL-3-Hydroxyisobutyric_Acid_Sodium_Salt.yaml`

## Verdict

Pass. The record preserves `cas:1219589-99-7` as the sodium-salt identity,
maps narrowly to the named acid parent `CHEBI:18064` rather than the old generic
`sodium salt` class, has the required registry and kg-microbe identity rows in
final SSSOM, and publishes no parent-only synonyms.

## Identity

- Reviewed record:
  `data/ingredients/mapped/DL-3-Hydroxyisobutyric_Acid_Sodium_Salt.yaml`.
- Identifier and grounding: `identifier: cas:1219589-99-7` with
  `ontology_mapping.ontology_id: CHEBI:18064`, source `CHEBI`,
  `mapping_quality: NARROW_MATCH`, and `mapping_status: MAPPED`.
- Local OAK resolves `CHEBI:18064` to active `3-hydroxyisobutyric acid`,
  formula `C4H8O3`, charge `0`, non-isomeric InChI, SMILES, and exact synonym
  `3-hydroxy-2-methylpropanoic acid`.
- PubChem resolves `1219589-99-7` to `Sodium 3-hydroxy-2-methylpropanoate`,
  formula `C4H7NaO3`, matching the record's stored sodium-salt structure.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/DL-3-Hydroxyisobutyric_Acid_Sodium_Salt.yaml data/ingredients/mapped/DL-Glyceraldehyde_3-phosphate.yaml data/ingredients/mapped/DL-Glycerol_1-phosphate_Sodium_Salt_Hydrate.yaml data/ingredients/mapped/DL-Histidine_Monohydrochloride_Monohydrate.yaml data/ingredients/mapped/DL-Isocitric_Acid_Trisodium_Salt_Hydrate.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/DL-3-Hydroxyisobutyric_Acid_Sodium_Salt.yaml data/ingredients/mapped/DL-Glyceraldehyde_3-phosphate.yaml data/ingredients/mapped/DL-Glycerol_1-phosphate_Sodium_Salt_Hydrate.yaml data/ingredients/mapped/DL-Histidine_Monohydrochloride_Monohydrate.yaml data/ingredients/mapped/DL-Isocitric_Acid_Trisodium_Salt_Hydrate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for all 5 files.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:18064 CHEBI:17138 CHEBI:14336 CHEBI:172950`:
  returned formula, charge, InChI, InChIKey, SMILES, mass, synonyms, and xrefs
  for `CHEBI:18064`.
- `curl -L ... /compound/name/1219589-99-7/property/.../JSON`: PubChem
  resolved the CAS value to CID 71311737, `Sodium 3-hydroxy-2-methylpropanoate`.
- `uv run --frozen python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`:
  passed; all id-label pairs corresponded, with full-corpus plausibility
  warnings only.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- `mappings/culturemech_recipe_membership.tsv` has no rows for
  `cas:1219589-99-7`, matching `occurrence_statistics.media_count: 0` and
  `total_occurrences: 0`.
- The curation evidence and history record the August 2026 correction from the
  generic `CHEBI:26714` sodium-salt parent to the chemically informative
  `CHEBI:18064` acid parent.
- The final `mappings/ingredient_mappings.sssom.tsv` rows include the required
  `skos:narrowMatch` to `CHEBI:18064`, the `skos:exactMatch` registry row for
  `cas:1219589-99-7`, and the `skos:exactMatch` kg-microbe identity row
  required for a subject mapped through a broader ChEBI parent.
- The ChEBI parent row has an empty `other` value, and the identity rows
  publish only `CAS:1219589-99-7`.

## Completeness

- The hidden/ignored-inclusive exact-identifier search over active `data`,
  `mappings`, `docs`, `scripts`, and `tests` found no second primary record for
  `cas:1219589-99-7`.
- The parent/child identity loss is represented by `NARROW_MATCH` plus
  companion local identity rows.
- The record has no source occurrences, nutritional roles, component
  decomposition, or environmental contexts to resolve.

## Recommended Edits

- None.
