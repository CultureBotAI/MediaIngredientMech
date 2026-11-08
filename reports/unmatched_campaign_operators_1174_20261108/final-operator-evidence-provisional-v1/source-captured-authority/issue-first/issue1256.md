The private bracket fix closes the two original one-way mutations, but an independent actual-native probe found a narrower within-observation mismatch at source `adba0b6b…`.

Both full index snapshots contain the same invalid blob. Between those observations, real Git writes temporarily restore the accepted index while the separate cached-path/entry/blob checks run, then restore the invalid blob before the final snapshot. Both the unrelated-contract and planned-owner variants return `complete`; no mutation occurs after the final read. A clean control succeeds, and leaving the invalid blob visible throughout correctly refuses.

The bounded fix should validate the captured stage/path/mode/blob snapshot itself, or prove every validated subview equals that captured view, then recheck the final logical snapshot. Preserve stat-cache refresh, legitimate installed staging, literal paths, and historical completed verification after later commits. This does not request global atomic protection or a current-index requirement on historical replay.

Native functions/results were not replaced; the probe only schedules real private Git index writes. Source payloads, maintained checkouts and scientific approval are untouched. Exact original/final snapshots, receipts, probe and source hashes are retained in the independent packet. Finding `IR-INDEX-COHERENCE-001` is a continuation of `W08-7D4DB26-SRC-001` under #1256, not a new unrelated issue.

Filed before the successor correction. The private bracket-only attempt was not committed or applied to campaign owners. Its84 partial source-test passes and deliberate interruption are preserved separately; they are not a full-suite result.

Independent packet: `.temp/all-unmatched-20261107/preflight/index-coherence1256-private-independent-v1/portable/`. HANDOFF SHA256 `14ee94bcc40808fd02e76bb25fabccc2ca729fee668b9325317d802387871573`; MANIFEST `ff24de5e0ce8480e52177837ce6068fa4e08b508e4afd5ddabee38fa37548c15`; FINDING `0894edfa518f009e9c8f4f39ee8f894a9642015dc5e7db4ba4b5a3e72f033753`. Root rehashed all37 declared members before this comment. Original7d4/21061 reports and all earlier failed attempts remain unchanged.
