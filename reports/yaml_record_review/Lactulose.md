# `data/ingredients/mapped/Lactulose.yaml`

## Verdict

Needs curation. The exact CHEBI:6359 identity, CAS RN, PubChem structure,
reviewed synonym, and final SSSOM row pass, but the carbon-source role is still
a provisional CHEBI-ancestry inference.

## Identity

- Reviewed record: `data/ingredients/mapped/Lactulose.yaml`.
- Identifier and grounding: `identifier: CHEBI:6359` with
  `ontology_mapping.ontology_id: CHEBI:6359`, label `lactulose`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS RN `4618-18-2`, molecular formula `C12H22O11`,
  InChI, and SMILES.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Lactose` through `Lanthanum_Iii_Chloride`: exited 0 and wrote zero ERROR
  rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Lactose.yaml data/ingredients/mapped/Lactulose.yaml data/ingredients/mapped/Laminaribiose.yaml data/ingredients/mapped/Laminarin_From_Laminaria_Digitata.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  exited 0 for the four CHEBI-primary records.

## Evidence

- EBI OLS4 resolves `CHEBI:6359` as active `lactulose`, lists CAS
  `4618-18-2`, and lists the same InChI as the YAML record.
- PubChem resolves CAS RN `4618-18-2` to CID `11333` with formula `C12H22O11`
  and the same InChI as the YAML record.
- The final SSSOM publishes one `skos:exactMatch` row to `CHEBI:6359`; its
  `other` field contains reviewed exact synonym
  `4-O-beta-D-galactopyranosyl-beta-D-fructofuranose` plus `CAS:4618-18-2`.
- Major: `nutritional_roles.CARBON_SOURCE` is backed only by
  `COMPUTATIONAL_PREDICTION` evidence from CHEBI ancestry through
  `CHEBI:16646` and says review is recommended. The carbohydrate ancestry is
  enough to propose the role, but the record still lacks inspected
  medium-level evidence that exact lactulose was supplied as a carbon source.
- The hidden and ignored-inclusive search over `mappings/ingredient_mappings.sssom.tsv`,
  `data`, `src`, `tests`, `reports`, and `docs` found the current final SSSOM
  row and no sibling MIM record that would split the same lactulose identity.

## Completeness

- The active CHEBI identity, CAS RN, formula, structure block, synonym, and
  final SSSOM row are present and consistent.
- The provisional carbon-source role needs curation before it can be treated as
  a supported role assertion.

## Recommended Edits

- Major: either replace `nutritional_roles.CARBON_SOURCE` in
  `data/ingredients/mapped/Lactulose.yaml` with inspected source evidence for
  exact lactulose use, or remove the provisional role.
- Sync the aggregate copy and regenerate derived products after the YAML
  changes; rerun strict, term, round-trip, component, and SSSOM validation.
