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
  - task_id: mediaingredientmech-infra-1325
    summary: Separate ordinary current reviewed exports from immutable historical projection replay
    status: open
    issue_url: https://github.com/CultureBotAI/MediaIngredientMech/issues/1325
    disposition: Explicit native routing in an isolated code branch; actual endpoint review selection, historical root pin and independent final review remain pending.
  - task_id: mediaingredientmech-infra-1303
    summary: Reviewed native adoption of permanent IDs into the existing campaign
    status: open
    issue_url: https://github.com/CultureBotAI/MediaIngredientMech/issues/1303
    disposition: Isolated operator implementation; actual eligibility decisions, data adoption, validation and independent release review remain pending.
  - task_id: mediaingredientmech-infra-1299
    summary: Reviewed stable-MIM source identities and MIM-only candidate exports
    status: open
    issue_url: https://github.com/CultureBotAI/MediaIngredientMech/issues/1299
    disposition: Isolated implementation depending on permanent IDs in PR 1279; final independent review and release remain pending.
```
<!-- mech-infra-tasks:end -->

## Tasks

### mediaingredientmech-infra-1325

Origin: the #1303 campaign adoption prerequisite. The original projection proves
only the immutable administrative migration, while new ordinary endpoint reviews
must cover current science independently. The routing gate keeps the projected
default, replays the original native checker against a separately pinned Git root
for ordinary reviews, and verifies complete current mapping and companion inputs.
See `docs/CURRENT_REVIEWED_EXPORTS.md` and `tests/test_reviewed_export_route.py`.
No campaign reviews, data, IDs, historical proof scope, QC pin or production
permission change. Future selector changes require actual reviewed artifacts.

### mediaingredientmech-infra-1303

Origin: the user's stable-ID priority for the existing unmatched-chemicals
campaign; no new cycle or goal is asserted. The completed legacy construction
requires an administrative bridge to the permanent-ID registry before a fresh
source-identity candidate can be reviewed. Dependencies: #1265 / PR #1279,
the separate reviewed source export #1299 and the exact original native
plan/application/case/origin evidence. Evidence: `docs/STABLE_ID_ADOPTION.md`,
`tests/test_stable_id_adoption.py` and the preserved implementation packet under
`.temp/all-unmatched-20261107/`. The operator uses native allocation, schema
serialization, synchronization, Claw dry-run and lease, and guarded filesystem
primitives. It preserves original full source accounting and requires authored
current concept eligibility; all actual data adoption remains pending.
The independent filesystem finding is tracked in #1314; preparation/receipt
traversal refusal is tracked in #1315. Literal original eligibility/hold evidence
and nullable residual-classification review conclusions are tracked in #1317. Original failures and review evidence
remain preserved. No source, mapping or role approval transfers through this
administrative operation, and the historical identity-projection cohort stays
unchanged.

### mediaingredientmech-infra-1299

The authorized unmatched-chemicals campaign exposed a gap between permanent
record addresses and reviewed source identity. Origin: the user's stable-ID
priority on 2026-11-10; no new cycle is asserted. Priority: blocking the new
candidate consumer workflow. Dependencies: #1265 / PR #1279 and independently
reviewed source evidence. Evidence: `MAPPING_SEMANTICS.md`,
`docs/SOURCE_IDENTITY_CANDIDATES.md`, `tests/test_source_bindings.py` and
[issue #1299](https://github.com/CultureBotAI/MediaIngredientMech/issues/1299).
The separate exporter preserves full source/occurrence accounting and existing
external dispositions without granting canonical publication or KG rebuild.
Campaign data adoption remains pending separately in
[issue #1303](https://github.com/CultureBotAI/MediaIngredientMech/issues/1303):
reuse authenticated existing IDs and review distinct-concept eligibility before
minting any new ID. This code task does not migrate the legacy campaign or
extend the historical identity-projection proof.
The executing/selected-producer mismatch found during review is tracked in
[issue #1305](https://github.com/CultureBotAI/MediaIngredientMech/issues/1305).
Its fix binds privately compiled source bytes, dependency declarations and honest
Git/runtime context, including the cached-dependency failure from #1195. Final
independent review remains pending; no campaign or KG acceptance is implied.
The additive semantics documentation also requires the narrow native successor
refresh tracked in [issue #1304](https://github.com/CultureBotAI/MediaIngredientMech/issues/1304):
only the mapping-review semantics input and the two dependent companion-review
pins change. Native `identity_projection --replace-derived` and `--check`
preserve all scientific decisions, historical authorities and the fixed cohort;
no graph regeneration is required by these changes.
Final-head follow-ups are tracked in
[issue #1308](https://github.com/CultureBotAI/MediaIngredientMech/issues/1308),
[issue #1309](https://github.com/CultureBotAI/MediaIngredientMech/issues/1309) and
[issue #1310](https://github.com/CultureBotAI/MediaIngredientMech/issues/1310):
required checks must pass for the applicable target, captures have an explicit
typed runtime contract, and complete expanded source URIs must be unique.
These admission repairs transfer no scientific approval and preserve all prior
holds and original source rows.


Operational-fit follow-up [#1321](https://github.com/CultureBotAI/MediaIngredientMech/issues/1321)
requires explicit immutable duration/age/margin/overhead policy, complete native
recovery-guard profiling, independent namespace and resource-scheduling acceptance,
and a fresh pre-lease fit refusal. The original full currentness guards remain;
lease identity, unchanged aware deadline and monotonic budget are checked after
expensive scans. No real campaign operational policy or adoption is authorized
by this implementation. Multi-hour fits can remain blocked pending scheduling.
