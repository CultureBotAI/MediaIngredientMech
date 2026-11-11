# Cycle 19 Stage 4 Record and Cohort Review Report (`record_review`)

- **Run ID**: `mech-goal-sequence-20261019`
- **Cycle**: `19` (`cycle-000019`)
- **Stage**: `4` (`stage-04` / `record_review`)
- **Revision**: `revision-0001`
- **Repository**: `CultureBotAI/MediaIngredientMech` (`mediaingredientmech`)
- **Base Commit (`main`)**: `c8f1be257770608369be85769f5e572662a7ef1e`
- **Workflow Profile SHA-256**: `45d7c23d67f490cea6b31e336e5d2ac98b7ce8fa4e791bd9d3be092cfdb5a10d`
- **Prior Stage 5 Evidence Manifest**: `reviews/workflow/mech-goal-sequence-20261019/cycle-000018/stage-05/revision-0001/evidence.yaml` (`e4cdb2c50d176c6971119f302438940803f08f7c8acaad20b8269033e003a7d8`)
- **Tracked Verified Closure Index**: `reviews/workflow/latest.yaml` (`7b837a3c7b6b3ae5e2fc5aef1e9e09b9501fa41f191402b112cbc0db1ce18a29`, synchronized with `verified-evidence-index.json` across `54` verified closure entries through Cycle 18 Stage 6 / PR `#1351`)
- **Authoritative Skills & Contracts**:
  - `.claude/skills/review-yaml-record/SKILL.md`
  - `.claude/skills/review-yaml-category/SKILL.md`
  - `.claude/skills/reconcile-review-records/SKILL.md`
  - `.claude/skills/mediaingredientmech-evolve-workflow/SKILL.md`
  - `docs/record-reviews.md`
  - `docs/record-review-profile.md`
  - `schema/record_review.yaml` (`229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb`)

---

## 1. Frozen Corpus Inventory and Input Provenance

At base commit `c8f1be257770608369be85769f5e572662a7ef1e` (incorporating Cycle 19 Stage 1 add/discovery review in PR `#1353`, Cycle 19 Stage 2 mechanism review in PR `#1355`, and Cycle 19 Stage 3 UniProt protein reference review in PR `#1356`), the frozen MediaIngredientMech YAML corpus and native structured review inventory consist of:

| Surface | Path / Glob | Count | SHA-256 Digest |
| --- | --- | ---: | --- |
| Individual ingredient records (all) | `data/ingredients/**/*.yaml` | `2,956` | `1e978e977f3ce6e522117a4e7e06d25b4fb9d2eeda34a05ede17ad0b250d322d` (`sha256sum` manifest) / `8e2972ec31744c09572ac2f513da673b17467a9d11974cfab88c68cc96c44f76` (`path:hash` manifest) |
| Mapped directory records | `data/ingredients/mapped/*.yaml` | `2,681` (`2,611` `MAPPED`, `70` `REJECTED`) | `b85e481acd795100b2c5aa4e3f690e67e9845fb8c0c41b32f49dedf30771804a` (`sha256sum` manifest) |
| Unmapped directory records | `data/ingredients/unmapped/*.yaml` | `275` (`262` `UNMAPPED`, `1` `AMBIGUOUS`, `12` `REJECTED`) | `564f397b0c83d3147996ed648c465880a0c86869ec5c8a5170a55bc4ad787f3f` (`sha256sum` manifest) |
| Aggregate mapped collection | `data/curated/mapped_ingredients.yaml` | `1` (`2,681` records) | `774718362b921a560f8474a5d77874f2779e44ac5a6afc992040084a701ea628` |
| Aggregate unmapped collection | `data/curated/unmapped_ingredients.yaml` | `1` (`275` records) | `284adda3e7ac0940308770552afa0419aa4f30372ddb2074b39b6da630478fb1` |
| Other `data/curated/*.yaml` collections | `data/curated/{unmapped_already_mapped,unmapped_complex_media,unmapped_incomplete_formula,unmapped_other,unmapped_placeholder}.yaml` | `5` | Validated by `scripts/record_review.py --repo-root . check` |
| Total validated YAML documents | `data/ingredients/*/*.yaml` + `data/curated/*.yaml` | `2,963` | `100%` schema-clean (`0` LinkML strict validation errors) |
| Native structured review bundles | `reviews/structured/*/review.{yaml,md}` | `1,015` bundles (`2,030` files) | `a5b269efd2ad258d74ab97cd780377fb9c8072112d2ee0547a0dcd4804a8e269` (sorted Python `sha256` manifest) / `2f938a82389d25375ea6e6eb23cabea2dee95a50169b9f4bf6a4531a1b3c027e` (`LC_ALL=C sort` `sha256sum` manifest) |
| LinkML ingredient schema | `src/mediaingredientmech/schema/mediaingredientmech.yaml` | `1` | `bb43dee29b21fdee72a48022456e733e49e95824c4c09674f9b3165c290fe012` |
| LinkML record-review schema | `schema/record_review.yaml` | `1` | `229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb` |
| Infrastructure task ledger | `INFRA_TASKS.md` | `1` | `dda5707f52661e91f46d96fcbabfc256ac39d4cc865a28a3e5ab6f0536958a5e` |
| Tracked verified closure index | `reviews/workflow/latest.yaml` | `1` (`54` entries) | `7b837a3c7b6b3ae5e2fc5aef1e9e09b9501fa41f191402b112cbc0db1ce18a29` |
| SSSOM mapping artifact | `mappings/ingredient_mappings.sssom.tsv` | `1` | `d5f76fc404967477903fafc79eaba86ecfef9e2c391926ec08c3c1af4a5220b6` |
| Unified mapping artifact | `UNIFIED_INGREDIENT_MAPPING.tsv` | `1` | `f6a8eb844e578d79da9538abf99c244fc25b2c928c50c64c0477b1218092a0f1` |

