# `data/ingredients/mapped/Lacidipine.yaml`

## Verdict

Pass. The exact CHEBI:135737 identity, CAS RN, PubChem structure, empty synonym
payload, and final SSSOM row are internally consistent.

## Identity

- Reviewed record: `data/ingredients/mapped/Lacidipine.yaml`.
- Identifier and grounding: `identifier: CHEBI:135737` with
  `ontology_mapping.ontology_id: CHEBI:135737`, label `lacidipine`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS RN `103890-78-4`, molecular formula `C26H33NO6`,
  InChI, and SMILES.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Lacidipine` through `Lacto-N-fucopentaose_I`: exited 0 and wrote zero ERROR
  rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Lacidipine.yaml data/ingredients/mapped/Lactate.yaml data/ingredients/mapped/Lactitol.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  exited 0 for the three CHEBI-primary records. The MICRO and MeSH/CAS records
  were outside this CHEBI-focused term-validation subset.

## Evidence

- EBI OLS4 resolves `CHEBI:135737` as active `lacidipine`.
- PubChem resolves CAS RN `103890-78-4` to a lacidipine CID with formula
  `C26H33NO6` and the same InChI as the YAML record.
- The final SSSOM publishes one `skos:exactMatch` row to `CHEBI:135737`; its
  `other` field contains only `CAS:103890-78-4`.
- The hidden and ignored-inclusive search over `mappings/ingredient_mappings.sssom.tsv`,
  `data`, `src`, `tests`, `reports`, and `docs` found the current final SSSOM
  row and no sibling MIM record that would split the same lacidipine identity.

## Completeness

- The active CHEBI identity, CAS RN, formula, structure block, and final SSSOM
  row are present and consistent.
- The record has no occurrence rows or synonyms, and the empty slots are
  appropriate for this CultureBotHT-only molecule.

## Recommended Edits

- None.
