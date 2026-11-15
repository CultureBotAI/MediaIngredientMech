# MediaIngredientMech Cycle 20 Stage 4 Review Findings (`review_findings`)

- **Run ID:** `mech-goal-sequence-20261019`
- **Cycle:** `20` (`cycle-000020`)
- **Stage:** `4` (`stage-04` / `record_review`)
- **Revision:** `revision-0001`
- **Reviewed Source Revision:** `24d76baa823d7fd07e8ea2596f0cca50e66392e2`
- **Native Structured Review Bundles:** `1,016` total under `reviews/structured/`
- **Carry-Forward Set:** `9` deferred workflow findings

## Overview Table

| Workflow Finding ID | Carried From | Status | Category | Severity | Repair Owner Skill | Issue Link | Summary |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `mim-c01-s04-f001` | `mim-c01-s04-f001` | `deferred` | `quantity` | `major` | `.claude/skills/curate-yaml-record/SKILL.md` | `#921` | Reconcile missing direct MicrobeDecoder occurrence on `data/ingredients/mapped/(2)-D-lyxose.yaml` (`CHEBI:62318`). |
| `mim-c01-s04-f003` | `mim-c01-s04-f003` | `deferred` | `provenance` | `minor` | `.claude/skills/curate-yaml-record/SKILL.md` | `#923` | Normalize non-monotonic `curation_history` timestamp order across 19 mapped ingredient records. |
| `mim-c01-s04-f004` | `mim-c01-s04-f004` | `deferred` | `evidence` | `major` | `.claude/skills/ingredient-roles/SKILL.md` | `#718` | Adjudicate cellular-role and role claims lacking primary literature citations across 624 records. |
| `mim-c01-s04-f005` | `mim-c01-s04-f005` | `deferred` | `evidence` | `minor` | `.claude/skills/ingredient-roles/SKILL.md` | `#718` | Adjudicate media-occurrence claims requiring upstream recipe identity disambiguation across 29 records. |
| `mim-c01-s04-f006` | `mim-c01-s04-f006` | `deferred` | `identity` / `grounding` | `major` | `.claude/skills/map-media-ingredients/SKILL.md` | `#718` | Resolve source-backed chemical identity and synonym-token scope across 266 claims in 262 distinct records. |
| `mim-c01-s04-f007` | `mim-c01-s04-f007` | `deferred` | `nomenclature` / `representation` / `identity` | `major` / `minor` | `.claude/skills/curate-yaml-record/SKILL.md` | `#718` | Adjudicate stock formulation, component source scope, and specific ontology grounding across 31 records. |
| `mim-c20-s04-f001` | `mim-cas-chebi-ols4-seed-candidates-13` | `deferred` | `grounding` | `minor` | `.claude/skills/map-media-ingredients/SKILL.md` | Stage 5 triage required | Apply 13 verified ChEBI OLS4 seed candidates from the CAS/ChEBI batch review through maintained curation inputs. |
| `mim-c20-s04-f002` | `mim-unmapped-cas-rn-groundings-2` | `deferred` | `grounding` | `minor` | `.claude/skills/map-media-ingredients/SKILL.md` | Stage 5 triage required | Ground `UNMAPPED_0159` and `UNMAPPED_0587` to CAS-RN-only identifiers where no ChEBI 3-star term exists. |
| `mim-c20-s04-f003` | `mim-polysalt-deduplicated-smiles-refused-39` | `deferred` | `consistency` | `informational` | `.claude/skills/reconcile-review-records/SKILL.md` | Stage 5 triage required | Preserve the explicit refusal to use CAS Common Chemistry deduplicated component SMILES for 39 polysalt/polyhydrate records. |

## Prior Deferred Cohorts Retained From Cycle 19 Stage 5

### `mim-c01-s04-f001`

