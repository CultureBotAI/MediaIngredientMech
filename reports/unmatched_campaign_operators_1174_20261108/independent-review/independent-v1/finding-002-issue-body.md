Independent adversarial review of #1174 reproduced false producer provenance in the provisional source operator. No maintained ingredient or campaign data was applied.

Affected source: `src/mediaingredientmech/curate/campaign_owner_apply.py`, reviewed SHA256 `74a448602d8d512a1b12037d88d0eba0a9ac9e1ea55c89e6bd3051afb23f0a99`, `_load` producer verification.

At preparation time the operator reads producer bytes from the package directory and compares them to the application root. Both reads inspect the current disk bytes. A long-lived process that imported version A can therefore accept a plan bound to later version B while still executing A.

The private deterministic probe imports the frozen implementation, appends a harmless identifying comment to that private source file, and builds the test plan from the changed file. `prepare` and dry-run application accept even though the known imported source hash differs from the accepted producer hash. The unchanged positive remains valid. The probe modifies only a private fixture and performs no owner application.

Bind the loaded implementation and relevant imported dependency bytes and file identities at import time. Compare accepted producer pins to that actual loaded snapshot at preparation and late boundaries; refuse stale imports or substitutions. Add regression coverage for the reproduced stale-import case and an unchanged positive. Preserve existing plan, receipt and scientific-approval restrictions; obtain independent re-review.

Finding `IR-CAMPAIGN-OPERATORS-2`; finding SHA256 `4b4063a784418cfc8ff3f159c83f143396b15b3571b46be04b7263381aba8e47`; probe SHA256 `b0941a51cc8169d904bf52872b5221115f6ffb0cd151c7eca405e3e9281f90d6`; result SHA256 `30e6a03adcb0a4c7acd048d4b75a61b7ca5664b8954b65330dbc6290169508a2`. Evidence accompanies the implementation PR.

Deduplication: the live all-state loaded/producer search returned no issue. #1174 is the parent capability task; #1194 concerns late catalog membership, a separate reproduced boundary. This is false provenance acceptance, not a claim of actual scientific-data corruption or a production exploit.
