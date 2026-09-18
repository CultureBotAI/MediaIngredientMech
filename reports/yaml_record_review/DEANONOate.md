# `data/ingredients/mapped/DEANONOate.yaml`

## Verdict

Pass. The record preserves a CAS-backed local DEANONOate identity with a
narrower mapping to the ChEBI diethylamine NONOate parent, has the required CAS
and kg-microbe exact identity rows in final SSSOM, and publishes only
same-subject synonyms in `other`.

## Identity

- Reviewed record: `data/ingredients/mapped/DEANONOate.yaml`.
- Identifier and grounding: `identifier: cas:372965-00-9` with
  `ontology_mapping.ontology_id: CHEBI:77707`, source `CHEBI`,
  `mapping_quality: NARROW_MATCH`, and `mapping_status: MAPPED`.
- Local OAK resolves `CHEBI:77707` to active `diethylamine NONOate`, formula
  `C4H11N.C4H11N3O2`, charge `0`, InChI, InChIKey, SMILES, and both curated
  record synonyms as ChEBI exact synonyms.
- PubChem resolves `372965-00-9` to `DEA NONOate` records with formula
  `C8H22N4O2`, matching the two-component ChEBI formula for the salt.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/DEANONOate.yaml data/ingredients/mapped/DETANO.yaml data/ingredients/mapped/DL-2-Aminoadipic_Acid.yaml data/ingredients/mapped/DL-2-Aminobutyric_Acid.yaml data/ingredients/mapped/DL-3-Aminoisobutyric_Acid.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/DEANONOate.yaml data/ingredients/mapped/DETANO.yaml data/ingredients/mapped/DL-2-Aminoadipic_Acid.yaml data/ingredients/mapped/DL-2-Aminobutyric_Acid.yaml data/ingredients/mapped/DL-3-Aminoisobutyric_Acid.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for all 5 files.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:77707 CHEBI:50154 CHEBI:37023 CHEBI:35621 CHEBI:27389`:
  returned formula, charge, InChI, InChIKey, SMILES, mass, synonyms, and xrefs
  for `CHEBI:77707`.
- `curl -L ... q=DEANONOate&ontology=chebi&exact=true`: live OLS returned
  zero exact ChEBI hits for the compact source label.
- `curl -L ... /compound/name/372965-00-9/property/.../JSON`: PubChem resolved
  the CAS value to DEA NONOate records.
- `uv run --frozen python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`:
  passed; all id-label pairs corresponded, with full-corpus plausibility
  warnings only.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- `mappings/culturemech_recipe_membership.tsv` has no rows for
  `cas:372965-00-9`, matching `occurrence_statistics.media_count: 0` and
  `total_occurrences: 0`.
- The final `mappings/ingredient_mappings.sssom.tsv` rows include the required
  `skos:narrowMatch` to `CHEBI:77707`, the `skos:exactMatch` registry row for
  `cas:372965-00-9`, and the `skos:exactMatch` kg-microbe identity row
  required for a subject mapped through a broader ChEBI parent.
- The two unstructured tokens on the final ChEBI parent row,
  `1,1-diethyl-2-hydroxy-3-oxotriazane--N-ethylethanamine (1/1)` and
  `N-ethylethanaminium 1,1-diethyl-3-oxotriazan-2-olate`, are same-subject
  ChEBI exact synonyms for `CHEBI:77707`.
- The final registry and kg-microbe identity rows publish only the structured
  same-subject token `CAS:372965-00-9` in `other`.

## Completeness

- The hidden/ignored-inclusive exact-identifier search over active `data`,
  `mappings`, `docs`, `scripts`, and `tests` found no second primary record for
  `cas:372965-00-9`; the CAS appears in this record, synchronized/generated
  projections, registry review surfaces, and the final SSSOM identity rows.
- The parent/child identity loss is represented by `NARROW_MATCH` plus
  companion local identity rows.
- The record has no source occurrences, nutritional roles, component
  decomposition, or environmental contexts to resolve.

## Recommended Edits

- None.
