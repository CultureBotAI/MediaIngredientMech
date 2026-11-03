# Step 7d native derived-output refresh plan

Prepared by read-only inspection. Root owns all writes and runs. The 38 planned owners have zero overlap with the 20 owners in the current companion cohort; its refresh must preserve that exact cohort and all claims. This plan adds no scientific or role approvals.

## Runtime and existing visualization inputs

Use `python3 RUN/run_step7d_mim.py step7d UNIQUE_TAG -- COMMAND...` for each command below. RUN is `/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/output/approved-plan-20261101T031134Z`. The runner sets the isolated pinned Claw checkout, Python 3.13.2 environment, current worktree, existing ontology cache, and `RECORD_REVIEW_BASE=467aa319a06ef992035f509f66fe251082b44ae1`. Prefer `UV_OFFLINE=1`; no dependency synchronization or embedding/research call is required.

The environment has pytest 9.0.2. Its existing `test-deps` path supplies pytest-cov 7.1.0 and coverage 7.17.0, verified by actual import. Do not install dev extras simply to run the suite. Native `just test` already succeeded under this profile in the preserved Step7c receipt.

Existing embeddings: `/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/MicroGrowLink/data/kgm_and_embeddings_paired/DeepWalkSkipGramEnsmallen_degreenorm_embedding_512_v3_2026-06-26_12_55_27.tsv.gz`, SHA-256 `b178b977ccfe00192e7a18fc1708dae19fbbd62e4efecb3539570c6f7a553457`, 5849378172 bytes. The full hash was recomputed during this preparation.

Existing native cache: `/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/output/approved-plan-20261101T031134Z/step7c/.umap_cache/ingredient_embeddings__CHEBI_ENVO_FOODON_MESH_NCIT_UBERON_kgmicrobe.compound_mediadive.ingredient_mediadive.solution__0757f043ac68.pkl`, SHA-256 `b6864e9f03cad721ed241b3e580477dac499692c578144196ea38278221c9b15`, 975767219 bytes, freshly hashed. `W/.umap_cache` was absent when checked. Root may create it and copy this exact cache file without overwriting another file. The source basename, size, mtime and prefix set give the same native cache key. Keep the source override even with a cache: the CLI checks the source exists. Step7c success receipt: `logs/step7c-visualizations-native-existing-embeddings-v2.json`. Graphviz sfdp is already installed. No new embeddings, network download, paid provider or cache-policy changes are needed.

## Ordered native commands

Before step 2, complete the guarded writes, record synchronization and native mapping receipt chain. Advance only the existing `REVIEWED_SOURCE` endpoint in the dated assembler to the verified new SSSOM SHA, as each prior batch did. This is a source boundary update, not scientific re-approval. Root handles the separately authorized snapshot rebuild and its trace review/commit after the owner commit; no snapshot producer is run by this plan.

1. `just sync-curated`
   After all guarded individual-record writes; inspect any serialization-only changes before native receipt hashes are finalized.

2. `python -B reports/sssom_completion_20260921/assemble_review.py`
   Only after the new native mapping receipt closes the source/SSSOM chain and REVIEWED_SOURCE is explicitly advanced to its verified endpoint.

3. `python -B reports/sssom_completion_20260921/assemble_review.py --check`
   No unchanged approval may carry across changed owner bytes.

4. `just export-kgx output/step7d-full-v1`
   New destination; complete explicit source graph for semantic evidence.

5. `python -B reports/semantic_review_20260921/resolution/build_review.py --bundle output/step7d-full-v1`
   Native builder; preserves unresolved findings and withdraws changed-owner inherited support.

6. `python -B -m mediaingredientmech.validation.semantic_release --root . --report reports/semantic_review_20260921/resolution/current-review.json`
   Require integrity PASS; report full-release FAIL honestly if open findings remain. Do not claim all assertions approved.

7. `python -B scripts/refresh_unchanged_cohort.py --root /Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/output/approved-plan-20261101T031134Z/step7d --baseline 467aa319a06ef992035f509f66fe251082b44ae1 --prior-review reports/step7c_mapping_751_313_235_20261102/refresh-v2/companion-review.json --output reports/step7d_mapping_901_20261103/companion-review.json --receipt reports/step7d_mapping_901_20261103/companion-refresh-receipt.json --prior-copy reports/step7d_mapping_901_20261103/prior-companion-review.json`
   Three paths must be absent; immutable successor. No projection override is needed unless a separately verified typed manifest changed; do not invent one.

8. `python -B -m mediaingredientmech.export.ingredient_bundle export --review reports/step7d_mapping_901_20261103/companion-review.json --output output/step7d-companion-v1`
   After paired selector repoint only; export independently replays selected cohort.

9. `just export-reviewed-sssom reports/sssom_completion_20260921/review.json output/step7d-reviewed-v1`
   New destination.

10. `just qc-reviewed-sssom reports/sssom_completion_20260921/review.json output/step7d-reviewed-v1`
   Assembler reproducibility, both partitions, SSSOM schema/prefix/CURIE checks.

11. `just export-supported-kgx reports/semantic_review_20260921/resolution/current-review.json output/step7d-supported-v1`
   New destination.

