# `data/ingredients/mapped/Bottromycin.yaml`

## Verdict

Needs curation, minor. The exact generic `mesh:C024712` bottromycin identity,
MicrobeDecoder source occurrence, SSSOM row, and aggregate copy agree, but
top-level `notes` and one evidence sentence still reflect the old unmapped
state.

## Identity

- Reviewed record: `data/ingredients/mapped/Bottromycin.yaml`.
- Identifier and grounding: `identifier: mesh:C024712` with
  `ontology_mapping.ontology_id: mesh:C024712`,
  `ontology_label: bottromycin`, `ontology_source: MESH`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Live OLS exact search for `Bottromycin` returns `mesh:C024712` for the
  generic bottromycin label. The same search also returns specific ChEBI
  bottromycin congener terms, but not a generic ChEBI term that supersedes the
  MeSH mapping.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Bottromycin.yaml data/ingredients/mapped/Bovine_Albumin.yaml data/ingredients/mapped/Bovine_Calf_Serum.yaml data/ingredients/mapped/Bovine_Serum_Albumin.yaml data/ingredients/mapped/Brain_Heart_Infusion.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Bottromycin.yaml data/ingredients/mapped/Bovine_Serum_Albumin.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for the MESH/NCIT-backed records in this batch. The three MICRO-backed
  records are intentionally covered outside Engine A.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K. Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- Hidden/ignored-inclusive search over `data/curated`, `mappings`,
  `data/custom`, and `reports`, excluding `data/curated/backups` and generated
  review directories, found the MicrobeDecoder raw label in
  `data/custom/microbedecoder/unmapped_labels.tsv`, the authoritative exact
  SSSOM row at `mappings/ingredient_mappings.sssom.tsv` row 621, and the
  aggregate copy in `data/curated/mapped_ingredients.yaml`.
- The local SSSOM row maps `MIM:Bottromycin` to `mesh:C024712` with
  `skos:exactMatch`, matching the primary `identifier` and
  `ontology_mapping`.
- A parsed comparison against `data/curated/mapped_ingredients.yaml` found
  exactly one aggregate record with the same identifier and preferred term, and
  it is identical to this per-record YAML.

## Completeness

- The exact generic MeSH identifier, MicrobeDecoder source occurrence, SSSOM
  row, and aggregate copy are populated.
- Minor gap: top-level `notes` still say curator review was needed, and
  `ontology_mapping.evidence` still says bottromycin is absent from ChEBI even
  though current OLS exposes specific ChEBI congener terms.

## Recommended Edits

- Minor: update `data/ingredients/mapped/Bottromycin.yaml` to replace the stale
  top-level import note and narrow the active evidence from "absent from CHEBI"
  to "no generic ChEBI bottromycin term"; then run `just sync-curated` and
  focused strict/term validation.
