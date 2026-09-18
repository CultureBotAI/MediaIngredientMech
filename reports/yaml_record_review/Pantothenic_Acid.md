# `data/ingredients/mapped/Pantothenic_Acid.yaml`

## Verdict

Pass. The CultureMech record maps exactly to active `CHEBI:7916`
pantothenic acid, carries source-backed vitamin evidence, and exports only
same-acid final synonyms.

## Identity

- Reviewed record: `data/ingredients/mapped/Pantothenic_Acid.yaml`.
- Identifier and grounding: `identifier: CHEBI:7916` with
  `ontology_mapping.ontology_id: CHEBI:7916`, label `pantothenic acid`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 126 CultureMech occurrences across 126 recipes.

## Validation

- `uv run --frozen python scripts/validate_strict.py` exited 0 across this
  five-record batch and wrote zero ERROR rows.
- A fresh OLS4 exact search for `Pantothenic acid` resolves `CHEBI:7916`
  `pantothenic acid`.
- A local CAS checksum calculation confirmed that `599-54-2` has the expected
  check digit.
- The final SSSOM row was inspected directly and maps `MIM:Pantothenic_Acid`
  exactly to `CHEBI:7916`.

## Evidence

- The CHEBI primary identifier, mapping target, structured formula, InChI, and
  SMILES all describe neutral pantothenic acid.
- The final SSSOM `other` column keeps only same-acid exact names plus
  `CAS:599-54-2`; raw `Role:` provenance strings in YAML are correctly
  filtered from the product.
- The `VITAMIN_SOURCE` role is backed by `DATABASE_ENTRY` evidence from the
  CultureMech import with original role text `Vitamin Source`, so it is not a
  provisional name-list role.

## Completeness

- The CAS conflict with calcium pantothenate was already resolved to
  `599-54-2`, the OAK/CHEBI xref for this neutral acid.
- No consequential gap was found for this exact CHEBI mapping and CultureMech
  role import.

## Recommended Edits

- None.
