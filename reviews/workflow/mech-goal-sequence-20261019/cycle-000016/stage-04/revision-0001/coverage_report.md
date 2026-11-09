# Cycle 16 Stage 4 Coverage Report (`record_review`)

- **Run ID**: `mech-goal-sequence-20261019`
- **Cycle**: `16` (`cycle-000016`)
- **Stage**: `4` (`stage-04` / `record_review`)
- **Revision**: `revision-0001`
- **Base Commit (`main`)**: `f9e11194d768bcf67cd5a9d5aecff540223fa98b`

---

## 1. Frozen Corpus Coverage Accounting

| Metric | Count | Percentage / Notes |
| --- | ---: | --- |
| Total individual ingredient YAML records (`data/ingredients/**/*.yaml`) | `2,956` | `100.00%` of individual ingredient records (`2,681` in `data/ingredients/mapped/` + `275` in `data/ingredients/unmapped/`) |
| Mapped status (`mapping_status: MAPPED`) | `2,611` | `88.33%` of individual corpus (`2,611 / 2,956`) |
| Unmapped status (`mapping_status: UNMAPPED`) | `262` | `8.86%` of individual corpus (`262 / 2,956`; includes `Na2moo4_X_H2o.yaml` [`UNMAPPED_0851`] and `Trisodium_Citrate_X_3_H2o.yaml` [`UNMAPPED_0852`] split in PR `#1026`) |
| Ambiguous status (`mapping_status: AMBIGUOUS`) | `1` | `0.03%` of individual corpus (`data/ingredients/unmapped/Unmapped_Ingredient_1.yaml`) |
| Rejected status (`mapping_status: REJECTED`) | `82` | `2.77%` of individual corpus (`70` in `data/ingredients/mapped/`, including `Carnitine_Dl_Hydrochloride.yaml` merged in PR `#1042`, + `12` in `data/ingredients/unmapped/`) |
| Curated collection YAML files (`data/curated/*.yaml`) | `7` | `mapped_ingredients.yaml`, `unmapped_ingredients.yaml`, `complex_ingredients.yaml`, `media_ingredients.yaml`, `unmapped_Bottle_ingredients.yaml`, `unmapped_bottle_plates_ingredients.yaml`, `unmapped_media_ingredients.yaml` |
| Total YAML documents validated | `2,963` | `2,956` individual records + `7` curated collections |
| Individual records reviewed in `reviews/structured/` (`targets:`) | `2,956` | `100.00%` (`962` in `kind: record` bundles, `2,954` in `kind: batch` bundles, `38` in `kind: repository` bundles, `3` in `kind: category` bundle) |
| Total structured review bundles (`reviews/structured/*/review.{yaml,md}`) | `1,015` | `2,030` files (`965` `kind: record` + `1` `kind: category` + `32` `kind: batch` + `17` `kind: repository`), `100.00%` passing `scripts/record_review.py --repo-root . check` |
| Records with active per-record findings (`needs_curation`) | `960` | `970` active findings (`644` `open` + `326` `deferred` in `20261017T083000Z-*`) across `6` open root-cause cohorts (`mim-c01-s04-f001`, `mim-c01-s04-f003`..`f007`), plus `2` split unmapped hydrate records (`UNMAPPED_0851`, `UNMAPPED_0852`) in `20261101T035857Z-approved-plan-step1-unified-review`, `8` open hydrate/stock holds in `20261102T061829Z-step7b-hydrate-stock-reconciliation`, and `29` excluded owner scientific holds in `20261103T060904Z-step7d-67-owner-scientific-author-review` |
| Records with resolved per-record findings (`pass_with_limitations`) | `2` | `data/ingredients/mapped/Ca_No32_X_4_H2o.yaml` (`mim-c01-s04-f002` / [#922](https://github.com/CultureBotAI/MediaIngredientMech/issues/922) via `20261021T120500Z-ca-no32-x-4-h2o`), `data/ingredients/mapped/Carnitine_Hydrochloride.yaml` (via `20261101T005710Z-carnitine-amide-alias-scientific` and `20261101T094737Z-approved-step3-carnitine-hydrochloride-review`) |
| Records with clean cohort reconciliation (`0` active per-record findings) | `1,994` | `1,994` individual records (`1,993` in `20261011T080001Z-mim-*`..`20261011T080014Z-mim-*` + `1` newly added mapped record `data/ingredients/mapped/25-didehydro-D-gluconate.yaml` [`CHEBI:11449`] verified in `20261102T224104Z-step7c-final-source-and-sssom-review`) |

---

## 2. Structured Review Bundle Distribution (`1,015` Bundles)

| Bundle Series | Kind | Bundles | Verdict Distribution | Target Records Covered |
| --- | --- | ---: | --- | --- |
| `reviews/structured/20261017T083000Z-*` | `record` | `961` | `961` `needs_curation` | `961` individual records (`971` initial findings; `960` records with `970` active findings after `20261021T120500Z-ca-no32-x-4-h2o`) |
| `reviews/structured/20261021T120500Z-ca-no32-x-4-h2o` | `record` | `1` | `1` `pass_with_limitations` | `1` individual record (`data/ingredients/mapped/Ca_No32_X_4_H2o.yaml`, `1` resolved finding `rec-f-5b1b1ab939d20218`) |
| `reviews/structured/20261101T*-{na2hpo4,melezitose,carnitine}*` | `record` | `3` | `1` `needs_curation`, `1` `blocked`, `1` `pass_with_limitations` | `3` individual records (`Na2hpo4_X_7_H2o.yaml`, `D-_-melezitose_Monohydrate.yaml`, `Carnitine_Hydrochloride.yaml`) |
| `reviews/structured/20261101T094737Z-approved-step3-carnitine-hydrochloride-review` | `category` | `1` | `1` `pass_with_limitations` | `12` targets (`3` ingredient records: `Carnitine_Dl_Hydrochloride.yaml`, `Carnitine_Hydrochloride.yaml`, `L-Carnitine_Hcl.yaml`) |
| `reviews/structured/20261011T080001Z-mim-*` .. `20261011T080014Z-mim-*` | `batch` | `14` | `13` `needs_curation`, `1` `not_assessed` | `2,953` individual records across `14` deterministic alphabetical cohorts |
| `reviews/structured/20261101T*` .. `20261104T*` (`batch`) | `batch` | `18` | `8` `pass_with_limitations`, `8` `needs_curation`, `2` `blocked` | Focused curation, diagnostics, and reconciliation batches across PRs `#1007`, `#1062`, `#1083`, `#1094`, `#1115`, `#1128`, `#1136` (including `25-didehydro-D-gluconate.yaml` in `20261102T224104Z-step7c-final-source-and-sssom-review`) |
| `reviews/structured/20261101T*` .. `20261102T*` (`repository`) | `repository` | `17` | `16` `pass_with_limitations`, `1` `needs_curation` | Repository-scoped curation, SSSOM, and hydrate/salt verification bundles across PRs `#1007`, `#1026`, `#1030`, `#1048`, `#1062`, `#1076`, `#1083`, `#1094`, `#1106` (including `Na2moo4_X_H2o.yaml` and `Trisodium_Citrate_X_3_H2o.yaml`) |
| **Total** | **All** | **`1,015`** | **`984` `needs_curation`, `27` `pass_with_limitations`, `3` `blocked`, `1` `not_assessed`** | **`2,956 / 2,956` (`100.00%`) individual ingredient records** |
