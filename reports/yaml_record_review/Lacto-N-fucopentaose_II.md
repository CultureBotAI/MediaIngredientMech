# `data/ingredients/mapped/Lacto-N-fucopentaose_II.yaml`

## Verdict

Needs curation. The CAS-backed CHEBI:89932 identity, CAS RN, structure, empty
synonym payload, and final SSSOM row pass, but the carbon-source role is still
a provisional CHEBI-ancestry inference.

## Identity

- Reviewed record: `data/ingredients/mapped/Lacto-N-fucopentaose_II.yaml`.
- Identifier and grounding: `identifier: CHEBI:89932` with
  `ontology_mapping.ontology_id: CHEBI:89932`, label
  `Lacto-N-fucopentaose-2`, source `CHEBI`, `mapping_quality: CAS_RN_LOOKUP`,
  `mapping_status: MAPPED`, and `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS RN `21973-23-9`, molecular formula `C32H55NO25`,
  InChI, and SMILES.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Lacto-N-fucopentaose_II` through `Lactone`: exited 0 and wrote zero ERROR
  rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Lacto-N-fucopentaose_II.yaml data/ingredients/mapped/Lacto-N-neotetraose.yaml data/ingredients/mapped/Lactone.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  exited 0 for the three CHEBI-primary records.

## Evidence

- EBI OLS4 resolves `CHEBI:89932` as active `Lacto-N-fucopentaose-2`, lists
  CAS `21973-23-9`, and lists `Lacto-N-fucopentaose II` as a related synonym.
- PubChem resolves CAS RN `21973-23-9` to CID `168012` with formula
  `C32H55NO25` and the same InChI as the YAML record.
- The final SSSOM publishes one `skos:exactMatch` row to `CHEBI:89932`; its
  `other` field contains only `CAS:21973-23-9`.
- Major: `nutritional_roles.CARBON_SOURCE` is backed only by
  `COMPUTATIONAL_PREDICTION` evidence from CHEBI ancestry through
  `CHEBI:16646` and says review is recommended. The carbohydrate ancestry is
  enough to propose the role, but the record still lacks inspected
  medium-level evidence that exact Lacto-N-fucopentaose II was supplied as a
  carbon source.
- The hidden and ignored-inclusive search over `mappings/ingredient_mappings.sssom.tsv`,
  `data`, `src`, `tests`, `reports`, and `docs` found the current final SSSOM
  row and Lacto-N-fucopentaose I/III sibling records, confirming this record
  denotes the II isomer specifically.

## Completeness

- The active CHEBI identity, CAS RN, formula, structure block, aggregate copy,
  and final SSSOM row are present and consistent.
- The provisional carbon-source role needs curation before it can be treated as
  a supported role assertion.

## Recommended Edits

- Major: either replace `nutritional_roles.CARBON_SOURCE` in
  `data/ingredients/mapped/Lacto-N-fucopentaose_II.yaml` with inspected source
  evidence for exact Lacto-N-fucopentaose II use, or remove the provisional
  role.
- Sync the aggregate copy and regenerate derived products after the YAML
  changes; rerun strict, term, round-trip, component, and SSSOM validation.
