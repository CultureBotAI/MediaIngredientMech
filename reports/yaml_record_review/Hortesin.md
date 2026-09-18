# `data/ingredients/mapped/Hortesin.yaml`

## Verdict

Pass. The local `kgmicrobe.compound` placeholder is intentional, the current
external searches still find no exact CHEBI/NCIT or PubChem target, and the
final SSSOM preserves the local identity row without unsupported synonyms.

## Identity

- Reviewed record: `data/ingredients/mapped/Hortesin.yaml`.
- Identifier and grounding:
  `identifier: kgmicrobe.compound:hortesin` with
  `ontology_mapping.ontology_id: kgmicrobe.compound:hortesin`, label
  `Hortesin`, source `kgmicrobe.compound`, `mapping_quality: PLACEHOLDER`,
  `mapping_status: MAPPED`, and `ingredient_type: SINGLE_INGREDIENT`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Hortesin.yaml data/ingredients/mapped/Hunters_Trace_Stock_Solution.yaml data/ingredients/mapped/Huperzine_A.yaml data/ingredients/mapped/Hyaluronic_Acid_Sodium_Salt_From_Streptococcus_Equi.yaml data/ingredients/mapped/Hydantoin.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- Engine A LinkML term validation was run for the three CHEBI-backed records in
  this batch and skipped for `Hortesin` because its exact target is a local
  `kgmicrobe.compound` registry CURIE.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip_20260916_1448`
  aggregated 2951 records.
- `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip_20260916_1448`
  passed with 2 files compared, 0 data differences, and only expected
  `generation_date` metadata differences.

## Evidence

- The 2026-05-10 placeholder review recorded no exact OLS candidate and no
  normalized local mapped duplicate for `Hortesin`.
- A fresh OLS4 search for `Hortesin` in CHEBI and NCIT returned zero hits, and
  PubChem returned no CID for `hortesin`.
- The row-review manifest classifies the final `UNKNOWN_TERM` as an
  `expected_registry_identifier` to keep pending promotion if an exact external
  ontology term appears.
- The final SSSOM publishes one `skos:exactMatch` row from `MIM:Hortesin` to
  `kgmicrobe.compound:hortesin` and exports no `other` synonym noise.
- The hidden and ignored-inclusive search over `data`, `src`, `tests`,
  `mappings`, `scripts`, `conf`, `docs`, and `.claude` found the current
  aggregate row, final SSSOM row, docs projections, no-hit review row, and
  row-review manifest entry.

## Completeness

- The local placeholder identifier, review note, aggregate copy, and final
  SSSOM row are present and consistent.
- No unsupported roles or noisy final synonyms are asserted.

## Recommended Edits

- None.
