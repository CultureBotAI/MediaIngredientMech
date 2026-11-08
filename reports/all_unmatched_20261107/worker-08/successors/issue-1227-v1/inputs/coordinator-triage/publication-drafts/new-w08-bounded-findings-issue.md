Independent review of Worker08’s published `b90a2fd4681d20e2586481b7b9b1114a78281b94` found bounded corrections in isolated proposals. Maintained owners/canonical mappings have not been changed by this review. The complete source assessment has188 cases and113 selected payloads;94 affected payloads are a union across findings, not94 chemical rejections.

The frozen external review is `.temp/all-unmatched-20261107/workers/w03/worktree/.temp/w08-published-head-independent-review-v1/`: findings SHA256 `11e3681d90be88d52a309fc6ed301bcb4c37c749ffb144640175cea6db501af5`, full manifest `9b34903748fba1da78b5649ad471a1804da04a78b7775004d71f6b8d36f8cf76`. Coordinator triage independently verified all5070 manifest members and all113 exact Git payloads; its action matrix SHA256 is `9a26d2adf42df8195f19b2090754978db063dfe515f8738a2a54f9d4c3f772f4`. Original findings, drafts, captures and reviews remain immutable.

This tracker covers the following seven remaining W08 groups. W08-IR-001 belongs to1226, IR-003/004 to1201, IR-008 to811 and IR-010 to1210; those scopes are not duplicated here.1173 tracks Worker01 lineage, and718 is broader context rather than this correction ledger.

| Finding | Confirmed defect | Bounded correction |
|---|---|---|
| W08-IR-002 | JCM403 numbered pointers remain global resolving labels | Qualify preferred terms with JCM and preparation identity; preserve exact old pointer strings and all source provenance as REJECTED_LABEL; retain source occurrence routing and append history. Re-review exact successor and all backlinks; do not resolve generic pointers by label alone. |
| W08-IR-005 | Retained supernatant water inference uses literal transcription method | Use CURATED_INTERPRETATION for the water-retention inference with explicit rationale and unmeasured retained-salt limits, or omit the derived has-part list until supported. Preserve all charge recipe facts in provenance and do not convert them into retained concentrations. Ground the water component if retained. |
| W08-IR-006 | Component completeness does not consistently follow source-relative enum meanings | For each precisely identified assertion, distinguish explicit omitted constituents (PARTIAL), source-unestablished closure (UNKNOWN), and complete source enumeration (COMPLETE). Missing concentration, final volume, titrant quantity or molecular grounding alone does not determine membership completeness. Preserve the bounded stock and all unknowns. |
| W08-IR-007 | Nalidixic-acid occurrence applicability lacks readable primary support | Bind a readable exact NBRC1314 primary capture or record that occurrence as source-held/unverified while retaining the independently supported acid candidate. Keep the successful1301 capture separate from failed1314/M2023 requests; do not claim an unread source was inspected. |
| W08-IR-009 | Trypticase soy broth mapping grade overstates primary-label match | Change mapping_quality to SYNONYM_MATCH with a truthful history event and preserve correct identifier, canonical ontology label, mixture components and own-identifier exact SSSOM semantics. |
| W08-IR-011 | Allen phosphate remaining requirement repeats a resolved dose distinction | Narrow case63 remaining requirement to unusual seven-water supplied-form confirmation or correction, and state the source-resolved5ml dose transcription separately. Preserve the chemical hold and frozen input. |
| W08-IR-012 | L-asparagine monohydrate retains parent treatment despite exact NCIT evidence | Adjudicate NCIT:C87433 against its exact L-hydrate synonym and CAS5794-13-8 under section3 exact-term priority, updating primary identifier and mapping grade where supported. Preserve the CAS/source alias/history and distinguish DL hydrate. Separately clarify or verify stereochemical SMILES scope without inventing a structure or calling an unspecified SMILES a racemate. |

The completeness correction requires source-specific judgment. The native enum means COMPLETE only when the cited source establishes the retained constituent list; PARTIAL means the source identifies omitted constituents; UNKNOWN means closure is not established. Missing amount, final volume, hydration, stereochemistry or a catalog CURIE is not an omitted constituent.

