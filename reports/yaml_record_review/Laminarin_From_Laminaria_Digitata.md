# `data/ingredients/mapped/Laminarin_From_Laminaria_Digitata.yaml`

## Verdict

Needs curation. The CAS-backed CHEBI:6364 laminarin identity, variable polymer
formula, empty synonym payload, and final SSSOM row pass, but the carbon-source
role is still a provisional CHEBI-ancestry inference.

## Identity

- Reviewed record:
  `data/ingredients/mapped/Laminarin_From_Laminaria_Digitata.yaml`.
- Identifier and grounding: `identifier: CHEBI:6364` with
  `ontology_mapping.ontology_id: CHEBI:6364`, label `laminarin`, source
  `CHEBI`, `mapping_quality: CAS_RN_LOOKUP`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS RN `9008-22-4` and generalized molecular formula
  `C12H22O11(C6H10O5)n`.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Lactose` through `Lanthanum_Iii_Chloride`: exited 0 and wrote zero ERROR
  rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Lactose.yaml data/ingredients/mapped/Lactulose.yaml data/ingredients/mapped/Laminaribiose.yaml data/ingredients/mapped/Laminarin_From_Laminaria_Digitata.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  exited 0 for the four CHEBI-primary records.

## Evidence

- EBI OLS4 resolves `CHEBI:6364` as active `laminarin`, lists CAS
  `9008-22-4`, and records the same generalized polymer formula as the YAML
  record.
- The final SSSOM publishes one `skos:exactMatch` row to `CHEBI:6364`; its
  `other` field contains only `CAS:9008-22-4`.
- Major: `nutritional_roles.CARBON_SOURCE` is backed only by
  `COMPUTATIONAL_PREDICTION` evidence from CHEBI ancestry through
  `CHEBI:16646` and says review is recommended. The carbohydrate ancestry is
  enough to propose the role, but the record still lacks inspected
  medium-level evidence that exact laminarin was supplied as a carbon source.
- The hidden and ignored-inclusive search over `mappings/ingredient_mappings.sssom.tsv`,
  `data`, `src`, `tests`, `reports`, and `docs` found the current final SSSOM
  row and no sibling MIM record that would split the same laminarin identity.

## Completeness

- The active CHEBI identity, CAS RN, variable formula, aggregate copy, and final
  SSSOM row are present and consistent.
- The empty InChI and SMILES slots are appropriate for a variable
  polysaccharide record.
- The provisional carbon-source role needs curation before it can be treated as
  a supported role assertion.

## Recommended Edits

- Major: either replace `nutritional_roles.CARBON_SOURCE` in
  `data/ingredients/mapped/Laminarin_From_Laminaria_Digitata.yaml` with
  inspected source evidence for exact laminarin use, or remove the provisional
  role.
- Sync the aggregate copy and regenerate derived products after the YAML
  changes; rerun strict, term, round-trip, component, and SSSOM validation.
