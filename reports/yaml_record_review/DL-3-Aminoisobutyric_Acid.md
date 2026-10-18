# `data/ingredients/mapped/DL-3-Aminoisobutyric_Acid.yaml`

## Verdict

Needs curation. The September stereochemical repair correctly preserved the DL
racemate as a CAS-backed local identity with a narrow mapping to
`CHEBI:27389`, the final SSSOM parent row no longer emits a broader
same-formula synonym, and the CAS and kg-microbe exact identity rows are
present, but the amino-acid-source role is still only a provisional
computational assertion.

## Identity

- Reviewed record: `data/ingredients/mapped/DL-3-Aminoisobutyric_Acid.yaml`.
- Identifier and grounding: `identifier: cas:144-90-1` with
  `ontology_mapping.ontology_id: CHEBI:27389`, source `CHEBI`,
  `mapping_quality: NARROW_MATCH`, and `mapping_status: MAPPED`.
- Local OAK resolves `CHEBI:27389` to active `3-aminoisobutyric acid`, formula
  `C4H9NO2`, charge `0`, non-isomeric InChI, SMILES, CAS xref `144-90-1`,
  and exact synonym `3-amino-2-methylpropanoic acid`.
- PubChem resolves `144-90-1` to `Beta-Aminoisobutyric Acid`, formula
  `C4H9NO2`, and the same non-isomeric InChIKey as the local ChEBI parent.
- Live OLS exact search for `DL-3-Aminoisobutyric acid` returned zero ChEBI
  hits, supporting the current CAS identity plus parent mapping rather than an
  exact ChEBI promotion.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/DEANONOate.yaml data/ingredients/mapped/DETANO.yaml data/ingredients/mapped/DL-2-Aminoadipic_Acid.yaml data/ingredients/mapped/DL-2-Aminobutyric_Acid.yaml data/ingredients/mapped/DL-3-Aminoisobutyric_Acid.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/DEANONOate.yaml data/ingredients/mapped/DETANO.yaml data/ingredients/mapped/DL-2-Aminoadipic_Acid.yaml data/ingredients/mapped/DL-2-Aminobutyric_Acid.yaml data/ingredients/mapped/DL-3-Aminoisobutyric_Acid.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for all 5 files.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:77707 CHEBI:50154 CHEBI:37023 CHEBI:35621 CHEBI:27389`:
  returned formula, charge, InChI, InChIKey, SMILES, mass, synonyms, and xrefs
  for `CHEBI:27389`.
- `curl -L ... q=DL-3-Aminoisobutyric%20acid&ontology=chebi&exact=true`:
  live OLS returned zero ChEBI hits.
- `curl -L ... /compound/name/144-90-1/property/.../JSON`: PubChem resolved
  the CAS value to `Beta-Aminoisobutyric Acid`.
- `uv run --frozen python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`:
  passed; all id-label pairs corresponded, with full-corpus plausibility
  warnings only.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- `mappings/culturemech_recipe_membership.tsv` has no rows for `cas:144-90-1`,
  matching `occurrence_statistics.media_count: 0` and
  `total_occurrences: 0`.
- The final `mappings/ingredient_mappings.sssom.tsv` rows include the required
  `skos:narrowMatch` to `CHEBI:27389`, the `skos:exactMatch` registry row for
  `cas:144-90-1`, and the `skos:exactMatch` kg-microbe identity row required
  for a subject mapped through a broader ChEBI parent.
- The exact ChEBI parent label `3-amino-2-methylpropanoic acid` is retained
  only as a `REJECTED_LABEL` in YAML and is not emitted in any final SSSOM
  `other` column for this subject.
- The `AMINO_ACID_SOURCE` role is supported only by a
  `COMPUTATIONAL_PREDICTION` evidence object whose curator note calls the ChEBI
  ancestry inference provisional and recommends review.

## Completeness

- The hidden/ignored-inclusive exact-identifier search over active `data`,
  `mappings`, `docs`, `scripts`, and `tests` found no second primary record for
  `cas:144-90-1`.
- The parent/child identity loss is represented by `NARROW_MATCH` plus
  companion local identity rows.
- The record has no source occurrences, component decomposition, or
  environmental contexts to resolve.

## Recommended Edits

- In `data/ingredients/mapped/DL-3-Aminoisobutyric_Acid.yaml`, remove the
  provisional `AMINO_ACID_SOURCE` role or replace its
  `COMPUTATIONAL_PREDICTION` evidence with inspected claim-level evidence for
  this supplied form.
- Regenerate synchronized curated and SSSOM products, then rerun
  `uv run --frozen python scripts/validate_strict.py`,
  `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/DL-3-Aminoisobutyric_Acid.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`,
  `uv run --frozen python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`,
  and `uv run --frozen python scripts/validate_sssom_invariants.py`.
