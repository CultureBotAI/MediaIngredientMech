# `data/ingredients/mapped/Ardacin_A.yaml`

## Verdict

Pass. The record keeps a distinct `kgmicrobe.compound:ardacin_a` identity,
anchors it to the generic NCIT `Ardacin` class with a non-identity
`NARROW_MATCH`, and emits the required kg-microbe registry row.

## Identity

- Reviewed record: `data/ingredients/mapped/Ardacin_A.yaml`.
- Active local identity: `identifier: kgmicrobe.compound:ardacin_a`,
  preferred term `Ardacin A`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- `ontology_mapping` targets `NCIT:C169786` with label `Ardacin`, source
  `NCIT`, and `mapping_quality: NARROW_MATCH`.
- Local OAK resolves `NCIT:C169786` to non-obsolete NCIT `Ardacin`, CAS
  `117742-13-9`, UNII `Z01YSQ279Y`, and exact synonyms `Ardacin` and
  `ARDACIN`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Arbutin.yaml data/ingredients/mapped/Ardacin_A.yaml data/ingredients/mapped/Ardacin_B.yaml data/ingredients/mapped/Ardacin_C.yaml data/ingredients/mapped/Arecoline_Hydrobromide.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Ardacin_A.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen runoak -i sqlite:obo:ncit term-metadata NCIT:C87429 NCIT:C169786`:
  returned CAS and UNII metadata for `NCIT:C169786`.
- `uv run --frozen runoak -i sqlite:obo:ncit aliases NCIT:C87429 NCIT:C169786`:
  returned the canonical `Ardacin` label and exact NCIT synonyms for
  `NCIT:C169786`.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed; 2951
  records, 83 decompositions, 505 components, 0 violations.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- The curation history preserves the kg-microbe placeholder source,
  low-confidence initial OLS search, and later NCIT backfill.
- `mappings/ingredient_mappings.sssom.tsv` rows 467-468 publish the
  `skos:narrowMatch` to NCIT `Ardacin` plus an exact registry row for
  `kgmicrobe.compound:ardacin_a`.
- `mappings/ingredient_mappings_unknown_term_triage.tsv` classified the
  `NCIT:C169786` UNKNOWN_TERM result as a missing prefix-validator coverage
  issue and the kg-microbe row as an expected registry identifier.
- A hidden, ignored-inclusive search across the full checkout, excluding the
  old `data/curated/backups` snapshots and noncanonical batch-review output,
  found the active YAML, aggregate copy, generated docs, SSSOM rows, and
  row-review rows.

## Completeness

- The local kg-microbe identity, NCIT parent, curation history, `ingredient_type`,
  SSSOM registry row, and aggregate copy are populated.
- Source occurrence counts are intentionally zero because this is a kg-microbe
  placeholder import rather than a media recipe ingredient.
- No role, component, chemical property, environmental context, discussion, or
  dataset entry is needed.

## Recommended Edits

- None.
