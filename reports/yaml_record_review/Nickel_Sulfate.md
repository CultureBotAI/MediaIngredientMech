# `data/ingredients/mapped/Nickel_Sulfate.yaml`

## Verdict

Pass with minor issues. The residual CultureMech label exactly maps to active
`CHEBI:53001` nickel sulfate and the final SSSOM row is clean, but the newer
residual-created YAML has not been backfilled with `ingredient_type` or
CHEBI-derived chemical properties.

## Identity

- Reviewed record: `data/ingredients/mapped/Nickel_Sulfate.yaml`.
- Identifier and grounding: `identifier: CHEBI:53001` with
  `ontology_mapping.ontology_id: CHEBI:53001`, label `nickel sulfate`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `match_level: EXACT`, and
  `mapping_status: MAPPED`.
- Occurrences: 19 CultureMech recipe occurrences across 19 media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Niaproof` through `Nicl2`: exited 0 and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.

## Evidence

- A fresh EBI OLS4 lookup resolves `CHEBI:53001` as active `nickel sulfate`
  with formula `Ni.O4S`, CAS `7786-81-4`, and synonyms including the exact
  source surface `Nickel sulfate`.
- A fresh PubChem CAS lookup for `7786-81-4` resolves to nickel sulfate with
  the same InChI as the active ChEBI term.
- The final SSSOM row maps `MIM:Nickel_Sulfate` exactly to `CHEBI:53001` and
  emits no `other` synonym noise.

## Completeness

- The active ChEBI term, CultureMech occurrence evidence, 19/19 occurrence
  count, and final exact row agree.
- Minor: as an exact CHEBI single-ingredient chemical, the record should have
  `ingredient_type: SINGLE_INGREDIENT` and a CHEBI-derived `chemical_properties`
  block with CAS RN, formula, InChI, and SMILES.

## Recommended Edits

- Minor: in `data/ingredients/mapped/Nickel_Sulfate.yaml`, set
  `ingredient_type: SINGLE_INGREDIENT` and backfill the ChEBI/PubChem chemical
  block for `CHEBI:53001`.
