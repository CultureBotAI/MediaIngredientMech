# MediaIngredientMech backlog-loop addendum

Read this after `backlog-loop-goal.md`.

- `just qc` does not include the blocking id-label product validation; run
  `just validate-products` for changes that can affect grounded identifiers.
- Changes under `data/ingredients/`, `data/curated/`, `data/custom/`, or
  `mappings/` need an append-only record created with `just new-history`.
- Rebuild every tracked published artifact affected by a source-record change.
- Large YAML diffs must be characterized by records and fields; do not accept
  or reject them from line count alone.
