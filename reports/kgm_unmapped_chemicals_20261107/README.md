# KG-Microbe chemical reconciliation — 2026-11-07

The fresh KG-Microbe queue exposed an absent source spelling for an existing sodium acetate trihydrate owner. This batch adds **one exact lexical alias and no new chemical owner**, corrects one unsupported provenance explanation, and preserves the scientific release boundary. [Before/after evidence](reconciliation-comparison-v1/summary.json) retains all **549 source candidates**: 547 entries are identical; only MediaDive 1315 and the rejected 3-methylacetate record change.

## Inputs and coverage

The read-only source checkout `kg-microbe-mim-1788-20261107` was captured at `f10fb3909ed32898a54176ca77e509a950d16b84`. It already consumed the reviewed MIM export from `0dac278466699129a083343a921c2e0ca18a9ab4`; this was an absent alias, not an old export awaiting consumption. The [source manifest](source-audit/source-manifest.json), SHA256 `e2f4252a44aabaffaad7d3d3ca27ac0fb96e50b58939747e095e2ca1b9e3b48e`, binds 95 files, native helper code/execution receipts and the exact matching inputs.

| Source | Retained candidates | Qualification |
|---|---:|---|
| MediaDive | 415 | 410 native queue rows, four context-free lookup recoveries and blank ID 1944 all retained |
| MicrobeDecoder | 10 | Complete compound subset with `--prefix compound --min-occurrences 0`; eight fall below the legacy threshold of 10 |
| metatraits | 82 | Current graph compound placeholders |
| metatraits_gtdb | 42 | Current graph compound placeholders |

The saved MediaDive queue had 201 rows; 166 exact ID/label pairs overlap the fresh 410-row queue. Its `occurrences=1` is a helper constant, not measured recipe frequency. Raw labels are preserved separately: 44 differ from transformed names. Hidden/ignored files were included in the search for other chemical failure outputs; external symlink directories were not followed. Trait/taxon/association failures were kept separate. See the [source audit](source-audit-execution/SOURCE_AUDIT_README.md).

