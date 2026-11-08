# Explicit demotion source interface

Authorship: `/root/next23_context`; implementation is not independently approved. Baseline: ordinary commit `9a1a4a35498a1bee0fc8b68653d1fc152cfff81b`.

Only an operation whose `kind` is `demote` gains the required `relocation_review_binding` key. All old edit/create/promote operation keys remain closed and unchanged. The new binding ID must select an existing role=`review` artifact and appear in `acceptance.review_bindings`; its bytes and the full plan are already acceptance-hash-bound. The review artifact is closed JSON with exactly these keys:

- `schema_version`: integer 1 (boolean true is not accepted).
- `operation`: `review_campaign_owner_demotion`.
- `operation_id`: exact source operation ID.
- `before_source_record`: exact authentic mapped predecessor path.
- `source_record`: exact exclusive unmapped destination path.
- `before_yaml_sha256`: real non-null predecessor digest.
- `after_yaml_sha256`: digest of the final native-rendered application payload.
- `origins`: the exact operation origin list, retaining published worker/head/proposal/payload-binding and case-hash values.

The tuple is mechanical evidence binding. The caller remains responsible for genuinely independent scientific review and accepted current input lineage. Free-text `change`/`verification` fields and AMBIGUOUS status do not dispatch or authorize relocation. Original published worker proposal/payload pins remain distinct from the separately accepted composed final payload.

The demote paths must be direct native record children, mapped to unmapped, with precisely the same basename. The true old payload must be MAPPED; the new payload must be AMBIGUOUS without an ontology_mapping object. Both paths must lack prior native owner-chain links. Full-catalog collision, schema, ordered history, native-render equality, complete inventory, source-case/origin, loaded producer, no-op, alias/inode and late-drift guards remain.

Source application returns `kind: demote`, `shape: demotion`, destination `source_record` and authentic `before_source_record`, real before/after digests, original full origins and the review binding. It reserves `owner-before-NNNN.yaml` before mutation, creates the destination exclusively, and retires the original source inode into `demotion-NNNN/retired-owner.yaml`. Existing top-level receipt/backup/checkpoint/retired_sources formats remain; there is no fictional new_record or generic old-path migration. Source `verify_completed` rechecks all these roles, frozen checkpoint, exact tuple, both preceding chains and complete current inventory. Later canonical advancement is verified from the frozen source checkpoint.

Failed writes retain a failed/recovery_required receipt and authentic recovery evidence. No atomic rollback is claimed. Native publisher validation and source completion have distinct recovery scopes. The publisher author owns complete old-subject removal, absent native-generated subject/registry slots, native receipt/policy publication and held-row lineage tests; this source-only packet does not claim those results.

Reusable private fixture API in `tests/test_campaign_owner_apply.py`: `demotion_case(root, *, chain_owner=None, before_status='MAPPED')` and `repin_demotion(root, plan, *, update_review=True)`. The fixture's acceptance is explicitly mechanical test data, not corpus approval. It uses a genuine private Git-published existing-owner origin and separate accepted review JSON. `DEMOTED` is `data/ingredients/unmapped/Existing.yaml`.
