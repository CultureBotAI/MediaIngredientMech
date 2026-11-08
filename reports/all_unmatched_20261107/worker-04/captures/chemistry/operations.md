Chemistry primary-review operations
===================================

Work was restricted to the chemistry artifact subtree, chemistry-prefixed fragments and isolated proposed payloads. No maintained ingredient YAML, SSSOM, publication selector or GitHub resource was changed by this subagent. Git status was checked repeatedly; artifact paths are ignored by the repository and require the parent to stage them explicitly.

Executed retrieval programs are preserved as `fragments/chemistry-fetch.py`, `chemistry-fetch-source.py`, and `chemistry-fetch-targeted.py`. Additional Python calls imported the same capture helper for the exact ontology terms, primary-paper pages, recipe supplements and scanned paper images listed in the receipt files. Each successful receipt preserves requested/final URL, actual access UTC, byte count and SHA256; failed attempts preserve the real error and attempted UTC. Existing files were never assigned a new retrieval date. `functions.web__run` discovery/open results are preserved in the web JSON captures; snippets are discovery evidence unless a primary source was separately inspected.

Actual access failures and limitations:

- Initial un-escalated curl requests failed DNS resolution under the restricted network. Public read-only retrievals subsequently succeeded through the auto-reviewed network escalation. No rejection was bypassed.
- The MediaDive `/rest/compound/<id>` endpoint returned HTTP200 with an application error `WrongCall`; these responses do not provide chemical metadata. The supported public ingredient HTML and solution endpoints were then used.
- Several TOGO requests timed out; the exact failed URLs and attempted UTC are retained in the source/targeted receipts. Available original DSMZ, NBRC, CCAP and JCM providers were pursued. An unsuccessful request is not evidence that a medium or substance does not exist.
- OLS searches for D-glutamate and ardacin B returned HTTP500. Exact D-glutamate ontology content was later captured directly. Grisamine and actinomycetin searches did not establish a unique small-molecule identity.
- JCM201 and JCM401 HTML returned `Nothing found.`; these captures are classified as unsuccessful searches. The independent reviewer subsequently recovered a JCM401 PDF through DSMZ bacmedia and supplied its original receipt.
- The actinomycetin PDF endpoint returned HTTP200 HTML rather than a PDF. Original scanned pages101–102 were instead retrieved from the public PMC page-image links and visually inspected. Lee2009 EuropePMC XML returned HTTP500, but full PMC HTML was retrieved and Table4 plus the relevant methods were read. Klein1979's public publisher landing page was accessible; its linked full-text endpoint returned HTTP403.
- The first packaging run failed because the receipt glob omitted `final-targeted-receipts.json`; the glob was corrected to include every `*receipts.json`. No missing access timestamps were invented.
- Shell startup repeatedly printed a pyenv rehash warning because the global shim directory is not writable. The frozen Python3.13 environment was used successfully with `-B`; no global environment was modified.

Read-only checks used `rg -uu` for record/identifier and stock duplicate searches, including ignored files. The current owner snapshots include complete histories and properties. Full assigned frozen cases and full recipe snapshots were parsed and hash-checked. Sibling frozen F/2 stock evidence was inspected only as a comparator, without claiming its source case.

`fragments/chemistry-package.py` packages the authored `chemistry-review-spec.json`, true retrieval receipts and exact current owner bytes. `fragments/chemistry-validate.py` verifies all74 cases, source fields, occurrence IDs, owner/capture hashes, proposal backlinks and YAML parse integrity. Its final output is captured in `fragment-validation-final.txt`. The parent runs the whole-shard structural auditor and native strict schema, OAK and partonomy checks. Separate biological-agent skepticism is required before any final disposition is independently complete.
