# `data/ingredients/mapped/Palmitic_Acid.yaml`

## Verdict

Pass. The CultureBotHT CAS-to-ChEBI lookup record maps `Palmitic acid` exactly
to `CHEBI:15756` hexadecanoic acid and exports only the matching CAS synonym.

## Identity

- Reviewed record: `data/ingredients/mapped/Palmitic_Acid.yaml`.
- Identifier and grounding: `identifier: CHEBI:15756` with
  `ontology_mapping.ontology_id: CHEBI:15756`, label `hexadecanoic acid`,
  source `CHEBI`, `mapping_quality: CAS_RN_LOOKUP`,
  `mapping_status: MAPPED`, and `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: no CultureMech media occurrences.

## Validation

- `uv run --frozen python scripts/validate_strict.py` exited 0 across this
  five-record batch and wrote zero ERROR rows.
- The existing OAK/OLS row review confirms `CHEBI:15756`; a fresh exact OLS4
  search for `Palmitic acid` also found only same-substance parent entries and
  measurement classes.
- A local CAS checksum calculation confirmed that `57-10-3` has the expected
  check digit.
- The final SSSOM row was inspected directly and maps `MIM:Palmitic_Acid`
  exactly to `CHEBI:15756`.

## Evidence

- The CAS-derived CHEBI primary identifier, mapping target, structured formula,
  InChI, and SMILES all describe hexadecanoic acid.
- The `CAS_RN_LOOKUP` grade accurately records how the mapping was established;
  Rule D still emits the own-identifier row as `skos:exactMatch`.
- The final SSSOM exports only `CAS:57-10-3` in `other`; that value matches the
  structured `chemical_properties.cas_rn`.
- There are no asserted role facets requiring additional source support.

## Completeness

- No consequential gap was found for this single-ingredient exact CHEBI
  mapping.

## Recommended Edits

- None.
