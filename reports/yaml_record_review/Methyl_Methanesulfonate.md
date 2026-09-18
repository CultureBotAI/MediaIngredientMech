# `data/ingredients/mapped/Methyl_Methanesulfonate.yaml`

## Verdict

Pass. The exact `CHEBI:25255` identity, CAS value, ChEBI/PubChem structure, and
final SSSOM row pass.

## Identity

- Reviewed record: `data/ingredients/mapped/Methyl_Methanesulfonate.yaml`.
- Identifier and grounding: `identifier: CHEBI:25255` with
  `ontology_mapping.ontology_id: CHEBI:25255`, label
  `methyl methanesulfonate`, source `CHEBI`, `mapping_quality: EXACT_MATCH`,
  `mapping_status: MAPPED`, and `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: zero CultureMech recipe occurrences.
- Chemical identity: CAS `66-27-3`, formula `C2H6O3S`, SMILES, and InChI for
  methyl methanesulfonate.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Methyl_Methanesulfonate` through `Methylcobalamin`: exited 0 and wrote zero
  ERROR rows.
- `uv run linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.

## Evidence

- EBI OLS4 resolves `CHEBI:25255` as active `methyl methanesulfonate` with CAS
  `66-27-3`, formula `C2H6O3S`, and the same SMILES and InChI carried in the
  YAML.
- PubChem resolves CAS `66-27-3` to CID 4156 with the same formula and InChI
  carried in the YAML.
- The OAK/OLS row-review manifest confirmed this row with no curation action.
- The final SSSOM publishes one `skos:exactMatch` row from
  `MIM:Methyl_Methanesulfonate` to `CHEBI:25255` with only `CAS:66-27-3` in
  `other`.

## Completeness

- The record does not publish unsupported roles or non-exact synonyms.
- `find` found no local `compounds_to_cas.csv`, and an
  `rg --no-ignore --hidden --glob '!.git'` search for the label and CAS under
  this checkout found only curated records, generated products, backups, and
  row-review reports; ignored files were included.

## Recommended Edits

- None.
