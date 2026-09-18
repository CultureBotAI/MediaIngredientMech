# `data/ingredients/mapped/Staphylomycin_M1.yaml`

## Verdict

Needs curation - major. The NCIT exact-synonym grounding for Staphylomycin M1
resolves, but `SELECTIVE_AGENT` is still a provisional name-pattern role.

## Identity

- Reviewed record: `data/ingredients/mapped/Staphylomycin_M1.yaml`.
- Identifier and grounding: `identifier: NCIT:C1295` with
  `ontology_mapping.ontology_id: NCIT:C1295`, label `Streptogramin A`, source
  `NCIT`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 0 source occurrences across 0 CultureMech media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Stallimycin` through `Stearic_Acid`: exited 0 and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this NCIT record.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh OLS4 lookup resolves active `NCIT:C1295` with label `Streptogramin A`
  and exact synonym `staphylomycin M1`, matching the recorded promotion from
  the local kg-microbe placeholder to NCIT.
- The final SSSOM row exact-matches `NCIT:C1295` and has empty `other`.
- Major: `physicochemical_roles.SELECTIVE_AGENT` is supported only by
  `COMPUTATIONAL_PREDICTION` from `infer_roles_from_name_lists`, with the
  provisional name-pattern curator note.

## Completeness

- The NCIT identity, aggregate row, and final SSSOM row agree.
- No unsupported active synonym, component, or final SSSOM payload was found;
  the only unsupported claim is the provisional selective-agent role.

## Recommended Edits

- Major: either remove `physicochemical_roles.SELECTIVE_AGENT` from
  `data/ingredients/mapped/Staphylomycin_M1.yaml`, or replace the name-pattern
  evidence with a source that explicitly uses Staphylomycin M1 as a selective
  agent in a culture context.
