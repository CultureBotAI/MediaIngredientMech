# `data/ingredients/mapped/Methyl_Alpha-D-glucopyranoside.yaml`

## Verdict

Pass. The exact `CHEBI:320061` identity, CAS value, ChEBI/PubChem structure,
and final SSSOM row pass.

## Identity

- Reviewed record:
  `data/ingredients/mapped/Methyl_Alpha-D-glucopyranoside.yaml`.
- Identifier and grounding: `identifier: CHEBI:320061` with
  `ontology_mapping.ontology_id: CHEBI:320061`, label
  `methyl alpha-D-glucopyranoside`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: zero CultureMech recipe occurrences.
- Chemical identity: CAS `97-30-3`, formula `C7H14O6`, SMILES, and InChI for
  methyl alpha-D-glucopyranoside.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Methyl_(R)-lactate` through `Methyl_Alpha-D-mannoside`: exited 0 and wrote
  zero ERROR rows.
- `uv run linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.

## Evidence

- EBI OLS4 resolves `CHEBI:320061` as active
  `methyl alpha-D-glucopyranoside` with formula `C7H14O6`, the same SMILES and
  InChI carried in the YAML, and CAS `97-30-3`.
- PubChem resolves CAS `97-30-3` to CID 64947 with the same formula and InChI
  carried in the YAML.
- The OAK/OLS row-review manifest confirmed this row with no curation action.
- The final SSSOM publishes one `skos:exactMatch` row from
  `MIM:Methyl_Alpha-D-glucopyranoside` to `CHEBI:320061` with only
  `CAS:97-30-3` in `other`.

## Completeness

- The record does not publish unsupported roles or non-exact synonyms.
- `find` found no local `compounds_to_cas.csv`, and an
  `rg --no-ignore --hidden --glob '!.git'` search for the CAS under this
  checkout found only curated records, generated products, and backups; ignored
  files were included.

## Recommended Edits

- None.
