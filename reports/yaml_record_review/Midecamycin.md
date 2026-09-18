# `data/ingredients/mapped/Midecamycin.yaml`

## Verdict

Pass. The exact `CHEBI:31845` midecamycin identity, MicrobeDecoder review,
structural fields, occurrence import, and final SSSOM row pass.

## Identity

- Reviewed record: `data/ingredients/mapped/Midecamycin.yaml`.
- Identifier and grounding: `identifier: CHEBI:31845` with
  `ontology_mapping.ontology_id: CHEBI:31845`, label `Midecamycin`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 11 imported MicrobeDecoder BacDive antibiotic occurrences.
- Chemical identity: formula `C41H67NO15`, SMILES, InChI, and molecular
  weight from the ChEBI/PubChem backfill.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Midecamycin` through `Mineral_3B_Solution_Minus_Nitrogen`: exited 0 and
  wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record and `Miharamycin_A`.

## Evidence

- `mappings/microbedecoder_auto_mapped_review.tsv` approved this mapping after
  the local OAK adapter resolved `CHEBI:31845` and its canonical label
  case-insensitively exact-matched `Midecamycin`.
- A fresh EBI OLS4 lookup resolves `CHEBI:31845` as active `Midecamycin` and
  distinguishes derivative or sibling terms such as midecamycin acetate,
  midecamycin cation, and miocamycin.
- The final SSSOM publishes one `skos:exactMatch` row from `MIM:Midecamycin`
  to `CHEBI:31845` with empty `other`.

## Completeness

- The identifier, CHEBI label, MicrobeDecoder provenance, structure, type, and
  final SSSOM row agree.
- The record does not publish raw synonyms or unsupported roles.

## Recommended Edits

- None.
