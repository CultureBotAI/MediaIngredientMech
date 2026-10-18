# `data/ingredients/mapped/MES_sodium_salt.yaml`

## Verdict

Needs curation. The exact CHEBI:62955 identity, CAS RN, ChEBI and PubChem
structure, curated synonyms, and final SSSOM row are consistent, but
`physicochemical_roles.BUFFER` is supported only by a provisional name-pattern
inference.

Severity: major.

## Identity

- Reviewed record: `data/ingredients/mapped/MES_sodium_salt.yaml`.
- Identifier and grounding: `identifier: CHEBI:62955` with
  `ontology_mapping.ontology_id: CHEBI:62955`, label
  `sodium 2-(N-morpholino)ethanesulfonate`, source `CHEBI`,
  `mapping_quality: CAS_RN_LOOKUP`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS RN `71119-23-8`, molecular formula
  `C6H12NO4S.Na`, InChI, and SMILES.
- Occurrences: 4 total occurrences in 4 CultureMech recipes.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `M-inositol` through `MES_sodium_salt`: exited 0 and wrote zero ERROR rows.
- `uv run --frozen linkml-term-validator validate-data` exited 0 for the
  CHEBI-primary subset `M-inositol`, `M-xylene`, and `MES_sodium_salt`;
  `MES_Buffer` and `MES_Hydrat` were skipped because their primary identifiers
  use local and CAS prefixes outside the CHEBI/OBO term adapter scope.

## Evidence

- EBI OLS4 resolves `CHEBI:62955` as active
  `sodium 2-(N-morpholino)ethanesulfonate`, lists CAS RN `71119-23-8`, and
  records the same ChEBI-form formula and InChI as the YAML record.
- PubChem resolves CAS RN `71119-23-8` to CID `23673676` with formula
  `C6H12NNaO4S` and the same InChI as the YAML record.
- The final SSSOM publishes one `skos:exactMatch` row to `CHEBI:62955`; its
  `other` field contains only exact salt synonyms and `CAS:71119-23-8`.

## Completeness

- The active CHEBI identity, CAS RN, formula, structure block, occurrence
  count, aggregate copy, and final SSSOM row are present and consistent.
- The `BUFFER` facet is based on `reference_type: COMPUTATIONAL_PREDICTION`
  with `reference_text: Inferred from curated media-role name pattern` and a
  curator note marking the role as provisional. No literature, database, or
  recipe evidence supports the asserted buffer activity in this record.

## Recommended Edits

- Curate evidence for `BUFFER`, or remove the role if no supporting
  ingredient-level evidence is available.
