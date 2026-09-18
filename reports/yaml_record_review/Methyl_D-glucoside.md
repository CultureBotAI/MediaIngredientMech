# `data/ingredients/mapped/Methyl_D-glucoside.yaml`

## Verdict

Pass. The exact generic-anomer `CHEBI:37657` methyl D-glucoside identity,
MicrobeDecoder source occurrence, ChEBI structure, and final SSSOM row pass.

## Identity

- Reviewed record: `data/ingredients/mapped/Methyl_D-glucoside.yaml`.
- Identifier and grounding: `identifier: CHEBI:37657` with
  `ontology_mapping.ontology_id: CHEBI:37657`, label `methyl D-glucoside`,
  source `CHEBI`, `mapping_quality: EXACT_MATCH`,
  `mapping_status: MAPPED`, and `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: twenty-six MicrobeDecoder `BacDive_Metabolite_utilization`
  occurrences and zero CultureMech recipe occurrences.
- Chemical identity: formula `C7H14O6`, SMILES, InChI with an unspecified
  anomeric center, and mass copied from ChEBI/PubChem.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Methyl_Beta-D-glucopyranoside` through `Methyl_Jasmonate`: exited 0 and
  wrote zero ERROR rows.
- `uv run linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.

## Evidence

- EBI OLS4 resolves `CHEBI:37657` as active `methyl D-glucoside` with formula
  `C7H14O6`, the same generic-anomer SMILES and InChI carried in the YAML, and
  CAS `3149-68-6`.
- The active MicrobeDecoder source table carries
  `kgmicrobe.trait:methyl_d_glucoside` as `methyl D-glucoside` with count 26 in
  `BacDive_Metabolite_utilization`.
- The final SSSOM publishes one `skos:exactMatch` row from
  `MIM:Methyl_D-glucoside` to `CHEBI:37657` with empty `other`.

## Completeness

- The record does not publish unsupported roles or non-exact synonyms.

## Recommended Edits

- None.
