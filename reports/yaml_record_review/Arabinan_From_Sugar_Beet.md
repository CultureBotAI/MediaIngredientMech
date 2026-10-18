# `data/ingredients/mapped/Arabinan_From_Sugar_Beet.yaml`

## Verdict

Needs curation. The CAS fallback identity and registry rows are internally
synchronized, but the FoodOn parent is not a valid broader term:
`FOODON:00003412` denotes a sugar-beet root, not arabinan extracted from sugar
beet.

## Identity

- Reviewed record:
  `data/ingredients/mapped/Arabinan_From_Sugar_Beet.yaml`.
- Active local identity: `identifier: cas:11078-27-6`, preferred term
  `Arabinan from Sugar Beet`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- `ontology_mapping` targets `FOODON:00003412` with label `sugar beet`,
  source `FOODON`, and `mapping_quality: NARROW_MATCH`.
- EBI OLS resolves `FOODON:00003412` to non-obsolete FoodOn `sugar beet` with
  a description of a primary root of `Beta vulgaris subsp. vulgaris`.
- PubChem's CAS-RN xref for `11078-27-6` resolves, but only to two
  formula-bearing CIDs with no `Arabinan from Sugar Beet` or `11078-27-6`
  synonym in the returned synonym payload.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Apramycin.yaml data/ingredients/mapped/Apramycin_Sulfate_Salt.yaml data/ingredients/mapped/Arabinan_From_Sugar_Beet.yaml data/ingredients/mapped/Arabinitol.yaml data/ingredients/mapped/Arabinobiose.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Arabinan_From_Sugar_Beet.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `curl -L https://www.ebi.ac.uk/ols4/api/ontologies/foodon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FFOODON_00003412`:
  resolved `FOODON:00003412` to non-obsolete `sugar beet`.
- `curl -L https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/xref/RN/11078-27-6/cids/JSON`:
  returned CIDs `156595897` and `163304491`.
- `curl -L https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/156595897,163304491/property/Title,MolecularFormula,CanonicalSMILES,InChI,InChIKey/JSON`:
  returned formulas and structures for both CAS-linked PubChem CIDs.
- `curl -L https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/156595897,163304491/synonyms/JSON`:
  returned `C48H80O34` and `YA46077` for CID `156595897` and no synonym payload
  for CID `163304491`.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed; 2951
  records, 83 decompositions, 505 components, 0 violations.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- `FOODON:00003412` was selected by a `stem-substring` backfill; the local
  row-review data marks the row as synonym-enrichment work rather than a
  curated chemical or material identity review.
- `mappings/ingredient_mappings.sssom.tsv` rows 453-455 publish a bad
  `skos:narrowMatch` from `MIM:Arabinan_From_Sugar_Beet` to sugar beet, plus
  exact CAS and kg-microbe registry rows for the local CAS fallback identity.
- `mappings/ingredient_mappings_row_review_manifest.tsv` already classified
  the CAS and kg-microbe rows as expected registry identifiers.
- A hidden, ignored-inclusive search across the full checkout, excluding the
  old `data/curated/backups` snapshots and noncanonical batch-review output,
  found the active YAML, aggregate copy, SSSOM rows, row-review rows, generated
  docs, and no hidden CultureBotHT raw row for `11078-27-6`.

## Completeness

- CAS, curation history, SSSOM registry rows, and the aggregate copy are
  populated.
- Source occurrence counts are intentionally zero because this is a CultureBotHT
  CAS fallback rather than a media recipe ingredient.
- Formula, structure, roles, component, environmental context, discussion, and
  dataset entries are correctly absent until the arabinan identity has a
  defensible parent or exact external grounding.

## Recommended Edits

- In `data/ingredients/mapped/Arabinan_From_Sugar_Beet.yaml`, remove
  `FOODON:00003412` as the ontology parent and either ground CAS `11078-27-6`
  to an exact chemical/material term or keep the CAS and kg-microbe identity
  rows without an unrelated FoodOn parent.
- Regenerate synchronized products, then rerun
  `uv run --frozen python scripts/validate_strict.py`,
  `uv run linkml-term-validator validate-data data/ingredients/mapped/Arabinan_From_Sugar_Beet.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`,
  and `uv run --frozen python scripts/validate_sssom_invariants.py`.
