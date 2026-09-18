# `data/ingredients/mapped/DL-Glyceraldehyde_3-phosphate.yaml`

## Verdict

Pass. The September stereochemical repair correctly preserved the DL racemate
as a CAS-backed local identity with a narrow mapping to `CHEBI:17138`, the final
SSSOM parent row no longer emits a broader same-formula synonym, and the CAS
and kg-microbe exact identity rows are present.

## Identity

- Reviewed record: `data/ingredients/mapped/DL-Glyceraldehyde_3-phosphate.yaml`.
- Identifier and grounding: `identifier: cas:591-59-3` with
  `ontology_mapping.ontology_id: CHEBI:17138`, source `CHEBI`,
  `mapping_quality: NARROW_MATCH`, and `mapping_status: MAPPED`.
- Local OAK resolves `CHEBI:17138` to active `glyceraldehyde 3-phosphate`,
  formula `C3H7O6P`, charge `0`, non-isomeric InChI, SMILES, CAS xref
  `591-59-3`, and exact synonym
  `2-hydroxy-3-oxopropyl dihydrogen phosphate`.
- PubChem resolves `591-59-3` to `3-Phosphoglyceraldehyde`, formula
  `C3H7O6P`, and the same non-isomeric InChIKey as the local ChEBI parent.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/DL-3-Hydroxyisobutyric_Acid_Sodium_Salt.yaml data/ingredients/mapped/DL-Glyceraldehyde_3-phosphate.yaml data/ingredients/mapped/DL-Glycerol_1-phosphate_Sodium_Salt_Hydrate.yaml data/ingredients/mapped/DL-Histidine_Monohydrochloride_Monohydrate.yaml data/ingredients/mapped/DL-Isocitric_Acid_Trisodium_Salt_Hydrate.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/DL-3-Hydroxyisobutyric_Acid_Sodium_Salt.yaml data/ingredients/mapped/DL-Glyceraldehyde_3-phosphate.yaml data/ingredients/mapped/DL-Glycerol_1-phosphate_Sodium_Salt_Hydrate.yaml data/ingredients/mapped/DL-Histidine_Monohydrochloride_Monohydrate.yaml data/ingredients/mapped/DL-Isocitric_Acid_Trisodium_Salt_Hydrate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for all 5 files.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:18064 CHEBI:17138 CHEBI:14336 CHEBI:172950`:
  returned formula, charge, InChI, InChIKey, SMILES, mass, synonyms, and xrefs
  for `CHEBI:17138`.
- `curl -L ... /compound/name/591-59-3/property/.../JSON`: PubChem resolved
  the CAS value to CID 729, `3-Phosphoglyceraldehyde`.
- `uv run --frozen python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`:
  passed; all id-label pairs corresponded, with full-corpus plausibility
  warnings only.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- `mappings/culturemech_recipe_membership.tsv` has no rows for `cas:591-59-3`,
  matching `occurrence_statistics.media_count: 0` and
  `total_occurrences: 0`.
- The final `mappings/ingredient_mappings.sssom.tsv` rows include the required
  `skos:narrowMatch` to `CHEBI:17138`, the `skos:exactMatch` registry row for
  `cas:591-59-3`, and the `skos:exactMatch` kg-microbe identity row required
  for a subject mapped through a broader ChEBI parent.
- The exact ChEBI parent label
  `2-hydroxy-3-oxopropyl dihydrogen phosphate` is retained only as a
  `REJECTED_LABEL` in YAML and is not emitted in any final SSSOM `other`
  column for this subject.
- The record does not assert nutritional roles, environmental contexts, or
  mixture components, so there are no unsupported claim-specific evidence
  objects to resolve.

## Completeness

- The hidden/ignored-inclusive exact-identifier search over active `data`,
  `mappings`, `docs`, `scripts`, and `tests` found no second primary record for
  `cas:591-59-3`; references to `CHEBI:17138` outside this mapped record are
  repair-script, test, and generated/review context.
- The parent/child identity loss is represented by `NARROW_MATCH` plus
  companion local identity rows.
- The aggregate copy in `data/curated/mapped_ingredients.yaml` and the
  per-record YAML agree.

## Recommended Edits

- None.
