# `data/ingredients/mapped/Netropsin.yaml`

## Verdict

Pass. The manual MeSH `mesh:D009429` Netropsin identity, reviewed promotion,
MicrobeDecoder occurrence, and final exact SSSOM row agree.

## Identity

- Reviewed record: `data/ingredients/mapped/Netropsin.yaml`.
- Identifier and grounding: `identifier: mesh:D009429` with
  `ontology_mapping.ontology_id: mesh:D009429`, label `Netropsin`, source
  `MESH`, `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Occurrences: 0 CultureMech recipe occurrences and 1 MicrobeDecoder source
  occurrence.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Netropsin` through `Nh42co3`: exited 0 and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this MeSH-primary
  record.

## Evidence

- A fresh OLS4 MeSH search resolves `mesh:D009429` as active `Netropsin`.
- The final SSSOM row maps `MIM:Netropsin` exactly to `mesh:D009429`, keeps the
  MeSH object label, and emits no `other` synonym noise.
- The record has no chemical, role, component, or environmental assertions that
  require narrower evidence.

## Completeness

- The active MeSH term, manual #213 promotion, MicrobeDecoder occurrence, empty
  CultureMech occurrence count, and final exact row agree.
- ChEBI/NCIT grounding is not required here because #213 intentionally chose
  MeSH for a MicrobeDecoder trait that was absent from those sources.

## Recommended Edits

- None.
