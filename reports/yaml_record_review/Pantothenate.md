# `data/ingredients/mapped/Pantothenate.yaml`

## Verdict

Pass. The CultureMech record maps exactly to active `CHEBI:16454`
pantothenate, keeps its original vitamin role with database-entry evidence, and
filters raw CultureMech role text out of final SSSOM `other`.

## Identity

- Reviewed record: `data/ingredients/mapped/Pantothenate.yaml`.
- Identifier and grounding: `identifier: CHEBI:16454` with
  `ontology_mapping.ontology_id: CHEBI:16454`, label `pantothenate`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 36 CultureMech occurrences across 36 recipes.

## Validation

- `uv run --frozen python scripts/validate_strict.py` exited 0 across this
  five-record batch and wrote zero ERROR rows.
- A fresh OLS4 exact search for `Pantothenate` resolves `CHEBI:16454`
  `pantothenate`.
- A local CAS checksum calculation confirmed that `20938-62-9` has the
  expected check digit.
- The final SSSOM row was inspected directly and maps `MIM:Pantothenate`
  exactly to `CHEBI:16454`.

## Evidence

- The CHEBI primary identifier, mapping target, structured formula, InChI, and
  SMILES all describe the pantothenate anion.
- The final SSSOM `other` column keeps only same-anion exact names plus
  `CAS:20938-62-9`; raw `Role:` and `Cross-references:` provenance strings in
  YAML are correctly filtered from the product.
- The `VITAMIN_SOURCE` role is backed by `DATABASE_ENTRY` evidence from the
  CultureMech import with original role text `Vitamin Source`, so it is not a
  provisional name-list role.

## Completeness

- No consequential gap was found for this exact CHEBI mapping and CultureMech
  role import.

## Recommended Edits

- None.
