# `data/ingredients/mapped/D.yaml`

## Verdict

Pass with minor issues. `D` is correctly tombstoned as a rejected comma-split
artifact merged into sodium lactate, the final SSSOM contains no `MIM:D` row,
and the record has no active occurrence count, but stale aspartate synonyms and
`ingredient_type: SINGLE_INGREDIENT` remain on the rejected record.

## Identity

- Reviewed record: `data/ingredients/mapped/D.yaml`.
- Identifier and grounding: `identifier: CHEBI:75228` with
  `ontology_mapping.ontology_id: CHEBI:75228`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: REJECTED`.
- Local OAK resolves `CHEBI:75228` to active `sodium lactate`, formula
  `C3H5O3.Na`, charge `0`, and CAS xref `72-17-3`.
- The curation history records that the original one-character label was the
  head of a comma split from `D,L-lactic acid, sodium salt`; the record was
  merged into sodium lactate and left as a rejected tombstone with SSSOM rows
  dropped.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/D-xylose.yaml data/ingredients/mapped/D-xylose_5-phosphate_Lithium_Salt.yaml data/ingredients/mapped/D.yaml data/ingredients/mapped/DAMPA.yaml data/ingredients/mapped/DCMU.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/D-xylose.yaml data/ingredients/mapped/D-xylose_5-phosphate_Lithium_Salt.yaml data/ingredients/mapped/D.yaml data/ingredients/mapped/DAMPA.yaml data/ingredients/mapped/DCMU.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed through `D` and then failed on `DAMPA` because its `cas:` fallback
  hit the known OAK SQL label-lookup error:
  `sqlite3.OperationalError: no such table: rdfs_label_statement`.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/D-xylose.yaml data/ingredients/mapped/D-xylose_5-phosphate_Lithium_Salt.yaml data/ingredients/mapped/D.yaml data/ingredients/mapped/DCMU.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed the 4-file CHEBI subset after skipping `DAMPA`.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:65327 CHEBI:37492 CHEBI:75228 CHEBI:116509`:
  returned formula, charge, mass, synonyms, and xrefs for `CHEBI:75228`.
- `uv run --frozen python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`:
  passed; all id-label pairs corresponded, with full-corpus plausibility
  warnings only.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- `mappings/culturemech_recipe_membership.tsv` contains 283 rows for
  `CHEBI:75228`, but those belong to the active sodium lactate subject rather
  than this rejected tombstone; this record's `occurrence_statistics` are
  correctly zeroed.
- The current final `mappings/ingredient_mappings.sssom.tsv` contains no
  `MIM:D` row, so the stale aspartate synonyms no longer leak into the
  published SSSOM output.
- The old kg-microbe aspartate synonyms and `ingredient_type:
  SINGLE_INGREDIENT` are stale residue claims on a rejected comma-split
  tombstone, but they are inert minor cleanup because the record is rejected
  and no SSSOM row is emitted.

## Completeness

- The hidden/ignored-inclusive exact-identifier search over active `data`,
  `mappings`, `docs`, `reports`, `.claude`, `.github`, `scripts`, `src`, and
  `tests` found `CHEBI:75228` on the active sodium lactate record and this
  rejected tombstone; the broad search also found generated projections and
  old review/backup surfaces.
- The wrong limonene CAS and aspartate structure fields described in history
  have already been removed.
- No role, component, or final SSSOM repair is required for this rejected
  record.

## Recommended Edits

- Optionally remove the stale aspartate synonyms and
  `ingredient_type: SINGLE_INGREDIENT` from
  `data/ingredients/mapped/D.yaml` so the tombstone contains only merge
  provenance for the comma-split artifact.
- Rerun `uv run --frozen python scripts/validate_strict.py` and
  `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/D.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`
  after that cleanup.
