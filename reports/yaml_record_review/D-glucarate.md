# `data/ingredients/mapped/D-glucarate.yaml`

## Verdict

Pass with minor issues. The record denotes the fully deprotonated
`CHEBI:30612` D-glucarate anion, the final SSSOM row is an exact match, the
CultureMech occurrence count matches, and `D-saccharate` is an intentional
same-substance raw label. Only the absorbed MicrobeDecoder `D-saccharate`
source count and the stale top-level import note need cleanup.

## Identity

- Reviewed record: `data/ingredients/mapped/D-glucarate.yaml`.
- Identifier and grounding: `identifier: CHEBI:30612` with
  `ontology_mapping.ontology_id: CHEBI:30612`, source `CHEBI`,
  `mapping_quality: SYNONYM_MATCH`, and `mapping_status: MAPPED`.
- OLS resolved `CHEBI:30612` as active `D-glucarate(2-)` with formula
  `C6H8O8` and charge `-2`; the record's stored formula, InChI, SMILES, and
  mass describe that same dianion.
- The raw MicrobeDecoder label `D-glucarate` matches the curated MIM subject,
  and issue #213 deliberately folded `D-saccharate` into the same dianion under
  the repository's anion convention.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/D-glucarate.yaml data/ingredients/mapped/D-gluconate.yaml data/ingredients/mapped/D-glucosamine.yaml data/ingredients/mapped/D-glucosaminic_Acid.yaml data/ingredients/mapped/D-glucose.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/D-glucarate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`:
  passed; all id-label pairs corresponded, with full-corpus plausibility
  warnings only.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.
- `uv run --frozen python scripts/run_shared_evidence_validator.py`: unavailable
  because the sibling `culturebotai-claw` checkout was absent.

## Evidence

- `data/custom/microbedecoder/ingredient_candidates.tsv` and
  `data/custom/microbedecoder/unmapped_labels.tsv` still show the original
  `d_glucarate` label with 25 BacDive utilization mentions, matching the
  record's current `source_occurrences` entry.
- The same hidden/ignored-inclusive search found the absorbed
  `kgmicrobe.trait:d_saccharate` source label with 16 BacDive utilization
  mentions. That raw label is retained as a synonym and exported in final
  SSSOM `other`, but its source count is not represented in
  `source_occurrences`.
- `mappings/culturemech_recipe_membership.tsv` contains one row for
  `CHEBI:30612`, matching `occurrence_statistics.media_count: 1` and
  `total_occurrences: 1`.
- `mappings/ingredient_mappings.sssom.tsv` maps `MIM:D-glucarate` to
  `CHEBI:30612` with `skos:exactMatch`, the canonical object label
  `D-glucarate(2-)`, CHEBI object source, and only the same-substance raw label
  `D-saccharate` in `other`.
- A live OLS exact search for `D-saccharate` did not return a newer exact
  CHEBI synonym that would supersede the local #213 decision; the final SSSOM
  token therefore remains backed by local raw-label curation, not by ChEBI.

## Completeness

- The hidden/ignored-inclusive exact-identifier search over `data` found no
  second active primary record for `CHEBI:30612`; it found only this record,
  synchronized aggregate/index copies, generated backups, and the one
  CultureMech membership row.
- No roles, environmental contexts, or decomposition edges are asserted, which
  is appropriate for this MicrobeDecoder metabolite record.
- The top-level `notes` string still says no CAS-RN or CHEBI/NCIT match was
  found and curator review was needed even though the record is now mapped to
  `CHEBI:30612`.

## Recommended Edits

- In `data/ingredients/mapped/D-glucarate.yaml`, update
  `source_occurrences` so the absorbed `D-saccharate` MicrobeDecoder count is
  traceable, either as a 41-count aggregate for the BacDive utilization column
  or as a separate raw-label-aware provenance entry if the schema grows one.
- Remove or refresh the stale top-level `notes` field.
- Regenerate synchronized curated and SSSOM products, then rerun
  `uv run --frozen python scripts/validate_strict.py`,
  `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/D-glucarate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`,
  `uv run --frozen python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`,
  and `uv run --frozen python scripts/validate_sssom_invariants.py`.
