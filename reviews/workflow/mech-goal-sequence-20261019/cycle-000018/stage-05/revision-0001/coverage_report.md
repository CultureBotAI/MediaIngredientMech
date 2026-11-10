# Cycle 18 Stage 05 (`resolve_review_findings`) — Finding & Group Coverage Report

- **Run ID:** `mech-goal-sequence-20261019`
- **Cycle:** `18`
- **Stage:** `5` (`resolve_review_findings`)
- **Repository:** `CultureBotAI/MediaIngredientMech` (`mediaingredientmech`)
- **Consumed Stage 04 Review Evidence:** [`reviews/workflow/mech-goal-sequence-20261019/cycle-000018/stage-04/revision-0001/evidence.yaml`](../stage-04/revision-0001/evidence.yaml) (`sha256: 5406f99e71a90270524c73341c7d49a7e7fffb9cba3ce9c1e3320a785ac8d139`, merged via PR `#1348`, merge commit `e1a72e277440d12f17d7636b4df4c96d40c4b818`)
- **Tracked Evidence Latest Index:** [`reviews/workflow/latest.yaml`](../../../../latest.yaml) (`sha256: 82e5361647d1dde3c1b977acb614b6a1d9dcf34fb28e5898ce0be64e64f620b3`, `52` verified entries through Cycle 18 Stage 4 PR `#1348`, `receipt_sha256: 3ab8f0e0da0d03077c712bc70f2a48ceecadca0407c4e0fe969a865f7e8aa464`)

## 1. Corpus & Finding Accounting

| Metric | Value | Verification Source |
| --- | ---: | --- |
| Individual ingredient records | `2,956` (`2,854` mapped + `102` unmapped) | `data/ingredients/{mapped,unmapped}/*.yaml` |
| Collection / ontology / mapping files | `7` | `data/curated/*.yaml`, `data/ontologies/*.yaml`, `mappings/*.tsv` |
| Structured review bundles | `1,015` (`971` individual + `44` cohort; `2,030` files) | `.venv/bin/python scripts/record_review.py --repo-root . check` |
| Historical review findings resolved in Cycle 1 Stage 5 | `1` (`mim-c01-s04-f002`, PR `#922` / Issue `#920`) | `reviews/records/structured/cohort/batch_0001-20261019T065629Z/review.yaml` |
| Active Stage 4 finding families consumed in Cycle 18 Stage 5 | `6` (`mim-c01-s04-f001`, `mim-c01-s04-f003`..`f007`) | `reviews/workflow/mech-goal-sequence-20261019/cycle-000018/stage-04/revision-0001/evidence.yaml` |
| Total active finding instances across `6` families | `970` (`1` + `19` + `624` + `29` + `266` + `31`) | `reviews/workflow/mech-goal-sequence-20261019/cycle-000018/stage-04/revision-0001/review_findings.md` |
| Root-cause repair groups in Cycle 18 Stage 5 | `3` (`mim-c18-s05-g001`..`g003`) | `reviews/workflow/mech-goal-sequence-20261019/cycle-000018/stage-05/revision-0001/issue_map.md` |
| Unassigned / ungrouped findings | `0` | `100%` of active finding families (`6/6`) assigned to groups `mim-c18-s05-g001`..`g003` |
| Immutable original review bundles modified in Stage 5 | `0` | `git status --short` / `.venv/bin/python scripts/record_review.py --repo-root . check` |

## 2. Group Coverage Matrix

| Group ID | Finding Family IDs | Instance Count | Distinct Records | Issue Tracker | Disposition | Carry-Forward |
| --- | --- | ---: | ---: | --- | --- | --- |
| `mim-c18-s05-g001` | `mim-c01-s04-f001` | `1` | `1` | `#921` (`OPEN`) | `deferred` | `mim-c01-s04-f001` |
| `mim-c18-s05-g002` | `mim-c01-s04-f003` | `19` | `19` | `#923` (`OPEN`) | `deferred` | `mim-c01-s04-f003` |
| `mim-c18-s05-g003` | `mim-c01-s04-f004`, `mim-c01-s04-f005`, `mim-c01-s04-f006`, `mim-c01-s04-f007` | `950` | `926` | `#718` (`OPEN`; `#861` `CLOSED`) | `deferred` | `mim-c01-s04-f004`, `mim-c01-s04-f005`, `mim-c01-s04-f006`, `mim-c01-s04-f007` |
| **Total** | **`6` families** | **`970`** | **`940` unique** | **`3` open issues (`#921`, `#923`, `#718`)** | **`100%` accounted** | **`6` carried forward** |
