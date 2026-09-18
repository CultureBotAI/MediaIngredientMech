# `data/ingredients/mapped/Dry_Cow-manure.yaml`

## Verdict

Pass. The record now has its own local dry-cow-manure identity, is correctly
anchored as narrower than ENVO animal manure with a local registry exact row,
and the final SSSOM rows preserve that distinction.

## Identity

- Reviewed record: `data/ingredients/mapped/Dry_Cow-manure.yaml`.
- Identifier and grounding: `identifier: kgmicrobe.ingredient:dry_cow-manure`
  with `ontology_mapping.ontology_id: ENVO:00003031`, source `ENVO`,
  `mapping_quality: NARROW_MATCH`, `mapping_status: MAPPED`,
  `ingredient_type: UNDEFINED_MIXTURE`, and 5 CultureMech source occurrences.
- Local OAK resolves `ENVO:00003031` to active `animal manure`, defined as
  manure derived from animal waste products.
- The exact subject is narrower than ENVO animal manure and lacks an exact
  external ontology term, so the local `kgmicrobe.ingredient` mint is the
  maintained identity.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Dry_Cow-manure.yaml data/ingredients/mapped/Duartin.yaml data/ingredients/mapped/Durhamycin.yaml data/ingredients/mapped/Dynemicin.yaml data/ingredients/mapped/Dyv_Metal_Solution.yaml`:
  exited 0 for the 5-file batch.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Dry_Cow-manure.yaml data/ingredients/mapped/Dynemicin.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed the ENVO and NCIT files. Duartin, Durhamycin, and DYV Metal Solution
  were skipped because they use `mesh:`, `cas:`, or local `kgmicrobe.*`
  identifiers outside this subset.
- `uv run --frozen runoak -i sqlite:obo:envo term-metadata ENVO:00003031`:
  returned the canonical ENVO label and definition for `ENVO:00003031`.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.
- `uv run --frozen python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`:
  passed; all id-label pairs corresponded, with only full-corpus plausibility
  warnings.

## Evidence

- `data/curated/mapped_ingredients.yaml` contains the same maintained record
  body as the per-record YAML.
- The 2026-08-18 curation history records the false-positive FOODON repair, the
  ENVO animal-manure parent decision, and the local kg-microbe identity mint.
- A fresh OLS search of ENVO, AGRO, and FOODON for the exact cow-manure phrase
  found no exact external replacement.
- A hidden/ignored-inclusive exact search over `data/ingredients` and
  `mappings` for `kgmicrobe.ingredient:dry_cow-manure` and `ENVO:00003031`
  found the active record, expected generated membership rows, old research rows
  for the merged cow-manure tombstone, and the final SSSOM rows.
- The final `mappings/ingredient_mappings.sssom.tsv` rows map
  `MIM:Dry_Cow-manure` to `ENVO:00003031` with `skos:narrowMatch` and to
  `kgmicrobe.ingredient:dry_cow-manure` with `skos:exactMatch`.

## Completeness

- Local identity provenance, ENVO parent evidence, occurrence provenance, and
  the merged cow-manure surface are populated.
- CAS RN, chemical structure, mixture components, nutritional roles,
  physicochemical roles, biological roles, and environmental contexts are
  correctly empty.

## Recommended Edits

- None.
