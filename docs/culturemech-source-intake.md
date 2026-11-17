# CultureMech source intake

Issue [#1453](https://github.com/CultureBotAI/MediaIngredientMech/issues/1453)
owns a separate, reviewed intake of CultureMech's structured variant inventory.
The active unmatched campaign retains its frozen manifest. An intake never
curates MIM records, changes canonical mappings, or installs a KGM release.

Use an isolated worktree and a new directory for each revision. Obtain the
handoff receipt SHA256 independently from its reviewed producer issue or release
record. A digest copied from the input directory is not an independent pin.

```bash
just culturemech-intake prepare \
  --handoff .temp/culturemech-handoff \
  --expected-handoff-sha256 <independently-recorded-sha256> \
  --producer-python <python-from-the-locked-producer-environment> \
  --output .temp/culturemech-intake-revision-1
```

The receipt binds the producer, bundle manifest, source archive, original prose
queue and coverage audit. The adapter verifies those bytes, all contractual
products and coverage membership/current recipe hashes. It extracts the verified
archive temporarily and runs that producer's native verifier before consuming
the tables. `--producer-root` may select an existing extracted copy, whose inputs
and implementation must match the pinned manifest before its code runs. The
environment must already contain the locked producer dependencies: this command
installs nothing and makes no network calls.

The explicit registry accepts `culturemech-direct-ingredients-v2` (six products)
and `culturemech-direct-ingredients-v3` (those six plus
`variant_ingredient_holds.tsv`). Unknown contracts/actions fail. V3 `SET_AMOUNT`
and `change_json.amount` preserve literal batch or unspecified-percent amounts;
they never populate concentration columns or imply a dilution calculation.

Prepared artifacts include:

- `source/`: the exact handoff inputs, including positive occurrences and the
  complete variant change ledger; v3 also retains the quarantined hold ledger.
- `source-mentions.tsv`: all positive occurrences and context-only descriptors,
  with original columns and source row coordinates. Positive ledger rows are
  not counted twice. V3 held mentions remain in `source-held-mentions.tsv`.
- `review-packet.json` and `review-cases.tsv`: cases grouped by exact raw label,
  upstream identifier, action, stage, role and variant name. Full descriptors,
  change payloads and every source occurrence coordinate/hash are retained.
  Held cases additionally preserve their exact unresolved field dimensions.
- `canonical-reviewed-sssom/`: freshly regenerated native supported and withheld
  SSSOM partitions, complete dispositions and manifest, validated against MIM's
  current content-bound scientific review.
- `intake.json`: source, owner-record, native review and product hashes, coverage
  dispositions and explicit pending-source-review status.

Candidates use current preferred terms and resolving synonyms, excluding
rejected labels. Classifications distinguish agreeing ID and label, missing
source ID, conflicting ID, ambiguous owners, known unmapped owners and no active
owner. A candidate does not authorize an identity binding.

`counts_as_presence` is inventory membership, not a physical-presence assertion.
Zero-concentration targets remain change events. `REMOVE` and old `REPLACE`
descriptors remain context-only, including labels absent from positive inventory.
Stock culture, timed additions, exposure assays and preparation stages stay
separate. No complete variant formulation or stock expansion is inferred.

V3 held mentions always retain `review_status=WITHHELD` and
`counts_as_presence=false`. `SOURCE_CLAIM` or `IDENTITY_FORM` uncertainty blocks
a supported identity binding. `QUANTITY`, `OPERATION` or `STAGE` uncertainty does
not automatically invalidate a separately reviewed identity: a binding may be
supported while those source assertions remain withheld. It still creates no
positive occurrence. A hold never demotes other supported cases globally.

## Review and finalize

Inspect actual source evidence, descriptors, stage and candidate MIM records.
Use the native [mapping skill](../.claude/skills/map-media-ingredients/SKILL.md)
and [record review profile](record-review-profile.md). Preserve negative reviews
and source holds. A justified `WITHHOLD` is a finished outcome; an unreviewed
placeholder is not completed review.

The binding-review JSON has `schema_version: 1`, `intake_sha256`, an `inputs` map
of repository-relative evidence files to SHA256, and one decision per case.
Decisions contain `case_id`, native `row_sha256` of the **complete case**,
`owner_record`, `disposition` (`SUPPORTED`/`WITHHOLD`), `review_reason`,
`review_evidence` and `evidence_key`. The evidence JSON's named `entries` item
repeats payload hash, owner path/hash, disposition and reason. This reuses the
native complete-payload verifier used by reviewed SSSOM and companion exports.
Save the independent narrative review through the immutable structured-review
workflow as well; the JSON proof does not replace scientific assessment.

For a unique candidate, use its exact MIM owner path/hash. Otherwise use
`source/bundle/manifest.json` and its pinned SHA256, retaining a source-owned hold
without inventing a MIM identity. A `SUPPORTED` decision additionally names
`canonical_row_sha256` from that unique owner's current native supported
exact-identity rows. Source review cannot override a withheld canonical mapping.
Withheld decisions must not assert a supported canonical row.

```bash
just culturemech-intake finalize \
  --intake .temp/culturemech-intake-revision-1 \
  --expected-intake-sha256 <intake-json-sha256> \
  --review reports/culturemech-intake/revision-1-binding-review.json \
  --output .temp/culturemech-reviewed-intake-revision-1

just culturemech-intake verify \
  --intake .temp/culturemech-intake-revision-1 \
  --expected-intake-sha256 <intake-json-sha256> \
  --review reports/culturemech-intake/revision-1-binding-review.json \
  --output .temp/culturemech-reviewed-intake-revision-1 \
  --expected-reviewed-sha256 <reviewed-intake-json-sha256>

uv run --frozen python scripts/validate_reviewed_sssom_schema.py \
  .temp/culturemech-reviewed-intake-revision-1/canonical-reviewed-sssom
```

Finalization checks every source artifact, complete MIM record membership,
native review, canonical partition and binding proof. It emits supported and
withheld binding tables, retained evidence, unchanged canonical SSSOM partitions
and a receipt. Verification independently rebuilds the expected products and
compares all bytes. Existing outputs are never replaced. Record and pin the
separate native SSSOM parser/schema QC result too.

A later integrated release must explicitly select the source revision,
reconcile current KGM inputs and complete the applicable scientific/publication
gates. This workflow does not close independent campaign release trackers.
