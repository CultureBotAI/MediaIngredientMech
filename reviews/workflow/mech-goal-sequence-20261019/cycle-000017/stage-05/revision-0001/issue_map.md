# Cycle 17 Stage 05 (`resolve_review_findings`) — Grouped Issue Map & Finding Dispositions

- **Run ID:** `mech-goal-sequence-20261019`
- **Cycle:** `17`
- **Stage:** `5` (`resolve_review_findings`)
- **Repository:** `CultureBotAI/MediaIngredientMech` (`mediaingredientmech`)
- **Consumed Stage 04 Review Evidence:** [`reviews/workflow/mech-goal-sequence-20261019/cycle-000017/stage-04/revision-0001/evidence.yaml`](../stage-04/revision-0001/evidence.yaml) (`sha256: 5d9e289adcc7771d7703a0c3fd02c26e4758660cc5a7f743b545a5e9e153d517`, merged via PR `#1306`, merge commit `1f61f36db6e059d600af6032b6bc5a40e60583eb`)
- **Consumed Stage 04 Review Reports:**
  - [`reviews/workflow/mech-goal-sequence-20261019/cycle-000017/stage-04/revision-0001/review_report.md`](../stage-04/revision-0001/review_report.md) (`sha256: 4db746e4b066024386d8162b3ff533992562e06fa0b69bd79bd2c1f17300cc4c`)
  - [`reviews/workflow/mech-goal-sequence-20261019/cycle-000017/stage-04/revision-0001/review_findings.md`](../stage-04/revision-0001/review_findings.md) (`sha256: 84ee742ac9ba21a29fd54a186db7920afff3f4d54d2626e619082ab9ff88b173`)
  - [`reviews/workflow/mech-goal-sequence-20261019/cycle-000017/stage-04/revision-0001/coverage_report.md`](../stage-04/revision-0001/coverage_report.md) (`sha256: 620a29aa80561e1789688cd32a32e40395f4588bebec141517abaac1bed44481`)
  - [`reviews/workflow/mech-goal-sequence-20261019/cycle-000017/stage-04/revision-0001/validation.md`](../stage-04/revision-0001/validation.md) (`sha256: d020713f039e478a3ce49ec0320571c2704a9b474f7032a50b46a056c0674f28`)

## 1. Executive Summary

Stage 5 consumes the accepted Cycle 17 Stage 4 review outputs and carried-forward finding families (`mim-c01-s04-f001` and `mim-c01-s04-f003`..`mim-c01-s04-f007`; note that `mim-c01-s04-f002` was resolved in Cycle 1 Stage 5 via PR `#922` / Issue `#920` and remains `0` findings in Cycle 17 Stage 4), groups all `6` active finding families by root cause and repair ownership into `3` deduplicated repair groups (`mim-c17-s05-g001` .. `mim-c17-s05-g003`), links each group to its live GitHub issue (`#921`, `#923`, `#718`), verifies exact-byte approval constraints against `reports/sssom_completion_20260921/review.json`, `reports/sssom_completion_20260921/mapping_review/nonmapping_cohorts.json`, and `reports/semantic_review_20260921/resolution/current-review.json`, and records verified dispositions and carry-forward blockers while preserving immutable historical review reports.

## 2. Grouped Issue Map (`mim-c17-s05-g001` .. `mim-c17-s05-g003`)

