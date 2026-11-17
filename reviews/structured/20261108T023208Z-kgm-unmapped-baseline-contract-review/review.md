# Independent baseline export contract and retained-history audit

- Review: 20261108T023208Z-kgm-unmapped-baseline-contract-review
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-11-08T02:30:58.231634Z
- Finished UTC: 2026-11-08T02:32:08.626040Z
- Reviewer: /root/step7d_independent_review (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: false

## Summary

Current reviewed products reproduce exactly and already match the KG-Microbe selected immutable release. No stale MIM export alone explains the chemical queue. Existing typed successors cannot accept current retained owned-name history; issue1150 records that bounded defect. No proposed alias or new scientific approval is assessed here.

## Scope And Provenance

Bounded baseline export, receipt and companion contract audit, including one independently reproduced successor-schema defect.

Selection: Eight exact baseline contract/provenance targets; complete native outputs were reproduced in isolated reviewer directories.
Coverage: full; 8 reviewed / 8 in the declared population.
Source: working_tree at Git base 0dac278466699129a083343a921c2e0ca18a9ab4.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| typed-refresh | src/mediaingredientmech/ingredient_bundle_refresh.py | source | Existing three typed successor contexts |
| policy-history | mappings/ingredient_mappings.sssom.tsv.manifest.json | source | Current legitimate policy history |
| canonical | mappings/ingredient_mappings.sssom.tsv | source | Baseline canonical mapping rows |
| mapping-review | reports/sssom_completion_20260921/review.json | source | Content-bound mapping dispositions |
| companion | reports/owned_name_deferred_669_20261103/companion-review.json | source | Separate scoped companion review |
| unified | UNIFIED_INGREDIENT_MAPPING.tsv | source | Baseline unified snapshot |
| unified-provenance | UNIFIED_INGREDIENT_MAPPING.provenance.json | source | Native MIM input provenance |
| history-probe | reports/kgm_unmapped_chemicals_20261107/baseline-independent/typed-history-proof-v1.json | source | Independent read-only compatibility reproduction |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| export | passed | True | canonical, mapping-review, companion | Actual native command completed; original receipt and log retained. |
| replay | passed | True | canonical, mapping-review, companion | Actual native command completed; original receipt and log retained. |
| companion-export | passed | True | canonical, mapping-review, companion | Actual native command completed; original receipt and log retained. |

## Scientific And Domain Assessments

### Existing three typed successor contexts

consistency: concern. Targets: typed-refresh.

The older form, registry and stock contexts exclude the current owned_name_suppression_updates key, so they cannot consume current retained history. Their narrow contracts also do not authorize arbitrary alias additions.

### Current legitimate policy history

consistency: supported. Targets: policy-history.

Current owned-name history is legitimate immutable prior attribution. Preserve it; the compatibility defect is in the older consumer shape check, not a reason to erase history.

### Baseline canonical mapping rows

consistency: supported. Targets: canonical.

Baseline canonical has 3014 rows; native export yields 1739 supported and 1275 withheld. Actual supported predicates are 1737 exact and two broader. Its content equals the source already selected by KGM.

### Content-bound mapping dispositions

consistency: supported. Targets: mapping-review.

Native replay validates all 26 receipt links and content-bound decisions. A changed owner or row cannot inherit support; new curation needs explicit receipt and mapping-specific review.

### Separate scoped companion review

consistency: supported. Targets: companion.

Native scoped export passes with 20 owners and 51 claims: 20 mappings,18 identifiers,10 occurrences,3 products;50 supported and one withheld. It is separate from the KGM supported/unified pair.

### Baseline unified snapshot

consistency: supported. Targets: unified.

Snapshot hash and all 2956 MIM record inputs match the native provenance;4170 snapshot rows. This does not assert current CultureMech/provider freshness.

### Native MIM input provenance

consistency: supported. Targets: unified-provenance.

Native MIM input digest is exact at this baseline. A later record edit creates real drift; stamping old output does not rebuild it.

### Independent read-only compatibility reproduction

consistency: supported. Targets: history-probe.

Read-only native API probes reproduce the schema refusal in all three contexts. The in-memory key-removal control is diagnostic only, not a proposed fix or accepted successor.

## Findings

### typed-successor-rejects-owned-name-history: Older typed refresh contexts reject legitimate owned-name history

minor / open / confirmed; issue key: mim-typed-successor-owned-name-history.

Current canonical manifest contains owned_name_suppression_updates, but the shared form/registry/stock shape check excludes it. All three native paths refuse before validating a successor. Preserve existing history and scientific constraints; do not remove the key to pass.

## Recommended Actions And Acceptance Checks

### preserve-unrelated-owned-name-history

When the older typed path is needed, admit the existing owned-name update history only as immutable unrelated provenance while retaining each context's exact transition and scientific constraints. Do not erase or repurpose history.

- Valid typed successors preserve every prior owned-name history entry exactly.
- Deleting, altering or reordering the unrelated history is rejected.
- All existing native receipt, owner, sidecar, selected-claim and approval restrictions remain enforced.
- A true alias addition uses its own bounded contract and is not relabeled hydrate_parent_predicate.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| native-code | src/mediaingredientmech/ingredient_bundle_refresh.py | supports | Read the exact allowed manifest keys and separate scientific contracts for the three older typed contexts. |
| current-history | mappings/ingredient_mappings.sssom.tsv.manifest.json | supports | Read current owned-name suppression history retained by the completed publication. |
| probe | reports/kgm_unmapped_chemicals_20261107/baseline-independent/typed-history-proof-v1.json | supports | All three actual-history probes refuse unknown manifest shape; private diagnostic controls reach the next guard. No maintained mutation. |
| audit | reports/kgm_unmapped_chemicals_20261107/baseline-independent/baseline-contract-audit-v1.json | supports | Exact current-baseline receipt replay, four-file export equality with the consumed KGM source, installed pair hashes and native MIM snapshot digest. |
| export | reports/kgm_unmapped_chemicals_20261107/baseline-independent/baseline-reviewed-export-v1.json | supports | Native isolated reviewed export completed with exit zero. |
| replay | reports/kgm_unmapped_chemicals_20261107/baseline-independent/baseline-reviewed-replay-v1.json | supports | Native validate-only independent product replay completed with exit zero. |
| companion-export | reports/kgm_unmapped_chemicals_20261107/baseline-independent/baseline-companion-export-v1.json | supports | Native scoped companion export completed with exit zero. |
| semantics | MAPPING_SEMANTICS.md | supports | Identity/form boundaries and export-only owned-name policy remain authoritative. |

## Limits And Additional Notes

- Truthful isolated overlay has actual durable HEAD0dac2784. Baseline tracked bytes were read from that commit; newly copied diagnostic proofs are separately captured working-tree inputs. The later author worktree is not represented as unchanged.
- No fresh scientific approval of sodium acetate aliases, roles, formulae or source occurrences is conferred.
- MIM-supported phosphatidylcholine remains separately downstream-held by KGM1799; the old native mapping approval does not clear that consumer hold.
- Native MIM snapshot freshness proves its own record digest, not all current CultureMech/provider inputs.
- Full QC/current-main checks and final changed-head review remain separate root-owned work. No result of a still-running or uninspected check is inferred.
- Probe controls deliberately remove a key only in memory to locate the guard. They do not constitute a valid successor or authorize changing historical files.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261108T023208Z-kgm-unmapped-baseline-contract-review
kind: repository
repository: CultureBotAI/MediaIngredientMech
title: Independent baseline export contract and retained-history audit
started_at: '2026-11-08T02:30:58.231634Z'
finished_at: '2026-11-08T02:32:08.626040Z'
reviewer:
  identity: /root/step7d_independent_review
  kind: agent
  model: gpt-6
  independence: independent
  independence_basis: Reviewer did not author current curation or successor code;
    independently read baseline inputs, ran native isolated exports/replay, and reproduced
    the typed-history refusal.
skill: review-sssom-output
completion: completed
verdict: needs_curation
native_verdict: Baseline exports pass; one fail-closed typed successor compatibility
  finding remains open.
scientific_review: false
summary: Current reviewed products reproduce exactly and already match the KG-Microbe
  selected immutable release. No stale MIM export alone explains the chemical queue.
  Existing typed successors cannot accept current retained owned-name history; issue1150
  records that bounded defect. No proposed alias or new scientific approval is assessed
  here.
source:
  git_revision: 0dac278466699129a083343a921c2e0ca18a9ab4
  state: working_tree
  inputs:
  - path: .claude/skills/review-sssom-output/SKILL.md
    sha256: 2e05b30eefce620fbb78196386e476c330b81e36738f2461b4be64391a61ecd5
    role: context
  - path: AGENTS.md
    sha256: fc7728986d82b43359a9055ae233bcf0d4ebaef8bb657ef1b4bb4aa87b2cbaaf
    role: context
  - path: MAPPING_SEMANTICS.md
    sha256: 6b52f2ac48109ddd5d81996a136b19776cab55efa69a5ec832cf716d6885a062
    role: context
  - path: UNIFIED_INGREDIENT_MAPPING.provenance.json
    sha256: 075fcc6ef6eca25c1e63d65889df37d4893be2b1b9d3630df90704012dc2c831
    role: target
  - path: UNIFIED_INGREDIENT_MAPPING.tsv
    sha256: f6a8eb844e578d79da9538abf99c244fc25b2c928c50c64c0477b1218092a0f1
    role: target
  - path: docs/record-review-profile.md
    sha256: da17e2048a13514a422bc94bd2f8d48943cffc5689b96e3f07da26423248d1a7
    role: context
  - path: docs/record-reviews.md
    sha256: 452a19ab688276747b7c4308523a14d4d99c1c39ef6909ae8a90b85b7a9b3e9b
    role: context
  - path: mappings/ingredient_mappings.sssom.tsv
    sha256: d5f76fc404967477903fafc79eaba86ecfef9e2c391926ec08c3c1af4a5220b6
    role: target
  - path: mappings/ingredient_mappings.sssom.tsv.manifest.json
    sha256: 6b6fe48246bd43dd70499e82f508a7b7ea0fcd121bccafafa0217aae84a17778
    role: target
  - path: reports/kgm_unmapped_chemicals_20261107/baseline-independent/baseline-companion-export-v1.json
    sha256: df3f64db4b5b226bfd92b068b78be6e574e95f15f1e49053784bd3d7080168a9
    role: context
  - path: reports/kgm_unmapped_chemicals_20261107/baseline-independent/baseline-companion-export-v1.log
    sha256: 61dc25102e26d7e3594995debc43efb8808b2abe6c07c74d3bd73a42c521e9a3
    role: context
  - path: reports/kgm_unmapped_chemicals_20261107/baseline-independent/baseline-contract-audit-v1.json
    sha256: dc1ac887c54ae13d00800b8941c281c88d5ac08015ec424ad002ab7a3e5f7ac6
    role: context
  - path: reports/kgm_unmapped_chemicals_20261107/baseline-independent/baseline-reviewed-export-v1.json
    sha256: 6b78fc7c577e817f45b64b979d683353698a5e27fd581044785a8a79f02b18dc
    role: context
  - path: reports/kgm_unmapped_chemicals_20261107/baseline-independent/baseline-reviewed-export-v1.log
    sha256: b02a92446e8a613fd0d96b0dd8147d439733fcf73e731b363a6388e95d616703
    role: context
  - path: reports/kgm_unmapped_chemicals_20261107/baseline-independent/baseline-reviewed-replay-v1.json
    sha256: 88b36a24931d83064044e7d3809da9342e42e805a094b4461b7194e67dbd0357
    role: context
  - path: reports/kgm_unmapped_chemicals_20261107/baseline-independent/baseline-reviewed-replay-v1.log
    sha256: b02a92446e8a613fd0d96b0dd8147d439733fcf73e731b363a6388e95d616703
    role: context
  - path: reports/kgm_unmapped_chemicals_20261107/baseline-independent/probe_typed_history_v1.py
    sha256: 8de5e6e685e6bc8b4e14563709b3b6b8dbc86872ee8826fa7130a65bd77a5549
    role: context
  - path: reports/kgm_unmapped_chemicals_20261107/baseline-independent/typed-history-issue-body-v1.md
    sha256: d5d4d4e4360fc750e2bef7728fbf7cbaaa524495b46e84e0949b5557b5ca97a0
    role: context
  - path: reports/kgm_unmapped_chemicals_20261107/baseline-independent/typed-history-proof-v1.json
    sha256: 081f877937478210cff1b8b54353471d6dcbef17900f88c55f858aebc9a05de4
    role: target
  - path: reports/owned_name_deferred_669_20261103/companion-review.json
    sha256: ba15d43306f33972d7abcd67185e5bf571f2224f00e757c2603e017a895ac815
    role: target
  - path: reports/sssom_completion_20260921/review.json
    sha256: ab301d1f66276cdfeefea79080ce49f26ebb02c1920a53c71512c14b283b16cf
    role: target
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/record_review.py
    sha256: 95a4ec41e38ec47ba3578e76838c46a0adbf47e49ad3636524735d08cfcb1c4d
    role: context
  - path: src/mediaingredientmech/ingredient_bundle_refresh.py
    sha256: cd85ce90c88bb69b05d618492af6bdc7d27adfa12ca1a5c753bb223207ff4f32
    role: target
scope:
  description: Bounded baseline export, receipt and companion contract audit, including
    one independently reproduced successor-schema defect.
  selection: Eight exact baseline contract/provenance targets; complete native outputs
    were reproduced in isolated reviewer directories.
  coverage: full
  population_size: 8
  reviewed_target_ids:
  - typed-refresh
  - policy-history
  - canonical
  - mapping-review
  - companion
  - unified
  - unified-provenance
  - history-probe
  exclusions:
  - target: Proposed sodium acetate alias and later edits
    reason: Those source bytes and scientific evidence require a separate final review.
  - target: KG-Microbe production/archive admission and new downstream adoption
    reason: Read-only upstream context; no rebuild or adoption authorized here.
  - target: Whole-corpus scientific release
    reason: Structural/provenance checks preserve existing holds and do not approve
      roles or withheld mappings.
targets:
- target_id: typed-refresh
  path: src/mediaingredientmech/ingredient_bundle_refresh.py
  label: Existing three typed successor contexts
  kind: source
  ownership_note: Baseline provenance or maintained contract; this audit changes no
    scientific record or approval.
- target_id: policy-history
  path: mappings/ingredient_mappings.sssom.tsv.manifest.json
  label: Current legitimate policy history
  kind: source
  ownership_note: Baseline provenance or maintained contract; this audit changes no
    scientific record or approval.
- target_id: canonical
  path: mappings/ingredient_mappings.sssom.tsv
  label: Baseline canonical mapping rows
  kind: source
  ownership_note: Baseline provenance or maintained contract; this audit changes no
    scientific record or approval.
- target_id: mapping-review
  path: reports/sssom_completion_20260921/review.json
  label: Content-bound mapping dispositions
  kind: source
  ownership_note: Baseline provenance or maintained contract; this audit changes no
    scientific record or approval.
- target_id: companion
  path: reports/owned_name_deferred_669_20261103/companion-review.json
  label: Separate scoped companion review
  kind: source
  ownership_note: Baseline provenance or maintained contract; this audit changes no
    scientific record or approval.
- target_id: unified
  path: UNIFIED_INGREDIENT_MAPPING.tsv
  label: Baseline unified snapshot
  kind: source
  ownership_note: Baseline provenance or maintained contract; this audit changes no
    scientific record or approval.
- target_id: unified-provenance
  path: UNIFIED_INGREDIENT_MAPPING.provenance.json
  label: Native MIM input provenance
  kind: source
  ownership_note: Baseline provenance or maintained contract; this audit changes no
    scientific record or approval.
- target_id: history-probe
  path: reports/kgm_unmapped_chemicals_20261107/baseline-independent/typed-history-proof-v1.json
  label: Independent read-only compatibility reproduction
  kind: source
  ownership_note: Baseline provenance or maintained contract; this audit changes no
    scientific record or approval.
evidence:
- evidence_id: native-code
  kind: record_content
  reference: src/mediaingredientmech/ingredient_bundle_refresh.py
  accessed_at: '2026-11-08T02:31:48.932195Z'
  support: supports
  summary: Read the exact allowed manifest keys and separate scientific contracts
    for the three older typed contexts.
  snapshot_sha256: cd85ce90c88bb69b05d618492af6bdc7d27adfa12ca1a5c753bb223207ff4f32
- evidence_id: current-history
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv.manifest.json
  accessed_at: '2026-11-08T02:31:48.932195Z'
  support: supports
  summary: Read current owned-name suppression history retained by the completed publication.
  snapshot_sha256: 6b6fe48246bd43dd70499e82f508a7b7ea0fcd121bccafafa0217aae84a17778
- evidence_id: probe
  kind: validation
  reference: reports/kgm_unmapped_chemicals_20261107/baseline-independent/typed-history-proof-v1.json
  accessed_at: '2026-11-08T02:31:48.932195Z'
  support: supports
  summary: All three actual-history probes refuse unknown manifest shape; private
    diagnostic controls reach the next guard. No maintained mutation.
  snapshot_sha256: 081f877937478210cff1b8b54353471d6dcbef17900f88c55f858aebc9a05de4
- evidence_id: audit
  kind: validation
  reference: reports/kgm_unmapped_chemicals_20261107/baseline-independent/baseline-contract-audit-v1.json
  accessed_at: '2026-11-08T02:31:48.932195Z'
  support: supports
  summary: Exact current-baseline receipt replay, four-file export equality with the
    consumed KGM source, installed pair hashes and native MIM snapshot digest.
  snapshot_sha256: dc1ac887c54ae13d00800b8941c281c88d5ac08015ec424ad002ab7a3e5f7ac6
- evidence_id: export
  kind: validation
  reference: reports/kgm_unmapped_chemicals_20261107/baseline-independent/baseline-reviewed-export-v1.json
  accessed_at: '2026-11-08T02:31:48.932195Z'
  support: supports
  summary: Native isolated reviewed export completed with exit zero.
  snapshot_sha256: 6b78fc7c577e817f45b64b979d683353698a5e27fd581044785a8a79f02b18dc
- evidence_id: replay
  kind: validation
  reference: reports/kgm_unmapped_chemicals_20261107/baseline-independent/baseline-reviewed-replay-v1.json
  accessed_at: '2026-11-08T02:31:48.932195Z'
  support: supports
  summary: Native validate-only independent product replay completed with exit zero.
  snapshot_sha256: 88b36a24931d83064044e7d3809da9342e42e805a094b4461b7194e67dbd0357
- evidence_id: companion-export
  kind: validation
  reference: reports/kgm_unmapped_chemicals_20261107/baseline-independent/baseline-companion-export-v1.json
  accessed_at: '2026-11-08T02:31:48.932195Z'
  support: supports
  summary: Native scoped companion export completed with exit zero.
  snapshot_sha256: df3f64db4b5b226bfd92b068b78be6e574e95f15f1e49053784bd3d7080168a9
- evidence_id: semantics
  kind: record_content
  reference: MAPPING_SEMANTICS.md
  accessed_at: '2026-11-08T02:31:48.932195Z'
  support: supports
  summary: Identity/form boundaries and export-only owned-name policy remain authoritative.
  snapshot_sha256: 6b52f2ac48109ddd5d81996a136b19776cab55efa69a5ec832cf716d6885a062
assessments:
- assessment_id: assess-typed-refresh
  area: consistency
  topic: Existing three typed successor contexts
  outcome: concern
  summary: The older form, registry and stock contexts exclude the current owned_name_suppression_updates
    key, so they cannot consume current retained history. Their narrow contracts also
    do not authorize arbitrary alias additions.
  target_ids:
  - typed-refresh
  evidence_ids:
  - native-code
  - probe
- assessment_id: assess-policy-history
  area: consistency
  topic: Current legitimate policy history
  outcome: supported
  summary: Current owned-name history is legitimate immutable prior attribution. Preserve
    it; the compatibility defect is in the older consumer shape check, not a reason
    to erase history.
  target_ids:
  - policy-history
  evidence_ids:
  - current-history
  - probe
- assessment_id: assess-canonical
  area: consistency
  topic: Baseline canonical mapping rows
  outcome: supported
  summary: Baseline canonical has 3014 rows; native export yields 1739 supported and
    1275 withheld. Actual supported predicates are 1737 exact and two broader. Its
    content equals the source already selected by KGM.
  target_ids:
  - canonical
  evidence_ids:
  - audit
  - export
  - replay
- assessment_id: assess-mapping-review
  area: consistency
  topic: Content-bound mapping dispositions
  outcome: supported
  summary: Native replay validates all 26 receipt links and content-bound decisions.
    A changed owner or row cannot inherit support; new curation needs explicit receipt
    and mapping-specific review.
  target_ids:
  - mapping-review
  evidence_ids:
  - audit
  - replay
  - semantics
- assessment_id: assess-companion
  area: consistency
  topic: Separate scoped companion review
  outcome: supported
  summary: 'Native scoped export passes with 20 owners and 51 claims: 20 mappings,18
    identifiers,10 occurrences,3 products;50 supported and one withheld. It is separate
    from the KGM supported/unified pair.'
  target_ids:
  - companion
  evidence_ids:
  - audit
  - companion-export
- assessment_id: assess-unified
  area: consistency
  topic: Baseline unified snapshot
  outcome: supported
  summary: Snapshot hash and all 2956 MIM record inputs match the native provenance;4170
    snapshot rows. This does not assert current CultureMech/provider freshness.
  target_ids:
  - unified
  evidence_ids:
  - audit
- assessment_id: assess-unified-provenance
  area: consistency
  topic: Native MIM input provenance
  outcome: supported
  summary: Native MIM input digest is exact at this baseline. A later record edit
    creates real drift; stamping old output does not rebuild it.
  target_ids:
  - unified-provenance
  evidence_ids:
  - audit
  - semantics
- assessment_id: assess-history-probe
  area: consistency
  topic: Independent read-only compatibility reproduction
  outcome: supported
  summary: Read-only native API probes reproduce the schema refusal in all three contexts.
    The in-memory key-removal control is diagnostic only, not a proposed fix or accepted
    successor.
  target_ids:
  - history-probe
  evidence_ids:
  - probe
  - native-code
  - current-history
findings:
- finding_id: typed-successor-rejects-owned-name-history
  issue_key: mim-typed-successor-owned-name-history
  category: consistency
  severity: minor
  native_severity: P3 / fail-closed successor compatibility
  normalization_reason: Current exports pass; the defect blocks later typed transitions
    without admitting unsupported data.
  status: open
  certainty: confirmed
  title: Older typed refresh contexts reject legitimate owned-name history
  description: Current canonical manifest contains owned_name_suppression_updates,
    but the shared form/registry/stock shape check excludes it. All three native paths
    refuse before validating a successor. Preserve existing history and scientific
    constraints; do not remove the key to pass.
  target_ids:
  - typed-refresh
  - policy-history
  - history-probe
  field_paths:
  - '_verify_policy_projection: allowed manifest keys'
  - owned_name_suppression_updates
  evidence_ids:
  - native-code
  - current-history
  - probe
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: src/mediaingredientmech/ingredient_bundle_refresh.py
    role: Typed companion successor contract
  external_issues:
  - https://github.com/CultureBotAI/MediaIngredientMech/issues/1150
actions:
- action_id: preserve-unrelated-owned-name-history
  description: When the older typed path is needed, admit the existing owned-name
    update history only as immutable unrelated provenance while retaining each context's
    exact transition and scientific constraints. Do not erase or repurpose history.
  finding_ids:
  - typed-successor-rejects-owned-name-history
  target_ids:
  - typed-refresh
  - policy-history
  - history-probe
  ownership_note: Maintained typed companion refresh contract and focused regression
    tests; separate from new alias curation and any scientific approval.
  acceptance_checks:
  - Valid typed successors preserve every prior owned-name history entry exactly.
  - Deleting, altering or reordering the unrelated history is rejected.
  - All existing native receipt, owner, sidecar, selected-claim and approval restrictions
    remain enforced.
  - A true alias addition uses its own bounded contract and is not relabeled hydrate_parent_predicate.
checks:
- check_id: export
  name: export
  status: passed
  required: true
  command: /Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/kgm-unmapped-20261107/env/bin/python
    -B -m mediaingredientmech.export.reviewed_sssom --root /Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/kgm-unmapped-20261107/worktree
    --review reports/sssom_completion_20260921/review.json --output /Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/kgm-unmapped-20261107/reviewer/baseline-reviewed-export-v1
  exit_code: 0
  summary: Actual native command completed; original receipt and log retained.
  target_ids:
  - canonical
  - mapping-review
  - companion
  evidence_ids:
  - export
- check_id: replay
  name: replay
  status: passed
  required: true
  command: /Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/kgm-unmapped-20261107/env/bin/python
    -B -m mediaingredientmech.export.reviewed_sssom --root /Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/kgm-unmapped-20261107/worktree
    --review reports/sssom_completion_20260921/review.json --output /Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/kgm-unmapped-20261107/reviewer/baseline-reviewed-export-v1
    --validate-only
  exit_code: 0
  summary: Actual native command completed; original receipt and log retained.
  target_ids:
  - canonical
  - mapping-review
  - companion
  evidence_ids:
  - replay
- check_id: companion-export
  name: companion-export
  status: passed
  required: true
  command: /Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/kgm-unmapped-20261107/env/bin/python
    -B -m mediaingredientmech.export.ingredient_bundle export --root /Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/kgm-unmapped-20261107/worktree
    --review reports/owned_name_deferred_669_20261103/companion-review.json --output
    /Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/kgm-unmapped-20261107/reviewer/baseline-companion-export-v1
  exit_code: 0
  summary: Actual native command completed; original receipt and log retained.
  target_ids:
  - canonical
  - mapping-review
  - companion
  evidence_ids:
  - companion-export
limitations:
- Truthful isolated overlay has actual durable HEAD0dac2784. Baseline tracked bytes
  were read from that commit; newly copied diagnostic proofs are separately captured
  working-tree inputs. The later author worktree is not represented as unchanged.
- No fresh scientific approval of sodium acetate aliases, roles, formulae or source
  occurrences is conferred.
- MIM-supported phosphatidylcholine remains separately downstream-held by KGM1799;
  the old native mapping approval does not clear that consumer hold.
- Native MIM snapshot freshness proves its own record digest, not all current CultureMech/provider
  inputs.
- Full QC/current-main checks and final changed-head review remain separate root-owned
  work. No result of a still-running or uninspected check is inferred.
- Probe controls deliberately remove a key only in memory to locate the guard. They
  do not constitute a valid successor or authorize changing historical files.
```
