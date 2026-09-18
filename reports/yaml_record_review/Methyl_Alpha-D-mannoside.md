# `data/ingredients/mapped/Methyl_Alpha-D-mannoside.yaml`

## Verdict

Pass. The exact `CHEBI:43943` alpha-D-mannoside identity, MicrobeDecoder source
occurrence, ChEBI structure, and final SSSOM row pass.

## Identity

- Reviewed record: `data/ingredients/mapped/Methyl_Alpha-D-mannoside.yaml`.
- Identifier and grounding: `identifier: CHEBI:43943` with
  `ontology_mapping.ontology_id: CHEBI:43943`, label
  `methyl alpha-D-mannoside`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: five MicrobeDecoder `BacDive_Metabolite_utilization`
  occurrences and zero CultureMech recipe occurrences.
- Chemical identity: formula `C7H14O6`, SMILES, InChI, and mass copied from
  ChEBI/PubChem.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Methyl_(R)-lactate` through `Methyl_Alpha-D-mannoside`: exited 0 and wrote
  zero ERROR rows.
- `uv run linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.

## Evidence

- EBI OLS4 resolves `CHEBI:43943` as active `methyl alpha-D-mannoside` with
  formula `C7H14O6` and the same SMILES and InChI carried in the YAML.
- The active MicrobeDecoder source table carries
  `kgmicrobe.trait:methyl_alpha_d_mannoside` as `methyl alpha-D-mannoside`
  with count 5 in `BacDive_Metabolite_utilization`.
- The final SSSOM publishes one `skos:exactMatch` row from
  `MIM:Methyl_Alpha-D-mannoside` to `CHEBI:43943` with empty `other`.

## Completeness

- The record does not publish unsupported roles or non-exact synonyms.

## Recommended Edits

- None.
