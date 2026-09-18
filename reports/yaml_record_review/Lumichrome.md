# `data/ingredients/mapped/Lumichrome.yaml`

## Verdict

Pass. The CultureBotHT exact CHEBI:17781 identity, CAS RN, PubChem structure,
exact synonym, and final SSSOM row are internally consistent.

## Identity

- Reviewed record: `data/ingredients/mapped/Lumichrome.yaml`.
- Identifier and grounding: `identifier: CHEBI:17781` with
  `ontology_mapping.ontology_id: CHEBI:17781`, label `lumichrome`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS RN `1086-80-2`, molecular formula `C12H10N4O2`,
  InChI, and SMILES.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Lovastatin` through `Lupeol`: exited 0 and wrote zero ERROR rows.
- `uv run --frozen linkml-term-validator validate-data` exited 0 for all five
  records in the batch.

## Evidence

- EBI OLS4 resolves `CHEBI:17781` as active `lumichrome`, lists
  `7,8-dimethylbenzo[g]pteridine-2,4(1H,3H)-dione` as a synonym, lists CAS
  `1086-80-2`, and records the same formula, InChI, and SMILES as the YAML
  record.
- PubChem resolves CAS RN `1086-80-2` to CID `5326566` with formula
  `C12H10N4O2` and the same InChI as the YAML record.
- The final SSSOM publishes one `skos:exactMatch` row to `CHEBI:17781`; its
  `other` field contains only the curated ChEBI synonym and `CAS:1086-80-2`.

## Completeness

- The active CHEBI identity, CAS RN, formula, structure block, aggregate copy,
  and final SSSOM row are present and consistent.
- No nutritional, physicochemical, cellular, or environmental role is asserted.

## Recommended Edits

- None.
