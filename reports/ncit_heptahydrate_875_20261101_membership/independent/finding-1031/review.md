# Independent supplemental finding: retired occurrence owner after #875

Recorded 2026-11-01T06:01:23Z. Read-only review of commit `cb9f59a0d045f104ee2c3c00c8d6c4ad4f4eaf1f`; no production edits. The directory suffix is an arbitrary allocated label, not the actual review timestamp. This finding supersedes the earlier exact-head PASS for Step 2. Root subsequently filed #1031 before implementation.

**BLOCKING:** `mappings/culturemech_recipe_membership.tsv` still publishes exactly 32 distinct recipe edges, each occurrence=1, under `kgmicrobe.compound:na2hpo4_x_7_h2o`. No active record owns that identifier after promotion, and no membership edge uses `NCIT:C61946`. The exact pairs and all input SHA256 hashes are in `results.json`.

The existing native test `tests/test_culturemech_membership.py::test_every_published_identifier_is_held_by_active_record` fails with exactly that retired identifier. The first invocation exited before collection because this isolated runtime lacks pytest-cov; its log is preserved. The second command cleared repository addopts and exercised the actual test:

```text
PYTHONPATH=src RUN/envs/mim/bin/python -m pytest -q -o addopts='' -p no:cacheprovider tests/test_culturemech_membership.py::test_every_published_identifier_is_held_by_active_record
1 failed in 4.66s
```

Native `build_culturemech_membership.collect()` on the current CultureMech occurrence table emits zero NCIT edges and reports the retired identifier as unknown for 32 recipes. Native `refresh_occurrence_statistics.read_occurrences()` still groups these 32 rows under the retired identifier. No source-label override exists for the accepted phosphate heptahydrate labels in the fully read occurrence utility. A fresh native rebuild would therefore remove these recipe links instead of transferring them. Simply replacing the stored edge keys without the durable source-label routing would not survive a rebuild.

`effective_occurrence_statistics()` consequently falls back to the owner's historical YAML26/26. The current flat export and browser JSON both display26/26. The probe's first browser extraction incorrectly searched key `identifier`; browser uses `id`. `browser-correction.json` records the correct row and this diagnostic correction. There is no claim that the browser row is absent.

Scope distinctions, measured using native functions with an in-memory override dictionary only:

| Exact label scope | Current occurrence rows / recipes routed to NCIT |
|---|---:|
| `Na2HPO4 x 7 H2O`, `Na2HPO4.7H2O` | 32 / 32 |
| Above plus middle dot `Na2HPO4·7H2O` and accepted bullet `Na2HPO4•7H2O` | 35 / 35 |
| Above plus `Sodium phosphate dibasic heptahydrate` | 52 / 52 |

The three middle-dot rows are already NCIT in the current unified mapping, while native occurrence routing leaves two unresolved and one at anhydrous CHEBI:34683. The bullet spelling is an accepted YAML synonym with no current source occurrence. The English label has17 unresolved source occurrences and is a separate potential expansion; this review does not authorize adding it silently. The 32 stored edges can be migrated without changing their recipe IDs or counts, preserving the published snapshot's provenance. Any additional recipe edges must be explicitly scoped and evidenced rather than described as an unchanged32-edge migration.

Negative boundaries retained in `selected-occurrences.json`: generic Na2HPO4, mono/di/tri/hexa/dodecahydrates, buffers and solutions. A narrow fix must not redirect these parent/sibling/preparation labels or broadly rewrite all CHEBI:34683 rows. Preserve historical YAML26/26 and repair effective products from the corrected maintained membership; no new chemistry or BUFFER approval follows.

The analogous Step3 hazard is confirmed:14 current `Carnitine Hydrochloride` rows still route to its present local identifier. A later promotion requires a separately reviewed durable source-label override and edge migration; the free `DL-carnitine` two-row group remains CHEBI:17126 and must stay separate.

The implementation search included ignored/hidden files in MIM `src`, `scripts`, `tests`, `docs`, `.github`, and justfile. A separate ignored-inclusive search found no direct membership utility references in isolated Claw `src` or CultureMech `src`/`scripts`. This is a bounded consumer search, not a claim about all repositories or all external consumers. No native generated outputs were written. Source/input hashes were unchanged through the probe, and the worktree remained clean at the reviewed commit when rechecked.

Required re-review: the guarded membership writer, exact label overrides and regression tests; same32 pairs and counts after migration; fresh native collect/read-occurrences behavior for accepted labels plus parent/sibling/preparation controls; updated count-bearing exports; applicable receipt/owner-preservation checks; exact final committed head. This report does not approve unreviewed repair code or a future head.
