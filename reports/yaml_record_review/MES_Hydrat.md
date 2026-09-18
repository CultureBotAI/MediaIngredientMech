# `data/ingredients/mapped/MES_Hydrat.yaml`

## Verdict

Needs curation. The CAS-primary MES monohydrate identity, narrow anhydrous
CHEBI parent, exact CAS/local registry rows, and aggregate copy pass, but the
final SSSOM `other` field exports an anhydrous MES record label as a synonym of
`MES Hydrat`.

Severity: major.

## Identity

- Reviewed record: `data/ingredients/mapped/MES_Hydrat.yaml`.
- Identifier and grounding: `identifier: cas:145224-94-8` with
  `ontology_mapping.ontology_id: CHEBI:39005`, label
  `2-(N-morpholino)ethanesulfonic acid`, source `CHEBI`,
  `mapping_quality: NARROW_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS RN `145224-94-8`.
- Occurrences: 4 total occurrences in 4 CultureMech recipes.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `M-inositol` through `MES_sodium_salt`: exited 0 and wrote zero ERROR rows.
- `uv run --frozen linkml-term-validator validate-data` exited 0 for the
  CHEBI-primary subset `M-inositol`, `M-xylene`, and `MES_sodium_salt`;
  `MES_Buffer` and `MES_Hydrat` were skipped because their primary identifiers
  use local and CAS prefixes outside the CHEBI/OBO term adapter scope.

## Evidence

- EBI OLS4 resolves `CHEBI:39005` as active
  `2-(N-morpholino)ethanesulfonic acid`, the anhydrous MES acid, with CAS RN
  `4432-31-9` and formula `C6H13NO4S`.
- PubChem resolves the record CAS RN `145224-94-8` to CID `16218417` with
  formula `C6H15NO5S`, the monohydrate composition.
- The final SSSOM publishes the expected `skos:narrowMatch` row to
  `CHEBI:39005` and exact registry rows to `cas:145224-94-8` and
  `kgmicrobe.compound:mes_hydrat`.

## Completeness

- The monohydrate CAS primary identifier, anhydrous CHEBI parent, occurrence
  count, aggregate copy, and exact CAS and kgmicrobe registry rows are present
  and consistent.
- The final `MIM:MES_Hydrat` `skos:narrowMatch` row carries
  `MES [2-(N-morpholino) ethane sulfonic acid]` in its `other` field. That
  token is the preferred label of the separate active anhydrous
  `Mes_2-_N-morpholino_Ethane_Sulfonic_Acid` record, so it erases the hydrate
  boundary when exported as a synonym of `MES Hydrat`.

## Recommended Edits

- Stop exporting the anhydrous `MES [2-(N-morpholino) ethane sulfonic acid]`
  label as an `other` synonym for `MIM:MES_Hydrat`.
