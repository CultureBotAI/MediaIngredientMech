# `data/ingredients/mapped/Naphthalene.yaml`

## Verdict

Pass. The exact `CHEBI:16482` naphthalene identity, CAS-backed structure,
`CARBON_SOURCE` role, occurrence count, ChEBI synonyms, and final exact SSSOM
row agree.

## Identity

- Reviewed record: `data/ingredients/mapped/Naphthalene.yaml`.
- Identifier and grounding: `identifier: CHEBI:16482` with
  `ontology_mapping.ontology_id: CHEBI:16482`, label `naphthalene`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 4 CultureMech recipe occurrences across 4 media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Nano` through `Naphthalene`: exited 0 and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.

## Evidence

- A fresh EBI OLS4 lookup resolves `CHEBI:16482` as active `naphthalene` with
  formula `C10H8`, CAS `91-20-3`, and the same InChI and SMILES as the record.
- A fresh PubChem CAS lookup for `91-20-3` resolves to naphthalene with the
  same formula and InChI, confirming the chemical block.
- The stored kg-microbe labels that publish in final SSSOM are listed by OLS as
  synonyms of the same ChEBI term.
- The `CARBON_SOURCE` role is supported by imported CultureMech `Carbon Source`
  role text.
- The final SSSOM row maps `MIM:Naphthalene` exactly to `CHEBI:16482`, uses the
  canonical object label, and keeps only same-substance ChEBI aliases plus
  `CAS:91-20-3` in `other`.

## Completeness

- The active ChEBI term, CAS RN, formula, structure, 4/4 occurrence count, role
  evidence, and final exact row agree.
- No component or environment assertions are present; those optional slots are
  appropriately empty for a single-compound record.

## Recommended Edits

- None.
