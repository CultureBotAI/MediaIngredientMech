# `data/ingredients/mapped/Lactitol.yaml`

## Verdict

Needs curation. The exact CHEBI:75323 identity, CAS RN, PubChem structure,
reviewed synonym, and final SSSOM row pass, but the carbon-source role is still
a provisional CHEBI-ancestry inference.

## Identity

- Reviewed record: `data/ingredients/mapped/Lactitol.yaml`.
- Identifier and grounding: `identifier: CHEBI:75323` with
  `ontology_mapping.ontology_id: CHEBI:75323`, label `lactitol`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS RN `585-86-4`, molecular formula `C12H24O11`,
  InChI, and SMILES.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Lacidipine` through `Lacto-N-fucopentaose_I`: exited 0 and wrote zero ERROR
  rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Lacidipine.yaml data/ingredients/mapped/Lactate.yaml data/ingredients/mapped/Lactitol.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  exited 0 for the three CHEBI-primary records.

## Evidence

- EBI OLS4 resolves `CHEBI:75323` as active `lactitol` and lists CAS
  `585-86-4`.
- PubChem resolves CAS RN `585-86-4` to a lactitol CID with formula
  `C12H24O11` and the same InChI as the YAML record.
- The final SSSOM publishes one `skos:exactMatch` row to `CHEBI:75323`; its
  `other` field contains reviewed exact synonym
  `4-O-beta-D-galactopyranosyl-D-glucitol` plus `CAS:585-86-4`.
- Major: `nutritional_roles.CARBON_SOURCE` is backed only by
  `COMPUTATIONAL_PREDICTION` evidence from CHEBI ancestry through
  `CHEBI:16646` and says review is recommended. The carbohydrate ancestry is
  enough to propose the role, but the record still lacks inspected
  medium-level evidence that exact lactitol was supplied as a carbon source.
- The hidden and ignored-inclusive search over `mappings/ingredient_mappings.sssom.tsv`,
  `data`, `src`, `tests`, `reports`, and `docs` found the current final SSSOM
  row and no sibling MIM record that would split the same lactitol identity.

## Completeness

- The active CHEBI identity, CAS RN, formula, structure block, synonym, and
  final SSSOM row are present and consistent.
- The provisional carbon-source role needs curation before it can be treated as
  a supported role assertion.

## Recommended Edits

- Major: either replace `nutritional_roles.CARBON_SOURCE` in
  `data/ingredients/mapped/Lactitol.yaml` with inspected source evidence for
  exact lactitol use, or remove the provisional role.
- Sync the aggregate copy and regenerate derived products after the YAML
  changes; rerun strict, term, round-trip, component, and SSSOM validation.
