# Cycle 13 Stage 4 Record and Cohort Review Report (`record_review`)

- **Run ID**: `mech-goal-sequence-20261019`
- **Cycle**: `13` (`cycle-000013`)
- **Stage**: `4` (`stage-04` / `record_review`)
- **Revision**: `revision-0001`
- **Repository**: `CultureBotAI/MediaIngredientMech` (`mediaingredientmech`)
- **Base Commit (`main`)**: `99fe4b44d78126d78041a69eeb366c52bedf0caa`
- **Workflow Profile SHA-256**: `059b5b9401ffeb04483cf7a46570f7f2f3c8c7fe6e574d80954bf71233cc609a`
- **Prior Stage 5 Evidence Manifest**: `reviews/workflow/mech-goal-sequence-20261019/cycle-000012/stage-05/revision-0001/evidence.yaml` (`4d57ba1b28f9628b2037d98fea9a10e9c55413243c8bc15141c4b09b2b2fe05e`)
- **Tracked Verified Closure Index**: `reviews/workflow/latest.yaml` (`1c7c8912902d4ca266300691825ea83edd302284627d756c1d65c519318d2246`, synchronized with `verified-evidence-index.json` across `36` verified closure entries through Cycle 12 Stage 6 / PR `#1024`)
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

At base commit `99fe4b44d78126d78041a69eeb366c52bedf0caa` (incorporating Cycle 13 Stage 2 mechanism review in PR `#1032`, Cycle 13 Stage 3 UniProt protein reference review in PR `#1034`, and curation/SSSOM updates in PRs `#1007`, `#1026`, `#1030`), the frozen MediaIngredientMech YAML corpus and native structured review inventory consist of:

| Surface | Path / Glob | Count | SHA-256 Digest |
| --- | --- | ---: | --- |
| Individual ingredient records (all) | `data/ingredients/**/*.yaml` | `2,955` | `7e734ef21db8f041cfd6ab9bbbd939558db7422b85609b38547a04a9375f89be` (`sha256sum` manifest) / `150a23387c6906506617e054e91d46a266273d685f6ce55b3ce02d34e6efcc1a` (`path:hash` manifest) |
| Mapped directory records | `data/ingredients/mapped/*.yaml` | `2,680` (`2,611` `MAPPED`, `69` `REJECTED`) | `fe35b92f81cc507d1112cea6db7d080679145ea0914eb6fa340491a705663fc5` (`sha256sum` manifest) |
| Unmapped directory records | `data/ingredients/unmapped/*.yaml` | `275` (`262` `UNMAPPED`, `1` `AMBIGUOUS`, `12` `REJECTED`) | `564f397b0c83d3147996ed648c465880a0c86869ec5c8a5170a55bc4ad787f3f` (`sha256sum` manifest) |
| Aggregate mapped collection | `data/curated/mapped_ingredients.yaml` | `1` (`2,680` records) | `2bc4b3663ea6beae04693bd517e2901ce69cf912d828599a0b1f7c19d2f8ba77` |
| Aggregate unmapped collection | `data/curated/unmapped_ingredients.yaml` | `1` (`275` records) | `22ececf4e0e7a37ca0636d4635ed5408a6517ba7ef6e7a1daf713f09a7802cd8` |
| Other `data/curated/*.yaml` collections | `data/curated/{complex_ingredients,media_ingredients,unmapped_Bottle_ingredients,unmapped_bottle_plates_ingredients,unmapped_media_ingredients}.yaml` | `5` | Validated by `scripts/record_review.py check` |
| Total validated YAML documents | `data/ingredients/*/*.yaml` + `data/curated/*.yaml` | `2,962` | `100%` schema-clean (`0` LinkML strict validation errors) |
| Native structured review bundles | `reviews/structured/*/review.{yaml,md}` | `986` bundles (`1,972` files) | `628a4a27e050aa06addc65d75b9af0a1669b6d800632db0aaae042f4ad5a801a` (`LC_ALL=C sort` `sha256sum` manifest) |
| LinkML ingredient schema | `src/mediaingredientmech/schema/mediaingredientmech.yaml` | `1` | `bb43dee29b21fdee72a48022456e733e49e95824c4c09674f9b3165c290fe012` |
| LinkML record-review schema | `schema/record_review.yaml` | `1` | `229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb` |
| Infrastructure task ledger | `INFRA_TASKS.md` | `1` | `dda5707f52661e91f46d96fcbabfc256ac39d4cc865a28a3e5ab6f0536958a5e` |
| Tracked verified closure index | `reviews/workflow/latest.yaml` | `1` (`36` entries) | `1c7c8912902d4ca266300691825ea83edd302284627d756c1d65c519318d2246` |
| SSSOM mapping artifact | `mappings/ingredient_mappings.sssom.tsv` | `1` | `68552edd452d5dccf1262b5d03190a6b668341952a554f349149f269403cca67` |
| Unified mapping artifact | `UNIFIED_INGREDIENT_MAPPING.tsv` | `1` | `6126d33febe2a577ff60295a36d6e5dd649a39e73c218f4d18468f3813adbce9` |

