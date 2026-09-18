# `data/ingredients/mapped/Minocycline_Hydrochloride.yaml`

## Verdict

Needs curation. The exact `CHEBI:50697` minocycline hydrochloride identity,
CAS, structure, row-review confirmation, curated IUPAC synonym, and final exact
row pass, but the selective-agent role is only a provisional name-pattern
prediction.

Severity: major.

## Identity

- Reviewed record: `data/ingredients/mapped/Minocycline_Hydrochloride.yaml`.
- Identifier and grounding: `identifier: CHEBI:50697` with
  `ontology_mapping.ontology_id: CHEBI:50697`, label
  `minocycline hydrochloride`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: no direct CultureMech recipe occurrences.
- Chemical identity: CAS `13614-98-7`, formula `H.C23H27N3O7.Cl`, SMILES, and
  InChI.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Minimycin` through `Mitomycin_C`: exited 0 and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record and the two other CHEBI-primary records in the same batch.

## Evidence

- `mappings/ingredient_mappings_oak_ols_review.tsv` and
  `mappings/ingredient_mappings_row_review_manifest.tsv` confirm
  `MIM:Minocycline_Hydrochloride` to `CHEBI:50697`.
- A fresh EBI OLS4 lookup resolves `CHEBI:50697` as active
  `minocycline hydrochloride` with the record's IUPAC label as an exact
  synonym.
- The final SSSOM publishes one `skos:exactMatch` row from
  `MIM:Minocycline_Hydrochloride` to `CHEBI:50697`.

## Completeness

- The active CHEBI target, salt-specific formula, SMILES, InChI, CAS RN,
  IUPAC synonym, and final exact row agree.
- `SELECTIVE_AGENT` has only `COMPUTATIONAL_PREDICTION` evidence from a curated
  media-role name pattern with a provisional curator note.

## Recommended Edits

- Major: add source-backed evidence that minocycline hydrochloride is used as a
  selective agent in media, or remove the provisional `SELECTIVE_AGENT` role.
