# `data/ingredients/mapped/Wolfes_Mineral_Mix_minus_Nitrilotriacetic_acid.yaml`

## Verdict

Needs curation. The local fallback identity and aggregate row agree, but the
record preserves a raw underscore-delimited source label in both
`preferred_term` and `ontology_mapping.ontology_label`, and the malformed label
is published in the final SSSOM row.

## Identity

- Reviewed record:
  `data/ingredients/mapped/Wolfes_Mineral_Mix_minus_Nitrilotriacetic_acid.yaml`.
- Identifier and grounding:
  `identifier: kgmicrobe.ingredient:wolfes_mineral_mix_minus_nitrilotriacetic_acid`
  with matching `ontology_mapping.ontology_id`, source `kgmicrobe.ingredient`,
  `mapping_quality: FALLBACK_REGISTRY`, and `mapping_status: MAPPED`.
- Published label: `Wolfe's mineral mix_minus_Nitrilotriacetic_acid`.
- `ingredient_type: STOCK_SOLUTION` and `solution_type: MINERAL_STOCK`.
- Synonyms: one raw CultureBotHT surface form,
  `Wolfe's mineral mix_minus_Nitrilotriacetic_acid`.
- Occurrences: one CultureBotHT media occurrence.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Wc_Trace_Elements_Solution` through
  `Wolfes_Mineral_Mix_minus_Nitrilotriacetic_acid`: exited 0 and wrote zero
  ERROR rows.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.
- Engine A label validation was limited to the CHEBI-primary record in this
  batch; this local `kgmicrobe.ingredient` row has no OBO adapter for that
  focused check.

## Evidence

- The `#114` curation history records this as a named multi-component
  preparation that had no exact CHEBI, NCIT, MeSH, FOODON, or ENVO term and
  should keep a local fallback identifier.
- The final SSSOM row has
  `MIM:Wolfes_Mineral_Mix_minus_Nitrilotriacetic_acid skos:exactMatch
  kgmicrobe.ingredient:wolfes_mineral_mix_minus_nitrilotriacetic_acid`, but its
  subject and object labels both contain
  `Wolfe's mineral mix_minus_Nitrilotriacetic_acid`.

## Issues

- Major: the public preferred label and local ontology label retain raw
  underscores from the CultureBotHT surface form. Those underscores make the
  exact local row look like a source identifier fragment rather than a curated
  human label.

## Completeness

- The local exact identity, stock-solution classification, aggregate copy, and
  occurrence count agree.

## Recommended Edits

- Normalize the preferred term and local ontology label to a readable surface
  such as `Wolfe's mineral mix minus nitrilotriacetic acid`.
- Rebuild SSSOM and rerun strict validation plus SSSOM invariant validation.
