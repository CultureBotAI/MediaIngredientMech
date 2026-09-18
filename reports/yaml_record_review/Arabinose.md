# `data/ingredients/mapped/Arabinose.yaml`

## Verdict

Needs curation. The generic ChEBI arabinose identity, corrected CAS, formula,
CultureMech occurrences, carbon-source role, SSSOM row, and aggregate copy pass,
but two CultureMech role/property strings remain in `synonyms` and the
`ENERGY_SOURCE` role is still provisional.

## Identity

- Reviewed record: `data/ingredients/mapped/Arabinose.yaml`.
- Identifier and grounding: `identifier: CHEBI:22599` with
  `ontology_mapping.ontology_id: CHEBI:22599`, `ontology_source: CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Local OAK resolves `CHEBI:22599` to non-obsolete ChEBI `arabinose`, formula
  `C5H10O5`, CAS `147-81-9`, and exact synonym `arabino-pentose`.
- The stored `cas_rn: 147-81-9` matches ChEBI's xref and the curation history
  documents correction of the earlier EC/EINECS registry number.
- `ingredient_type: SINGLE_INGREDIENT` is present and fits the ChEBI molecular
  entity.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Arabinogalactan.yaml data/ingredients/mapped/Arabinose.yaml data/ingredients/mapped/Arabinotriose.yaml data/ingredients/mapped/Arabinoxylan_Rye_Flour.yaml data/ingredients/mapped/Arabitol.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Arabinose.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:27569 CHEBI:22599 CHEBI:62799 CHEBI:18403`:
  returned formula, CAS, and mass metadata for `CHEBI:22599`.
- `uv run --frozen runoak -i sqlite:obo:chebi aliases CHEBI:27569 CHEBI:22599 CHEBI:62799 CHEBI:18403`:
  returned the canonical `arabinose` label and exact `arabino-pentose` synonym
  for `CHEBI:22599`.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed; 2951
  records, 83 decompositions, 505 components, 0 violations.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- `mappings/culturemech_recipe_membership.tsv` has five
  `CHEBI:22599` memberships, matching `occurrence_statistics: 5/5`.
- `mappings/ingredient_mappings_oak_ols_review.tsv` confirmed the
  `MIM:Arabinose` to `CHEBI:22599` row, and
  `mappings/ingredient_mappings_row_review_manifest.tsv` records no mapping
  repair was needed.
- `mappings/ingredient_mappings.sssom.tsv` row 461 maps `MIM:Arabinose` to
  `CHEBI:22599` with `skos:exactMatch`, synonym `arabino-pentose`, CAS
  `147-81-9`, and a `CONFIRMED` row-review trailer.
- `nutritional_roles.CARBON_SOURCE` is backed by the imported CultureMech role
  text, but the two `RAW_TEXT` CultureMech synonym strings are role/property
  metadata, not ingredient labels.
- `nutritional_roles.ENERGY_SOURCE` cites only `Canonical energy substrate
  (catabolised for energy)` and marks itself provisional, so it lacks
  claim-level source evidence.
- A hidden, ignored-inclusive search across the full checkout, excluding the
  old `data/curated/backups` snapshots and noncanonical batch-review output,
  found the active YAML, aggregate copy, generated docs, SSSOM row, row-review
  rows, and CultureMech recipe-membership rows.

## Completeness

- CAS, formula, ChEBI identity, CultureMech occurrences, carbon-source role,
  curation history, `ingredient_type`, SSSOM, and the aggregate copy are
  populated.
- SMILES and InChI are absent because the generic ChEBI `arabinose` term does
  not expose a structure in the local OBO metadata.
- No component, environmental context, discussion, or dataset entry is needed.
- The bad raw synonym strings and unsupported energy-source role are the only
  consequential gaps.

## Recommended Edits

- In `data/ingredients/mapped/Arabinose.yaml`, remove the two
  `RAW_TEXT` CultureMech role/property strings from `synonyms`; keep their
  carbon-source content on `nutritional_roles.CARBON_SOURCE`.
- In the same maintained record, remove `nutritional_roles.ENERGY_SOURCE`
  unless direct source evidence for Arabinose as an energy source is attached
  to that role.
- Regenerate synchronized products, then rerun
  `uv run --frozen python scripts/validate_strict.py`,
  `uv run linkml-term-validator validate-data data/ingredients/mapped/Arabinose.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`,
  and `uv run --frozen python scripts/validate_sssom_invariants.py`.
