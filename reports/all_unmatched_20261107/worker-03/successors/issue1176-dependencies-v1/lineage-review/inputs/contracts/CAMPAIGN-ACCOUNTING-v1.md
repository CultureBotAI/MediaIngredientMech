# Coordinator campaign accounting

This private, read-only helper checks the frozen 1,879-case union and all ten
exact shard hashes in `frozen-baseline.json`, then invokes the unchanged pinned
`audit_worker_outcomes_v1.py` for each explicitly selected active worker bundle.
The worker outcome schema remains [OUTCOME-CONTRACT-v1.md](OUTCOME-CONTRACT-v1.md).
It does not create decisions, apply proposals, update the coordinator ledger,
control workers, contact GitHub or judge scientific adequacy.

Run from `.temp/all-unmatched-20261107` with the existing Python 3.13 environment:

```sh
PYTHONDONTWRITEBYTECODE=1 ../kgm-unmapped-20261107/env/bin/python \
  scripts/audit_campaign_accounting_v1.py \
  --baseline frozen-baseline.json \
  --baseline-sha256 622bd1bb65656c4277dd0d5dc97f84275c49e76845c29cae247485b44f134fdb \
  --bundles preflight/campaign-accounting-v1/active-bundles-template.json \
  --current-mim-root ../kgm-unmapped-20261107/worktree \
  --output preflight/campaign-accounting-v1/NEW-observation.json
```

The output must be a new file under `preflight/campaign-accounting-v1`; existing
reports are never overwritten. A valid observation returns exit zero even when
work is incomplete or conflicts exist. Inspect the JSON fields. A wrong baseline,
union, shard or auditor pin, or invalid coordinator configuration stops the run
without a success report. Do not treat exit zero as campaign acceptance.

`active-bundles-template.json` names the coordinator-provided artifact paths; it
is not evidence that the workers have produced or completed them. Select only
current active bundles, using a new explicit configuration for each observation.
Do not search for a convenient older passing output automatically. Configuration:

```json
{
  "schema_version": 1,
  "bundles": [{
    "bundle_id": "w01-active-shard",
    "worker_slot": 1,
    "decisions": "/explicit/worker-01/shard/decisions.json",
    "evidence": "/explicit/worker-01/shard/evidence.json",
    "proposals": "/explicit/worker-01/shard/proposals.json",
    "artifact_root": "/explicit/worker-01",
    "source_root": "/explicit/campaign/queue",
    "mim_root": "/explicit/worker-01/worktree"
  }]
}
```

The worker's actual capture paths determine the declared roots. For worker01's
full shard, the common `worker-01/` artifact root permits hash-bound references
such as `canary/captures/...` to the immutable sibling canary evidence. The active
full-shard decisions must account for that case once. Do not also list historical
canary decisions as another active bundle: that is a duplicate claim and blocks
structural completeness. The earlier canary bundle used its own `canary/` artifact
root; that historical schema and its captures remain unchanged. An explicitly
declared `canary_case` is permitted only for a genuine canary observation and
never counts as a completed full shard.

Worker02–10 assignments use `worker-NN/{decisions,evidence,proposals}.json` directly,
without an assumed `shard/` subdirectory. No file is created in those roots by
this helper. `mim_root` is the worker's exact before-owner reference root; it is
required by the unchanged auditor when the worker cites existing owners.

The explicit coordinator `--current-mim-root` is a separate comparison target.
For this pre-integration campaign checkpoint it is
`../kgm-unmapped-20261107/worktree`, the PR1158 baseline, not the original `main`
checkout. Later deliberate integration can change these bytes. A before/current
conflict then requires provenance and integration review; it is not a scientific
rejection of the integrated record. The helper selects no winning proposal and
never merges proposed payloads, even when two proposals target one owner.

Interpretation:

- `missing_case_ids` means no claim was read from the selected bundles. Available
  decisions without evidence/proposal files remain raw claims, with missing files
  reported and `strict_audit: NOT_RUN`.
- `not_fully_audited_case_ids` includes every case not accepted by a complete
  strict worker audit, plus duplicate active claims. Partial full-shard files
  keep the native auditor's missing-coverage failure; they are never rewritten as
  synthetic canaries or counted complete.
- Duplicate, unknown and cross-shard claims, exact source identity/hash/occurrence
  mismatches, stale/current owner conflicts and different proposed owner bytes
  are explicit arrays. Full-shard structural passes, source-case counts, literal
  source-name counts and unique owner-path counts remain separate. Names and
  owner paths are not counts of distinct chemical identities.
- `structural_inventory_complete` requires ten full-shard native passes, every
  frozen case exactly once, stable captured inputs, and no reported conflict.
  `campaign_complete_or_scientific_approval` is always false. Independent-review
  states are merely the workers' structurally bound declarations, not validation
  of reviewer independence, primary-source applicability or scientific adequacy.
- Reading live files is an observation, not an atomic worker checkpoint. Captured
  inputs are rehashed before completion; changed inputs prevent completeness.
  Issue #1161 also binds each consumed evidence capture, proposal payload and
  worker-before-owner reference to its original declared root, initially resolved
  root and normalized relative path. The final boundary reruns the unchanged
  native `safe_file` check and verifies each role's bytes. Equal-byte leaf or
  ancestor symlink substitutions and changed root bindings prevent completeness;
  `consumed_path_roles` and `path_role_errors` retain the exact affected roles.
  Prefer immutable published bundles for final acceptance, and inspect all input
  hashes and the recorded explicit roots. This helper does not verify Git/PR/CI
  status or that a chosen worker worktree is clean.

Offline regression controls are in `test_audit_campaign_accounting_v1.py`. They
use only synthetic 1,879-case queues and never assign outcomes to real cases:

```sh
PYTHONDONTWRITEBYTECODE=1 ../kgm-unmapped-20261107/env/bin/python -m pytest \
  -o addopts='' -p no:cacheprovider --confcutdir=scripts \
  --basetemp=preflight/campaign-accounting-v1/NEW-pytest \
  scripts/test_audit_campaign_accounting_v1.py -q
```

Keep unique check logs and preserve unsuccessful runs. No maintained repository
source, gate, workflow, outcome auditor or worker artifact is changed by this
coordinator helper.
