# `data/ingredients/mapped/Green_House_Soil.yaml`

## Verdict

Pass. The local `kgmicrobe.ingredient:green_house_soil` identity preserves this
specific soil ingredient, the generic ENVO soil term is only a narrow parent,
the occurrence count is retained, and the final SSSOM parent and registry rows
agree.

## Identity

- Reviewed record: `data/ingredients/mapped/Green_House_Soil.yaml`.
- Identifier and grounding:
  `identifier: kgmicrobe.ingredient:green_house_soil` with parent
  `ontology_mapping.ontology_id: ENVO:00001998`, label `soil`, source `ENVO`,
  `mapping_quality: NARROW_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: UNDEFINED_MIXTURE`.
- Occurrence statistics: `total_occurrences: 11` and `media_count: 11`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Granaticin.yaml data/ingredients/mapped/Grasseriomycin.yaml data/ingredients/mapped/Green_House_Soil.yaml data/ingredients/mapped/Grisamine.yaml data/ingredients/mapped/Griseolutein_A.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Green_House_Soil.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for the ENVO parent and skipped only the local kg-microbe registry
  identifier.

## Evidence

- The matching aggregate `data/curated/mapped_ingredients.yaml` entry is
  identical to the split per-record YAML.
- OLS4 resolves `ENVO:00001998` as active `soil`, matching the intended generic
  parent rather than the exact greenhouse-sourced ingredient identity.
- `data/custom/kgmicrobe_ingredients.tsv` contains
  `kgmicrobe.ingredient:green_house_soil` with parent `ENVO:00001998`, minted
  from this record on 2026-05-02.
- The final `mappings/ingredient_mappings.sssom.tsv` rows map
  `MIM:Green_House_Soil` to `ENVO:00001998` by `skos:narrowMatch` and to
  `kgmicrobe.ingredient:green_house_soil` by `skos:exactMatch`; no raw
  `Green House Soil` token is exported in `other`.
- A hidden/ignored-inclusive search over `data`, `src`, `tests`, `mappings`,
  `scripts`, `conf`, `docs`, and `.claude` found the active YAML, the custom
  kg-microbe ingredient registry row, matching aggregate copies, generated
  products, final SSSOM rows, row-review TSVs, and ignored aggregate backups.

## Completeness

- The exact local ingredient identity, generic ENVO parent, undefined-mixture
  type, occurrence counts, raw CultureMech label, minted kg-microbe registry
  entry, and final SSSOM rows are populated.
- No role facet is asserted, which is acceptable for this record.

## Recommended Edits

- None.
