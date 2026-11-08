Worker 06 completed the bounded source-review shard: **188 of 188 cases**, **100 selected proposals** (76 new owners; 24 existing-owner edits), and **1056 evidence records**. Every case and final proposal has a separate skeptical review. Completion does not mean all identities are resolved or released.

Assigned branch: `review/all-unmatched-w06-source-review-20261107`. The final branch head is the commit containing this handoff; its exact SHA is reported in the session completion and can be read with `git rev-parse HEAD`. Frozen base: `e000d66dd26ab053e9b17ce7bf8d3c873c3dde99`, explicitly dependent on candidate PR [1158](https://github.com/CultureBotAI/MediaIngredientMech/pull/1158). This is not a claim about current main or PR merge status. No worker PR was opened.

The assignment remained unchanged: shard SHA256 `6e5d487b0ffb05a867766fe51bc90074c7aa2e48459335cf983f021720ce2808`. The 145 CultureMech cases preserve all 310 occurrence IDs. The 43 KG cases comprise 37 MediaDive, four MetaTraits, one MicrobeDecoder and one MetaTraits-GTDB case. KG empty occurrence-ID lists mean the frozen source does not expose those IDs; they do not mean zero observations. All 88 embedded downstream hold rows, raw labels (including blanks), source flags and complete source-case digests are retained in [source-holds.json](source-holds.json).

Use [decisions.json](decisions.json), [evidence.json](evidence.json) and **[proposals.json](proposals.json)** as the canonical selected bundle. Apply only payloads selected by that last file, after coordinator review. Earlier drafts, superseded proposals, failed requests and remediation receipts remain as provenance. In particular, the C yeast-extract draft is superseded by the single reviewed combined B payload; there are 101 authored proposal fragments but 100 selected owners.

Actual authorship and separate review scopes are published in [agent-scopes.json](agent-scopes.json):

| Author | Cases | CM occurrence IDs | Authored proposals | Separate reviewer |
|---|---:|---:|---:|---|
| /root/research_a | 47 | 103 | 33 | /root |
| /root/research_b | 47 | 89 | 25 | /root/research_a |
| /root/research_c | 51 | 118 | 27 | /root/research_b |
| /root | 43 | 0 | 16 | /root/research_c |

[Final integration review](research-b/integration-review/review-final.json) binds all 188 decisions and 100 payload hashes, their scientific reviewer receipts, occurrence partitions and preserved holds. It has zero open integration findings. B did not approve its own scientific work; A reviewed B. [Root review of A](independent/root-review-a/final-review-v2.json), [A review of B](research-a/review-b/review-b-v6.json), [B review of C](research-b/review-c/review-final.json), and [C review of root](research-c/review-root/completion-addendum.json) retain prior reviews and resolved findings. [C final integration check](research-c/final-integration-check.json) independently confirms the assembled selection. Three in-process subagents were used; no additional external session was started.

Native formal review: [authoritative YAML](../../../reviews/structured/20261108T055544Z-w06-source-shard/review.yaml) and [rendered Markdown](../../../reviews/structured/20261108T055544Z-w06-source-shard/review.md). The native inspect → validate → save workflow assessed 288 targets (188 exact source cases plus 100 proposed payloads), with `needs_curation` verdict and 31 open bounded source findings. Source-only cases have no invented MIM owner. This is the team-authored synthesis; its separate scientific review evidence is explicit.

Final checks and durable logs:

- [Whole-shard structural audit](structural-audit-final.json): PASS, 188/188 accounted, no missing cases. It explicitly does not establish scientific adequacy or approval.
- [Strict proposal schema validation](logs/proposal-schema-command.json): PASS for all 100 selected payloads; [diagnostics TSV](logs/proposal-schema-final.tsv) contains no errors.
- [Final invariants](logs/final-invariants.json): PASS, exact frozen owner hashes, unchanged maintained paths, source holds and unique proposed identities/paths. The owner search enumerated all 2,956 record files including ignored files.
- [Auditor synthetic controls](logs/auditor-synthetic-tests-retry.log): 22 passed. Initial invocation lacked the optional coverage plugin; the retry isolated these external auditor tests from unrelated package-coverage addopts without changing repository configuration.
- [Invariant controls](logs/invariant-controls.json): unchanged bundle passes; missing case and tampered source digest are rejected in private fixtures.
- [Native validation](logs/native-validate.log), [save receipt](logs/native-save.json), and [append-only retained-review check](logs/native-check.log). See [validation-status.json](validation-status.json) for exact command exit codes.
- Core authored bundle whitespace check passes. Native rendered Markdown retains cosmetic trailing spaces (including blank-source headings); [exact diagnostic](logs/native-render-whitespace.log) is retained without modifying the immutable saved review or raw evidence.
- [Final diff review](research-a/final-diff-review.json) covers the staged report/native-review changes; no maintained ingredient, mapping, schema, selector, export or historical review change is included.

The scientific outcomes are: 28 unresolved, 87 stock_product_mixture_context, 30 existing_identity_or_alias, 34 new_distinct_ingredient_proposal, 3 malformed_or_nonchemical_token, 3 supplied_form_correction, 3 broad_parent_relation_only. All outcomes are case-specific; proposed stock and product boundaries can remain useful while source-release requirements remain unresolved. [Primary access limitations](primary-access-limitations.json) names eight cases without a linked recovered primary recipe capture. Frozen source and official ontology evidence support narrow judgments where appropriate; failed retrievals are not positive evidence. Other version, grade, hydration, stereochemistry, preparation and historical-lot limits remain in each decision.

Notable bounded proposals include independently transcribed stock formulations, specific salt/hydrate and stereochemistry corrections, manufacturer-qualified hydrolysate and yeast-base families, and source evidence for existing materials. The Roscoff Gaffron+Se stock is specifically the 2019 formulation: it is a related-version candidate, **not an approved exact mapping of TOGO M2262**. Current supplier products do not prove historical lot invariance. Unknown titrants, child forms and solution percentage bases are retained as unknown rather than guessed.

Evidence-backed findings were filed after deduplication: [1179, malformed JCM1357 Na2MnO4·2H2O](https://github.com/CultureBotAI/MediaIngredientMech/issues/1179), and [1202, separate casein-derived Hipolypepton from the Polypeptone owner](https://github.com/CultureBotAI/MediaIngredientMech/issues/1202). The former remains unresolved source chemistry; the latter has exact bounded proposals plus a cross-worker owner dependency.

[Cross-shard owner conflicts](research-c/cross-shard-owner-conflicts.json) and its [readable routing ledger](research-c/cross-shard-owner-conflicts.md) flag candidate dependencies, not approval of other workers’ cases. Calcium pantothenate overlaps worker07 and Polypeptone/Hipolypepton worker05; sulfur, carbonate and titanium preparations, JCM numbered-stock families, alginate, N-Z-Amine preparations and distinct Ardacin components require explicit scope comparison. Related recipe numbers or labels do not authorize identity merges. [Ontology/collision audit](research-c/proposal-ontology-audit.json) records the final canonical selection and separately retained author fragments.

The additional shared immutable cache README and manifest were checked: SHA256 `0a8c6b1d8fd3a60de0b5c269613cf25e30ee94f4ae20aa987679639d603e27d5`. Its primary capture bytes were not reused by this worker. Our own captures and explicit in-process shared captures retain original bytes and retrieval times. [Cache consultation receipt](shared/immutable-cache-consultation.json) records this; cache review was never treated as source, owner or export approval.

Coordinator integration must compare the cross-shard proposals against the original before-owner hashes, choose one coherent owner payload, apply through guarded writers, synchronize maintained surfaces, and withdraw inherited support for every changed owner. Full owner review and the separate source/owner/export gates remain necessary. Registry promotions also require the documented mapped-surface migration and SSSOM handling. No maintained sources, holds or publication selectors were changed here; no downstream rebuild, merge, force push or cleanup was performed.

Exact bundle hashes:

| Artifact | SHA256 |
|---|---|
| [decisions.json](decisions.json) | `2dccd8d6b063acdece7089a18ce8bedfa0ee82ae22d6a7a93da8ba1cdc716719` |
| [evidence.json](evidence.json) | `0693725fa940f3d7bf6a46558bf4fd5ceee51acd611ab360a968e8413882de92` |
| [proposals.json](proposals.json) | `fc838985c5b79ef4cef5a502efe3242cdc1b87c8baf805e9b7f56e96de4ed61f` |
| [source-holds.json](source-holds.json) | `eaddfd7ffe5ba2ba1be011696ad741e1b010db2cc9ca4678954a640484f70b77` |
| [structural-audit-final.json](structural-audit-final.json) | `f787f5c160468ef99ef178f17a7c239a842d82505ed06318a7c14effb1b13395` |
| [research-b/integration-review/review-final.json](research-b/integration-review/review-final.json) | `6db4f736392b106c970cab0942cb4299810687a1c9b92ab8af2a1064a6c77ad9` |

[SHA256SUMS](SHA256SUMS) binds every final report artifact and the saved native review pair, excluding the manifest itself. [Artifact index](artifact-index.json) identifies the canonical selection and review chain.
