# `data/ingredients/mapped/Nh4h2po4.yaml`

## Verdict

Pass. The exact `CHEBI:62982` ammonium dihydrogen phosphate identity,
CAS-backed structure, source-backed `NITROGEN_SOURCE` role, occurrence count,
and final SSSOM row agree.

## Identity

- Reviewed record: `data/ingredients/mapped/Nh4h2po4.yaml`.
- Identifier and grounding: `identifier: CHEBI:62982` with
  `ontology_mapping.ontology_id: CHEBI:62982`, label
  `ammonium dihydrogen phosphate`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 17 CultureMech recipe occurrences across 17 media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Nh4cl` through `Nh4no3`: exited 0 and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.

## Evidence

- A fresh EBI OLS4 lookup resolves `CHEBI:62982` as active
  `ammonium dihydrogen phosphate` with formula `H2O4P.H4N`, CAS
  `7722-76-1`, and the same InChI and SMILES as the record.
- A fresh PubChem CAS lookup for `7722-76-1` resolves to ammonium dihydrogen
  phosphate with the same InChI, confirming the chemical block.
- `NITROGEN_SOURCE` is supported by imported CultureMech `Nitrogen Source`
  role text, and raw `Role:`/`Properties:` labels are filtered from final
  SSSOM.
- The final SSSOM row maps `MIM:Nh4h2po4` exactly to `CHEBI:62982` and the
  exported `other` values are registry synonyms plus `CAS:7722-76-1`.

## Completeness

- The active ChEBI term, CAS RN, formula, structure, 17/17 occurrence count,
  role evidence, and final exact row agree.
- No component or environment assertions are present; those optional slots are
  appropriately empty.

## Recommended Edits

- None.
