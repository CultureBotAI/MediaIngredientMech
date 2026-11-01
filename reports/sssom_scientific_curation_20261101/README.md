# Scoped mapping corrections and publication decision

This standalone batch starts from MIM main `4625afd492b6cf43e3b499d1425d2453d490009d`
and uses an isolated Claw checkout at merged commit
`d8f95e7ec5769d6c49ead59663ac67e323868b72`. It neither advances a cycle nor
claims a supervisor binding. The shared M5 Claw checkout, the qc-evidence
workflow, unified mapping and installed workflow profile were not changed.

The canonical SSSOM remains **2,987 rows**. Exactly nine existing rows change:
two regenerated carnitine rows, and seven rows whose only change is removal of
one verified false `other` token. No rows are added, deleted or repositioned;
2,978 complete row payloads remain identical. Header dates now follow the
newest actual curation date, 2026-11-01. The sole YAML correction changes the
carnitinamide alias to `REJECTED_LABEL` and records its provenance; synchronized
exports remove that alias. The separate `DL-carnitine` token is deliberately
retained pending its identity decision. Its historical provenance survives in
the before-row receipt; fresh generator provenance is not evidence approving it.

The [native receipt](../sssom_completion_20260921/mapping_changes/issue669-1003-scoped-alias-corrections.json)
binds eight owners and every changed row, without carrying approval across
changed content. Reviewed release counts are **1,740 supported / 1,247 withheld**.
Only one prior disposition changes: the carnitine local registry row moves from
SUPPORTED to WITHHOLD after its owner changes. Every other disposition is
preserved. The native semantic integrity check passes; scientific release
remains FAIL with 1,733 blocking findings and 2,272 assertions (previously
2,271). No role or component approval is inferred from these mapping repairs.
The regenerated semantic disposition table rebinds all 2,987 mapping assertions
to the new whole-file source hash; this is not 2,987 scientific re-reviews.

