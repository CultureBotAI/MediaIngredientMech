# `data/ingredients/mapped/Methyl_Jasmonate.yaml`

## Verdict

Pass. The CAS-to-CHEBI `(-)-methyl jasmonate` identity, structure,
CAS_RN_LOOKUP grade, IUPAC synonym, and final SSSOM row pass.

## Identity

- Reviewed record: `data/ingredients/mapped/Methyl_Jasmonate.yaml`.
- Identifier and grounding: `identifier: CHEBI:15929` with
  `ontology_mapping.ontology_id: CHEBI:15929`, label `(-)-methyl jasmonate`,
  source `CHEBI`, `mapping_quality: CAS_RN_LOOKUP`,
  `mapping_status: MAPPED`, and `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: zero CultureMech recipe occurrences.
- Chemical identity: CAS `1211-29-6`, formula `C13H20O3`, SMILES, and InChI
  for `(-)-methyl jasmonate`.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Methyl_Beta-D-glucopyranoside` through `Methyl_Jasmonate`: exited 0 and
  wrote zero ERROR rows.
- `uv run linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.

## Evidence

- EBI OLS4 resolves `CHEBI:15929` as active `(-)-methyl jasmonate` with CAS
  `1211-29-6`, formula `C13H20O3`, the same SMILES and InChI carried in the
  YAML, `Methyl jasmonate` as a synonym, and the curated IUPAC synonym.
- PubChem resolves CAS `1211-29-6` to CID 5281929 with the same formula and
  InChI carried in the YAML.
- The OAK/OLS row-review manifest confirmed the `CHEBI:15929` row with no
  curation action, and the #317/#438 regrade retained the CAS lookup provenance
  without changing the identity.
- The final SSSOM publishes one `skos:exactMatch` row from
  `MIM:Methyl_Jasmonate` to `CHEBI:15929`; its `other` column contains the
  curated IUPAC synonym and `CAS:1211-29-6`.

## Completeness

- The record does not publish unsupported roles or non-exact synonyms.
- `find` found no local `compounds_to_cas.csv`, and an
  `rg --no-ignore --hidden --glob '!.git'` search for the label and CAS under
  this checkout found only curated records, generated products, backups, and
  row-review reports; ignored files were included.

## Recommended Edits

- None.
