# `data/ingredients/mapped/Arabinoxylan_Rye_Flour.yaml`

## Verdict

Needs curation. The record exactly maps the `Arabinoxylan (Rye Flour)` label to
FoodOn `rye flour`; rye flour is a source material, not the extracted
arabinoxylan ingredient, so the active identifier and SSSOM exactMatch denote
the wrong material.

## Identity

- Reviewed record:
  `data/ingredients/mapped/Arabinoxylan_Rye_Flour.yaml`.
- Identifier and grounding: `identifier: FOODON:03302492` with
  `ontology_mapping.ontology_id: FOODON:03302492`, `ontology_source: FOODON`,
  `mapping_quality: LEXICAL_MATCH`, and `mapping_status: MAPPED`.
- EBI OLS resolves `FOODON:03302492` to non-obsolete FoodOn `rye flour`, a
  finely ground seed product, not an arabinoxylan polysaccharide.
- The record carries no CAS, local registry identifier, component model, or
  chemical parent that preserves the arabinoxylan identity.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Arabinogalactan.yaml data/ingredients/mapped/Arabinose.yaml data/ingredients/mapped/Arabinotriose.yaml data/ingredients/mapped/Arabinoxylan_Rye_Flour.yaml data/ingredients/mapped/Arabitol.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Arabinoxylan_Rye_Flour.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `curl -L https://www.ebi.ac.uk/ols4/api/ontologies/foodon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FFOODON_03302492`:
  resolved `FOODON:03302492` to non-obsolete `rye flour`.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed; 2951
  records, 83 decompositions, 505 components, 0 violations.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- The mapping came from `resolve_unmapped_v2` with a stem-match strategy; the
  mapping evidence says it matched via `Arabinoxylan (Rye Flour)`, and the
  top-level `notes` still say curator review is needed.
- `mappings/ingredient_mappings.sssom.tsv` row 464 maps
  `MIM:Arabinoxylan_Rye_Flour` to `FOODON:03302492` with `skos:exactMatch`,
  collapsing the MIM subject to FoodOn `rye flour`.
- `mappings/ingredient_mappings_row_review_manifest.tsv` classified the
  synonym-enrichment row as already represented, but that only explains the
  review of proposed lexical variants; it does not make rye flour an exact
  match for arabinoxylan.
- The only `nutritional_roles` evidence cites `Inferred from curated media-role
  name pattern` and explicitly marks the carbon-source role as provisional.
- A hidden, ignored-inclusive search across the full checkout, excluding the
  old `data/curated/backups` snapshots and noncanonical batch-review output,
  found the active YAML, aggregate copy, generated docs, SSSOM row, row-review
  rows, and MIM CURIE alias row.

## Completeness

- The aggregate copy matches the per-record YAML, including the bad FoodOn
  exact identity, the stale review-needed note, and the unsupported
  carbon-source role.
- Source occurrence counts are intentionally zero because this is a CultureBotHT
  import rather than a media recipe ingredient.
- No component, environmental context, discussion, or dataset entry is needed
  until the ingredient identity is corrected.

## Recommended Edits

- In `data/ingredients/mapped/Arabinoxylan_Rye_Flour.yaml`, replace
  `FOODON:03302492` with an arabinoxylan-specific identity. If no exact
  rye-flour arabinoxylan term is available, keep a distinct local
  `kgmicrobe.ingredient:arabinoxylan_rye_flour` identity and relate it to an
  arabinoxylan parent rather than to rye flour.
- In the same maintained record, remove `nutritional_roles.CARBON_SOURCE`
  unless direct source evidence for Arabinoxylan from rye flour as a carbon
  source is attached to that role.
- Regenerate synchronized products, then rerun
  `uv run --frozen python scripts/validate_strict.py`,
  `uv run linkml-term-validator validate-data data/ingredients/mapped/Arabinoxylan_Rye_Flour.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`,
  and `uv run --frozen python scripts/validate_sssom_invariants.py`.
