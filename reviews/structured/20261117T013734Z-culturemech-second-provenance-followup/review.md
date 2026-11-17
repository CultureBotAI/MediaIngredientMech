# Independent two-field provenance reconciliation for the second intake review

- Review: 20261117T013734Z-culturemech-second-provenance-followup
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-11-17T01:37:34Z
- Finished UTC: 2026-11-17T01:37:34Z
- Reviewer: Codex release687_current (independent)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Independently inspected the exact successor diff: only the chlorate narrative digest and sodium-sulfide witness explanation changed. All scientific dispositions, case pins and payload membership remain byte-equivalent at the parsed-field level. The two prior minor findings are resolved; the original bounded scientific sample and its limitations remain unchanged.

## Scope And Provenance

All decision reasons, sampled complete scientific payloads and precise blocking witnesses.

Selection: Risk-based sample declared per target; no statistical representativeness claimed.
Coverage: sampled; 1 reviewed / 143 in the declared population.
Source: working_tree at Git base 557d2bd45347ccc87e1daf49119524f82c9743ed.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| second-219-284 | reports/culturemech_intake_second_cross_review_20261117-v2/second-219-284.json | source | second-219-284 |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Explicit bounded cross-review | passed | True | second-219-284 | Independently read all 143 decision reasons. Read complete owner266 plus its two descriptors and exact local canonical row; approval correctly excludes the external parent CHEBI:15978. Read complete owner268 history plus full Pinchuk old-side REPLACE case 1d009355 (zero positive occurrences) and its separate monobasic-conflict witness 013d738a. Read complete owner281 and exact ammonium-salt versus anion witness 81424774. Read complete owner270 and hydrate witness c51054. The selected identity boundaries and context-only replacement membership are preserved. Narrative provenance errors were independently confirmed and filed as issues 1535 and 1536; they do not change these dispositions. |

## Scientific And Domain Assessments

### Bounded independent source-binding cross-review

identity: supported. Targets: second-219-284.

Independently read all 143 decision reasons. Read complete owner266 plus its two descriptors and exact local canonical row; approval correctly excludes the external parent CHEBI:15978. Read complete owner268 history plus full Pinchuk old-side REPLACE case 1d009355 (zero positive occurrences) and its separate monobasic-conflict witness 013d738a. Read complete owner281 and exact ammonium-salt versus anion witness 81424774. Read complete owner270 and hydrate witness c51054. The selected identity boundaries and context-only replacement membership are preserved. Narrative provenance errors were independently confirmed and filed as issues 1535 and 1536; they do not change these dispositions. Successor independently checked: both minor narrative findings corrected with no scientific decision changes.

## Findings

### chlorate-locator: Incorrect narrative descriptor digest

minor / resolved / confirmed; issue key: culturemech-intake-second-chlorate-locator-1535.

Case b198a7c5e3164e5112e16cb10007008ceb321feeff7a7c4bc2f2dcad109d6e3d evidence_locators[0] contains an extra 4c in descriptor digest d300b6526d61bfef904b8c9ca20b96a7c020a0bb686b85b9f007dc74079a07f8. The author disclosed this before this reviewer independently verified it. The machine-readable inspected hash and complete case pin are correct.

Disposition: The exact successor changes only the documented narrative error. Original targets and evidence remain retained; scientific identity judgments and machine payload pins are unchanged.

### sulfide-witness-wording: Witness explanation asserts absent embedded fields

minor / resolved / confirmed; issue key: culturemech-intake-second-sulfide-witness-1536.

Case d0c8d3c8ab968b81703d7291e78c7bbb018c735fd3e2cd11b342b18b11d1be20 witness c51054cca36e6a38a39f35805ff8a40060d922a22aa5f7b78988ff6d6906217c has no term or mediaingredientmech_chebi_term. Its explanation incorrectly says those fields assert anhydrous CHEBI76208. The selected candidate/owner, rather than this descriptor, is anhydrous. Literal sodium sulfide hydrate evidence still justifies WITHHOLD against that owner.

