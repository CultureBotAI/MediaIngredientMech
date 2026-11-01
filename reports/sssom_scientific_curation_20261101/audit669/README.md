# Scoped synonym and identity audit (#669)

This directory preserves the audit of main `4625afd492b6cf43e3b499d1425d2453d490009d`, primary database snapshots, native checks, and narrowly authorized curation evidence. It is not whole-record or release approval. The parent report and native review bundles describe the final publication state.

## Frozen baseline and ownership

`inventory.json` measures 2,987 canonical rows and all 45 current Rule K collisions: 25 `HYDRATE_FAMILY_UNREVIEWED`, 20 `UNREVIEWED`, zero new failures and zero unused baseline entries. Native preferred-name ownership follows merge representatives; none of these current 45 pairs depends on retired-owner credit. The evidence includes an ignored-inclusive search over the original reports, notes, history and skill directories, plus specifically read prior generation and repair outputs; it does not claim an unbounded filesystem search.

Seven colliding tokens are actual YAML synonyms; 38 are generated-only. Only six of those 38 are recoverable from today's KG target-alias loader. Missing from a current dictionary is not evidence of chemical falsity. `pair-dispositions.json` and `.tsv` retain exact selectors, owners, hashes, source distinctions and proposed dispositions.

- Seven YAML cases remain unchanged: beta-lactose, D-mannitol, L-asparagine, L-cysteine, L-glutamic acid, L-proline and L-tryptophan. Current ChEBI asserts the beta-lactose generic label only as related; the other six have exact as well as related assertions. Current label-index ordering already selects the generic preferred-name owner for all seven. Unqualified SSSOM alias policy is a separate unresolved choice.
- Twenty-three generated-only pairs overlap subject or owner records in open PR #912.
- Eight generated-only pairs require identity or commercial/common-name adjudication. These include shared ontology IDs, a demonstrably same-substance sodium succinate pair, and explicit source-identity contradictions. They are not blanket-retired.
- Seven generated-only tokens have independent evidence of a salt/free-acid, hydrate/anhydrous, different salt/hydrate, or stock/solute distinction. Their exact before/after transform is in `seven-alias-apply.json`, with unchanged YAML owner hashes. `seven-removal-feasibility.json` preserves the original release pins: all 18 rows owned by those seven records were already withheld. No support may be inferred from the cleanup.

## Authorized local corrections and retained questions

Issue [#1003](https://github.com/CultureBotAI/MediaIngredientMech/issues/1003) records the residual carnitinamide IUPAC synonym on Carnitine Hydrochloride. Official ChEBI:48601 assigns the name to the amide, a different functional group from carnitine. The guarded writer retained the name and original source as `REJECTED_LABEL`, appended actual-process/LLM history, and preserved all other scientific fields. The original owner bytes, apply log, strict/term checks and exporter regression tests are retained here. `DL-carnitine` is a different, unresolved parent-name alias: it remains in canonical `other` and the Rule K baseline pending source-backed salt/stereochemistry adjudication.

Issues [#1004](https://github.com/CultureBotAI/MediaIngredientMech/issues/1004) and [#1005](https://github.com/CultureBotAI/MediaIngredientMech/issues/1005) separately track hydrochloride/free-base CAS and lithium-salt/free-acid CAS contradictions. No replacement identifiers, stereochemistry or merges were guessed. All six native mapping rows owned by these two records are already `WITHHOLD`; `identity-issue-existing-holds.json` records their exact selectors/positions and content-bound review hash. The exact #669 policy/options and pre-fix seven-pair comments are preserved with their live URLs.

The seven-token migration removes only the selected `other` values and their seven matching baseline obligations (45 to 38), while preserving every other field and all YAML. `post-apply-alias-proof.json` is a timestamped proof against canonical immediately before that migration; the preceding subject-block splice is a separate operation. Any later release decision must use the final native review/receipt, not assume this intermediate hash is current.

## Reproduction and scope

The maintained bounded writers are `scripts/reject_carnitinamide_synonym.py` and `scripts/retire_reviewed_generated_aliases.py`. Both default to dry-run. The latter requires an actual final native candidate that independently omits every selected token, exact row and baseline selectors, and matching unchanged owner hashes. Source-specific regression tests and actual command/exit/log-hash receipts are under `logs/`; shared full-data checks are recorded in the parent report.

The diagnostic Python files in this directory record the original isolated run recipe and absolute input locations. They are not alternate source writers. Primary OLS/PubChem responses are saved in `sources/`, with capture URLs, times and hashes in the source manifests. The prior repaired candidate is comparison evidence only; `prior-candidate-input-comparison.json` confirms that all 2,953 original maintained record hashes match that prior generation's input manifest. It does not make that diagnostic candidate canonical.

Complete live PR file snapshots contain 141 paths for #912 and 46 for #914. These seven pairs and the #1003 record do not intersect their source-record paths. Shared aggregate/export paths overlap, and #912 also touches canonical SSSOM; changes must remain selector-specific and preserve the other work. No unified mapping rebuild or broad native-candidate promotion is part of this audit.

## Final scoped observations

The safe-only final surface was rechecked in `final-scoped-verification.json`: 2,987 canonical rows, 1,740 supported and 1,247 withheld; the Rule K baseline contains the exact remaining 38 pairs. The seven selected rows differ only in `other`, their owner YAML is unchanged, and all 18 native owner rows remain withheld. Carnitine Hydrochloride retains `DL-carnitine` as a deferred canonical alias; its corrected amide name is absent from resolving exports and both owner mappings are withheld. The six rows in #1004/#1005 also remain withheld.

The native guarded saver validated and saved these distinct scientific observations:

- [Amide claim review (Markdown)](../../../reviews/structured/20261101T005710Z-carnitine-amide-alias-scientific/review.md) and [authoritative YAML](../../../reviews/structured/20261101T005710Z-carnitine-amide-alias-scientific/review.yaml).
- [Seven alias rulings (Markdown)](../../../reviews/structured/20261101T005710Z-seven-generated-alias-rulings/review.md) and [authoritative YAML](../../../reviews/structured/20261101T005710Z-seven-generated-alias-rulings/review.yaml).

Both are explicitly self-reviews with `pass_with_limitations`, covering only the listed claims. The separate root review covers deterministic publication checks, and independent review remains separately recorded. Final maintained code passed 48 scoped regression tests. Draft review serialization/schema errors are retained in the command receipts; corrected final documents validated and saved successfully. No saved historical review was rewritten.
