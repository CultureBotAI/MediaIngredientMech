# MediaIngredientMech Cycle 2 Stage 5 Issue Map & Finding Dispositions

- **Run ID:** `mech-goal-sequence-20261019`
- **Cycle:** `2` (`cycle-000002`)
- **Stage:** `5` (`stage-05` / `resolve_review_findings`)
- **Revision:** `1` (`revision-0001`)
- **Source Revision:** `7f56a13130d8d220efa48cef78559e80351c5a46`
- **Scope Frozen At:** `2026-10-22T08:20:00Z`
- **Consumed Stage 4 Evidence:** `reviews/workflow/mech-goal-sequence-20261019/cycle-000002/stage-04/revision-0001/evidence.yaml` (`sha256: 98456ad5e221f87e55a88f089a3ae77320d5ae1115e4e209926bff1b6c72fdcc`)
- **Tracked Evidence Index:** `reviews/workflow/latest.yaml` (updated from `verified-evidence-index.json` to include verified Cycle 2 Stage 4 closure receipt `382b5adbc2afc652384d6165cda0c40e312cf6cd22cd34e27c1ec4300a875cb1` / PR `#930`)

---

## 1. Root-Cause Grouping & Issue Deduplication Summary

All `6` open root-cause cohorts (`970` active per-record findings across `960` records) carried forward into Cycle 2 Stage 4 (`reviews/workflow/mech-goal-sequence-20261019/cycle-000002/stage-04/revision-0001/evidence.yaml`) were grouped into `3` root-cause and repair-ownership groups (`mim-c02-s05-g001` .. `mim-c02-s05-g003`) and deduplicated against live GitHub issues in `CultureBotAI/MediaIngredientMech`:

