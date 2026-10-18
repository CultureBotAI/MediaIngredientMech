# `data/ingredients/mapped/Dodecandioic_Acid.yaml`

## Verdict

Pass. The CultureBotHT CAS lookup uniquely resolves `693-23-2` to active
`CHEBI:4676` dodecanedioic acid, the formula, InChI, and SMILES match ChEBI and
PubChem, and the final SSSOM row is a clean exact match with the CAS payload in
the expected place.

## Identity

- Reviewed record: `data/ingredients/mapped/Dodecandioic_Acid.yaml`.
- Identifier and grounding: `identifier: CHEBI:4676` with
  `ontology_mapping.ontology_id: CHEBI:4676`, source `CHEBI`,
  `mapping_quality: CAS_RN_LOOKUP`, `mapping_status: MAPPED`,
  `ingredient_type: SINGLE_INGREDIENT`, and 0/0 CultureMech occurrences.
- Local OAK resolves `CHEBI:4676` to active `dodecanedioic acid`, formula
  `C12H22O4`, the expected InChI and SMILES, CAS xref `693-23-2`, and
  dodecanedioic acid synonyms.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Docosane.yaml data/ingredients/mapped/Docosanol.yaml data/ingredients/mapped/Dodecandioic_Acid.yaml data/ingredients/mapped/Dodecane.yaml data/ingredients/mapped/Dodecanoate.yaml`:
  exited 0 for the 5-file batch.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Docosane.yaml data/ingredients/mapped/Docosanol.yaml data/ingredients/mapped/Dodecandioic_Acid.yaml data/ingredients/mapped/Dodecane.yaml data/ingredients/mapped/Dodecanoate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed all 5 records.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:46050 CHEBI:197511 CHEBI:4676 CHEBI:28817 CHEBI:18262`:
  returned the canonical ChEBI label, definition, synonyms, CAS xref,
  formula, InChI, SMILES, charge, and mass for `CHEBI:4676`.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.
- `uv run --frozen python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`:
  passed; all id-label pairs corresponded, with only full-corpus plausibility
  warnings.

## Evidence

- `data/curated/mapped_ingredients.yaml` contains the same maintained record
  body as the per-record YAML.
- PubChem resolves CAS `693-23-2` to CID 12736 with formula `C12H22O4` and the
  same InChIKey as the record.
- The hidden/ignored-inclusive exact search over `data/ingredients` and
  `mappings` for `CHEBI:4676` and `693-23-2` found the active per-record YAML,
  the row-review rows, and the final SSSOM row.
- `mappings/ingredient_mappings_row_review_manifest.tsv` records the
  `CHEBI:4676` synonym enrichment row as already represented.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:Dodecandioic_Acid` to `CHEBI:4676` with `skos:exactMatch`, canonical
  object label `dodecanedioic acid`, CHEBI object source, and `CAS:693-23-2`.

## Completeness

- CAS RN, formula, InChI, SMILES, and CultureBotHT CAS provenance are
  populated.
- The 0/0 occurrence count is acceptable for a CultureBotHT compound with no
  tracked CultureMech recipe memberships.
- Supplied forms, mixture components, nutritional roles, physicochemical roles,
  biological roles, and environmental contexts are correctly empty.

## Recommended Edits

- None.
