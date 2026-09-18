# `data/ingredients/mapped/Methyl_Beta-D-glucopyranoside.yaml`

## Verdict

Pass. The exact `CHEBI:320055` beta-D-glucopyranoside identity, CAS value,
ChEBI/PubChem structure, and final SSSOM row pass.

## Identity

- Reviewed record:
  `data/ingredients/mapped/Methyl_Beta-D-glucopyranoside.yaml`.
- Identifier and grounding: `identifier: CHEBI:320055` with
  `ontology_mapping.ontology_id: CHEBI:320055`, label
  `methyl beta-D-glucopyranoside`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: zero CultureMech recipe occurrences.
- Chemical identity: CAS `709-50-2`, formula `C7H14O6`, SMILES, and InChI for
  methyl beta-D-glucopyranoside.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Methyl_Beta-D-glucopyranoside` through `Methyl_Jasmonate`: exited 0 and
  wrote zero ERROR rows.
- `uv run linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.

## Evidence

- EBI OLS4 resolves `CHEBI:320055` as active
  `methyl beta-D-glucopyranoside` with CAS `709-50-2`, formula `C7H14O6`, and
  the same SMILES and InChI carried in the YAML.
- PubChem resolves CAS `709-50-2` to CID 445238 with the same formula and InChI
  carried in the YAML.
- The OAK/OLS row-review manifest confirmed this row with no curation action.
- The final SSSOM publishes one `skos:exactMatch` row from
  `MIM:Methyl_Beta-D-glucopyranoside` to `CHEBI:320055` with only
  `CAS:709-50-2` in `other`.

## Completeness

- The record does not publish unsupported roles or non-exact synonyms.
- `find` found no local `compounds_to_cas.csv`, and an
  `rg --no-ignore --hidden --glob '!.git'` search for the label and CAS under
  this checkout found only curated records, generated products, backups, and
  row-review reports; ignored files were included.

## Recommended Edits

- None.