| Issue | Decision and evidence |
| --- | --- |
| [#669](https://github.com/CultureBotAI/MediaIngredientMech/issues/669) | Retire exactly seven independently supported generated aliases; Rule K baseline 45 → 38. Preserve seven generic/stereochemical policy cases, 23 pairs overlapping PR #912, and eight identity/alias cases. [Complete pair audit and sources](audit669/README.md); [scientific seven-token review](../../reviews/structured/20261101T005710Z-seven-generated-alias-rulings/review.md). |
| [#718](https://github.com/CultureBotAI/MediaIngredientMech/issues/718) | Reproduce the native release, correct stale release-guide counts, and inventory all 1,247 withheld rows across 1,001 owners. [Final exact reasons and counts](audit718/final/classification.md). This classification grants no new scientific approval. |
| [#875](https://github.com/CultureBotAI/MediaIngredientMech/issues/875) | Exact **NCIT:C61946** exists for sodium phosphate dibasic heptahydrate. NCI binds CAS 7782-85-6, seven waters and UNII70WT22SF4B; §3 step1 precedes CAS fallback. Defer atomic identity/ledger/SSSOM/unified change because PR #914 changes the same unified row. Existing anhydrous structure and provisional BUFFER concerns remain open. [Scientific review](../../reviews/structured/20261101T004549Z-na2hpo4-heptahydrate-exact-identity/review.md). |
| [#901](https://github.com/CultureBotAI/MediaIngredientMech/issues/901) | Current cohort has 72 CLOSE_MATCH records: 68 in PR #912, two with PR #914 ledger overlap, and two source-supported corrections blocked by PR #764's approval supersession dependency. Both melezitose and sodium perchlorate remain unchanged. [Audit and preserved failed attempt](audit901/audit-report.md); [blocked melezitose review](../../reviews/structured/20261101T005659Z-melezitose-formof-blocked-review/review.md). |
| [#1003](https://github.com/CultureBotAI/MediaIngredientMech/issues/1003) | Reject the verified carnitinamide name left in Carnitine_Hydrochloride after its earlier mapping repair. Official ChEBI48601 versus17126 establishes the amide/carboxylate difference. [Scoped scientific review](../../reviews/structured/20261101T005710Z-carnitine-amide-alias-scientific/review.md). |
| [#1006](https://github.com/CultureBotAI/MediaIngredientMech/issues/1006) | Independent review found receipt/backup collisions could overwrite evidence or fail after a YAML write. The maintained writer now reserves exclusive outputs before touching the owner, with collision regressions. The blocked melezitose helper and its corresponding fix are archived, not installed as an executable curation step. |
| [#1008](https://github.com/CultureBotAI/MediaIngredientMech/issues/1008) | CI exposed stale dependency pins in the optional ingredient bundle. A [successor review](../ingredient_bundle_20261101/review.json) preserves the historical review and advances only three container hashes after proving that all 20 owners, 51 claims, selected mapping payloads, complete scientific decisions/evidence, schemas and semantic metadata remain unchanged. Date/version headers alone advance with the canonical curation date. No approval or exporter guard is changed. |
| [#1009](https://github.com/CultureBotAI/MediaIngredientMech/issues/1009) | Independent review of the companion repair found that identical CLI destinations could collapse before the output writer checked them. The helper validates the ordered resolved destinations before reading inputs or writing files, with no-write regressions for duplicate and aliased paths. |

## Whole-candidate promotion decision

**Do not replace the entire canonical file with the raw regenerated candidate.**
The final safe-scope raw candidate has 2,980 rows and zero native invariant
rejects, but replacement would change 2,364 existing payloads, remove ten rows
and add three. Of the currently supported rows, 1,329 would have changed
payloads. Differences include source provenance, dates, explanations,
confidence/justification, labels, synonyms and registry namespaces. Those
differences do not acquire scientific approval from a successful build.

The proposed canonical update is only the nine-row change described above.
[Every changed canonical field](generation/canonical-row-change-summary.json)
and [every raw-candidate delta](generation/ready-promotion-row-delta.json) are
retained separately. The native [mechanical review](../../reviews/structured/20261101T005659Z-scoped-sssom-promotion-check/review.md)
does not replace the three narrow scientific claim reviews or their limitations.

| Local artifact | Meaning |
| --- | --- |
| `output/sssom-scientific-audit/baseline.sssom.tsv` | Untouched main input, before curation; 2,980 rows. |
| `output/sssom-scientific-audit/final.sssom.tsv` | Historical attempted melezitose+carni proposal, 2,981 rows; blocked by native release pins and excluded from this PR. |
| `output/sssom-scientific-audit/ready.sssom.tsv` | Definitive final raw diagnostic for the safe scope, 2,980 rows; SHA256 `084fd8cfc300272a0dcb220ebc1ca2076aee83229e3847cf64e0c1ca1c37359b`. |
| `mappings/ingredient_mappings.sssom.tsv` | Scoped canonical proposal, 2,987 rows; SHA256 `f408f36b9de77c2089a07907b40d6a27401087e13528f0597a6cf7b386048ac0`. |

Full diagnostic TSVs and large external inputs remain local. Their exact paths,
revisions and hashes are in [generation provenance](generation/generation-receipt.json)
and the [input manifest](generation/validation-inputs.json). CultureMech remains
comparison input, not a bulk import. KG's actual unified mapping is the builder
input; its Mediadive nodes are a separately hashed comparison source.

## Checks and remaining decisions

Final `just qc`, reviewed SSSOM export/validation, supported KGX export/validation,
semantic integrity, canonical/candidate invariants, schema/CURIE/label checks,
165 focused MIM tests, 84 merged-generator tests and changed-code Ruff checks pass.
Canonical and candidate have no GAP/ORPHAN/STALE/predicate/grade drift. Native
limits remain explicit: BTO/MICRO B4 transforms unavailable, adapter skips,
nonblocking label warnings, six tracked cross-prefix node-ID differences,
38 Rule K obligations, and 18 non-gating opaque-subject filename warnings.
The [command receipts](generation/logs/) distinguish successful final checks,
earlier setup failures and the superseded blocked-proposal checks.

The initial PR CI run additionally exposed the optional companion-bundle
dependency failure tracked in #1008. Its immutable successor passes native
export, manifest-pinned replay, 72 focused bundle tests and Ruff. The final
helper reproduces the successor review byte-for-byte. The historical review
is preserved; the [successor audit and check receipts](../ingredient_bundle_20261101/README.md)
distinguish unchanged scientific claims from changed global dependency hashes.

Human scientific decisions remain on [#669](https://github.com/CultureBotAI/MediaIngredientMech/issues/669)
(generic/stereochemical alias publication policy),
[#1004](https://github.com/CultureBotAI/MediaIngredientMech/issues/1004)
(DL-carnitine hydrochloride versus free-base CAS), and
[#1005](https://github.com/CultureBotAI/MediaIngredientMech/issues/1005)
(sn-glycerol-3-phosphate lithium salt versus free-acid CAS). Options, primary
evidence and recommendations are recorded on those issues. All six mapping
rows for the latter two records remain WITHHOLD. No identities were guessed,
records merged, old scientific reports overwritten, or paid provider credits used.