---

## 2. Native Structured Review Verification (`scripts/record_review.py --repo-root . check`)

Running `.venv/bin/python scripts/record_review.py --repo-root . check` across the repository verifies all **`1,015`** native structured review bundles (`2,030` paired `review.yaml` + `review.md` files under `reviews/structured/`) with exit code `0` (`valid_reviews: 1015`, `coverage: "declared_scopes_only"`, `0` stale `source_sha256` target hashes, `0` schema or profile violations):

1. **Per-Record Bundles (`kind: record`, `965` bundles covering `962` distinct records)**:
   - **`961` initial per-record bundles** (`reviews/structured/20261017T083000Z-*/review.{yaml,md}`, `verdict: needs_curation`) covering `961` ingredient records with `971` initial per-record findings (`645` `open` + `326` `deferred`).
   - **`1` successor per-record bundle** (`reviews/structured/20261021T120500Z-ca-no32-x-4-h2o/review.{yaml,md}`, `verdict: pass_with_limitations`, `0` open findings) recording the Cycle 1 Stage 5 remediation of `data/ingredients/mapped/Ca_No32_X_4_H2o.yaml` (`rec-f-5b1b1ab939d20218` / `mim-c01-s04-f002`), leaving **`960` records** with **`970` active per-record findings** (`644` `open` + `326` `deferred`) in the initial per-record series.
   - **`3` `20261101T*` per-record bundles** added in PRs `#1007`, `#1026`, `#1030`:
     - `reviews/structured/20261101T004549Z-na2hpo4-heptahydrate-exact-identity/review.{yaml,md}` (`kind: record`, target `data/ingredients/mapped/Na2hpo4_X_7_H2o.yaml`, `verdict: needs_curation`, `2` findings; exact heptahydrate identity promoted to `NCIT:C61946` in PR `#1030` and recorded in `20261101T054115Z-approved-step2-ncit-heptahydrate-review`, while retaining open `BUFFER` role citation and anhydrous chemistry holds).
     - `reviews/structured/20261101T005659Z-melezitose-formof-blocked-review/review.{yaml,md}` (`kind: record`, target `data/ingredients/mapped/D-_-melezitose_Monohydrate.yaml`, `verdict: blocked`, `2` findings documenting `biolink:form_of` SSSOM emission hold and `CARBOHYDRATE_SOURCE` role citation hold; `biolink:form_of` form mapping subsequently landed in PR `#1083` and was verified in `20261101T212612Z-melezitose901-final-independent-diagnostics`, while the role citation hold remains active under `mim-c01-s04-f004`).
     - `reviews/structured/20261101T005710Z-carnitine-amide-alias-scientific/review.{yaml,md}` (`kind: record`, target `data/ingredients/mapped/Carnitine_Hydrochloride.yaml`, `verdict: pass_with_limitations`, `0` open findings; documents rejection of distinct chemical `carnitinamide` [`CHEBI:65018`] alias on `Carnitine_Hydrochloride.yaml` [`CHEBI:35280`] in PR `#1007`).
