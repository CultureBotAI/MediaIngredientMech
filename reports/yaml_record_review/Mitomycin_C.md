# `data/ingredients/mapped/Mitomycin_C.yaml`

## Verdict

Needs curation. The exact `CHEBI:27504` mitomycin C identity, CAS, structure,
row-review confirmation, curated IUPAC synonym, and final exact row pass, but
the selective-agent role is only a provisional name-pattern prediction.

Severity: major.

## Identity

- Reviewed record: `data/ingredients/mapped/Mitomycin_C.yaml`.
- Identifier and grounding: `identifier: CHEBI:27504` with
  `ontology_mapping.ontology_id: CHEBI:27504`, label `mitomycin C`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: no direct CultureMech recipe occurrences.
- Chemical identity: CAS `50-07-7`, formula `C15H18N4O5`, SMILES, and InChI.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Minimycin` through `Mitomycin_C`: exited 0 and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record and the two other CHEBI-primary records in the same batch.

## Evidence

- `mappings/ingredient_mappings_oak_ols_review.tsv` and
  `mappings/ingredient_mappings_row_review_manifest.tsv` confirm
  `MIM:Mitomycin_C` to `CHEBI:27504`.
- A fresh EBI OLS4 lookup resolves `CHEBI:27504` as active `mitomycin C` with
  the record's IUPAC label as an exact synonym.
- The final SSSOM publishes one `skos:exactMatch` row from `MIM:Mitomycin_C`
  to `CHEBI:27504`.

## Completeness

- The active CHEBI target, formula, SMILES, InChI, CAS RN, IUPAC synonym, and
  final exact row agree.
- `SELECTIVE_AGENT` has only `COMPUTATIONAL_PREDICTION` evidence from a curated
  media-role name pattern with a provisional curator note.

## Recommended Edits

- Major: add source-backed evidence that mitomycin C is used as a selective
  agent in media, or remove the provisional `SELECTIVE_AGENT` role.