The external final reviewer identified29 unsupported PARTIAL assertions among34, excluding five rather than rewriting them all. Independent coordinator source-table readback refines five of those29: the two PCR-S11 phosphate stock recipes, Allen phosphate stock, MediaDive552 “5.0g in100ml H2O” preparation, and JCM941 Solution C explicitly enumerate their two retained inputs. COMPLETE is recommended for that literal input-list scope, preserving all chemical-form and physical-composition uncertainty; the other24 uncertain lists warrant UNKNOWN. The five exclusions remain separately assessed (YPS omitted literal inputs; PCR buffer and JCM628/629 pH/CO2 treatment). Do not invent titrants, carriers or gas quantities. The exact34-row table and original source hashes are in `completeness-adjudication-refinement.json` and `complete-list-primary-proof.json`.

For JCM403, actual primary formulation separates the six-input vitamin solution from the5mg B12/100ml distilled-water stock. Six provider-free pointer aliases resolve through native policy despite citation provenance. Qualify the preferred preparation names and preserve pointers as non-resolving provenance; registry promotion of the existing B12 placeholder is separately tracked under1201.

For NBRC1356 mineral base1, the source instructs use of the supernatant after precipitation. Retained water is an inference, so record CURATED_INTERPRETATION if retained, with UNKNOWN retained composition. Charged salt quantities must not become retained concentrations.

For nalidixic acid, independently readable NBRC1301 supports the acid/source claim; exact NBRC1314/TOGOM2023 applicability remains unavailable. Obtain readable primary evidence or hold only that occurrence. Source retrieval failure neither rejects the supported acid identity nor justifies claiming the failed source was read.

For L-asparagine monohydrate, the archived official NCIT:C87433 response (`54c71948e42aaa1995f271abc3cf70e4ccb9c7b6ae304fa1eff8d754a7af4dae`) records CAS5794-13-8, formula C4H8N2O3.H2O and exact synonym “L-Asparagine Monohydrate”. Under MAPPING_SEMANTICS§3, evaluate that exact target before retaining CAS-primary/NARROW_MATCH. Preserve the distinct DL hydrate. The non-isomeric SMILES does not itself assert racemization; do not invent a replacement structure. Any primary-ID change requires dependent-reference accounting and fresh content-bound review.

Other small corrections retain sound chemistry: Trypticase soy broth is an exact synonym of the ontology’s preferred “tryptic soy broth”, so its actual lookup grade is SYNONYM_MATCH; the Allen stock dose is already resolved as5ml of a6g/L source stock, while the unusual seven-water supplied formula remains held.

Exact non-bulk targets follow. The29 completeness targets are fully listed in the attached action matrix rather than authorizing edits to every PARTIAL record.

**JCM403 numbered pointers remain global resolving labels**

| Proposal / owner | Exact payload SHA256 |
|---|---|
| `vm-prop-jcm403-b12` / `data/ingredients/unmapped/Vitamin_B12_Solution_See_Medium_No_403.yaml` | `94956716b71347bd431921e64a06ddd2593d6e7bc50e748e1be3c3cc78bb73a8` |
| `vm-prop-jcm403-vitamin` / `data/ingredients/mapped/Vitamin_Solution_See_Medium_No_403.yaml` | `a86933326bed8cdf623c0a8dc41622bd6e3bc54243addf1610be4f884dda1db5` |

**Retained supernatant water inference uses literal transcription method**

| Proposal / owner | Exact payload SHA256 |
|---|---|
| `vm1201-prop-nbrc1356-mineral-base1` / `data/ingredients/mapped/NBRC1356_Mineral_Base1_Supernatant.yaml` | `0aa699c355adee9161a6778c5ee892e07d5f85b2cf90494dea6b31f9072f0256` |

**Nalidixic-acid occurrence applicability lacks readable primary support**

| Proposal / owner | Exact payload SHA256 |
|---|---|
| `op-nalidixic-new` / `data/ingredients/mapped/Nalidixic_Acid.yaml` | `ca0acf4743b49628c9a2086a412abbc2c82840367a40251061e8b43608b50d72` |

