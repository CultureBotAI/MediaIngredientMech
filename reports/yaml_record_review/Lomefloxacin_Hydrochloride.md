# `data/ingredients/mapped/Lomefloxacin_Hydrochloride.yaml`

## Verdict

Needs curation. The CultureBotHT exact CHEBI:6518 identity, CAS RN, PubChem
structure, exact synonym, and final SSSOM row pass, but
`physicochemical_roles.SELECTIVE_AGENT` is still an unsupported provisional
name-pattern inference.

## Identity

- Reviewed record: `data/ingredients/mapped/Lomefloxacin_Hydrochloride.yaml`.
- Identifier and grounding: `identifier: CHEBI:6518` with
  `ontology_mapping.ontology_id: CHEBI:6518`, label `lomefloxacin
  hydrochloride`, source `CHEBI`, `mapping_quality: EXACT_MATCH`,
  `mapping_status: MAPPED`, and `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS RN `98079-52-8`, molecular formula
  `C17H19F2N3O3.HCl`, InChI, and SMILES.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Locust_Bean_Gum` through `Loratadine`: exited 0 and wrote zero ERROR rows.
- `uv run --frozen linkml-term-validator validate-data` exited 0 for all five
  records in the batch.

## Evidence

- EBI OLS4 resolves `CHEBI:6518` as active `lomefloxacin hydrochloride`, lists
  CAS `98079-52-8`, and records the same formula, InChI, SMILES, and IUPAC
  synonym as the YAML record.
- PubChem resolves CAS RN `98079-52-8` to CID `68624` with the same InChI as
  the YAML record.
- The final SSSOM publishes one `skos:exactMatch` row to `CHEBI:6518`; its
  `other` field contains only the curated ChEBI synonym and `CAS:98079-52-8`.
- Major: `physicochemical_roles.SELECTIVE_AGENT` is backed only by
  `COMPUTATIONAL_PREDICTION` evidence from a curated media-role name pattern and
  says review is recommended. The CultureBotHT mapping evidence records FEBA
  stress-panel provenance, but the role facet itself still lacks inspected
  evidence that exact lomefloxacin hydrochloride was used as a selective agent
  in a medium.

## Completeness

- The active CHEBI identity, CAS RN, formula, structure block, aggregate copy,
  and final SSSOM row are present and consistent.
- The provisional selective-agent role needs curation before it can be treated
  as a supported role assertion.

## Recommended Edits

- Major: either replace `physicochemical_roles.SELECTIVE_AGENT` in
  `data/ingredients/mapped/Lomefloxacin_Hydrochloride.yaml` with inspected
  source evidence for exact lomefloxacin hydrochloride use as a selective agent,
  or remove the provisional role.
- Sync the aggregate copy and regenerate derived products after the YAML
  change; rerun strict, term, round-trip, component, and SSSOM validation.
