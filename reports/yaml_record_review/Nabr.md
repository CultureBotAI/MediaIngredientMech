# `data/ingredients/mapped/Nabr.yaml`

## Verdict

Pass. The exact `CHEBI:63004` sodium bromide identity, CAS-backed structure,
occurrence count, `MINERAL_SOURCE` role, ChEBI synonyms, and final exact row
agree.

## Identity

- Reviewed record: `data/ingredients/mapped/Nabr.yaml`.
- Identifier and grounding: `identifier: CHEBI:63004` with
  `ontology_mapping.ontology_id: CHEBI:63004`, label `sodium bromide`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`,
  `mapping_status: MAPPED`, and `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 322 CultureMech recipe occurrences across 322 media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Na3-citrate_X_2_H2o` through `Nabr`: exited 0 and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.

## Evidence

- A fresh EBI OLS4 lookup resolves `CHEBI:63004` as active `sodium bromide` with
  formula `Br.Na`, CAS `7647-15-6`, and the same InChI and SMILES as the record.
- A fresh PubChem CAS lookup for `7647-15-6` resolves to sodium bromide with the
  same formula and InChI, confirming the chemical block.
- The `Bromide salt of sodium`, `Bromnatrium`, and `Trisodium tribromide` labels
  are all listed as OLS synonyms for the same ChEBI term.
- The `MINERAL_SOURCE` role is supported by imported CultureMech `Mineral`
  source role text. The #128 follow-up correctly avoids asserting bromide as a
  microbial trace element.
- The final SSSOM row maps `MIM:Nabr` exactly to `CHEBI:63004`, uses the
  canonical object label, and keeps only ChEBI same-substance aliases plus
  `CAS:7647-15-6` in `other`.

## Completeness

- The active ChEBI term, CAS RN, formula, structure, 322/322 occurrence count,
  role evidence, and final exact row agree.
- No component or environment assertions are present; those optional slots are
  appropriately empty for a single-salt record.

## Recommended Edits

- None.