Disposition: The exact successor changes only the documented narrative error. Original targets and evidence remain retained; scientific identity judgments and machine payload pins are unchanged.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| second-219-284 | reports/culturemech_intake_second_cross_review_20261117-v2/second-219-284.json | partial | Independently read all 143 decision reasons. Read complete owner266 plus its two descriptors and exact local canonical row; approval correctly excludes the external parent CHEBI:15978. Read complete owner268 history plus full Pinchuk old-side REPLACE case 1d009355 (zero positive occurrences) and its separate monobasic-conflict witness 013d738a. Read complete owner281 and exact ammonium-salt versus anion witness 81424774. Read complete owner270 and hydrate witness c51054. The selected identity boundaries and context-only replacement membership are preserved. Narrative provenance errors were independently confirmed and filed as issues 1535 and 1536; they do not change these dispositions. |
| successor-two-field-diff | reports/culturemech_second_provenance_followup_20261117/second-219-284-v2.json | supports | Exact pinned successor equals the original document with only the two independently inspected narrative corrections. The corrected digest matches its inspected member; the hydrate explanation correctly distinguishes source wording from the selected anhydrous owner. |

## Limits And Additional Notes

- Not an independent double-review of every scientific payload, source coordinate or original publication. Exact sample sizes and witnesses are declared per target.
- The sampled packet claims and maintained owners were reread; underlying primary publications were not re-retrieved during this second-pass cross-review. Quantity, growth, release adoption and global canonical publication are outside its scope.
- Native finalization, exact product replay, complete author-case coverage and final PR review remain required. Timestamps record consolidation of the preceding read-only inspection.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261117T013734Z-culturemech-second-provenance-followup
kind: batch
repository: CultureBotAI/MediaIngredientMech
title: Independent two-field provenance reconciliation for the second intake review
started_at: '2026-11-17T01:37:34Z'
finished_at: '2026-11-17T01:37:34Z'
reviewer:
  identity: Codex release687_current
  kind: agent
  independence: independent
  independence_basis: Did not author these second-slice decisions. Authored disjoint
    middle binding decisions and contributed upstream CultureMech schema, provenance
    and some curation, including the Pinchuk variant. This report claims independence
    from the reviewed binding judgments, not all upstream curation, and only the explicitly
    listed payload sample.
skill: lbnl-mech-record-review; native docs/record-reviews.md and MAPPING_SEMANTICS.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: 'Independently inspected the exact successor diff: only the chlorate narrative
  digest and sodium-sulfide witness explanation changed. All scientific dispositions,
  case pins and payload membership remain byte-equivalent at the parsed-field level.
  The two prior minor findings are resolved; the original bounded scientific sample
  and its limitations remain unchanged.'
source:
  git_revision: 557d2bd45347ccc87e1daf49119524f82c9743ed
  state: working_tree
  inputs:
  - path: .temp/1453/review-partitions-final-v3-6f1b1d18a5/owner-0266.json
    sha256: cce52fa60e0ff4fc1c539cd13a9c26e3e1667546a21b75a646f7d92cc8033f58
    role: context
  - path: .temp/1453/review-partitions-final-v3-6f1b1d18a5/owner-0268.json
    sha256: 790f5d459c8b9e43fa0355b9294d1ba655801821b78ddd79ce89e34a92024263
    role: context
  - path: .temp/1453/review-partitions-final-v3-6f1b1d18a5/owner-0270.json
    sha256: 74e190254bd494259dbb4cdfdaa3df291d5df53d3ac9f4888295593e6b4e0fb0
    role: context
  - path: .temp/1453/review-partitions-final-v3-6f1b1d18a5/owner-0273.json
    sha256: 0adbfd305a0d3a4cf6c84a6da8aa381e62ebe169720fe195ea0c54480450028d
    role: context
  - path: .temp/1453/review-partitions-final-v3-6f1b1d18a5/owner-0281.json
    sha256: b5ba9137250304c88546ec4ca449105ac9265a3aa9de39feb450e13c7e6d60dd
    role: context
  - path: MAPPING_SEMANTICS.md
    sha256: 6b52f2ac48109ddd5d81996a136b19776cab55efa69a5ec832cf716d6885a062
    role: context
  - path: data/ingredients/mapped/Na2_Beta-glycerol_PO4_X_5_H2O.yaml
    sha256: c164e18d33c5954842f23467b3825f9bf31e92d9cec5627d05f23c9cd5fc70f5
    role: context
  - path: data/ingredients/mapped/Na2hpo4.yaml
    sha256: ae7db57bde47a3797858aa3d5b0ca8f64921a2d453645096233dab4012beb9d4
    role: context
  - path: data/ingredients/mapped/Na2s.yaml
    sha256: db44dbfe79849cd40432beb30aeaf6ed242e55578b8ceef9cfa95479d21ae547
    role: context
  - path: data/ingredients/mapped/Naclo3.yaml
    sha256: db0c6987dd528bd31d3bb66437355be2e4a4cfc94bf4ddddac6e378fba8c8b1d
    role: context
  - path: data/ingredients/mapped/Nh4h2po4.yaml
    sha256: a2d12b074aab0a9b3e910910df77b4470e20e4941841d9d42083657a6c70e724
    role: context
  - path: reports/culturemech_intake_second_cross_review_20261117-v2/second-219-284.json
    sha256: a309fe8b6a841afea0d0b4463a205fe322a2722fced2797930bd0cbfe815791b
    role: target
  - path: reports/culturemech_second_provenance_followup_20261117/second-219-284-v2.json
    sha256: b846c03927bd2d0e5e09bbb4b6911295761c4e11f743c1e223d67bd5eac731ef
    role: context
  - path: reports/sssom_completion_20260921/review.json
    sha256: ab301d1f66276cdfeefea79080ce49f26ebb02c1920a53c71512c14b283b16cf
    role: context
  - path: reviews/structured/20261117T013626Z-culturemech-intake-second-cross-review/review.yaml
    sha256: 35ce19f2e0fac754f22e47332ddeb43a75782f591009e303c25b84350f21a7cc
    role: context
