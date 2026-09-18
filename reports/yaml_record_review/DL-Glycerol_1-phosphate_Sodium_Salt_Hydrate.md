# `data/ingredients/mapped/DL-Glycerol_1-phosphate_Sodium_Salt_Hydrate.yaml`

## Verdict

Needs curation. The local CAS identity, close mapping to the anhydrous
`CHEBI:14336` parent, and exact registry row are structurally correct, but the
final close-match row still publishes anhydrous parent synonyms for the
sodium-salt hydrate subject, and the `CARBON_SOURCE` role is still only a
provisional computational assertion.

## Identity

- Reviewed record:
  `data/ingredients/mapped/DL-Glycerol_1-phosphate_Sodium_Salt_Hydrate.yaml`.
- Identifier and grounding: `identifier: cas:17603-42-8` with
  `ontology_mapping.ontology_id: CHEBI:14336`, source `CHEBI`,
  `mapping_quality: CLOSE_MATCH`, and `mapping_status: MAPPED`.
- Local OAK resolves `CHEBI:14336` to active `glycerol 1-phosphate`, formula
  `C3H9O6P`, charge `0`, non-isomeric InChI, SMILES, and exact anhydrous-parent
  synonyms `2,3-dihydroxypropyl dihydrogen phosphate` and
  `glycerol 1-(dihydrogen phosphate)`.
- PubChem resolves `17603-42-8` to sodium glycerol-phosphate entries, including
  the stored CID 23672316 and a racemic glycerol 1-phosphate sodium salt
  hydrate entry, supporting a distinct sodium-salt identity rather than exact
  collapse onto `CHEBI:14336`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/DL-3-Hydroxyisobutyric_Acid_Sodium_Salt.yaml data/ingredients/mapped/DL-Glyceraldehyde_3-phosphate.yaml data/ingredients/mapped/DL-Glycerol_1-phosphate_Sodium_Salt_Hydrate.yaml data/ingredients/mapped/DL-Histidine_Monohydrochloride_Monohydrate.yaml data/ingredients/mapped/DL-Isocitric_Acid_Trisodium_Salt_Hydrate.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/DL-3-Hydroxyisobutyric_Acid_Sodium_Salt.yaml data/ingredients/mapped/DL-Glyceraldehyde_3-phosphate.yaml data/ingredients/mapped/DL-Glycerol_1-phosphate_Sodium_Salt_Hydrate.yaml data/ingredients/mapped/DL-Histidine_Monohydrochloride_Monohydrate.yaml data/ingredients/mapped/DL-Isocitric_Acid_Trisodium_Salt_Hydrate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for all 5 files.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:18064 CHEBI:17138 CHEBI:14336 CHEBI:172950`:
  returned formula, charge, InChI, InChIKey, SMILES, mass, synonyms, and xrefs
  for `CHEBI:14336`.
- `curl -L ... /compound/name/17603-42-8/property/.../JSON`: PubChem resolved
  the CAS value to sodium glycerol-phosphate entries, including CID 23672316.
- `uv run --frozen python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`:
  passed; all id-label pairs corresponded, with full-corpus plausibility
  warnings only.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- `mappings/culturemech_recipe_membership.tsv` has no rows for
  `cas:17603-42-8`, matching `occurrence_statistics.media_count: 0` and
  `total_occurrences: 0`.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:DL-Glycerol_1-phosphate_Sodium_Salt_Hydrate` to `CHEBI:14336` with
  `skos:closeMatch`, matching the August 2026 hydrate regrade.
- The final close-match row still publishes
  `2,3-dihydroxypropyl dihydrogen phosphate` and
  `glycerol 1-(dihydrogen phosphate)` in `other`; both are ChEBI synonyms for
  anhydrous glycerol 1-phosphate and omit the sodium-salt hydrate boundary.
- The final registry row maps exactly to `cas:17603-42-8` and publishes only
  `CAS:17603-42-8`.
- The `CARBON_SOURCE` role is supported only by a
  `COMPUTATIONAL_PREDICTION` evidence object whose curator note says the
  name-pattern role is provisional and recommends review.

## Completeness

- The hidden/ignored-inclusive exact-identifier search over active `data`,
  `mappings`, `docs`, `scripts`, and `tests` found no second primary record for
  `cas:17603-42-8`.
- The hydrate relation to the anhydrous parent is represented honestly as
  `CLOSE_MATCH`.
- The record has no source occurrences, component decomposition, or
  environmental contexts to resolve.

## Recommended Edits

- In
  `data/ingredients/mapped/DL-Glycerol_1-phosphate_Sodium_Salt_Hydrate.yaml`,
  remove or retype the two anhydrous `CHEBI:14336` synonyms so the final SSSOM
  builder does not publish them as `other` for the hydrate subject.
- In the same file, remove the provisional `CARBON_SOURCE` role or replace its
  `COMPUTATIONAL_PREDICTION` evidence with inspected claim-level evidence for
  this supplied form.
- Regenerate synchronized curated and SSSOM products, then rerun
  `uv run --frozen python scripts/validate_strict.py`,
  `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/DL-Glycerol_1-phosphate_Sodium_Salt_Hydrate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`,
  `uv run --frozen python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`,
  and `uv run --frozen python scripts/validate_sssom_invariants.py`.
