# `data/ingredients/mapped/Methyl_6-Hydroxyangolensate.yaml`

## Verdict

Pass. The exact `CHEBI:181871` identity, ChEBI structure, IUPAC synonym, and
final SSSOM row pass.

## Identity

- Reviewed record: `data/ingredients/mapped/Methyl_6-Hydroxyangolensate.yaml`.
- Identifier and grounding: `identifier: CHEBI:181871` with
  `ontology_mapping.ontology_id: CHEBI:181871`, label
  `Methyl 6-hydroxyangolensate`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: zero CultureMech recipe occurrences.
- Chemical identity: formula `C27H34O8`, SMILES, and InChI for methyl
  6-hydroxyangolensate.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Methyl_(R)-lactate` through `Methyl_Alpha-D-mannoside`: exited 0 and wrote
  zero ERROR rows.
- `uv run linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.

## Evidence

- EBI OLS4 resolves `CHEBI:181871` as active
  `Methyl 6-hydroxyangolensate` with formula `C27H34O8`, the same SMILES and
  InChI carried in the YAML, and the long IUPAC synonym curated in the record.
- The OAK/OLS row-review manifest confirmed this row with no curation action.
- The final SSSOM publishes one `skos:exactMatch` row from
  `MIM:Methyl_6-Hydroxyangolensate` to `CHEBI:181871` with the long IUPAC
  synonym as the only `other` token.

## Completeness

- The record does not publish unsupported roles or non-exact synonyms.
- `find` found no local `compounds_to_cas.csv`, and an
  `rg --no-ignore --hidden --glob '!.git'` search for the label under this
  checkout found only curated records, generated products, backups, and
  row-review reports; ignored files were included.

## Recommended Edits

- None.
