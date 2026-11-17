# Independent source-binding cross-review — 2026-11-17

Scope: CultureMech intake #1453, PR1460. This is a bounded independent review, not a claim to have reread every source payload in the middle slice.

Intake SHA256: `6bcc92540daba081d8180346d135c2ae40471c9fb0a7005b46aa5c9902d684f7`.
Packet SHA256: `8fa677ea9ed591941564c24d4e190e943f6bb84f22f03f909342c58cf3617760`.

Read all 216 scientific disposition reasons in the original `middle.json`, in three complete pages of 72. Independently read every scientific descriptor and complete current owner, including history, for these five preparation cases:

- Owner159 Glycine-NaOH buffer, case `0ea6670d447a141e35c7f28201c47b7f07405b51605b14a6b2ca65cd7d3f1f5a`, two descriptors.
- Owner183 K-phosphate buffer, case `82d0141603f9cb24e01a6f12f6404ce7621e5e8a29e279e2c42713d44f04262a`, two descriptors.
- Owner213 MES buffer, case `656841db39b55b10a3012695b543b23950119854fd8619ecd95016f161fea063`, three descriptors.
- Owner313 Phosphate Buffer Stock Solution, case `10c3eadcbf9a47bf71a5c39bad25e3a74ff63126c1f9fcd7ec28c2a9ee89f05e`, one descriptor.
- Owner348 Salt Solution II, case `624c1392d542ba666613a7348e44a31e22ecfe2dbece0fdf282a011ebf356c8a`, one descriptor.

The first three were independently identified as unsupported preparation equivalences. The original reviewer checked analogous cases and identified the latter two; this reviewer then independently read their complete scientific payloads and owners. Shared labels and numeric suffixes in different MediaDive namespaces do not establish identical stock preparation. The MES source also contains an acid annotation and simple-compound description, while the owner expressly distinguishes a prepared stock from pure MES. Owner313 explicitly distinguishes its unidentified preparation variant from a generic phosphate-buffer class.

The finding is recorded in MediaIngredientMech #1485. All five now have concrete, payload-pinned WITHHOLD witnesses. Independently read the revised reasons/witnesses and verified these successor file hashes:

- `middle-v2.json`: `39beb1f9128a734ff08463d04ed7a9beaf8f724733d5a9542be93646b9a87f60`.
- `middle-extra-v3.json`: `d742b7add9dae24d2336c9acd2366caefc69a75d13122ecbcf6eb6df16a17b18`.

Also read the complete held scientific payload for owner109 case `59f0064aa440bbf726708377040575f2a00638adafe8723dd0f3ded078bec642` and the current owner identity/evidence. Supporting the explicitly defibrinated sheep-blood identity is consistent with preserving its QUANTITY hold, zero positive occurrences and separate replacement event. No numerical equivalence between the conflicting dose reports is approved.

Residual quantity/metadata observations in the original reasons were referred for explicit issue tracking: EDTA charge-specific chemical properties; DMSO 1000% volume fraction; and diethyl-phosphonate percentage/mass representations. Those observations do not confer quantitative approval or alter this frozen source.

Additional pass: read all 90 disposition reasons in `middle-extra-v3.json` and all 26 in `middle-late.json`. Independently read the complete owner314 held PIPES case `730bf2620791610200e50d3a41a44a81d59575bcf87c5997180ee2b36d18a1d7`, including witness `be0c4fa6954a08e17723bac8b9ea3abe36d8c43bc621153c3be500d032b61ce4`. Its SOURCE_CLAIM hold explicitly concerns the unavailable Hartzell preparation; the corrected WITHHOLD disposition preserves this gate. The source-specific Reed preparation cannot supply missing evidence for Hartzell. Also read the complete owner109 history; it supports the distinct defibrinated preparation used in the quantity-only held case above.

N2O gas mass-per-volume and the recorded extreme pyrrole-2-carboxylic-acid quantity were referred for inclusion in existing quantity follow-ups, without changing source identity approvals or frozen source bytes.

Result: the five material preparation findings are addressed in the successor dispositions. No remaining blocker was found within this bounded sample. All other middle payloads remain the original reviewer's responsibility; their full coverage assertions are checked separately by the assembler. Native finalization, replay and product hashes remain required.
