# MediaIngredientMech Cycle 12 Stage 4 Coverage Report

- **Run ID:** `mech-goal-sequence-20261019`
- **Cycle / Stage / Revision:** `cycle-000012` / `stage-04` (`record_review`) / `revision-0001`
- **Reviewed Baseline Commit:** `4625afd492b6cf43e3b499d1425d2453d490009d`

## 1. Frozen Inventory Coverage Summary

| Corpus Segment | Path Pattern | Document Count | Reviewed Count | Records with Active Findings | Clean Records (`0` Active Findings) |
| --- | --- | ---: | ---: | ---: | ---: |
| Mapped individual records (`mapping_status: MAPPED`) | `data/ingredients/mapped/*.yaml` | 2,611 | 2,611 | 699 (705 findings) | 1,912 |
| Unmapped / ambiguous individual records (`UNMAPPED`: 260, `AMBIGUOUS`: 1) | `data/ingredients/unmapped/*.yaml` | 261 | 261 | 261 (265 findings) | 0 |
| Rejected tombstones (`mapping_status: REJECTED`; 69 in `mapped/`, 12 in `unmapped/`) | `data/ingredients/mapped/*.yaml`, `data/ingredients/unmapped/*.yaml` | 81 | 81 | 0 (0 findings) | 81 |
| Individual `IngredientRecord` total | `data/ingredients/mapped/*.yaml` (2,680), `data/ingredients/unmapped/*.yaml` (273) | **2,953** | **2,953** | **960 (970 findings)** | **1,993** |
| Active collection YAML files | `data/curated/*.yaml` | **7** | **7** | (covered via per-record & aggregate checks) | - |
| **Total validated YAML corpus** | `data/ingredients/*/*.yaml` + `data/curated/*.yaml` | **2,960** | **2,960** | **960 (970 findings)** | **1,993** |

## 2. Native Structured Review Bundle Breakdown (`976` Bundles)

| Bundle Series | Pattern | Bundle Count | Scope Covered | Notes |
| --- | --- | ---: | --- | --- |
| Initial per-record review bundles | `reviews/structured/20261017T083000Z-*/review.{yaml,md}` | `961` | `961` individual records (`960` with active findings + `1` superseded by `20261021T120500Z-ca-no32-x-4-h2o`) | Merged in PR `#908` |
| Successor per-record review bundle | `reviews/structured/20261021T120500Z-ca-no32-x-4-h2o/review.{yaml,md}` | `1` | `data/ingredients/mapped/Ca_No32_X_4_H2o.yaml` (`verdict: pass_with_limitations`, `native_verdict: mapping_status=MAPPED; open=0; deferred=0; resolved=1`, `0` open findings) | Merged in Cycle 1 Stage 5 (Issue `#922`, `mim-c01-s04-f002`) |
| Corpus-wide reconciliation batch bundles | `reviews/structured/20261011T*-mim-*/review.{yaml,md}` | `14` | `13` disjoint batches (`20261011T024629Z-mim-reconcile-all-batch-01` .. `20261011T024640Z-mim-reconcile-all-batch-13`) covering all `2,953` individual records + `1` token-scope reassessment successor | Indexed in `reviews/reconciliation/20261011T023739Z-all-mim/README.md` |
| **Total validated structured bundles** | `reviews/structured/**/review.{yaml,md}` | **`976`** | **`2,953 / 2,953` (`100.0%`) individual records** | Verified via `.venv/bin/python scripts/record_review.py check` (`exit_code: 0`) |
