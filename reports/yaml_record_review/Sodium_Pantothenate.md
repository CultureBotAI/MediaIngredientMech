# `data/ingredients/mapped/Sodium_Pantothenate.yaml`

## Verdict

Pass. The exact `NCIT:C220851` sodium pantothenate identity, restored
CultureMech evidence, occurrence count, and final SSSOM row pass.

## Identity

- Reviewed record: `data/ingredients/mapped/Sodium_Pantothenate.yaml`.
- Identifier and grounding: `identifier: NCIT:C220851` with
  `ontology_mapping.ontology_id: NCIT:C220851`, label
  `Sodium Pantothenate`, source `NCIT`, `mapping_quality: EXACT_MATCH`,
  `match_level: EXACT`, and `mapping_status: MAPPED`.
- Occurrences: 2 source occurrences across 2 CultureMech media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Sodium_Nitrate_Nitrogen_Source` through `Sodium_Pantothenate`: exited 0 and
  wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this NCIT-primary
  record.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.
- `uv run --frozen python scripts/run_shared_evidence_validator.py` is
  unavailable because the sibling `culturebotai-claw` checkout is absent.

## Evidence

- Fresh EBI OLS4 lookup resolves active `NCIT:C220851` with label
  `Sodium Pantothenate`.
- The ontology evidence points at
  `culturemech:output/ingredient_occurrences.tsv`, and the curation history
  records both the original exact-label grounding and the later structured
  evidence restoration for #541.
- Final SSSOM publishes one exact row to `NCIT:C220851` with the restored
  CultureMech occurrence-table source and no unsafe `other` payload.

## Completeness

- The NCIT ID, label, occurrence count, ontology evidence, history, and final
  exact row agree.
- Optional synonym, role, component, and chemical-property fields are correctly
  empty for this residual exact-label record.

## Recommended Edits

- None.
