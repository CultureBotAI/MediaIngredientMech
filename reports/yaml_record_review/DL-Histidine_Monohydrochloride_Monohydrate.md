# `data/ingredients/mapped/DL-Histidine_Monohydrochloride_Monohydrate.yaml`

## Verdict

Needs curation. The CAS-backed local identity and NCIT parent mapping are
represented with exact local identity rows and an empty parent-row synonym
payload, but the `AMINO_ACID_SOURCE` role is still only a provisional
computational assertion.

## Identity

- Reviewed record:
  `data/ingredients/mapped/DL-Histidine_Monohydrochloride_Monohydrate.yaml`.
- Identifier and grounding: `identifier: cas:123333-71-1` with
  `ontology_mapping.ontology_id: NCIT:C87334`, source `NCIT`,
  `mapping_quality: NARROW_MATCH`, and `mapping_status: MAPPED`.
- Live OLS resolves `NCIT:C87334` to active
  `Histidine Monohydrochloride Monohydrate`; NCIT's exact synonyms include
  L-histidine labels, so the DL supplied form correctly remains CAS-primary
  rather than collapsing exactly onto the NCIT parent.
- PubChem resolves `123333-71-1` to
  `DL-Histidine, monohydrochloride, monohydrate`, formula `C6H12ClN3O3`,
  matching the record's stored PubChem CID and formula.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/DL-3-Hydroxyisobutyric_Acid_Sodium_Salt.yaml data/ingredients/mapped/DL-Glyceraldehyde_3-phosphate.yaml data/ingredients/mapped/DL-Glycerol_1-phosphate_Sodium_Salt_Hydrate.yaml data/ingredients/mapped/DL-Histidine_Monohydrochloride_Monohydrate.yaml data/ingredients/mapped/DL-Isocitric_Acid_Trisodium_Salt_Hydrate.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/DL-3-Hydroxyisobutyric_Acid_Sodium_Salt.yaml data/ingredients/mapped/DL-Glyceraldehyde_3-phosphate.yaml data/ingredients/mapped/DL-Glycerol_1-phosphate_Sodium_Salt_Hydrate.yaml data/ingredients/mapped/DL-Histidine_Monohydrochloride_Monohydrate.yaml data/ingredients/mapped/DL-Isocitric_Acid_Trisodium_Salt_Hydrate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for all 5 files.
- `curl -L ... q=Histidine%20Monohydrochloride%20Monohydrate&ontology=ncit&exact=true`:
  live OLS resolved `NCIT:C87334`.
- `curl -L ... /compound/name/123333-71-1/property/.../JSON`: PubChem
  resolved the CAS value to CID 517335,
  `DL-Histidine, monohydrochloride, monohydrate`.
- `uv run --frozen python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`:
  passed; all id-label pairs corresponded, with full-corpus plausibility
  warnings only.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- `mappings/culturemech_recipe_membership.tsv` has no rows for
  `cas:123333-71-1`, matching `occurrence_statistics.media_count: 0` and
  `total_occurrences: 0`.
- The final `mappings/ingredient_mappings.sssom.tsv` rows include the required
  `skos:narrowMatch` to `NCIT:C87334`, the `skos:exactMatch` registry row for
  `cas:123333-71-1`, and the `skos:exactMatch` kg-microbe identity row
  required for a subject mapped through a broader NCIT parent.
- The NCIT parent row has an empty `other` value, and the identity rows publish
  only `CAS:123333-71-1`.
- The `AMINO_ACID_SOURCE` role is supported only by a
  `COMPUTATIONAL_PREDICTION` evidence object whose curator note says the
  name-pattern role is provisional and recommends review.

## Completeness

- The hidden/ignored-inclusive exact-identifier search over active `data`,
  `mappings`, `docs`, `scripts`, and `tests` found no second primary record for
  `cas:123333-71-1`; `NCIT:C87334` is also reused by
  `L-Histidine_Monohydrochloride_Monohydrate` as the same broader NCIT parent.
- The parent/child identity loss is represented by `NARROW_MATCH` plus
  companion local identity rows.
- The record has no source occurrences, component decomposition, or
  environmental contexts to resolve.

## Recommended Edits

- In
  `data/ingredients/mapped/DL-Histidine_Monohydrochloride_Monohydrate.yaml`,
  remove the provisional `AMINO_ACID_SOURCE` role or replace its
  `COMPUTATIONAL_PREDICTION` evidence with inspected claim-level evidence for
  this supplied form.
- Regenerate synchronized curated and SSSOM products, then rerun
  `uv run --frozen python scripts/validate_strict.py`,
  `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/DL-Histidine_Monohydrochloride_Monohydrate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`,
  `uv run --frozen python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`,
  and `uv run --frozen python scripts/validate_sssom_invariants.py`.
