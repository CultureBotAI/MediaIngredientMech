# `data/ingredients/mapped/Methyl_3-_4-hydroxyphenylpropionate.yaml`

## Verdict

Pass. The exact `CHEBI:176565` identity, CAS value, ChEBI structure, curated
synonyms, and final SSSOM row pass.

## Identity

- Reviewed record:
  `data/ingredients/mapped/Methyl_3-_4-hydroxyphenylpropionate.yaml`.
- Identifier and grounding: `identifier: CHEBI:176565` with
  `ontology_mapping.ontology_id: CHEBI:176565`, label
  `methyl 3-(4-hydroxyphenyl)propionate`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: zero CultureMech recipe occurrences.
- Chemical identity: CAS `5597-50-2`, formula `C10H12O3`, SMILES, and InChI
  for methyl 3-(4-hydroxyphenyl)propionate.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Methyl_(R)-lactate` through `Methyl_Alpha-D-mannoside`: exited 0 and wrote
  zero ERROR rows.
- `uv run linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.

## Evidence

- EBI OLS4 resolves `CHEBI:176565` as active
  `methyl 3-(4-hydroxyphenyl)propionate` with formula `C10H12O3`, the same
  SMILES and InChI carried in the YAML, CAS `5597-50-2`, and
  `methyl 3-(4-hydroxyphenyl)propanoate` as a synonym.
- PubChem resolves CAS `5597-50-2` to CID 79706 with the same formula and InChI
  carried in the YAML.
- PubMed PMID `27217493` uses `MHPP` as the abbreviation for methyl
  3-(4-hydroxyphenyl)propionate, supporting the CultureBotHT-derived `MHPP`
  synonym.
- The final SSSOM publishes one `skos:exactMatch` row from
  `MIM:Methyl_3-_4-hydroxyphenylpropionate` to `CHEBI:176565`; its `other`
  column contains the same-subject `MHPP`, ChEBI synonym, and `CAS:5597-50-2`
  tokens.

## Completeness

- The record does not publish unsupported roles or non-exact synonyms.
- `find` found no local `compounds_to_cas.csv`, and an
  `rg --no-ignore --hidden --glob '!.git'` search for the label and CAS under
  this checkout found only curated records, generated products, backups, and
  row-review reports; ignored files were included.

## Recommended Edits

- None.
