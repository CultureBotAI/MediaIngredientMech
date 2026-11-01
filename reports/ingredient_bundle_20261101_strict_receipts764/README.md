# Strict-receipt companion dependency refresh

This immutable successor advances only the complete base mapping-review hash after the #764/#766 strict receipt port. The maintained `scripts/refresh_unchanged_cohort.py` verified the prior review and its inputs against merged main `7a06935dceb6ffc4ccccc1a1693e01f2950a8601` before producing `review.json`, `dependency-refresh.json` and the exact `prior-review.json` copy.

All 20 owner records and 51 complete claim decisions are unchanged: 20 mappings, 18 identifier assertions, three products and ten occurrences. Fifty decisions remain SUPPORTED and one remains WITHHOLD. The existing invalid Lysozyme CAS claim stays withheld. Canonical SSSOM, its date and semantic metadata, scoped claim payloads, evidence, schema and profile are unchanged. This operation confers no new scientific approval.

The exported bundle passed the native validator with manifest SHA256 `d958f6d359f18ae407024eaf4e1e0ae22dc87fe9076cad78233d0c29b8bf9d5c`. The four-class execution comparison includes this actual successor, alongside every mapping, assertion and finding disposition. Source, output and command evidence is retained in the [strict-receipt execution report](../strict_approval_receipts_764_20261101/README.md).
