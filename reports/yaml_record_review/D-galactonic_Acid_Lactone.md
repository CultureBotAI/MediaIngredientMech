# `data/ingredients/mapped/D-galactonic_Acid_Lactone.yaml`

## Verdict

Needs curation, with a major identity-specificity issue. The current
`CHEBI:15895` target is an active, structurally self-consistent
`D-galactono-1,4-lactone` term, but the raw MicrobeDecoder label
`D-galactonic acid lactone` omits the `gamma`/`1,4` specificity in ChEBI's
synonyms. A cross-lane local research ledger also disputes the current
`SYNONYM_MATCH`, so the exact identity needs a curator decision rather than
leaving the final SSSOM exactMatch row in place by default.

## Identity

- Reviewed record: `data/ingredients/mapped/D-galactonic_Acid_Lactone.yaml`.
- Current identifier and grounding: `identifier: CHEBI:15895`,
  `ontology_mapping.ontology_id: CHEBI:15895`,
  `ontology_label: D-galactono-1,4-lactone`, `ontology_source: CHEBI`,
  `mapping_quality: SYNONYM_MATCH`, and `mapping_status: MAPPED`.
- Live OLS lookup by `CHEBI:15895` returns active `CHEBI:15895` labelled
  `D-galactono-1,4-lactone`, neutral formula `C6H10O6`, and CAS xref
  `2782-07-2`.
- The same live synonym list keeps the current term's specificity in labels
  such as `D-galactonic acid gamma-lactone`,
  `D-Galactonic acid, gamma-lactone`, and `D-Galactono-1,4-lactone`; the raw
  `D-galactonic acid lactone` string is not a registered synonym under exact
  or case-folded comparison.
- A hidden/ignored-inclusive exact `^identifier:` search under `data` found
  only this current record using `CHEBI:15895`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/D-fucose.yaml data/ingredients/mapped/D-galactonate.yaml data/ingredients/mapped/D-galactonic_Acid_Lactone.yaml data/ingredients/mapped/D-galactose.yaml data/ingredients/mapped/D-galacturonic_Acid.yaml`:
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
  `kgmicrobe.trait:d_galactonic_acid_lactone` import row and its 21
  `BacDive_Metabolite_utilization` count under `data/custom/microbedecoder`.
- `mappings/culturemech_recipe_membership.tsv` contains 0 rows for
  `CHEBI:15895`, matching the record's 0/0 CultureMech `occurrence_statistics`;
  the 21 BacDive mentions are correctly kept under `source_occurrences`.
- `mappings/record_research_validation.tsv` flags the current
  `CHEBI:15895`/`SYNONYM_MATCH` as a P1 `BOTH_LANES_DISPUTE` and records that
  the Claude lane rejected the exact-synonym grade because the nearest ChEBI
  strings preserve the missing `gamma` qualifier.
- The final SSSOM row publishes
  `MIM:D-galactonic_Acid_Lactone skos:exactMatch CHEBI:15895`. Its `other`
  field is empty, so the defect is the exactMatch identity itself, not a noisy
  synonym payload.
- No nutritional, physicochemical, cellular-metabolic, environmental, or
  component claims are asserted.

## Completeness

- The top-level `notes` still repeat the import-time statement that there was
  "no CAS-RN or CHEBI/NCIT match" and "Curator review needed"; the larger
  issue is that the subsequent promotion to `CHEBI:15895` does not close the
  specificity gap.
- The stored formula, SMILES, and InChI match `CHEBI:15895`, but they therefore
  describe the disputed 1,4/gamma-lactone target rather than independently
  proving that the raw source label meant that exact ring form.
- The aggregate record in `data/curated/mapped_ingredients.yaml` round-trips
  with the per-record YAML.

## Recommended Edits

- Major: in `data/ingredients/mapped/D-galactonic_Acid_Lactone.yaml`, re-decide
  the MicrobeDecoder label against the full P1 ledger context. Either add
  source-backed evidence that `D-galactonic acid lactone` was intended to mean
  `D-galactono-1,4-lactone`, or demote the record to an unresolved/local
  identity that does not publish `MIM:D-galactonic_Acid_Lactone
  skos:exactMatch CHEBI:15895`; then rebuild final SSSOM.