targets:
- target_id: second-219-284
  path: reports/culturemech_intake_second_cross_review_20261117-v2/second-219-284.json
  kind: source
  label: second-219-284
  ownership_note: Frozen review decisions; maintained candidate owners and exact source
    cases remain in the bound owner packets. This report does not mutate those scientific
    owners.
scope:
  description: All decision reasons, sampled complete scientific payloads and precise
    blocking witnesses.
  selection: Risk-based sample declared per target; no statistical representativeness
    claimed.
  coverage: sampled
  sampling_method: Purposive exact preparation, supplied-form, stale-ID and gas/quantity
    boundary cases; all reasons read, scientific payloads only as explicitly listed.
  population_size: 143
  reviewed_target_ids:
  - second-219-284
checks:
- check_id: second-219-284
  name: Explicit bounded cross-review
  status: passed
  required: true
  summary: Independently read all 143 decision reasons. Read complete owner266 plus
    its two descriptors and exact local canonical row; approval correctly excludes
    the external parent CHEBI:15978. Read complete owner268 history plus full Pinchuk
    old-side REPLACE case 1d009355 (zero positive occurrences) and its separate monobasic-conflict
    witness 013d738a. Read complete owner281 and exact ammonium-salt versus anion
    witness 81424774. Read complete owner270 and hydrate witness c51054. The selected
    identity boundaries and context-only replacement membership are preserved. Narrative
    provenance errors were independently confirmed and filed as issues 1535 and 1536;
    they do not change these dispositions.
  target_ids:
  - second-219-284
evidence:
- evidence_id: second-219-284
  kind: record_content
  reference: reports/culturemech_intake_second_cross_review_20261117-v2/second-219-284.json
  accessed_at: '2026-11-17T01:36:26Z'
  support: partial
  summary: Independently read all 143 decision reasons. Read complete owner266 plus
    its two descriptors and exact local canonical row; approval correctly excludes
    the external parent CHEBI:15978. Read complete owner268 history plus full Pinchuk
    old-side REPLACE case 1d009355 (zero positive occurrences) and its separate monobasic-conflict
    witness 013d738a. Read complete owner281 and exact ammonium-salt versus anion
    witness 81424774. Read complete owner270 and hydrate witness c51054. The selected
    identity boundaries and context-only replacement membership are preserved. Narrative
    provenance errors were independently confirmed and filed as issues 1535 and 1536;
    they do not change these dispositions.
  snapshot_sha256: a309fe8b6a841afea0d0b4463a205fe322a2722fced2797930bd0cbfe815791b
- evidence_id: successor-two-field-diff
  kind: record_content
  reference: reports/culturemech_second_provenance_followup_20261117/second-219-284-v2.json
  accessed_at: '2026-11-17T01:37:34Z'
  support: supports
  summary: Exact pinned successor equals the original document with only the two independently
    inspected narrative corrections. The corrected digest matches its inspected member;
    the hydrate explanation correctly distinguishes source wording from the selected
    anhydrous owner.
  snapshot_sha256: b846c03927bd2d0e5e09bbb4b6911295761c4e11f743c1e223d67bd5eac731ef
assessments:
- assessment_id: second-219-284
  area: identity
  topic: Bounded independent source-binding cross-review
  outcome: supported
  summary: 'Independently read all 143 decision reasons. Read complete owner266 plus
    its two descriptors and exact local canonical row; approval correctly excludes
    the external parent CHEBI:15978. Read complete owner268 history plus full Pinchuk
    old-side REPLACE case 1d009355 (zero positive occurrences) and its separate monobasic-conflict
    witness 013d738a. Read complete owner281 and exact ammonium-salt versus anion
    witness 81424774. Read complete owner270 and hydrate witness c51054. The selected
    identity boundaries and context-only replacement membership are preserved. Narrative
    provenance errors were independently confirmed and filed as issues 1535 and 1536;
    they do not change these dispositions. Successor independently checked: both minor
    narrative findings corrected with no scientific decision changes.'
  target_ids:
  - second-219-284
  evidence_ids:
  - second-219-284
  - successor-two-field-diff
