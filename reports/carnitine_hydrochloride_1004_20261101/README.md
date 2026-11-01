# Approved carnitine hydrochloride migration (#1004)

The approved decision is recorded on [#1004](https://github.com/CultureBotAI/MediaIngredientMech/issues/1004#issuecomment-6555569867). This batch identifies DL-carnitine hydrochloride as exact **NCIT:C216679**, CAS **461-05-2**, with chloride-bearing chemistry from PubChem **CID 5970**. It explicitly reverses the 2026-07-05 surface-form non-merge ruling. No ChEBI contact or paid research provider was used.

## Source decision and preservation

[NCI EVS](https://api-evsrest.nci.nih.gov/api/v1/concept/ncit/C216679?include=full) supplies the active NCIt 26.10d exact identity and CAS. [PubChem CID 5970](https://pubchem.ncbi.nlm.nih.gov/compound/5970) supplies formula C7H16ClNO3, molecular weight 197.66 and the chloride-bearing structure. [ChEBI:48601](https://www.ebi.ac.uk/chebi/CHEBI:48601) is carnitinamide chloride, a distinct amide despite its conflicting CAS cross-reference. The Sigma C9500 factual extract supports the original racemate. The 19 source artifacts and retrieval context are bound by [sources/manifest.json](sources/manifest.json), SHA256 `d5bf100092c4a16d29552e79475b1a8a8891a797c046377365a46f0fb85ce911`.

The original CultureBotHT CSV is a hash-bound ignored local snapshot associated with checkout context, not a commit-attested upstream blob. The successful supplier evidence is a factual extract from an independently captured rendered response; the earlier empty HTML response is retained as a failed capture. Direct CAS API access returned 401, so this report does not claim CAS Registry verification.

The guarded source transaction changed exactly three of 2,955 individual records; the other 2,952 remained byte-identical. Carnitine_Hydrochloride keeps its preferred name and 14/14 historical counts, acquires the exact NCIT identity and CID 5970 chemistry, and preserves the duplicate raw name as a RAW_TEXT synonym. The amide and free-substance systematic names remain attributed REJECTED_LABEL provenance. Carnitine_Dl_Hydrochloride remains a zero-count REJECTED tombstone with corrected identifier, ontology and representative NCIT:C216679; its former free-parent chemistry is preserved in history and beforeimages. Each record retains its complete own history prefix.

Only NLDM component position 59 changes identity, from the retired local salt ID to NCIT:C216679; name, 17.5 UM, MIM_CATALOG scope, other components and evidence remain intact. The two approved salt labels receive finite occurrence-routing overrides. Exactly 14 existing membership identity cells migrate with recipe IDs/counts preserved; tests also admit later recipe/count growth. Free and L-carnitine controls remain unchanged.

The rejection ledger moves the existing CHEBI:91318 rejection to the new owner and adds one owner-scoped CHEBI:48601 rejection. The merged [Claw #700](https://github.com/CultureBotAI/culturebotai-claw/pull/700), `6a7172585eb68da7f4fe01aee75a82458ddd470c`, separately prevents the rejected amide proposal across maintained and legacy CAS/source automation without banning legitimate amide records. Its merge, checks and cleanup were verified before this MIM batch.

## Generated mapping and review boundaries

| Surface | Verified change |
| --- | --- |
| Canonical SSSOM | 2,986 → 2,982 rows: two changed, four removed, none added. Five salt rows become one exact NCIT row; the wrong cas:461-06-3, parent and registry assertions are retired. |
| NLDM mapping | Only source and mapping_date change. Its exact original triple-bound validation stamp remains historical provenance. |
| Rule K baseline | The two salt/free-DL alias allowances are removed after candidate proof. |
| Unified snapshot | One row changes: Carnitine Hydrochloride gains NCIT:C216679, CAS 461-05-2 and the two accepted salt spellings. All 4,170 names, 209,330 occurrences, and 4,169 unrelated rows remain unchanged. |
| Mapping decisions | 1,739 SUPPORTED and 1,243 WITHHOLD; all 2,980 unrelated decisions preserve their payload/status/evidence after relocation. |
| NLDM approvals | Its mapping and all 68 component/role approvals withdraw. Component 59 is the only changed nonmapping payload; the other 67 payload hashes remain identical. |
| Companion | The unchanged 20-owner/51-claim cohort is preserved; 17 mapping evidence locations relocate through the native verifier. |

[Receipt 17](../sssom_completion_20260921/mapping_changes/issue1004-carnitine-hydrochloride-merge.json) binds all three owners and the complete row transition. All 16 preceding receipts remain unchanged. Historical source tokens are preserved alongside actual new provenance; they do not independently support the new NCIT identity. The new NCIT row has no inherited validation stamp. Both changed mappings remain WITHHOLD; no scientific approval is created by the source mutation, receipt, native structured review or companion refresh.

The diagnostic native candidate has 2,975 rows. Promotion selects the bounded approved rows; every unrelated canonical row and metadata byte is preserved. Canonical SHA256 is `d5cd812a8c44c85438d73c68c7a8c3067a505765e4cd54e3a64cef029f2d8ed6`; unified SHA256 is `ca62e2f031ebe0f9e6185efc7816207912095beef9799a04634c889cc27196b5`.

Native semantic integrity passes. The full graph retains its separate FAIL verdict with 1,732 blocking findings and 2,336 open assertions; the supported subset has 2,151 approved assertions. One historical active-duplicate finding (`SEM:44d0b3a4f069e5dbbbf5`) leaves the active graph when the duplicate becomes a tombstone; this is not a new scientific approval. Eight pre-existing aggregate discussion-field omissions remain unchanged; the three target aggregate records exactly match their individual records.

## Execution and findings

The source base is `99fe4b44d78126d78041a69eeb366c52bedf0caa`. Generation uses the clean isolated merged Claw producer `6a7172585eb68da7f4fe01aee75a82458ddd470c`; the unchanged native validator pin is `16fd7c9484d98b14a53aec55616d26dae70a0af7`. CultureMech is `a74dd489720c9df96cc073ffd11568d407d3c06c`. Exact working input hashes and the read-only KG-Microbe revision/dirty-state context are preserved in generation receipts. CultureMech output tables and MediaDive nodes are comparison inputs for the raw SSSOM builder; the unified producer consumes the recorded normalized CultureMech YAML. Shared checkouts, Intel workflow-review files, qc-evidence.yaml and the vendored pin are preserved.

- [#1036](https://github.com/CultureBotAI/MediaIngredientMech/issues/1036): a completed-source no-op must bind the original complete receipt, current outputs, timestamp and all beforeimages.
- [#1037](https://github.com/CultureBotAI/MediaIngredientMech/issues/1037): publication wrappers bind the exact checked bytes and complete input/receipt sets. Final package evidence binds the authorized companion selector advance; the original package checkpoint and all original reviews remain preserved.
- [#1038](https://github.com/CultureBotAI/MediaIngredientMech/issues/1038): promotion preserves exactly NLDM's native replayed historical stamp while requiring an unstamped new NCIT identity.
- [#1039](https://github.com/CultureBotAI/MediaIngredientMech/issues/1039): the plain unified TSV retains hash-prefixed ingredient names. The original diagnostic undercount is preserved and explicitly superseded; production artifacts were correct throughout.

[Implementation evidence](implementation/README.md) preserves actual guarded transactions, primary proof bindings, original/fixed tests, fault injections, review checkpoints and exact native journal archives. [Generation evidence](generation/README.md) preserves the diagnostic candidate, native input/label receipts, approved canonical delta, unified publication and dependency-chain verification. These are standalone evidence artifacts with no invented supervisor or goal-cycle binding.

## Validation

[Final validation evidence](validation/README.md) records 484 focused regression tests and the full Python 3.13 suite: **3,693 passed, one skipped, 27 warnings**. `just qc` passed, including strict/schema/evidence validation, qc-sssom, round-trip/index/visualization checks, duplicate-ID and component checks, and flat-export coverage. CURIE/product-label validation, unified rejection/freshness gates, and the complete mapping/semantic/companion receipt chain passed. Both native visualizations retain current metadata and exclude the rejected duplicate.

Product validation retains 101 non-blocking label warnings. Native B4 checks were additionally run against the actual read-only KG-Microbe transforms; BTO and MICRO transform inputs were unavailable and are explicitly recorded. Structural checks do not grant scientific approval. The [structured review directory](../../reviews/structured/) holds native review records; the PR identifies this batch's exact bundle and later committed-head attestation. CI and merge-queue verification are recorded separately from these local results.
