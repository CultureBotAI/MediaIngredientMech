# `data/ingredients/mapped/Na-3-hydroxybutyrate.yaml`

## Verdict

Needs curation - major. The exact `CHEBI:113373` sodium
3-hydroxybutyrate identity, CAS provenance, structure, occurrence count, ChEBI
synonyms, and final exact row pass, but `CARBON_SOURCE` is only a provisional
name-pattern inference.

## Identity

- Reviewed record: `data/ingredients/mapped/Na-3-hydroxybutyrate.yaml`.
- Identifier and grounding: `identifier: CHEBI:113373` with
  `ontology_mapping.ontology_id: CHEBI:113373`, label
  `sodium 3-hydroxybutyrate`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: three CultureMech recipe occurrences.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Na-3-hydroxybutyrate` through `Na-ascorbate`: exited 0 and wrote zero ERROR
  rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.

## Evidence

- A fresh EBI OLS4 lookup resolves `CHEBI:113373` as active
  `sodium 3-hydroxybutyrate`, with `cas:150-83-4`, formula `C4H7O3.Na`, the
  stored InChI/SMILES, and the curated ChEBI sodium-salt synonyms.
- The final SSSOM publishes one `skos:exactMatch` row from
  `MIM:Na-3-hydroxybutyrate` to `CHEBI:113373` with same-substance synonyms
  and `CAS:150-83-4` in `other`.
- Major: `nutritional_roles.CARBON_SOURCE` is supported only by
  `COMPUTATIONAL_PREDICTION` from a curated name-pattern rule and has a
  provisional curator note. No inspected source on the role asserts sodium
  3-hydroxybutyrate is used as a carbon source in the relevant media.

## Completeness

- The active ChEBI target, CAS RN, structure, 3/3 occurrence count, accepted
  synonyms, and final row agree.
- The only consequential gap is role evidence for `CARBON_SOURCE`.

## Recommended Edits

- Major: in `data/ingredients/mapped/Na-3-hydroxybutyrate.yaml`, either replace
  the `CARBON_SOURCE` name-pattern inference with source-backed evidence for
  this sodium salt or remove the unsupported role. Re-run strict validation,
  final SSSOM validation, and component partonomy validation after the repair.
