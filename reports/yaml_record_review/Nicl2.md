# `data/ingredients/mapped/Nicl2.yaml`

## Verdict

Pass. The exact `CHEBI:34887` anhydrous nickel dichloride identity,
CAS-backed structure, source-backed `TRACE_ELEMENT` role, rejected hydrate
aliases, occurrence count, and final SSSOM row agree.

## Identity

- Reviewed record: `data/ingredients/mapped/Nicl2.yaml`.
- Identifier and grounding: `identifier: CHEBI:34887` with
  `ontology_mapping.ontology_id: CHEBI:34887`, label `nickel dichloride`,
  source `CHEBI`, `mapping_quality: EXACT_MATCH`,
  `mapping_status: MAPPED`, and `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 440 CultureMech recipe occurrences across 440 media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Niaproof` through `Nicl2`: exited 0 and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.

## Evidence

- A fresh EBI OLS4 lookup resolves `CHEBI:34887` as active
  `nickel dichloride` with formula `Cl2Ni`, CAS `7718-54-9`, and the same
  InChI and SMILES as the record.
- A fresh PubChem CAS lookup for `7718-54-9` resolves to anhydrous nickel
  chloride with the same InChI, confirming the chemical block.
- `TRACE_ELEMENT` is backed by CultureMech `Mineral source` role text for the
  nickel salt, and the raw `Role:`/`Properties:` label is filtered from final
  SSSOM.
- The rejected hydrated `NiCl2` aliases remain in YAML as `REJECTED_LABEL`
  provenance and are omitted from final SSSOM `other`, preserving the
  anhydrous boundary.
- The final SSSOM row maps `MIM:Nicl2` exactly to `CHEBI:34887` and emits only
  same-form labels plus `CAS:7718-54-9`.

## Completeness

- The active ChEBI term, CAS RN, formula, structure, source-backed role,
  hydrate-alias rejection, 440/440 occurrence count, and final exact row agree.
- No component or environment assertions are present; those optional slots are
  appropriately empty.

## Recommended Edits

- None.
