# Issue1247: exact native-origin and local revision binding

This immutable private successor repairs the independently reproduced v2 defects documented at issue1247 comment6719418842. It does not rematerialize campaign intake, accept science, create a real campaign application plan, modify native code or apply any maintained owner.

The v2 crosswalk verified a genuinely published proposal independently, but joined it to native preparation by origin ID, head and case hashes only. Two different valid originals at the same head could therefore be confused. The new `_verify_native_origin` compares the actual native `proposal_binding` and `payload_binding` with the crosswalk's exact published head, path and file hash. It parses the native captured original ledger and compares the complete selected proposal and canonical object digest; that includes original owner path, kind, preimage, source cases and all remaining authored fields. The actual original payload digest is joined too.

Local capture paths are intentionally separate from publication identity: two independent regular files containing identical committed bytes are allowed. Different published paths are not silently treated as one origin. A reconciled final operation payload is a third concept: it may legitimately differ from an individual source payload, and continues to be checked against actual native preparation, accepted final operation hashes and review bindings. No original is replaced with the final combined payload to make the join work.

`Proofs` captures the actual local integration HEAD at entry. Each final proof recheck requires the same HEAD, and a supplied native plan's baseline must equal that captured entry HEAD. Existing actual input hashes, owner inventory/membership, alias checks and native rechecks remain. The extra baseline comparison also refuses an A→B→A revision transition around native preparation. This is a local revision check; it does not prove a remote branch has not advanced.

The public function signature and closed input shapes are unchanged from v2, documented byte-exact in `historical-v2/README.md`. The result additionally exposes `local_head`. Both `scientific_approval` and `application_authorized` remain false. `accounting.py`, `build_scaffold.py`, `test_accounting.py` and `test_crosswalk.py` are byte-identical to v2. All66 v2 cases remain; no assertion was removed or loosened. The complete v1/v2 packets remain outside this directory untouched.

## Verification

Python3.13.2 ran the combined suite:76 passed,12 dependency deprecation warnings. Ruff and Black checks pass for all six active Python files. The native operator and its complete producer pin set are unchanged from v2, verified in `preservation-and-producers.json`.

Ten new cases exercise the real native prepare path, not a fabricated success receipt:

- The reviewer's two-valid-originals-at-one-head counterexample refuses without owner writes; both matched-original positives pass first.
- Identical original bytes at a different published ledger or payload path refuse.
- Different local capture paths and a composed final payload with two origins/one operation pass; the original source hashes remain distinct from the composed final hash.
- Late same-tree HEAD changes at either final proof boundary refuse, with and without a native plan.
- An initially stale native baseline still refuses.
- Actual native preparation at B cannot justify accounting that starts and ends at A.

Every new fixture checks retained owner bytes; no maintained source corpus is passed to the application writer. Tests create only durable private fixture repositories under this packet. `pytest-v1.log` preserves an initial wrong-cwd missing-test-file invocation; it executed no test. `pytest-v2.log` preserves74 passing cases before the explicit entry-baseline guard and two additional controls. `executed-producer-v1/` preserves that tested source. The final76-case run is `pytest-v3.log`.

Use a new private fixture directory for a repeat, and keep the shared environment read-only:

```bash
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$C/integration/worktree/src" \
  "$T/env/bin/python" -B -m pytest -q --noconftest -o addopts='' \
  --basetemp=NEW_PRIVATE_FIXTURE_DIR \
  test_accounting.py test_crosswalk.py test_crosswalk_v3.py
```

The independent reviewer must re-run the exact original probes and assess this frozen source separately. This author's tests and handoff do not grant independent acceptance, scientific approval, current-source acceptance or permission to apply owners. The existing campaign accounting counts remain historical until root freezes a new published-input cutoff.