| Group ID | Finding IDs | Finding Count | Root Cause & Repair Ownership | Linked GitHub Issue | Issue State | Stage 5 Disposition |
| --- | --- | ---: | --- | --- | --- | --- |
| `mim-c17-s05-g001` | `mim-c01-s04-f001` | `1` (`1` record) | Missing direct MicrobeDecoder `D-lyxose` occurrence / provenance reconciliation on `data/ingredients/mapped/(2)-D-lyxose.yaml` (`CHEBI:62318`); co-located on a record with active semantic exclusion `SEM:cd74f8ddafa04d7e9a9a` (`media_occurrences`, `exclude-claim`) and exact-byte non-mapping cohort approval (`owner_record_sha256: 62258c9bdabaf8728fafb6923345fe4b24b9956069113896acb16e9631c1451e`). | [https://github.com/CultureBotAI/MediaIngredientMech/issues/921](https://github.com/CultureBotAI/MediaIngredientMech/issues/921) | `OPEN` | `deferred` (byte-bound to `reports/sssom_completion_20260921/mapping_review/nonmapping_cohorts.json` and `reports/semantic_review_20260921/resolution/current-review.json`; carried forward to coordinated semantic/SSSOM refresh) |
| `mim-c17-s05-g002` | `mim-c01-s04-f003` | `19` (`19` records) | Non-monotonic `curation_history` timestamp order (`2026-03-09` batch-import event appended after `2026-03-14`/`2026-03-15` events) across `19` mapped records (`11` in `batch_0001`, `8` in `batch_0002`); all `19/19` records are byte-pinned in `reports/sssom_completion_20260921/review.json["record_inputs"]` and `reports/semantic_review_20260921/resolution/current-review.json["record_inputs"]`. | [https://github.com/CultureBotAI/MediaIngredientMech/issues/923](https://github.com/CultureBotAI/MediaIngredientMech/issues/923) | `OPEN` | `deferred` (byte-bound across all `19/19` records in `reports/sssom_completion_20260921/review.json` and `reports/semantic_review_20260921/resolution/current-review.json`; carried forward to coordinated refresh under `#923`) |
| `mim-c17-s05-g003` | `mim-c01-s04-f004`, `mim-c01-s04-f005`, `mim-c01-s04-f006`, `mim-c01-s04-f007` | `950` (`926` distinct records) | Semantic release exclusions (`exclude-claim`) in `reports/semantic_review_20260921/resolution/current-review.json` requiring primary literature citations (`624` role claims), upstream recipe identity disambiguation (`29` media occurrence claims), raw synonym-token disambiguation (`266` claims across `262` records; false-certainty overstatement resolved in closed `#861`), and `31` stock/formulation component/ontology grounding reviews. | [https://github.com/CultureBotAI/MediaIngredientMech/issues/718](https://github.com/CultureBotAI/MediaIngredientMech/issues/718) (context: closed [#861](https://github.com/CultureBotAI/MediaIngredientMech/issues/861)) | `OPEN` | `deferred` (blocked on per-record primary literature curation, upstream recipe disambiguation, and semantic-release resolution ledger updates under `#718`) |

## 3. Exact-Byte Approval Constraint Verification (`src/mediaingredientmech/record_refresh.py`)

Before applying any in-place YAML edits in Stage 5, we verified the exact-byte hash binding across the two repository-wide review ledgers (`reports/sssom_completion_20260921/review.json` and `reports/semantic_review_20260921/resolution/current-review.json`):

1. **`src/mediaingredientmech/record_refresh.py` invariant:**
   - The refresh helper explicitly enforces: *"A receipt chain is not a license to preserve byte-bound approvals across a record edit."*
   - `reports/sssom_completion_20260921/assemble_review.py --check` validates that every `owner_record_sha256` in `mapping_review/decisions/*.json` and `mapping_review/nonmapping_cohorts.json`, plus every `record_inputs[path].sha256` in `reports/sssom_completion_20260921/review.json` and `reports/semantic_review_20260921/resolution/current-review.json`, matches the live disk SHA-256 of `data/ingredients/{mapped,unmapped}/*.yaml` and `data/curated/{mapped,unmapped}_ingredients.yaml`.
2. **Group `mim-c17-s05-g001` (`data/ingredients/mapped/(2)-D-lyxose.yaml`, `#921`):**
   - Current SHA-256: `62258c9bdabaf8728fafb6923345fe4b24b9956069113896acb16e9631c1451e`.
   - Pinned in `reports/sssom_completion_20260921/review.json["record_inputs"]`, `reports/sssom_completion_20260921/mapping_review/nonmapping_cohorts.json` (`owner_record_sha256`), and `reports/semantic_review_20260921/resolution/current-review.json` (which also carries active semantic finding `SEM:cd74f8ddafa04d7e9a9a` on `media_occurrences`).
   - Editing `(2)-D-lyxose.yaml` without a coordinated re-review of the `20260921` SSSOM/semantic release ledgers breaks `assemble_review.py --check` and `reviewed_sssom` export gates.
3. **Group `mim-c17-s05-g002` (`19` mapped records in `batch_0001` and `batch_0002`, `#923`):**
   - All `19/19` records are byte-pinned in both `reports/sssom_completion_20260921/review.json["record_inputs"]` and `reports/semantic_review_20260921/resolution/current-review.json["record_inputs"]`, and their aggregate surface `data/curated/mapped_ingredients.yaml` (`sha256: 0003cc90c06c963d48543dc5d62141b8e2e612ce69191a66ba6fb0a21415c9e1`) is also byte-pinned in `reports/sssom_completion_20260921/mapping_review/nonmapping_cohorts.json`.
   - Furthermore, all `19` records are inspected inputs in `reviews/records/structured/cohort/batch_0001-20261019T065629Z/` and `reviews/records/structured/cohort/batch_0002-20261019T065629Z/`, checked by `.venv/bin/python scripts/record_review.py --repo-root . check`.
4. **Group `mim-c17-s05-g003` (`950` semantic release exclusions across `926` distinct records, `#718`):**
   - Each excluded claim is gated by `exclude-claim` in `reports/semantic_review_20260921/resolution/current-review.json` (`sha256: ba19853b3116187c96fd2a78f7eb18fd7c288cb8c504bb81ff046d12138e046f`) and already prevented from leaking into the published reviewed SSSOM bundle (`3,014` source mapping rows: `1,739` `SUPPORTED` + `1,275` `WITHHOLD`, `0` excluded claims leaked).

## 4. Per-Finding Disposition Table

| Finding ID | Category | Count | Group ID | Issue URL | Disposition | Carry-Forward |
| --- | --- | ---: | --- | --- | --- | --- |
| `mim-c01-s04-f001` | `evidence_completeness` | `1` | `mim-c17-s05-g001` | `https://github.com/CultureBotAI/MediaIngredientMech/issues/921` | `deferred` | `true` |
| `mim-c01-s04-f003` | `curation_history_order` | `19` | `mim-c17-s05-g002` | `https://github.com/CultureBotAI/MediaIngredientMech/issues/923` | `deferred` | `true` |
| `mim-c01-s04-f004` | `cellular_role_evidence` | `624` | `mim-c17-s05-g003` | `https://github.com/CultureBotAI/MediaIngredientMech/issues/718` | `deferred` | `true` |
| `mim-c01-s04-f005` | `media_occurrence_evidence` | `29` | `mim-c17-s05-g003` | `https://github.com/CultureBotAI/MediaIngredientMech/issues/718` | `deferred` | `true` |
| `mim-c01-s04-f006` | `synonym_claim_scope` | `266` | `mim-c17-s05-g003` | `https://github.com/CultureBotAI/MediaIngredientMech/issues/718` | `deferred` | `true` |
| `mim-c01-s04-f007` | `component_and_grounding_scope` | `31` | `mim-c17-s05-g003` | `https://github.com/CultureBotAI/MediaIngredientMech/issues/718` | `deferred` | `true` |
