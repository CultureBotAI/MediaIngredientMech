# `data/ingredients/mapped/6-deoxy-d-galactose.yaml`

## Verdict

Needs curation, major. The corrected surface form is
`6-deoxy-D-galactose`, but the record maps it to the narrower
`CHEBI:2179` pyranose child instead of the exact `CHEBI:28847` D-fucose term.

## Identity

- Reviewed record: `data/ingredients/mapped/6-deoxy-d-galactose.yaml`.
- Identifier and grounding: `identifier: CHEBI:2179` with
  `ontology_mapping.ontology_id: CHEBI:2179`, source `CHEBI`,
  `mapping_quality: SYNONYM_MATCH`, and `mapping_status: MAPPED`.
- The official ChEBI page resolves `CHEBI:2179` to `D-fucopyranose`, defined in
  local OAK metadata as the six-membered ring form of D-fucose.
- Local OAK metadata resolves `CHEBI:28847` to `D-fucose` and lists
  `6-deoxy-D-galactose` as an exact synonym.
- The record's stored formula, SMILES, InChI, and molecular weight match
  `CHEBI:2179`, not the broader exact D-fucose identity that the source label
  names.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/6-O-Acetyl-D-glucose.yaml data/ingredients/mapped/6-O-sialyllactose_Sodium_Salt.yaml data/ingredients/mapped/6-Pentyl-2H-pyran-2-one.yaml data/ingredients/mapped/6-deoxy-d-galactose.yaml data/ingredients/mapped/6-hydroxypyridine-3-carboxylic_Acid.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/6-deoxy-d-galactose.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen runoak -i sqlite:obo:chebi aliases CHEBI:17901 CHEBI:26714 CHEBI:66729 CHEBI:2179 CHEBI:16168 CHEBI:28847`:
  returned `6-deoxy-D-galactose` as an exact synonym on `CHEBI:28847` and only
  as a related synonym on `CHEBI:2179`.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:17901 CHEBI:26714 CHEBI:66729 CHEBI:2179 CHEBI:16168 CHEBI:28847`:
  confirmed that `CHEBI:2179` denotes the pyranose form.

## Evidence

- The current ChEBI ID denotes a specific ring form and is narrower than the
  corrected source label `6-deoxy-D-galactose`.
- `CHEBI:28847` is the exact ChEBI term for D-fucose and carries
  `6-deoxy-D-galactose` as an exact synonym.
- The current SSSOM row exports an exact match from `MIM:6-deoxy-d-galactose`
  to `CHEBI:2179`; that exact substitution would force a pyranose form the
  source did not state.
- The source occurrence count is traceable to
  `data/custom/microbedecoder/unmapped_labels.tsv`, where
  `kgmicrobe.trait:6_deoxy_d_galactose` appears in
  `BacDive_Metabolite_utilization` with count 1.
- The hidden/ignored-inclusive search over `data`, `mappings`, `reports`,
  `scripts`, `tests`, and `src` found the active YAML, aggregate copy, SSSOM
  row, source microbedecoder row, stale advisory rows that already proposed
  `CHEBI:28847`, and ignored aggregate backups.

## Completeness

- The corrected preferred term and ingredient type are populated.
- Chemistry should be revisited during the regrounding, because the current
  structure block belongs to the pyranose child.

## Recommended Edits

- In `data/ingredients/mapped/6-deoxy-d-galactose.yaml`, reground the record
  from `CHEBI:2179` `D-fucopyranose` to `CHEBI:28847` `D-fucose`.
- Remove or replace the pyranose-specific `chemical_properties` block unless a
  verified structure for `CHEBI:28847` is available.
- Rebuild `mappings/ingredient_mappings.sssom.tsv` and
  `data/curated/mapped_ingredients.yaml`, then rerun strict validation, SSSOM
  invariants, and the id/label correspondence gate.
