# Independent correction review — #1535 / #1536, 2026-11-17

Read the complete unified diff and correction helper for the successor of the second scientific slice. The predecessor is `a309fe8b6a841afea0d0b4463a205fe322a2722fced2797930bd0cbfe815791b`; the verified successor is `b846c03927bd2d0e5e09bbb4b6911295761c4e11f743c1e223d67bd5eac731ef`.

The diff changes exactly two narrative fields. Scientific dispositions, review reasons, inspected payload sets, case hashes and canonical row choices are unchanged.

- For sodium chlorate case `b198a7c5e3164e5112e16cb10007008ceb321feeff7a7c4bc2f2dcad109d6e3d`, independently read the complete descriptor in owner273. Its actual key is `d300b6526d61bfef904b8c9ca20b96a7c020a0bb686b85b9f007dc74079a07f8`, agreeing with the repaired evidence locator. The descriptor explicitly names sodium chlorate with CHEBI:65242.
- For sodium sulfide case `d0c8d3c8ab968b81703d7291e78c7bbb018c735fd3e2cd11b342b18b11d1be20`, independently read the complete blocking descriptor `c51054cca36e6a38a39f35805ff8a40060d922a22aa5f7b78988ff6d6906217c` and candidate in owner270. The literal KOMODO snippet states sodium sulfide hydrate. This descriptor has no term or MIM-derived-term field. The selected candidate is CHEBI:76208; the corrected witness reason now attributes that identifier to the candidate rather than the descriptor.

Result: both provenance findings are addressed; the successor is cleared for final assembly. This is a narrow correction review, not an independent reread of all 143 source cases. The predecessor and its native review pair remain preserved.

Also independently reread the #1538 package fix and real extracted-CLI regression. Bytecode suppression precedes the native imports; the subprocess test removes ambient PYTHONDONTWRITEBYTECODE and checks that no unmanifested __pycache__ appears. The reported seven package tests passed. No additional material issue found in this bounded implementation review.