- **Status:** `deferred`
- **Issue:** `https://github.com/CultureBotAI/MediaIngredientMech/issues/921`
- **Cycle 19 Group:** `mim-c19-s05-g001`
- **Disposition:** carried forward because `(2)-D-lyxose.yaml` is byte-bound in
  `reports/sssom_completion_20260921/mapping_review/nonmapping_cohorts.json`
  and `reports/semantic_review_20260921/resolution/current-review.json`.

### `mim-c01-s04-f003`

- **Status:** `deferred`
- **Issue:** `https://github.com/CultureBotAI/MediaIngredientMech/issues/923`
- **Cycle 19 Group:** `mim-c19-s05-g002`
- **Disposition:** carried forward because all 19 affected mapped records are
  byte-bound in `reports/sssom_completion_20260921/review.json` and
  `reports/semantic_review_20260921/resolution/current-review.json`.

### `mim-c01-s04-f004` through `mim-c01-s04-f007`

- **Status:** `deferred`
- **Issue:** `https://github.com/CultureBotAI/MediaIngredientMech/issues/718`
- **Cycle 19 Group:** `mim-c19-s05-g003`
- **Disposition:** carried forward as the open semantic-review backlog across
  role-evidence, media-occurrence, synonym-token, component-scope, and ontology
  grounding claims. Cycle 19 Stage 5 deduplicated these under issue `#718`;
  the closed issue `#861` remains context for the false-certainty overstatement
  that was already resolved.

## New Cycle 20 Stage 4 Deferred Findings

### `mim-c20-s04-f001` - ChEBI OLS4 Seed Candidates

- **Native finding:** `FIND-CHEBI-OLS4-SEED-CANDIDATES-13`
- **Native issue key:** `mim-cas-chebi-ols4-seed-candidates-13`
- **Native review:** `reviews/structured/20261111T061500Z-cas-chebi-grounding-and-polysalt-audit/review.yaml`
- **Status:** `deferred`
- **Severity:** `minor`
- **Affected scope:** 13 mapped ingredient records
- **Follow-up:** Stage 5 should deduplicate the issue key, group it with the
  appropriate mapping-maintenance owner, and apply exact CHEBI OLS4 seed
  candidates only through the repository's maintained mapping curation inputs.

### `mim-c20-s04-f002` - Unmapped CAS-RN Groundings

- **Native finding:** `FIND-UNMAPPED-CAS-RN-GROUNDINGS-2`
- **Native issue key:** `mim-unmapped-cas-rn-groundings-2`
- **Native review:** `reviews/structured/20261111T061500Z-cas-chebi-grounding-and-polysalt-audit/review.yaml`
- **Status:** `deferred`
- **Severity:** `minor`
- **Affected scope:** `data/ingredients/unmapped/Ethanolamine_Acetate.yaml` and
  `data/ingredients/unmapped/Α-D-Glucose_Monohydrate.yaml`
- **Follow-up:** Stage 5 should verify there is still no specific 3-star ChEBI
  term, then ground `UNMAPPED_0159` to `cas:54300-24-2` and `UNMAPPED_0587` to
  `cas:14431-43-7` using the identifier-management and mapping curation rules.

### `mim-c20-s04-f003` - Polysalt/Polyhydrate SMILES Refusals

- **Native finding:** `FIND-POLYSALT-DEDUPLICATED-SMILES-REFUSED-39`
- **Native issue key:** `mim-polysalt-deduplicated-smiles-refused-39`
- **Native review:** `reviews/structured/20261111T061500Z-cas-chebi-grounding-and-polysalt-audit/review.yaml`
- **Status:** `deferred`
- **Severity:** `informational`
- **Affected scope:** 39 polysalt or polyhydrate records
- **Follow-up:** Stage 5 should preserve the refusal as an accepted-risk or
  no-change disposition unless a maintained exact structure source appears; the
  rejected CAS Common Chemistry deduplicated component SMILES are explicitly not
  an admissible structure seed for these records.