findings:
- finding_id: chlorate-locator
  issue_key: culturemech-intake-second-chlorate-locator-1535
  category: provenance
  severity: minor
  status: resolved
  certainty: confirmed
  title: Incorrect narrative descriptor digest
  ownership_note: Owned by the second-slice review author; correct only a successor
    decision snapshot, not source ingredients or canonical rows.
  description: Case b198a7c5e3164e5112e16cb10007008ceb321feeff7a7c4bc2f2dcad109d6e3d
    evidence_locators[0] contains an extra 4c in descriptor digest d300b6526d61bfef904b8c9ca20b96a7c020a0bb686b85b9f007dc74079a07f8.
    The author disclosed this before this reviewer independently verified it. The
    machine-readable inspected hash and complete case pin are correct.
  target_ids:
  - second-219-284
  evidence_ids:
  - second-219-284
  - successor-two-field-diff
  field_paths:
  - decisions[case_id=b198a7c5e3164e5112e16cb10007008ceb321feeff7a7c4bc2f2dcad109d6e3d].evidence_locators[0]
  external_issues:
  - https://github.com/CultureBotAI/MediaIngredientMech/issues/1535
  previous_occurrences:
  - repository: CultureBotAI/MediaIngredientMech
    review_id: 20261117T013626Z-culturemech-intake-second-cross-review
    finding_id: chlorate-locator
  disposition_reason: The exact successor changes only the documented narrative error.
    Original targets and evidence remain retained; scientific identity judgments and
    machine payload pins are unchanged.
- finding_id: sulfide-witness-wording
  issue_key: culturemech-intake-second-sulfide-witness-1536
  category: provenance
  severity: minor
  status: resolved
  certainty: confirmed
  title: Witness explanation asserts absent embedded fields
  ownership_note: Owned by the second-slice review author; correct only a successor
    decision snapshot, not source ingredients or canonical rows.
  description: Case d0c8d3c8ab968b81703d7291e78c7bbb018c735fd3e2cd11b342b18b11d1be20
    witness c51054cca36e6a38a39f35805ff8a40060d922a22aa5f7b78988ff6d6906217c has no
    term or mediaingredientmech_chebi_term. Its explanation incorrectly says those
    fields assert anhydrous CHEBI76208. The selected candidate/owner, rather than
    this descriptor, is anhydrous. Literal sodium sulfide hydrate evidence still justifies
    WITHHOLD against that owner.
  target_ids:
  - second-219-284
  evidence_ids:
  - second-219-284
  - successor-two-field-diff
  field_paths:
  - decisions[case_id=d0c8d3c8ab968b81703d7291e78c7bbb018c735fd3e2cd11b342b18b11d1be20].blocking_witnesses[0].reason
  external_issues:
  - https://github.com/CultureBotAI/MediaIngredientMech/issues/1536
  previous_occurrences:
  - repository: CultureBotAI/MediaIngredientMech
    review_id: 20261117T013626Z-culturemech-intake-second-cross-review
    finding_id: sulfide-witness-wording
  disposition_reason: The exact successor changes only the documented narrative error.
    Original targets and evidence remain retained; scientific identity judgments and
    machine payload pins are unchanged.
actions: []
limitations:
- Not an independent double-review of every scientific payload, source coordinate
  or original publication. Exact sample sizes and witnesses are declared per target.
- The sampled packet claims and maintained owners were reread; underlying primary
  publications were not re-retrieved during this second-pass cross-review. Quantity,
  growth, release adoption and global canonical publication are outside its scope.
- Native finalization, exact product replay, complete author-case coverage and final
  PR review remain required. Timestamps record consolidation of the preceding read-only
  inspection.
links:
- https://github.com/CultureBotAI/MediaIngredientMech/issues/1453
- https://github.com/CultureBotAI/MediaIngredientMech/pull/1460
related_reviews:
- repository: CultureBotAI/MediaIngredientMech
  review_id: 20261117T013626Z-culturemech-intake-second-cross-review
  relationship: Resolves both minor provenance findings after exact independent two-field
    successor inspection; retains all prior targets and scope limits.
```
