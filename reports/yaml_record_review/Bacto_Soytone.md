# `data/ingredients/mapped/Bacto_Soytone.yaml`

## Verdict

Needs curation; severity minor. This is correctly marked as a rejected
tombstone for the obsolete `CHEBI:8150` loser that was merged into the live
`FOODON:03315720` Soy peptone representative, but `kg_microbe_node_id` still
points at obsolete `CHEBI:8150` after the identifier was repointed.

## Identity

- Reviewed record: `data/ingredients/mapped/Bacto_Soytone.yaml`.
- Tombstone state: `mapping_status: REJECTED`, `identifier: FOODON:03315720`,
  `representative: FOODON:03315720`, and
  `ontology_mapping.ontology_id: FOODON:03315720` with
  `ontology_label: vegetable protein, hydrolyzed`.
- OLS exact search in `foodon` resolves `FOODON:03315720` to
  `vegetable protein, hydrolyzed`.
- Hidden/ignored-inclusive search of `mappings/ingredient_mappings.sssom.tsv`
  found no `MIM:Bacto_Soytone` row; the live `MIM:Soy_Peptone` row carries
  `Bacto Soytone` as an alias.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Bacto-tryptone.yaml data/ingredients/mapped/Bacto_Brain_Heart_Infusion.yaml data/ingredients/mapped/Bacto_Peptone.yaml data/ingredients/mapped/Bacto_Soytone.yaml data/ingredients/mapped/Bacto_Tryptic_Soy_Agar.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Bacto_Soytone.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- OLS exact search for `FOODON:03315720` confirmed the live representative term.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed;
  2951 records, 83 decompositions, 505 components, 0 violations.
- `uv run --frozen python scripts/audit_kg_microbe_node_ids.py --check` passed
  the same-prefix gate but reports this record as a cross-prefix mismatch:
  `identifier: FOODON:03315720` versus `kg_microbe_node_id: CHEBI:8150`.

## Evidence

- Hidden/ignored-inclusive searches over `data/curated`, `mappings`, and
  `data/custom`, excluding `data/curated/backups`, found the aggregate copy,
  the kg-microbe node-id mismatch report, and the live `Soy_Peptone` SSSOM
  alias row.
- The curation history records the obsolete `CHEBI:8150` cleanup, the merge
  into Soy peptone, and the 2026-08-15 identifier repointing to the first live
  representative.
- Zeroed 0/0 occurrence counts are expected for this rejected tombstone because
  occurrences were transferred to the representative in the preceding merge.

## Completeness

- The rejection status, representative pointer, replacement FOODON target, and
  aggregate copy are populated.
- No dedicated SSSOM row should be exported for this tombstone.
- The stale `kg_microbe_node_id` is the only consequential leftover in the
  checked fields.

## Recommended Edits

- Clear or repoint `kg_microbe_node_id` on
  `data/ingredients/mapped/Bacto_Soytone.yaml`, synchronize
  `data/curated/mapped_ingredients.yaml`, and rerun focused strict validation,
  `scripts/audit_kg_microbe_node_ids.py --check`, SSSOM invariants, and
  flat-export coverage.
