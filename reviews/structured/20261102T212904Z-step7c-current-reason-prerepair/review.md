# Independent pre-repair observation of stale Step7c current mapping reasons

- Review: 20261102T212904Z-step7c-current-reason-prerepair
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-11-02T21:29:04Z
- Finished UTC: 2026-11-02T21:29:04Z
- Reviewer: Codex /root/step7a_final_adversarial (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: false

## Summary

Four generated current-reason claims contradict receipt24-corrected source/canonical fields. Preserve the archived reasons and qualify their historical scope under the verified transition; keep all touched mapping rows withheld.

## Scope And Provenance

Exactly four generated current-reason entries in the first Step7c post-receipt24 assembly, before the issue1112 repair.

Selection: Directly reproduced contradictions in rows38,233,2229 and2920; not a broad historical review sweep.
Coverage: full; 4 reviewed / 4 in the declared population.
Source: working_tree at Git base 54eadef802d2ff159bf4ba9bec51492fe3bb99d4.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| mapping-reason-38 | reports/sssom_completion_20260921/review.json # decisions[source_position=38] | generated | MIM:14-Butanediol |
| mapping-reason-233 | reports/sssom_completion_20260921/review.json # decisions[source_position=233] | generated | MIM:5-dehydro-D-gluconate |
| mapping-reason-2229 | reports/sssom_completion_20260921/review.json # decisions[source_position=2229] | generated | MIM:Phenethylamine_Hydrochloride |
| mapping-reason-2920 | reports/sssom_completion_20260921/review.json # decisions[source_position=2920] | generated | MIM:Wc_Trace_Elements_Solution |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Compare each current reason to exact current canonical fields and receipt24 | failed | True | mapping-reason-38, mapping-reason-233, mapping-reason-2229, mapping-reason-2920 | Four confirmed false-current claims remain in generated decision/evidence prose after the verified source changes. |
| Check current touched-row dispositions | passed | True | mapping-reason-38, mapping-reason-233, mapping-reason-2229, mapping-reason-2920 | All eight batch rows are WITHHOLD. The complete mapping ledger has1744SUPPORTED and1241WITHHOLD; this audit does not approve any row. |

## Scientific And Domain Assessments

### Current reason text versus historical concerns

provenance: concern. Targets: mapping-reason-38, mapping-reason-233, mapping-reason-2229, mapping-reason-2920.

The correction receipts support narrowly qualifying four historical allegations. WC provisional TRACE_ELEMENT and all unassessed relation, identity, alias-scope and evidence concerns remain review obligations. Preserve original historical basis and no-approval semantics.

## Findings

### stale-current-reasons: Generated current review reasons repeat corrected historical defects as still present

minor / open / confirmed; issue key: mim-1112-step7c-historical-concern-qualification.

Rows38,233,2229 and2920 retain current-tense claims that fragment aliases still leak, the mono-keto row still publishes a di-keto name without source recovery, the free-base row still exports hydrochloride, and WC remains exact-mapped to a generic class. The captured canonical and source records prove those narrow portions corrected. Historical concerns and residual/unassessed role or mapping obligations remain valid as review history; no row should be approved by this provenance repair.

## Recommended Actions And Acceptance Checks

### qualify-historical-reasons

Add a narrowly receipt/owner/row-bound historical-concern qualification to the native assembler, with positive and refusal regression tests. Rebuild current products while preserving original historical inputs and all WITHHOLD dispositions.

- Corrected portions explicitly described as historical; the original text and evidence basis remain available.
- No unrelated/unverified change receives qualification.
- All eight touched rows stay WITHHOLD; no scientific or role approval growth.
- Independent final review verifies generated products and reconciles this exact finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| diagnostics | reports/step7c_pre_repair_1112_20261102/diagnostics.json | supports | Exact captured four rows, decisions, evidence basis, issue1112 body/readback and live dedup; primary finding packet records contradiction. |
| canonical | mappings/ingredient_mappings.sssom.tsv | supports | Current canonical rows38/233/2229/2920 contain the reviewed alias removals and broad WC parent relation. |
| mapping-review | reports/sssom_completion_20260921/review.json | supports | Current generated decision reasons still assert four corrected defects as present; all four remain withheld. |
| mapping-evidence | reports/sssom_completion_20260921/mapping-evidence.json | supports | Same false-current wording and explicit receipt24/historical basis. |
| receipt24 | reports/sssom_completion_20260921/mapping_changes/issue751-313-235-stock-and-source-labels.json | supports | Native transition binds source corrections and canonical endpoints while explicitly granting no approval. |

## Limits And Additional Notes

- Captured first-generation Step7c product observation; later repair may change current working bytes.
- Source.git_revision uses durable merged54eadef8 with exact working-tree overlay inputs; de31ae2f is the observed execution checkpoint only.
- Final tests, QC and final-head review remain required and are not claimed here.
- Standalone observation; supervisor binding remains null.
- The source correction itself and canonical row scope were independently cleared earlier; this newly discovered wording defect does not undo source identity decisions.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261102T212904Z-step7c-current-reason-prerepair
kind: batch
repository: CultureBotAI/MediaIngredientMech
title: Independent pre-repair observation of stale Step7c current mapping reasons
started_at: '2026-11-02T21:29:04Z'
finished_at: '2026-11-02T21:29:04Z'
reviewer:
  identity: Codex /root/step7a_final_adversarial
  kind: agent
  independence: independent
  independence_basis: Reviewer did not author assembler, source correction, projection
    operator or generated products; independently compared frozen canonical rows,
    decisions, evidence and native receipt.
skill: reconcile-review-records; review-sssom-output
completion: completed
verdict: needs_curation
scientific_review: false
native_verdict: Confirmed generated-provenance finding1112 OPEN; all scientific holds
  retained.
summary: Four generated current-reason claims contradict receipt24-corrected source/canonical
  fields. Preserve the archived reasons and qualify their historical scope under the
  verified transition; keep all touched mapping rows withheld.
source:
  git_revision: 54eadef802d2ff159bf4ba9bec51492fe3bb99d4
  state: working_tree
  inputs:
  - path: .claude/skills/reconcile-review-records/SKILL.md
    sha256: b8c3e3fdb31e58a49343f20b11c7a1c2a3616f16ef36601ccd072e2693031474
    role: context
  - path: AGENTS.md
    sha256: fc7728986d82b43359a9055ae233bcf0d4ebaef8bb657ef1b4bb4aa87b2cbaaf
    role: context
  - path: MAPPING_SEMANTICS.md
    sha256: 6b52f2ac48109ddd5d81996a136b19776cab55efa69a5ec832cf716d6885a062
    role: context
  - path: conf/record_review.yaml
    sha256: 07a8fa6d17ee664c7a2bc2d5b5821bd106f6aa454299b4f3e0440176876cd82e
    role: context
  - path: data/ingredients/mapped/14-Butanediol.yaml
    sha256: 55cd8e1fa92c1ba42584e7ae3b9c04a78b0a8ba137d559c45b303bff2a24015c
    role: context
  - path: data/ingredients/mapped/5-dehydro-D-gluconate.yaml
    sha256: 54d31d5d3d203accaadfb8ff171bf9f178a0a72210b1dd12f2078fa09acd9bb5
    role: context
  - path: data/ingredients/mapped/Phenethylamine_Hydrochloride.yaml
    sha256: c1c7fe3ea0f2ad27aa9a9ab246e10d2796062c8d829e40212487e0802e48b30b
    role: context
  - path: data/ingredients/mapped/Wc_Trace_Elements_Solution.yaml
    sha256: cc5326c0fa7ef1d0d5245cbd151a8f0c7a8ff6f92a061a3c112a1df415e3e480
    role: context
  - path: docs/record-review-profile.md
    sha256: da17e2048a13514a422bc94bd2f8d48943cffc5689b96e3f07da26423248d1a7
    role: context
  - path: docs/record-reviews.md
    sha256: 452a19ab688276747b7c4308523a14d4d99c1c39ef6909ae8a90b85b7a9b3e9b
    role: context
  - path: mappings/ingredient_mappings.sssom.tsv
    sha256: 62fd37c2ed8ace9b9295618d44e251d11fc35feb711053b66d322e5a7bce14f1
    role: context
  - path: reports/sssom_completion_20260921/assemble_review.py
    sha256: b791bafb32eaad4f9e7a19f293aab52775913f593318df85ea31aa76aa727446
    role: context
  - path: reports/sssom_completion_20260921/mapping-evidence.json
    sha256: 1e72a5eb111ad8df664542d648227a91a7cd96b5b46cc15db2b9fc88e335b707
    role: context
  - path: reports/sssom_completion_20260921/mapping_changes/issue751-313-235-stock-and-source-labels.json
    sha256: 3d8d3d1189d0393d5ccd23ce3b83a5196e1664f045269254160df33a20e6ea07
    role: context
  - path: reports/sssom_completion_20260921/review.json
    sha256: a5fc7dc1509ac8ff7ab06606c9eb21fde3bb9bd072ba56077a051045e21ad1da
    role: target
  - path: reports/step7c_pre_repair_1112_20261102/diagnostics.json
    sha256: 533c58346b4e45f22fe7eaec0dbd326ae267e433200268ce378adb275153e09b
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/record_review.py
    sha256: 95a4ec41e38ec47ba3578e76838c46a0adbf47e49ad3636524735d08cfcb1c4d
    role: context
scope:
  description: Exactly four generated current-reason entries in the first Step7c post-receipt24
    assembly, before the issue1112 repair.
  selection: Directly reproduced contradictions in rows38,233,2229 and2920; not a
    broad historical review sweep.
  coverage: full
  population_size: 4
  reviewed_target_ids:
  - mapping-reason-38
  - mapping-reason-233
  - mapping-reason-2229
  - mapping-reason-2920
  exclusions:
  - target: Scientific mapping approval, provisional roles, unrelated rows and final
      complete release gates
    reason: Only generated provenance wording was assessed; corrected fields do not
      renew approval.
  - target: Original historical concern inputs and original native reviews
    reason: Must remain immutable; this observation does not reject or silently close
      their broader findings.
targets:
- target_id: mapping-reason-38
  path: reports/sssom_completion_20260921/review.json
  selector: decisions[source_position=38]
  label: MIM:14-Butanediol
  kind: generated
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/14-Butanediol.yaml
    role: maintained record context
  - repository: CultureBotAI/MediaIngredientMech
    path: reports/sssom_completion_20260921/assemble_review.py
    role: current reason producer
- target_id: mapping-reason-233
  path: reports/sssom_completion_20260921/review.json
  selector: decisions[source_position=233]
  label: MIM:5-dehydro-D-gluconate
  kind: generated
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/5-dehydro-D-gluconate.yaml
    role: maintained record context
  - repository: CultureBotAI/MediaIngredientMech
    path: reports/sssom_completion_20260921/assemble_review.py
    role: current reason producer
- target_id: mapping-reason-2229
  path: reports/sssom_completion_20260921/review.json
  selector: decisions[source_position=2229]
  label: MIM:Phenethylamine_Hydrochloride
  kind: generated
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Phenethylamine_Hydrochloride.yaml
    role: maintained record context
  - repository: CultureBotAI/MediaIngredientMech
    path: reports/sssom_completion_20260921/assemble_review.py
    role: current reason producer
- target_id: mapping-reason-2920
  path: reports/sssom_completion_20260921/review.json
  selector: decisions[source_position=2920]
  label: MIM:Wc_Trace_Elements_Solution
  kind: generated
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Wc_Trace_Elements_Solution.yaml
    role: maintained record context
  - repository: CultureBotAI/MediaIngredientMech
    path: reports/sssom_completion_20260921/assemble_review.py
    role: current reason producer
checks:
- check_id: current-reason-readback
  name: Compare each current reason to exact current canonical fields and receipt24
  status: failed
  required: true
  summary: Four confirmed false-current claims remain in generated decision/evidence
    prose after the verified source changes.
  target_ids:
  - mapping-reason-38
  - mapping-reason-233
  - mapping-reason-2229
  - mapping-reason-2920
  evidence_ids:
  - diagnostics
  - canonical
  - mapping-review
  - mapping-evidence
  - receipt24
- check_id: hold-preservation
  name: Check current touched-row dispositions
  status: passed
  required: true
  summary: All eight batch rows are WITHHOLD. The complete mapping ledger has1744SUPPORTED
    and1241WITHHOLD; this audit does not approve any row.
  target_ids:
  - mapping-reason-38
  - mapping-reason-233
  - mapping-reason-2229
  - mapping-reason-2920
  evidence_ids:
  - mapping-review
  - receipt24
evidence:
- evidence_id: diagnostics
  kind: validation
  reference: reports/step7c_pre_repair_1112_20261102/diagnostics.json
  accessed_at: '2026-11-02T21:29:04Z'
  support: supports
  summary: Exact captured four rows, decisions, evidence basis, issue1112 body/readback
    and live dedup; primary finding packet records contradiction.
  snapshot_sha256: 533c58346b4e45f22fe7eaec0dbd326ae267e433200268ce378adb275153e09b
- evidence_id: canonical
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  accessed_at: '2026-11-02T21:29:04Z'
  support: supports
  summary: Current canonical rows38/233/2229/2920 contain the reviewed alias removals
    and broad WC parent relation.
  snapshot_sha256: 62fd37c2ed8ace9b9295618d44e251d11fc35feb711053b66d322e5a7bce14f1
- evidence_id: mapping-review
  kind: record_content
  reference: reports/sssom_completion_20260921/review.json
  accessed_at: '2026-11-02T21:29:04Z'
  support: supports
  summary: Current generated decision reasons still assert four corrected defects
    as present; all four remain withheld.
  snapshot_sha256: a5fc7dc1509ac8ff7ab06606c9eb21fde3bb9bd072ba56077a051045e21ad1da
- evidence_id: mapping-evidence
  kind: record_content
  reference: reports/sssom_completion_20260921/mapping-evidence.json
  accessed_at: '2026-11-02T21:29:04Z'
  support: supports
  summary: Same false-current wording and explicit receipt24/historical basis.
  snapshot_sha256: 1e72a5eb111ad8df664542d648227a91a7cd96b5b46cc15db2b9fc88e335b707
- evidence_id: receipt24
  kind: validation
  reference: reports/sssom_completion_20260921/mapping_changes/issue751-313-235-stock-and-source-labels.json
  accessed_at: '2026-11-02T21:29:04Z'
  support: supports
  summary: Native transition binds source corrections and canonical endpoints while
    explicitly granting no approval.
  snapshot_sha256: 3d8d3d1189d0393d5ccd23ce3b83a5196e1664f045269254160df33a20e6ea07
assessments:
- assessment_id: historical-current-distinction
  area: provenance
  topic: Current reason text versus historical concerns
  outcome: concern
  summary: The correction receipts support narrowly qualifying four historical allegations.
    WC provisional TRACE_ELEMENT and all unassessed relation, identity, alias-scope
    and evidence concerns remain review obligations. Preserve original historical
    basis and no-approval semantics.
  target_ids:
  - mapping-reason-38
  - mapping-reason-233
  - mapping-reason-2229
  - mapping-reason-2920
  evidence_ids:
  - diagnostics
  - canonical
  - mapping-review
  - mapping-evidence
  - receipt24
findings:
- finding_id: stale-current-reasons
  issue_key: mim-1112-step7c-historical-concern-qualification
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Generated current review reasons repeat corrected historical defects as still
    present
  description: Rows38,233,2229 and2920 retain current-tense claims that fragment aliases
    still leak, the mono-keto row still publishes a di-keto name without source recovery,
    the free-base row still exports hydrochloride, and WC remains exact-mapped to
    a generic class. The captured canonical and source records prove those narrow
    portions corrected. Historical concerns and residual/unassessed role or mapping
    obligations remain valid as review history; no row should be approved by this
    provenance repair.
  target_ids:
  - mapping-reason-38
  - mapping-reason-233
  - mapping-reason-2229
  - mapping-reason-2920
  field_paths:
  - decisions[].review_reason
  - entries[].review_reason
  evidence_ids:
  - diagnostics
  - canonical
  - mapping-review
  - mapping-evidence
  - receipt24
  native_severity: P3
  normalization_reason: Incorrect generated provenance wording; no erroneous row approval
    or loss of holds observed.
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: reports/sssom_completion_20260921/assemble_review.py
    role: generated reason producer
  external_issues:
  - https://github.com/CultureBotAI/MediaIngredientMech/issues/1112
actions:
- action_id: qualify-historical-reasons
  description: Add a narrowly receipt/owner/row-bound historical-concern qualification
    to the native assembler, with positive and refusal regression tests. Rebuild current
    products while preserving original historical inputs and all WITHHOLD dispositions.
  finding_ids:
  - stale-current-reasons
  target_ids:
  - mapping-reason-38
  - mapping-reason-233
  - mapping-reason-2229
  - mapping-reason-2920
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: reports/sssom_completion_20260921/assemble_review.py
    role: generated reason producer
  acceptance_checks:
  - Corrected portions explicitly described as historical; the original text and evidence
    basis remain available.
  - No unrelated/unverified change receives qualification.
  - All eight touched rows stay WITHHOLD; no scientific or role approval growth.
  - Independent final review verifies generated products and reconciles this exact
    finding.
limitations:
- Captured first-generation Step7c product observation; later repair may change current
  working bytes.
- Source.git_revision uses durable merged54eadef8 with exact working-tree overlay
  inputs; de31ae2f is the observed execution checkpoint only.
- Final tests, QC and final-head review remain required and are not claimed here.
notes:
- Standalone observation; supervisor binding remains null.
- The source correction itself and canonical row scope were independently cleared
  earlier; this newly discovered wording defect does not undo source identity decisions.
links:
- https://github.com/CultureBotAI/MediaIngredientMech/issues/1112
tags:
- step7c
- independent
- provenance
- pre-repair
- no-scientific-approval
```
