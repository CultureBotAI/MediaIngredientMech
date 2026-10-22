# MediaIngredientMech Cycle 2 Stage 5 Coverage Report

- **Run ID:** `mech-goal-sequence-20261019`
- **Cycle:** `2` (`cycle-000002`)
- **Stage:** `5` (`stage-05` / `resolve_review_findings`)
- **Revision:** `1` (`revision-0001`)
- **Source Revision:** `7f56a13130d8d220efa48cef78559e80351c5a46`
- **Scope Frozen At:** `2026-10-22T08:20:00Z`
- **Consumed Stage 4 Evidence:** `reviews/workflow/mech-goal-sequence-20261019/cycle-000002/stage-04/revision-0001/evidence.yaml` (`sha256: 98456ad5e221f87e55a88f089a3ae77320d5ae1115e4e209926bff1b6c72fdcc`)

---

## 1. Stage 4 Finding Intake & Stage 5 Resolution Coverage

| Metric | Value | Notes |
| --- | ---: | --- |
| Total individual `IngredientRecord` YAML files in corpus | `2,953` | `2,680` files in `data/ingredients/mapped/*.yaml` (`2,611` `MAPPED` + `69` `REJECTED`) + `273` files in `data/ingredients/unmapped/*.yaml` (`260` `UNMAPPED` + `1` `AMBIGUOUS` + `12` `REJECTED`); by `mapping_status`: `2,611` `MAPPED` + `260` `UNMAPPED` + `1` `AMBIGUOUS` + `81` `REJECTED` |
| Records passing with `0` active findings | `1,993` | Includes `data/ingredients/mapped/Ca_No32_X_4_H2o.yaml` resolved in Cycle 1 Stage 5 under [#922](https://github.com/CultureBotAI/MediaIngredientMech/issues/922) |
| Consumed Cycle 2 Stage 4 root-cause finding cohorts | `6` | `mim-c01-s04-f001`, `mim-c01-s04-f003`, `mim-c01-s04-f004`, `mim-c01-s04-f005`, `mim-c01-s04-f006`, `mim-c01-s04-f007` |
| Consumed active per-record findings across `960` records | `970` | `1` (`f001`) + `19` (`f003`) + `624` (`f004`) + `29` (`f005`) + `266` (`f006`) + `31` (`f007`) |
| Root-cause & repair-ownership groups formed in Stage 5 | `3` | `mim-c02-s05-g001` ([#921](https://github.com/CultureBotAI/MediaIngredientMech/issues/921)), `mim-c02-s05-g002` ([#923](https://github.com/CultureBotAI/MediaIngredientMech/issues/923)), `mim-c02-s05-g003` ([#718](https://github.com/CultureBotAI/MediaIngredientMech/issues/718)) |
| Stage 4 findings accounted for in Stage 5 (`100%` partition) | `6 / 6` | `0` ungrouped findings; `6` deferred with documented byte-binding and source-curation blockers in `carry_forward_ids` |
| Tracked review index (`reviews/workflow/latest.yaml`) entries | `4` | Synchronized from `verified-evidence-index.json` (Cycle 1 Stage 4 `#919`, Cycle 1 Stage 5 `#924`, Cycle 1 Stage 6 `#926`, Cycle 2 Stage 4 `#930`) |

---

## 2. Partition Verification by Group

1. **`mim-c02-s05-g001` -> [#921](https://github.com/CultureBotAI/MediaIngredientMech/issues/921) (`OPEN`)**:
   - Finding IDs: `["mim-c01-s04-f001"]` (`1` finding on `data/ingredients/mapped/(2)-D-lyxose.yaml`, `CHEBI:62318`).
   - Status: `deferred` (byte-bound in `reports/sssom_completion_20260921/mapping_review/nonmapping_cohorts.json` and `reports/semantic_review_20260921/resolution/current-review.json`; co-located with `SEM:cd74f8ddafa04d7e9a9a`).
2. **`mim-c02-s05-g002` -> [#923](https://github.com/CultureBotAI/MediaIngredientMech/issues/923) (`OPEN`)**:
   - Finding IDs: `["mim-c01-s04-f003"]` (`19` findings across `19` mapped records).
   - Status: `deferred` (`19/19` affected records are byte-bound in `reports/sssom_completion_20260921/review.json["record_inputs"]` and `reports/semantic_review_20260921/resolution/current-review.json["record_inputs"]`, including `17` `SUPPORTED` and `5` in `nonmapping_cohorts.json`; `src/mediaingredientmech/record_refresh.py` forbids preserving byte-bound approvals via receipt chains across YAML byte edits).
3. **`mim-c02-s05-g003` -> [#718](https://github.com/CultureBotAI/MediaIngredientMech/issues/718) (`OPEN`)**:
   - Finding IDs: `["mim-c01-s04-f004", "mim-c01-s04-f005", "mim-c01-s04-f006", "mim-c01-s04-f007"]` (`950` findings across `926` distinct records).
   - Status: `deferred` (requires organism/recipe-backed `Citation` objects (`doi`/`pmid`), upstream recipe identity grounding, and semantic-release resolution ledger updates).
