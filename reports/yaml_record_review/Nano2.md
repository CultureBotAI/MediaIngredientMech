# `data/ingredients/mapped/Nano2.yaml`

## Verdict

Pass. The exact `CHEBI:78870` sodium nitrite identity, CAS-backed structure,
`NITROGEN_SOURCE` role, occurrence count, ChEBI synonyms, and final exact SSSOM
row agree.

## Identity

- Reviewed record: `data/ingredients/mapped/Nano2.yaml`.
- Identifier and grounding: `identifier: CHEBI:78870` with
  `ontology_mapping.ontology_id: CHEBI:78870`, label `sodium nitrite`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 30 CultureMech recipe occurrences across 30 media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Nano` through `Naphthalene`: exited 0 and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.

## Evidence

- A fresh EBI OLS4 lookup resolves `CHEBI:78870` as active `sodium nitrite`
  with formula `NO2.Na`, CAS `7632-00-0`, and the same InChI and SMILES as the
  record.
- A fresh PubChem CAS lookup for `7632-00-0` resolves to sodium nitrite with
  the same InChI, confirming the chemical block.
- The stored kg-microbe labels that publish in final SSSOM are listed by OLS as
  synonyms of the same ChEBI term.
- The `NITROGEN_SOURCE` role is supported by imported CultureMech `Nitrogen
  Source` role text.
- The final SSSOM row maps `MIM:Nano2` exactly to `CHEBI:78870`, uses the
  canonical object label, and keeps only same-substance ChEBI aliases plus
  `CAS:7632-00-0` in `other`.

## Completeness

- The active ChEBI term, CAS RN, formula, structure, 30/30 occurrence count,
  role evidence, and final exact row agree.
- No component or environment assertions are present; those optional slots are
  appropriately empty for a single-salt record.

## Recommended Edits

- None.
