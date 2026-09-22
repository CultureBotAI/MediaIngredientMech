# Completed semantic audit — release verdict FAIL

> Historical snapshot. The later [identity-correction batch](corrections/README.md)
> records 11 corrected blockers and three withdrawn mappings. Use its validator
> for the current corpus; full semantic approval still fails.

The review covers **all 2,951 source records (2,877 active), 3,024 SSSOM rows,
5,798 KGX nodes, and 4,533 KGX assertion edges**. Coverage is complete; semantic
approval is not granted. The current full graph has unresolved identity and
evidence problems.

Existing reviews were reused only after establishing that their source records
are byte-identical to their reviewed Git snapshots. All subsequent SSSOM field
changes were checked, and additional evidence/scope judgments are recorded in
[DECISIONS.md](DECISIONS.md). This is a completed consolidation and follow-up audit,
not a claim that every external source was freshly researched.

| Active record disposition | Count |
| --- | ---: |
| Pass | 1,263 |
| Pass with minor issues | 193 |
| Needs curation | 1,164 |
| Reviewed and intentionally retained as unmapped | 257 |

The 74 rejected records remain excluded. Four other unmapped records are included
in `needs_curation` because their retained parent proposals have scope problems.

## Findings

* All **14 existing identity blockers remain unresolved**. They include dibasic
  phosphate mapped to trisodium phosphate, a sodium-nitrate source mapped to the
  NCIT nano prefix, and an EDTA label mapped to the generic chelator class.
* **671 role assertions have only provisional computational evidence; 11 have
  no evidence.** All eight cellular metabolic roles also lack organism context.
* **51 component assertions** based on abbreviation expansion or curated
  interpretation require verification against the original source preparation.
  GYPS/PYGS explicitly expose the unresolved salts-versus-starch ambiguity.
* BHI's **exact formulation** reference is not established by the stored list of
  common constituent names.
* Four unpublished parent proposals confuse whole preparations, related
  compounds, or polymer fragments with a broader class.

These counts overlap at the record level. A blocked record does not make every
one of its mappings false. Unsupported predictions remain distinguishable from
demonstrably wrong identities; no prediction was relabeled as experimental truth.

## Correction made

Fixed the new KGX exporter's hierarchy projection: **166 broader-parent mappings
now become child-to-parent `biolink:subclass_of` edges**, following MIM's explicit
mapping contract. Original SSSOM rows and relations remain in the edge annotations.
The inverse direction is covered by a regression test. No scientific curation
finding was silently closed or removed from the corpus.

The rebuilt graph retains **5,798 nodes, 4,533 assertion edges, and 4,528 unique
triples**. Its archive SHA256 is
`14e7ca13c3ff3735ba18a0d15db092280746a5a83eae2a3730a91201f8fd074b`.
The SSSOM remains unchanged at SHA256
`3609d71f8a1c3d19f0fba0654c704f7f823d928116dd292507afcec91d7e23d2`.

## Review files

| File | Purpose |
| --- | --- |
| [records.tsv](records.tsv) | Every source record, source/report hashes, reviewed Git snapshot, verdict, and finding IDs |
| [sssom.tsv](sssom.tsv) | Every mapping row, row hash, direction review, and record-review disposition |
| [kgx_nodes.tsv](kgx_nodes.tsv) | Every node; reference stubs and unresolved concepts are not chemical identity approvals |
| [kgx_assertions.tsv](kgx_assertions.tsv) | Every assertion, its payload hash, verdict, and rationale |
| [findings.tsv](findings.tsv) | Complete open correction backlog; `record_scope` distinguishes active records from rejected-record cleanup |
| [unpublished_candidates.tsv](unpublished_candidates.tsv) | All eight retained unmapped parent proposals |
| [resolved_findings.tsv](resolved_findings.tsv) | The corrected hierarchy-export defect |
| [manifest.json](manifest.json) | Coverage counts, exact input/member hashes, methods, and explicit failing release verdict |
| [validation.json](validation.json) | Integrity and rejection checks, bound to the manifest and validator hashes |

## Verification

From the repository root:

```bash
# Check that the review still covers and matches the current records and bundle.
python reports/semantic_review_20260921/validate_review.py

# Require semantic release approval. This intentionally exits 1 for this snapshot.
python reports/semantic_review_20260921/validate_review.py --require-pass
```

The validator checks every source/member hash and exact coverage, including the
SSSOM-to-KGX hierarchy projection. Negative checks reject a stale source hash,
missing mapping/node/assertion reviews even after their member hashes are updated,
and an incorrectly asserted passing release verdict.

The corrected exporter passed 19 focused regression tests, Ruff, formatting,
and package type checking. The preceding full suite passed 2,445 tests with six
skips; it was not rerun wholesale for the focused hierarchy correction. The
rebuilt archive passed the native KGX reader and exhaustive source comparison.

`build_review.py` reproduces this dated adjudication snapshot and requires the
two reviewed commits in local Git history. It deliberately refuses changed source
records or unreviewed SSSOM changes; it cannot automatically approve new biology.

No remote issues, messages, commits, or publication were created by this audit.