The current corpus has **2,956 direct mapped/unmapped record files**, excluding nested historical backups (#1152). These flags overlap; do not sum them or interpret lexical coverage as scientific approval:

| Diagnostic flag | Before | After |
|---|---:|---:|
| Consumed supported lexical coverage | 104 | 104 |
| Owner has withheld mappings | 235 | 235 |
| Unmapped owner match | 140 | 140 |
| Rejected/non-resolving match only | 18 | 18 |
| No exact casefold name match | 61 | 60 |
| Multiple lexical owners | 6 | 6 |
| Ambiguous current owner | 1 | 1 |
| Downstream material hold | 26 | 26 |
| Blank source label | 1 | 1 |
| MIM name absent from consumed supported export | 366 | 367 |

## Applied decisions and generated products

- **#1149 — MediaDive 1315:** add `Na acetate x 3 H2O` to the existing `Sodium_Acetate_Trihydrate` owner (`CHEBI:32138`, CAS 6131-90-4). MediaDive, ChEBI and PubChem captures support that supplied hydrate; MediaDive's discrepant formula was not copied. Receipt 27 withdrew inherited support, then a [fresh mapping-only review](sodium-acetate/mapping-followup-decision.json) assessed the changed owner and all six published alias tokens. No role or whole-record approval was added.
- **#1151 — 3-methylacetate:** correct active notes and append history because raw record 19685 contains this literal minor product. The guessed mercaptopropionate/importer-fragment explanation is superseded; historical wording is preserved. `UNMAPPED_0736` remains **REJECTED**, with no ontology mapping or inferred replacement. Its reconciliation entry changes only the owner hash.
- The native SSSOM diagnostic contains **3,007 rows** and was not adopted wholesale: it also differs in unrelated row membership and local registry namespaces. The guarded publication updates only canonical position 2556 (`source`, `mapping_date`, `other`), with corresponding header dates, retaining **3,014 canonical rows**.
- The [native unified rebuild](unified-generation/traced-rebuild.json) retains **4,170 rows in the same order**. All **13 changed cells across eight rows** trace to the same sodium acetate trihydrate owner: seven existing synonym cells and six cells resolving the already-present source spelling. No other owner changes. TSV SHA256 `c12f09602dbb4be511c6e813b046fe5965a42134a124a2b3678deb3880591b70`; native provenance SHA256 `7175c41748e60418b6e57a984eb8450aa20ed64b1015286a52aff4ec1c0256f4`.

Native full-graph regeneration also withdraws one inherited sodium acetate physicochemical-role approval because its owner bytes changed. That role remains OPEN under the broader #718 backlog; this mapping-only review does not re-approve it. [Exact disposition delta](semantic-disposition-delta.json) records the sole status transition and the changed mapping assertion identity.

The immutable [candidate reviewed generation](candidate-reviewed-sssom/manifest.json) contains **1,739 SUPPORTED / 1,275 WITHHOLD** rows, unchanged in count. Supported predicates remain 1,737 exact and two reviewed broad mappings (#1156). The withheld TSV is byte-identical. `PASS_SUPPORTED_SUBSET` is not a full-corpus scientific pass.

| Artifact | Frozen KG-consumed SHA256 | Candidate SHA256 |
|---|---|---|
| Canonical source | `d5f76fc404967477903fafc79eaba86ecfef9e2c391926ec08c3c1af4a5220b6` | `097b612c4cce6144a426b64757ea76d447c1d12efcee540dfaac0b6ce163c221` |
| Reviewed manifest | `b02a92446e8a613fd0d96b0dd8147d439733fcf73e731b363a6388e95d616703` | `86cc8cec342e5aa28373abcd59c90e428d3fcfedeef646234a323bb31142bc67` |
| Supported TSV | `7e68fea7fd788928f29c7671156198af101baaa3b3051f19bab78a5479d2a940` | `204c7909ecad9762704d950693210a4e25b53fdac2fdb2e8e6689270889d64cd` |
| Withheld TSV | `5817fb845c65f995fb0c78095168af1cbf0c837a991004fcd0a9d73cd0874c88` | `5817fb845c65f995fb0c78095168af1cbf0c837a991004fcd0a9d73cd0874c88` |
| Disposition TSV | `2a075c9c4a699c9d22a5e8b736bc6d7c00c344f19363f28178c0b50b6b590a19` | `b04cf2ad39e5f3574fcc01de87e9a789c6ecd8e9dc088327cb63368ea0b5efb2` |

## Preserved holds and remaining decisions

All [10 MicrobeDecoder compound IDs](scientific-holds/microbedecoder-holds-v1.md) retain **225 exact source assertions** and unresolved material identities, including two distinct sugar source IDs. No generic sugar identity, universal medium recipe, gas ratio or component-specific utilization is inferred. Exact record hashes, predicates and citations remain bound to the holds.

[Five targeted MediaDive cases](scientific-holds/targeted-mediadive-holds-v1.md) remain for **#1157**, which this batch does not close: Tris 331 needs complete alias-scope review; calcium pantothenate 1512 needs D/DL and unrelated-alias review; nitrilotriacetate 1930 needs a distinct monohydrate identity; silicate 2160 needs pentahydrate and stock context; maltose 776 has contradictory hydration metadata. Existing WITHHOLD and REJECTED_LABEL decisions remain. These five targeted scientific holds are not the same count as the ledger's 26 downstream-held candidates.

The [bounded diagnostic synthesis](reconciliation-synthesis/README.md) covers every candidate and all 61 original exact-name nonhits; 60 remain after the one alias. Formulas, hydrates, preparations, explicit alternatives and biological materials need the stated primary-source or product decisions. No bulk curation is implied.

## Implementation and verification

The PR also addresses typed history compatibility (#1150), direct-record inventory (#1152), hard-linked target and late-manifest protections (#1153–#1154), output-parent substitution (#1155), and supported-predicate documentation (#1156). Reconciliation uses the native current review and a coherent consumed partition; source names never override native dispositions or material holds. The [focused reconciler receipt](reconciler-1155-validation-v1/receipt.json) records 47 passing tests and Ruff/Black checks.

Local validation passed: `just qc` (including native SSSOM, round-trip and flat-export checks), reviewed SSSOM export/schema replay, supported KGX and companion exports, native unified freshness/rejections, Ruff/Black/Mypy, and all 1,018 saved native reviews. The complete pytest run finished with **4,898 passed, 525 skipped, 31 warnings and zero failures**; package coverage is **79%** against the unchanged 35% floor. The skipped tests are reported as skipped, not as executed passes. See [local execution evidence](validation-final/local-checks.json).

The [final independent native review](../../reviews/structured/20261108T033443Z-kgm-unmapped-final-independent-review/review.yaml) and [rendered assessment](../../reviews/structured/20261108T033443Z-kgm-unmapped-final-independent-review/review.md) cover 82 declared targets and 432 exact inputs. It resolves five prior findings (#1150 and #1153–#1156), identifies no new finding in that scope, and returns **pass with limitations**. The reviewer used an actual durable `0dac2784` overlay with working-tree provenance; the separate committed-head audit binds the same implementation bytes to `cd76b3e5`. This is limited mapping/source science and implementation review, not corpus, role, publication or merge approval.

The [recorded CI observation](validation-final/ci-cd76-observation-v1.json) has 15 successful checks and pytest still running at implementation head `cd76b3e5`. Final published-head attestation and complete CI are separate outstanding checks; they are not represented as passed by this local review. The PR records their later actual outcome.

## Downstream adoption

This is a separate paired candidate for later adoption. A downstream reviewer must bind the final approved MIM commit, the complete supported/withheld/disposition/manifest generation, and the unified TSV/native provenance pair; verify their hashes and scientific holds; and run KG-Microbe's own admission checks. The [native adoption guard inspection](downstream-adoption-inspection.json) confirms KG-Microbe requires its separate reviewed-release refresh; the old context-free lookup cannot consume this candidate directly. No prospective KG resolution count is claimed. The active KG checkout, mapping inputs and build were not changed. No downstream rebuild or merge is part of this task. No paid provider credits were used.
