# `data/ingredients/mapped/Lentilan_From_Mushroom.yaml`

## Verdict

Needs curation. The CAS-backed CHEBI:31770 identity, variable polymer formula,
ChEBI SMILES, and final SSSOM row pass, but the carbon-source role is still a
provisional CHEBI-ancestry inference and the preferred term likely misspells
`Lentinan` as `Lentilan`.

## Identity

- Reviewed record: `data/ingredients/mapped/Lentilan_From_Mushroom.yaml`.
- Identifier and grounding: `identifier: CHEBI:31770` with
  `ontology_mapping.ontology_id: CHEBI:31770`, label `lentinan`, source
  `CHEBI`, `mapping_quality: CAS_RN_LOOKUP`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS RN `37339-90-5`, generalized molecular formula
  `(C42H70O35)n`, and SMILES.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Lecithin` through `Leucodin`: exited 0 and wrote zero ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Lecithin.yaml data/ingredients/mapped/Lentilan_From_Mushroom.yaml data/ingredients/mapped/Leucodin.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  exited 0 for the three CHEBI-primary records.

## Evidence

- EBI OLS4 resolves `CHEBI:31770` as active `lentinan`, lists CAS
  `37339-90-5`, records the same generalized polymer formula and SMILES as the
  YAML record, and has the same mushroom-origin scope.
- PubChem lookup by CAS RN `37339-90-5` found no CID, so the ChEBI structure is
  the inspected structure source for this polymer.
- The final SSSOM publishes one `skos:exactMatch` row to `CHEBI:31770`; its
  `other` field contains only `CAS:37339-90-5`.
- Major: `nutritional_roles.CARBON_SOURCE` is backed only by
  `COMPUTATIONAL_PREDICTION` evidence from CHEBI ancestry through
  `CHEBI:16646` and says review is recommended. The carbohydrate ancestry is
  enough to propose the role, but the record still lacks inspected
  medium-level evidence that exact lentinan was supplied as a carbon source.
- Minor: the preferred term and filename spell the ChEBI identity as `Lentilan`.
  The ChEBI label, ChEBI synonym, and the CAS-backed curation history all use
  `lentinan`, so the record appears to carry a typo from the source label.
- The hidden and ignored-inclusive search over `mappings/ingredient_mappings.sssom.tsv`,
  `data`, `src`, `tests`, `reports`, and `docs` found the current final SSSOM
  row and no sibling MIM record that would split the same lentinan identity.

## Completeness

- The active CHEBI identity, CAS RN, variable formula, ChEBI SMILES, aggregate
  copy, and final SSSOM row are present and consistent.
- The provisional carbon-source role needs curation before it can be treated as
  a supported role assertion.

## Recommended Edits

- Major: either replace `nutritional_roles.CARBON_SOURCE` in
  `data/ingredients/mapped/Lentilan_From_Mushroom.yaml` with inspected source
  evidence for exact lentinan use, or remove the provisional role.
- Minor: correct the preferred label and source path spelling from `Lentilan` to
  `Lentinan`, preserving the source spelling as rejected or raw provenance only
  if it is needed.
- Sync the aggregate copy and regenerate derived products after the YAML
  changes; rerun strict, term, round-trip, component, and SSSOM validation.
