# Cycle 3 Stage 4 Coverage & Provenance Report (`record_review`)

- **Run ID**: `mech-goal-sequence-20261019`
- **Cycle**: `3` (`cycle-000003`)
- **Stage**: `4` (`stage-04` / `record_review` / `review_yaml_records`)
- **Revision**: `revision-0001`
- **Source Revision (`main`)**: `524fa44d989b3e272cb3bff9d68e53d02407dac7`
- **Scope Frozen At**: `2026-10-23T12:15:00Z`

---

## 1. Corpus Coverage Accounting (`100%`)

| Inventory Slice | Eligible Count | Reviewed Count | Coverage | Pass (`0` Active Findings) | Active Finding Records | Active Finding Count |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `data/ingredients/mapped/*.yaml` (`MAPPED`) | `2,609` | `2,609` | `100.0%` | `1,910` | `699` | `705` |
| `data/ingredients/mapped/*.yaml` (`REJECTED`) | `71` | `71` | `100.0%` | `71` | `0` | `0` |
| `data/ingredients/unmapped/*.yaml` (`MAPPED`) | `2` | `2` | `100.0%` | `2` | `0` | `0` |
| `data/ingredients/unmapped/*.yaml` (`UNMAPPED`) | `260` | `260` | `100.0%` | `0` | `260` | `264` |
| `data/ingredients/unmapped/*.yaml` (`AMBIGUOUS`) | `1` | `1` | `100.0%` | `0` | `1` | `1` |
| `data/ingredients/unmapped/*.yaml` (`REJECTED`) | `10` | `10` | `100.0%` | `10` | `0` | `0` |
| **Total Individual `IngredientRecord` YAMLs** | **`2,953`** | **`2,953`** | **`100.0%`** | **`1,993`** | **`960`** | **`970`** |
| Active collection YAMLs (`data/curated/*.yaml`) | `3` | `3` | `100.0%` | `3` | `0` | `0` |
| Historical collection snapshots (`data/curated/*pre_reclassify.yaml`, `*.bak`) | `4` | `4` | `100.0%` | `4` | `0` | `0` |
| **Total YAML Documents Audited** | **`2,960`** | **`2,960`** | **`100.0%`** | **`2,000`** | **`960`** | **`970`** |

---

## 2. Native Structured Review Bundle Accounting (`976` Bundles)

All `976` structured review bundles in `reviews/structured/` (`1,952` `review.yaml` + `review.md` files; manifest `sha256: 17c962c558829428cc5c6df8c8be66afa4791c20b781b60a846e6695d038bb6f`) are validated by `.venv/bin/python scripts/record_review.py check`:

| Bundle Cohort | Bundle Count | Scope Type | Verdict Distribution |
| --- | ---: | --- | --- |
| Initial per-record review bundles (`20261017T083000Z-*`) | `961` | `record` (`1` record per bundle) | `960` active (`needs_follow_up`), `1` superseded (`20261017T083000Z-ca-no32-x-4-h2o`) |
| Post-remediation successor bundle (`20261021T120500Z-ca-no32-x-4-h2o`) | `1` | `record` (`data/ingredients/mapped/Ca_No32_X_4_H2o.yaml`) | `1` `pass` (`0` active findings; supersedes `20261017T083000Z-ca-no32-x-4-h2o` & `20261011T211000Z-mim-ca-no32-x-4-h2o-occurrence-total`) |
| Corpus-wide & cohort reconciliation bundles (`20261011T*-mim-*`) | `14` | `category` (`2,953` individual records + `7` collection files) | `8` `pass`, `6` `needs_follow_up` |
| **Total Native Structured Review Bundles** | **`976`** | — | **`valid_reviews: 976` (`0` stale `source_sha256`)** |

---

## 3. Overlap Matrix Across Active Finding Cohorts (`960` Unique Records, `970` Active Findings)

| Cohort Pair / Combination | Record Count | Affected Records |
| --- | ---: | --- |
| `mim-c01-s04-f001` + `mim-c01-s04-f004` | `1` | `data/ingredients/mapped/(2)-D-lyxose.yaml` |
| `mim-c01-s04-f003` + `mim-c01-s04-f004` | `3` | `data/ingredients/mapped/H3bo4.yaml`, `data/ingredients/mapped/Magnesium_Chloride_Anhydrous.yaml`, `data/ingredients/mapped/Mnso4_X_7_H2o.yaml` |
| `mim-c01-s04-f003` + `mim-c01-s04-f006` | `1` | `data/ingredients/mapped/Modified_Pfennig_Medium_Sl-8_Solution_B_Medium_28.yaml` |
| `mim-c01-s04-f003` + `mim-c01-s04-f007` | `1` | `data/ingredients/mapped/Trace_Element_Solution_Sl-8_Medium_192.yaml` |
| `mim-c01-s04-f006` (`2` findings in same cohort on same record) | `4` | `data/ingredients/unmapped/Buffer.yaml`, `data/ingredients/unmapped/Mineral_salt_solution.yaml`, `data/ingredients/unmapped/Salt_solution.yaml`, `data/ingredients/unmapped/Standard_vitamin_solution.yaml` |
| Single-finding records across `mim-c01-s04-f003` .. `mim-c01-s04-f007` | `950` | `14` (`f003`-only) + `620` (`f004`-only) + `29` (`f005`-only) + `257` (`f006`-only) + `30` (`f007`-only) |
| **Total Unique Records with Active Findings** | **`960`** | **`970` total active findings** |
