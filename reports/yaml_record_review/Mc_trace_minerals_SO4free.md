# `data/ingredients/mapped/Mc_trace_minerals_SO4free.yaml`

## Verdict

Pass. The local sulfate-free trace-mineral-stock identity, exact component
transcription, trace-element evidence, occurrence count, and final SSSOM row
all pass.

## Identity

- Reviewed record: `data/ingredients/mapped/Mc_trace_minerals_SO4free.yaml`.
- Identifier and grounding:
  `identifier: kgmicrobe.ingredient:mc_trace_minerals_so4free` with matching
  `ontology_mapping.ontology_id`, label `Mc_trace_minerals_SO4free`, source
  `kgmicrobe.ingredient`, `mapping_quality: FALLBACK_REGISTRY`,
  `mapping_status: MAPPED`, `ingredient_type: STOCK_SOLUTION`, and
  `solution_type: TRACE_METAL_MIX`.
- Occurrences: 22 CultureBotHT media.
- Components: 12 sulfate-free trace-mineral stock constituents.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Mc_general_salts_SO4free` through `Meat_Extract`: exited 0 and wrote zero
  ERROR rows.
- Engine A term validation was skipped for this record because
  `kgmicrobe.ingredient` is a local non-OBO registry prefix covered by the
  product id-label validator rather than by `linkml-term-validator`.

## Evidence

- The FEBA media definitions Google Sheet exported from the recorded source URL
  has `Mixes!1142:1157` for `Mc_trace_minerals_SO4free`, listing 12
  chloride, citrate, borate, molybdate, selenate, vanadium, and tungstate
  constituents with the same g/L concentrations recorded in the YAML.
- The CultureBotHT compounds crosswalk exported from the recorded source URL
  has rows for the chloride salts used by the sulfate-free Mixes-tab block,
  including manganese(II) chloride tetrahydrate, copper(II) chloride
  dihydrate, and aluminum chloride hydrate.
- The `unmapped_ingredients_ols_exact_audit.tsv` row for this slug reports no
  exact OLS hit for `Mc_trace_minerals_SO4free` or
  `Mc trace minerals SO4free`, supporting the local registry mint.
- The final SSSOM publishes one `skos:exactMatch` row from
  `MIM:Mc_trace_minerals_SO4free` to
  `kgmicrobe.ingredient:mc_trace_minerals_so4free` with empty `other`.

## Completeness

- The 12 `components` rows exactly match the Mixes-tab recipe, pair every
  concentration with `G_PER_L`, and resolve to existing MIM catalog targets.
- The `TRACE_ELEMENT` role is supported by the same CultureBotHT Mixes-tab
  entry, which identifies this as the sulfate-free trace-mineral stock for Mc
  media.

## Recommended Edits

- None.
