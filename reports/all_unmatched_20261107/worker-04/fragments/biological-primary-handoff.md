Biological primary review handoff, 2026-11-08

All 51 assigned cases have individual source-bound assessments, exact frozen input digests and occurrence IDs, complete recipe-context references, captured primary evidence, and explicit preserved limitations. Final primary v2 contains 51 decisions, 357 evidence entries, and 11 isolated owner proposals. No maintained ingredient YAML, SSSOM, publication selector or downstream output was edited.

The dispositions are 30 stock/product/material contexts, 8 existing identities or aliases, 10 cases with new distinct ingredient proposals, and 3 unresolved oatmeal-form cases. The 10 new-owner cases share 9 new owners: eight recipe-specific seawater/mineral stocks and DSMZ 781 horse-dung extract. The other two payloads add two verified filtered-natural-seawater labels to the existing owner and annotate colloidal chitin with the explicitly source-bound DSMZ 1681 protocol. Generic labels are retained in contextual notes/evidence only for the nine new owners; they do not resolve globally.

The eight stock proposals are JCM 492 Modified MJ seawater, DSMZ 611 synthetic seawater mix, JCM 512 DL minerals, DSMZ 946a 2x seawater, JCM 651 0.5x seawater, JCM 910 1x seawater, JCM 1269 4x seawater, and DSMZ 1009 sea-salt preparation. Components preserve original forms and batch quantities with UNMAPPED references where chemical identity was not independently selected. JCM 910 quantities are explicitly calculated from JCM 651 under the source's doubling instruction. Existing Sulfur-free DL Minerals is compositionally distinct from JCM 512 and is retained as a baseline comparison.

Substantive boundaries retained:

- Prepared seawaters, acid/filtered plant extracts, and resulting stock mixtures do not become bare seawater, water, plant tissue or purified compounds.
- JCM 248 explicitly establishes dry cow manure as the starting material for source 1707; the prior #391 merge is supported for that input, while the resulting filtrate and withheld animal-manure parent relation remain separate.
- NCIT C29298 explicitly describes colloidal whole-oat fine powder. Generic or powdered Quaker source material does not establish the precise physical form; medical usage alone is not an identity distinction.
- C9322 supplier evidence supports bovine-liver catalase reagent and excludes a human-specific protein interpretation, without globally merging all catalase products.
- Formula-free MJ and 0.1x artificial seawater remain precise source-context requirements after available primary recipes were inspected. Source-unit defects are preserved and deduplicated to CultureMech #408/#150 where applicable; DSMZ 1009 has no such defect.

Validation: guarded schema writers passed all newly generated stock/material payloads; exact case digests, occurrences, capture hashes, before-owner hashes, proposed bytes and proposal backlinks passed captures/biological/fragment-integrity-v2.json. Every case has actual captured primary-source evidence. The root owns final strict/native review packaging and whole-188 structural validation. Structural checks are not scientific approval. Separate skeptical review by /root/media covers all 51 cases and 11 payloads; its v1 findings were remediated in v2 and final recheck was requested.

Metadata incident: an independent chemistry-review fetch helper accidentally replaced only biological/final-retrievals.json after v1. No original successful response body was changed. All 139 v1 primary/ontology body hashes passed the preserved comparison in superseded/biological-v1/primary-body-hash-check.json. Original receipt bytes and redirect final_url fields were lost; surviving URL/access-time/path/hash/error fields were reconstructed only from archived v1 evidence, with an explicit reconstructed filename, new hashes and disclosure. Two failed-retrieval evidence entries were repaired. Exact v1 fragments/payloads remain under superseded/biological-v1 with INVALIDATED.md. The helper now writes to isolated reviewer run directories with exclusive file creation; the negative control proves an existing receipt cannot be overwritten.

Final primary fragment hashes:

- biological-decisions.json: ea99dbb7383f701d187962de9ebb497b34bffb362b7cad724d2165b3949c458d
- biological-evidence.json: 71b95081610306003e21addb113c76963809f17a17b402abe793818d2894afd5
- biological-proposals.json: 273b5c4bef21bf69f38b16107d8b42b550ebdf84edb26cfa1c1a16f6fb55cc84

All proposed existing-owner changes retain original baseline hashes. Coordinator integration must reconcile cross-shard owner proposals, withdraw inherited support for changed bytes, and review complete resulting owner payloads; no release hold was cleared here.

Separately, /root/biological completed the independent chemistry review of all 74 final cases and 26 proposals. The durable review is independent-review/chemistry-reviewed-by-biological-v1.json, SHA256 126dcdd33fba79fe7cf62babcfa4dc4ce3679f6f0d1040e38733a566e2782360. Four findings were resolved and all 404 chemistry evidence captures validated against their hashes. That review retains full-owner publication holds and is bound to the chemistry author's final fragment hashes.
