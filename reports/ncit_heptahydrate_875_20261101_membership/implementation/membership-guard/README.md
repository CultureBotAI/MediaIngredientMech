# #1033 precommit owner uniqueness repair

This append-only revision supersedes the earlier implementation-stability claim. The earlier 30-file evidence index and all its listed bytes remain unchanged, including original membership writer 85317d... and shared producer f7cd1b.... Those earlier passing tests did not cover the subsequently discovered valid-owner race.

## Change

`promote_heptahydrate_ncit.publish()` now accepts an explicit optional `validate_scope` callback and runs it within the native transaction validator, after the existing input-byte and reservation-identity checks. The membership writer supplies the ignored/nested-inclusive `unique_destination(root)` check. The implementation uses no runtime monkeypatch or global replacement. The original #875 source/promotion call sites retain the default behavior, with no new application or curation history.

This closes the specific reproduced gap: a native-serializer-valid duplicate NCIT owner introduced under an ignored nested directory after evidence reservation causes the precommit transaction to fail. Membership and all anchored source bytes remain unchanged; the competing owner survives; the exact membership beforeimage and failed receipt remain available. This check makes no guarantee against arbitrary edits after a completed transaction.

Final hashes are in `stable-source.json`: membership writer a3a8af0a..., shared producer 9effce3c..., tests 2aa06a3a..., router 8ecd6beb... . `source-snapshot/` preserves their exact bytes. The historical f7cd producer remains preserved under the parent evidence directory and prior frozen Step2 reports; its historical execution/receipt claims have not been relabeled as executions of this newer code.

## Validation

- New valid-owner regression against the pre-fix writer: expected failure (`DID NOT RAISE`). Independent original native reproduction is copied under `independent-original/`.
- Final combined suite: **154 passed, zero skipped, one deselected**. This includes the original 84 source/promotion writer tests, the updated membership suite and existing 8 semantic identity routing tests. The committed-membership assertion remains pending root application.
- First post-fix run rejected the race correctly but the test expected `ValueError`; the native transaction wraps it as `ValidationFailed`. That diagnostic log is retained. The test now asserts the native exception type and preservation properties.
- Fresh-process counterfactual disables only the optional callback: the new regression fails (`DID NOT RAISE ValidationFailed`). The separate plugin lives only in the external test process and never changes source files or production data.
- Native locked CLI dry-run PASS; its proposed output hash and 32 memberships are unchanged. Ruff PASS.
- At stable-source capture 06:06:28Z, membership, owner YAML, SSSOM, rejection ledger and unified mapping bytes were still unchanged; no production application, commit or push was performed by this agent.

Independent re-review and root application/export checks remain separate steps. No scientific approval or later-plan implementation is asserted.
