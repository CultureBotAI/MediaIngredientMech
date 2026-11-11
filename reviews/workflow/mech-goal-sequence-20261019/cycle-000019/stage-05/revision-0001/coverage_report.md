# Cycle 19 Stage 05 (`resolve_review_findings`) — Finding & Group Coverage Report

- **Run ID:** `mech-goal-sequence-20261019`
- **Cycle:** `19`
- **Stage:** `5` (`resolve_review_findings`)
- **Repository:** `CultureBotAI/MediaIngredientMech` (`mediaingredientmech`)
- **Consumed Stage 04 Review Evidence:** [`reviews/workflow/mech-goal-sequence-20261019/cycle-000019/stage-04/revision-0001/evidence.yaml`](../stage-04/revision-0001/evidence.yaml) (`sha256: c984ff194eda5ecfbed294c31d802d2b06730fa2a1ca4c62d542cb392e17e211`, merged via PR `#1359`, merge commit `c27c53e3b50e769c15643e4ae94d9989a034a325`)
- **Tracked Evidence Latest Index:** [`reviews/workflow/latest.yaml`](../../../../latest.yaml) (`sha256: 6876e9a5f697eaafb5e29cbd3b5cf78ecfeb2841c6627948b43a5ab0e6c420dd`, `55` verified entries through Cycle 19 Stage 4 PR `#1359`, `receipt_sha256: a697680afd0b3396df96b89196dde8a10de03f39f93951b4e31bd5c82edfc203`)

## 1. Corpus & Finding Accounting

| Metric | Value | Verification Source |
| --- | ---: | --- |
| Individual ingredient records | `2,956` (`2,854` mapped + `102` unmapped) | `data/ingredients/{mapped,unmapped}/*.yaml` |
| Collection / ontology / mapping files | `7` | `data/curated/*.yaml`, `data/ontologies/*.yaml`, `mappings/*.tsv` |
| Structured review bundles | `1,015` (`971` individual + `44` cohort; `2,030` files) | `.venv/bin/python scripts/record_review.py --repo-root . check` |
| Historical review findings resolved in Cycle 1 Stage 5 | `1` (`mim-c01-s04-f002`, PR `#922` / Issue `#920`) | `reviews/records/structured/cohort/batch_0001-20261019T065629Z/review.yaml` |
| Active Stage 4 finding families consumed in Cycle 19 Stage 5 | `6` (`mim-c01-s04-f001`, `mim-c01-s04-f003`..`f007`) | `reviews/workflow/mech-goal-sequence-20261019/cycle-000019/stage-04/revision-0001/evidence.yaml` |
| Total active finding instances across `6` families | `970` (`1` + `19` + `624` + `29` + `266` + `31`) | `reviews/workflow/mech-goal-sequence-20261019/cycle-000019/stage-04/revision-0001/review_findings.md` |
| Root-cause repair groups in Cycle 19 Stage 5 | `3` (`mim-c19-s05-g001`..`g003`) | `reviews/workflow/mech-goal-sequence-20261019/cycle-000019/stage-05/revision-0001/issue_map.md` |
| Unassigned / ungrouped findings | `0` | `100%` of active finding families (`6/6`) assigned to groups `mim-c19-s05-g001`..`g003` |
| Immutable original review bundles modified in Stage 5 | `0` | `git status --short` / `.venv/bin/python scripts/record_review.py --repo-root . check` |

## 2. Group Coverage Matrix

| Group ID | Finding Family IDs | Instance Count | Distinct Records | Issue Tracker | Disposition | Carry-Forward |
| --- | --- | ---: | ---: | --- | --- | --- |
| `mim-c19-s05-g001` | `mim-c01-s04-f001` | `1` | `1` | `#921` (`OPEN`) | `deferred` | `mim-c01-s04-f001` |
| `mim-c19-s05-g002` | `mim-c01-s04-f003` | `19` | `19` | `#923` (`OPEN`) | `deferred` | `mim-c01-s04-f003` |
| `mim-c19-s05-g003` | `mim-c01-s04-f004`, `mim-c01-s04-f005`, `mim-c01-s04-f006`, `mim-c01-s04-f007` | `950` | `926` | `#718` (`OPEN`; `#861` `CLOSED`) | `deferred` | `mim-c01-s04-f004`, `mim-c01-s04-f005`, `mim-c01-s04-f006`, `mim-c01-s04-f007` |
| **Total** | **`6` families** | **`970`** | **`940` unique** | **`3` open issues (`#921`, `#923`, `#718`)** | **`100%` accounted** | **`6` carried forward** |
