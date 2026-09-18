# `data/ingredients/mapped/Tryptoneyeastbeef_(tyb).yaml`

## Verdict

Pass. The fallback registry identity, three-component decomposition, escaped
SSSOM subject alias, aggregate row, and final SSSOM row pass.

## Identity

- Reviewed record: `data/ingredients/mapped/Tryptoneyeastbeef_(tyb).yaml`.
- Identifier and grounding:
  `identifier: kgmicrobe.ingredient:tryptone_yeast_beef_tyb` with matching
  `ontology_mapping.ontology_id`, label `Tryptone/yeast/beef (tyb)`, source
  `kgmicrobe.ingredient`, `mapping_quality: FALLBACK_REGISTRY`,
  `mapping_status: MAPPED`, and `ingredient_type: UNDEFINED_MIXTURE`.
- Components: `tryptone` / `MICRO:0000182`, `yeast extract` /
  `FOODON:03315426`, and `beef extract` / `FOODON:03302088` as complete
  label-enumerated `MIM_CATALOG` parts.
- Occurrences: 1 MicrobeDecoder trait occurrence and no CultureMech recipe
  occurrences.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Tryptoneyeastbeef_(tyb)` through `Tuberactinamine_A`: exited 0 and wrote
  zero ERROR rows.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.
- Engine A label validation was limited to the CHEBI records in this batch;
  the `kgmicrobe.ingredient` fallback registry row has no OBO adapter for that
  focused check.

## Evidence

- The MicrobeDecoder source label explicitly lists the three retained
  top-level parts. The record correctly represents the blend through
  `components` rather than mapping it to only tryptone, only yeast extract, or
  only beef extract.
- The final SSSOM row publishes the escaped subject
  `MIM:Tryptoneyeastbeef_~28tyb~29` with exact object
  `kgmicrobe.ingredient:tryptone_yeast_beef_tyb`; `mappings/mim_curie_aliases.tsv`
  records the unescaped-to-escaped alias for the file stem.

## Issues

None.

## Completeness

- No concentrations are present in `components`, which is consistent with the
  source label naming a blend without proportions.
- A hidden/ignored-inclusive search across `mappings`, `data/curated`, and
  `reports` found no stale final SSSOM row for the unescaped parenthesized
  subject.

## Recommended Edits

None.
