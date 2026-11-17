# Cycle 20 Stage 4 Record and Cohort Review Report (`record_review`)

- **Run ID:** `mech-goal-sequence-20261019`
- **Cycle:** `20` (`cycle-000020`)
- **Stage:** `4` (`stage-04` / `record_review`)
- **Revision:** `revision-0001`
- **Repository:** `CultureBotAI/MediaIngredientMech` (`mediaingredientmech`)
- **Source Revision:** `24d76baa823d7fd07e8ea2596f0cca50e66392e2`
- **Scope Frozen At:** `2026-11-15T04:14:40Z`
- **Workflow Profile SHA-256:** `45d7c23d67f490cea6b31e336e5d2ac98b7ce8fa4e791bd9d3be092cfdb5a10d`
- **Frozen Effective Workflow SHA-256:** `7c320cc21b5f9d88f99208f0344a4bb533fdc96f17020fd091690a780e75b2b6`
- **Previous Finding-Disposition Evidence:** `reviews/workflow/mech-goal-sequence-20261019/cycle-000019/stage-05/revision-0001/evidence.yaml` (`d4e4c0efbc0d12a17774552eb054ec021d6469351725ef4bf6dd26c5246ef58e`)
- **Tracked Verified Closure Index:** `reviews/workflow/latest.yaml` (`104a95e61c15121eab2c93f1bf84471949de53baaa8411f4e70eb64f62dccddc`, `57` entries through Cycle 19 Stage 6 / PR `#1363`)

---

## 1. Frozen Corpus Inventory

Cycle 20 Stage 4 froze the current `main`-aligned source revision after the merged
Cycle 20 Stage 3 protein-example audit. The review task is read-only with
respect to scientific data: `data/ingredients/`, `data/curated/`,
`mappings/ingredient_mappings.sssom.tsv`, `UNIFIED_INGREDIENT_MAPPING.tsv`,
and existing `reviews/structured/` bundles were inspected and preserved as-is.

| Surface | Path / Glob | Count | SHA-256 Digest / Basis |
| --- | --- | ---: | --- |
| Individual ingredient records | `data/ingredients/**/*.yaml` | `2,956` | `1e978e977f3ce6e522117a4e7e06d25b4fb9d2eeda34a05ede17ad0b250d322d` sorted per-record `sha256sum` manifest |
| Mapped directory records | `data/ingredients/mapped/*.yaml` | `2,681` | `2,611` active `MAPPED` records + `70` `REJECTED` tombstones |
| Unmapped directory records | `data/ingredients/unmapped/*.yaml` | `275` | `262` `UNMAPPED`, `1` `AMBIGUOUS`, `12` `REJECTED` |
| Aggregate mapped collection | `data/curated/mapped_ingredients.yaml` | `1` | `774718362b921a560f8474a5d77874f2779e44ac5a6afc992040084a701ea628` |
| Aggregate unmapped collection | `data/curated/unmapped_ingredients.yaml` | `1` | `284adda3e7ac0940308770552afa0419aa4f30372ddb2074b39b6da630478fb1` |
| Other curated collections | `data/curated/unmapped_*.yaml` | `5` | Covered by `scripts/record_review.py --repo-root . check` |
| Native structured reviews | `reviews/structured/*/review.{yaml,md}` | `1,016` bundles / `2,032` files | Existing immutable YAML/Markdown review pairs verified by `scripts/record_review.py --repo-root . check` |
| LinkML ingredient schema | `src/mediaingredientmech/schema/mediaingredientmech.yaml` | `1` | `bb43dee29b21fdee72a48022456e733e49e95824c4c09674f9b3165c290fe012` |
| LinkML record-review schema | `schema/record_review.yaml` | `1` | `229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb` |
| SSSOM mapping artifact | `mappings/ingredient_mappings.sssom.tsv` | `1` | `d5f76fc404967477903fafc79eaba86ecfef9e2c391926ec08c3c1af4a5220b6` |
| Unified mapping artifact | `UNIFIED_INGREDIENT_MAPPING.tsv` | `1` | `f6a8eb844e578d79da9538abf99c244fc25b2c928c50c64c0477b1218092a0f1` |

Cycle 20 Stages 1-3 left the maintained ingredient corpus unchanged. A targeted
`git diff` from Cycle 19 Stage 4's reviewed source revision
`c8f1be257770608369be85769f5e572662a7ef1e` to the Stage 4 source revision
shows exactly one native structured review bundle added under
`reviews/structured/20261111T061500Z-cas-chebi-grounding-and-polysalt-audit/`
and no changes under the ingredient, curated, mapping, or schema surfaces listed
above.

---

## 2. Native Structured Review Verification

`scripts/record_review.py --repo-root . check` is the canonical repository-local
retention and source-hash gate for native review bundles. Cycle 20 Stage 4 ran it
against all `1,016` structured review bundles under `reviews/structured/`; the
checker validates the structured YAML schema, current target hashes,
rendered-Markdown parity, Git visibility, and append-only retention.

The verified native bundle inventory is:

