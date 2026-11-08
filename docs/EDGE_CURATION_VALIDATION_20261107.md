The native EdgeMech adapter transports pinned reviewed MIM mappings without
discarding source rows, native decisions, owning records or evidence bindings.
It retains supported and withheld scope and creates no new scientific review
or KG occurrence approval. This is the MIM slice of
[CLAW #767](https://github.com/CultureBotAI/culturebotai-claw/issues/767).

The adapter uses the shared native assertion contract at CLAW commit
`1b5391d083ba85ac94e5279c3cba25ac4fde243c` (prerequisite CLAW PR #953).
The dedicated integration workflow checks that exact checkout and import
origin; missing shared code fails its mandatory feature tests.

Validation on 2026-11-07:

- Focused native adapter, publication and existing reviewed-SSSOM tests:
  **92 passed**, with `MIM_REQUIRE_EDGE_CONTRACT=1` and the exact shared checkout.
- `uv lock --check --offline` passed; no native dependency upgrade or relock.
- The real immutable `1848b0fe521bc2462f165912fcf92d09ad9a8cec` archive and
  reviewed bundle were verified before a positions 1/21/25 canary, followed by
  the complete native partition through the same launcher and environment.
- The corrected publisher persisted 3 canary assertions (1 supported,
  2 withheld), then 2,999 complete assertions (1,747 supported, 1,252 withheld).
  All input/output bytes, partition membership, decisions and persisted
  counters were verified. Zero new reviews or KG approvals were created.

Input archive SHA256:
`33ff549d7a2bf34e943156e800e00149736a30dfc0a974f3ca9a9884358bfef2`.
Native bundle manifest SHA256:
`9bb29d5605d93dea351be9624d99c5d8ada57d4b9831b22764957b784bd685af`.

Persisted artifacts are analytical outputs under ignored
`output/edge-curation-20261107/`:

| Export | Rows | JSONL bytes | Manifest SHA256 | JSONL SHA256 |
|---|---:|---:|---|---|
| `mim-canary-durable` | 3 | 25,392 | `fe53049961c2ef1d5756b2e2bc2ed99c75049a5e0e448e8ed05e29cf7c8bb597` | `cb03a199754812e9a4a895013e3af981f5b0606966baf81936eafc3fbd2129c2` |
| `mim-full-durable` | 2,999 | 24,592,536 | `7b5c493d9301022b5972c304f69dd6f5e9ddad12881bac79ed48a90cb603e9c9` | `58748c350d4770aca02b0a82cf983afe64c8d10658b84a8dc3a0adb605a9888d` |

The retained launcher is `scripts/adhoc/run_edge_adapter_canary_20261107.py`.
Supply `--archive`, `--bundle`, `--source-commit`, `--archive-sha256` and
`--manifest-sha256` as above, then `--positions 1 21 25` or `--all` and a new
`--output` directory. Source checking is retained in
`scripts/adhoc/check_edge_contract_pin_20261107.py`.

An independent read-only review filed #1145 and #1146. The repaired publisher
exclusively reserves the destination, publishes the manifest last through
non-replacing links, and syncs files and directory entries. Race, interruption
and directory-sync regression tests pass; independent repair reinspection
found no additional blocking finding. Fixes #1145. Fixes #1146.

Issue #1144 remains open for extracting a minimal shared-contract package;
the native LinkML version is unchanged. This PR intentionally does not infer
organism growth, medium preference, biological function, or eligibility of a
current KG occurrence from a matching ingredient endpoint.
