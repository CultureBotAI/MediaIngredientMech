# `data/ingredients/mapped/Na-ampicillin.yaml`

## Verdict

Needs curation - major. The exact `CHEBI:34535` ampicillin sodium identity, CAS
provenance, accepted synonyms, duplicate merge, structure, and final exact row
pass, but `SELECTIVE_AGENT` is only a provisional name-list inference.

## Identity

- Reviewed record: `data/ingredients/mapped/Na-ampicillin.yaml`.
- Identifier and grounding: `identifier: CHEBI:34535` with
  `ontology_mapping.ontology_id: CHEBI:34535`, label `ampicillin sodium`,
  source `CHEBI`, `mapping_quality: EXACT_MATCH`,
  `mapping_status: MAPPED`, and `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 12 CultureMech recipe occurrences.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Na-3-hydroxybutyrate` through `Na-ascorbate`: exited 0 and wrote zero ERROR
  rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.

## Evidence

- A fresh EBI OLS4 lookup resolves `CHEBI:34535` as active
  `ampicillin sodium`, with `cas:69-52-3`, formula `C16H18N3O4S.Na`, the
  stored InChI/SMILES, and the curated sodium ampicillin synonyms.
- The final SSSOM publishes one `skos:exactMatch` row from
  `MIM:Na-ampicillin` to `CHEBI:34535` with same-substance synonyms, the folded
  raw `Ampicillin sodium salt` label, and `CAS:69-52-3` in `other`.
- Major: `physicochemical_roles.SELECTIVE_AGENT` is supported only by
  `COMPUTATIONAL_PREDICTION` from a curated name-pattern rule and has a
  provisional curator note. The antibiotic identity makes the role plausible,
  but the record lacks inspected evidence for its selective-agent use in the
  imported media context.

## Completeness

- The active ChEBI target, CAS RN, structure, 12/12 occurrence count, duplicate
  merge, accepted synonyms, and final row agree.
- The only consequential gap is source-backed evidence for `SELECTIVE_AGENT`.

## Recommended Edits

- Major: in `data/ingredients/mapped/Na-ampicillin.yaml`, replace the
  provisional `SELECTIVE_AGENT` inference with source-backed role evidence or
  remove the role. Re-run strict validation and final SSSOM validation after
  the repair.
