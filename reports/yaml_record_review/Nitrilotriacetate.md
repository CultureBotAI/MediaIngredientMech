# `data/ingredients/mapped/Nitrilotriacetate.yaml`

## Verdict

Needs curation - major. The exact `CHEBI:25548` nitrilotriacetate trianion
identity, CAS-backed structure, occurrence count, synonym-match grading, and
final SSSOM row pass, but `CHELATOR` is still backed only by imported
`Mineral` role text.

## Identity

- Reviewed record: `data/ingredients/mapped/Nitrilotriacetate.yaml`.
- Identifier and grounding: `identifier: CHEBI:25548` with
  `ontology_mapping.ontology_id: CHEBI:25548`, label
  `nitrilotriacetate(3-)`, source `CHEBI`,
  `mapping_quality: SYNONYM_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 14 CultureMech recipe occurrences across 14 media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Niso4_X_6_H2o` through `Nitrilotriacetic_Acid`: exited 0 and wrote zero
  ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.

## Evidence

- A fresh EBI OLS4 lookup resolves `CHEBI:25548` as active
  `nitrilotriacetate(3-)` with formula `C6H6NO6`, CAS `28528-44-1`, and the
  same InChI and SMILES as the record.
- A fresh PubChem CAS lookup for `28528-44-1` resolves to the same trianion
  InChI, confirming the chemical block.
- The final SSSOM row maps `MIM:Nitrilotriacetate` exactly to `CHEBI:25548`
  and the exported `other` values are same-substance aliases plus
  `CAS:28528-44-1`.
- Major: `physicochemical_roles.CHELATOR` cites a `DATABASE_ENTRY` whose
  curator note preserves only the original CultureMech role text `Mineral`.
  That source text does not itself support a chelator role.

## Completeness

- The active ChEBI term, CAS RN, formula, structure, 14/14 occurrence count,
  synonym-match grading, and final exact row otherwise agree.
- The remaining consequential gap is the unsupported chelator role evidence.

## Recommended Edits

- Major: in `data/ingredients/mapped/Nitrilotriacetate.yaml`, replace the
  `CHELATOR` role evidence with inspected source-backed chelation evidence, or
  remove the role until that evidence exists.
