# `data/ingredients/mapped/Mc_general_salts.yaml`

## Verdict

Pass. The local stock-solution identity, exact component transcription,
mineral-source evidence, occurrence count, and final SSSOM row all pass.

## Identity

- Reviewed record: `data/ingredients/mapped/Mc_general_salts.yaml`.
- Identifier and grounding:
  `identifier: kgmicrobe.ingredient:mc_general_salts` with matching
  `ontology_mapping.ontology_id`, label `Mc_general_salts`, source
  `kgmicrobe.ingredient`, `mapping_quality: FALLBACK_REGISTRY`,
  `mapping_status: MAPPED`, `ingredient_type: STOCK_SOLUTION`, and
  `solution_type: MINERAL_STOCK`.
- Occurrences: three CultureBotHT media.
- Components: KCl, magnesium chloride hexahydrate, magnesium sulfate
  heptahydrate, and calcium chloride.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Marine_agar_2216` through `Mc_general_salts`: exited 0 and wrote zero ERROR
  rows.
- Engine A term validation was skipped for this record because
  `kgmicrobe.ingredient` is a local non-OBO registry prefix covered by the
  product id-label validator rather than by `linkml-term-validator`.

## Evidence

- The FEBA media definitions Google Sheet exported from the recorded source URL
  has `Mixes!1090:1093` for `Mc_general_salts`, listing KCl at 0.67 g/L,
  magnesium chloride hexahydrate at 5.5 g/L, magnesium sulfate heptahydrate at
  6.9 g/L, and calcium chloride at 0.21 g/L.
- The CultureBotHT compounds crosswalk exported from the recorded source URL
  has `Calcium chloride` as CAS `10043-52-4` with formula `CaCl2`, supporting
  the anhydrous `CHEBI:3312` component rather than the distinct calcium
  chloride dihydrate row.
- The `unmapped_ingredients_ols_exact_audit.tsv` row for this slug reports no
  exact OLS hit for `Mc_general_salts` or `Mc general salts`, supporting the
  local registry mint.
- The final SSSOM publishes one `skos:exactMatch` row from
  `MIM:Mc_general_salts` to
  `kgmicrobe.ingredient:mc_general_salts` with empty `other`.

## Completeness

- The four `components` rows exactly match the Mixes-tab recipe, pair every
  concentration with `G_PER_L`, and resolve to existing MIM catalog targets.
- The `MINERAL_SOURCE` role is supported by the same CultureBotHT Mixes-tab
  entry, which identifies this as the inorganic general-salts stock for Mc
  media.

## Recommended Edits

- None.
