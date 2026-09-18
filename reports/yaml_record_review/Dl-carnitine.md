# `data/ingredients/mapped/Dl-carnitine.yaml`

## Verdict

Pass. The CultureMech identity exact-matches active `CHEBI:17126` carnitine by
the known `D,L-carnitine` synonym, its CAS RN and structure resolve to the same
non-isomeric PubChem compound, and the final SSSOM row publishes only true
synonyms for the DL-carnitine subject.

## Identity

- Reviewed record: `data/ingredients/mapped/Dl-carnitine.yaml`.
- Identifier and grounding: `identifier: CHEBI:17126` with
  `ontology_mapping.ontology_id: CHEBI:17126`, source `CHEBI`,
  `mapping_quality: SYNONYM_MATCH`, `mapping_status: MAPPED`,
  `ingredient_type: SINGLE_INGREDIENT`, and 2 CultureMech source occurrences.
- Local OAK resolves `CHEBI:17126` to active `carnitine`, formula `C7H15NO3`,
  the expected InChI and SMILES, and related synonym `D,L-carnitine`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Dl-alanine.yaml data/ingredients/mapped/Dl-alpha-lipoic_Acid.yaml data/ingredients/mapped/Dl-aspartic_Acid.yaml data/ingredients/mapped/Dl-carnitine.yaml data/ingredients/mapped/Dl-dithiothreitol.yaml`:
  exited 0 for the 5-file batch.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Dl-alanine.yaml data/ingredients/mapped/Dl-alpha-lipoic_Acid.yaml data/ingredients/mapped/Dl-aspartic_Acid.yaml data/ingredients/mapped/Dl-carnitine.yaml data/ingredients/mapped/Dl-dithiothreitol.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  exited 0 for all 5 records.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:16494 CHEBI:22660 CHEBI:17126 CHEBI:18320 CHEBI:42106 CHEBI:30314 CHEBI:43796`:
  returned the canonical ChEBI label, definition, synonyms, formula, InChI,
  SMILES, charge, and mass for `CHEBI:17126`.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.
- `uv run --frozen python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`:
  passed; all id-label pairs corresponded, with only full-corpus plausibility
  warnings.

## Evidence

- `data/curated/mapped_ingredients.yaml` contains the same maintained record
  body as the per-record YAML.
- PubChem resolves CAS `406-76-8` to CID 288 with formula `C7H15NO3` and the
  same InChIKey as the record.
- A hidden/ignored-inclusive exact search over `data/ingredients` for
  `CHEBI:17126` and `406-76-8` found this active DL-carnitine record plus the
  expected L-carnitine and carnitine-hydrochloride records that use
  `CHEBI:17126` as earlier or parent grounding.
- `mappings/ingredient_mappings_row_review_manifest.tsv` records the
  `CHEBI:17126` synonym enrichment row as already represented.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:Dl-carnitine` to `CHEBI:17126` with `skos:exactMatch`, canonical object
  label `carnitine`, CHEBI object source, the DL-carnitine synonym, and
  `CAS:406-76-8`.

## Completeness

- CAS RN, formula, InChI, SMILES, kg-microbe synonymy, ChEBI synonymy, and
  CultureMech occurrence provenance are populated.
- Supplied forms, mixture components, nutritional roles, physicochemical roles,
  biological roles, and environmental contexts are correctly empty.

## Recommended Edits

- None.
