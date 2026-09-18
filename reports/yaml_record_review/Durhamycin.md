# `data/ingredients/mapped/Durhamycin.yaml`

## Verdict

Needs curation. The local `kgmicrobe.compound:durhamycin` identity is still the
right placeholder for a family-level source label with only A/B variant
candidates in external ontologies, but the `SELECTIVE_AGENT` role is still only
a provisional name-list inference.

## Identity

- Reviewed record: `data/ingredients/mapped/Durhamycin.yaml`.
- Identifier and grounding: `identifier: kgmicrobe.compound:durhamycin` with
  `ontology_mapping.ontology_id: kgmicrobe.compound:durhamycin`, source
  `kgmicrobe.compound`, `mapping_quality: PLACEHOLDER`,
  `mapping_status: MAPPED`, and `ingredient_type: SINGLE_INGREDIENT`.
- A fresh OLS search for `Durhamycin` across ChEBI, MeSH, and NCIT returned
  only durhamycin A and durhamycin B variant terms, so the family-level local
  placeholder is still justified.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Dry_Cow-manure.yaml data/ingredients/mapped/Duartin.yaml data/ingredients/mapped/Durhamycin.yaml data/ingredients/mapped/Dynemicin.yaml data/ingredients/mapped/Dyv_Metal_Solution.yaml`:
  exited 0 for the 5-file batch.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Dry_Cow-manure.yaml data/ingredients/mapped/Dynemicin.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed the ENVO and NCIT files. Duartin, Durhamycin, and DYV Metal Solution
  were skipped because they use `mesh:`, `cas:`, or local `kgmicrobe.*`
  identifiers outside this subset.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.
- `uv run --frozen python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`:
  passed; all id-label pairs corresponded, with only full-corpus plausibility
  warnings.

## Evidence

- `data/curated/mapped_ingredients.yaml` contains the same maintained record
  body as the per-record YAML.
- `mappings/ingredient_mappings_unknown_term_manual_candidate_review.tsv`
  records `NO_IDENTITY_PROMOTION` because `CHEBI:65814` durhamycin A and
  `CHEBI:65815` durhamycin B are specific variants while the source label is
  family-level.
- A hidden/ignored-inclusive exact search over `data/ingredients` and
  `mappings` for `kgmicrobe.compound:durhamycin` found the active Durhamycin
  YAML, expected local-placeholder triage rows, the manual candidate review,
  and the final SSSOM row.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:Durhamycin` to local `kgmicrobe.compound:durhamycin` with
  `skos:exactMatch`, local object source, and no `other` tokens.
- Major: `physicochemical_roles.SELECTIVE_AGENT` has only
  `COMPUTATIONAL_PREDICTION` evidence from `infer_roles_from_name_lists` and a
  provisional curator note. It is not source-backed.

## Completeness

- Placeholder-retention evidence and the current no-exact-candidate context are
  populated.
- CAS RN, structure fields, occurrences, supplied forms, mixture components,
  nutritional roles, biological roles, and environmental contexts are correctly
  empty.

## Recommended Edits

- Major: replace the `SELECTIVE_AGENT` computational role in
  `data/ingredients/mapped/Durhamycin.yaml` with source-backed role evidence
  scoped to durhamycin, or remove the role if no support is available; then
  synchronize `data/curated/mapped_ingredients.yaml`.
