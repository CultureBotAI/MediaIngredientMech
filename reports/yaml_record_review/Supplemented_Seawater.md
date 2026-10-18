# `data/ingredients/mapped/Supplemented_Seawater.yaml`

## Verdict

Pass. The local supplemented-seawater identity, close parent edge to
`ENVO:00002149`, occurrence count, aggregate row, and final SSSOM registry
rows all pass.

## Identity

- Reviewed record: `data/ingredients/mapped/Supplemented_Seawater.yaml`.
- Identifier and grounding:
  `identifier: kgmicrobe.ingredient:supplemented_seawater` with
  `ontology_mapping.ontology_id: ENVO:00002149`, label `sea water`, source
  `ENVO`, `mapping_quality: CLOSE_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: UNDEFINED_MIXTURE`.
- Occurrences: 2 occurrences across 2 CultureMech media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Supplemented_Seawater` through `Synephrine_Tartrate`: exited 0 and wrote
  zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this ENVO-parent
  record.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh OLS4 lookup resolves active `ENVO:00002149` with label `sea water`.
- The May 2026 mapping review correctly kept the formulated
  supplemented-seawater preparation on a local KG-Microbe identifier and
  retained generic sea water only as a close ENVO parent.
- The final SSSOM emits the expected `skos:closeMatch` to `ENVO:00002149` plus
  the exact `kgmicrobe.ingredient:supplemented_seawater` registry identity row,
  and both rows leave `other` empty.

## Completeness

- The local identity, ENVO parent, aggregate row, 2 occurrences, and final
  SSSOM rows agree.
- The record has no active roles, components, environmental contexts, datasets,
  or chemical structure fields needing narrower evidence.
- An ignored/hidden search of local curated, mapping, generated, report,
  source, and documentation paths found the expected import, ENVO close-match,
  aggregate, final SSSOM, row-review, and generated rows. Other
  `ENVO:00002149` records represent different seawater preparations or rejected
  tombstones, not duplicate active records for supplemented seawater.

## Recommended Edits

- None.