---

## 2. Native Structured Review Verification (`scripts/record_review.py check`)

Running `.venv/bin/python scripts/record_review.py check` across the repository verifies all **`986`** native structured review bundles (`1,972` paired `review.yaml` + `review.md` files under `reviews/structured/`) with exit code `0` (`valid_reviews: 986`, `coverage: "declared_scopes_only"`, `0` stale `source_sha256` target hashes, `0` schema or profile violations):

1. **Per-Record Bundles (`kind: record`, `965` bundles covering `962` distinct records)**:
   - **`961` initial per-record bundles** (`reviews/structured/20261017T083000Z-*/review.{yaml,md}`, `verdict: needs_curation`) covering `961` ingredient records with `971` initial per-record findings (`645` `open` + `326` `deferred`).
   - **`1` successor per-record bundle** (`reviews/structured/20261021T120500Z-ca-no32-x-4-h2o/review.{yaml,md}`, `verdict: pass_with_limitations`, `0` open findings) recording the Cycle 1 Stage 5 remediation of `data/ingredients/mapped/Ca_No32_X_4_H2o.yaml` (`rec-f-5b1b1ab939d20218` / `mim-c01-s04-f002`), leaving **`960` records** with **`970` active per-record findings** (`644` `open` + `326` `deferred`) in the initial per-record series.
   - **`3` new `20261101T*` per-record bundles** added in PRs `#1007`, `#1026`, `#1030`:
     - `reviews/structured/20261101T004549Z-na2hpo4-heptahydrate-exact-identity/review.{yaml,md}` (`kind: record`, target `data/ingredients/mapped/Na2hpo4_X_7_H2o.yaml`, `verdict: needs_curation`, `2` findings; exact heptahydrate identity subsequently promoted to `NCIT:C61946` in PR `#1030` and recorded in `20261101T054115Z-approved-step2-ncit-heptahydrate-review`, while retaining open `BUFFER` role citation and anhydrous chemistry holds).
     - `reviews/structured/20261101T005659Z-melezitose-formof-blocked-review/review.{yaml,md}` (`kind: record`, target `data/ingredients/mapped/D-_-melezitose_Monohydrate.yaml`, `verdict: blocked`, `2` findings documenting `biolink:form_of` SSSOM emission hold under Rule K and `CARBOHYDRATE_SOURCE` role citation hold).
     - `reviews/structured/20261101T005710Z-carnitine-amide-alias-scientific/review.{yaml,md}` (`kind: record`, target `data/ingredients/mapped/Carnitine_Hydrochloride.yaml`, `verdict: pass_with_limitations`, `0` open findings; documents rejection of distinct chemical `carnitinamide` (`CHEBI:65018`) alias on `Carnitine_Hydrochloride.yaml` (`CHEBI:35280`) in PR `#1007`; adds `Carnitine_Hydrochloride.yaml` as the `962`nd distinct record with a `kind: record` bundle).
2. **Cohort / Batch Bundles (`kind: batch`, `15` bundles)**:
   - **`14` corpus-wide reconciliation batch bundles** (`reviews/structured/20261011T080001Z-mim-*` through `20261011T080014Z-mim-*`, `13` `verdict: needs_curation` + `1` `verdict: not_assessed`) covering all `2,953` pre-PR-#1026 individual records (`2,680` mapped + `273` unmapped).
   - **`1` generated-alias ruling batch bundle** (`reviews/structured/20261101T005710Z-seven-generated-alias-rulings/review.{yaml,md}`, `kind: batch`, `7` targets, `verdict: pass_with_limitations`, `0` open findings) added in PR `#1007`.
3. **Repository Scope Bundles (`kind: repository`, `6` bundles, all `verdict: pass_with_limitations`, `0` open findings)**:
   - `reviews/structured/20261101T005659Z-scoped-sssom-promotion-check/review.{yaml,md}` (`2` targets)
   - `reviews/structured/20261101T020938Z-sssom-followup-mechanical/review.{yaml,md}` (`2` targets)
   - `reviews/structured/20261101T035857Z-approved-plan-step1-unified-review/review.{yaml,md}` (`66` targets, including all `9` mapped hydrate/salt records re-grounded in PR `#1026` plus the `2` newly split unmapped hydrate records `data/ingredients/unmapped/Na2moo4_X_H2o.yaml` [`UNMAPPED_0851`] and `data/ingredients/unmapped/Trisodium_Citrate_X_3_H2o.yaml` [`UNMAPPED_0852`])
   - `reviews/structured/20261101T054115Z-approved-step2-ncit-heptahydrate-review/review.{yaml,md}` (`40` targets, including `data/ingredients/mapped/Na2hpo4_X_7_H2o.yaml` promoted to `NCIT:C61946` in PR `#1030`)
   - `reviews/structured/20261101T062014Z-approved-step2-membership-followup/review.{yaml,md}` (`36` targets)
   - `reviews/structured/20261101T071748Z-approved-step2-cohort-test-followup/review.{yaml,md}` (`22` targets)

