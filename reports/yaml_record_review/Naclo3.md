# `data/ingredients/mapped/Naclo3.yaml`

## Verdict

Pass. The exact `CHEBI:65242` sodium chlorate identity, CAS-backed structure,
`MINERAL_SOURCE` role, occurrence count, ChEBI synonyms, and final exact SSSOM
row agree.

## Identity

- Reviewed record: `data/ingredients/mapped/Naclo3.yaml`.
- Identifier and grounding: `identifier: CHEBI:65242` with
  `ontology_mapping.ontology_id: CHEBI:65242`, label `sodium chlorate`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 16 CultureMech recipe occurrences across 16 media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Nacl` through `Nah2po4`: exited 0 and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.

## Evidence

- A fresh EBI OLS4 lookup resolves `CHEBI:65242` as active `sodium chlorate`
  with formula `ClO3.Na`, CAS `7775-09-9`, and the same InChI and SMILES as
  the record.
- A fresh PubChem CAS lookup for `7775-09-9` resolves to sodium chlorate with
  the same InChI, confirming the chemical block.
- The stored kg-microbe labels are listed by OLS as synonyms of the same ChEBI
  term.
- The `MINERAL_SOURCE` role is supported by imported CultureMech `Mineral`
  source role text.
- The final SSSOM row maps `MIM:Naclo3` exactly to `CHEBI:65242`, uses the
  canonical object label, and keeps only same-substance ChEBI aliases plus
  `CAS:7775-09-9` in `other`.

## Completeness

- The active ChEBI term, CAS RN, formula, structure, 16/16 occurrence count,
  role evidence, and final exact row agree.
- No component or environment assertions are present; those optional slots are
  appropriately empty for a single-salt record.

## Recommended Edits

- None.
