# Step 2 preliminary independent integration review

**No unresolved implementation blocker remains in the reviewed scope after #1029.** Final native capture and final committed-head review are still required; this note does not approve a release mapping or the record's unresolved chemistry/BUFFER claims.

The review covered the approved #875 exact-heptahydrate correction, the narrow #1028 unchanged-cohort refresh fix, the guarded writer, actual applied record/ledger/SSSOM, candidate generation provenance, the 16th mapping-change receipt, regenerated unified product, companion successor, and preservation of semantic holds. No implementation or scientific data edits were made by the reviewer. External fixture mutations were isolated under this directory.

## Finding and repair

The preliminary writer had a real evidence-reservation race, filed before repair as [#1029](https://github.com/CultureBotAI/MediaIngredientMech/issues/1029). Replacing a reserved receipt or any of its three backup paths after reservation let the real native transaction change both sources and report success while the evidence pathname held competing bytes. `probe_reservation_race.py`, `reservation-race.json`, `reservation-race.log`, and the four retained fixture directories preserve the failures. The exact originally applied writer is preserved as `writer-before-reservation-fix.py`, SHA-256 `a66389a3379a761ee263aceb08222b6508f57cb9b8e69e996e82af732b59bb85`.

The repair retains the open descriptor identities, checks corresponding path entries before mutation, inside validation and around completion, and fails without overwriting competing entries. If mutation already occurred, native journal/before-images remain and the surviving receipt records failure. No production reapplication occurred.

Independent re-review of fixed producer SHA-256 `f7cd1b46dc464cc8801a73f6b1cbd251bd5c0c7ffdf7241eff0e9cbee6f1c131` and writer tests `8adfdd21e8042059abd058b94ae846d1fc1e432bb876d64f5db79ad7ddf87e51` passed 16 additional real-native cases: receipt and all three backups, regular and symlink replacements, at reservation and after commit. All refused false completion. No source changed in precommit cases; postcommit cases preserved competing paths, native journals and exact before-images. See `probe_reservation_fixed.py`, `reservation-fixed/results.json`, and `reservation-fixed.log`.

The earlier #1028 defect is also repaired without adding approval behavior. The refresh compares all decision content except verified location fields, uses each snapshot's own evidence locator, preserves complete resolved evidence, and records both locations. The actual successor replay below confirms that repair works for this promotion. Separate initial and repaired review evidence is under `../refresh-1028/`.

## Applied scope and evidence

`verify_applied.py` independently checked the actual inputs and receipts; full results are in `applied-verification.json` and `.log`.

- Owner identifier and grounding are exact `NCIT:C61946`. All unrelated fields are identical to durable base `40b787d37d33d544551389ff019f2d64ad63d7cc`; prior history and mapping evidence are exact prefixes with one new event and one source assertion appended. Chemistry, roles, accepted hydrate aliases, rejected sibling labels and occurrence statistics are preserved.
- The archived official NCI EVS payload and its fetch receipt match SHA-256 `a112c3e91dd6aa46feb112621ba5d13673df69f1b20665e042e22b8aa05a1d83`. I read the complete response: active C61946, exact heptahydrate label, CAS 7782-85-6, formula `2Na.HO4P.7H2O`, FDA UNII `70WT22SF4B`, NCIt 26.10d. This supports the approved §3 step 1 identity. A direct live web-tool recheck failed because that tool could not access the API endpoint; no fabricated live result is claimed.
- Both aggregate collections preserve every non-target record. Their only non-record metadata change is generation date. The mapped record matches the individual owner.
- The 90-row rejection ledger changes exactly one row's `mim_id` and rationale; `CHEBI:34683` remains rejected. Other rows are unchanged.
- Canonical SSSOM changes 2,987→2,986 rows: exactly one target ontology row changes and its obsolete registry sibling is removed. Every other byte, including unrelated rows and header, is identical. The new row preserves historical source-token provenance, adds inspected NCI/Codex provenance, retains the complete accepted alias/CAS payload, and drops the stale ChEBI validation stamp.
- The 2,979-row native candidate remains diagnostic. Its target is exactly the promoted row except for the deliberate preservation of old source tokens. The candidate was not broadly promoted.
- I independently hashed every one of the 2,691 generation inputs (8,741,198,033 bytes), all five comparison inputs and four label maps. Before/after manifests agree; producer, harness, prior-stamp and candidate hashes agree with the generation receipt.
- The actual source/promotion receipt hashes, owner and ledger before/after hashes, canonical hashes, both complete native recovery journals and their exact before-images all match. All 15 prior mapping receipts are unchanged; sequence 16 binds the exact one-change/one-removal transition and remains approval-free.

## Products and approval boundary

`verify_products.py` and `products-verification.json`/`.log` retain the independent replay.

- The native companion successor reproduces byte-for-byte. Every native audit field matches. All 20 owners and 51 complete claims/decisions remain unchanged; 14 selected base-decision locations move. Scientific approval remains false. The prior review is preserved exactly, and the baseline is durable merged main `40b787d`.
- Unified SHA-256 is `6126d33febe2a577ff60295a36d6e5dd649a39e73c218f4d18468f3813adbce9`: 4,170 rows and 209,330 occurrences. Exactly three heptahydrate spellings change `mim_id` to NCIT and gain the exact NCI label in `synonyms`; 4,167 rows are identical. Occurrences and recipe examples remain identical. There are zero REJECTED rows with empty `mim_id` and zero `kgmicrobe.compound` rows leaking CHEBI into the three identity columns.
- Every non-target mapping decision and complete resolved evidence entry is preserved through the receipt position map. Every nonmapping approval remains unchanged. The target BUFFER assertion remains OPEN; the new exact mapping remains WITHHOLD.
- The two existing target finding rows change only the current owner hash. No finding is retired. Full semantic assertion counts change solely by removal of one withheld mapping: OPEN 2,272→2,271; APPROVED remains 2,220. This is not new scientific approval.
- Active CI, documentation and integration-test selection point to the new immutable companion successor. Protected evidence workflow/pin files are unchanged.

## Validation and limits

The first pre-freeze focused run had 84 passes and one expected integration failure because the unified rebuild was still pending; its original log is preserved. After regeneration and #1029 repair, the same writer/refresh scope passes **133 tests**, including the actual committed-surface regression and real native transaction checks (`focused-tests-fixed.log`). Existing LinkML/Pydantic deprecation warnings do not fail the tests.

Default `git diff --check` flags the required final TSV delimiter on the changed BUFFER assertion row because `review_evidence` is empty. Do not remove that delimiter and lose the schema column. This is a generated-format check note, not a scientific or implementation defect.

This review does not cover final packaging/QC that is not yet frozen. It also does not resolve inherited anhydrous InChI/SMILES, independently prove BUFFER behavior, enlarge the companion cohort, change sibling hydrates, or port the later approval model. Final native review must bind the actual frozen source/evidence bytes and record completed required gates; final exact-head review must follow the commit.
