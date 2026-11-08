Independent adversarial review of the new #1174 source-application operator reproduced a late-membership omission in `verify_completed`. This concerns a provisional implementation snapshot, not released code or actual campaign data.

Affected source: `src/mediaingredientmech/curate/campaign_owner_apply.py`, SHA256 `74a448602d8d512a1b12037d88d0eba0a9ac9e1ea55c89e6bd3051afb23f0a99`.

The verifier enumerates direct owner files before `_validate_records` and native checkpoint replay, then rechecks only the file objects already captured. A new direct ingredient YAML introduced during that work is absent from the final inventory proof.

The independent deterministic private fixture first completes a real mixed edit/create/promotion application. Its unchanged positive returns a complete four-owner proof matching the actual catalog. The negative adds `data/ingredients/unmapped/Unexpected_late.yaml` after the initial inventory and before intervening validation finishes. `verify_completed` still returns complete with four owners, although the actual direct catalog contains five. The probe changes only private test fixtures.

Retain and re-enumerate complete direct owner membership at the final verification boundary, and apply the same current-byte/location guards to all members. Audit historical snapshot membership and required absence claims at corresponding late boundaries. The canonical/policy publisher must also recheck the full membership it relies on before returning its final proof. Do not weaken assertions or substitute count-only checks.

Add regression tests for the real late-addition counterexample, late removal/path alias as applicable, and an unchanged positive. Preserve the failing evidence and obtain independent re-review of final bytes.

Finding ID `IR-CAMPAIGN-OPERATORS-1`; finding JSON SHA256 `8ae45b2b99a3da3010ebd76afc2e6ce3c01797188905d6ec95b89715f4126e84`; probe SHA256 `42b565843e64c9da1a0712acec053f3c038d7c7d45ed2b6ccfb597bb4c4df4d5`; result SHA256 `783a5bd8416493e27bf2d66295eb1af98f55a1a520becf7b9669c60865abd9d4`. Evidence will accompany the implementation PR.

Deduplication: the current all-state campaign/owner issue search and full issue snapshot were checked. #1174 is the parent capability task; #1161 fixes evidence-path substitution in the separate accounting observer, and #1162 fixes inventory count definitions. Neither covers this newly reproduced completed-source verifier omission. No production write exploit, scientific approval or mapping defect is inferred from the fixture.
