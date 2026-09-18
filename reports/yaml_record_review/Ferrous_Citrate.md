# `data/ingredients/mapped/Ferrous_Citrate.yaml`

## Verdict

Pass with minor issues. The MeSH ferrous citrate identity resolves and the
final SSSOM row is a clean exact match with no synonym noise, but the record
still has stale import-era top-level notes and is missing
`ingredient_type: SINGLE_INGREDIENT`.

## Identity

- Reviewed record: `data/ingredients/mapped/Ferrous_Citrate.yaml`.
- Identifier and grounding: `identifier: mesh:C016600` with matching
  `ontology_mapping.ontology_id`, canonical label `monoferrous acid citrate`,
  source `MESH`, `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- The June 2026 id-label repair retained the source surface form `Ferrous
  citrate` in `preferred_term`/`synonyms` while correcting the structured
  ontology label to the canonical MeSH label.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Ferric_Iron.yaml data/ingredients/mapped/Ferric_Malate_Solution.yaml data/ingredients/mapped/Ferric_nitrilotriacetate.yaml data/ingredients/mapped/Ferrihydrite.yaml data/ingredients/mapped/Ferrous_Citrate.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Ferrous_Citrate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.

## Evidence

- The matching `data/curated/mapped_ingredients.yaml` entry carries the same
  MeSH identifier, exact mapping, source synonym, and refreshed occurrence
  counts as the per-record YAML.
- `mappings/ingredient_mappings_unknown_term_triage.tsv` records that the old
  OAK/OLS row-review `UNKNOWN_TERM` finding came from missing prefix coverage
  in the synonym-review dispatcher, not from a bad mapping; the same triage row
  says prefix-specific EBI OLS resolved `mesh:C016600`.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:Ferrous_Citrate` to `mesh:C016600` with `skos:exactMatch` and no
  `other` payload.
- Minor: the top-level `notes` still say "no CAS-RN or CHEBI/NCIT match.
  Curator review needed." That sentence is stale after the MeSH exact-match
  upgrade and label repair.
- Minor: this simple mapped chemical is missing
  `ingredient_type: SINGLE_INGREDIENT`.
- A hidden/ignored-inclusive search over `data/ingredients`, `data/curated`,
  `mappings`, `scripts`, `src`, `tests`, and `reports` for `Ferrous_Citrate`
  and `Ferrous citrate` found the active YAML, aggregate copy, final SSSOM row,
  unknown-term triage row, row-review provenance, old batch validation output,
  and ignored aggregate backups.

## Completeness

- The exact MeSH identity, canonical label, occurrence count, and final SSSOM
  row are populated.
- The record needs a current top-level note and an ingredient classification,
  but no component or environment claim is required.

## Recommended Edits

- Minor: set `ingredient_type: SINGLE_INGREDIENT` and replace the stale
  top-level `notes` in `data/ingredients/mapped/Ferrous_Citrate.yaml`, sync
  `data/curated/mapped_ingredients.yaml`, and rerun strict validation plus the
  roundtrip gate.
