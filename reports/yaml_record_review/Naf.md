# `data/ingredients/mapped/Naf.yaml`

## Verdict

Pass. The exact `CHEBI:28741` sodium fluoride identity, CAS-backed structure,
`MINERAL_SOURCE` role, occurrence count, ChEBI synonym, and final exact SSSOM
row agree.

## Identity

- Reviewed record: `data/ingredients/mapped/Naf.yaml`.
- Identifier and grounding: `identifier: CHEBI:28741` with
  `ontology_mapping.ontology_id: CHEBI:28741`, label `sodium fluoride`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 302 CultureMech recipe occurrences across 302 media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Nacl` through `Nah2po4`: exited 0 and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.

## Evidence

- A fresh EBI OLS4 lookup resolves `CHEBI:28741` as active `sodium fluoride`
  with formula `F.Na`, CAS `7681-49-4`, and the same InChI and SMILES as the
  record.
- A fresh PubChem CAS lookup for `7681-49-4` resolves to sodium fluoride with
  the same InChI, confirming the chemical block.
- `Sodium Fluoride` is a same-term ChEBI synonym, and final SSSOM avoids
  re-emitting that case variant in `other`.
- The `MINERAL_SOURCE` role is supported by imported CultureMech `Mineral`
  source role text. The #128 follow-up deliberately kept `MINERAL_SOURCE`
  without asserting that fluoride is a microbial trace element.
- The final SSSOM row maps `MIM:Naf` exactly to `CHEBI:28741`, uses the
  canonical object label, and keeps only `CAS:7681-49-4` in `other`.

## Completeness

- The active ChEBI term, CAS RN, formula, structure, 302/302 occurrence count,
  role evidence, and final exact row agree.
- No component or environment assertions are present; those optional slots are
  appropriately empty for a single-salt record.

## Recommended Edits

- None.
