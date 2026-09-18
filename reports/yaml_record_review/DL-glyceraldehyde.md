# `data/ingredients/mapped/DL-glyceraldehyde.yaml`

## Verdict

Needs curation. The September stereochemical repair correctly preserved the DL
racemate as a CAS-backed local identity with a narrow mapping to `CHEBI:5445`,
the final SSSOM parent row no longer emits a broader same-formula synonym, and
the CAS and kg-microbe exact identity rows are present, but the carbon-source
role is still only a provisional computational assertion.

## Identity

- Reviewed record: `data/ingredients/mapped/DL-glyceraldehyde.yaml`.
- Identifier and grounding: `identifier: cas:56-82-6` with
  `ontology_mapping.ontology_id: CHEBI:5445`, source `CHEBI`,
  `mapping_quality: NARROW_MATCH`, and `mapping_status: MAPPED`.
- Local OAK resolves `CHEBI:5445` to active `glyceraldehyde`, formula
  `C3H6O3`, charge `0`, non-isomeric InChI, SMILES, CAS xref `56-82-6`, and
  exact synonym `2,3-dihydroxypropanal`.
- PubChem resolves `56-82-6` to `Glyceraldehyde`, formula `C3H6O3`, and the
  same non-isomeric InChIKey as the local ChEBI parent.

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
  for `CHEBI:5445`.
- `curl -L ... /compound/name/56-82-6/property/.../JSON`: PubChem resolved the
  CAS value to CID 751, `Glyceraldehyde`.
- `uv run --frozen python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`:
  passed; all id-label pairs corresponded, with full-corpus plausibility
  warnings only.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- `mappings/culturemech_recipe_membership.tsv` has no rows for `cas:56-82-6`,
  matching `occurrence_statistics.media_count: 0` and
  `total_occurrences: 0`.
- The final `mappings/ingredient_mappings.sssom.tsv` rows include the required
  `skos:narrowMatch` to `CHEBI:5445`, the `skos:exactMatch` registry row for
  `cas:56-82-6`, and the `skos:exactMatch` kg-microbe identity row required
  for a subject mapped through a broader ChEBI parent.
- The exact ChEBI parent label `2,3-dihydroxypropanal` is retained only as a
  `REJECTED_LABEL` in YAML and is not emitted in any final SSSOM `other`
  column for this subject.
- The `CARBON_SOURCE` role is supported only by a
  `COMPUTATIONAL_PREDICTION` evidence object whose curator note calls the ChEBI
  ancestry inference provisional and recommends review.

## Completeness

- The hidden/ignored-inclusive exact-identifier search over active `data`,
  `mappings`, `docs`, `scripts`, and `tests` found no second primary record for
  `cas:56-82-6`; references to `CHEBI:5445` outside this mapped record are
  repair-script, test, and generated/review context.
- The parent/child identity loss is represented by `NARROW_MATCH` plus
  companion local identity rows.
- The record has no source occurrences, component decomposition, or
  environmental contexts to resolve.

## Recommended Edits

- In `data/ingredients/mapped/DL-glyceraldehyde.yaml`, remove the provisional
  `CARBON_SOURCE` role or replace its `COMPUTATIONAL_PREDICTION` evidence with
  inspected claim-level evidence for this supplied form.
- Regenerate synchronized curated and SSSOM products, then rerun
  `uv run --frozen python scripts/validate_strict.py`,
  `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/DL-glyceraldehyde.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`,
  `uv run --frozen python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`,
  and `uv run --frozen python scripts/validate_sssom_invariants.py`.
