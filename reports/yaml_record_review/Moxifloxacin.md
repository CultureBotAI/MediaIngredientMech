# `data/ingredients/mapped/Moxifloxacin.yaml`

## Verdict

Needs curation. The exact `CHEBI:63611` moxifloxacin identity, CultureBotHT CAS
provenance, structure, ChEBI synonym, and final exact row pass, but the
selective-agent role is only a provisional name-pattern prediction.

Severity: major.

## Identity

- Reviewed record: `data/ingredients/mapped/Moxifloxacin.yaml`.
- Identifier and grounding: `identifier: CHEBI:63611` with
  `ontology_mapping.ontology_id: CHEBI:63611`, label `moxifloxacin`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: no direct CultureMech recipe occurrences.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Monomethyl_Succinate` through `Moxifloxacin`: exited 0 and wrote zero ERROR
  rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.

## Evidence

- A fresh EBI OLS4 lookup resolves `CHEBI:63611` as active `moxifloxacin` and
  exposes the stored IUPAC name as an exact synonym.
- A fresh PubChem lookup for CAS `151096-09-2` returns formula `C21H24FN3O4`
  and the same InChI stored on the record.
- The final SSSOM publishes one `skos:exactMatch` row from `MIM:Moxifloxacin`
  to `CHEBI:63611` with the ChEBI IUPAC synonym and `CAS:151096-09-2` in
  `other`.

## Completeness

- The active ChEBI target, CAS RN, structure, synonym, and final row agree.
- `SELECTIVE_AGENT` has only `COMPUTATIONAL_PREDICTION` evidence from a curated
  media-role name pattern with a provisional curator note.

## Recommended Edits

- Major: add source-backed evidence that moxifloxacin is used as a selective
  agent in media, or remove the provisional `SELECTIVE_AGENT` role.
