# Cycle 3 Stage 4 Stable Review Findings (`review_findings`)

- **Run ID**: `mech-goal-sequence-20261019`
- **Cycle**: `3` (`cycle-000003`)
- **Stage**: `4` (`stage-04` / `record_review` / `review_yaml_records`)
- **Revision**: `revision-0001`
- **Source Revision (`main`)**: `524fa44d989b3e272cb3bff9d68e53d02407dac7`
- **Previous Evidence**: `reviews/workflow/mech-goal-sequence-20261019/cycle-000002/stage-05/revision-0001/evidence.yaml` (`sha256: ad70008f1b7348a8da9abea22a245585f32fc764a99869942b03f8baab955840`)

---

## 1. Carry-Forward Summary from Cycle 2 Stage 5

Between Cycle 2 Stage 5 (`7f56a13130d8d220efa48cef78559e80351c5a46`) and Cycle 3 Stage 4 (`524fa44d989b3e272cb3bff9d68e53d02407dac7`), `0` ingredient records or native structured review bundles changed. All `6` open root-cause cohorts (`mim-c01-s04-f001` and `mim-c01-s04-f003` .. `mim-c01-s04-f007`) that were deferred in Cycle 2 Stage 5 (`ad70008f1b7348a8da9abea22a245585f32fc764a99869942b03f8baab955840`) remain open on `main` (`970` active per-record findings across `960` records) and are carried forward with their original stable `finding_id` values (`carried_from: mim-c01-s04-f00*`) for Cycle 3 Stage 5 grouped remediation.

*(Cohort `mim-c01-s04-f002` on `data/ingredients/mapped/Ca_No32_X_4_H2o.yaml` was resolved in Cycle 1 Stage 5 under PR `#924` / issue `#922`, verified by successor review bundle `reviews/structured/20261021T120500Z-ca-no32-x-4-h2o/review.yaml` with `overall_verdict: pass` and `0` active findings.)*

