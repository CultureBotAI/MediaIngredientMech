# `data/ingredients/mapped/Myo-inositol.yaml`

## Verdict

Needs curation. The exact `CHEBI:17268` myo-inositol identity, CAS metadata,
scyllo-inositol duplicate repair, occurrence count, and final exact row pass,
but the vitamin-source role is only a provisional name-pattern prediction.

Severity: major.

## Identity

- Reviewed record: `data/ingredients/mapped/Myo-inositol.yaml`.
- Identifier and grounding: `identifier: CHEBI:17268` with
  `ontology_mapping.ontology_id: CHEBI:17268`, label `myo-inositol`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 59 CultureMech recipe occurrences.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Myo-inositol` through `N-Acetyl-D-glucosamine_6-phosphate_Sodium_Salt`:
  exited 0 and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.

## Evidence

- A fresh EBI OLS4 lookup resolves `CHEBI:17268` as active `myo-inositol` with
  the expected same-substance aliases.
- The 2026-08-13 merge correctly records why the old `m-Inositol` duplicate was
  moved off `CHEBI:10642` scyllo-inositol and into this CAS-supported
  myo-inositol record.
- The final SSSOM publishes one `skos:exactMatch` row from `MIM:Myo-inositol`
  to `CHEBI:17268` with same-substance synonyms and `CAS:87-89-8` in `other`.

## Completeness

- The active ChEBI target, stereoisomer repair, CAS RN, occurrence count, and
  final row agree.
- `VITAMIN_SOURCE` has only `COMPUTATIONAL_PREDICTION` evidence from a curated
  media-role name pattern with a provisional curator note.

## Recommended Edits

- Major: add source-backed evidence that myo-inositol is used as a vitamin or
  growth-factor source in media, or remove the provisional `VITAMIN_SOURCE`
  role.
