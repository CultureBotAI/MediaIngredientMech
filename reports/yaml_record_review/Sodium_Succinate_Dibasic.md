# `data/ingredients/mapped/Sodium_Succinate_Dibasic.yaml`

## Verdict

Needs curation - major. The #263/#320 regrounding removed the unrelated
`CHEBI:150903` target, but this record still publishes exact synonyms and a
carbon-source role inherited from that old glycoside. It also appears to be a
residual same-CAS duplicate of the live anhydrous sodium succinate record.

## Identity

- Reviewed record: `data/ingredients/mapped/Sodium_Succinate_Dibasic.yaml`.
- Identifier and grounding: `identifier: cas:150-90-3` with
  `ontology_mapping.ontology_id: CHEBI:63675`, label
  `sodium succinate (anhydrous)`, source `CHEBI`,
  `mapping_quality: NARROW_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 6 source occurrences across 6 CultureMech media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Sodium_Salicylate` through `Sodium_Thiophosphate_Tribasic_Hydrate`: exited 0
  and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-parent
  record.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh EBI OLS4 lookup resolves active `CHEBI:63675` with label
  `sodium succinate (anhydrous)` and CAS `150-90-3`.
- Fresh PubChem lookup for CAS `150-90-3` resolves to sodium succinate, the same
  CAS and identity as `data/ingredients/mapped/Sodium_Succinate.yaml`.
- A hidden/ignored-inclusive search over `data`, `src`, `tests`, `mappings`,
  `scripts`, and `reports` found the old glycoside alias
  `Fuc(a1-3)[Glc(a1-4)]Gal` still active in this per-record YAML, in the
  aggregate YAML, and in final SSSOM `other`.
- The hidden/ignored-inclusive mapping search also found
  `other_cross_record_baseline.tsv` tracking
  `MIM:Sodium_Succinate_Dibasic` as a possible duplicate of
  `MIM:Sodium_Succinate`.
- Major: all three active synonyms still name the old unrelated
  `CHEBI:150903` glycoside rather than disodium succinate.
- Major: `nutritional_roles.CARBON_SOURCE` still cites carbohydrate ancestry
  from the old glycoside grounding, and `ENERGY_SOURCE` is also provisional.

## Completeness

- The current parent ChEBI term and CAS value now describe disodium succinate,
  but the active synonym list, final `other` payload, nutritional roles, and
  duplicate record boundary still need cleanup.

## Recommended Edits

- Major: merge this residual CAS record into
  `data/ingredients/mapped/Sodium_Succinate.yaml` if the two records are
  confirmed to denote the same CAS `150-90-3` anhydrous disodium succinate.
- Major: if this record survives, remove the three active glycoside synonyms and
  rebuild final SSSOM so they leave the `MIM:Sodium_Succinate_Dibasic` row's
  `other` column.
- Major: remove or re-evidence the stale `CARBON_SOURCE` and provisional
  `ENERGY_SOURCE` role facets.
