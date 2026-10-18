# `data/ingredients/mapped/Menaquinone.yaml`

## Verdict

Pass. The exact generic ChEBI identity, structure, MicrobeDecoder occurrence,
and final SSSOM row all pass.

## Identity

- Reviewed record: `data/ingredients/mapped/Menaquinone.yaml`.
- Identifier and grounding: `identifier: CHEBI:16374` with
  `ontology_mapping.ontology_id: CHEBI:16374`, label `menaquinone`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: one MicrobeDecoder `BacDive_Antibiotic_sensitivity` occurrence
  and zero CultureMech recipe occurrences.
- Chemical identity: formula `(C5H8)n.C11H8O2`, InChI, and SMILES copied from
  ChEBI/PubChem.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Melibiose` through `Menaquinone`: exited 0 and wrote zero ERROR rows.
- `uv run --frozen linkml-term-validator validate-data` exited 0 for this
  CHEBI-primary record.

## Evidence

- EBI OLS4 resolves `CHEBI:16374` as active `menaquinone` with CAS
  `11032-49-8`, formula `(C5H8)n.C11H8O2`, and the same InChI and SMILES
  carried in the YAML.
- The final SSSOM publishes one `skos:exactMatch` row from `MIM:Menaquinone` to
  `CHEBI:16374` with empty `other`.

## Completeness

- The record does not publish unsupported roles or non-exact synonyms.

## Recommended Edits

- None.
