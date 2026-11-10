# Cycle 17 Stage 05 (`resolve_review_findings`) — Finding & Group Coverage Report

- **Run ID:** `mech-goal-sequence-20261019`
- **Cycle:** `17`
- **Stage:** `5` (`resolve_review_findings`)
- **Repository:** `CultureBotAI/MediaIngredientMech` (`mediaingredientmech`)
- **Consumed Stage 04 Review Evidence:** [`reviews/workflow/mech-goal-sequence-20261019/cycle-000017/stage-04/revision-0001/evidence.yaml`](../stage-04/revision-0001/evidence.yaml) (`sha256: 5d9e289adcc7771d7703a0c3fd02c26e4758660cc5a7f743b545a5e9e153d517`, merged via PR `#1306`, merge commit `1f61f36db6e059d600af6032b6bc5a40e60583eb`)
- **Tracked Evidence Latest Index:** [`reviews/workflow/latest.yaml`](../../../../latest.yaml) (`sha256: 82e80c98258075682f62dc5d02cb78a0df3a523a7cded9a786cd3a6ae48a2632`, `49` verified entries through Cycle 17 Stage 4 PR `#1306`, `receipt_sha256: b07bdc8ca945375f33f3e26af294e9d776bc88659f3eb8c32c3e4b914e066299`)

## 1. Corpus & Finding Accounting

| Metric | Value | Verification Source |
| --- | ---: | --- |
| Individual ingredient records | `2,956` (`2,854` mapped + `102` unmapped) | `data/ingredients/{mapped,unmapped}/*.yaml` |
| Collection / ontology / mapping files | `7` | `data/curated/*.yaml`, `data/ontologies/*.yaml`, `mappings/*.tsv` |
| Structured review bundles | `1,015` (`971` individual + `44` cohort; `2,030` files) | `.venv/bin/python scripts/record_review.py --repo-root . check` |
| Historical review findings resolved in Cycle 1 Stage 5 | `1` (`mim-c01-s04-f002`, PR `#922` / Issue `#920`) | `reviews/records/structured/cohort/batch_0001-20261019T065629Z/review.yaml` |
| Active Stage 4 finding families consumed in Cycle 17 Stage 5 | `6` (`mim-c01-s04-f001`, `mim-c01-s04-f003`..`f007`) | `reviews/workflow/mech-goal-sequence-20261019/cycle-000017/stage-04/revision-0001/evidence.yaml` |
| Total active finding instances across `6` families | `970` (`1` + `19` + `624` + `29` + `266` + `31`) | `reviews/workflow/mech-goal-sequence-20261019/cycle-000017/stage-04/revision-0001/review_findings.md` |
| Root-cause repair groups in Cycle 17 Stage 5 | `3` (`mim-c17-s05-g001`..`g003`) | `reviews/workflow/mech-goal-sequence-20261019/cycle-000017/stage-05/revision-0001/issue_map.md` |
| Unassigned / ungrouped findings | `0` | `100%` of active finding families (`6/6`) assigned to groups `mim-c17-s05-g001`..`g003` |
| Immutable original review bundles modified in Stage 5 | `0` | `git status --short` / `.venv/bin/python scripts/record_review.py --repo-root . check` |

## 2. Group Coverage Matrix

| Group ID | Finding Family IDs | Instance Count | Distinct Records | Issue Tracker | Disposition | Carry-Forward |
| --- | --- | ---: | ---: | --- | --- | --- |
| `mim-c17-s05-g001` | `mim-c01-s04-f001` | `1` | `1` | `#921` (`OPEN`) | `deferred` | `mim-c01-s04-f001` |
| `mim-c17-s05-g002` | `mim-c01-s04-f003` | `19` | `19` | `#923` (`OPEN`) | `deferred` | `mim-c01-s04-f003` |
| `mim-c17-s05-g003` | `mim-c01-s04-f004`, `mim-c01-s04-f005`, `mim-c01-s04-f006`, `mim-c01-s04-f007` | `950` | `926` | `#718` (`OPEN`; `#861` `CLOSED`) | `deferred` | `mim-c01-s04-f004`, `mim-c01-s04-f005`, `mim-c01-s04-f006`, `mim-c01-s04-f007` |
| **Total** | **`6` families** | **`970`** | **`940` unique** | **`3` open issues (`#921`, `#923`, `#718`)** | **`100%` accounted** | **`6` carried forward** |
