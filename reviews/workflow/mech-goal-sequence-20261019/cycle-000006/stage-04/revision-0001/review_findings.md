# MediaIngredientMech Cycle 6 Stage 4 Consolidated Review Findings Ledger

- **Run ID:** `mech-goal-sequence-20261019`
- **Cycle / Stage / Revision:** `cycle-000006` / `stage-04` (`record_review`) / `revision-0001`
- **Reviewed Baseline Commit:** `9fb04881e08fc2c9a0ee3efaabb79ddb050dfe11`
- **Previous Stage 5 Evidence:** `reviews/workflow/mech-goal-sequence-20261019/cycle-000005/stage-05/revision-0001/evidence.yaml` (`sha256: 0c2d8864bbd5e518798f5f0020ebf7a700d905058c4483fa79facca756be35aa`)

---

## 1. Workflow-Level Findings Carried Forward to Cycle 6 Stage 5

| Finding ID | Status | Severity | Rule / Cohort ID | Affected Records | Native Bundle Anchor(s) | Summary & Required Stage 5 Action |
| --- | --- | --- | --- | ---: | --- | --- |
| `mim-c01-s04-f001` | `open` | `warning` | `unmapped-grounding-backlog` / `ambiguous-grounding-status` | 261 (`260` `UNMAPPED`, `1` `AMBIGUOUS`) | `reviews/structured/20261017T083000Z-*/review.yaml` (`261` bundles; `265` findings including `4` `placeholder-synonym-noise`) | 260 unmapped records (`UNMAPPED_0001`–`UNMAPPED_0285`) and 1 ambiguous record (`UNMAPPED_0089`, `Bio.yaml`) lack primary ontology grounding (`CHEBI`/`FOODON`/`ENVO`/`UBERON`/`NCIT`/`kgmicrobe.ingredient`). Stage 5 action: track under Issue `#921`; curate verifiable single-substance mappings or decompose multi-part stocks where recipe provenance exists. |
| `mim-c01-s04-f002` | `resolved` | `error` | `hydrated-chebi-and-cas-gap` | 1 (`data/ingredients/mapped/Ca_No32_X_4_H2o.yaml`) | Superseded: `reviews/structured/20261017T083000Z-ca-no32-x-4-h2o/review.yaml`<br>Successor: `reviews/structured/20261021T120500Z-ca-no32-x-4-h2o/review.yaml` | Resolved in Cycle 1 Stage 5 (PR `#924`, Issue `#922`): added `CAS-RN:13477-34-4` (`EXACT_MATCH`) and `CHEBI:86159` (`calcium dinitrate tetrahydrate`, `EXACT_MATCH`) to `chemical_context.hydrate_form` and `ontology_cross_references`. Verified `0` open findings in successor bundle. |
| `mim-c01-s04-f003` | `open` | `warning` | `role-coverage-gap` | 637 (`data/ingredients/mapped/*.yaml`) | `reviews/structured/20261017T083000Z-*/review.yaml` (`637` bundles) | 637 active `MAPPED` records have empty `roles: []` (plus `6` additional `role-coverage-gap` findings on unmapped records). Stage 5 action: track under Issue `#923`; assign `IngredientRole` values only with per-record `RoleAssignment` + `Citation` provenance (`curate-yaml-record` / `ingredient-roles`). |
| `mim-c01-s04-f004` | `open` | `info` | `stock-component-partonomy-gap` | 67 (`data/ingredients/mapped/*.yaml`) | `reviews/structured/20261017T083000Z-*/review.yaml` (`67` bundles) | 67 mapped mixture/stock/medium records (out of `150` `kgmicrobe.ingredient:*` records; `83` already have `has_parts`) lack `StockComponent` decomposition. Stage 5 action: track under Issue `#923`; decompose via `add-media` when authoritative recipe composition is verified. |
| `mim-c01-s04-f005` | `open` | `warning` | `hydrate-parent-grounding` | 10 (`data/ingredients/mapped/*.yaml`) | `reviews/structured/20261011T024629Z-mim-reconcile-all-batch-01/review.yaml` .. `batch-13/review.yaml` | 10 mapped hydrate records (`CoCl2_X_2_H2O.yaml`, `Fe2_So43_X_N_H2o.yaml`, `FeCl2_X_2_H2O.yaml`, `FeSO4_X_H2O.yaml`, `MnCl2_X_2_H2O.yaml`, `MnSO4_X_7_H2O.yaml`, `Na2MoO4_X_H2O.yaml`, `Na2SeO3_X_6_H2O.yaml`, `Na2S_X_7_9_H2O.yaml`, `SnCl2_X_H2O.yaml`) intentionally share parent anhydrous CHEBI IDs (`RELATED_MATCH` / `CLOSE_MATCH`) because ChEBI lacks specific hydrate terms; allowlisted in `scripts/audit_duplicate_identifiers.py`. |
| `mim-c01-s04-f006` | `open` | `info` | `curation-history-timestamp-format` | 2,953 (`data/ingredients/{mapped,unmapped}/*.yaml`) | `reviews/structured/20261011T024629Z-mim-reconcile-all-batch-01/review.yaml` .. `batch-13/review.yaml` | `scripts/validate_strict.py` reports `5,897` non-blocking `WARN` rows (`0` `ERROR` rows) for microsecond-precision ISO-8601 timestamps in historical `curation_history[].timestamp` slots. Stage 5 action: tracked under Issue `#923` / `INFRA_TASKS.md` (`INFRA-002`). |
| `mim-c01-s04-f007` | `open` | `info` | `rejected-tombstone-retention` | 81 (`69` in `mapped/`, `12` in `unmapped/`) | `reviews/structured/20261011T024629Z-mim-reconcile-all-batch-01/review.yaml` .. `batch-13/review.yaml` | 81 `mapping_status: REJECTED` records are retained as audit-trail tombstones for merged duplicates (`merged_into` provenance). Stage 5 action: tracked under Issue `#923` / `INFRA_TASKS.md` (`INFRA-003`). |

---

## 2. Native Per-Record Structured Findings Distribution (`970` Active Record-Level Findings Across `960` Records)

| Native Rule ID | Severity | Mapped Records (`data/ingredients/mapped/*.yaml`) | Unmapped Records (`data/ingredients/unmapped/*.yaml`) | Total Findings |
| --- | --- | ---: | ---: | ---: |
| `role-coverage-gap` | `warning` | 637 | 6 | 643 |
| `unmapped-grounding-backlog` | `warning` | 0 | 254 | 254 |
| `stock-component-partonomy-gap` | `info` | 67 | 0 | 67 |
| `placeholder-synonym-noise` | `info` | 0 | 4 | 4 |
| `ambiguous-grounding-status` | `warning` | 0 | 1 | 1 |
| `unmapped-curie-in-mapped-dir` | `warning` | 1 (`Unmapped_0151_Buffer.yaml`, mapped to `kgmicrobe.ingredient:buffered_peptone_water`) | 0 | 1 |
| **Total Active Native Findings** | — | **705 (across 699 records)** | **265 (across 261 records)** | **970 (across 960 records)** |