2. **Category Bundle (`kind: category`, `1` bundle covering `3` ingredient records)**:
   - `reviews/structured/20261101T094737Z-approved-step3-carnitine-hydrochloride-review/review.{yaml,md}` (`kind: category`, `12` `targets:` entries including the `3` ingredient records `data/ingredients/mapped/Carnitine_Dl_Hydrochloride.yaml` [`NCIT:C216679`, `REJECTED`], `data/ingredients/mapped/Carnitine_Hydrochloride.yaml` [`NCIT:C216679`], and `data/ingredients/mapped/NLDM_metabolites.yaml` [`kgmicrobe.ingredient:nldm_metabolites`], plus `data/ingredients/mapped/L-Carnitine_Hydrochloride.yaml` [`CHEBI:233463`] in `source.inputs` as `role: context`, `verdict: pass_with_limitations`, `0` open findings) added in PR `#1042`.
3. **Cohort / Batch Bundles (`kind: batch`, `32` bundles covering `2,954` distinct ingredient records)**:
   - **`14` corpus-wide reconciliation batch bundles** (`reviews/structured/20261011T080001Z-mim-*` through `20261011T080014Z-mim-*`, `13` `verdict: needs_curation` + `1` `verdict: not_assessed`) covering all `2,953` pre-PR-#1026 individual records (`2,680` mapped + `273` unmapped).
   - **`18` focused curation and reconciliation batch bundles** (`20261101T005710Z-seven-generated-alias-rulings` through `20261104T055649Z-deferred23-independent-final-export-policy-review`: `8` `verdict: pass_with_limitations`, `8` `verdict: needs_curation`, `2` `verdict: blocked`), including:
     - `20261102T224104Z-step7c-final-source-and-sssom-review` (`verdict: pass_with_limitations`, `11` targets including newly added mapped record `data/ingredients/mapped/25-didehydro-D-gluconate.yaml` [`CHEBI:11449`], `2` resolved findings reconciling `20261102T211849Z-step7c-source-prereview` and `20261102T212904Z-step7c-current-reason-prerepair` in PR `#1115`).
     - `20261104T023946Z-step7d-independent-final-science-and-snapshot` (`verdict: pass_with_limitations`, `203` targets across `67` owner records, `44` resolved findings reconciling `20261103T060904Z-step7d-67-owner-scientific-author-review`, `20261103T064120Z-step7d-independent-stale-parent-comments`, `20261103T065928Z-step7d-independent-test-coordinate-blocker`, `20261103T070134Z-step7d-independent-full-suite-blockers`, and `20261103T072631Z-step7d-independent-quoted-inventory-finding` for `38` applied owner corrections in PR `#1128`, while preserving scientific holds on the `29` excluded owners).
     - `20261104T055649Z-deferred23-independent-final-export-policy-review` (`verdict: pass_with_limitations`, `130` targets across `22` owner records, `4` resolved findings reconciling `20261104T045618Z-deferred23-independent-publication-proof-findings`, `20261104T051118Z-deferred23-independent-native-continuation-finding`, and `20261104T052359Z-deferred23-independent-fixture-prefix-finding` in PR `#1136`).
4. **Repository Scope Bundles (`kind: repository`, `17` bundles covering `38` distinct ingredient records)**:
   - **`16` `pass_with_limitations` repository bundles** (`0` open findings) covering PRs `#1007`, `#1026`, `#1030`, `#1048`, `#1062`, `#1076`, `#1083`, `#1094`, `#1106` (including `20261101T035857Z-approved-plan-step1-unified-review` covering `data/ingredients/unmapped/Na2moo4_X_H2o.yaml` [`UNMAPPED_0851`] and `data/ingredients/unmapped/Trisodium_Citrate_X_3_H2o.yaml` [`UNMAPPED_0852`]).
   - **`1` `needs_curation` repository bundle** (`reviews/structured/20261102T061829Z-step7b-hydrate-stock-reconciliation/review.{yaml,md}`, `43` targets, `10` findings: `2` `resolved` + `8` `open` holding remaining hydrate/stock items from PR `#1106`).

Across all `1,015` structured review bundles, **`2,956 / 2,956` (`100.00%`)** of individual ingredient YAML records (`2,681` mapped + `275` unmapped) are explicitly declared in `targets:` with current `source_sha256` digests verified by `scripts/record_review.py --repo-root . check`. Zero ingredient records or structured review bundles changed between Cycle 18 Stage 4 (`54cff4e96e4b5ca5a4ad70db8aeade908281193a`) and Cycle 19 Stage 4 (`c8f1be257770608369be85769f5e572662a7ef1e`), leaving all `6` carried-forward cohorts unchanged in active count.

