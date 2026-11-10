# MediaIngredientMech infrastructure tasks

This versioned ledger collects repository requirements and upgrades discovered
during every goal. The workflow profile and its parent govern intake, stage 6
implementation, closure and cycle restart.

## Intake protocol

- Give each actionable task a stable ID such as `mediaingredientmech-infra-0001` and retain it
  across cycles. Record the originating run, cycle and goal, observation,
  desired outcome, evidence paths, priority, dependencies and status.
- Link each task to an actual issue in https://github.com/CultureBotAI/MediaIngredientMech/issues.
  Search existing open and closed issues before creating one. If access fails,
  retain an explicit pending-link blocker; never invent an issue number or URL.
- Preserve resolved and deferred entries with their issue, implementation PR,
  validation and disposition. Do not overwrite previous cycle evidence.
- At stage 6, freeze a bounded snapshot, write a dependency-aware plan and
  acceptance criteria, implement selected work, validate, and complete the
  commit sequence, write the closure receipt and stop; only the supervisor
  dispatches another goal. New arrivals after the cutoff enter the next cycle;
  never expand the frozen task-ID scope. A new blocking prerequisite requires
  an explicit deferred disposition for the selected task. Carry unfinished work
  forward explicitly.

## Machine-readable task inventory

This fenced mapping is the inventory stage 6 freezes and reconciles. Each task
uses `task_id`, `summary`, `status` (`note`, `open`, `deferred`, or `resolved`),
optional `issue_url`, and optional `disposition`. Status `note` may have a
pending issue link; all other statuses require a real issue URL. Keep richer
notes below keyed by the same stable task ID.

<!-- mech-infra-tasks:start -->
```yaml
schema_version: '1.0.0'
tasks:
  - task_id: mediaingredientmech-infra-1300
    summary: Explicit stable-ID splits and deprecation without a successor
    status: open
    issue_url: https://github.com/CultureBotAI/MediaIngredientMech/issues/1300
    disposition: Implemented on the PR1279 dependency; focused checks pass, independent review and full checks pending. No data or registry changes.
```
<!-- mech-infra-tasks:end -->

## Tasks

### mediaingredientmech-infra-1300

Origin: resumed all-unmatched campaign, 2026-11-10 user requirement for persistent
identity lifecycle. Priority: prerequisite to the next reviewed release.
Dependency: #1265 / PR #1279, exact implementation base
`890e46360779ffad9895896fc280cc846f97c55f`.

The existing lifecycle supports one registered replacement per retired/merged
ID. #1300 adds explicit one-to-many splits and deprecation with no successor,
without another allocator, re-minting, arbitrary child selection or transfer of
scientific equivalence. Preserve all existing IDs and ledgers. Source-identity
publication and campaign migration are separate work.

Evidence/design: `.temp/all-unmatched-20261107/preflight/stable-id-model-audit-20261110-v1/`
in the campaign coordinator; maintained contract and test coverage are in
`docs/STABLE_MIM_IDS.md` and `tests/test_stable_id_lifecycle.py`.
Focused validation: 221 distinct passing cases and one unchanged corpus-dependent
skip (every current SSSOM subject has an exactMatch); the new synthetic test
explicitly checks that a broadMatch-only current owner has no equivalent term.
The current 2,956-record trusted-base identity/history gate, focused Ruff/Black,
two-module mypy and diff checks pass. Exact commands/output are retained in the
owned worktree's `.temp/lifecycle1300-checks/`. These focused runs explicitly
disable coverage; full-suite coverage/required gates are unchanged and remain
pending with distinct review. No actual lifecycle or source operation ran.
