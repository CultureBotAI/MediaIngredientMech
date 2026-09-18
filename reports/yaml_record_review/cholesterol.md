# `data/ingredients/mapped/cholesterol.yaml`

## Verdict

Needs curation, minor. The 2026-07-05 correction moved cholesterol off the
deuterated isotopologue and onto active `CHEBI:16113`, but the post-correction
`chemical_properties` block still has only formula and CAS rather than the
expected ChEBI InChI and SMILES.

## Identity

- Reviewed record: `data/ingredients/mapped/cholesterol.yaml`.
- Identifier and grounding: `identifier: CHEBI:16113` with matching
  `ontology_mapping.ontology_id`, canonical label `cholesterol`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- CAS RN: `57-88-5`.
- Structure: formula `C27H46O`; InChI and SMILES are absent after the
  isotope-mapping correction.
- Synonyms: three non-deuterated cholesterol exact synonyms from kg-microbe.
- Occurrences: four CultureMech occurrences across four media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on this 5-file batch:
  exited 0 and wrote zero ERROR rows.
- `uv run linkml-term-validator validate-data` passed for this CHEBI-primary
  record with `--labels`.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.
- Fresh OLS4 exact search for `cholesterol` in CHEBI returned the active
  `CHEBI:16113` label `cholesterol`.

## Evidence

- The final SSSOM row correctly exports
  `MIM:cholesterol skos:exactMatch CHEBI:16113`.
- The final SSSOM `other` field contains only the three non-deuterated exact
  cholesterol synonyms and matching `CAS:57-88-5`.
- No deuterated synonyms from the original `CHEBI:140435` mapping remain in the
  active YAML or final SSSOM row.

## Issues

- Minor: InChI and SMILES should be backfilled from `CHEBI:16113` now that the
  record no longer maps to the deuterated isotopologue.

## Completeness

- The exact CHEBI identifier, CAS, formula, single-ingredient type, non-isotope
  synonyms, occurrence count, aggregate copy, and final SSSOM row agree.
- ChEBI structure backfill is incomplete.

## Recommended Edits

- Backfill InChI and SMILES from `CHEBI:16113`.
- Rerun strict validation and the final SSSOM invariant gate.
