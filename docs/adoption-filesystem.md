# Guarded filesystem primitives for stable-ID adoption

These imports support the #1303 transaction's filesystem operations. They do
not allocate IDs, validate ingredient science, grant admission, synchronize
aggregates or implement a complete adoption transaction.

`curate/publication_guard.py` is copied byte for byte from MediaIngredientMech
commit `84241993a278a7a413422ef89a52c0b47dc57831` (SHA-256
`f6d1e625b3bd2c7e01cd938cb00e77c57bdfc7ffda350b8925ef690c0e4b464b`).
Its original commit is `cd76b3e5d3475545f68b65cd765a876ca61e0a2b`, carried in
[PR1158](https://github.com/CultureBotAI/MediaIngredientMech/pull/1158) and
[PR1205](https://github.com/CultureBotAI/MediaIngredientMech/pull/1205).

`curate/adoption_filesystem.py` originally extracted `require`, `_new_owner`,
`_rename_exclusive` and `_retire` unchanged from `campaign_owner_apply.py` at
the same commit. The original owner primitives were introduced in commit
`1c5f6056c4`, with relocation guards refined in `16c39b63bc`, in PR1205.
The rest of that fixed-cohort operator and its scientific inputs are not imported.
Prior review of those sources does not replace review of this extraction or
its new callers.

[Issue #1314](https://github.com/CultureBotAI/MediaIngredientMech/issues/1314)
documents a scoped divergence in the new `_retire` adaptation. It now binds
the initially empty recovery directory and its ancestors, compares the opened
directory descriptor with that identity, and checks freshness before moving
the source. After movement it rechecks the same directory and permits only
the retired entry. Both directory descriptors are closed on acquisition or
later failure. The three other extracted functions and the full
`publication_guard.py` remain unchanged. The immutable original extraction and
its independent failing reproduction remain historical evidence; no legacy
campaign code or receipt is rewritten by this repair.

The caller must validate and stage the complete set of candidate bytes before
mutation, hold the repository write lease, reserve all receipt/backup outputs,
and supply a `recheck` callback that verifies the complete expected transaction
state. It must also validate the closed destination paths and their scope;
these primitives do not interpret a plan or authorize arbitrary paths.
Use the existing `reserve_receipt_outputs` and retain its open handles;
`check_reserved` detects replaced, linked or aliased evidence entries.

- `FrozenFile` retains input bytes, file identity and parent identities. It
  rejects symlinks, nonregular files and hardlinks, and verifies later drift.
- `publish_validated` renders through a caller-provided native gate and replaces
  one held entry. It checks inputs before and after publication. Replacement
  does not write through a hardlink to the old inode.
- `_new_owner` accepts already validated bytes and installs an exclusive new
  entry using the held parent descriptor. It refuses a competing destination.
- `_retire` moves a held source into a fresh recovery directory using a native
  no-replace rename. It preserves the original inode and bytes. Unsupported
  platforms refuse; there is no overwriting rename fallback.
- `finish_receipt` checks the reservation and inputs and clears a success
  payload when it detects drift during receipt writing.

These are per-file operations, not a batch atomicity or automatic recovery
guarantee. A late error can leave a published file or a retired/raced inode in
recovery. The outer operator must record the actual completed prefix and
failure, preserve backups and partial state, and never fabricate success or
silently roll back or retry. It must verify the full final inventory, ledger,
aggregates and other transaction invariants before recording completion.

`tests/test_adoption_filesystem.py` adapts the original exclusive-create,
exclusive-retirement, parent-alias, wrong-inode, hardlink, reservation and
late-input checks. Its synthetic bytes test filesystem boundaries only; they
are not scientific or native-schema fixtures. All original maintained tests
remain unchanged. Additional #1314 controls cover pre-open directory and
ancestor replacement, same-directory contamination, descriptor mismatch and
acquisition failures, plus later swaps and retained partial recovery evidence.
