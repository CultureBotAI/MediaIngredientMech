# Worker09 coordinator handoff

Review complete: **187/187 source cases**, all with primary evidence and a separate skeptical review. **32 isolated owner proposals** (25 existing-owner edits, 7 new owners), affecting 53 assigned cases. **49 cases remain explicitly unresolved**; review completion is not identity resolution or export approval.

Branch: `review/all-unmatched-w09-source-review-20261107`. Frozen base: `e000d66dd26ab053e9b17ce7bf8d3c873c3dde99`, with unmerged dependency [MIM PR1158](https://github.com/CultureBotAI/MediaIngredientMech/pull/1158). The final pushed commit SHA is reported in the worker final message; this handoff and its manifest are part of that ordinary branch commit. No worker PR, merge, cleanup or downstream rebuild.

## Authoritative artifacts

Use root [decisions.json](decisions.json), [evidence.json](evidence.json), [proposals.json](proposals.json), [progress.json](progress.json), and [structural-audit-final.json](structural-audit-final.json). Subgroup decisions preserve the primary-author stage with pending reviewer fields; root decisions attach the actual completed peer receipts after exact scientific-payload checks. Do not count subgroup/round snapshots as additional source cases.

The exact shard bytes are copied in [common/frozen-shard-09.json](common/frozen-shard-09.json), SHA256 `cb12696153cb5d9aa50db98542df76757d024d85b5ad73944893e4a0ee3555c0`. It contains94 CultureMech cases with168 occurrences across155 full recipes, and93 KG cases. KG empty occurrence-ID lists retain the original graph/source count definitions in the complete case objects. The155 full recipe copies preserve exact frozen bytes; they are evidence, not edited CultureMech records.

| Artifact | SHA256 |
|---|---|
| `decisions.json` | `fe923a82f96b10bd99ec6f61612241a37fc08ab6786a08c2d17e45c84ab4e556` |
| `evidence.json` | `a4ffe505c8d9297770de38910c105a865b6c25bfb68e5a2ea33ee72789f4686c` |
| `proposals.json` | `ebd5c81f285ed6f41e76974012143990b33528a2beb4f9930f52b56d6469ab8e` |
| `structural-audit-final.json` | `6d1bf5cc0e5e1528e58a3586b896fa6fcd924caf9835466329b774b643ce7ad6` |

[MANIFEST.json](MANIFEST.json) records exact artifact paths and hashes, including the native review pair. The manifest excludes itself and the later final-assembly reviewer receipt to avoid a hash cycle; that receipt binds the manifest independently.

## Actual review scopes

| Primary author | Primary cases / proposals | Separate skeptical reviewer | Final receipt |
|---|---:|---|---|
| `/root/antibiotics` |58 /7| `/root/salts` |[58-case review](salts/review-of-antibiotics/review-final.json)|
| `/root/materials` |60 /10| `/root/antibiotics` |[60-case review](antibiotics/review-of-materials/review-final.json)|
| `/root/salts` |69 /15| `/root/materials` |[69-case review](materials/review-of-salts/review-final.json)|

[agent-scopes.json](agent-scopes.json) lists every exact assigned case ID and actual role. [Independent bindings](validation/independent-review-bindings.json) check each final decision hash excluding only `independent_review`, plus the reviewed proposal/evidence files and actual captured bytes. No additional external sessions or paid research were used.

Six scientific reviewer findings were corrected and re-reviewed: ordinary Casamino acids now uses exact MeSH C017721 instead of unnecessary registry fallback; its inherited0.01% fragment remains RAW_TEXT pending claim-specific evidence; recovered JCM 1118 is no longer described as unavailable; added-water amounts are separated from asserted final volumes; the recovered Allen calcium stock is now a concrete proposal; an unrelated JCM197 citation was removed from the NBRC 1160/TOGO M1901 case. Initial findings, author responses, capture attempts, and final re-review are retained. First-round materials proposal bytes were overwritten before the reviewer copied them; observed original hashes remain, and subsequent/final exact inputs were copied and checked.

[Integration-helper review](antibiotics/review-of-integration/integration-helper-review.json) also closed three mechanical guard gaps with controlled tests. [Final assembly review](antibiotics/review-of-integration/final-assembly-review.json) records the independent assembled-artifact/diff review.

## Proposed changes and retained boundaries

Seven new owners are proposed: iron(II) chloride dihydrate CAS 16399-77-2 with asymmetric CHEBI:30812 parent; exact (R,R)-butane-2,3-diol CHEBI:16982; methyl cellulose CHEBI:53448; sodium syringate CHEBI:132110; source-specific JCM 226 Czapek concentrate; JCM 629 artificial saltwater; and TOGO M2231 calcium chloride dihydrate stock (2.5 g/L). Water addition is not treated as measured final volume. Stock components are not exact identities of the whole stock.

Existing-owner candidates include three antibiotic promotions (Collinomycin, Aburamycin A and Cinerubin A), evidence/quality updates for Glebomycin/Hitachimycin/Vulgamycin, explicit Angustmycin ambiguity, ordinary Casamino exact material identity, and verified source-specific salt/material spelling aliases. Exact before/after bytes, evidence IDs, source backlinks and integration obligations are in proposals.json.

| Final disposition | Cases |
|---|---:|
| `existing_identity_or_alias` | 71 |
| `stock_product_mixture_context` | 48 |
| `unresolved` | 49 |
| `malformed_or_nonchemical_token` | 5 |
| `new_distinct_ingredient_proposal` | 6 |
| `broad_parent_relation_only` | 7 |
| `supplied_form_correction` | 1 |

## Findings filed

- [MIM1171](https://github.com/CultureBotAI/MediaIngredientMech/issues/1171): bare Geomycin does not choose between the historical mixture and oxytetracycline trade-name sense.
- [MIM1175](https://github.com/CultureBotAI/MediaIngredientMech/issues/1175): bis-nitrophenyl assay labels conflict with linked ChEBI structures; obtain original reagent evidence.
- [CultureMech673](https://github.com/CultureBotAI/CultureMech/issues/673): residual Waris-H Dissolve rows and Fe-EDTA preparation/dose hierarchy.
- [CultureMech674](https://github.com/CultureBotAI/CultureMech/issues/674): BB MoO3 subscript loss and trace-stock hierarchy.

Live issue bodies, relevant comments, dedup results, primary evidence and exact filed text are under common/. Existing issues #408, #741/#745, #1053 and #1108 and the other cited prior scientific decisions remain separate obligations. No broad new tracker replaces them.

## Coordinator dependencies

- **Thiamine/w05:** same existing owner SHA 627c0ae9…; CHEBI:9532 exact row remains WITHHOLD. The chloride-bearing structure/aliases conflict with the pure-compound target. CAS 136-09-4 is not chloride CAS 154-87-0 and must not be removed solely from the old combined reason. Source Co-carboxylase still needs its supplied form; the 0.2% stock remains distinct. No shared-owner edit was made.
- **MnCl2 tetrahydrate/w02:** shared existing owner; w02 source MnCl4 x 4 H2O is a separate claim, not an adopted equivalence.
- **Tryptone/w03:** the proposed Tryptone owner spelling additions overlap the baseline RELATED_SYNONYM hit for Pancreatic digest of casein. Reconcile exact owner bytes before integration without claiming the other source case.
- **Other lexical candidates:** Soy/Phytone owners link w05/w08; water and ketoglutarate rejected/raw aliases link other shards. The complete 17-candidate ledger is [common/cross-shard-lexical-owner-candidates.json](common/cross-shard-lexical-owner-candidates.json). These are dependency candidates, not 17 approved identities or reviews of other shards.

The shared primary cache manifest was verified as `0a8c6b1d8fd3a60de0b5c269613cf25e30ee94f4ae20aa987679639d603e27d5`; reused captures retain original bytes and access times. Cache integrity confers no source-case, owner or export approval.

## Validation and native review

- Whole-shard structural audit: PASS,187 accounted and187 independent statuses complete,563 evidence entries,32 proposals; `scientific_adequacy_or_approval_established:false`.
- Closed-schema validation:32 isolated YAML payloads,0 errors.
- Read-only full-corpus proposal overlay:0 baseline and0 candidate partonomy violations; no introduced active identifier collisions; append-only history and before/after hashes checked. All 5,184 protected baseline files unchanged.
- Seven assembly controls and 22 campaign auditor controls pass. Independent helper review records 16 additional controlled checks.
- Native inspect/validate/save succeeded. Repository-wide append-only native check passed against the frozen base (1,020 valid retained reviews); the actual log is [validation/native-check-final.log](validation/native-check-final.log).

Native [YAML](../../../reviews/structured/20261108T053020Z-worker09-complete-source-review/review.yaml) and [rendered Markdown](../../../reviews/structured/20261108T053020Z-worker09-complete-source-review/review.md) declare full 187-case coverage, completion `completed`, verdict **needs_curation**. This is source-case identity/form/preparation review, not full-payload publication approval.

Canonical YAML/aggregates/SSSOM/unified products, semantic review selectors and publication selectors were not changed. Full synchronization/export/rebuild gates were intentionally not run because the campaign reserves maintained integration and downstream builds for the coordinator. The coordinator must use guarded writers, reconcile shared-owner edits, withdraw inherited content-bound support for changed owners, refresh native complete-payload review and exports, and run the maintained gates. Every unresolved source case retains a precise `missing_requirement`; no uncertainty is erased by structural PASS.
