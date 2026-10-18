# `data/ingredients/mapped/Neutral_red.yaml`

## Verdict

Pass. The manual exact `CHEBI:86370` neutral red grounding, CultureMech gap
provenance, occurrence count, and final exact SSSOM row agree.

## Identity

- Reviewed record: `data/ingredients/mapped/Neutral_red.yaml`.
- Identifier and grounding: `identifier: CHEBI:86370` with
  `ontology_mapping.ontology_id: CHEBI:86370`, label `neutral red`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`,
  `mapping_status: MAPPED`, and `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 4 CultureMech recipe occurrences across 4 media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Netropsin` through `Nh42co3`: exited 0 and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.

## Evidence

- A fresh EBI OLS4 lookup resolves `CHEBI:86370` as active `neutral red`, the
  hydrochloride pH-indicator dye, with formula `C15H16N4.HCl`.
- The #260 curation note distinguishes this dye from `CHEBI:86372` neutral red
  base and `CHEBI:86373` neutral red(1+), which are adjacent but not the
  weighed media ingredient asserted here.
- The final SSSOM row maps `MIM:Neutral_red` exactly to `CHEBI:86370` and emits
  no `other` synonym noise.

## Completeness

- The active ChEBI term, manual gap-label provenance, 4/4 occurrence count, and
  final exact row agree.
- No role, component, or environment assertions are present; those optional
  slots are appropriately empty.

## Recommended Edits

- None.
