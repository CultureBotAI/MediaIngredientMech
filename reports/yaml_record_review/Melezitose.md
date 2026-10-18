# `data/ingredients/mapped/Melezitose.yaml`

## Verdict

Pass. The exact anhydrous ChEBI identity, structure, occurrence count, and final
SSSOM row all pass.

## Identity

- Reviewed record: `data/ingredients/mapped/Melezitose.yaml`.
- Identifier and grounding: `identifier: CHEBI:6731` with
  `ontology_mapping.ontology_id: CHEBI:6731`, label `melezitose`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: two CultureMech recipes plus 67 MicrobeDecoder
  `BacDive_Metabolite_utilization` occurrences.
- Chemical identity: formula `C18H32O16`, InChI, and SMILES copied from
  ChEBI/PubChem.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Meat_peptone` through `Melezitose`: exited 0 and wrote zero ERROR rows.
- `uv run --frozen linkml-term-validator validate-data` exited 0 for this
  CHEBI-primary record.

## Evidence

- EBI OLS4 resolves `CHEBI:6731` as active `melezitose` with CAS `597-12-6`,
  formula `C18H32O16`, the same InChI and SMILES carried in the YAML, and the
  exact IUPAC synonym for the anhydrous trisaccharide.
- The hydrate record `data/ingredients/mapped/D-_-melezitose_Hydrate.yaml`
  remains separate and has its own CAS-primary identity; this record's final
  SSSOM row does not export hydrate-specific synonyms or CAS values.
- The final SSSOM publishes one `skos:exactMatch` row from `MIM:Melezitose` to
  `CHEBI:6731` with empty `other`.

## Completeness

- The record does not publish unsupported roles or non-exact synonyms.

## Recommended Edits

- None.