Across all `986` structured review bundles, **`2,955 / 2,955` (`100.00%`)** of individual ingredient YAML records (`2,680` mapped + `275` unmapped) are explicitly declared in `targets:` with current `source_sha256` digests verified by `scripts/record_review.py check`.

---

## 3. Summary of Open Findings Preserved for Cycle 13 Stage 5 (`grouped_remediation`)

All **`6`** open root-cause finding cohorts carried forward from Cycle 12 Stage 5 (`reviews/workflow/mech-goal-sequence-20261019/cycle-000012/stage-05/revision-0001/evidence.yaml`, `sha256: 4d57ba1b28f9628b2037d98fea9a10e9c55413243c8bc15141c4b09b2b2fe05e`) remain active (`970` active per-record findings across `960` records in `20261017T083000Z-*`, plus `2` newly split unmapped hydrate records `Na2moo4_X_H2o.yaml` [`UNMAPPED_0851`] and `Trisodium_Citrate_X_3_H2o.yaml` [`UNMAPPED_0852`] tracked in `20261101T035857Z-approved-plan-step1-unified-review`) and are preserved with stable IDs for Cycle 13 Stage 5 (`grouped_remediation`):

| Finding ID | Carried From | Category / Severity | Per-Record Count | Tracked Issue(s) | Summary |
| --- | --- | --- | ---: | --- | --- |
| `mim-c01-s04-f001` | `mim-c01-s04-f001` | `quantity` / `major` | `1` (`1` record) | [#921](https://github.com/CultureBotAI/MediaIngredientMech/issues/921) | Reconcile missing direct MicrobeDecoder occurrence on `data/ingredients/mapped/(2)-D-lyxose.yaml` (`CHEBI:62318`; native finding `rec-f-444b73747dddc915`) |
| `mim-c01-s04-f002` | `mim-c01-s04-f002` | `provenance` / `minor` | `0` active (`1` resolved in Cycle 1 Stage 5) | [#922](https://github.com/CultureBotAI/MediaIngredientMech/issues/922) | Resolved in Cycle 1 Stage 5 (`data/ingredients/mapped/Ca_No32_X_4_H2o.yaml`, verified in `reviews/structured/20261021T120500Z-ca-no32-x-4-h2o/review.yaml`) |
| `mim-c01-s04-f003` | `mim-c01-s04-f003` | `provenance` / `minor` | `19` (`19` records) | [#923](https://github.com/CultureBotAI/MediaIngredientMech/issues/923) | Normalize non-monotonic `curation_history` timestamp order across 19 mapped ingredient records |
| `mim-c01-s04-f004` | `mim-c01-s04-f004` | `evidence` / `major` | `624` (`624` records) | [#718](https://github.com/CultureBotAI/MediaIngredientMech/issues/718) | Adjudicate prediction-only or empty primary nutritional/cellular role assertions lacking literature citations across 624 mapped records (`595` single-role + `29` multi-role) |
| `mim-c01-s04-f005` | `mim-c01-s04-f005` | `evidence` / `minor` | `29` (`29` records) | [#718](https://github.com/CultureBotAI/MediaIngredientMech/issues/718) | Adjudicate prediction-only or empty secondary physicochemical role assertions lacking literature citations across 29 mapped records (`17` single-role + `12` multi-role) |
| `mim-c01-s04-f006` | `mim-c01-s04-f006` | `identity` & `grounding` / `major` | `266` (`262` initial records + `2` newly split unmapped hydrate records `UNMAPPED_0851`/`UNMAPPED_0852`) | [#718](https://github.com/CultureBotAI/MediaIngredientMech/issues/718) | Resolve exact chemical identity, preparation form, or complex parent scope across 262 unmapped/ambiguous records (`266` findings across `261` unmapped identity + `4` complex parent scope + `1` ambiguous `PYGS`, plus `2` newly split unmapped hydrate records `Na2moo4_X_H2o.yaml` and `Trisodium_Citrate_X_3_H2o.yaml` from PR `#1026`) |
| `mim-c01-s04-f007` | `mim-c01-s04-f007` | `nomenclature` / `representation` / `identity` (`major` / `minor`) | `31` (`31` records) | [#718](https://github.com/CultureBotAI/MediaIngredientMech/issues/718), [#861](https://github.com/CultureBotAI/MediaIngredientMech/issues/861) | Adjudicate context-dependent exported synonym/CAS token scope and component source scope across 31 records (`17` nomenclature token scope + `13` component source scope + `1` Furaltadone CAS alias) |
