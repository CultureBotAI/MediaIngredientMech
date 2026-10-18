# `data/ingredients/mapped/D-arabitol.yaml`

## Verdict

Pass with minor issues. The MicrobeDecoder `D-arabitol` label is a ChEBI synonym
of active `CHEBI:18333` `D-arabinitol`, the neutral polyol structure matches,
the BacDive source-occurrence count is preserved separately from the 0/0
CultureMech count, and the final SSSOM row has no unsafe `other` payload. The
only curation cleanup is stale top-level import prose that still says curator
review is needed and no CHEBI match was found.

## Identity

- Reviewed record: `data/ingredients/mapped/D-arabitol.yaml`.
- Current identifier and grounding: `identifier: CHEBI:18333`,
  `ontology_mapping.ontology_id: CHEBI:18333`,
  `ontology_label: D-arabinitol`, `ontology_source: CHEBI`,
  `mapping_quality: SYNONYM_MATCH`, and `mapping_status: MAPPED`.
- Live OLS lookup by `CHEBI:18333` returns active `CHEBI:18333` labelled
  `D-arabinitol`; exact synonyms include `D-Arabitol`/`D-arabinitol`; the term
  carries neutral formula `C5H12O5`.
- The stored formula, SMILES, and InChI are consistent with that neutral
  D-arabinitol identity.
- A hidden/ignored-inclusive exact `^identifier:` search under `data` found
  only this current record using `CHEBI:18333`.

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
  `kgmicrobe.trait:d_arabitol` import row and its 331
  `BacDive_Metabolite_utilization` count under `data/custom/microbedecoder`.
- `mappings/culturemech_recipe_membership.tsv` contains 0 rows for
  `CHEBI:18333`, matching the record's 0/0 CultureMech `occurrence_statistics`;
  the 331 BacDive mentions are correctly kept under `source_occurrences`.
- The final SSSOM row publishes `MIM:D-arabitol skos:exactMatch CHEBI:18333`.
  Its `other` field is empty.
- No nutritional, physicochemical, cellular-metabolic, environmental, or
  component claims are asserted.

## Completeness

- The top-level `notes` still repeat the import-time statement that there was
  "no CAS-RN or CHEBI/NCIT match" and "Curator review needed"; the
  `PROMOTED_TO_MAPPED` history and current ontology mapping now supersede that
  statement.
- No required CAS slot is missing. Live ChEBI now carries `cas:488-82-4` for
  this term, so a future curator could add it after normal registry
  confirmation, but the absence does not make the current identity ambiguous.
- The aggregate record in `data/curated/mapped_ingredients.yaml` round-trips
  with the per-record YAML.

## Recommended Edits

- Minor: in `data/ingredients/mapped/D-arabitol.yaml`, replace the stale
  import-time top-level `notes` with a short note that this was a MicrobeDecoder
  BacDive utilization import later promoted through the ChEBI `D-arabitol`
  synonym; rerun strict validation afterward.
