# W04 issue 1239 source-origin correction handoff

This immutable supplement selects one corrected W04 ferric ammonium citrate proposal and retains the complete prior shard: **188 cases, 119 selected payloads, all 115 original proposals accounted**. It succeeds published parent `030ba5a8965bc193955c7c14d125eb098fc56036`, which preserved the original bound source head `548e7bdd0ce2a68b3ae0df6ad7a6150a4e5c9bb9`. Existing branch: `review/all-unmatched-w04-source-review-20261107`. Ordinary publication and final-head attestations are recorded after commit in `.temp/all-unmatched-worker-04/issue-1239-v1/publication/publication-receipt.json`. No maintained application or union acceptance is authorized by this handoff.

The authoritative current selected indexes are below. `candidate-v1/`, earlier native-content drafts, and `finding-lineage.json` are preserved intermediate stages. Use `final-finding-lineage-v1.json` for the completed source-origin review disposition. Select the exact new FAC payload; do not select the old proposal or combine the two.

| Current input | SHA256 |
| --- | --- |
| [decisions.json](decisions.json) | `eb3ef8dc0f05ae11efbfaf476a603be021fb0a4279f480f898d411fc5d2796e1` |
| [proposals.json](proposals.json) | `7c507aa37b0936b628ac2a057eb1067d7a8c12837f4d57c309eebb4461d70ce3` |
| [evidence.json](evidence.json) | `d09155083ed46d9357d7e4976b3e0c77e9b8e5994d351c0812cf54ea978a30a7` |
| [old-proposal-ledger.json](old-proposal-ledger.json) | `9800b60089c1066cc0ee3005adff2baf79272e6a213322a9aaa6f91299ee0af6` |
| [predecessor-proposal-ledger.json](predecessor-proposal-ledger.json) | `e74ef9f6cd49fdcf2da359653fdae01245985e675185663e420558824c79f6fa` |
| [full-accounting-and-review-bindings.json](full-accounting-and-review-bindings.json) | `3c956da1e43d9406c672e9ff26c950397737eb70c096ae80d7b2a5c6949ad88c` |
| [final-finding-lineage-v1.json](final-finding-lineage-v1.json) | `d1e4eb1f57c41d20e0da3b1a11f4efd4e833edc06c2a33e6237901b631a6178e` |

## Exact correction and source membership

New proposal `I1239-P-ferric-ammonium-citrate`: [complete payload](proposals/Ferric_Ammonium_Citrate.issue-1239.after.yaml), SHA256 `90b583b2603fb0d42edb9d15d2342659f4894195bd4389348b6e4f2bedb61762`. It supersedes `FINAL-CHEM-P-ferric-ammonium-citrate`, SHA256 `0ffadb41562f1baedb86136939efaf34a626805f6ce3eb8847bb72a994c95835`. Authentic maintained before-owner `data/ingredients/mapped/Ferric_Ammonium_Citrate.yaml` remains SHA256 `ae646b9c5f3e9c8ec01d939e1b97733259825a14e4a8a03626bc65453035426e`.

Only `synonyms[7].synonym_type` changes to `REJECTED_LABEL`, with literal `FerriSeltz` and source `kg_microbe` unchanged. Active notes explain the primary evidence and continued union hold. One truthful agent-assisted curation event is appended; all 17 prior events and the exact prior notes remain preserved. All other aliases, generic CHEBI:31604 identity, CAS, mapping evidence, provisional role, occurrence statistics, component/supplied-form fields and provenance are unchanged. No medicine owner, formula, components, quantity or role is invented. Current W04 evidence already uses `LLM_SUGGESTION` under #1226; no enum change is made here.

The only changed case is case77 `CM_NAME:83637b465eeb4e8f0203f455ed0e87a88f2463531cf5f294bf72466f46483953`, frozen input SHA256 `2f30f8b09acfab3845f40bf40143c9488d610bb563a3757ccb18e6d5d50e9caf`. Its original two source occurrences remain:

- `CM_OCC:10a83715a587375e54fab948229d33bdf5ad387165a11bb9c8085ec7cfc8ddc9`: CultureMech009649 / TOGOM3209 SL7 solid.
- `CM_OCC:4814cdac28a0b2be2d8e7d9ab95a4b37b4b3fbb2c961e470feeaeb0f5e70f830`: CultureMech009648 / TOGOM3208 SL7 solution.

Both frozen recipes state `Fe(III)NH4-Citrate`, 4.6 µM. Neither names FerriSeltz. This source quantity does not establish a fixed molecular stoichiometry or medicine dose. The other 187 cases and 118 complete selected payloads are unchanged. The original 115-proposal ledger remains 110 named replacements plus five byte-identical retentions, with the same four additional proposals from the previous successor. There are no new owners in this supplement.

## Primary evidence and separate review

