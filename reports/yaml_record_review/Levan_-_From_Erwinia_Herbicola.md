# `data/ingredients/mapped/Levan_-_From_Erwinia_Herbicola.yaml`

## Verdict

Needs curation. The CAS-backed CHEBI:16703 polymer identity, ChEBI CAS xref,
structure block, exact synonym, and final SSSOM row pass, but
`nutritional_roles.CARBON_SOURCE` is still a provisional CHEBI-ancestry
inference.

## Identity

- Reviewed record: `data/ingredients/mapped/Levan_-_From_Erwinia_Herbicola.yaml`.
- Identifier and grounding: `identifier: CHEBI:16703` with
  `ontology_mapping.ontology_id: CHEBI:16703`, label
  `(2->6)-beta-D-fructan`, source `CHEBI`, `mapping_quality: EXACT_MATCH`,
  `mapping_status: MAPPED`, and `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS RN `9013-95-0`, generalized molecular formula
  `(C6H10O5)n.C12H22O11`, InChI, and SMILES.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Leupeptin` through `Levomenthol`: exited 0 and wrote zero ERROR rows.
- `uv run --frozen linkml-term-validator validate-data ... -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`
  exited 0 for all five CHEBI-primary records.

## Evidence

- EBI OLS4 resolves `CHEBI:16703` as active `(2->6)-beta-D-fructan`, lists
  `Levan` and `(2->6)-beta-D-fructofuranan` as synonyms, lists CAS
  `9013-95-0`, and records the same generalized formula, InChI, and SMILES as
  the YAML record.
- PubChem lookup by CAS RN `9013-95-0` found no CID, so the inspected structure
  source for this variable polymer is ChEBI rather than PubChem.
- The final SSSOM publishes one `skos:exactMatch` row to `CHEBI:16703`; its
  `other` field contains only the ChEBI exact synonym
  `(2->6)-beta-D-fructofuranan` and `CAS:9013-95-0`.
- Major: `nutritional_roles.CARBON_SOURCE` is backed only by
  `COMPUTATIONAL_PREDICTION` evidence from CHEBI ancestry through
  `CHEBI:16646` and says review is recommended. The carbohydrate ancestry is
  enough to propose the role, but the record still lacks inspected
  medium-level evidence that exact levan was supplied as a carbon source.

## Completeness

- The active CHEBI identity, CAS RN, generalized formula, structure block,
  aggregate copy, and final SSSOM row are present and consistent.
- The provisional carbon-source role needs curation before it can be treated as
  a supported role assertion.

## Recommended Edits

- Major: either replace `nutritional_roles.CARBON_SOURCE` in
  `data/ingredients/mapped/Levan_-_From_Erwinia_Herbicola.yaml` with inspected
  source evidence for exact levan use, or remove the provisional role.
- Sync the aggregate copy and regenerate derived products after the YAML
  change; rerun strict, term, round-trip, component, and SSSOM validation.
