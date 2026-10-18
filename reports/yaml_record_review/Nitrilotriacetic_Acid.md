# `data/ingredients/mapped/Nitrilotriacetic_Acid.yaml`

## Verdict

Needs curation - major. The exact `CHEBI:44557` nitrilotriacetic acid
identity, CAS-backed structure, occurrence count, and final SSSOM row pass, but
`CHELATOR` is backed only by imported `Mineral` role text and a stray
auto-proposed PubMed search snippet remains as mapping evidence.

## Identity

- Reviewed record: `data/ingredients/mapped/Nitrilotriacetic_Acid.yaml`.
- Identifier and grounding: `identifier: CHEBI:44557` with
  `ontology_mapping.ontology_id: CHEBI:44557`, label
  `nitrilotriacetic acid`, source `CHEBI`, `mapping_quality: EXACT_MATCH`,
  `mapping_status: MAPPED`, and `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 1348 CultureMech recipe occurrences across 1348 media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Niso4_X_6_H2o` through `Nitrilotriacetic_Acid`: exited 0 and wrote zero
  ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.

## Evidence

- A fresh EBI OLS4 lookup resolves `CHEBI:44557` as active
  `nitrilotriacetic acid` with formula `C6H9NO6`, CAS `139-13-9`, and the
  same InChI and SMILES as the record.
- A fresh PubChem CAS lookup for `139-13-9` resolves to nitrilotriacetic acid
  with the same InChI, confirming the chemical block.
- The final SSSOM row maps `MIM:Nitrilotriacetic_Acid` exactly to
  `CHEBI:44557`; the raw disodium/trisodium salt fragments and raw
  `Role:`/`Properties:` labels are filtered from final `other`.
- Major: `physicochemical_roles.CHELATOR` cites CultureMech `Mineral source`
  text. That source text does not itself support a chelator role.
- Minor: `ontology_mapping.evidence` still includes `pmid: 34939907` from
  `PubMed search ('Nitrilotriacetic acid')`; the snippet is about an
  NTA-containing liposome and does not support this exact media-ingredient
  grounding.

## Completeness

- The active ChEBI term, CAS RN, formula, structure, 1348/1348 occurrence
  count, and final exact row otherwise agree.
- The remaining consequential gap is the unsupported chelator role evidence;
  the PubMed search evidence is redundant cleanup.

## Recommended Edits

- Major: in `data/ingredients/mapped/Nitrilotriacetic_Acid.yaml`, replace the
  `CHELATOR` role evidence with inspected source-backed chelation evidence, or
  remove the role until that evidence exists.
- Minor: remove the auto-proposed `pmid: 34939907` evidence object from
  `ontology_mapping`.
