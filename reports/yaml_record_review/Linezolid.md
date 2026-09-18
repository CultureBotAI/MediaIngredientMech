# `data/ingredients/mapped/Linezolid.yaml`

## Verdict

Needs curation. The CultureBotHT exact CHEBI:63607 identity, CAS RN, PubChem
structure, exact synonym, and final SSSOM row pass, but
`physicochemical_roles.SELECTIVE_AGENT` is still an unsupported provisional
name-pattern inference.

## Identity

- Reviewed record: `data/ingredients/mapped/Linezolid.yaml`.
- Identifier and grounding: `identifier: CHEBI:63607` with
  `ontology_mapping.ontology_id: CHEBI:63607`, label `linezolid`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS RN `165800-03-3`, molecular formula `C16H20FN3O4`,
  InChI, and SMILES.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Lincomycin_Hydrochloride` through `Lithocholic_Acid`: exited 0 and wrote
  zero ERROR rows.
- `uv run --frozen linkml-term-validator validate-data` exited 0 for all five
  CHEBI-grounded records in the batch.

## Evidence

- EBI OLS4 resolves `CHEBI:63607` as active `linezolid`, lists CAS
  `165800-03-3`, and records the same formula, InChI, SMILES, and IUPAC synonym
  as the YAML record.
- PubChem resolves CAS RN `165800-03-3` to CID `441401` with formula
  `C16H20FN3O4` and the same InChI as the YAML record.
- The final SSSOM publishes one `skos:exactMatch` row to `CHEBI:63607`; its
  `other` field contains only the curated ChEBI synonym and `CAS:165800-03-3`.
- Major: `physicochemical_roles.SELECTIVE_AGENT` is backed only by
  `COMPUTATIONAL_PREDICTION` evidence from a curated media-role name pattern and
  says review is recommended. The record needs inspected medium-level evidence
  that exact linezolid was used as a selective agent before retaining that role.

## Completeness

- The active CHEBI identity, CAS RN, formula, structure block, aggregate copy,
  and final SSSOM row are present and consistent.
- The provisional selective-agent role needs curation before it can be treated
  as a supported role assertion.

## Recommended Edits

- Major: either replace `physicochemical_roles.SELECTIVE_AGENT` in
  `data/ingredients/mapped/Linezolid.yaml` with inspected source evidence for
  exact linezolid use as a selective agent, or remove the provisional role.
- Sync the aggregate copy and regenerate derived products after the YAML
  change; rerun strict, term, round-trip, component, and SSSOM validation.
