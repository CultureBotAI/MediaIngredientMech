# `data/ingredients/mapped/Nh4hco3.yaml`

## Verdict

Pass. The exact `CHEBI:184335` ammonium bicarbonate identity, CAS-backed
structure, source-backed `NITROGEN_SOURCE` role, occurrence count, and final
SSSOM row agree.

## Identity

- Reviewed record: `data/ingredients/mapped/Nh4hco3.yaml`.
- Identifier and grounding: `identifier: CHEBI:184335` with
  `ontology_mapping.ontology_id: CHEBI:184335`, label
  `Ammonium bicarbonate`, source `CHEBI`, `mapping_quality: EXACT_MATCH`,
  `mapping_status: MAPPED`, and `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 31 CultureMech recipe occurrences across 31 media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Nh4cl` through `Nh4no3`: exited 0 and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.

## Evidence

- A fresh EBI OLS4 lookup resolves `CHEBI:184335` as active
  `Ammonium bicarbonate` with formula `CHO3.H4N`, CAS `1066-33-7`, and the
  same InChI and SMILES as the record.
- A fresh PubChem CAS lookup for `1066-33-7` resolves to ammonium bicarbonate
  with the same InChI, confirming the chemical block.
- `NITROGEN_SOURCE` is supported by imported CultureMech `Nitrogen Source`
  role text, and raw `Role:`/`Properties:` labels are filtered from final
  SSSOM.
- The final SSSOM row maps `MIM:Nh4hco3` exactly to `CHEBI:184335` and the
  exported `other` values are registry synonyms plus `CAS:1066-33-7`.

## Completeness

- The active ChEBI term, CAS RN, formula, structure, 31/31 occurrence count,
  role evidence, and final exact row agree.
- No component or environment assertions are present; those optional slots are
  appropriately empty.

## Recommended Edits

- None.
