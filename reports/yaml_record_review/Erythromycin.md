# `data/ingredients/mapped/Erythromycin.yaml`

## Verdict

Pass. The generic erythromycin record maps exactly to `CHEBI:48923`, carries a
CultureMech-backed selective-agent role, and exports only its CAS token in the
final SSSOM `other` column.

## Identity

- Reviewed record: `data/ingredients/mapped/Erythromycin.yaml`.
- Identifier and grounding: `identifier: CHEBI:48923` with matching
  `ontology_mapping.ontology_id`, canonical label `erythromycin`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, five
  CultureMech occurrences, and `ingredient_type: SINGLE_INGREDIENT`.
- `runoak -i ols:chebi info` resolved `CHEBI:48923` to `erythromycin`.
- PubChem resolved CAS RN `114-07-8` to CID 12560 with formula
  `C37H67NO13`, matching the expected erythromycin A identity for the generic
  CAS alias.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Epinephrine.yaml data/ingredients/mapped/Ertapenem.yaml data/ingredients/mapped/Erythromycin.yaml data/ingredients/mapped/Erythromycin_A.yaml data/ingredients/mapped/Erythromycin_B.yaml --out /tmp/mim_ery_batch_strict.tsv`:
  exited 0 for the 5-file batch; the output TSV contained only its header.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Erythromycin.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.

## Evidence

- The matching `data/curated/mapped_ingredients.yaml` entry carries the same
  ChEBI identifier, CAS RN, CultureMech occurrence count, duplicate-merge
  history, and `SELECTIVE_AGENT` role as the per-record YAML.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:Erythromycin` to `CHEBI:48923` with `skos:exactMatch`, the canonical
  ChEBI object label, and only `CAS:114-07-8` in `other`.
- `mappings/culturemech_recipe_membership.tsv` has five rows for
  `CHEBI:48923`, matching `occurrence_statistics`.
- A hidden/ignored-inclusive search over `data/ingredients`, `mappings`, and
  `reports/yaml_record_review` for `MIM:Erythromycin`, `CHEBI:48923`, and
  `114-07-8` found the active YAML, aggregate copy, final SSSOM row, five
  CultureMech recipe-membership rows, and expected row-review TSVs; it did not
  expose a contradictory active mapping.
- The active `SELECTIVE_AGENT` role is backed by the original CultureMech role
  text with `reference_type: DATABASE_ENTRY`, not a provisional name-list
  inference.

## Completeness

- The exact identity, CAS RN, occurrence count, duplicate-merge history,
  supported role, and final SSSOM payload are populated.
- The raw `Role:`/`Properties:` labels remain in YAML as provenance but are
  correctly filtered from final SSSOM `other`.

## Recommended Edits

- None.
