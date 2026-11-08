The maintained `data/normalized_yaml/algae/hsm.yaml` contains an ingredient token `Sterile` with concentration 1%. In the original [CCAP HSM formulation](https://www.ccap.ac.uk/wp-content/uploads/MR_HSM.pdf), the phrase is the heading **Sterile 1% Marmite solution**, followed by the stock preparation and its 1 mL addition. `Sterile` is a preparation qualifier, not a substance.

The primary PDF captured during the authorized MIM all-unmatched campaign has SHA256 `8160988acfb8d06ce0b7f6c7e930372d4c953b779607bcfdaf8d730b64b9613b`. The current `main` recipe was retrieved on 2026-11-08 and has SHA256 `8e23a83a001ba7d86f7e67eee0566d96d9f935ef1efaa38799c6de0b8fc33d92`.

Follow-up: restore the source-defined Marmite stock structure and its preparation/addition relationship; preserve the raw malformed token as import provenance rather than requesting an ontology identity for `Sterile`. Verify concentration basis and final-medium addition against the primary PDF. No CultureMech or MIM maintained data was edited by this source review.

The source-specific decision is retained in MIM worker03 case `CM_NAME:4ba585285bcf878810bd999f17ae1e57a8b19c653af064c1b7c1ef86aef7e33e`, with separate skeptical review, under `reports/all_unmatched_20261107/worker-03/materials/`.

Deduplication: all-state indexed searches for Marmite, Sterile plus Marmite, and hsm.yaml returned no issue/PR match. #273 and #387 concern previous preparation/parse cleanup but are closed; this exact residual is still present. #408 concerns the different volume-unit substitution defect and is not duplicated here.
