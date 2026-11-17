# Reviewed CultureMech v3 source intake — 2026-11-17

This is the separate intake requested by [MIM1453](https://github.com/CultureBotAI/MediaIngredientMech/issues/1453), implemented in [PR1460](https://github.com/CultureBotAI/MediaIngredientMech/pull/1460). It preserves the active campaign's frozen inputs. It does not publish a new global SSSOM release, repair upstream scientific records, or install mappings in KG-Microbe.

The producer scanned all 15,915 normalized records: 209,330 unchanged base occurrences plus 454 variant occurrences, 2,565 positive inventory groups, 492 change events and 138 explicitly held mentions. Its seven products preserve direct structured ingredients and the reviewed variant-prose queue. Referenced-stock expansion and unreviewed prose are not inferred as additional chemistry.

All 5,007 source cases have explicit dispositions. The 797 cases with a supported native canonical row received authored scientific binding decisions; 623 are supported and 174 are withheld on concrete source/form/preparation grounds. The remaining 4,210 cases are withheld by the unchanged native canonical gate. A supported identity binding does not certify source quantity, growth, variant physical presence or complete preparation equivalence.

| Source membership | Supported identity binding | Withheld identity binding | Total retained |
|---|---:|---:|---:|
| Positive inventory occurrences | 16,732 | 193,052 | 209,784 |
| Context-only removed/replaced-old descriptors | 30 | 133 | 163 |
| Quarantined source held mentions | 2 | 136 | 138 |

The two held mentions with supported identities retain their QUANTITY/OPERATION holds and create zero positive occurrences. All other held dimensions remain explicit; overlapping dimensions must not be summed as separate mentions. [The exact accounting](final-accounting-v3.json) verifies these totals against the pinned source intake and includes every finalized product hash.

| Artifact | SHA256 or immutable commit |
|---|---|
| CultureMech producer | `6f1b1d18a5528532fa239400bd73c1a040fb78a0` |
| Producer bundle manifest | `ede822e6424433644ae25f363cb5bfb88b154b453c1e954185ecc2c6cb3c829f` |
| Original accepted handoff | `c011b4b6a2d4210c7ed0fb9dd0456f7e436e156f7aedb55dd6f4af5a12b34bfb` |
| Frozen prepared intake | `6bcc92540daba081d8180346d135c2ae40471c9fb0a7005b46aa5c9902d684f7` |
| Complete source review packet | `8fa677ea9ed591941564c24d4e190e943f6bb84f22f03f909342c58cf3617760` |
| Final binding review | `b548dbcb6271f59083693da632a2318bfbbf868b5b2a208e86a77bb4ae77fa4a` |
| Reviewed intake receipt | `9fd1da62fad47c3b5b7290ea3f9fc2b687b23fc8c98e8dc926e1460572c3f1d8` |
| Exact membership accounting | `980e6c022bcea13b4d5ac21aac621d6bfa30e685b566ea3938c02378dbf83380` |

The final [binding review, evidence and eight unchanged author snapshots](final-source-binding-review-v3-r2/) retain complete-case hashes, all supported scientific payload hashes, and actual inspected member/field witnesses for each authored hold. A single blocking witness can quarantine a whole unchanged case; that does not claim unread payloads were reviewed. Every author slice has an immutable native YAML/Markdown review. The bounded independent cross-reviews preserve their exact sampling limits, including [the two narrative corrections](root-second-provenance-review.md). Superseded observations remain available in their earlier immutable pairs.

Native SSSOM export retains 1,739 supported and 1,275 withheld mapping rows from the September21 content-bound review. Supported SSSOM SHA256 is `7e68fea7fd788928f29c7671156198af101baaa3b3051f19bab78a5479d2a940`; withheld SSSOM is `5817fb845c65f995fb0c78095168af1cbf0c837a991004fcd0a9d73cd0874c88`. Native SSSOM parsing/schema QC passed and its receipt is preserved separately; these unchanged canonical rows are distinct from the 623 supported source-binding cases.

The [strict QC JSON](final-native-sssom-schema-qc-v3.json) has SHA256 `ccf9f6e21a2486c666610b7a2f182b2e024cf73597f2eea8981ad539b535f2e3`. The [original raw stdout log](final-native-sssom-schema-qc-v3.log), including all six extension-field warnings, retains SHA256 `f13e28e14aa46d68ca38705ead6a89f40cd3ab1383e48966b146a45e9e5cd2c0`. [The serialization receipt](qc-serialization-receipt-1540.json) records the exact extraction and unchanged parsed native result. Issue1540 corrected the earlier mixed stdout file labeled as JSON; it changed no scientific or finalized intake bytes.

Review findings affecting implementation/proof were addressed:1459,1461,1462,1465,1467,1530,1535,1536,1537,1538,1539 and1540. Scientific source and canonical follow-ups remain open where their exact cases are withheld. In particular, CultureMech792/793 and other source identity issues do not disappear when an intake is completed. Quantity findings794,799 and800 remain outside identity approval. All exact issue/evidence locators are retained in the case decisions rather than summarized as blanket approval.

The complete source bundle, original producer archive, prepared packet and finalized tables remain immutable local delivery artifacts. Reproduce using the committed assembler/finalizer and the [isolated verification procedure](../../docs/culturemech-source-intake.md#isolated-verification-package). The package receipt independently identifies the committed consumer used for replay. Delivery receipts belong to that package checkpoint and must not be confused with a later documentation-only PR head.
