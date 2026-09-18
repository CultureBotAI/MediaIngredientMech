# `data/ingredients/mapped/Mnso4_X_7_H2o.yaml`

## Verdict

Needs curation. The local `MnSO4 x 7 H2O` identity, curated anhydrous-parent
narrow match, occurrence count, rejected sibling-hydrate labels, and dual final
SSSOM rows pass, but the trace-element role is only a provisional name-pattern
prediction.

Severity: major.

## Identity

- Reviewed record: `data/ingredients/mapped/Mnso4_X_7_H2o.yaml`.
- Identifier and grounding:
  `identifier: kgmicrobe.compound:mnso4_x_7_h2o` with
  `ontology_mapping.ontology_id: CHEBI:86360`, label
  `manganese(II) sulfate`, source `CHEBI`,
  `mapping_quality: NARROW_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 16 CultureMech recipe occurrences.
- Local chemical identity: formula `Mn.O4S.7H2O` from the #652 local-hydrate
  repair.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Mnso4_X_7_H2o` through `Modified_Trace_Vitamins`: exited 0 and wrote zero
  ERROR rows.
- Direct Engine A term validation was skipped for this local registry record
  because its primary `kgmicrobe.compound` identifier is outside the OBO subset
  used for the batch.

## Evidence

- #652 changed the primary identifier from the anhydrous parent `CHEBI:86360`
  to the local `kgmicrobe.compound:mnso4_x_7_h2o`, retained
  `CHEBI:86360` only as a `NARROW_MATCH` parent, preserved the 7-water
  formula, and removed the anhydrous CAS.
- #251 marked the one-water, wildcard, and anhydrous strings as
  `REJECTED_LABEL`, so only 7-water labels remain as exportable synonyms.
- `reports/hydrate_grounding.tsv` marks this row `OK_LOCAL_REGISTRY_ID`.
- The final SSSOM publishes the intended pair of rows: an exact match to the
  local registry identity and a narrow match to anhydrous `CHEBI:86360`.

## Completeness

- The local identity, parent row, formula, rejected non-7-water aliases, 16/16
  occurrence count, and final rows agree.
- `TRACE_ELEMENT` has only `COMPUTATIONAL_PREDICTION` evidence from a curated
  media-role name pattern with a provisional curator note.

## Recommended Edits

- Major: add source-backed evidence that MnSO4 x 7 H2O is used as a trace
  element source in media, or remove the provisional `TRACE_ELEMENT` role.