**Trypticase soy broth mapping grade overstates primary-label match**

| Proposal / owner | Exact payload SHA256 |
|---|---|
| `op1201-trypticase-soy-broth` / `data/ingredients/unmapped/Trypticase_Soy_Broth.yaml` | `cbc788c1a9ce7cea22a92b4360bad7c113f0e99c2cf5a1ecbbd3a0e79f99aa6c` |

**L-asparagine monohydrate retains parent treatment despite exact NCIT evidence**

| Proposal / owner | Exact payload SHA256 |
|---|---|
| `op-l-asn-hydrate-alias` / `data/ingredients/mapped/L-Asparagine_Monohydrate.yaml` | `07d8b55d6773f4e16ad57e18e5ed72a4438bdeb207cdfb435da84cc2cb62e20a` |


Exact affected `/component_assertion/completeness` entries (all currently PARTIAL):

| Proposal | Source-relative recommendation |
|---|---|
| `if1201-new-dsmz_trace_2n_naoh` | UNKNOWN |
| `if1201-new-jcm_1130_10n_naoh` | UNKNOWN |
| `if1201-new-atcc_nitrosolobus_6n_naoh` | UNKNOWN |
| `if1201-new-pcr_s11_01n_naoh` | UNKNOWN |
| `if1201-new-dsmz_104_8n_naoh` | UNKNOWN |
| `if1201-new-jcm_221_02n_naoh` | UNKNOWN |
| `if1201-new-wolin_mineral_05n_naoh` | UNKNOWN |
| `if1201-new-atcc_1340_naoh_4g_100ml` | UNKNOWN |
| `if1201-new-jcm_574_1m_kh2po4` | UNKNOWN |
| `if1201-new-jcm_574_1m_k2hpo4` | UNKNOWN |
| `if1201-new-pbbm_1m_na2hpo4` | UNKNOWN |
| `if1201-new-pcr_s11_50mm_nah2po4` | COMPLETE for the explicit literal two-input list |
| `if1201-new-pcr_s11_50mm_na2hpo4` | COMPLETE for the explicit literal two-input list |
| `if1201-new-allen_m2231_phosphate_stock` | COMPLETE for the explicit literal two-input list |
| `if1201-new-jcm_908_sulfide_10pct_wv` | UNKNOWN |
| `if1201-new-jcm_713_sulfide_24pct` | UNKNOWN |
| `if1201-new-atcc_1943_sulfide_25pct` | UNKNOWN |
| `if1201-new-atcc_1942_sulfide_5pct` | UNKNOWN |
| `if1201-new-mediadive_552_thiosulfate_5g_100ml` | COMPLETE for the explicit literal two-input list |
| `if1201-new-jcm_941_solution_c` | COMPLETE for the explicit literal two-input list |
| `op1201-r2a-medium` | UNKNOWN |
| `op1201-amphotericin-stock` | UNKNOWN |
| `vm1201-prop-nbrc1356-mineral-base1` | UNKNOWN |
| `vm1201-prop-jcm515-b12-partial` | UNKNOWN |
| `vm1201-prop-jcm647-b12-partial` | UNKNOWN |
| `vm1201-prop-jcm1354-b12-partial` | UNKNOWN |
| `vm1201-prop-atcc2883-b12-partial` | UNKNOWN |
| `vm1201-prop-togo125-k1-partial` | UNKNOWN |
| `vm1201-prop-dsm1245-k1-partial` | UNKNOWN |

Required follow-up: preserve beforeimages and historical/source evidence; make bounded successor proposals and exact case/evidence backlinks; bind a new complete manifest; obtain independent review of the final scientific payloads and native schema/partonomy/lineage checks. No maintained-data application, source-hold release, role/export approval, owner merge or cross-shard winner selection is authorized by this issue.

Deduplication context: all-state title/body inventory and targeted current comments were read. Generic pedigree in718/1173 and the worker06-specific1217 findings do not already track these W08 payload corrections. The coordinator performs final live deduplication before filing.
