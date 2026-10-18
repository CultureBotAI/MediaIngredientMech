# `data/ingredients/mapped/Candiplanecin.yaml`

## Verdict

Needs curation, minor. The former local placeholder was correctly upgraded to
exact MeSH `mesh:C033379` candiplanecin and publishes a valid SSSOM row, but
one ontology-mapping evidence note still describes the pre-upgrade placeholder
state as pending curator promotion.

## Identity

- Reviewed record: `data/ingredients/mapped/Candiplanecin.yaml`.
- Identifier and grounding: `identifier: mesh:C033379`,
  `ontology_mapping.ontology_id: mesh:C033379`,
  `ontology_label: candiplanecin`, `ontology_source: MESH`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Direct MeSH OLS search returns exact CURIE `mesh:C033379` with label
  `candiplanecin`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Candiplanecin.yaml data/ingredients/mapped/Cantharidin.yaml data/ingredients/mapped/Capecitabine.yaml data/ingredients/mapped/Capreomycin.yaml data/ingredients/mapped/Caproic_Acid.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Candiplanecin.yaml data/ingredients/mapped/Cantharidin.yaml data/ingredients/mapped/Capecitabine.yaml data/ingredients/mapped/Capreomycin.yaml data/ingredients/mapped/Caproic_Acid.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed all 5 files.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip.GkFQqh`
  followed by
  `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip.GkFQqh`:
  passed; both curated collection files had 0 data differences and only the
  expected scratch `generation_date` metadata differences.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K. Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- The 2026-05-01 `AUTO_UPGRADE_TO_MESH` event records the label-exact
  replacement of `kgmicrobe.compound:candiplanecin` with `mesh:C033379`.
- Hidden/ignored-inclusive search over `data/curated`, `mappings`,
  `docs/data`, and `reports`, excluding bulky backups and generated
  review-report directories, found the active `MIM:Candiplanecin` SSSOM row,
  matching aggregate/docs rows, and
  `mappings/ingredient_mappings_unknown_term_triage.tsv`, which classifies the
  old `UNKNOWN_TERM` row as missing MeSH validator-prefix coverage.
- The first `ontology_mapping.evidence` entry is stale: it still says the
  record uses kg-microbe's local placeholder with no OLS hits and is pending
  promotion, even though the second evidence entry and current mapping are
  exact MeSH.

## Completeness

- The exact MeSH identifier, mapping evidence, aggregate copy, SSSOM row, docs
  row, and label-index row are present.
- No CAS, formula, chemical structure, component list, or media role is
  asserted.

## Recommended Edits

- In `data/ingredients/mapped/Candiplanecin.yaml`, remove the stale
  `kgmicrobe.compound` placeholder evidence note or rewrite it as historical
  source-label provenance that no longer claims promotion is pending.
- Regenerate aggregate/docs outputs and prove the cleanup with strict
  validation and round-trip verification.
