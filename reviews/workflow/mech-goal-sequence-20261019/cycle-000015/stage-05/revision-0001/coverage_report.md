# MediaIngredientMech Cycle 15 Stage 5 Coverage Report

- **Run ID:** `mech-goal-sequence-20261019`
- **Cycle:** `15` (`cycle-000015`)
- **Stage:** `5` (`stage-05` / `resolve_review_findings`)
- **Revision:** `1` (`revision-0001`)
- **Source Revision:** `f956c9b43fb286d49abb9a500f57011cbdf117b0`
- **Scope Frozen At:** `2026-11-09T05:52:35Z`
- **Consumed Stage 4 Evidence:** `reviews/workflow/mech-goal-sequence-20261019/cycle-000015/stage-04/revision-0001/evidence.yaml` (`sha256: 2e0e5905f2a976ed7201b13f5700862fdbcecab15c8af1a4bda94911a3c42f8c`)

---

## 1. Stage 4 Finding Intake & Stage 5 Resolution Coverage

| Metric | Value | Notes |
| --- | ---: | --- |
| Total individual `IngredientRecord` YAML files in corpus | `2,956` | `2,681` files in `data/ingredients/mapped/*.yaml` (`2,611` `MAPPED` + `70` `REJECTED`) + `275` files in `data/ingredients/unmapped/*.yaml` (`262` `UNMAPPED` + `1` `AMBIGUOUS` + `12` `REJECTED`); by `mapping_status`: `2,611` `MAPPED` + `262` `UNMAPPED` + `1` `AMBIGUOUS` + `82` `REJECTED` (reviewed at Stage 4 base revision `1ee414ec38d33841a2c2e8c1bd477b17680669e2` and merged to `main` at `f956c9b43fb286d49abb9a500f57011cbdf117b0` via PR `#1283`) |
| Records passing with `0` active findings | `1,996` | Including `data/ingredients/mapped/Ca_No32_X_4_H2o.yaml` resolved in Cycle 1 Stage 5 under [#922](https://github.com/CultureBotAI/MediaIngredientMech/issues/922), `data/ingredients/mapped/Carnitine_Hydrochloride.yaml` added in PR `#1042`, and `data/ingredients/mapped/25-didehydro-D-gluconate.yaml` added in PR `#1094` / reviewed in PR `#1115` |
| Consumed Cycle 15 Stage 4 root-cause finding cohorts | `6` | `mim-c01-s04-f001`, `mim-c01-s04-f003`, `mim-c01-s04-f004`, `mim-c01-s04-f005`, `mim-c01-s04-f006`, `mim-c01-s04-f007` |
| Consumed active per-record findings across `960` records | `970` | `1` (`f001`) + `19` (`f003`) + `624` (`f004`) + `29` (`f005`) + `266` (`f006`) + `31` (`f007`) |
| Root-cause & repair-ownership groups formed in Stage 5 | `3` | `mim-c15-s05-g001` ([#921](https://github.com/CultureBotAI/MediaIngredientMech/issues/921)), `mim-c15-s05-g002` ([#923](https://github.com/CultureBotAI/MediaIngredientMech/issues/923)), `mim-c15-s05-g003` ([#718](https://github.com/CultureBotAI/MediaIngredientMech/issues/718)) |
| Stage 4 findings accounted for in Stage 5 (`100%` partition) | `6 / 6` | `0` ungrouped findings; `6` deferred with documented byte-binding and source-curation blockers in `carry_forward_ids` |
| Tracked review index (`reviews/workflow/latest.yaml`) entries | `43` | Synchronized from `verified-evidence-index.json` (Cycle 1 Stage 4 `#919`, Cycle 1 Stage 5 `#924`, Cycle 1 Stage 6 `#926`, Cycle 2 Stage 4 `#930`, Cycle 2 Stage 5 `#932`, Cycle 2 Stage 6 `#934`, Cycle 3 Stage 4 `#938`, Cycle 3 Stage 5 `#939`, Cycle 3 Stage 6 `#940`, Cycle 4 Stage 4 `#944`, Cycle 4 Stage 5 `#945`, Cycle 4 Stage 6 `#946`, Cycle 5 Stage 4 `#950`, Cycle 5 Stage 5 `#951`, Cycle 5 Stage 6 `#952`, Cycle 6 Stage 4 `#956`, Cycle 6 Stage 5 `#958`, Cycle 6 Stage 6 `#959`, Cycle 7 Stage 4 `#970`, Cycle 7 Stage 5 `#972`, Cycle 7 Stage 6 `#973`, Cycle 8 Stage 4 `#977`, Cycle 8 Stage 5 `#978`, Cycle 8 Stage 6 `#979`, Cycle 9 Stage 4 `#983`, Cycle 9 Stage 5 `#984`, Cycle 9 Stage 6 `#985`, Cycle 10 Stage 4 `#989`, Cycle 10 Stage 5 `#990`, Cycle 10 Stage 6 `#991`, Cycle 11 Stage 4 `#995`, Cycle 11 Stage 5 `#996`, Cycle 11 Stage 6 `#997`, Cycle 12 Stage 4 `#1002`, Cycle 12 Stage 5 `#1011`, Cycle 12 Stage 6 `#1024`, Cycle 13 Stage 4 `#1127`, Cycle 13 Stage 5 `#1129`, Cycle 13 Stage 6 `#1135`, Cycle 14 Stage 4 `#1141`, Cycle 14 Stage 5 `#1142`, Cycle 14 Stage 6 `#1143`, Cycle 15 Stage 4 `#1283`) |

---

## 2. Partition Verification by Group

1. **`mim-c15-s05-g001` -> [#921](https://github.com/CultureBotAI/MediaIngredientMech/issues/921) (`OPEN`)**:
   - Finding IDs: `["mim-c01-s04-f001"]` (`1` finding on `data/ingredients/mapped/(2)-D-lyxose.yaml`, `CHEBI:62318`).
   - Status: `deferred` (byte-bound in `reports/sssom_completion_20260921/mapping_review/nonmapping_cohorts.json` and `reports/semantic_review_20260921/resolution/current-review.json`; co-located with `SEM:cd74f8ddafa04d7e9a9a`).
2. **`mim-c15-s05-g002` -> [#923](https://github.com/CultureBotAI/MediaIngredientMech/issues/923) (`OPEN`)**:
   - Finding IDs: `["mim-c01-s04-f003"]` (`19` findings across `19` mapped records).
   - Status: `deferred` (`19/19` affected records are byte-bound in `reports/sssom_completion_20260921/review.json["record_inputs"]` and `reports/semantic_review_20260921/resolution/current-review.json["record_inputs"]`, including `17` `SUPPORTED` and `5` in `nonmapping_cohorts.json`; `src/mediaingredientmech/record_refresh.py` forbids preserving byte-bound approvals via receipt chains across YAML byte edits).
3. **`mim-c15-s05-g003` -> [#718](https://github.com/CultureBotAI/MediaIngredientMech/issues/718) (`OPEN`)**:
   - Finding IDs: `["mim-c01-s04-f004", "mim-c01-s04-f005", "mim-c01-s04-f006", "mim-c01-s04-f007"]` (`950` findings across `926` distinct records).
   - Status: `deferred` (requires organism/recipe-backed `Citation` objects (`doi`/`pmid`), upstream recipe identity grounding, and semantic-release resolution ledger updates).
