# `data/ingredients/mapped/Methyl_(R)-lactate.yaml`

## Verdict

Pass. The exact `CHEBI:74611` R-lactate ester identity, MicrobeDecoder source
occurrence, absorbed raw synonym, chemical structure, and final SSSOM row pass.

## Identity

- Reviewed record: `data/ingredients/mapped/Methyl_(R)-lactate.yaml`.
- Identifier and grounding: `identifier: CHEBI:74611` with
  `ontology_mapping.ontology_id: CHEBI:74611`, label `methyl (R)-lactate`,
  source `CHEBI`, `mapping_quality: EXACT_MATCH`,
  `mapping_status: MAPPED`, and `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: three MicrobeDecoder `BacDive_Metabolite_utilization`
  occurrences and zero CultureMech recipe occurrences.
- Chemical identity: formula `C4H8O3`, SMILES, InChI, and mass copied from
  ChEBI/PubChem.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Methyl_(R)-lactate` through `Methyl_Alpha-D-mannoside`: exited 0 and wrote
  zero ERROR rows.
- `uv run linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.

## Evidence

- EBI OLS4 resolves `CHEBI:74611` as active `methyl (R)-lactate` with formula
  `C4H8O3`, the same SMILES and InChI carried in the YAML, and CAS
  `17392-83-5`.
- The active MicrobeDecoder source table carries
  `kgmicrobe.trait:methyl_r_lactate` as `methyl (R)-lactate` with count 3 in
  `BacDive_Metabolite_utilization`.
- The absorbed raw label `D-lactic Acid Methyl Ester` is the same ester:
  OLS4 lists the casefold-equivalent `D-lactic acid methyl ester` as a
  synonym of `CHEBI:74611`.
- The final SSSOM publishes one `skos:exactMatch` row from
  `MIM:Methyl_~28R~29-lactate` to `CHEBI:74611` with only the absorbed
  MicrobeDecoder raw label in `other`.

## Completeness

- The record does not publish unsupported roles or non-exact synonyms.

## Recommended Edits

- None.
