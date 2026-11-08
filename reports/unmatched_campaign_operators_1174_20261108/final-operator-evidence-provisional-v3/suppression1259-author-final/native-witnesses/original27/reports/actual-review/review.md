# PRIVATE MECHANICAL FIXTURE: no scientific or application approval

- Review: 20261108T124921Z-mechanical-fixture-transition-review
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-11-08T12:45:53.394300Z
- Finished UTC: 2026-11-08T12:49:21.879184Z
- Reviewer: fixture-distinct-reviewer (independent)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: false

## Summary

Mechanical fixture validates the closed review-consumption boundary only.

## Scope And Provenance

Mechanical fixture four-event transition input coverage

Selection: Frozen09fe42ca four-pair bindings with15exactYAMLcaptures,7beforeimages/8proposals; all4emitters in934conditionaloperations.
Coverage: full; 4 reviewed / 4 in the declared population.
Source: working_tree at Git base 714d3fc00073052f934e1106562f90681032c5d2.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| W07-SUPPRESSION-01 | reports/transition.json # subject=MIM:Bacto_Peptone; token_key=peptone | snapshot_row | MIM:Bacto_Peptone / Peptone |
| W07-SUPPRESSION-02 | reports/transition.json # subject=MIM:Glebomycin; token_key=bluensomycin | snapshot_row | MIM:Glebomycin / Bluensomycin |
| W07-SUPPRESSION-03 | reports/transition.json # subject=MIM:Netropsin; token_key=congocidin | snapshot_row | MIM:Netropsin / Congocidin |
| W07-SUPPRESSION-04 | reports/transition.json # subject=MIM:Starch; token_key=corn starch | snapshot_row | MIM:Starch / Corn Starch |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Fixture tuple equality | passed | True | W07-SUPPRESSION-01, W07-SUPPRESSION-02, W07-SUPPRESSION-03, W07-SUPPRESSION-04 | Synthetic mechanical fixture only |

## Scientific And Domain Assessments

### Exact mechanical transition binding

provenance: supported. Targets: W07-SUPPRESSION-01.

Fixture-only complete transition equality

### Exact mechanical transition binding

provenance: supported. Targets: W07-SUPPRESSION-02.

Fixture-only complete transition equality

### Exact mechanical transition binding

provenance: supported. Targets: W07-SUPPRESSION-03.

Fixture-only complete transition equality

### Exact mechanical transition binding

provenance: supported. Targets: W07-SUPPRESSION-04.

Fixture-only complete transition equality

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| TRANSITION | reports/transition.json | supports | Exact synthetic mechanical fixture transition; original science remains separately bound. |

## Limits And Additional Notes

- Synthetic fixture only, not real scientific authorization.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261108T124921Z-mechanical-fixture-transition-review
kind: batch
repository: CultureBotAI/MediaIngredientMech
title: 'PRIVATE MECHANICAL FIXTURE: no scientific or application approval'
started_at: '2026-11-08T12:45:53.394300Z'
finished_at: '2026-11-08T12:49:21.879184Z'
reviewer:
  identity: fixture-distinct-reviewer
  kind: agent
  independence: independent
  independence_basis: Synthetic assigned reviewer role for a test; no real scientific
    decision is manufactured.
skill: review-sssom-output
completion: completed
verdict: pass_with_limitations
native_verdict: Private structural test fixture; no approval
scientific_review: false
summary: Mechanical fixture validates the closed review-consumption boundary only.
source:
  git_revision: 714d3fc00073052f934e1106562f90681032c5d2
  state: working_tree
  inputs:
  - path: reports/transition.json
    sha256: 1974723c24e14c9f1f3bf06a0a656d7d21e2b929a6cc620173dec0edd292c5fe
    role: target
  - path: intake/plan.json
    sha256: d970ffa53517d80adfbe75d24fd551aca90094cb79e8a97e2825d95b9def76cf
    role: context
  - path: source-receipt/application.json
    sha256: 5752df26bc2af3246527b56a36a73eee150cf56fe277027610c666e656af023c
    role: context
  - path: reports/science/review.yaml
    sha256: 99bef708606134cf404608f52e4fa61696fb67412122a27ade5c789d345c1f71
    role: context
  - path: reports/science/review-inputs/conditional-decisions.json
    sha256: 26c5f381bcf3600f18c54722213c076389d0d17d732bbf760783e1cfdc4d333c
    role: context
  - path: reports/generated/candidate.tsv
    sha256: 3a6c3c4084756e6733418a75bc0cdc13f16fe9e2e76cde6f7506f73cddd67fcb
    role: context
  - path: reports/generated/sidecar.tsv
    sha256: e258ba2332b06c2dc616feb68afc9cff474759bb72a848179f00eb58b3240a6b
    role: context
  - path: reports/generated/manifest.json
    sha256: 0d5be3d672ee840e9b3ef7a072e700d6d4a3f3018e90abfa9611cf572cfcbead
    role: context
