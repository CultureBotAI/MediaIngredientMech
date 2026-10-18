# `data/ingredients/mapped/Mc_vitamins.yaml`

## Verdict

Pass. The local vitamin-stock identity, exact component transcription,
vitamin-source evidence, occurrence count, and final SSSOM row all pass.

## Identity

- Reviewed record: `data/ingredients/mapped/Mc_vitamins.yaml`.
- Identifier and grounding: `identifier: kgmicrobe.ingredient:mc_vitamins` with
  matching `ontology_mapping.ontology_id`, label `Mc_vitamins`, source
  `kgmicrobe.ingredient`, `mapping_quality: FALLBACK_REGISTRY`,
  `mapping_status: MAPPED`, `ingredient_type: STOCK_SOLUTION`, and
  `solution_type: VITAMIN_MIX`.
- Occurrences: 22 CultureBotHT media.
- Components: ten vitamin and micronutrient cofactor constituents.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Mc_general_salts_SO4free` through `Meat_Extract`: exited 0 and wrote zero
  ERROR rows.
- Engine A term validation was skipped for this record because
  `kgmicrobe.ingredient` is a local non-OBO registry prefix covered by the
  product id-label validator rather than by `linkml-term-validator`.

## Evidence

- The FEBA media definitions Google Sheet exported from the recorded source URL
  has `Mixes!1112:1125` for `Mc_vitamins`, listing the same ten constituents
  and g/L concentrations recorded in the YAML.
- The CultureBotHT compounds crosswalk exported from the recorded source URL
  has rows for every listed vitamin-stock constituent, including rows whose
  synonym columns cover the local surface forms `vitamin B12`,
  `p-aminobenzoic acid`, `pyridoxine hydrochloride`, and `thiamine HCl`.
- The `unmapped_ingredients_ols_exact_audit.tsv` row for this slug reports no
  exact OLS hit for `Mc_vitamins` or `Mc vitamins`, supporting the local
  registry mint.
- The final SSSOM publishes one `skos:exactMatch` row from `MIM:Mc_vitamins`
  to `kgmicrobe.ingredient:mc_vitamins` with empty `other`.

## Completeness

- The ten `components` rows exactly match the Mixes-tab recipe, pair every
  concentration with `G_PER_L`, and resolve to existing MIM catalog targets.
- The `VITAMIN_SOURCE` role is supported by the same CultureBotHT Mixes-tab
  entry, which identifies this as the 100X vitamin stock for Mc media.

## Recommended Edits

- None.
