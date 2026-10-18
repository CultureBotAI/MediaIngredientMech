# `data/ingredients/mapped/Kao_And_Michayluk_Vitamin_Solution.yaml`

## Verdict

Needs curation. The named Kao and Michayluk formulation is correctly preserved
as a local `kgmicrobe.ingredient` identity with a close parent mapping to the
generic MICRO vitamin solution class, but `VITAMIN_SOURCE` is only provisional
name-pattern evidence and the import-era notes still say curator review is
needed.

## Identity

- Reviewed record:
  `data/ingredients/mapped/Kao_And_Michayluk_Vitamin_Solution.yaml`.
- Identifier and grounding:
  `identifier: kgmicrobe.ingredient:kao_and_michayluk_vitamin_solution` with
  `ontology_mapping.ontology_id: MICRO:0000460`, label `vitamin solution`,
  source `MICRO`, `mapping_quality: CLOSE_MATCH`, `mapping_status: MAPPED`,
  and `ingredient_type: STOCK_SOLUTION`.
- Occurrence statistics: `media_count: 1` and `total_occurrences: 1`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Kao_And_Michayluk_Vitamin_Solution.yaml data/ingredients/mapped/Karanjin.yaml data/ingredients/mapped/Kasugamycin.yaml data/ingredients/mapped/Kawain.yaml data/ingredients/mapped/Kbr.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `scripts/_engine_a_obo_safe.sh data/ingredients/mapped/Kao_And_Michayluk_Vitamin_Solution.yaml "CHEBI FOODON NCIT MESH UBERON ENVO BTO PATO"`:
  exited 1, so Engine A LinkML term validation was skipped for this MICRO
  record because `MICRO:0000460` is outside the justfile's OBO-safe adapter
  set.
- `uv run --frozen linkml-term-validator validate-data ... --labels`: passed
  for the four ChEBI records in the batch.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip_20260916_2200`:
  aggregated 2951 records.
- `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip_20260916_2200`:
  passed with 2 files compared, 0 data differences, and only expected
  `generation_date` metadata differences.

## Evidence

- Exact EBI OLS4 search for `Kao and Michayluk vitamin solution` returned zero
  hits, supporting the current local identity plus close parent mapping rather
  than an exact public ontology CURIE.
- The final SSSOM publishes the expected `skos:closeMatch` row to
  `MICRO:0000460` and an exact registry row to
  `kgmicrobe.ingredient:kao_and_michayluk_vitamin_solution`. The
  `UNKNOWN_TERM` stamps are expected for the MICRO and KG-Microbe prefixes on
  this validator surface.
- Major: `nutritional_roles.VITAMIN_SOURCE` has only
  `COMPUTATIONAL_PREDICTION` evidence from a curated name-pattern rule, with no
  inspected CultureMech, MediaDive, or literature evidence attached to the
  role claim.
- Minor: `notes` still carries the original "Curator review needed" text even
  though the record now has a reviewed local identity.
- The hidden and ignored-inclusive search over `data/ingredients`, `mappings`,
  `reports/kg_microbe_node_id_mismatches.tsv`, `reports/hydrate_grounding.tsv`,
  `docs/data`, `src`, `tests`, `conf`, and `.claude` found the current YAML,
  final SSSOM rows, docs projections, external-prefix validation rows,
  unknown-term triage rows, and row-review dispositions; it found no hits in
  `reports/kg_microbe_node_id_mismatches.tsv`,
  `reports/hydrate_grounding.tsv`, or `mappings/needs_curator_review.tsv`.

## Completeness

- The local registry identifier, close MICRO parent mapping, aggregate copy,
  occurrence count, and final SSSOM identity rows are present and consistent.
- The record is incomplete until the vitamin-source role is supported by
  inspected claim-level evidence or removed.

## Recommended Edits

- Major: remove `nutritional_roles.VITAMIN_SOURCE` unless an inspected
  CultureMech, MediaDive, or literature source supports this exact formulation
  as a vitamin source, then rerun strict, term, round-trip, component, and
  SSSOM validation.
- Minor: refresh `notes` in
  `data/ingredients/mapped/Kao_And_Michayluk_Vitamin_Solution.yaml` so the
  record no longer says curator review is still pending after the May local
  identity repair.
