# `data/ingredients/mapped/N-decanoyl-DL-Homoserine_Lactone.yaml`

## Verdict

Pass. The exact `CHEBI:181434` N-decanoyl-DL-homoserine lactone identity,
CultureBotHT CAS provenance, ChEBI synonym, structure, and final exact row
pass.

## Identity

- Reviewed record:
  `data/ingredients/mapped/N-decanoyl-DL-Homoserine_Lactone.yaml`.
- Identifier and grounding: `identifier: CHEBI:181434` with
  `ontology_mapping.ontology_id: CHEBI:181434`, label
  `N-Decanoyl-DL-homoserine lactone`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: no direct CultureMech recipe occurrences.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `N-acetylneuraminate` through `N-decanoyl-DL-Homoserine_Lactone`: exited 0
  and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.

## Evidence

- A fresh EBI OLS4 search for `CHEBI:181434` resolves the active
  `N-Decanoyl-DL-homoserine lactone` class and its exact
  `N-(2-oxooxolan-3-yl)decanamide` synonym.
- A fresh PubChem name lookup resolves `CAS:177315-87-6` for
  N-decanoyl-DL-homoserine lactone, matching the CultureBotHT CAS imported into
  `chemical_properties`.
- The final SSSOM publishes one `skos:exactMatch` row from
  `MIM:N-decanoyl-DL-Homoserine_Lactone` to `CHEBI:181434` with the ChEBI
  synonym and `CAS:177315-87-6` in `other`.

## Completeness

- The active ChEBI target, CAS RN, structure, accepted synonym, and final row
  agree.
- The record does not assert components, roles, or non-synonym final `other`
  text.

## Recommended Edits

- None.
