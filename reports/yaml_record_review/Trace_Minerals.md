# `data/ingredients/mapped/Trace_Minerals.yaml`

## Verdict

Needs curation, major. The local trace-mineral stock/pre-mix identity is
synchronized, but `see below` and starred raw source labels leak into final
SSSOM `other`.

## Identity

- Reviewed record: `data/ingredients/mapped/Trace_Minerals.yaml`.
- Identifier and grounding: `identifier:
  kgmicrobe.ingredient:trace_minerals` with matching
  `ontology_mapping.ontology_id`, label `Trace minerals`, source
  `kgmicrobe.ingredient`, `mapping_quality: FALLBACK_REGISTRY`,
  `mapping_status: MAPPED`, `ingredient_type: STOCK_SOLUTION`, and
  `solution_type: TRACE_METAL_MIX`.
- Synonyms: raw mim-queue source form plus raw CultureMech forms `Trace
  minerals (see below)` and `Trace minerals*`.
- Occurrences: 3 CultureMech recipe occurrences in 3 media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Trace_Mineral_Solution` through `Trans-aconitic_Acid`: exited 0 and wrote
  zero ERROR rows.
- Direct old Engine A/OBO term validation was skipped for this row because
  `kgmicrobe.ingredient` is a non-OBO local registry prefix.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- The May review rejected identity to the broad MeSH `Trace Elements` class,
  and the August issue 288 curation minted a local identity for this
  trace-mineral stock/pre-mix.
- The final SSSOM row has
  `MIM:Trace_Minerals skos:exactMatch kgmicrobe.ingredient:trace_minerals`
  and exports `Trace minerals (see below)|Trace minerals*` in `other`.

## Issues

### Major: recipe notes reach final `other`

Both final `other` tokens are raw CultureMech occurrence labels. `see below`
is a recipe cross-reference and `*` is a footnote marker, so neither is a true
synonym of the local stock identity.

## Completeness

- The local identity, fallback registry mapping, occurrence count, aggregate
  copy, and final exact row agree.
- No roles, components, parent ontology rows, or chemical properties are
  asserted.
- The only issue is the leaked raw CultureMech aliases.

## Recommended Edits

- Mark `Trace minerals (see below)` and `Trace minerals*` as non-exportable raw
  source text so the final SSSOM `other` column is empty for this row.