targets:
- target_id: W07-SUPPRESSION-01
  path: reports/transition.json
  kind: snapshot_row
  label: MIM:Bacto_Peptone / Peptone
  selector: subject=MIM:Bacto_Peptone; token_key=peptone
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Bacto_Peptone.yaml
    role: authentic_emitter_or_credited_owner
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Peptone.yaml
    role: authentic_emitter_or_credited_owner
  ownership_note: Read-only frozen whole-owner pair assessment. Source workers own
    source changes; root owns future capability/application. No owner edit or scientific/release
    approval.
- target_id: W07-SUPPRESSION-02
  path: reports/transition.json
  kind: snapshot_row
  label: MIM:Glebomycin / Bluensomycin
  selector: subject=MIM:Glebomycin; token_key=bluensomycin
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Glebomycin.yaml
    role: authentic_emitter_or_credited_owner
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Bluensomycin.yaml
    role: authentic_emitter_or_credited_owner
  ownership_note: Read-only frozen whole-owner pair assessment. Source workers own
    source changes; root owns future capability/application. No owner edit or scientific/release
    approval.
- target_id: W07-SUPPRESSION-03
  path: reports/transition.json
  kind: snapshot_row
  label: MIM:Netropsin / Congocidin
  selector: subject=MIM:Netropsin; token_key=congocidin
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Netropsin.yaml
    role: authentic_emitter_or_credited_owner
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Congocidin.yaml
    role: authentic_emitter_or_credited_owner
  ownership_note: Read-only frozen whole-owner pair assessment. Source workers own
    source changes; root owns future capability/application. No owner edit or scientific/release
    approval.
- target_id: W07-SUPPRESSION-04
  path: reports/transition.json
  kind: snapshot_row
  label: MIM:Starch / Corn Starch
  selector: subject=MIM:Starch; token_key=corn starch
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Starch.yaml
    role: authentic_emitter_or_credited_owner
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Corn_Starch.yaml
    role: authentic_emitter_or_credited_owner
  ownership_note: Read-only frozen whole-owner pair assessment. Source workers own
    source changes; root owns future capability/application. No owner edit or scientific/release
    approval.
scope:
  description: Mechanical fixture four-event transition input coverage
  selection: Frozen09fe42ca four-pair bindings with15exactYAMLcaptures,7beforeimages/8proposals;
    all4emitters in934conditionaloperations.
  coverage: full
  population_size: 4
  reviewed_target_ids:
  - W07-SUPPRESSION-01
  - W07-SUPPRESSION-02
  - W07-SUPPRESSION-03
  - W07-SUPPRESSION-04
  exclusions:
  - target: Other17native candidate events, all other aliases/owners and whole campaign
      application or export
    reason: Outside four selected obligations; no broad token or owner approval transfers.
  - target: Source-case acceptance, supplied-form completion, role and mapping-row
      admission
    reason: Retained separate scientific/approval decisions; current name evidence
      does not resolve these holds.
checks:
- check_id: mechanical
  name: Fixture tuple equality
  status: passed
  required: true
  target_ids:
  - W07-SUPPRESSION-01
  - W07-SUPPRESSION-02
  - W07-SUPPRESSION-03
  - W07-SUPPRESSION-04
  evidence_ids:
  - TRANSITION
  summary: Synthetic mechanical fixture only
evidence:
- evidence_id: TRANSITION
  kind: record_content
  reference: reports/transition.json
  snapshot_sha256: 1974723c24e14c9f1f3bf06a0a656d7d21e2b929a6cc620173dec0edd292c5fe
  support: supports
  accessed_at: '2026-11-08T12:49:21Z'
  summary: Exact synthetic mechanical fixture transition; original science remains
    separately bound.
assessments:
- assessment_id: W07-SUPPRESSION-01-transport
  area: provenance
  topic: Exact mechanical transition binding
  outcome: supported
  target_ids:
  - W07-SUPPRESSION-01
  evidence_ids:
  - TRANSITION
  summary: Fixture-only complete transition equality
- assessment_id: W07-SUPPRESSION-02-transport
  area: provenance
  topic: Exact mechanical transition binding
  outcome: supported
  target_ids:
  - W07-SUPPRESSION-02
  evidence_ids:
  - TRANSITION
  summary: Fixture-only complete transition equality
- assessment_id: W07-SUPPRESSION-03-transport
  area: provenance
  topic: Exact mechanical transition binding
  outcome: supported
  target_ids:
  - W07-SUPPRESSION-03
  evidence_ids:
  - TRANSITION
  summary: Fixture-only complete transition equality
- assessment_id: W07-SUPPRESSION-04-transport
  area: provenance
  topic: Exact mechanical transition binding
  outcome: supported
  target_ids:
  - W07-SUPPRESSION-04
  evidence_ids:
  - TRANSITION
  summary: Fixture-only complete transition equality
findings: []
actions: []
limitations:
- Synthetic fixture only, not real scientific authorization.
notes: []
```
