# `data/ingredients/mapped/Lincomycin_Hydrochloride.yaml`

## Verdict

Needs curation. The ChEBI CHEBI:182465 identity, formula, exact synonym, and
final SSSOM row pass, but the CAS RN resolves to conflicting stereochemistry in
PubChem and `physicochemical_roles.SELECTIVE_AGENT` is still a provisional
name-pattern inference.

## Identity

- Reviewed record: `data/ingredients/mapped/Lincomycin_Hydrochloride.yaml`.
- Identifier and grounding: `identifier: CHEBI:182465` with
  `ontology_mapping.ontology_id: CHEBI:182465`, label
  `Lincomycin hydrochloride`, source `CHEBI`, `mapping_quality: EXACT_MATCH`,
  `mapping_status: MAPPED`, and `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS RN `859-18-7`, molecular formula
  `C18H34N2O6S.HCl`, InChI, and SMILES.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Lincomycin_Hydrochloride` through `Lithocholic_Acid`: exited 0 and wrote
  zero ERROR rows.
- `uv run --frozen linkml-term-validator validate-data` exited 0 for all five
  CHEBI-grounded records in the batch.

## Evidence

- EBI OLS4 resolves `CHEBI:182465` as active `Lincomycin hydrochloride`, lists
  CAS `859-18-7`, and records the same formula, InChI, SMILES, and IUPAC
  synonym as the YAML record.
- PubChem resolves CAS RN `859-18-7` to formula `C18H35ClN2O6S`, matching the
  same hydrochloride composition, but the returned InChIKey suffix differs from
  the ChEBI/YAML suffix. A curator should resolve that CAS structure conflict
  before relying on the PubChem registry for this salt.
- The final SSSOM publishes one `skos:exactMatch` row to `CHEBI:182465`; its
  `other` field contains only the curated ChEBI synonym and `CAS:859-18-7`.
- Major: `physicochemical_roles.SELECTIVE_AGENT` is backed only by
  `COMPUTATIONAL_PREDICTION` evidence from a curated media-role name pattern and
  says review is recommended. The CultureBotHT mapping evidence records that
  the ingredient came from FEBA/Hans80 antibiotic panels, but the role facet
  itself still lacks inspected evidence that exact lincomycin hydrochloride was
  used as a selective agent in a medium.

## Completeness

- The active CHEBI identity, formula, structure block, aggregate copy, and final
  SSSOM row are present and internally consistent.
- The CAS/PubChem stereochemistry conflict and provisional selective-agent role
  need curation before the record is fully supported.

## Recommended Edits

- Major: resolve whether CAS RN `859-18-7` should stay on the ChEBI/YAML
  stereochemical form or whether the record's structure needs correction.
- Major: either replace `physicochemical_roles.SELECTIVE_AGENT` with inspected
  source evidence for exact lincomycin hydrochloride use as a selective agent,
  or remove the provisional role.
- Sync the aggregate copy and regenerate derived products after any YAML
  change; rerun strict, term, round-trip, component, and SSSOM validation.
