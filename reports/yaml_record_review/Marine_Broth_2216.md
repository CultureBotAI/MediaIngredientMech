# `data/ingredients/mapped/Marine_Broth_2216.yaml`

## Verdict

Needs curation. The local registry identity, catalog variants, ATCC component
transcription, occurrence count, and final SSSOM row pass, but the record still
uses `UNDEFINED_MIXTURE` where the current schema expects `NAMED_MEDIUM` for a
complete named medium formulation.

Severity: major.

## Identity

- Reviewed record: `data/ingredients/mapped/Marine_Broth_2216.yaml`.
- Identifier and grounding:
  `identifier: kgmicrobe.ingredient:marine_broth_2216` with matching
  `ontology_mapping.ontology_id`, label `Marine broth 2216`, source
  `kgmicrobe.ingredient`, `mapping_quality: FALLBACK_REGISTRY`, and
  `mapping_status: MAPPED`.
- Occurrences: 19 CultureMech recipes; the current
  `mappings/culturemech_recipe_membership.tsv` contains 19
  `kgmicrobe.ingredient:marine_broth_2216` edges.
- Components: 17 component rows transcribed from the ATCC Marine Agar/Broth
  2216 scratch formula with agar omitted.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Mannobiose` through `Marine_Broth_2216`: exited 0 and wrote zero ERROR rows.
- Engine A term validation was skipped for this record because
  `kgmicrobe.ingredient` is a local non-OBO registry prefix covered by the
  product id-label validator rather than by `linkml-term-validator`.
- `uv run --frozen python scripts/validate_component_partonomy.py` exited 0
  across 2,951 records and 505 components.

## Evidence

- A gitignore-independent `rg --no-ignore --hidden` search over the repository
  found the live mapped record, synchronized curated and product rows, the
  CultureMech residual and recipe-membership rows, and historical backup rows;
  it found no inspected ontology record that would supersede the local
  `kgmicrobe.ingredient` mint.
- The `add_culturemech_gap_labels` maintained input documents the minting
  decision: MICRO had only adjacent marine agar classes, not a verified 2216
  formulation, and the broth twin was promoted alongside `Marine_agar_2216` to
  avoid leaving one of the two local identities unmapped.
- The ATCC Medium 2887 source URL resolves to a two-page PDF. Its scratch
  formula for Difco Marine Agar 2216 lists peptone, yeast extract, ferric
  citrate, the same salts and concentrations in the YAML, agar at 15 g/L, and
  says to omit agar for broth medium.
- The final SSSOM publishes one `skos:exactMatch` row from
  `MIM:Marine_Broth_2216` to
  `kgmicrobe.ingredient:marine_broth_2216` with only the curated
  CultureMech catalog variants in `other`.

## Completeness

- The 17 component rows correctly omit agar from the 18-component Marine Agar
  2216 sibling formula and keep distilled water at 1 L/L.
- The current `ingredient_type: UNDEFINED_MIXTURE` conflicts with the July
  history entry that reclassified this exact record from `UNDEFINED_MIXTURE` to
  the former `DEFINED_MEDIUM` category. That enum is now `NAMED_MEDIUM`, which
  is the schema's category for complete named formulations such as Marine agar
  2216.

## Recommended Edits

- Change `ingredient_type` to `NAMED_MEDIUM` in
  `data/ingredients/mapped/Marine_Broth_2216.yaml` and regenerate
  `data/curated/mapped_ingredients.yaml` plus docs products.
