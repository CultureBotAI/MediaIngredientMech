# `data/ingredients/mapped/Methyl_Beta-D-xylopyranoside.yaml`

## Verdict

Pass. The exact `CHEBI:74863` beta-D-xylopyranoside identity,
MicrobeDecoder source occurrence, ChEBI structure, and final SSSOM row pass.

## Identity

- Reviewed record: `data/ingredients/mapped/Methyl_Beta-D-xylopyranoside.yaml`.
- Identifier and grounding: `identifier: CHEBI:74863` with
  `ontology_mapping.ontology_id: CHEBI:74863`, label
  `methyl beta-D-xylopyranoside`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: thirteen MicrobeDecoder `BacDive_Metabolite_utilization`
  occurrences and zero CultureMech recipe occurrences.
- Chemical identity: formula `C6H12O5`, SMILES, InChI, and mass copied from
  ChEBI/PubChem.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Methyl_Beta-D-glucopyranoside` through `Methyl_Jasmonate`: exited 0 and
  wrote zero ERROR rows.
- `uv run linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.

## Evidence

- EBI OLS4 resolves `CHEBI:74863` as active
  `methyl beta-D-xylopyranoside` with formula `C6H12O5`, the same SMILES and
  InChI carried in the YAML, and CAS `612-05-5`.
- The active MicrobeDecoder source table carries
  `kgmicrobe.trait:methyl_beta_d_xylopyranoside` as
  `methyl beta-D-xylopyranoside` with count 13 in
  `BacDive_Metabolite_utilization`.
- The final SSSOM publishes one `skos:exactMatch` row from
  `MIM:Methyl_Beta-D-xylopyranoside` to `CHEBI:74863` with empty `other`.

## Completeness

- The record does not publish unsupported roles or non-exact synonyms.
- The separate CAS-primary `Methyl-beta-D-xylopyranoside.yaml` record now
  duplicates this exact identity and owns the merge/promote cleanup; this record
  already carries the specific CHEBI identity.

## Recommended Edits

- None to this record.
