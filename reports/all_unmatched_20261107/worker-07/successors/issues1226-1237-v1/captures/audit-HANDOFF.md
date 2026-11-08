# Frozen campaign evidence-provenance audit

**Finding: 697 new agent-authored mapping-evidence entries across 646 frozen proposals use the human-supplied evidence type. One additional changed historical entry remains ambiguous.** This is a provenance finding, not 697 chemical rejections or approval of the mappings. It belongs to existing [issue1226](https://github.com/CultureBotAI/MediaIngredientMech/issues/1226), including W08-IR-001. No issue or comment was written by this audit.

All output is confined to this private directory. Worker02 head `0597d00417be4d7cdfb5a31970043eec9bbc88fe`, its published artifacts, maintained ingredients and the complete sealed BSA packet are preserved. No candidate writer, payload correction, schema/gate change, source selection, corpus edit, GitHub/Git mutation, merge, export, new external session or paid provider was performed.

## Exact denominator and result

The scope is the immutable `preflight/final-intake-candidate-v1/HANDOFF.json` and `all-active-proposal-entries-v1.json`: **981 proposals**, comprising 631 new owners and 350 existing-owner edits. The intake SHA256 is `686f9cc38f17e00c0dde9b0af1a634090b1ad3896c2b539f265163f5731a5814`; handoff SHA256 is `2c2efd62124fcb7c0eaf406a85ad6b1ac386a07d5afce6aa8a2714bdf1ce808b`. All ten frozen origins remain selected, including provisional W06. Later W06v3 and W07 lineage heads are not selected or silently substituted; no later-head delta was needed to answer this frozen audit.

Research B verified every exact before/after byte pair, committed payload/core-ledger origin, case/evidence projection and full record field difference: 981/981 passed, 30 core ledgers and 1,329 actual input files checked, with 8,252 field-diff operations. The skeptical reviewer independently recomputed the 981 pair hashes and evidence deltas without B's helper. Exact-path absence for new owners is not a semantic duplicate search.

| Mechanical category | Entries |
|---|---:|
| Added/changed complete mapping `MANUAL_CURATION` objects | 698 |
| Proposals containing those objects | 646 |
| Exact historical mapping objects retained | 29 |
| Old complete mapping objects removed | 4 |
| Separate component `MANUAL_CURATION` additions | 2 |

The duplicate-aware full-value delta matches the preliminary list exactly. Changed notes count as an old-object removal and new-object addition; unchanged entries remain inherited even when positions could move. Parent context is checked separately. No exact reordering, duplicate group or mapping-to-component move occurs in this snapshot; meaningful tests cover those exceptions.

## Classification and proposed native types

Research C inspected all 698 full flagged values, before/after evidence and campaign history, tracing the actual agent authors and 45 linked reviewer artifacts. The complete per-entry ledger includes owner, proposal, frozen head, full value, field locator, before/after hashes, author events, reviewer references, evidence basis and explicit scope limits.

| Flagged-entry classification | Count | Proposed treatment |
|---|---:|---|
| `new_agent_record` | 697 | 696 `LLM_SUGGESTION`; one `DATABASE_MATCH` |
| `ambiguous_needs_review` | 1 | No forced type |
| `supported_actual_human_source` | 0 | None established among these flagged entries |
| `inherited_unchanged` | 0 | The 29 exact inherited objects are outside the flagged denominator and excluded from repair |

The native definition of **MappingEvidence → EvidenceTypeEnum.MANUAL_CURATION** explicitly says evidence supplied by a human reviewer. A source URL, a publication's human author, an ontology curator, an agent peer review or `llm_assisted` alone does not establish that contribution. `ComponentEvidenceTypeEnum.MANUAL_CURATION` instead describes a curator-established constituent list and rationale; its two additions are not defects merely because the spelling matches. `EvidenceSourceEnum`, `mapping_quality` and other review/history enums remain separate axes.

The single direct-database proposal is **w05::MATERIALS-C1193-Neopeptone**, `ontology_mapping.evidence[0]`, payload `2aeb5ee8b780b6dac0616c6ea296f891c08d05fcbbe5d941007e165d34b3bb96`. Its exact narrow statement is established by the successful MICRO:0000177 capture `0e3ebc5a1c5d82f5eaa4cb33eb337c7a8a0ab12e131a97ecc9d2f0504b44d9a6`: label, non-obsolete status and Bacto Neopeptone manufacturer definition. Root and the skeptical reviewer independently read this capture. `annotation.createdBy: Carrine Blank` is ontology provenance, not human review of this MIM evidence row. No whole-owner scientific approval follows.

The historical exception is **w09::ma-casamino-distinct**, `ontology_mapping.evidence[1]`, payload `66e70b490105953e4767731b9bd4343e5be464ae90907361e368839d15820ea5`. The new prefix “HISTORICAL; superseded by exact MeSH identity below.” is agent-authored; the remaining note is the entire old #263 assertion. Baseline `reground_263` history and the current #263 body do not establish the original human/process supplier. Preserve both complete objects and defer retyping this wrapper. The separately new evidence[2] is assessed on its own authorship; this exception does not erase that finding.

W09's three ChEBI-definition rows retain conditional database alternatives because their complete wording also asserts source-identity applicability. A narrower type is not selected merely because an ontology URL appears. Other source-specific identity/preparation/alias judgments receive `LLM_SUGGESTION` proposals with their exact notes and provenance retained. This does not call their primary source facts fictional. No `CROSS_REFERENCE` replacement is selected without the exact database relation establishing the complete claim.

Historical manual/user-approved events are not declared absent from the corpus. The exact CO2 and Angustmycin examples in `historical-provenance-boundary-examples-v1.json` demonstrate why new agent history cannot retroactively retype old evidence. Inheritance alone also does not authenticate original human supply.

## Actual reviewers, controls and limitations

- `/root/research_b`: complete deterministic 981-proposal byte/origin/diff audit, helper and 18 private tests. Final helper is `mechanical/audit_v2.py`; original v1 remains preserved.
- `/root/research_c`: all 698 flagged-entry provenance classifications and type suggestions, 45 historical reviewer artifacts and 862 hashed inputs. Primary scientific truth was not re-reviewed across all claims; direct source captures were reopened only for the listed typing exceptions.
- `/root/final_reviewer`: independent raw-pair/delta recomputation, helper/test scrutiny, all-entry classification/binding checks, selected full source/historical exceptions, W02 conflict boundary and final assembly. Actual final scope/verdict is in `skeptical/final-review.json`; it is not a scientific approval receipt.
- `/root`: contracts, current issue deduplication, selected historical/direct-database corroboration, exact matrix assembly, native draft validation and preservation/handoff. Root and some agents previously authored/reviewed W02 work. **All 58 W02 flagged entries are mechanical/provenance-only; no independent scientific self-approval is provided.**

The 18 tests cover retained historical objects, reordered lists, duplicate additions/removals, modified complete values, mapping/component separation, changed attachment context, missing/bad-hash input, duplicate YAML keys, full field differences and output path/refusal behavior. A separate replay produced 991 byte-identical output files. Pytest ran in the private mechanical cwd on Python3.13 with addopts cleared, coverage/plugin/cache disabled and private basetemps.

The skeptical reviewer found a lexical output-containment/overwrite weakness in B's initial audit helper. No escaped write occurred in the actual run. Immutable v2 rejects traversal, symlinked roots/parents/output and existing run destinations; four regression controls cover it. This is ordinary audit output guarding, not an atomic or hostile-concurrency transaction guarantee. The original helper, logs and run remain unchanged.

Root's initial native YAML draft was correctly refused for PyYAML-generated anchors/aliases. `review-draft-v2.yaml` preserves identical parsed content without aliases; native validation and rendering pass. The failure and exact correction are retained. The private native draft has 981 targets/assessments, `scientific_review: false`, explicit `self_review` conflict disclosure and all 88 original W08-IR-001 target IDs. Its verdict is `needs_curation`; neither structural validation nor audit completion means the proposals were repaired. The normal saver was not invoked because the user restricted outputs to this private directory.

## Coordinator recommendation before writer work

`coordinator-notification-before-writer-v1.json` records the early report; `machine-finding-draft-v2.json` and this handoff provide the final report to coordinator/root **before any candidate writer work**. The skeptical reviewer caught a counter-label error in machine draft v1: 696 is the number of LLM evidence entries, across 645 proposals. Immutable v2 distinguishes entry and proposal counters; the original and correction receipt remain. Classifications and scientific fields did not change. The issue refresh found #1226 after the first snapshot; both immutable snapshots remain, and `issue-dedup-assessment-v2.json` binds current routing. #1227 explicitly excludes W08-IR-001 in favor of #1226. No duplicate filing is needed.

One guarded coordinator metadata-only candidate batch is feasible **after final source/owner choices settle**, using the claim-specific matrix rather than a global replacement. Rebind each eligible entry to final owner bytes, complete evidence-object hash, exact enum range and duplicate-aware locator. Refuse stale inputs or changed source context. The proposed allowlist is the selected `evidence_type` fields plus an explicitly declared truthful append-only curation-history event; preserve every prior history item, source string, raw value, notes, original capture timestamp and scientific field. Exclude the ambiguous historical wrapper and inherited/component entries.

Reconcile overlaps without choosing winners through this metadata repair. Use maintained native writer/schema/partonomy checks and meaningful negative controls on any later authorized candidate. Changed owner bytes invalidate inherited approval bindings: keep old reviews immutable and require fresh independent assessment of the exact complete successor, final current owners and full canonical base. A failed publication/check may leave rejected candidate artifacts; file existence is not approval. No schema weakening, source-hold release or export follows.

Authoritative artifacts:

- `provenance/entry-provenance-ledger-v1.json`: SHA256 `98bfa525356aa223a08fcd2be11d9dc7476231aa6cd9efa4db1f85b2e66109e2`.
- `provenance/native-type-suggestions-v1.json`: SHA256 `9ca6b04f03fdaabd65dacd90a160cf9f51dc549e607b5f5634616469532f1b33`.
- `mechanical/mechanical-review.json`: SHA256 `f7e0ca3cf3ac5ef8fb22163e8d5b6b319be255a536fe54e98c39137c435c67da`.
- `review-draft-v2.yaml`: SHA256 `04404d4b41c283c8817103fbd990b1c1d9046ee915ff5105724a8738ebe00440`.
- `review-draft-v2.md`: SHA256 `4759822be8d3b95a0c873fb68fc75bed02001e46b3032903a1c27e28bbeff202`.

The pre-final manifest binds the completed inputs for skeptical final assembly. Final `MANIFEST.json` adds that manifest and the exact final reviewer receipt without rewriting reviewed files. Retained test-runtime fixtures remain on disk and are explicitly excluded from the delivery manifest; no cleanup was performed. Closing receipts record exact preservation checks and their scope.
