# `data/ingredients/mapped/Nickel_II_chloride_hexahydrate.yaml`

## Verdict

Needs curation - major. The exact `CHEBI:53542` nickel chloride hexahydrate
identity, CAS-backed structure, hydrate spelling cleanup, occurrence count, and
final SSSOM row pass, but the `TRACE_ELEMENT` role is still backed only by a
provisional in-session LLM assignment.

## Identity

- Reviewed record:
  `data/ingredients/mapped/Nickel_II_chloride_hexahydrate.yaml`.
- Identifier and grounding: `identifier: CHEBI:53542` with
  `ontology_mapping.ontology_id: CHEBI:53542`, label
  `nickel chloride hexahydrate`, source `CHEBI`,
  `mapping_quality: CAS_RN_LOOKUP`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 2992 CultureMech recipe occurrences across 2991 media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Niaproof` through `Nicl2`: exited 0 and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.

## Evidence

- A fresh EBI OLS4 lookup resolves `CHEBI:53542` as active
  `nickel chloride hexahydrate` with formula `2Cl.6H2O.Ni`, CAS `7791-20-0`,
  and the same InChI and SMILES as the record.
- A fresh PubChem CAS lookup for `7791-20-0` resolves to nickel chloride
  hexahydrate with the same InChI, confirming the chemical block.
- The final SSSOM row maps `MIM:Nickel_II_chloride_hexahydrate` exactly to
  `CHEBI:53542`; its hydrate synonyms, formula surface, and `CAS:7791-20-0`
  are all same-form labels for the hexahydrate.
- Major: `nutritional_roles.TRACE_ELEMENT` is backed only by
  `COMPUTATIONAL_PREDICTION` evidence whose note says it came from in-session
  Claude reasoning and needs review.

## Completeness

- The active ChEBI term, CAS RN, formula, structure, hydrate source labels,
  2991/2992 occurrence count, and final exact row agree.
- The remaining consequential gap is the unsupported provisional role.

## Recommended Edits

- Major: in
  `data/ingredients/mapped/Nickel_II_chloride_hexahydrate.yaml`, either replace
  `nutritional_roles.TRACE_ELEMENT` with inspected source evidence for nickel
  chloride hexahydrate as a trace-element source in media, or remove the
  provisional role.
