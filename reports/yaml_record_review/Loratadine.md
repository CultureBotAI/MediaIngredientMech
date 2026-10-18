# `data/ingredients/mapped/Loratadine.yaml`

## Verdict

Pass. The CultureBotHT exact CHEBI:6538 identity, CAS RN, PubChem structure,
exact synonym, and final SSSOM row are internally consistent.

## Identity

- Reviewed record: `data/ingredients/mapped/Loratadine.yaml`.
- Identifier and grounding: `identifier: CHEBI:6538` with
  `ontology_mapping.ontology_id: CHEBI:6538`, label `loratadine`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS RN `79794-75-5`, molecular formula `C22H23ClN2O2`,
  InChI, and SMILES.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Locust_Bean_Gum` through `Loratadine`: exited 0 and wrote zero ERROR rows.
- `uv run --frozen linkml-term-validator validate-data` exited 0 for all five
  records in the batch.

## Evidence

- EBI OLS4 resolves `CHEBI:6538` as active `loratadine`, lists the long IUPAC
  synonym carried by the YAML record, lists CAS `79794-75-5`, and records the
  same formula, InChI, and SMILES as the YAML record.
- PubChem resolves CAS RN `79794-75-5` to CID `3957` with formula
  `C22H23ClN2O2` and the same InChI as the YAML record.
- The final SSSOM publishes one `skos:exactMatch` row to `CHEBI:6538`; its
  `other` field contains only the curated ChEBI synonym and `CAS:79794-75-5`.

## Completeness

- The active CHEBI identity, CAS RN, formula, structure block, aggregate copy,
  and final SSSOM row are present and consistent.
- No nutritional, physicochemical, cellular, or environmental role is asserted.

## Recommended Edits

- None.
