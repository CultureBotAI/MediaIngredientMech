# Strict mapping receipt port

This is the #764/#766 replacement on the #817 exact-byte approval model, based on merged main `7a06935dceb6ffc4ccccc1a1693e01f2950a8601`. Receipts establish the history needed to withdraw an old approval; they never renew it. Changed owner bytes require fresh scoped scientific review. Section-refresh receipts remain audit-only.

The common receipt verifier checks the complete ordered inventory, row operations and replay, exact owner-byte links, and the maintained receipt-11 checkpoint for the resolved negative hold. The semantic gate independently recomputes these proofs and requires both implementation modules even when there are no receipts. Mapping-edge identities retain the native eleven-field payload and pipe escaping (#765).

Independent review findings were filed before repair:

- #1063: reject undeclared removals, invalid/boolean positions and conflicting row operations.
- #1064: compare the explicitly selected companion successor as well as mapping, assertion and finding decisions. The earlier incomplete diagnostic remains historical evidence.
- #1065: reject a held owner's change-and-restoration after the fixed checkpoint. Unrelated-owner changes and exact no-op links remain valid.
- #1066: preserve each archived identity/role pin's own evidence; refuse duplicate owners within an identity archive and duplicate source positions within either positive mapping cohort. Valid overlap between separate archives remains supported.
- #1067: migrate the reduced carnitine consumer fixture to the complete native receipt contract, preserving its withdrawal and unchanged-owner controls and adding missing-field refusals. Production validation stays strict.

The regenerated canonical source remains byte-identical: 2,981 rows, of which the reviewed export supports 1,739 and withholds 1,242. The supported graph has 2,151 approved edges and preserves 2,335 unapproved edges separately. The complete semantic report passes integrity validation but retains its FAIL verdict, 1,732 blocking findings and 2,335 blocking assertions. This infrastructure port makes no scientific decision and adds no mapping-change receipt.

The native composite QC and product gates pass. A supplemental invariant run uses the actual read-only KG-Microbe ontology transforms at `d6baf5b90003a2032747559d94c00f86a7a4c615`, with unchanged before/after file hashes and checkout state. Its reject table has zero data rows. Rule B4 remains unavailable for one BTO row and 73 MICRO rows. The original auxiliary physical-line counter included metadata; its appended CSV-based correction and the original result are both retained.

The [companion dependency refresh](../ingredient_bundle_20261101_strict_receipts764/README.md) preserves all 20 owners and 51 claim decisions (50 SUPPORTED, one WITHHOLD). The maintained [comparison](compare_dispositions.py) verifies all four decision classes and the unchanged source inventory against a hash-bound baseline. Native bundle validation remains a separate required check; comparison is not approval.

The original #764 branch, historical receipts and reviews, ingredient records, canonical mapping, unified snapshot, validator pin and evidence workflow are preserved. This is a standalone approved-plan execution with no supervisor binding or goal/cycle advancement.
