# Identity corrections complete; full semantic approval still FAIL

The correction batch addresses all **14 identity blockers** in the preceding
snapshot: **11 corrected or merged**, and **three unsupported mappings withdrawn**.
The latter remain explicitly `AMBIGUOUS`: Artepaulin, 2-tetrachloroethane, and
2-dimethylsuccinic Acid. Original source identity evidence is still needed.

Twenty current records were changed or added, including four merge survivors,
one restored trisodium-nitrilotriacetate record, and the monobasic-phosphate record
that must receive its own source label. The disodium stock and trisodium substance
are now distinct. Manufacturer evidence also refined the hydrate finding: the CAS
is used for both forms, so the hydrate has a local identity and retains the
supplier CAS as procurement metadata.

## Current MIM-only artifacts

| Metric | Count |
| --- | ---: |
| Maintained source records | 2,952 |
| Mapped / unmapped / ambiguous / rejected | 2,610 / 261 / 3 / 78 |
| Active ingredient nodes | 2,874 |
| All KGX nodes, including referenced identifiers and roles | 5,787 |
| KGX assertion edges | 4,525 |
| Unique subject–predicate–object triples | 4,519 |
| SSSOM mapping rows | 3,016 |
| Role assertions | 988 |
| Component assertions | 506 |

The graph is in `output/mim-kgx-20260921-identity-corrections/`. Its deterministic
archive SHA256 is
`eddb7a634749520d35bd90219ab3034080db8feddcebeec1481bbc1e7e27fa83`.
These counts describe MIM's ingredient assertions and their referenced terms;
no KG-Microbe ontology graph is imported.

## Validation and review

- SSSOM JsonSchema, PrefixMapCompleteness, and StrictCurieFormat pass. Existing
  custom metadata/column warnings remain informational.
- MIM mapping invariants and currency pass. The separate ontology-label check
  verifies all 2,126 eligible rows against the actual local ontology/stub files:
  zero absent targets and zero label mismatches.
- Every graph record/assertion was compared independently with its source.
  KGX 2.7.0 reads all nodes and edges and preserves the JSON annotations.
  A second build produces an identical archive. Strict Biolink conformance is
  not claimed for MIM's native predicates.
- The full regression run had 2,436 passing tests, six skips, and five failures.
  After correcting those failures, all **84 affected and newly relevant tests
  passed**, including the initially excluded unified-rejection tests. The whole
  suite was not rerun after those targeted corrections. Package coverage is 61%
  against the required 35%; Ruff, package mypy, and focused formatting pass.

The [adversarial self-review](ADVERSARIAL_REVIEW.md) documents each discovered
problem and its disposition. This is not an independent human sign-off.
The complete before/after records, reasons, and scientific source URLs are in
[identity-plan.json](identity-plan.json); the 14 explicit outcomes are in
[blocker_dispositions.tsv](blocker_dispositions.tsv).

**Full semantic approval remains FAIL.** The current graph has 670 role assertions
with prediction-only evidence, 11 without evidence, and eight cellular roles
without organism context. The prior component findings, including 51 assertions
requiring original preparation verification, remain open. Identity corrections
have not silently cleared those findings. [current_records.tsv](current_records.tsv)
covers every current record; unchanged records inherit only byte-identical prior
reviews, while changed records receive a limited identity-review disposition.

```bash
python reports/semantic_review_20260921/corrections/validate_followup_review.py
# Intentionally exits 1 while semantic approval is absent:
python reports/semantic_review_20260921/corrections/validate_followup_review.py --require-pass
```

The original audit is a historical snapshot; its original freshness validator
correctly rejects the changed corpus. Use the follow-up validator for this batch.

## Derived and downstream data

The unified export was fully regenerated against 15,878 local CultureMech recipe
files and contains 3,870 distinct ingredient-name rows. All 15 reviewed source-ID
rejections pass, including the Trypticase/Bacto-tryptone detergent caveat. The
producer code, all recipe/source hashes, and the temporary-input workaround are
recorded in [unified-build.json](unified-build.json). The wrapper excludes six
ignored backups and 78 rejected merge records; the shared upstream builder still
needs that input-index correction.

Recipe membership was refreshed only for the affected identity families. All
active record counts agree with the checked-in membership table. Unchanged
families retain their prior membership snapshot; this is not a full refresh of
all occurrence counts from the newer CultureMech table. See
[membership-refresh.json](membership-refresh.json).

**Downstream regeneration is not complete.** A hidden/ignored-inclusive search
followed by parsed-YAML inspection finds 106 recipes with Trypticase/Bacto-tryptone
still assigned CHEBI:78018, and three with Peptone assigned FOODON:03302071.
[Every remaining assignment](downstream-remaining-identifiers.json) includes its
recipe ID, JSON pointer, source path, and hash. These are current-snapshot counts,
not a reconstruction of the original 96/358 cohorts. CultureMech was inspected
read-only.

[Issue drafts](issue-drafts/) are local proposals only. Nothing was posted,
pushed, merged, or deleted remotely during this batch.
