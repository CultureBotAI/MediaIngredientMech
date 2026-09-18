# `data/ingredients/mapped/Defibrinated_sheep_blood.yaml`

## Verdict

Pass. The record exact-maps defibrinated sheep blood to active
`MICRO:0001570`, uses the undefined-mixture classification expected for a
blood-product ingredient, and has a clean final SSSOM row plus a matching 25/25
CultureMech occurrence count.

## Identity

- Reviewed record: `data/ingredients/mapped/Defibrinated_sheep_blood.yaml`.
- Identifier and grounding: `identifier: MICRO:0001570` with
  `ontology_mapping.ontology_id: MICRO:0001570`,
  `ontology_label: defibrinated sheep blood`, `ontology_source: MICRO`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: UNDEFINED_MIXTURE`.
- Live OLS exact search in the `micro` ontology for `defibrinated sheep blood`
  returned one active result, `MICRO:0001570`, with label
  `defibrinated sheep blood`.
- `src/mediaingredientmech/curie.py` lists `MICRO:0001570` in the verified
  MICRO set and documents that it was checked as defining, non-obsolete, and
  round-tripping through the canonical OLS4 IRI for issue #260.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Defibrinated_sheep_blood.yaml data/ingredients/mapped/Delamanid.yaml data/ingredients/mapped/Delta-Decalactone.yaml data/ingredients/mapped/Delta-Dodecalactone.yaml data/ingredients/mapped/Delta-Nonalactone.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Defibrinated_sheep_blood.yaml data/ingredients/mapped/Delamanid.yaml data/ingredients/mapped/Delta-Decalactone.yaml data/ingredients/mapped/Delta-Dodecalactone.yaml data/ingredients/mapped/Delta-Nonalactone.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  failed on `MICRO:0001570` with the known local sqlite
  `rdfs_label_statement` lookup error before it reached the ChEBI records in
  this batch.
- `curl -L ... q=defibrinated sheep blood&ontology=micro&exact=true`: live OLS
  returned the exact `MICRO:0001570` row.
- `uv run --frozen python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`:
  passed; all id-label pairs corresponded, with only full-corpus plausibility
  warnings.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- `scripts/add_culturemech_gap_labels.py` is the maintained input that created
  this record and maps `Defibrinated sheep blood` to `MICRO:0001570`, distinct
  from `MICRO:0001230` `sheep blood`.
- The hidden/ignored-inclusive exact search over active `data/ingredients`,
  `data/curated`, `mappings`, `docs/data`, `src`, `scripts`, and `tests`
  found no second active per-record YAML for `MICRO:0001570`.
- The hidden/ignored-inclusive search of
  `mappings/culturemech_recipe_membership.tsv` found 25 `MICRO:0001570` rows
  with occurrence weights summing to 25, matching the explicit 25/25
  `occurrence_statistics`.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:Defibrinated_sheep_blood` to `MICRO:0001570` with
  `skos:exactMatch`, MICRO object source, empty `other`, and a manual curation
  validation stamp.

## Completeness

- The MICRO identity, undefined-mixture classification, occurrence count,
  membership rows, final SSSOM row, and generated docs rows are populated and
  agree.
- No chemical properties, CAS RN, component list, synonyms, or nutritional
  roles are asserted; leaving them empty is appropriate for this undefined
  blood-product mixture.

## Recommended Edits

- None.
