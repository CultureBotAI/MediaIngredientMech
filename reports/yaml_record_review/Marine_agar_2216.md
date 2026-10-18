# `data/ingredients/mapped/Marine_agar_2216.yaml`

## Verdict

Needs curation. The local registry identity, catalog variant, ATCC component
transcription, occurrence count, and final SSSOM row pass, but the record still
uses `UNDEFINED_MIXTURE` where the current schema expects `NAMED_MEDIUM` for a
complete named medium formulation.

Severity: major.

## Identity

- Reviewed record: `data/ingredients/mapped/Marine_agar_2216.yaml`.
- Identifier and grounding:
  `identifier: kgmicrobe.ingredient:marine_agar_2216` with matching
  `ontology_mapping.ontology_id`, label `Marine agar 2216`, source
  `kgmicrobe.ingredient`, `mapping_quality: FALLBACK_REGISTRY`, and
  `mapping_status: MAPPED`.
- Occurrences: 32 CultureMech recipes; the current
  `mappings/culturemech_recipe_membership.tsv` contains 32
  `kgmicrobe.ingredient:marine_agar_2216` edges.
- Components: 18 component rows transcribed from the ATCC Marine Agar/Broth
  2216 scratch formula.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Marine_agar_2216` through `Mc_general_salts`: exited 0 and wrote zero ERROR
  rows.
- Engine A term validation was skipped for this record because
  `kgmicrobe.ingredient` is a local non-OBO registry prefix covered by the
  product id-label validator rather than by `linkml-term-validator`.

## Evidence

- A gitignore-independent `rg --no-ignore --hidden` search over the repository
  found the live mapped record, synchronized curated and product rows, the
  CultureMech residual rows, and historical backup rows; it found no inspected
  ontology record that would supersede the local `kgmicrobe.ingredient` mint.
- The `add_culturemech_gap_labels` maintained input documents the minting
  decision: MICRO had only adjacent marine agar classes, not a verified 2216
  formulation, and no ChEBI or FoodOn term covered the complete compounded
  medium.
- The ATCC Medium 2887 source URL resolves to a two-page PDF. Its scratch
  formula for Difco Marine Agar 2216 lists peptone, yeast extract, ferric
  citrate, the same salts and concentrations in the YAML, agar at 15 g/L, and
  distilled water at 1,000 mL/L.
- The final SSSOM publishes one `skos:exactMatch` row from
  `MIM:Marine_agar_2216` to
  `kgmicrobe.ingredient:marine_agar_2216` with only the curated
  `Marine agar 2216 (BD-Difco)` catalog variant in `other`.

## Completeness

- The 18 component rows match the full ATCC Marine Agar 2216 scratch formula.
- The current `ingredient_type: UNDEFINED_MIXTURE` is stale. The schema uses
  `NAMED_MEDIUM` for complete named formulations and explicitly lists Marine
  agar 2216 as an example of that record granularity.

## Recommended Edits

- Change `ingredient_type` to `NAMED_MEDIUM` in
  `data/ingredients/mapped/Marine_agar_2216.yaml` and regenerate
  `data/curated/mapped_ingredients.yaml` plus docs products.
