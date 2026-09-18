# `data/ingredients/mapped/Nh42co3.yaml`

## Verdict

Pass. The promoted `NH42CO3` formula shorthand now exactly maps to
`CHEBI:229630` ammonium carbonate, and its ChEBI structure, MediaDive CAS
support, occurrence count, and final SSSOM row agree.

## Identity

- Reviewed record: `data/ingredients/mapped/Nh42co3.yaml`.
- Identifier and grounding: `identifier: CHEBI:229630` with
  `ontology_mapping.ontology_id: CHEBI:229630`, label `ammonium carbonate`,
  source `CHEBI`, `mapping_quality: EXACT_MATCH`,
  `mapping_status: MAPPED`, and `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 2 CultureMech recipe occurrences across 2 media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Netropsin` through `Nh42co3`: exited 0 and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.

## Evidence

- A fresh EBI OLS4 lookup resolves `CHEBI:229630` as active
  `ammonium carbonate` with formula `CO3.2H4N` and the same InChI and SMILES as
  the record.
- A fresh PubChem lookup for the source CAS `10361-29-2` resolves to ammonium
  carbonate with the same InChI, supporting the #213 promotion note that
  interprets `NH42CO3` as `(NH4)2CO3`.
- The final SSSOM row maps `MIM:Nh42co3` exactly to `CHEBI:229630` and emits no
  `other` synonym noise.

## Completeness

- The active ChEBI term, formula, structure, source CAS support, 2/2 occurrence
  count, and final exact row agree.
- No role, component, or environment assertions are present; those optional
  slots are appropriately empty.

## Recommended Edits

- None.
