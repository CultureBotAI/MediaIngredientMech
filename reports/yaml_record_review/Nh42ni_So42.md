# `data/ingredients/mapped/Nh42ni_So42.yaml`

## Verdict

Needs curation - major. The record is currently a duplicate exact mapping to
`CHEBI:86149` ammonium nickel sulfate hexahydrate, while the explicit
hexahydrate row already carries the same identity; final SSSOM also exports a
concentration-qualified hydrate label, and `TRACE_ELEMENT` remains only a
provisional role prediction.

## Identity

- Reviewed record: `data/ingredients/mapped/Nh42ni_So42.yaml`.
- Identifier and grounding: `identifier: CHEBI:86149` with
  `ontology_mapping.ontology_id: CHEBI:86149`, label
  `ammonium nickel sulfate hexahydrate`, source `CHEBI`,
  `mapping_quality: SYNONYM_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 150 CultureMech recipe occurrences across 150 media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Nh42hpo4` through `Nh43_Citrate`: exited 0 and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.

## Evidence

- A fresh EBI OLS4 lookup resolves `CHEBI:86149` as active
  `ammonium nickel sulfate hexahydrate` with formula
  `6H2O.2H4N.Ni.2O4S`, CAS `7785-20-8`, and the same InChI and SMILES as the
  record.
- Major: this row and
  `data/ingredients/mapped/Nh42ni_So42_X_6_H2o.yaml` both actively exact-map to
  the same `CHEBI:86149` hydrate with the same 150/150 occurrence count.
  `mappings/other_cross_record_baseline.tsv` still flags their cross-exported
  labels as unresolved hydrate-family or unreviewed labels, and final SSSOM
  keeps both exact rows.
- Major: final SSSOM `other` for `MIM:Nh42ni_So42` includes the explicit
  `x 6 H2O` hydrate label and `x 6 H2O (0.1% w/v)`. The latter is
  concentration-qualified and neither is a clean alias for a separate
  non-hydrate-looking source row.
- Major: `nutritional_roles.TRACE_ELEMENT` has only
  `COMPUTATIONAL_PREDICTION` evidence from in-session Claude reasoning, and
  the evidence note explicitly marks the role provisional.

## Completeness

- The ChEBI term itself is active and structurally matches the stored hydrate
  block.
- The record is incomplete until the duplicate active ammonium-nickel-sulfate
  rows are merged or separated by an explicit source distinction, the
  concentration-qualified synonym is filtered, and the provisional role is
  either sourced or removed.

## Recommended Edits

- Major: decide whether `data/ingredients/mapped/Nh42ni_So42.yaml` is an
  accidental duplicate of the explicit hexahydrate row or a genuinely distinct
  anhydrous/source shorthand record. Merge or remap it accordingly, then
  rebuild SSSOM so only supported exact rows remain.
- Major: reject or demote the concentration-qualified
  `(NH4)2Ni(SO4)2 x 6 H2O (0.1% w/v)` synonym before rebuilding final SSSOM.
- Major: replace the provisional `TRACE_ELEMENT` assertion with database or
  publication evidence at the role claim or remove it before rebuilding
  downstream products.
