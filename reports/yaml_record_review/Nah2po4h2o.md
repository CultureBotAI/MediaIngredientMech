# `data/ingredients/mapped/Nah2po4h2o.yaml`

## Verdict

Needs curation - major. The record intentionally preserved the monohydrate as
distinct from anhydrous `CHEBI:37585`, but fresh OLS4 now exposes exact
`CHEBI:114249` sodium dihydrogenphosphate monohydrate with CAS `10049-21-5`;
the current CAS/local registry rows and anhydrous parent row should be promoted
to that term.

## Identity

- Reviewed record: `data/ingredients/mapped/Nah2po4h2o.yaml`.
- Identifier and grounding: `identifier: cas:10049-21-5` with
  `ontology_mapping.ontology_id: CHEBI:37585`, label
  `sodium dihydrogenphosphate`, source `CHEBI`,
  `mapping_quality: NARROW_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 4 CultureMech recipe occurrences across 4 media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Nah2po4_X_2_H2o` through `Nalidixic_Acid_Sodium_Salt`: exited 0 and left
  `reports/instance_validation_failures.tsv` header-only.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-parent
  record.

## Evidence

- A fresh OLS4 search for `sodium dihydrogenphosphate monohydrate` resolves the
  exact active term `CHEBI:114249`; direct lookup of that term lists CAS
  `10049-21-5`, formula `H2O.H2O4P.Na`, and the monohydrate InChI and SMILES.
- A fresh PubChem CAS lookup for `10049-21-5` resolves to sodium phosphate,
  monobasic, monohydrate with the same InChI as `CHEBI:114249`.
- Major: the active record still uses `cas:10049-21-5` as its identifier and
  publishes `skos:narrowMatch CHEBI:37585`; because a form-specific CHEBI term
  exists, MAPPING_SEMANTICS Section 3 calls for exact grounding to the hydrate
  term instead of a CAS-primary parent mapping.
- Major: final SSSOM `other` publishes `NaH2PO4 x 2 H2O`, a dihydrate sibling,
  plus a catalog-decorated monohydrate source label. Neither is a clean synonym
  for the monohydrate record.

## Completeness

- The record preserved the monohydrate/anhydrous distinction and has the
  required exact CAS and `kgmicrobe.compound` sibling rows for the current
  parent mapping.
- The record is incomplete now that `CHEBI:114249` can supply an exact
  ontology identity, formula, InChI, SMILES, and CAS xref.

## Recommended Edits

- Major: reground `data/ingredients/mapped/Nah2po4h2o.yaml` to
  `CHEBI:114249` `sodium dihydrogenphosphate monohydrate`, replace the CAS/local
  registry SSSOM rows with the normal exact CHEBI row, and populate the
  CHEBI-backed monohydrate chemistry.
- Major: reject or delete the dihydrate and catalog-decorated active synonyms
  before regenerating final SSSOM.
