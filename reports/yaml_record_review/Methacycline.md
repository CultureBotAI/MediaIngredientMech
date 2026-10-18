# `data/ingredients/mapped/Methacycline.yaml`

## Verdict

Pass. The exact ChEBI identity, structure, MicrobeDecoder occurrence, and final
SSSOM row all pass.

## Identity

- Reviewed record: `data/ingredients/mapped/Methacycline.yaml`.
- Identifier and grounding: `identifier: CHEBI:6805` with
  `ontology_mapping.ontology_id: CHEBI:6805`, label `methacycline`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: one MicrobeDecoder `BacDive_Antibiotic_sensitivity` occurrence
  and zero CultureMech recipe occurrences.
- Chemical identity: formula `C22H22N2O8`, InChI, and SMILES copied from
  ChEBI/PubChem.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Meso-Erythritol` through `Methane`: exited 0 and wrote zero ERROR rows.
- `uv run --frozen linkml-term-validator validate-data` exited 0 for this
  CHEBI-primary record.

## Evidence

- EBI OLS4 resolves `CHEBI:6805` as active `methacycline` with CAS `914-00-1`,
  formula `C22H22N2O8`, and the same InChI and SMILES carried in the YAML.
- The final SSSOM publishes one `skos:exactMatch` row from `MIM:Methacycline`
  to `CHEBI:6805` with empty `other`.

## Completeness

- The record does not publish unsupported roles or non-exact synonyms.

## Recommended Edits

- None.
