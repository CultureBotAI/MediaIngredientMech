# `data/ingredients/mapped/N-decane.yaml`

## Verdict

Pass. The exact `CHEBI:41808` decane identity, PubChem CAS provenance,
source-backed carbon-source role, occurrence count, accepted synonyms, and
final exact row pass.

## Identity

- Reviewed record: `data/ingredients/mapped/N-decane.yaml`.
- Identifier and grounding: `identifier: CHEBI:41808` with
  `ontology_mapping.ontology_id: CHEBI:41808`, label `decane`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: six CultureMech recipe occurrences.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `N-acetylneuraminate` through `N-decanoyl-DL-Homoserine_Lactone`: exited 0
  and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.

## Evidence

- A fresh EBI OLS4 lookup resolves `CHEBI:41808` as active `decane`, with
  `cas:124-18-5`, formula `C10H22`, the stored InChI/SMILES, and the curated
  ChEBI synonyms.
- CultureMech supplied original role text `Carbon Source`, which directly
  supports the migrated `CARBON_SOURCE` role.
- The final SSSOM publishes one `skos:exactMatch` row from `MIM:N-decane` to
  `CHEBI:41808` with same-substance synonyms and `CAS:124-18-5` in `other`.

## Completeness

- The active ChEBI target, CAS RN, structure, 6/6 occurrence count,
  source-backed role, accepted synonyms, and final row agree.
- The raw `Role: Carbon source; Properties: ...` import string remains only in
  YAML and is correctly filtered from final SSSOM `other`.

## Recommended Edits

- None.