---

## 3. Summary of Open Findings Preserved for Cycle 19 Stage 5 (`resolve_review_findings`)

All **`6`** open root-cause finding cohorts carried forward from Cycle 18 Stage 5 (`reviews/workflow/mech-goal-sequence-20261019/cycle-000018/stage-05/revision-0001/evidence.yaml`, `sha256: e4cdb2c50d176c6971119f302438940803f08f7c8acaad20b8269033e003a7d8`) remain active (`970` active per-record findings across `960` records in `20261017T083000Z-*`, plus `2` split unmapped hydrate records `Na2moo4_X_H2o.yaml` [`UNMAPPED_0851`] and `Trisodium_Citrate_X_3_H2o.yaml` [`UNMAPPED_0852`] tracked in `20261101T035857Z-approved-plan-step1-unified-review`, `8` open hydrate/stock reconciliation holds in `20261102T061829Z-step7b-hydrate-stock-reconciliation`, and `29` excluded owner scientific holds in `20261103T060904Z-step7d-67-owner-scientific-author-review`) and are preserved with stable IDs for Cycle 19 Stage 5 (`resolve_review_findings`):

| Finding ID | Carried From | Category / Severity | Per-Record Count | Tracked Issue(s) | Summary |
| --- | --- | --- | ---: | --- | --- |
| `mim-c01-s04-f001` | `mim-c01-s04-f001` | `quantity` / `major` | `1` (`1` record) | [#921](https://github.com/CultureBotAI/MediaIngredientMech/issues/921) | Reconcile missing direct MicrobeDecoder occurrence on `data/ingredients/mapped/(2)-D-lyxose.yaml` (`CHEBI:62318`; native finding `rec-f-444b73747dddc915`) |
| `mim-c01-s04-f002` | `mim-c01-s04-f002` | `provenance` / `minor` | `0` active (`1` resolved in Cycle 1 Stage 5) | [#922](https://github.com/CultureBotAI/MediaIngredientMech/issues/922) | Resolved in Cycle 1 Stage 5 (`data/ingredients/mapped/Ca_No32_X_4_H2o.yaml`, verified in `reviews/structured/20261021T120500Z-ca-no32-x-4-h2o/review.yaml`) |
| `mim-c01-s04-f003` | `mim-c01-s04-f003` | `provenance` / `minor` | `19` (`19` records) | [#923](https://github.com/CultureBotAI/MediaIngredientMech/issues/923) | Normalize non-monotonic `curation_history` timestamp order across 19 mapped ingredient records |
| `mim-c01-s04-f004` | `mim-c01-s04-f004` | `evidence` / `major` | `624` (`624` records) | [#718](https://github.com/CultureBotAI/MediaIngredientMech/issues/718) | Adjudicate prediction-only or empty primary nutritional/cellular role assertions lacking literature citations across 624 mapped records (`595` single-role + `29` multi-role) |
| `mim-c01-s04-f005` | `mim-c01-s04-f005` | `evidence` / `minor` | `29` (`29` records) | [#718](https://github.com/CultureBotAI/MediaIngredientMech/issues/718) | Adjudicate prediction-only or empty secondary physicochemical role assertions lacking literature citations across 29 mapped records (`17` single-role + `12` multi-role) |
| `mim-c01-s04-f006` | `mim-c01-s04-f006` | `identity` & `grounding` / `major` | `266` (`262` initial records + `2` split hydrate records `UNMAPPED_0851`/`UNMAPPED_0852`) | [#718](https://github.com/CultureBotAI/MediaIngredientMech/issues/718) | Resolve exact chemical identity, preparation form, or complex parent scope across 262 unmapped/ambiguous records (`266` findings across `261` unmapped identity + `4` complex parent scope + `1` ambiguous `PYGS`, plus `2` split unmapped hydrate records `Na2moo4_X_H2o.yaml` and `Trisodium_Citrate_X_3_H2o.yaml` from PR `#1026`) |
| `mim-c01-s04-f007` | `mim-c01-s04-f007` | `nomenclature` / `representation` / `identity` (`major` / `minor`) | `31` (`31` records) | [#718](https://github.com/CultureBotAI/MediaIngredientMech/issues/718), [#861](https://github.com/CultureBotAI/MediaIngredientMech/issues/861) | Adjudicate context-dependent exported synonym/CAS token scope and component source scope across 31 records (`17` nomenclature token scope + `13` component source scope + `1` Furaltadone CAS alias) |
