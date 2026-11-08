# Bounded campaign publication contract (#1174)

This implementation is a capability tested against private fixtures. No actual campaign owner or canonical publication has been performed. Source application, scientific mapping admission, and the fresh companion review remain separate.

## Entry points

- `publish(root, plan_path, receipt_dir, apply=False)` reconstructs the plan and defaults to a dry run. The output directory must already exist under `reports/` and all four output paths must be absent.
- `validate(root, plan_path)` independently reconstructs the same source, generation, row, policy and native receipt transition after publication.
- The CLIs are `scripts/publish_unmatched_campaign.py` and `scripts/validate_unmatched_campaign_publication.py`. Use Python 3.13 and the integration worktree's `src` on PYTHONPATH. All plan and output paths must be absolute, lexically canonical, and free of aliases.

## Closed plan

Exact top-level keys: schema_version (1), kind (`unmatched_campaign_publication_v1`), issue (the full #1174 URL), approval (`NONE`), batch (`issue1174-...`), scope, owner_plan, owner_receipt, publication_producers, before, generation, receipt_prefix, native_context, rows. Unknown keys are errors.

File references have exactly path (repository-relative) and sha256. `owner_plan` and `owner_receipt` refer to the separate accepted source-owner application contract. Its real verifier reconstructs accepted evidence, source inventories, payloads, old-path retirement, and its native checkpoint. Every changed owner is retained in the native mapping receipt, including source-only changes.

`publication_producers` exactly binds the publisher, source-owner loader and privately executed native dependency bytes listed by `LOADED_PRODUCERS`; its current keys are the authoritative interface. Already-cached public dependencies are neither trusted as the executing implementation nor silently reloaded. The shared bounded loader compiles captured bytes in private namespaces and retains those exact execution snapshots. `before` contains immutable canonical, policy, sidecar and baseline copies. These must match the source application's protected checkpoint. The source owner plan must protect all native checkpoint files plus the policy, sidecar and Rule K baseline.

`generation` contains candidate, sidecar and manifest references plus absolute producer_root and kg_root. Generate the real candidate triple inside this worktree using the pinned Claw producer at 76c1ebee, with `--prior-stamps-from` explicitly naming the current canonical. The manifest must bind the complete mapped-owner set, producer graph, source inputs, captured label resolution and exact three source revisions; its MIM revision must equal the accepted source-application baseline. No providers are called by replay. The generator replay verifies all candidate rows and native diagnostic suppression bytes using the captured canonical label resolution; this does not replace scientific/id-label review.

`receipt_prefix` lists every pre-existing native receipt path and hash. `native_context` lists exactly the three native historical context inputs. Old history is not rewritten; the prospective owner chain and canonical row replay must both pass before output reservation.

Each `rows` item has exactly owner, before_position, native_position and preserve_fields. Positions are one-based; null means a genuine added or removed native slot. Every selected owner's before and native slots must be accounted for exactly once. A preserved historical field is limited to source, comment, confidence or validation_method and is explicitly traced. Every other selected cell comes from native generation. Unselected physical rows are retained byte-for-byte; only the two header date values may follow the native date rule.

## Publication and preserved boundaries

The policy transition changes only the canonical artifact hash and appends one closed `campaign_publication_updates` entry. Existing decisions, all historical update arrays, the historical owner-attribution map, suppressed_aliases.tsv and other_cross_record_baseline.tsv are preserved. Selected stale policy pins require the existing native owner receipt bridge. Promotions retain their real old digest and explicit old path, and refuse prior owner-chain links on either old path or destination; null before hashes are only for real creations.

The unchanged native Rule K evaluator checks the entire proposed canonical output before reservation, including unselected rows and prior-only tokens absent from the diagnostic sidecar. New suppression effects are a fail-closed execution boundary. Do not omit scientifically supported owners to evade it; review any required bounded extension under the already authorized #669 policy before applying the real campaign.

All outputs and backups are exclusively reserved before mutation, using held directory handles. Complete owner/proof/producer/receipt membership, original input bytes and identities, source retirement and output handles are rechecked at mutation and completion boundaries. Partial attempts preserve recovery evidence but clear both success-shaped receipts; there is no silent rollback or automatic scientific approval.

The publisher emits no positive scientific review or companion adapter. Final scientific review, current native QC, mapping admission/withdrawal checks, fresh full companion review, full tests and independent adversarial review remain required before any release.
