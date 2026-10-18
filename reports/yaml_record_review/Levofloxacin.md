# `data/ingredients/mapped/Levofloxacin.yaml`

## Verdict

Needs curation. The CultureBotHT CHEBI:63598 identity, CAS RN, PubChem
structure, exact synonym, and final SSSOM row pass, but
`physicochemical_roles.SELECTIVE_AGENT` is still an unsupported provisional
name-pattern inference.

## Identity

- Reviewed record: `data/ingredients/mapped/Levofloxacin.yaml`.
- Identifier and grounding: `identifier: CHEBI:63598` with
  `ontology_mapping.ontology_id: CHEBI:63598`, label `levofloxacin`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS RN `100986-85-4`, molecular formula `C18H20FN3O4`,
  InChI, and SMILES.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Leupeptin` through `Levomenthol`: exited 0 and wrote zero ERROR rows.
- `uv run --frozen linkml-term-validator validate-data ... -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`
  exited 0 for all five CHEBI-primary records.

## Evidence

- EBI OLS4 resolves `CHEBI:63598` as active `levofloxacin`, lists the long
  IUPAC synonym carried by the YAML record, lists CAS `100986-85-4`, and records
  the same formula, InChI, and SMILES.
- PubChem resolves CAS RN `100986-85-4` to CID `149096` with formula
  `C18H20FN3O4` and the same InChI as the YAML record.
- The final SSSOM publishes one `skos:exactMatch` row to `CHEBI:63598`; its
  `other` field contains only the curated ChEBI synonym and `CAS:100986-85-4`.
- Major: `physicochemical_roles.SELECTIVE_AGENT` is backed only by
  `COMPUTATIONAL_PREDICTION` evidence from a curated media-role name pattern and
  says review is recommended. The CultureBotHT mapping evidence records that
  the ingredient came from FEBA/Hans80 antibiotic panels, but the role facet
  itself still lacks inspected evidence that exact levofloxacin was used as a
  selective agent in a medium.

## Completeness

- The active CHEBI identity, CAS RN, formula, structure block, aggregate copy,
  and final SSSOM row are present and consistent.
- The provisional selective-agent role needs curation before it can be treated
  as a supported role assertion.

## Recommended Edits

- Major: either replace `physicochemical_roles.SELECTIVE_AGENT` in
  `data/ingredients/mapped/Levofloxacin.yaml` with inspected source evidence for
  exact levofloxacin use as a selective agent, or remove the provisional role.
- Sync the aggregate copy and regenerate derived products after the YAML
  change; rerun strict, term, round-trip, component, and SSSOM validation.
