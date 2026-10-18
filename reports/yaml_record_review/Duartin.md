# `data/ingredients/mapped/Duartin.yaml`

## Verdict

Pass with minor issues. The CultureBotHT CAS identity is preserved as a local
`cas:52305-04-1` record, the broad MeSH parent resolves exactly to `duartin`,
and the local/CAS/MeSH final SSSOM rows preserve the narrow CAS subject. The
MeSH parent row still carries a stale `UNKNOWN_TERM` validation stamp from the
older CHEBI-focused review dispatcher.

## Identity

- Reviewed record: `data/ingredients/mapped/Duartin.yaml`.
- Identifier and grounding: `identifier: cas:52305-04-1` with
  `ontology_mapping.ontology_id: mesh:C087989`, source `MESH`,
  `mapping_quality: NARROW_MATCH`, `mapping_status: MAPPED`,
  `ingredient_type: SINGLE_INGREDIENT`, and 0/0 CultureMech occurrences.
- Prefix-specific EBI OLS search resolves `mesh:C087989` to active `duartin`
  with a systematic isoflavan synonym.
- PubChem did not resolve CAS `52305-04-1`, and no exact ChEBI entry is present
  in this record's curation history; the CAS-backed local identity is therefore
  still needed.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Dry_Cow-manure.yaml data/ingredients/mapped/Duartin.yaml data/ingredients/mapped/Durhamycin.yaml data/ingredients/mapped/Dynemicin.yaml data/ingredients/mapped/Dyv_Metal_Solution.yaml`:
  exited 0 for the 5-file batch.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Dry_Cow-manure.yaml data/ingredients/mapped/Dynemicin.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed the ENVO and NCIT files. Duartin, Durhamycin, and DYV Metal Solution
  were skipped because they use `mesh:`, `cas:`, or local `kgmicrobe.*`
  identifiers outside this subset.
- Prefix-specific `curl -L 'https://www.ebi.ac.uk/ols4/api/search?q=mesh:C087989&ontology=mesh'`:
  resolved `mesh:C087989` to active `duartin`.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.
- `uv run --frozen python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`:
  passed; all id-label pairs corresponded, with only full-corpus plausibility
  warnings.

## Evidence

- `data/curated/mapped_ingredients.yaml` contains the same maintained record
  body as the per-record YAML.
- A hidden/ignored-inclusive exact search over `data/ingredients` and
  `mappings` for `52305-04-1` and `mesh:C087989` found the active Duartin YAML,
  stale row-review rows, expected `UNKNOWN_TERM` triage for the MeSH, CAS, and
  local registry rows, the external-prefix OLS validation row, and the final
  SSSOM rows.
- `mappings/ingredient_mappings_external_prefix_ols_validation.tsv` records
  `mesh:C087989` as `RESOLVED_EXACT_CURIE` with exact label `duartin`.
- The final `mappings/ingredient_mappings.sssom.tsv` rows keep the MeSH parent
  as `skos:narrowMatch` and the CAS and local registry identities as
  `skos:exactMatch`.
- Minor: the final MeSH SSSOM row still has `validation_method` of
  `none|UNKNOWN_TERM|2026-07-07`, inherited from the older synonym-review
  dispatcher that lacked full prefix coverage.

## Completeness

- CAS RN, CultureBotHT provenance, MeSH parent evidence, and expected local
  registry rows are populated.
- Formula and structure fields are correctly empty while no exact ChEBI term is
  available.
- Occurrences, supplied forms, mixture components, nutritional roles,
  physicochemical roles, biological roles, and environmental contexts are
  correctly empty.

## Recommended Edits

- Minor: refresh the Duartin MeSH SSSOM validation metadata from
  `mappings/ingredient_mappings_external_prefix_ols_validation.tsv` so the final
  MeSH parent row no longer reports `UNKNOWN_TERM`.
