# `data/ingredients/mapped/Miharamycin_A.yaml`

## Verdict

Needs curation. The exact `CHEBI:216282` miharamycin A identity, CHEBI IUPAC
synonym, row-review confirmation, structural fields, and final exact row pass,
but final SSSOM `other` still exports process text and the selective-agent role
is only a provisional name-pattern prediction.

Severity: major.

## Identity

- Reviewed record: `data/ingredients/mapped/Miharamycin_A.yaml`.
- Identifier and grounding: `identifier: CHEBI:216282` with
  `ontology_mapping.ontology_id: CHEBI:216282`, label `Miharamycin A`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: no direct CultureMech recipe occurrences.
- Chemical identity: formula `C20H30N10O9`, SMILES, and InChI from the CHEBI
  sqlite backfill.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Midecamycin` through `Mineral_3B_Solution_Minus_Nitrogen`: exited 0 and
  wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record and `Midecamycin`.

## Evidence

- `mappings/ingredient_mappings_oak_ols_review.tsv` and
  `mappings/ingredient_mappings_row_review_manifest.tsv` confirm
  `MIM:Miharamycin_A` to `CHEBI:216282`.
- A fresh EBI OLS4 lookup resolves `CHEBI:216282` as active `Miharamycin A`
  with the long IUPAC label as an exact synonym, distinct from sibling
  `Miharamycin B`.
- The final SSSOM publishes one `skos:exactMatch` row from
  `MIM:Miharamycin_A` to `CHEBI:216282`.

## Completeness

- The active CHEBI target, formula, SMILES, InChI, IUPAC synonym, and final
  exact row agree.
- The final SSSOM `other` field still exports `produces: miharamycin A`, which
  is process text rather than a synonym for the ingredient.
- `SELECTIVE_AGENT` has only `COMPUTATIONAL_PREDICTION` evidence from a curated
  media-role name pattern with a provisional curator note.

## Recommended Edits

- Major: mark `produces: miharamycin A` as `REJECTED_LABEL`, or otherwise
  filter it from final SSSOM `other` for
  `data/ingredients/mapped/Miharamycin_A.yaml`.
- Major: add source-backed evidence that miharamycin A is used as a selective
  agent in media, or remove the provisional `SELECTIVE_AGENT` role.
