# `data/ingredients/mapped/D-aspartate.yaml`

## Verdict

Pass with minor issues. The MicrobeDecoder `D-aspartate` label is a ChEBI
synonym of active `CHEBI:29994` `D-aspartate(2-)`, the 2- structure and the
repository's bare-aspartate protonation rule agree, the 1/1 CultureMech count
and 30 BacDive source occurrences are traceable, and the final SSSOM row has no
unsafe `other` payload. The only curation cleanup is stale top-level import
prose that still says curator review is needed and no CHEBI match was found.

## Identity

- Reviewed record: `data/ingredients/mapped/D-aspartate.yaml`.
- Current identifier and grounding: `identifier: CHEBI:29994`,
  `ontology_mapping.ontology_id: CHEBI:29994`,
  `ontology_label: D-aspartate(2-)`, `ontology_source: CHEBI`,
  `mapping_quality: SYNONYM_MATCH`, and `mapping_status: MAPPED`.
- Live OLS lookup by `CHEBI:29994` returns active `CHEBI:29994` labelled
  `D-aspartate(2-)`; `D-aspartate` is a listed synonym; the term carries
  formula `C4H5NO4` and charge -2.
- `MAPPING_SEMANTICS.md` explicitly treats bare aspartate labels as descending
  to the growth-medium dianion rather than staying on ChEBI's protonation-
  agnostic aspartate parent, so this D-specific record is not an acid/dianion
  collapse.
- A hidden/ignored-inclusive exact `^identifier:` search under `data` found
  only this current record using `CHEBI:29994`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/D-arabinose.yaml data/ingredients/mapped/D-arabitol.yaml data/ingredients/mapped/D-aspartate.yaml data/ingredients/mapped/D-erythrose.yaml data/ingredients/mapped/D-fructose.yaml`:
  passed; 5 files scanned and 0 ERROR rows.
- Five `uv run --frozen linkml-term-validator validate-data ... -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`
  invocations, one per reviewed CHEBI-primary file in this batch: all exited 0.
- `uv run --frozen python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`:
  passed; all id-label pairs corresponded, with 104 non-blocking plausibility
  warnings across the full corpus.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K. Rule B4 was skipped because
  the sibling kg-microbe transformed ontology files were absent.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip_20260916_1334`
  followed by
  `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip_20260916_1334`:
  passed; 2 files compared, 0 data differences, and only expected
  `generation_date` metadata differences.
- `uv run --frozen python scripts/run_shared_evidence_validator.py`: failed
  because the sibling `culturebotai-claw` evidence validator checkout is absent.

## Evidence

- The hidden/ignored-inclusive MicrobeDecoder search found the original
  `kgmicrobe.trait:d_aspartate` import row and its 30
  `BacDive_Metabolite_utilization` count under `data/custom/microbedecoder`.
- `mappings/culturemech_recipe_membership.tsv` contains 1 row for
  `CHEBI:29994`, matching the record's 1/1 CultureMech `occurrence_statistics`.
- `mappings/microbedecoder_residual_grounded.tsv` records the
  `UNMAPPED_0641` promotion to `CHEBI:29994` through the `D-aspartate` synonym.
- The final SSSOM row publishes `MIM:D-aspartate skos:exactMatch CHEBI:29994`.
  Its `other` field is empty.
- No nutritional, physicochemical, cellular-metabolic, environmental, or
  component claims are asserted.

## Completeness

- The top-level `notes` still repeat the import-time statement that there was
  "no CAS-RN or CHEBI/NCIT match" and "Curator review needed"; the
  `PROMOTED_TO_MAPPED` history and current ontology mapping now supersede that
  statement.
- The aggregate record in `data/curated/mapped_ingredients.yaml` round-trips
  with the per-record YAML.

## Recommended Edits

- Minor: in `data/ingredients/mapped/D-aspartate.yaml`, replace the stale
  import-time top-level `notes` with a short note that this was a MicrobeDecoder
  BacDive utilization import later promoted through the ChEBI `D-aspartate`
  synonym; rerun strict validation afterward.
