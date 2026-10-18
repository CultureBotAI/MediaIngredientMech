# `data/ingredients/mapped/Nicotine_Fluka.yaml`

## Verdict

Pass with minor issues. The supplier-qualified CultureMech residual maps to
active `CHEBI:18723` nicotine and final SSSOM is clean, but the newer
residual-created YAML has not been backfilled with `ingredient_type` or
ChEBI-derived chemical properties.

## Identity

- Reviewed record: `data/ingredients/mapped/Nicotine_Fluka.yaml`.
- Identifier and grounding: `identifier: CHEBI:18723` with
  `ontology_mapping.ontology_id: CHEBI:18723`, label `nicotine`, source
  `CHEBI`, `mapping_quality: SYNONYM_MATCH`, `match_level: NORMALIZED`, and
  `mapping_status: MAPPED`.
- Occurrences: 1 CultureMech recipe occurrence across 1 medium.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Nicotine_Fluka` through `Nisin`: exited 0 and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.

## Evidence

- A fresh EBI OLS4 lookup resolves `CHEBI:18723` as active `nicotine` and
  preserves `nicotine` as the canonical label.
- A fresh PubChem lookup for the supplier-qualified text `Nicotine Fluka`
  returned no CID; the mapping therefore still rests on the restored
  CultureMech residual occurrence and exact ontology synonym evidence, not on
  source-specific CAS or structure confirmation.
- The final SSSOM row maps `MIM:Nicotine_Fluka` exactly to `CHEBI:18723` and
  emits no `other` synonym noise.

## Completeness

- The active ChEBI term, CultureMech occurrence evidence, 1/1 occurrence count,
  and final exact row agree.
- Minor: as a CHEBI-primary single-ingredient chemical, the record should have
  `ingredient_type: SINGLE_INGREDIENT` and a ChEBI-derived
  `chemical_properties` block when the supplier-qualified surface can be
  resolved to a concrete nicotine form.

## Recommended Edits

- Minor: in `data/ingredients/mapped/Nicotine_Fluka.yaml`, set
  `ingredient_type: SINGLE_INGREDIENT` and backfill the ChEBI/PubChem chemical
  block for the verified nicotine form.
