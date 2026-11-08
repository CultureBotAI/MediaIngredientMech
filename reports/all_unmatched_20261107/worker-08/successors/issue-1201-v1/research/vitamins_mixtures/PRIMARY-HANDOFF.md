# Vitamin and mixture issue1201 reassessment — frozen primary v1

All 26 prior no-proposal cases were re-opened against their complete frozen cases, full recipe snapshots, original primary captures and ignored-inclusive owner catalog. `reassessment-ledger.json` accounts for every case. `decisions.json` contains 26 successor decisions; all require independent review.

The bundle proposes 14 isolated payloads for 10 cases: two JCM top layers; the NBRC1356 mineral-base1 supernatant; partial TOGO M2567 mineral bases A and B; JCM1023/JCM903 vitamin stocks; JCM554 SL10; three NBRC vitamin formulas; an extended existing NBRC1356 nine-vitamin proposal; Gibco11120 MEM100X vitamins; and JCM510 methane-air blend. The other 16 cases have explicit remaining source requirements. The reviewer should challenge whether the carrier-unknown B12/K1 stocks support additional source-qualified partial preparations.

`vm1201-prop-nbrc-common9` supersedes `vm-prop-new-60`. Its original case `CM_NAME:6fd34e4bc1aee4bbad6880aa32d6415080fef7455f1e630a2afe26cb815ebe51` must also receive independent review and a metadata-only backlink update. Original common9 ingredient identity and component payload are preserved; six additional NBRC source recipes provide matching formula provenance. See `original-case-backlink-remap.json` and the complete primary comparison capture.

Frozen hashes:

- Decisions: `752ed322f143b2d487dd789c74b69f19cc6abc2ba7dba9f34d921e43282f42ed`
- Additional evidence: `234cb51be06635749674a84c0a6ac3ac6aa492d87053828330d1094b2bb681a9`
- Proposals: `b7f6677eadb86335b2055f1b32201a80ced2753afdd1e6ca167152771e68ad7b`
- All-26 ledger: `73a8a1a1becc8ddd32c8c69e245bfd22fee597f1dd01050294b17e9686216b79`

`validation.json` records passing strict/schema checks, full-catalog partonomy and structural accounting against a private combined overlay of 188 cases and 59 proposals. Three malformed-input controls were rejected. All 15,088 blobs from published commit `7efd3f8b98f9e822431dcb510c2c242a2569cfc7` remained unchanged. The overlay is validation input only and does not replace the coordinator's integration.

All payloads were written through `write_validated_ingredient`; new history events use `record_curation_event`. Capture paths are relative to the original worker08 artifact root. Existing captures preserve original retrieval times; new publication captures contain bounded factual extractions. No maintained data, roles, source holds, exports or SSSOM rows changed. Registry proposals still require content-bound admission and cross-shard reconciliation. No merge, rebuild, commit, paid research or external session was performed by this subagent.
