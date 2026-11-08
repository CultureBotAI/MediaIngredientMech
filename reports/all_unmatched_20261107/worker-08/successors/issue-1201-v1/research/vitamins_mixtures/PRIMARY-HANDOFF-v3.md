# Frozen primary successor v3

Use `decisions-v3.json`, `evidence-v3.json`, `proposals-v3.json` and `reassessment-ledger-v3.json`. Earlier v1 and v2 files remain unchanged.

All 26 cases are reassessed. There are 21 isolated proposals and 31 additional evidence entries. Seventeen cases have directly supported preparation or existing-owner provenance curation. Two cases have comparison-only links to the JCM515 stock: the NBRC 0.002% B12 cohort and TOGO M498 2 mg/100 ml. Those links do not establish stock equivalence or source membership. Seven cases retain specific no-proposal holds.

Independent findings addressed:

- **VM1201-F1:** Added six partial stock proposals without inferred solvent, vitamer or percentage basis. Equal nominal strength permits comparison only.
- **VM1201-F2:** Corrected the NBRC824 processing claim. NBRC1020 filters its vitamin stock; NBRC824 includes vitamins before receiving-medium autoclaving. Their enumerated input formulas match, without a claim of identical processed media.
- **VM1201-F3:** Retrieved the actual cited CultureBotHT Mixes sheet and compared the recovered TOGO LS4D formula. The sheet supports the existing cyanocobalamin component. The Thauer proposal changes only notes and history; it preserves components, assertions, aliases, counts and roles.
- Normalized prose spacing in 19 payload successors, preserving identifiers, component names, quantities, units and prior history. The exact old/new captures are recorded in `primary-remediation-v3.json`.

The common nine-vitamin successor still replaces `vm-prop-new-60` and retains its original case `CM_NAME:6fd34e4bc1aee4bbad6880aa32d6415080fef7455f1e630a2afe26cb815ebe51`. Independent review must cover all 26 cases, that original case's backlink, and all 21 exact payloads.

Final primary hashes:

- Decisions: `df7d929bd321a4f6cbf3e2fb5262c07ba9d8c53aaf983eb5ebc4f7a61c41bfb6`
- Evidence: `7d946d7c919336b6fd44a0b72e3c53ce141e81c2675db55333408682d2f8253c`
- Proposals: `19472e837f51117a33e6168cc066d6c3b1d92a31dc3ce79dc1d9414ad3a3b53f`
- Ledger: `e348266e138660794fbc5a97894f73d72046a15a1d659256a121038e7a0070d8`

`validation-v3.json` records passing schema checks, native partonomy for the 66-proposal private overlay, whole-shard structural accounting and three rejected malformed-input controls. All 15,088 published predecessor blobs remain unchanged. This validates the artifact structure; scientific peer review and coordinator admission remain separate. No maintained data, source holds, roles, exports or SSSOM rows changed.
