# `data/ingredients/mapped/DL-Isocitric_Acid_Trisodium_Salt_Hydrate.yaml`

## Verdict

Needs curation. The local kg-microbe identity and close mapping to
`CHEBI:172950` correctly avoid collapsing this hydrate onto its anhydrous
parent, but stale anhydrous parent properties still leak into the record and
final SSSOM, and the `CARBON_SOURCE` role is still only a provisional
computational assertion.

## Identity

- Reviewed record:
  `data/ingredients/mapped/DL-Isocitric_Acid_Trisodium_Salt_Hydrate.yaml`.
- Identifier and grounding:
  `identifier: kgmicrobe.compound:dl-isocitric_acid_trisodium_salt_hydrate`
  with `ontology_mapping.ontology_id: CHEBI:172950`, source `CHEBI`,
  `mapping_quality: CLOSE_MATCH`, and `mapping_status: MAPPED`.
- Local OAK resolves `CHEBI:172950` to active `Isocitric acid, DL-`, formula
  `C6H5O7.3Na`, InChIKey `HWMVXEKEEAIYGB-UHFFFAOYSA-K`, and exact synonym
  `trisodium;1-hydroxypropane-1,2,3-tricarboxylate`.
- PubChem resolves the record's carried `CAS:1637-73-6` to CID 168942,
  `Isocitric acid, dl-`, formula `C6H5Na3O7`, matching the anhydrous ChEBI
  parent rather than the hydrate subject.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/DL-3-Hydroxyisobutyric_Acid_Sodium_Salt.yaml data/ingredients/mapped/DL-Glyceraldehyde_3-phosphate.yaml data/ingredients/mapped/DL-Glycerol_1-phosphate_Sodium_Salt_Hydrate.yaml data/ingredients/mapped/DL-Histidine_Monohydrochloride_Monohydrate.yaml data/ingredients/mapped/DL-Isocitric_Acid_Trisodium_Salt_Hydrate.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/DL-3-Hydroxyisobutyric_Acid_Sodium_Salt.yaml data/ingredients/mapped/DL-Glyceraldehyde_3-phosphate.yaml data/ingredients/mapped/DL-Glycerol_1-phosphate_Sodium_Salt_Hydrate.yaml data/ingredients/mapped/DL-Histidine_Monohydrochloride_Monohydrate.yaml data/ingredients/mapped/DL-Isocitric_Acid_Trisodium_Salt_Hydrate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for all 5 files.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:18064 CHEBI:17138 CHEBI:14336 CHEBI:172950`:
  returned formula, InChI, InChIKey, SMILES, mass, synonyms, and xrefs for
  `CHEBI:172950`.
- `curl -L ... /compound/name/1637-73-6/property/.../JSON`: PubChem resolved
  the carried CAS value to the anhydrous parent.
- `uv run --frozen python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`:
  passed; all id-label pairs corresponded, with full-corpus plausibility
  warnings only.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- `mappings/culturemech_recipe_membership.tsv` has no rows for
  `kgmicrobe.compound:dl-isocitric_acid_trisodium_salt_hydrate`, matching
  `occurrence_statistics.media_count: 0` and `total_occurrences: 0`.
- The current `CLOSE_MATCH` grade correctly records that the hydrate is similar
  to, but not subsumed by, the anhydrous `CHEBI:172950` trisodium salt.
- The final `mappings/ingredient_mappings.sssom.tsv` close-match row still
  publishes `trisodium;1-hydroxypropane-1,2,3-tricarboxylate` and
  `CAS:1637-73-6` in `other`; both resolve to the anhydrous parent rather than
  the hydrate subject.
- The final kg-microbe identity row also emits `CAS:1637-73-6`, even though the
  August 2026 hydrate minting history records that this local hydrate had no
  verified CAS.
- The record's `chemical_properties` block still carries the anhydrous
  `C6H5O7.3Na` formula, InChI, SMILES, and `cas_rn: 1637-73-6` from before
  the hydrate-local registry term was minted.
- The `CARBON_SOURCE` role is supported only by a
  `COMPUTATIONAL_PREDICTION` evidence object whose curator note says the
  name-pattern role is provisional and recommends review.

## Completeness

- The hidden/ignored-inclusive exact-identifier search over active `data`,
  `mappings`, `docs`, `scripts`, and `tests` found no second primary record for
  `kgmicrobe.compound:dl-isocitric_acid_trisodium_salt_hydrate`.
- The record now has an exact local identity row and a close ChEBI parent row,
  but it still lacks hydrate-specific CAS and structure provenance.
- The record has no source occurrences, component decomposition, or
  environmental contexts to resolve.

## Recommended Edits

- In
  `data/ingredients/mapped/DL-Isocitric_Acid_Trisodium_Salt_Hydrate.yaml`,
  remove or retype the anhydrous `CHEBI:172950` synonym and clear stale
  anhydrous `chemical_properties.cas_rn`, formula, InChI, and SMILES unless a
  hydrate-specific source supports them.
- Remove the provisional `CARBON_SOURCE` role or replace its
  `COMPUTATIONAL_PREDICTION` evidence with inspected claim-level evidence for
  this supplied form.
- Regenerate synchronized curated and SSSOM products, then rerun
  `uv run --frozen python scripts/validate_strict.py`,
  `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/DL-Isocitric_Acid_Trisodium_Salt_Hydrate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`,
  `uv run --frozen python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`,
  and `uv run --frozen python scripts/validate_sssom_invariants.py`.
