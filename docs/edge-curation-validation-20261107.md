The native EdgeMech adapter transports pinned reviewed MIM mappings while
preserving complete source rows, native decisions, owning records and evidence
bindings. Supported and withheld scope survive; no new scientific review or KG
occurrence approval is created. This implements the MIM adapter for
[CLAW #767](https://github.com/CultureBotAI/culturebotai-claw/issues/767).

Shared native contracts are pinned at CLAW
`1b5391d083ba85ac94e5279c3cba25ac4fde243c`; the contracts-only prerequisite is
[CLAW #962](https://github.com/CultureBotAI/culturebotai-claw/pull/962).
The dedicated integration tier requires that exact checkout and import origin.
The base native mypy tier follows the existing optional-import policy for this
exporter while retaining its other type checks. No dependency version changed.

Validation on 2026-11-07:

- Native Ruff, Black and mypy quality recipes passed across 61 source files.
- 92 adapter, publication and reviewed-SSSOM integration tests passed with the
  shared contract required.
- The real pinned source archive and reviewed bundle were verified before the
  three-row canary, then the complete export used the same launcher/environment.
- Persisted row counts, hashes and status counters were checked. The refreshed
  JSONL bytes are identical to the preceding independently reviewed export.

The immutable native source is `1848b0fe521bc2462f165912fcf92d09ad9a8cec`.
Archive SHA256 is `33ff549d7a2bf34e943156e800e00149736a30dfc0a974f3ca9a9884358bfef2`;
native bundle manifest SHA256 is `9bb29d5605d93dea351be9624d99c5d8ada57d4b9831b22764957b784bd685af`.

Final artifacts remain under ignored `output/edge-curation-20261107/`:

| Export | Rows | Bytes | Manifest SHA256 |
| --- | ---: | ---: | --- |
| `mim-canary-quality` | 3 | 25,392 | `2f0a74b3985f7e57a0a404897b2451529c66c444cfd12cdf025d9d419aaea730` |
| `mim-full-quality` | 2,999 | 24,592,536 | `3b8166c8a30d95c5c56387c9bd80a1a7c482058a2d9d781e31b3c1496d176741` |

Canary JSONL SHA256: `cb03a199754812e9a4a895013e3af981f5b0606966baf81936eafc3fbd2129c2`.
Full JSONL SHA256: `58748c350d4770aca02b0a82cf983afe64c8d10658b84a8dc3a0adb605a9888d`.
The canary retains one supported and two withheld decisions. The full export
retains 1,747 supported and 1,252 withheld decisions. Both create zero reviews
and zero KG approvals. Earlier receipts remain preserved.

Use retained `scripts/adhoc/run_edge_adapter_canary_20261107.py` with the pinned
archive, bundle, commit and hashes, `--positions 1 21 25` for the canary, then
`--all` and a new destination after verifying persisted canary artifacts.

Independent read-only review filed publication findings #1145/#1146; their
repairs exclusively reserve destinations, publish manifests last, and sync
files and directory entries. Regression tests and independent repair review
passed. The #1148 quality repair also passed independent read-only review.
Fixes #1145. Fixes #1146. Fixes #1148.

Issue #1144 remains open for a minimal shared-contract package because the
native and CLAW LinkML requirements differ. Endpoint matches do not establish
organism growth, medium preference, function or current KG occurrence review.
This PR remains draft and requires explicit approval before merging.
