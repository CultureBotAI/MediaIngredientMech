# MediaIngredientMech Stage 5 Issue Map & Finding Dispositions

- **Run ID:** `mech-goal-sequence-20261019`
- **Cycle:** `1`
- **Stage:** `5` (`resolve_review_findings`)
- **Revision:** `1`
- **Consumed Stage 4 Evidence:** `reviews/workflow/mech-goal-sequence-20261019/cycle-000001/stage-04/revision-0001/evidence.yaml` (`sha256: 4d81bb6763c9c382558ddc6a9180d127349ee8f6ab3d9459989bbe29c2d71045`)
- **Tracked Evidence Index:** `reviews/workflow/latest.yaml`

## Summary of Stage 5 Dispositions

| Workflow Finding ID | Stage 4 Status | Stage 5 Disposition | GitHub Issue(s) | Repair Owner Skill | Linked Successor Review / Blocker |
| --- | --- | --- | --- | --- | --- |
| `mim-c01-s04-f001` | `open` | `deferred` | [#921](https://github.com/CultureBotAI/MediaIngredientMech/issues/921) | `.claude/skills/curate-yaml-record/SKILL.md` | Deferred: co-located with semantic-release baseline finding `SEM:cd74f8ddafa04d7e9a9a` and byte-bound `owner_record_sha256` in `reports/sssom_completion_20260921/mapping_review/nonmapping_cohorts.json` and `reports/semantic_review_20260921/resolution/current-review.json` |
| `mim-c01-s04-f002` | `open` | `resolved` | [#922](https://github.com/CultureBotAI/MediaIngredientMech/issues/922) | `.claude/skills/curate-yaml-record/SKILL.md` | Resolved in `reports/sssom_completion_20260921/mapping_changes/review-record-issues-20261003.json` and dependent review manifests; verified by successor review `reviews/structured/20261021T120500Z-ca-no32-x-4-h2o/review.yaml` |
| `mim-c01-s04-f003` | `open` | `deferred` | [#923](https://github.com/CultureBotAI/MediaIngredientMech/issues/923) | `.claude/skills/curate-yaml-record/SKILL.md` | Deferred: 17 of 19 affected mapped records carry byte-bound `SUPPORTED` scientific approvals in `reports/sssom_completion_20260921/review.json` (including 3 in `nonmapping_cohorts.json`); YAML byte changes without a coordinated mapping-specific re-review batch revoke `SUPPORTED`/`APPROVED` dispositions |
| `mim-c01-s04-f004` | `open` | `deferred` | [#718](https://github.com/CultureBotAI/MediaIngredientMech/issues/718) | `.claude/skills/ingredient-roles/SKILL.md` | Deferred: 624 primary nutritional/cellular role assertions (`595` single-role + `29` multi-role) require organism- or recipe-backed literature citations (`doi`/`pmid`) and coordinated semantic-release role-plan re-verification |
| `mim-c01-s04-f005` | `open` | `deferred` | [#718](https://github.com/CultureBotAI/MediaIngredientMech/issues/718) | `.claude/skills/ingredient-roles/SKILL.md` | Deferred: 29 secondary physicochemical role assertions (`17` single-role + `12` multi-role) require primary formulation/literature citations and semantic-release role-plan re-verification |
| `mim-c01-s04-f006` | `open` | `deferred` | [#718](https://github.com/CultureBotAI/MediaIngredientMech/issues/718) | `.claude/skills/map-media-ingredients/SKILL.md` | Deferred: 266 findings across 262 unmapped/ambiguous records (`261` unmapped identity + `4` complex parent scope + `1` ambiguous `PYGS.yaml`) require primary recipe/formulation verification and ontology grounding |
| `mim-c01-s04-f007` | `open` | `deferred` | [#718](https://github.com/CultureBotAI/MediaIngredientMech/issues/718) | `.claude/skills/curate-yaml-record/SKILL.md` | Deferred: 31 findings (`17` exported synonym/CAS token scope + `13` component source scope + `1` `Furaltadone_Hydrochloride.yaml` CAS alias) require primary source-recipe verification and semantic-release component/token ledger adjudication |

---

## Detailed Dispositions

### 1. `mim-c01-s04-f002` — `resolved` ([#922](https://github.com/CultureBotAI/MediaIngredientMech/issues/922))
- **Predecessor Finding:** `reviews/structured/20261017T083000Z-ca-no32-x-4-h2o/review.yaml` (`rec-f-5b1b1ab939d20218`)
- **Cause & Repair Ownership:** Provenance receipt text discrepancy in `reports/sssom_completion_20260921/mapping_changes/review-record-issues-20261003.json` (`records[0].change`, line 18), which named `CHEBI:31348` instead of `CHEBI:86159` (`calcium dinitrate tetrahydrate`) for `data/ingredients/mapped/Ca_No32_X_4_H2o.yaml`.
- **Implemented Fix:**
  - Updated `records[0].change` in `reports/sssom_completion_20260921/mapping_changes/review-record-issues-20261003.json` from `CHEBI:31348` to `CHEBI:86159`.
  - Synchronized the `review-record-issues-20261003.json` input SHA-256 (`9b578f6c25c1ebabb8e58c5a59d6188b7c1f2dd3c8c70ed021b35144c6da1226`) in `reports/sssom_completion_20260921/review.json` (`sha256: 6c74c7cc3eb8075ec18e20ab594a9b5eae9910b08b98c9d0746b3374af6c7ac6`), `reports/ingredient_bundle_20260924/review.json` (`base_review_sha256`), and `reports/semantic_review_20260921/resolution/current-review.json`.
  - Saved successor structured review bundle `reviews/structured/20261021T120500Z-ca-no32-x-4-h2o/review.yaml` and `review.md` via `scripts/record_review.py save`, recording `rec-f-5b1b1ab939d20218` as `status: resolved` with `previous_occurrences` linked to `20261017T083000Z-ca-no32-x-4-h2o#rec-f-5b1b1ab939d20218` and `20261011T024629Z-mim-reconcile-all-batch-01#f-5b1b1ab939d20218`.

### 2. `mim-c01-s04-f001` — `deferred` ([#921](https://github.com/CultureBotAI/MediaIngredientMech/issues/921))
- **Predecessor Finding:** `reviews/structured/20261017T083000Z-2-d-lyxose/review.yaml` (`rec-f-444b73747dddc915`)
- **Blocker / Deferral Rationale:** `data/ingredients/mapped/(2)-D-lyxose.yaml` is bound by exact `owner_record_sha256` (`62258c9bdabaf8728fafb6923345fe4b24b9956069113896acb16e9631c1451e`) in `reports/sssom_completion_20260921/mapping_review/nonmapping_cohorts.json` (`source_position: 3`, `unresolved_nonmapping_finding_ids: ["SEM:cd74f8ddafa04d7e9a9a"]`) and `reports/semantic_review_20260921/resolution/current-review.json`. Reconciling `kgmicrobe.trait:d_lyxose` (`count: 159`) from `data/custom/microbedecoder/unmapped_labels.tsv` must be executed together with the `SEM:cd74f8ddafa04d7e9a9a` semantic-release disposition and `nonmapping_cohorts.json` token-level review.

### 3. `mim-c01-s04-f003` — `deferred` ([#923](https://github.com/CultureBotAI/MediaIngredientMech/issues/923))
- **Predecessor Findings:** 19 per-record findings across `(R)-amygdalin.yaml` through `3-trehalosamine.yaml`.
- **Blocker / Deferral Rationale:** 17 of the 19 mapped records carry byte-bound `SUPPORTED` scientific approvals in `reports/sssom_completion_20260921/review.json` (including `(R)-lactate.yaml`, `2-aminobenzoate.yaml`, and `2-deoxyadenosine.yaml` in `reports/sssom_completion_20260921/mapping_review/nonmapping_cohorts.json`). Modifying their YAML bytes without a coordinated mapping-specific re-review batch invalidates `owner_record_sha256` in `assemble_review.py` and `supported_kgx`.

### 4. `mim-c01-s04-f004`, `mim-c01-s04-f005`, `mim-c01-s04-f006`, `mim-c01-s04-f007` — `deferred` ([#718](https://github.com/CultureBotAI/MediaIngredientMech/issues/718))
- **Predecessor Findings:** 950 per-record findings across 926 records (`624` primary role evidence + `29` physicochemical role evidence + `266` unmapped/ambiguous identity & parent scope + `31` exported token & component source scope).
- **Blocker / Deferral Rationale:** Tracked under overarching curation issue [#718](https://github.com/CultureBotAI/MediaIngredientMech/issues/718) (`Curate the claims excluded from the reviewed MIM release`). These cohorts require primary literature citations (`doi`/`pmid`), upstream recipe source lookup, and coordinated semantic-release ledger updates (`reports/semantic_review_20260921/resolution/`).
