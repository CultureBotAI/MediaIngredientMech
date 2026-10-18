# `data/ingredients/mapped/Butamine.yaml`

## Verdict

Needs curation, minor. The fallback-registry identity, MicrobeDecoder
provenance, SSSOM row, and aggregate copy agree, but the top-level notes still
say curator review is needed after the record was promoted to a mapped
kg-microbe compound.

## Identity

- Reviewed record: `data/ingredients/mapped/Butamine.yaml`.
- Identifier and grounding: `identifier: kgmicrobe.compound:butamine` with
  `ontology_mapping.ontology_id: kgmicrobe.compound:butamine`,
  `ontology_label: Butamine`, `ontology_source: kgmicrobe.compound`,
  `mapping_quality: FALLBACK_REGISTRY`, and `mapping_status: MAPPED`.
- Live OLS exact search for `Butamine` returned no exact CHEBI, NCIT, FOODON,
  ENVO, MeSH, BTO, or UBERON term for this label; the only current OLS hit is
  the differently labeled MeSH term `mesh:C064506` for boroleucine.
- The fallback identifier therefore preserves the imported MicrobeDecoder label
  as a distinct kg-microbe compound rather than forcing an adjacent public
  ontology term.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Bromosuccinate.yaml data/ingredients/mapped/Bromothymol_Blue.yaml data/ingredients/mapped/Brucella_Agar.yaml data/ingredients/mapped/Brucine.yaml data/ingredients/mapped/Butamine.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Bromosuccinate.yaml data/ingredients/mapped/Bromothymol_Blue.yaml data/ingredients/mapped/Brucine.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for the three CHEBI-backed records in this batch.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K. Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- Hidden/ignored-inclusive search over `data/curated`, `mappings`,
  `data/custom`, and `reports`, excluding `data/curated/backups` and generated
  review directories, found the MicrobeDecoder candidate and unmapped-label
  provenance for `kgmicrobe.trait:butamine`, the authoritative fallback SSSOM
  row at `mappings/ingredient_mappings.sssom.tsv` row 637, a stale Edison
  advisory row agreeing with the fallback state, and the aggregate copy in
  `data/curated/mapped_ingredients.yaml`.
- The local SSSOM row maps `MIM:Butamine` to
  `kgmicrobe.compound:butamine` with `skos:exactMatch`,
  `object_source: kgm:compound`, and manual curation provenance, matching the
  primary `identifier` and `ontology_mapping`.
- A parsed comparison against `data/curated/mapped_ingredients.yaml` found
  exactly one aggregate record with the same identifier and preferred term, and
  it is identical to this per-record YAML.

## Completeness

- The kg-microbe fallback identifier, raw MicrobeDecoder label, source
  occurrence count, manual fallback provenance, SSSOM row, and aggregate copy
  are populated.
- Minor gap: top-level `notes` still preserve the original import text saying
  no CAS/CHEBI/NCIT match was found and curator review was needed, which is
  stale after the 2026-08-06 fallback-registry promotion.
- `occurrence_statistics.total_occurrences: 0` and `media_count: 0` are
  consistent with a MicrobeDecoder-only import that has no CultureMech recipe
  memberships.

## Recommended Edits

- Minor: update the maintained `notes` in
  `data/ingredients/mapped/Butamine.yaml` to describe the accepted
  fallback-registry decision, then run `just sync-curated` and focused
  strict/SSSOM validation.
