# `data/ingredients/mapped/Minocycline.yaml`

## Verdict

Pass. The exact `CHEBI:50694` minocycline identity, MicrobeDecoder review,
structural fields, occurrence import, and final SSSOM row pass.

## Identity

- Reviewed record: `data/ingredients/mapped/Minocycline.yaml`.
- Identifier and grounding: `identifier: CHEBI:50694` with
  `ontology_mapping.ontology_id: CHEBI:50694`, label `minocycline`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 60 imported MicrobeDecoder BacDive antibiotic/metabolite
  occurrences.
- Chemical identity: formula `C23H27N3O7`, SMILES, InChI, and molecular
  weight from the ChEBI/PubChem backfill.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Minimycin` through `Mitomycin_C`: exited 0 and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record and the two other CHEBI-primary records in the same batch.

## Evidence

- `mappings/microbedecoder_auto_mapped_review.tsv` approved this mapping after
  the local OAK adapter resolved `CHEBI:50694` and its canonical label
  case-insensitively exact-matched `minocycline`.
- A fresh EBI OLS4 lookup resolves `CHEBI:50694` as active `minocycline` and
  distinguishes the base from `CHEBI:50697` minocycline hydrochloride and
  minocycline ionization-state classes.
- The final SSSOM publishes one `skos:exactMatch` row from `MIM:Minocycline`
  to `CHEBI:50694` with empty `other`.

## Completeness

- The identifier, CHEBI label, MicrobeDecoder provenance, structure, type, and
  final SSSOM row agree.
- The record does not publish raw synonyms or unsupported roles.

## Recommended Edits

- None.
