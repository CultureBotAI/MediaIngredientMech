# `data/ingredients/mapped/Dl-histidine.yaml`

## Verdict

Needs curation. The CultureMech identity exact-matches active `CHEBI:27570`
histidine by synonym, its CAS RN and structure match ChEBI and PubChem, and the
final SSSOM row is clean; the `AMINO_ACID_SOURCE` role is still only a
provisional ChEBI-ancestry inference.

## Identity

- Reviewed record: `data/ingredients/mapped/Dl-histidine.yaml`.
- Identifier and grounding: `identifier: CHEBI:27570` with
  `ontology_mapping.ontology_id: CHEBI:27570`, source `CHEBI`,
  `mapping_quality: SYNONYM_MATCH`, `mapping_status: MAPPED`,
  `ingredient_type: SINGLE_INGREDIENT`, and 3 CultureMech source occurrences.
- Local OAK resolves `CHEBI:27570` to active `histidine`, formula `C6H9N3O2`,
  the expected InChI and SMILES, CAS xref `4998-57-6`, and `DL-Histidine` as a
  related synonym.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Dl-histidine.yaml data/ingredients/mapped/Dl-malic_Acid.yaml data/ingredients/mapped/Dl-methionine.yaml data/ingredients/mapped/Dl-mevalonic_Acid.yaml data/ingredients/mapped/Dl-tryptophan.yaml`:
  exited 0 for the 5-file batch.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Dl-histidine.yaml data/ingredients/mapped/Dl-malic_Acid.yaml data/ingredients/mapped/Dl-methionine.yaml data/ingredients/mapped/Dl-mevalonic_Acid.yaml data/ingredients/mapped/Dl-tryptophan.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed all 5 records.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:27570 CHEBI:6650 CHEBI:16811 CHEBI:25351 CHEBI:57912`:
  returned the canonical ChEBI label, definition, synonyms, CAS xref,
  formula, InChI, SMILES, charge, and mass for `CHEBI:27570`.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.
- `uv run --frozen python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`:
  passed; all id-label pairs corresponded, with only full-corpus plausibility
  warnings.

## Evidence

- `data/curated/mapped_ingredients.yaml` contains the same maintained record
  body as the per-record YAML.
- PubChem resolves CAS `4998-57-6` to CID 773 with formula `C6H9N3O2` and the
  same InChIKey as the record.
- A hidden/ignored-inclusive exact search over `data/ingredients` and
  `mappings` for `CHEBI:27570` and `4998-57-6` found the active DL-histidine
  record, the expected L-histidine repair history, generated membership rows,
  and final review rows.
- `mappings/ingredient_mappings_row_review_manifest.tsv` records the
  `CHEBI:27570` mapping as confirmed with no row-review action required.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:Dl-histidine` to `CHEBI:27570` with `skos:exactMatch`, canonical object
  label `histidine`, CHEBI object source, true histidine synonyms, and
  `CAS:4998-57-6`.
- Major: `nutritional_roles.AMINO_ACID_SOURCE` has only
  `COMPUTATIONAL_PREDICTION` evidence from the ChEBI `CHEBI:33709` amino acid
  ancestry closure. It is not source-backed.

## Completeness

- CAS RN, formula, InChI, SMILES, kg-microbe synonymy, ChEBI synonymy, and
  CultureMech occurrence provenance are populated.
- Supplied forms, mixture components, physicochemical roles, biological roles,
  and environmental contexts are correctly empty.

## Recommended Edits

- Major: replace the `AMINO_ACID_SOURCE` computational role in
  `data/ingredients/mapped/Dl-histidine.yaml` with source-backed role evidence
  scoped to DL-histidine, or remove the role if no support is available; then
  synchronize `data/curated/mapped_ingredients.yaml`.
