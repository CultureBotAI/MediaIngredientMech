Worker03's source-review lane identified and corrected five proposal/review defects before the final frozen handoff. This tracker records their exact scope and separate re-review; the maintained-owner defects have their own issues below. No maintained ingredients, canonical exports or release selectors were edited.

| Finding | Correction verified in isolated artifacts |
| --- | --- |
| B-M1 | Source-defined liver/Columbia formulations and identified products were initially deferred for unrelated supplier/species gaps. Concrete source-bounded proposals and targeted catalog evidence now replace those generic deferrals. |
| B-M2 | Difco Marine source530 identity was initially called unresolved solely because current owners need reconciliation. The final decision separates source identity support from the outstanding owner-integration obligation. |
| C-B1 | Ten new registry-stock intended owner filenames differed from their identifiers' suffixes. Corrected exact paths now match the retained stock identities. |
| C-B2 | Available original-source leads had not been followed for six cases. The author pursued the primary chains, and the reviewer checked the resulting captures. JCM826's literal sulfur formula and technical-product composition remain unresolved where the primary source itself is insufficient. Resorcinol's unverified historical recipe lineage/dose is not claimed as a confirmed quantity defect. |
| C-B3 | Alias provenance and combined web-evidence entries included incorrect source attribution; one PubMed result was unrelated, and new-owner history claimed a nonexistent prior MAPPED state. Corrected entries bind the actual sources; the unrelated result is retained as unsuccessful research and creation histories no longer invent a prior status. |

These distinct findings are resolved **in the isolated proposal/review lane**. Separate reviewers inspected the corrected bytes:

- `materials/independent-review-of-broths.json`, SHA256 `3846ffd9725a4885003a5977d26cfddbde95e68f55d266c3f08afdc6668204c8`: all 86 broth cases and 20 proposals.
- `broths/independent-review-of-chemicals.json`, SHA256 `27b2531af69f9db9d2301d6183ed5ad0669e1229b0c279814e1d37de9d6e9605`: all 51 chemical cases and 34 proposals, including the completed primary-source followups.
- `chemicals/independent-review-of-materials.json`, SHA256 `538eaf7b66609279db6e4d6544b53d4a87a3aa469fab256bfa81dc1fcbde70af`: all 51 materials cases and 20 proposals.

Paths above are under `reports/all_unmatched_20261107/worker-03/`. Each review binds its exact author/core hashes and every final proposal payload. The frozen shard SHA256 is `90d5d5df1ae9609c08593c93216d78449f6ac2781f1d5e7e95695751fdd0c228`; the assigned base remains `e000d66dd26ab053e9b17ce7bf8d3c873c3dde99` with unmerged dependency #1158.

The later coordinator-observed JCM431 pointer miss, `M-JCM431-POINTER-1`, is tracked under existing #1173's `IR-SHARD-ARTIFACT-9` and #718 rather than duplicated here. Its earlier review and proposal bytes remain archived, and the amended independent materials review explicitly supersedes the missed alias approval. Source-local routing remains separate from a globally resolving synonym. The coordinator must reconcile worker01 and worker03's complete payloads and case sets; no winner is selected.

Confirmed maintained-owner findings: #1182 (BD211065), #1183 (molasses), #1184 (PHB), #1185 (neutral citrate hydrate aliases), #1186 (oxygen-free source formula on sulfate). The HSM extraction defect is CultureBotAI/CultureMech#676. The known TOGO volume-unit issue remains CultureBotAI/CultureMech#408.

Follow-up: use the final worker03 handoff and content-bound independent reviews to reconcile overlapping proposals, then apply only reviewed nonconflicting changes through guarded writers. Existing native holds, changed-owner full-payload review and new-owner admission (#1165) remain required before export. No case-review, schema or structural PASS is a release approval.

Deduplication: the live all-state indexed search for worker03 spellings and representative finding IDs C-B2 and B-M1 was inspected. The five newly filed owner issues concern different maintained defects; no existing dedicated worker03 proposal-review correction tracker was found. Full search responses and exact review captures are retained with the handoff.