The [PMDA September 2024 label](https://www.pmda.go.jp/PmdaSearch/iyakuDetail/ResultDataSetPDF/180078_7290004B1030_1_09), section3.1, identifies a formulated FerriSeltz powder containing 600mg ferric ammonium citrate per3g plus excipients; section19 separately describes active FAC. This supports rejecting a whole-product exact alias. Exact original [PDF capture](evidence/ferriseltz-pmda-202409.pdf) SHA256 `ed32d4c1c55534ae3ebf4eb7e51739d645b751fb63dfe51126c49fc29cb4a98d` and [successful receipt](evidence/ferriseltz-pmda-retrieval-success.json) preserve retrieval start `2026-11-08 07:07:29 UTC` and completion `07:07:42 UTC`. Reuse and current local inspection are distinguished in [capture provenance](provenance/capture-reuse.json). The original failed retrieval is also preserved. No new download or unread paper is represented as inspected.

Root authored this bounded correction. `/root/biological` independently read the complete predecessor, successor, PMDA evidence and both source recipes and sealed [scientific review](independent-review/successor-review-v1.json), SHA256 `e1d8c7ebcfabc46570b87dce4910e9a1b05adb83e2d878eb0a5a5f4025e3282f`; [seal](independent-review/SEAL-v1.json), SHA256 `bf30917a6f1bc9d5da1c788c818ba0b7206a397761675b3c2ca51a3096cec9d1`. Its additive native/maintained-scope review is preserved separately. `/root/assembly_review` independently checked complete case/payload/hash accounting, source membership, history, native controls, receipt integrity and original W07 finding lineage; its package seal is included in the final manifest. The reviewer receipts identify actual scope and corrections to reviewer-side assertions. This one-payload supplement does not claim fresh scientific review of unchanged118payloads; their exact prior sealed reviews remain bound.

## Native checks and preservation

Current guarded serialization, changed-payload closed schema, prospective filename checks, full overlay partonomy and full188/119 structural accounting pass. Full prospective overlay:3029records,119decompositions,746components, zero partonomy violations. Native before/after alias controls and a reverse-type negative control show only FerriSeltz loses resolution; the four metadata strings remain excluded. Independent checks exercised the actual MIM and pinned CLAW policies. All119 payloads have exact schema coverage through this current check plus preserved checks for118 identical payloads; unchanged expensive validations were not rerun without cause.

The unchanged native review helper saved [YAML](../../../../../reviews/structured/20261108T084949Z-worker04-ferriseltz-source-origin-successor/review.yaml) and [Markdown](../../../../../reviews/structured/20261108T084949Z-worker04-ferriseltz-source-origin-successor/review.md). Their exact bindings and successful validate/save/full-check commands are in [native publication receipt](validation/native-publication-receipt.json). Native verdict remains `needs_curation`: an isolated supported proposal is not maintained-owner approval. Earlier native-content drafts and the failed v2 timestamp validation are preserved. The saved review carried a preliminary local LINEAGE inspection time; [additive clarification](provenance/native-lineage-inspection-time-clarification-v1.json) records actual final-lineage inspection during08:49:38–08:49:49UTC, without changing primary retrieval timestamps or the saved pair.

**Preserved native failure:** the frozen duplicate baseline remains exit2 for the earlier retired CHEBI:86477 sulfite family. Its separate explicit one-row proposed data-ledger companion passes the unchanged checker. Neither result is waived or silently relabelled; the canonical baseline and gates remain unchanged. This alias-only delta changes no identifier, path, parent mapping or partonomy input, so those exact earlier results remain applicable.

[Preservation receipt](validation/predecessor-and-w02-preservation.json) rehashes every prior tracked blob, all764 previous-successor manifest entries, and all2399 sealed W02 entries. All16740 tracked predecessor blobs and both sealed bodies are unchanged. No maintained corpus, aggregate, mapping, shared export, code, schema, gate, owner-selection rule or workflow changed.

## Coordinator handoff and retained holds

[Issue1239](https://github.com/CultureBotAI/MediaIngredientMech/issues/1239) / FAC-F01 is corrected only in this exact W04 source origin. The maintained individual, aggregate and SSSOM still carry the old resolving alias. The broader W07 `TARGET-009` union is not terminally superseded or accepted here; the new native finding remains open and related to W07. Coordinator must rebuild its coupled FAC union from the corrected source origins and independently review the complete result. W09 aliases and its source membership have not been imported or approved. The historical191/191 statistics are preserved, not a claim of reviewing all191 members. FAC-F02 remains an optional unchanged metadata typing observation.

The exact coordinator triage handoff remains SHA256 `104fb4aa417c6a49cab0feda1ffcd24526b0868a42af06640729971664a2d9f4`; the live #1226 comment6718777633 is captured. Its stale combined-payload enum concern remains distinct from this already-correct W04 origin. [#1237](https://github.com/CultureBotAI/MediaIngredientMech/issues/1237) Columbia mixed-owner partition remains **BLOCKED_OWNER_CONTINUITY**: nominal Oxoid39g support does not partition the authentic mixed UNMAPPED_0118 owner. No competing FAC union, Columbia bulk merge or guessed formulation was authored.

All23 prior native findings and three observations, source-specific facts/holds, supported/withheld qualifications, provisional-role limits, whole-owner and export holds persist. No paid provider, new external session, GitHub mutation, PR, merge, release or cleanup occurred. After ordinary commit/push and final-head re-review, worker04 returns idle; coordinator owns integration and issue disposition.