| Finding ID | Carried From | Status | Tracked Issue | Affected Records | Active Findings | Summary |
| --- | --- | --- | --- | ---: | ---: | --- |
| `mim-c01-s04-f001` | `mim-c01-s04-f001` | `open` | [#921](https://github.com/CultureBotAI/MediaIngredientMech/issues/921) | `1` | `1` | Reconcile missing direct MicrobeDecoder occurrence on `data/ingredients/mapped/(2)-D-lyxose.yaml` (`CHEBI:62318`; native finding `rec-f-444b73747dddc915`) |
| `mim-c01-s04-f003` | `mim-c01-s04-f003` | `open` | [#923](https://github.com/CultureBotAI/MediaIngredientMech/issues/923) | `19` | `19` | Normalize non-monotonic `curation_history` timestamp order across `19` mapped ingredient records |
| `mim-c01-s04-f004` | `mim-c01-s04-f004` | `open` | [#718](https://github.com/CultureBotAI/MediaIngredientMech/issues/718) | `624` | `624` | Adjudicate prediction-only or empty primary nutritional/cellular role assertions lacking literature citations across `624` mapped records (`595` single-role + `29` multi-role; issue `#718`) |
| `mim-c01-s04-f005` | `mim-c01-s04-f005` | `open` | [#718](https://github.com/CultureBotAI/MediaIngredientMech/issues/718) | `29` | `29` | Adjudicate prediction-only or empty secondary physicochemical role assertions lacking literature citations across `29` mapped records (`17` single-role + `12` multi-role; issue `#718`) |
| `mim-c01-s04-f006` | `mim-c01-s04-f006` | `open` | [#718](https://github.com/CultureBotAI/MediaIngredientMech/issues/718) | `262` | `266` | Resolve exact chemical identity, preparation form, or complex parent scope across `262` unmapped/ambiguous records (`266` findings across `261` unmapped identity + `4` complex parent scope + `1` ambiguous `PYGS`; issue `#718`) |
| `mim-c01-s04-f007` | `mim-c01-s04-f007` | `open` | [#718](https://github.com/CultureBotAI/MediaIngredientMech/issues/718) | `31` | `31` | Adjudicate context-dependent exported synonym/CAS token scope and component source scope across `31` records (`17` nomenclature token scope + `13` component source scope + `1` Furaltadone CAS alias; issues `#718`, `#861`) |

---

## 2. Detailed Cohort Specifications

### 2.1 `mim-c01-s04-f001` — Missing Direct MicrobeDecoder Occurrence on `(2)-D-lyxose.yaml`
- **Status**: `open` (`carried_from: mim-c01-s04-f001`)
- **Tracked Issue**: [https://github.com/CultureBotAI/MediaIngredientMech/issues/921](https://github.com/CultureBotAI/MediaIngredientMech/issues/921)
- **Target Record**: `data/ingredients/mapped/(2)-D-lyxose.yaml` (`CHEBI:62318`, `sha256: 62258c9bdabaf8728fafb6923345fe4b24b9956069113896acb16e9631c1451e`)
- **Native Structured Review Bundles**:
  - `reviews/structured/20261017T083000Z-2-d-lyxose/review.yaml` (`finding_id: rec-f-444b73747dddc915`)
  - `reviews/structured/20261011T114631Z-mim-corpus-audit-s/review.yaml` (`finding_id: mim-20261011-114631-s-d-lyxose-occurrence`)
  - `reviews/structured/20261011T150500Z-mim-20261011-114631-s-d-lyxose-occurrence/review.yaml`
- **Evidence & Blocker**:
  - `data/ingredients/mapped/(2)-D-lyxose.yaml` records `SYNONYM_MERGER` history merging `D-lyxose` (`kgmicrobe.trait:d_lyxose`, `159` occurrences in `D-lyxose.yaml`), yet `occurrence_statistics.total_occurrences` is `4` (`PPLO Broth` recipes) and omits the `159` direct `MicrobeDecoder` occurrences.
  - `(2)-D-lyxose.yaml` is byte-bound (`owner_record_sha256: 62258c9bdabaf8728fafb6923345fe4b24b9956069113896acb16e9631c1451e`) in `reports/sssom_completion_20260921/mapping_review/nonmapping_cohorts.json` and `reports/semantic_review_20260921/resolution/current-review.json` (co-located with open role-evidence finding `SEM:cd74f8ddafa04d7e9a9a`). Under `src/mediaingredientmech/record_refresh.py`, modifying `(2)-D-lyxose.yaml` requires coordinated re-review of `SEM:cd74f8ddafa04d7e9a9a` and re-binding of `nonmapping_cohorts.json`.

### 2.2 `mim-c01-s04-f003` — Non-Monotonic `curation_history` Timestamps (`19` Mapped Records)
- **Status**: `open` (`carried_from: mim-c01-s04-f003`)
- **Tracked Issue**: [https://github.com/CultureBotAI/MediaIngredientMech/issues/923](https://github.com/CultureBotAI/MediaIngredientMech/issues/923)
- **Target Records (`19` mapped records)**:
  1. `data/ingredients/mapped/Agar.yaml` (`rec-f-2be9d7ca4acbf7ab`)
  2. `data/ingredients/mapped/Biotin.yaml` (`rec-f-2b60895f56e83539`)
  3. `data/ingredients/mapped/Disodium_Succinate.yaml` (`rec-f-48999ba19660a70f`)
  4. `data/ingredients/mapped/Glass_beads.yaml` (`rec-f-69da8cfdf2575034`)
  5. `data/ingredients/mapped/H3bo4.yaml` (`rec-f-50164a7fc4c9d311`)
  6. `data/ingredients/mapped/Macroelements_Stock_Solution_Ras.yaml` (`rec-f-2dc4ed776b13bcff`)
  7. `data/ingredients/mapped/Magnesium_Chloride_Anhydrous.yaml` (`rec-f-ac7b9d257c3a8267`)
  8. `data/ingredients/mapped/Mnso4_X_7_H2o.yaml` (`rec-f-07d737d09c44533e`)
  9. `data/ingredients/mapped/Modified_Pfennig_Medium_Sl-8_Solution_B_Medium_28.yaml` (`rec-f-ee0df63c2105ef80`)
  10. `data/ingredients/mapped/Nicotinic_Acid.yaml` (`rec-f-152d1590b0859d9e`)
  11. `data/ingredients/mapped/P-Aminobenzoic_Acid.yaml` (`rec-f-ffba74e1eb64b13c`)
  12. `data/ingredients/mapped/Pancreatic_Digest_Of_Casein.yaml` (`rec-f-184fb8425e1e9363`)
  13. `data/ingredients/mapped/Peptone.yaml` (`rec-f-d53075a18c448801`)
  14. `data/ingredients/mapped/Vitamin_B12.yaml` (`rec-f-9979541371a79d15`)
  15. `data/ingredients/mapped/Salt_Solution_Medium_27.yaml` (`rec-f-a1f6215c749d8bc7`)
  16. `data/ingredients/mapped/Trace_Element_Solution_Sl-8_Medium_192.yaml` (`rec-f-854bb43eb425a824`)
  17. `data/ingredients/mapped/Trypticase.yaml` (`rec-f-b8ba84dd125df3c2`)
  18. `data/ingredients/mapped/Tryptone.yaml` (`rec-f-8a4cfdb7ff098664`)
  19. `data/ingredients/mapped/Yeast_Extract.yaml` (`rec-f-1f3331cd0fa4fc43`)
- **Native Structured Review Bundles**:
  - `reviews/structured/20261011T163951Z-mim-curation-history-order-mapped-a/review.yaml` (`9` records)
  - `reviews/structured/20261011T163952Z-mim-curation-history-order-mapped-b/review.yaml` (`10` remaining records; `Ca_No32_X_4_H2o.yaml` resolved in Cycle 1 Stage 5)
  - `19` individual bundles in `reviews/structured/20261017T083000Z-*/review.yaml`
- **Evidence & Blocker**:
  - Each of these `19` records contains a `2026-03-09T21:44:22.257115Z` `CURATOR_REVIEW` event inserted before `2026-03-09T06:53:*Z` `LLM_ASSISTED_CURATION` events.
  - All `19` records are byte-bound in `reports/sssom_completion_20260921/review.json` (`17` `SUPPORTED` + `2` `WITHHOLD`, with `5` also in `reports/sssom_completion_20260921/mapping_review/nonmapping_cohorts.json`) and `reports/semantic_review_20260921/resolution/current-review.json`. Under `src/mediaingredientmech/record_refresh.py`, `validate_record_refresh` rejects preserving byte-bound approvals through receipt chains when record bytes change.

### 2.3 `mim-c01-s04-f004` — Primary Nutritional & Cellular Role Assertions Lacking Literature Citations (`624` Mapped Records)
- **Status**: `open` (`carried_from: mim-c01-s04-f004`)
- **Tracked Issue**: [https://github.com/CultureBotAI/MediaIngredientMech/issues/718](https://github.com/CultureBotAI/MediaIngredientMech/issues/718)
- **Target Scope**: `624` mapped records (`624` active findings: `595` single-role assertions + `29` multi-role assertions across `CARBON_SOURCE`, `NITROGEN_SOURCE`, `MINERAL_SOURCE`, `TRACE_ELEMENT`, `VITAMIN_SOURCE`, `AMINO_ACID_SOURCE`, `ELECTRON_ACCEPTOR`, `ELECTRON_DONOR`, `GROWTH_FACTOR`, `COFACTOR_PROVIDER`, `SELECTIVE_AGENT`, `ANTIBIOTIC`, and `DEFINED_COMPONENT`).
- **Native Structured Review Bundles**:
  - `reviews/structured/20261011T183500Z-mim-semantic-review-20260921-active-findings/review.yaml` (`finding_id: mim-20261011-183500-role-evidence-primary`)
  - `624` individual bundles in `reviews/structured/20261017T083000Z-*/review.yaml`
- **Disposition**: Requires source-backed primary literature citations (`doi`/`pmid`) or recipe-specific functional validation; tracked in `reports/semantic_review_20260921/resolution/finding-dispositions.tsv` under `#718`.

### 2.4 `mim-c01-s04-f005` — Secondary Physicochemical Role Assertions Lacking Literature Citations (`29` Mapped Records)
- **Status**: `open` (`carried_from: mim-c01-s04-f005`)
- **Tracked Issue**: [https://github.com/CultureBotAI/MediaIngredientMech/issues/718](https://github.com/CultureBotAI/MediaIngredientMech/issues/718)
- **Target Scope**: `29` mapped records (`29` active findings: `17` single-role assertions + `12` multi-role assertions across `BUFFER`, `CHELATOR`, `PH_INDICATOR`, `REDOX_INDICATOR`, `REDUCING_AGENT`, `SURFACTANT`, `SOLIDIFYING_AGENT`, `CRYOPROTECTANT`, `OSMOPROTECTANT`, and `SOLVENT`).
- **Native Structured Review Bundles**:
  - `reviews/structured/20261011T183500Z-mim-semantic-review-20260921-active-findings/review.yaml` (`finding_id: mim-20261011-183500-role-evidence-physicochemical`)
  - `29` individual bundles in `reviews/structured/20261017T083000Z-*/review.yaml`
- **Disposition**: Requires primary literature or standard media handbook citations (`doi`/`pmid`); tracked in `reports/semantic_review_20260921/resolution/finding-dispositions.tsv` under `#718`.

### 2.5 `mim-c01-s04-f006` — Unmapped/Ambiguous Identity, Preparation Form, & Complex Parent Scope (`262` Records, `266` Findings)
- **Status**: `open` (`carried_from: mim-c01-s04-f006`)
- **Tracked Issue**: [https://github.com/CultureBotAI/MediaIngredientMech/issues/718](https://github.com/CultureBotAI/MediaIngredientMech/issues/718)
- **Target Scope**: `262` records (`266` active findings: `261` unmapped identity/grounding findings across `260` `UNMAPPED` records + `1` `MAPPED` record, `4` complex-parent formulation scope findings, and `1` `AMBIGUOUS` formulation scope finding on `data/ingredients/unmapped/PYGS.yaml`).
- **Native Structured Review Bundles**:
  - `reviews/structured/20261011T183500Z-mim-semantic-review-20260921-active-findings/review.yaml` (`finding_id: mim-20261011-183500-unmapped-identity-scope`)
  - `262` individual bundles in `reviews/structured/20261017T083000Z-*/review.yaml`
- **Disposition**: Requires upstream recipe verification, authoritative registry grounding, or explicit complex mixture decomposition; tracked under `#718`.

### 2.6 `mim-c01-s04-f007` — Context-Dependent Exported Synonym/CAS Token Scope & Component Source Scope (`31` Records, `31` Findings)
- **Status**: `open` (`carried_from: mim-c01-s04-f007`)
- **Tracked Issues**: [https://github.com/CultureBotAI/MediaIngredientMech/issues/718](https://github.com/CultureBotAI/MediaIngredientMech/issues/718) and [https://github.com/CultureBotAI/MediaIngredientMech/issues/861](https://github.com/CultureBotAI/MediaIngredientMech/issues/861)
- **Target Scope**: `31` records (`31` active findings: `17` context-dependent nomenclature/token scope findings on mapped records, `13` component assertion source-scope findings on stock/solution records, and `1` CAS alias verification finding on `data/ingredients/mapped/Furaltadone.yaml`).
- **Native Structured Review Bundles**:
  - `reviews/structured/20261011T183500Z-mim-semantic-review-20260921-active-findings/review.yaml` (`finding_id: mim-20261011-183500-synonym-component-scope`)
  - `31` individual bundles in `reviews/structured/20261017T083000Z-*/review.yaml`
- **Disposition**: Requires upstream CultureMech/TOGO/MediaDive recipe context verification and coordinated SSSOM/component receipt updates; tracked under `#718` and `#861`.
