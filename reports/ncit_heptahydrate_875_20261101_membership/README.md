# NCIT heptahydrate membership correction: #1031 / #1033

Production membership application, native exports, full QC and final receipt-chain checks are complete. This portable evidence bundle is frozen; final native review capture and exact final-head review remain pending.

The #875 identity correction changed the heptahydrate owner to NCIT:C61946 but omitted its maintained CultureMech membership keys. Exactly **32 existing recipe/count pairs** retained the retired local identity. A preliminary message said 42; the independently verified artifact and native 28+4 occurrence groups establish 32. The repair changes only those identity keys, preserves the source header and every unrelated row, and restores effective counts 32/32 without changing historical YAML statistics 26/26. It does not rebuild against today's CultureMech cohort.

## Actual application

Root applied the reviewed writer once on 2026-11-01 at 06:10:12Z. The immutable application receipt is `application/apply.json`, SHA-256 `1f227990d5b0ecc22d2064110d45c790d0778c92c692e2c5363e2b086996f54c`. Only `mappings/culturemech_recipe_membership.tsv` changed in that transaction. Before SHA 6537498d833f45295193865d6cd5f98ad31200c5dbe4a706c6f541dcf30a5064; after SHA 55ce5fabd42eb4cc1df628d4fd6a45b813caccbc7d7773105ece5633dd313897. The receipt binds the exact source writer inputs and 32 recipe/count pairs. The preflight binds the executing membership writer a3a8af0a... and shared publisher 768166cf... .

The exact beforeimage and complete native journal are retained as deterministic gzip files. Decompression recovers the original bytes and hashes recorded in `portable-sources.json`; absolute run-local paths inside the original receipt/journal are preserved as historical execution evidence. The journal's embedded beforeimage must equal the standalone preimage. No extra copies of large test fixtures are included.

`application/verified-application.json` proves preserved source metadata, all 32 pairs, unchanged total rows, and unchanged owner YAML, canonical SSSOM, rejection ledger and unified mapping. Prior production receipts and frozen review reports remain historical evidence; this follow-up does not reapply their changes or add source curation history.

## Why the additional guard repairs were required

- #1031: the existing active-owner membership test failed because the retired ID had no active owner. Native collection over the archived snapshot discarded those 32 recipe occurrences. The finite routing correction adds only `Na2HPO4 x 7 H2O`, `Na2HPO4.7H2O`, and the already accepted bullet spelling `Na2HPO4•7H2O`. Parent, sibling-hydrate, buffer and unrelated labels retain their routing. Middle-dot and long-form expansion remain outside this bounded repair.
- #1033: independent native probes inserted valid duplicate NCIT owner records under ignored/nested directories after receipt reservation. The initial membership wrapper and then the original source/promotion call sites accepted these conflicts. All three publishing paths now recheck uniqueness inside native precommit validation, alongside existing input-byte and receipt/backup-identity checks. Promotion also refuses pre-existing conflicts on its no-op branch. Competing records and failure evidence survive rejection.

The guarantee assumes the repository lock and validates immediately before the native mutation; it does not claim protection from arbitrary edits after a completed transaction.

## Evidence and review status

`finding-1031/` preserves the original failing test and bounded author preflight. `implementation/` retains exact sources, hashes, dry-runs, passing tests and intentional fresh-process mutation failures for each revision. Earlier false-confidence and exception-type diagnostics remain labeled in their own READMEs. `independent/` contains the original valid-owner probes and separate re-reviews, including the final source re-review of all three paths. The latest source suite passed 158 tests; the committed-artifact assertion was intentionally pending application at that time. Final post-application checks are recorded below and in `checks/final-checks.json`.

The previous native review of cb9f59a0d045f104ee2c3c00c8d6c4ad4f4eaf1f is superseded for the amended change. Independent source review is distinct from the pending final native bundle and exact final-head review. Mapping remains WITHHOLD; chemistry and BUFFER questions remain open. This membership repair adds no scientific approval and performs no later approved-plan step.

## Portable verification

Run `python3 reports/ncit_heptahydrate_875_20261101_membership/verify.py` from the repository, or run `verify.py` directly after copying this folder elsewhere. It verifies copied hashes, decompresses and compares the exact beforeimages, reconstructs the bounded identity-key migration, and checks the applied output hash. Once the final inventory is frozen, it also checks that inventory. It does not write files or confer scientific approval.

The copied independent probe scripts retain their original execution paths and input hashes as evidence. Re-running those native transactions requires the matching isolated Claw/MIM environment and fixture layout; the large temporary fixture trees and full upstream occurrence table are intentionally omitted. Their results are not claims that the old absolute paths remain available in a fresh checkout.

`checks/preservation-and-effective-counts.json` verifies the 185-file prior report inventory and all three original application/publication receipts. It also captures the corrected 32/32 catalog/browser counts and index occurrence count 32, alongside unchanged historical YAML 26/26.

## Final post-application checks

- Full `just qc` passed at 2026-11-01T06:13:54Z, with log SHA-256 `509779056a924761900d9efeeb30d5d203d77cf6c45eca8b3dabb3983571fff4`.
- Final focused suite: **220 passed**, including committed memberships, active-owner ownership, native writer/guard regressions, occurrence consumers and receipt alignment.
- All seven native commands passed: reviewed SSSOM export and validation, semantic integrity, supported KGX export and validation, and companion export and validation. Semantic integrity is PASS while the full semantic release remains FAIL for the retained scientific backlog; successful integrity checks are not scientific approval.
- `application/export-delta.json` compares 13 changed native export files to pre-amendment commit cb9f59a0d045f104ee2c3c00c8d6c4ad4f4eaf1f. JSON/CSV data differences are only target effective counts 26→32; browser JSON also updates its generation timestamp. Markdown updates target counts, generated timestamps and the derived occurrence totals: ALL 223056→223062 and MAPPED 222462→222468. All other export content is identical.
- The same delta binds **5,417 unchanged protected tracked files**, including ingredient/aggregate YAML, review and receipt evidence, all other mappings, unified/provenance artifacts, workflows and pin files. The initial diagnostic rejection of Markdown totals omitted a legitimate derived +6 change and was not a production defect.

The earlier native review of cb9f59a is preserved as historical evidence and cannot approve the amended source tree. Final native bundle review and exact final-head review remain pending outside this frozen report. No Step 3–7 work is included.

Independent applied-state verification is retained in `independent/applied/`: the reviewer verified the actual receipt/journal, exact 32-pair migration and 202066 unchanged rows, all 256 prior native inputs (241 unchanged; 15 expected source/export changes), nine JSON/CSV product deltas, all final log hashes, and three actual-state native tests. This PASS remains distinct from the final native bundle and exact final-head review, which are intentionally outside the frozen package.
