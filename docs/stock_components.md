# Recipe-level decomposition: `components` / `StockComponent`

## What it is
`IngredientRecord.components` is a list of `StockComponent` entries that decompose a
`STOCK_SOLUTION` or `DEFINED_MEDIUM` record into its constituent ingredients. It lets a
named mixture (e.g. a trace-element or vitamin solution) be resolved to its parts instead
of staying an opaque `UNMAPPED` mixture.

```yaml
- identifier: MICRO:0000455
  preferred_term: WC Trace Elements Solution
  ingredient_type: STOCK_SOLUTION
  components:
    - component_name: FeCl3 x 6 H2O      # required
      component_id: CHEBI:30808          # optional — omit when unmapped
      concentration_value: "1.5"         # optional — string preserves source formatting / ranges
      concentration_unit: G_PER_L        # optional
      source: "CultureMech:M278"         # provenance — keeps the recipe verifiable
    - component_name: H3BO3
      concentration_value: "0.01"
      concentration_unit: G_PER_L
```

`StockComponent` fields: `component_name` (**required**), `component_id`, `concentration_value`,
`concentration_unit`, `source`. The slot is optional and backwards-compatible — records
without it (i.e. all of them today) validate unchanged.

## Populating it — only from a verified source
**Do not fabricate recipes.** Populate `components` only from a verifiable source and record
that source in `component_id`/`source`. Suitable sources:
- a CultureMech medium that lists the solution's composition (the `solutions[].composition`
  array — see below),
- a MediaDive solution definition (by solution ID),
- a cited publication / DOI.

## Current status (2026-06-09)
This change adds the **schema + validation + tests + docs foundation** only — no records are
populated yet, because there is currently **no verifiable in-repo recipe for the
high-occurrence unmapped stock solutions** (Wolfe's vitamin/mineral mix, `Mc_*`, `P-IV`, …):
- CultureMech tracks `solutions[]` on media, but of **5314** solution entries only **5** have a
  non-empty `composition`, and **none of those 5 correspond to a MIM ingredient record**
  (they are `(see Medium [Mxxx])` references, not MIM records). The target solutions all have
  empty compositions.
- `mediadive_cache.sqlite` is a raw HTTP-response cache, not a queryable solution→ingredient
  table, and the unmapped records carry no MediaDive source_id to key on.

So population awaits a recipe source that maps to these records (a curator-provided recipe,
or a future CultureMech/MediaDive enrichment that fills `solutions[].composition`). When that
exists, write `components` from it; the `test_stock_components.py` guards keep the slot honest.
