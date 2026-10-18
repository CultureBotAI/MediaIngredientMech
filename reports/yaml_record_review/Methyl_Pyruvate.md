# `data/ingredients/mapped/Methyl_Pyruvate.yaml`

## Verdict

Pass. The exact `CHEBI:51850` methyl pyruvate identity, MicrobeDecoder source
occurrence, ChEBI structure, and final SSSOM row pass.

## Identity

- Reviewed record: `data/ingredients/mapped/Methyl_Pyruvate.yaml`.
- Identifier and grounding: `identifier: CHEBI:51850` with
  `ontology_mapping.ontology_id: CHEBI:51850`, label `methyl pyruvate`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: ninety-eight MicrobeDecoder `BacDive_Metabolite_utilization`
  occurrences and zero CultureMech recipe occurrences.
- Chemical identity: formula `C4H6O3`, SMILES, InChI, and mass copied from
  ChEBI/PubChem.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Methyl_Methanesulfonate` through `Methylcobalamin`: exited 0 and wrote zero
  ERROR rows.
- `uv run linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.

## Evidence

- EBI OLS4 resolves `CHEBI:51850` as active `methyl pyruvate` with formula
  `C4H6O3`, the same SMILES and InChI carried in the YAML, and CAS `600-22-6`.
- The active MicrobeDecoder source table carries
  `kgmicrobe.trait:methyl_pyruvate` as `methyl pyruvate` with count 98 in
  `BacDive_Metabolite_utilization`.
- The final SSSOM publishes one `skos:exactMatch` row from
  `MIM:Methyl_Pyruvate` to `CHEBI:51850` with empty `other`.

## Completeness

- The record does not publish unsupported roles or non-exact synonyms.

## Recommended Edits

- None.
