# `data/ingredients/mapped/Trace_Metals_Solution.yaml`

## Verdict

Pass. The local `kgmicrobe.ingredient:trace_metals_solution` fallback
identity, stock-solution classification, occurrence count, aggregate row, and
final SSSOM row for this generic trace-metals stock placeholder are
synchronized.

## Identity

- Reviewed record: `data/ingredients/mapped/Trace_Metals_Solution.yaml`.
- Identifier and grounding: `identifier:
  kgmicrobe.ingredient:trace_metals_solution` with matching
  `ontology_mapping.ontology_id`, label `Trace Metals Solution`, source
  `kgmicrobe.ingredient`, `mapping_quality: FALLBACK_REGISTRY`,
  `mapping_status: MAPPED`, `ingredient_type: STOCK_SOLUTION`, and
  `solution_type: TRACE_METAL_MIX`.
- Synonyms: raw CultureMech source form `Trace Metals Solution`.
- Occurrences: 4 CultureMech recipe occurrences in 4 media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Trace_Element_Solution_SL-10` through `Trace_Metals_Solution`: exited 0 and
  wrote zero ERROR rows.
- Direct old Engine A/OBO term validation was skipped for this row because
  `kgmicrobe.ingredient` is a non-OBO local registry prefix.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- The issue 114 curation searched ChEBI, NCIT, MeSH, FOODON, and ENVO by label
  and synonym and minted a local `kgmicrobe.ingredient` identifier because the
  label is a lab preparation rather than one ontology substance.
- The final SSSOM row has
  `MIM:Trace_Metals_Solution skos:exactMatch
  kgmicrobe.ingredient:trace_metals_solution`, uses `kgm:ingredient`, and
  leaves `other` empty.

## Completeness

- The local stock-solution identity, occurrence count, aggregate copy, and
  final SSSOM row agree.
- No roles, parent ontology rows, components, or final synonym/export tokens
  require curation for the generic placeholder.

## Recommended Edits

- None.