12. `just qc-supported-kgx reports/semantic_review_20260921/resolution/current-review.json output/step7d-supported-v1`
   Exact supported selection and complete excluded backlog.

13. `just export-indexes`
   Native nine data/curated index outputs.

14. `just export-lists`
   Native JSON/CSV/Markdown lists and label_index; Markdown timestamps are expected native output.

15. `just export-browser`
   Native docs/data/ingredients.json.

16. `env KG_MICROBE_EMBEDDINGS=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/MicroGrowLink/data/kgm_and_embeddings_paired/DeepWalkSkipGramEnsmallen_degreenorm_embedding_512_v3_2026-06-26_12_55_27.tsv.gz NUMBA_CACHE_DIR=/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/output/approved-plan-20261101T031134Z/step7d-execution-20261103/visualization-environment/numba-cache UV_OFFLINE=1 just generate-visualizations`
   Root may copy the verified existing native cache into W/.umap_cache first. Keep default reducers/coverage/prefixes/seed; no embed or embed-map.

17. `env UV_OFFLINE=1 just qc`
   Includes qc-sssom, strict, evidence, roundtrip/index/visualization and flat coverage; also writes native diagnostic reports.

18. `just check-unified-freshness`
   After root-owned Step7d exception rebuild and native sidecar, separate ordinary commit.

19. `just check-unified-rejections`
   Do not alter thresholds, rejection policy or owner selection.

20. `env UV_OFFLINE=1 just test-record-reviews`
   Dedicated immutable structured-review contract tier, as CI.

21. `env UV_OFFLINE=1 just test`
   Full tests plus maintained-package 35% coverage floor and script coverage report; no test weakening.

22. `env UV_OFFLINE=1 just lint format-check typecheck`
   Matches quality workflow; checks only, no formatter writes.

23. `env UV_OFFLINE=1 just validate-products`
   Dedicated blocking CI gate not included in just qc; uses existing pinned local ontology cache.

The complete machine-readable argv list, tags, inspected source hashes and runtime facts are in `derived-export-refresh-plan.json`. Commands are sequential; the producer destinations are new directories, so do not rerun over partial outputs.

## Prevent stale review dependencies

After the native companion refresh succeeds, repoint only `REVIEW` in `tests/test_ingredient_bundle.py` and the paired `--review` in `.github/workflows/qc-reviewed-sssom.yaml` to the same new companion review. Preserve every other byte/assertion; no other test/workflow edit is authorized. The two selectors currently point to `reports/step7c_mapping_751_313_235_20261102/refresh-v2/companion-review.json`.

The mapping assembler writes `reports/sssom_completion_20260921/{mapping-evidence.json,review.json}`. Its `--check` independently reproduces those files and verifies the native receipt chain. The full KGX export feeds the native semantic builder, which writes `resolution/{record-lineage.json,finding-dispositions.tsv,assertion-dispositions.tsv,current-review.json,historical-review-evidence.json}`. These are evidence refreshes, not new approval. If the builder changes its historical-evidence archive, re-run the assembler check; a newly stale input needs a new versioned assemble/build receipt, not a manual hash patch or waived assertion.

`semantic_release` without `--require-pass` tests integrity while retaining the honest full-source semantic FAIL/backlog. The supported export excludes that backlog. Record both the integrity result and semantic verdict; do not conflate them. Preserve all changed-owner withdrawals and all deferred alias obligations.

After final graph/support exports, run the supported-table schema check from `.github/workflows/qc-supported-kgx.yaml`: parse `output/step7d-supported-v1/ingredient_mappings.sssom.tsv` with `sssom.parsers.parse_sssom_table` and validate JsonSchema, PrefixMapCompleteness and StrictCurieFormat. The reviewed-SSSOM recipe already validates its own supported and withheld tables.

## Minimal maintained export scope

`sync-curated` aggregates the individual records and re-exports their canonical serialization. Run it before closing source hashes; any later byte rewrite invalidates the bound review/receipt. It is the correct direction for guarded per-record changes. Never run `sync-individual` first.

The small native derived refresh is `export-indexes`, `export-lists`, `export-browser`, then `generate-visualizations`. It needs no schema documentation, ingredient HTML, dashboard, membership rebuild, research, embedding generation, or unrelated report update. Indexes are deterministic and cover nine files. Lists generate the six CSV/JSON files, label index and three Markdown lists; Markdown has a native generation timestamp. Browser JSON has a generation timestamp; QC compares the ingredient payload. If only deterministic list files are required, the supported script offers `--format json` then `--format csv`, but the full native recipe also keeps the published Markdown content current.

Visualization regeneration changes the two native JSON outputs only; coordinate jitter is documented and is not a source semantic change. Review node membership/identity/metadata with the native strict currency check, not coordinate byte stability. No threshold, random seed, reducer, prefix selection or policy change is part of this task.

The `just qc` composite does not include the dedicated product-label gate, unified freshness, reviewed/supported export jobs, full pytest or static quality. Those are listed explicitly above. CI must still independently report all required checks green on the final head and merge-queue candidate.

No producer, test suite, QC command, source edit, selector edit or GitHub mutation was performed to prepare this plan.
