Title: Retire the FerriSeltz formulation alias from generic ferric ammonium citrate

Independent follow-up to the preserved W07 two-owner review, manifest SHA256 `fa86b7a9bdc84ae7e796d2dcb507d2dd031a0f8c1462492a45bff2fdfb00c04c`. I rehashed all2,339 manifest-listed files, rebound both reviewed candidates to the active37-candidate set, inspected the exact primary sections and reproduced native synonym/row behavior. These are unapplied candidates. Original reviews, histories and genuine scope holds remain; neither review nor this triage approves release.

**FAC-F01** confirms an inherited whole-product/active-ingredient conflation. The authentic `data/ingredients/mapped/Ferric_Ammonium_Citrate.yaml` beforeimage SHA256 `ae646b9c5f3e9c8ec01d939e1b97733259825a14e4a8a03626bc65453035426e` and current reconciled candidate `70f3b34f5cddc485f53242cd6f04ff1bc9fd6598e2be906f6da89393af8f2234` both retain:

`FerriSeltz` — `EXACT_SYNONYM`, source `kg_microbe`, at `synonyms[7]`.

Both native MIM synonym policy and pinned Claw76c1 publishability classify it as resolving. The [official PMDA FerriSeltz powder20% label](https://www.pmda.go.jp/PmdaSearch/iyakuDetail/ResultDataSetPDF/180078_7290004B1030_1_09), September2024 revision, page1 §3.1, instead specifies600mg ferric ammonium citrate in a3g product with flavour, aspartame, sodium bicarbonate and tartaric acid. Page2 §19 describes the active ingredient. Exact PDF SHA256 `ed32d4c1c55534ae3ebf4eb7e51739d645b751fb63dfe51126c49fc29cb4a98d`; the independent reviewer inspected the full text and the composition-table image. The formulated product is not identical to its generic FAC component. No medium occurrence is inferred to use this medicine.

Retain the exact label and source as provenance-only `REJECTED_LABEL`, with claim-specific evidence and a truthful curation event. Preserve the supported generic CHEBI31604 material identity, all three new medium aliases and their eight assigned occurrences, raw histories and source-specific uncertainty. Do not invent a fixed molecular formula/stoichiometry, green/brown grade, supplier, nitrogen role, new medicine owner or source reassignment. If the formulation is ever separately requested, it needs its own supported identity/composition scope.

**FAC-F02 qualification:** four Role/Properties sentences at synonyms[0–3] are already nonresolving in both native policies. Optional provenance-preserving REJECTED_LABEL typing can accompany curation, but this is not an export leak, independent acceptance blocker or evidence that the underlying role is false. Keep the provisional nitrogen-role assessment separate.

Source review: `20261108T071449Z-worker07-fac-independent`, native YAML SHA256 `cf1d6a381fe37bac2031e2d45c1b57c8c9190bfd58ec5c42dbfb1296520c282a`. Exact triage and native controls: `C/preflight/fac-polypeptone-findings-triage-v1/`. Fresh all-state GitHub searches including title/body/comments for FerriSeltz returned zero results; broader FAC-name searches returned #1201 and historical #213, neither the exact product-alias finding. This issue describes the frozen authentic before/current private candidate, not an unverified statement about live main.

Corrected whole-candidate bytes need independent review and native alias checks before source application. Preserve mapping/source/role/export holds and all historical evidence. No new schema, gate, threshold or owner-selection change is needed.

<!-- mim-fingerprints:ferric-ammonium-citrate-ferriseltz-product-exact-alias -->
