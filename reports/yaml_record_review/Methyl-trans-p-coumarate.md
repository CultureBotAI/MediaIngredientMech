# `data/ingredients/mapped/Methyl-trans-p-coumarate.yaml`

## Verdict

Pass. The CAS-primary identity, same-structure ChEBI identity row, local
chemistry, and final SSSOM rows pass.

## Identity

- Reviewed record: `data/ingredients/mapped/Methyl-trans-p-coumarate.yaml`.
- Identifier and grounding: `identifier: cas:19367-38-5` with
  `ontology_mapping.ontology_id: CHEBI:194094`, label
  `(E)-4-coumaric acid methyl ester`, source `CHEBI`, `mapping_quality:
  SYNONYM_MATCH`, `mapping_status: MAPPED`, and `ingredient_type:
  SINGLE_INGREDIENT`.
- Occurrences: zero CultureMech recipe occurrences.
- Chemical identity: `cas_rn: 19367-38-5`, PubChem CID 5319562, formula
  `C10H10O3`, and the PubChem InChI for the trans/E ester.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Methyl-alpha-D-xylopyranoside` through `Methyl-trans-p-coumarate`: exited 0
  and wrote zero ERROR rows.
- Direct Engine A term validation was skipped for this CAS-primary registry
  record because CAS CURIEs are intentionally outside the OBO adapter scope.

## Evidence

- EBI OLS4 resolves `CHEBI:194094` as active
  `(E)-4-coumaric acid methyl ester` with formula `C10H10O3` and the same
  trans/E InChI and SMILES carried in the YAML.
- PubChem resolves CAS `19367-38-5` to CID 5319562 with formula `C10H10O3` and
  the same InChI carried in the YAML.
- The #326 regrade notes explain why the former parent row is now a synonym
  match: the CAS row and the ChEBI row have the same structure.
- The final SSSOM publishes the expected `skos:exactMatch` row to
  `CHEBI:194094` and a registry `skos:exactMatch` row to `cas:19367-38-5`; the
  only `other` token is `CAS:19367-38-5`.

## Completeness

- The record does not publish unsupported roles or cis/stereo-unspecified
  synonyms.

## Recommended Edits

- None.