| Kind | Bundle Count | Scope |
| --- | ---: | --- |
| `record` | `965` | Initial per-record and successor/reassessment reviews |
| `category` | `1` | Carnitine hydrochloride cohort review |
| `batch` | `33` | Corpus, source, SSSOM, hydrate, export-policy, and CAS/ChEBI batch reviews |
| `repository` | `17` | Repository-level SSSOM and curation follow-up reviews |
| **Total** | **`1,016`** | **All `2,956 / 2,956` current individual ingredient records have at least one declared `targets:` entry with a verified `source_sha256`** |

The only new bundle since Cycle 19 Stage 4 is:

| Review Bundle | Kind | Targets | Verdict | Deferred Native Findings |
| --- | --- | ---: | --- | ---: |
| `reviews/structured/20261111T061500Z-cas-chebi-grounding-and-polysalt-audit/review.yaml` | `batch` | `54` | `needs_curation` | `3` |

That batch review was added by PR `#1361` (`f1d8defb8`) and covers 13
ChEBI OLS4 seed candidates, 2 unmapped CAS-RN-only groundings, and 39
polysalt/polyhydrate structure-composition refusals. It is preserved as a
native structured review; this Stage 4 report only lifts its three deferred
native findings into workflow-level carry-forward IDs for Cycle 20 Stage 5.

---

## 3. Carry-Forward Finding Families

Cycle 19 Stage 5 consumed the previous accepted Stage 4 review output, grouped
all six active historical cohorts into three repair-ownership groups, linked
them to live GitHub issues `#921`, `#923`, and `#718`, and explicitly deferred
all six under stable IDs. Cycle 20 Stage 4 retains those six IDs and adds three
new deferred workflow findings from the 54-record CAS/ChEBI batch review.

| Workflow Finding ID | Carried From | Status | Native Source | Issue Link | Summary |
| --- | --- | --- | --- | --- | --- |
| `mim-c01-s04-f001` | `mim-c01-s04-f001` | `deferred` | Cycle 19 Stage 5 group `mim-c19-s05-g001` | `#921` | Reconcile the missing direct MicrobeDecoder occurrence on `data/ingredients/mapped/(2)-D-lyxose.yaml` |
| `mim-c01-s04-f003` | `mim-c01-s04-f003` | `deferred` | Cycle 19 Stage 5 group `mim-c19-s05-g002` | `#923` | Normalize non-monotonic `curation_history` timestamp order across 19 mapped ingredient records |
| `mim-c01-s04-f004` | `mim-c01-s04-f004` | `deferred` | Cycle 19 Stage 5 group `mim-c19-s05-g003` | `#718` | Adjudicate cellular-role and role claims lacking primary literature citations across 624 records |
| `mim-c01-s04-f005` | `mim-c01-s04-f005` | `deferred` | Cycle 19 Stage 5 group `mim-c19-s05-g003` | `#718` | Adjudicate media-occurrence claims requiring upstream recipe identity disambiguation across 29 records |
| `mim-c01-s04-f006` | `mim-c01-s04-f006` | `deferred` | Cycle 19 Stage 5 group `mim-c19-s05-g003` | `#718` | Adjudicate raw recipe/source synonym claims across 266 claims in 262 distinct records |
| `mim-c01-s04-f007` | `mim-c01-s04-f007` | `deferred` | Cycle 19 Stage 5 group `mim-c19-s05-g003` | `#718` | Adjudicate component, ontology-grounding, and identifier claims across 31 records |
| `mim-c20-s04-f001` | `mim-cas-chebi-ols4-seed-candidates-13` | `deferred` | `FIND-CHEBI-OLS4-SEED-CANDIDATES-13` | Stage 5 triage required | Apply 13 verified ChEBI OLS4 seed candidates through maintained mapping curation inputs |
| `mim-c20-s04-f002` | `mim-unmapped-cas-rn-groundings-2` | `deferred` | `FIND-UNMAPPED-CAS-RN-GROUNDINGS-2` | Stage 5 triage required | Ground `UNMAPPED_0159` and `UNMAPPED_0587` to CAS-RN-only identifiers where no ChEBI 3-star term exists |
| `mim-c20-s04-f003` | `mim-polysalt-deduplicated-smiles-refused-39` | `deferred` | `FIND-POLYSALT-DEDUPLICATED-SMILES-REFUSED-39` | Stage 5 triage required | Preserve the explicit refusal to seed 39 polysalt/polyhydrate records from deduplicated component SMILES |

The next Cycle 20 Stage 5 grouped-remediation goal should deduplicate the three
new CAS/ChEBI finding keys against existing issues before creating or reusing
real GitHub issue links. This Stage 4 goal did not create or mutate issues.

---

## 4. Limitations and Non-Actions

- Stage 4 did not edit ingredient YAML, curated aggregate YAML, SSSOM rows,
  unified mapping outputs, browser exports, or existing immutable structured
  review bundles.
- Stage 4 did not update `reviews/workflow/latest.yaml`; the tracked latest index
  is updated only after verified closure by a subsequent goal with supervisor
  evidence-index authority.
- Stage 4 did not backfill `causal_graphs` or `protein_examples`. Cycle 20
  Stages 2 and 3 verified that `docs/CAUSAL_GRAPH_CONTRACT.md` Steps 3-7 and
  the validated graph/UniProt writer remain prerequisites for safe YAML writes.
- The new CAS/ChEBI native review findings are deferred for issue grouping and
  maintained-input remediation in Cycle 20 Stage 5; this report preserves them
  without treating them as already remediated.