| Group ID | Workflow Finding ID(s) | Per-Record Findings | Stage 4 Status | Stage 5 Disposition | GitHub Issue(s) | Repair Owner Skill | Blocker & Carry-Forward Rationale |
| --- | --- | ---: | --- | --- | --- | --- | --- |
| `mim-c02-s05-g001` | `mim-c01-s04-f001` | 1 (`1` record) | `open` | `deferred` | [#921](https://github.com/CultureBotAI/MediaIngredientMech/issues/921) (`OPEN`) | `.claude/skills/curate-yaml-record/SKILL.md` | `data/ingredients/mapped/(2)-D-lyxose.yaml` (`CHEBI:62318`) is byte-bound (`owner_record_sha256: 62258c9bdabaf8728fafb6923345fe4b24b9956069113896acb16e9631c1451e`) in `reports/sssom_completion_20260921/mapping_review/nonmapping_cohorts.json` (`source_position: 3`) and `reports/semantic_review_20260921/resolution/current-review.json`, and co-located with open role-evidence finding `SEM:cd74f8ddafa04d7e9a9a` ([#718](https://github.com/CultureBotAI/MediaIngredientMech/issues/718)). Under the exact-byte approval policy (`src/mediaingredientmech/record_refresh.py`), any edit requires a fresh scientific review bound to the resulting bytes. |
| `mim-c02-s05-g002` | `mim-c01-s04-f003` | 19 (`19` records) | `open` | `deferred` | [#923](https://github.com/CultureBotAI/MediaIngredientMech/issues/923) (`OPEN`) | `.claude/skills/curate-yaml-record/SKILL.md` | All `19` affected mapped records (`(R)-amygdalin.yaml` through `3-trehalosamine.yaml`) are byte-bound in `reports/sssom_completion_20260921/review.json["record_inputs"]` (`17` `SUPPORTED` + `2` `WITHHOLD`) and `reports/semantic_review_20260921/resolution/current-review.json`, with `5` (`(R)-lactate.yaml`, `2-aminobenzoate.yaml`, `2-dehydro-D-gluconate.yaml`, `2-deoxyadenosine.yaml`, `2-dichloroethane.yaml`) also byte-bound in `reports/sssom_completion_20260921/mapping_review/nonmapping_cohorts.json`. Under `src/mediaingredientmech/record_refresh.py`, audit-history reordering cannot use receipt chains to preserve prior byte-bound approvals and must accompany a full mapping-review refresh batch. |
| `mim-c02-s05-g003` | `mim-c01-s04-f004`, `mim-c01-s04-f005`, `mim-c01-s04-f006`, `mim-c01-s04-f007` | 950 (`926` distinct records) | `open` | `deferred` | [#718](https://github.com/CultureBotAI/MediaIngredientMech/issues/718) (`OPEN`), [#861](https://github.com/CultureBotAI/MediaIngredientMech/issues/861) (`CLOSED` context) | `.claude/skills/ingredient-roles/SKILL.md`, `.claude/skills/map-media-ingredients/SKILL.md`, `.claude/skills/curate-yaml-record/SKILL.md` | Tracked under existing open curation backlog issue [#718](https://github.com/CultureBotAI/MediaIngredientMech/issues/718) (`Curate the claims excluded from the reviewed MIM release`): `624` primary nutritional/cellular role evidence findings (`mim-c01-s04-f004`), `29` secondary physicochemical role evidence findings (`mim-c01-s04-f005`), `266` unmapped/ambiguous chemical identity & parent-scope findings across `262` records (`mim-c01-s04-f006`), and `31` context-dependent exported synonym/CAS token scope & component source-scope findings (`mim-c01-s04-f007`). Requires primary literature citations (`doi`/`pmid`), upstream recipe source lookup, and coordinated semantic-release ledger updates. |

*(Note: `mim-c01-s04-f002` on `data/ingredients/mapped/Ca_No32_X_4_H2o.yaml` was resolved in Cycle 1 Stage 5 under [#922](https://github.com/CultureBotAI/MediaIngredientMech/issues/922) and verified in `reviews/structured/20261021T120500Z-ca-no32-x-4-h2o/review.yaml` with `0` open findings.)*

---

## 2. Detailed Group & Finding Dispositions

### Group 1: `mim-c02-s05-g001` (`mim-c01-s04-f001`) — `deferred` ([#921](https://github.com/CultureBotAI/MediaIngredientMech/issues/921))

- **Predecessor Finding:** `reviews/structured/20261017T083000Z-2-d-lyxose/review.yaml` (`rec-f-444b73747dddc915`, issue key `mim-reconciliation-source-count-5703779de3d5d6d5`)
- **Target Record:** `data/ingredients/mapped/(2)-D-lyxose.yaml` (`CHEBI:62318`)
- **Cause & Repair Ownership:** `.claude/skills/curate-yaml-record/SKILL.md` — `occurrence_statistics.total_occurrences` (`4`) and synonyms reflect MicrobeDecoder merge provenance, whereas `data/custom/microbedecoder/unmapped_labels.tsv` records `D-lyxose` (`kgmicrobe.trait:d_lyxose`, `count: 159`) without a corresponding `MicrobeDecoder` entry in `occurrence_statistics.source_occurrences`.
- **Stage 5 Disposition (`deferred`):**
  - Reused open GitHub issue [#921](https://github.com/CultureBotAI/MediaIngredientMech/issues/921) (`Reconcile missing direct MicrobeDecoder D-lyxose occurrence on (2)-D-lyxose.yaml (CHEBI:62318)`).
  - Deferred because `data/ingredients/mapped/(2)-D-lyxose.yaml` is bound by exact `owner_record_sha256` (`62258c9bdabaf8728fafb6923345fe4b24b9956069113896acb16e9631c1451e`) in `reports/sssom_completion_20260921/mapping_review/nonmapping_cohorts.json` (`source_position: 3`, `unresolved_nonmapping_finding_ids: ["SEM:cd74f8ddafa04d7e9a9a"]`), `reports/sssom_completion_20260921/review.json`, and `reports/semantic_review_20260921/resolution/current-review.json`.
  - Under `src/mediaingredientmech/record_refresh.py` (`REQUIRED_POLICY_REJECTION`), occurrence count and synonym adjustments on byte-bound records require fresh scientific approval bound to the resulting YAML bytes, which must be executed together with `SEM:cd74f8ddafa04d7e9a9a` ([#718](https://github.com/CultureBotAI/MediaIngredientMech/issues/718)) and `D-_-lyxose.yaml` (`CHEBI:47878`).

### Group 2: `mim-c02-s05-g002` (`mim-c01-s04-f003`) — `deferred` ([#923](https://github.com/CultureBotAI/MediaIngredientMech/issues/923))

- **Predecessor Findings:** `19` per-record findings across:
  1. `data/ingredients/mapped/(R)-amygdalin.yaml` (`CHEBI:17019`, `SUPPORTED`, `source_position: 4`)
  2. `data/ingredients/mapped/(R)-lactate.yaml` (`CHEBI:16004`, `SUPPORTED`, `source_position: 5`, also in `nonmapping_cohorts.json`)
  3. `data/ingredients/mapped/(R)-malic_Acid.yaml` (`CHEBI:30796`, `SUPPORTED`, `source_position: 6`)
  4. `data/ingredients/mapped/(S)-azetidine-2-carboxylic_Acid.yaml` (`CHEBI:6198`, `SUPPORTED`, `source_position: 7`)
  5. `data/ingredients/mapped/(S)-mandelic_Acid.yaml` (`CHEBI:32800`, `SUPPORTED`, `source_position: 8`)
  6. `data/ingredients/mapped/1-methylphenanthrene.yaml` (`CHEBI:35860`, `SUPPORTED`, `source_position: 23`)
  7. `data/ingredients/mapped/2-aminobenzoate.yaml` (`CHEBI:16567`, `SUPPORTED`, `source_position: 74`, also in `nonmapping_cohorts.json`)
  8. `data/ingredients/mapped/2-aminopentanoic_Acid.yaml` (`CHEBI:19475`, `SUPPORTED`, `source_position: 75`)
  9. `data/ingredients/mapped/2-dehydro-D-gluconate.yaml` (`CHEBI:16808`, `WITHHOLD`, `source_position: 79`, also in `nonmapping_cohorts.json`)
  10. `data/ingredients/mapped/2-deoxyadenosine.yaml` (`CHEBI:17256`, `SUPPORTED`, `source_position: 80`, also in `nonmapping_cohorts.json`)
  11. `data/ingredients/mapped/2-dichloroethane.yaml` (`CHEBI:27789`, `WITHHOLD`, `source_position: 84`, also in `nonmapping_cohorts.json`)
  12. `data/ingredients/mapped/2-naphthyl_Dihydrogen_Phosphate.yaml` (`CHEBI:91043`, `SUPPORTED`, `source_position: 93`)
  13. `data/ingredients/mapped/2-naphthyl_Tetradecanoate.yaml` (`CHEBI:90249`, `SUPPORTED`, `source_position: 94`)
  14. `data/ingredients/mapped/2-oxobutanoate.yaml` (`CHEBI:16763`, `SUPPORTED`, `source_position: 95`)
  15. `data/ingredients/mapped/2-oxopentanoate.yaml` (`CHEBI:28644`, `SUPPORTED`, `source_position: 99`)
  16. `data/ingredients/mapped/3-aminobutyrate.yaml` (`CHEBI:87997`, `SUPPORTED`, `source_position: 137`)
  17. `data/ingredients/mapped/3-dehydro-D-gluconate.yaml` (`CHEBI:85256`, `SUPPORTED`, `source_position: 140`)
  18. `data/ingredients/mapped/3-hydroxybenzoate.yaml` (`CHEBI:16193`, `SUPPORTED`, `source_position: 143`)
  19. `data/ingredients/mapped/3-trehalosamine.yaml` (`CHEBI:223561`, `SUPPORTED`, `source_position: 158`)
- **Stage 5 Disposition (`deferred`):**
  - Reused open GitHub issue [#923](https://github.com/CultureBotAI/MediaIngredientMech/issues/923) (`Normalize non-monotonic curation_history timestamp order across 19 mapped ingredient records`).
  - Deferred because all `19/19` records are byte-bound in `reports/sssom_completion_20260921/review.json["record_inputs"]` and `reports/semantic_review_20260921/resolution/current-review.json["record_inputs"]` (`17` `SUPPORTED` + `2` `WITHHOLD`, with `5` also byte-bound in `reports/sssom_completion_20260921/mapping_review/nonmapping_cohorts.json`). Under `src/mediaingredientmech/record_refresh.py`, reordering `curation_history` changes the file SHA-256 and cannot be carried across byte-bound approvals via receipt chains without a fresh mapping-review batch.

### Group 3: `mim-c02-s05-g003` (`mim-c01-s04-f004`, `mim-c01-s04-f005`, `mim-c01-s04-f006`, `mim-c01-s04-f007`) — `deferred` ([#718](https://github.com/CultureBotAI/MediaIngredientMech/issues/718))

- **Predecessor Findings (`950` findings across `926` distinct records):**
  - `mim-c01-s04-f004` (`624` findings across `624` mapped records; `.claude/skills/ingredient-roles/SKILL.md`): Prediction-only or empty primary nutritional/cellular role assertions (`595` single-role + `29` multi-role) lacking `Citation` (`doi`/`pmid`) evidence.
  - `mim-c01-s04-f005` (`29` findings across `29` mapped records; `.claude/skills/ingredient-roles/SKILL.md`): Prediction-only or empty secondary physicochemical role assertions (`17` single-role + `12` multi-role) lacking literature/formulation citations.
  - `mim-c01-s04-f006` (`266` findings across `262` records; `.claude/skills/map-media-ingredients/SKILL.md`): Unresolved exact chemical identity, preparation form, or complex parent scope (`261` unmapped identity + `4` unmapped complex parent scope + `1` ambiguous `PYGS.yaml`).
  - `mim-c01-s04-f007` (`31` findings across `31` mapped records; `.claude/skills/curate-yaml-record/SKILL.md`): Context-dependent exported synonym/CAS token scope (`17` nomenclature findings), complex component source scope (`13` representation findings), and `1` retained Furaltadone free-base CAS alias finding on `Furaltadone_Hydrochloride.yaml`.
- **Stage 5 Disposition (`deferred`):**
  - Reused existing open GitHub tracker [#718](https://github.com/CultureBotAI/MediaIngredientMech/issues/718) (`Curate the claims excluded from the reviewed MIM release`, with historical context in closed issue [#861](https://github.com/CultureBotAI/MediaIngredientMech/issues/861)).
  - Carried forward in `carry_forward_ids` with immutable original review reports preserved under `reviews/structured/20261017T083000Z-*/review.yaml`, `reviews/reconciliation/20261011T023739Z-all-mim/`, and `reviews/workflow/mech-goal-sequence-20261019/cycle-000002/stage-04/revision-0001/`.
