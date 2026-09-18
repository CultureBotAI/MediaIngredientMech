# `data/ingredients/mapped/Trace_Metal_Solution.yaml`

## Verdict

Needs curation, major. The local stock-solution identity is synchronized, but
the final SSSOM row exports a starred recipe-local alias as a synonym.

## Identity

- Reviewed record: `data/ingredients/mapped/Trace_Metal_Solution.yaml`.
- Identifier and grounding: `identifier:
  kgmicrobe.ingredient:trace_metal_solution` with matching
  `ontology_mapping.ontology_id`, label `Trace metal solution`, source
  `kgmicrobe.ingredient`, `mapping_quality: FALLBACK_REGISTRY`,
  `mapping_status: MAPPED`, and `ingredient_type: STOCK_SOLUTION`.
- Synonyms: raw mim-queue source form plus raw CultureMech source form
  `Trace metal solution*`.
- Occurrences: 2 CultureMech recipe occurrences in 2 media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Trace_Element_Solution_SL-10` through `Trace_Metals_Solution`: exited 0 and
  wrote zero ERROR rows.
- Direct old Engine A/OBO term validation was skipped for this row because
  `kgmicrobe.ingredient` is a non-OBO local registry prefix.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- The August issue 288 curation minted a local `kgmicrobe.ingredient` identity
  after searching ChEBI, NCIT, MeSH, FOODON, and ENVO and retaining no parent
  because a generic trace-metal solution is a named multi-component
  preparation.
- The final SSSOM row has
  `MIM:Trace_Metal_Solution skos:exactMatch
  kgmicrobe.ingredient:trace_metal_solution` and exports `Trace metal
  solution*` in `other`.

## Issues

### Major: the starred source form reaches final SSSOM

`Trace metal solution*` is a CultureMech occurrence label with a footnote
marker, not a true synonym of the local stock identity. The marker should be
retained only as source provenance and filtered from final `other`.

## Completeness

- The local identity, fallback registry mapping, occurrence count, aggregate
  copy, and final exact row agree.
- No roles, components, parent ontology rows, or chemical properties are
  asserted.
- The only issue is the leaked starred alias.

## Recommended Edits

- Mark `Trace metal solution*` as non-exportable raw source text so the final
  SSSOM `other` column is empty for this row.
