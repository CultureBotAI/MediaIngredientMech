# Chemistry primary handoff

All 74 assigned chemistry cases have source-bound decisions. The final primary fragment contains 404 evidence entries and 26 isolated owner proposals. No maintained data, SSSOM, release selector, GitHub resource or branch was changed by this subagent.

Final primary files:

| File | SHA256 |
| --- | --- |
| `chemistry-decisions.json` | `066a5cd0629b5d77544e6dd6cb86ac8b9d5921bb2f8958e32f0bd5ca6eb063b7` |
| `chemistry-evidence.json` | `498b116cffe504394a17c8ceedefd3d7685ee8e75bfded864f621b0cff82871f` |
| `chemistry-proposals.json` | `d3c6384c8fb355304adeb3e2bac9069d695827a64ba5b568287027517b77a500` |

The independent biological reviewer inspected every case and all 26 payloads, resolved four substantive findings, and reported no remaining narrow-delta findings. Its exact-hash review is `independent-review/chemistry-reviewed-by-biological-v1.json`, SHA256 `126dcdd33fba79fe7cf62babcfa4dc4ce3679f6f0d1040e38733a566e2782360`. This does not approve inherited complete owner payloads or remove publication holds.

The proposals include four new chemical identities (generic retinol, barium carbonate, bis-tris propane and the explicitly reviewed bare 2-oxoglutarate dianion), exact putrescine dihydrochloride grounding, conservative spelling/qualified aliases, sodium glutamate monohydrate structure repair, residual incorrect-form alias rejection, and five source-qualified stocks. Stock source labels are nonresolving `REJECTED_LABEL` provenance; they do not create global aliases for context-dependent names. All before hashes are the original current owner bytes, and the coordinator must reconcile overlapping owner proposals before integration.

Material source findings retained:

- MediaDB292 AAM-minus contains D-glutamate in the frozen source, while Lee2009 methods omit L-glutamic acid from AAM-minus and Table4 row13 identifies L-glutamic acid. This is a source/recipe/stereochemistry conflict, not an ontology-label gap.
- MediaDive404 supports 1:1 magnesium hydrogen citrate through its CAS, formula, mass and source molarity. The five-occurrence MIM owner was deliberately regrounded to 3:2 trimagnesium dicitrate in issue320 using a preprocessed CAS, while retaining 1:1 chemistry. The source-bound split requirement does not silently reverse that historical whole-owner decision.
- TOGO2692's titanium(III)-citrate title conflicts with its explicit TiCl2 precursor. Its50ml preparation is known; oxidation-state correction is the missing fact.
- Na3EDTA in TOGO2734 conflicts with disodium EDTA in original DSMZ1005. Hydrate conflicts in citrate, tungstate, molybdate, sulfite and EDTA remain case-specific; no waters or counterions were normalized away.
- TAPS source metadata incorrectly points to an unrelated peptide; the source buffer still lacks acid-versus-sodium-salt procurement evidence. The sodium-salt owner's unqualified TAPS alias is proposed for rejection.
- Original Welsch1947 pp101–102 identifies actinomycetin as crude culture filtrate. The graph vocabulary cases remain preparation context, not unique chemical structures; automatic SINGLE_INGREDIENT typing on the existing placeholder is not newly approved.

`captures/chemistry/operations.md` records retrieval methods and actual failures. Original URLs, access times and hashes are in the receipt files. `captures/chemistry/fragment-validation-final.txt` reports PASS for all case digests, exact source fields and occurrence IDs, current owner/capture hashes, proposal backlinks and YAML parsing. The parent remains responsible for the whole-shard outcome auditor, strict native schema/OAK/partonomy review, issue deduplication, publication decisions, commit/push and the coordinator handoff.

The chemistry subagent completed independent review of all 63 media cases, all 26 final isolated payloads and all 253 evidence captures. Final review `independent-review/media-reviewed-by-chemistry-v2.json` has SHA256 `06df7024ae3f93dfc5af7e20f1250e3bb4019905d2950b9fe9d7100964efebe9` and binds decisions `c503be4a8ee4cba608098110061fda994ebe59ec7e9c0c690818d36685f38c28`, evidence `6aba65f3858a2908114a20e0c45b1197a2470ba48d31973e9ff02255f3e3893b`, and proposals `25d6b43527c508a2a677753a8f198b41319f564d20570c278752ebb916a313e7`. All six initial findings and the additional evidence-placement/scope findings were resolved. No narrow-delta scientific finding remains; inherited owner and source/publication holds are preserved. The immutable v1 review records the original findings. Review operations and unsuccessful extra manufacturer retrieval attempts are documented under `independent-review/media-review-chemistry-operations.md` and `independent-review/media-chemistry-captures/`. No branch mutation, commit or push was performed by this subagent.
