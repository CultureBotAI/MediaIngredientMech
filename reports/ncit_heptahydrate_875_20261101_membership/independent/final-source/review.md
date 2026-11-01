# Independent final source re-review: #1031 / #1033

Source-review verdict: PASS within the bounded membership-repair scope, pending production artifact, native bundle and exact final-head checks. This is not scientific approval or merge approval.

Reviewed membership writer SHA256a3a8af0acfd2daa94a5da70270f0fd0923b7be0da644a4878688cac2c4aaad17 and original/shared publisher SHA256768166cfb726e3a751b451a89bebfa30c8dea7e22f05ba085cf4fb9db96550ee. All three mutation call sites now supply owner-uniqueness validation at native commit validation. Promotion also checks uniqueness before a completed-state no-op. Existing input-byte and reserved-output-identity checks remain intact. The bounded guarantee assumes the caller's repository lock and checks the namespace immediately within native validation; it does not promise exclusion of arbitrary later uncooperative writes.

Independent actual-native transaction probes, saved in this new directory without overwriting prior failures:

| Probe | Result |
|---|---|
| Membership repair on exact frozen production preimage | PASS; only membership changed to55ce5fabd42eb4cc1df628d4fd6a45b813caccbc7d7773105ece5633dd313897 |
| Repeated membership apply | PASS; no-op, immutable receipt preserved |
| Valid ignored/nested competing owner inserted after membership reservation | REFUSED before membership mutation |
| Same insertion after original source-phase reservation | REFUSED before owner/ledger mutation |
| Same insertion after original promotion reservation | REFUSED before SSSOM mutation |

Each competing record was accepted by the native validated serializer before insertion and remained intact afterward. Failed receipts and reserved preimages survive; there are no apply journals for these rejected mutations. Source-phase fixtures use the exact original frozen owner/ledger/SSSOM hashes and preserved NCI bytes. Promotion fixtures first complete a clean native source apply and use the archived native candidate target row. In that fixture's input_changes report, owner/ledger differences reflect the legitimate setup step, not a failed promotion mutation.

Independent regression run:158passed,1deselected,12dependency deprecation warnings, no skipped tests. The one deselected case checks production memberships and intentionally awaits the root's application. Command:

```text
PYTHONPATH=src:../claw-source/src RUN/envs/mim/bin/python -m pytest -q -o addopts='' -p no:cacheprovider --basetemp ../step2-independent/all-writer-scope-fixed-20261101T060930Z/pytest-tmp tests/test_repair_heptahydrate_membership.py -k 'not committed_memberships' tests/test_promote_heptahydrate_ncit.py tests/test_semantic_identity_occurrences.py
```

The prior independent scope comparison establishes202098 rows before/after: exactly32 existing recipe/count pairs migrate and202066 unrelated rows remain equal, with identical source-provenance header. Frozen hashes plus explicit recipe/count guards prevent other membership changes. Original YAML counts26/26 and all identity/SSSOM/rejection-ledger inputs remain untouched by this repair; generated effective counts are expected to recover32/32 after production application.

Finite source-label routing is exactly the current preferred `Na2HPO4 x 7 H2O`, dotted `Na2HPO4.7H2O`, and accepted bullet `Na2HPO4•7H2O`. Native producer and sibling/parent/preparation controls pass. The known middle-dot and English-name expansion remain explicitly outside this32-edge repair; no claim that all source spelling/count drift is resolved. No chemistry, BUFFER, companion, or release approval is added.

Findings #1031 and #1033 were reported before implementation/fixes. The earlier failure bundles, original production receipts and inventory remain immutable. The new wrapper's initial missing namespace recheck and both original source/promote call-site gaps now fail closed in independent reproductions. Final product checks must still verify the actual membership/output deltas, anchored source bytes, original receipt preservation, full QC/receipt replay, durable native review capture, and final committed head.
