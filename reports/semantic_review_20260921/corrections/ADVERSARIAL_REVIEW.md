# Adversarial review of the correction batch

This was a self-review and independent artifact comparison, not a second agent or human sign-off. No GitHub issues or comments have been posted. The files in `issue-drafts/` are proposed outbound messages only.

| Finding | Disposition | Evidence |
| --- | --- | --- |
| Rejecting merged synonyms because tombstones still own their old labels | Fixed: Rule K excludes REJECTED owners; active and ambiguous owners still block collisions | `tests/test_sssom_other_cross_record.py` |
| Assigning source fragments to guessed constitutional isomers | Fixed by withdrawing identities; original source resolution remains open | Two AMBIGUOUS records and `blocker_dispositions.tsv` |
| Treating the manufacturer's hydrate CAS as necessarily invalid | Revised: manufacturer explicitly uses this CAS; distinct local hydrate identity and supplied-form CAS retained | MP Biomedicals certificate cited in `identity-plan.json` |
| Losing procurement CAS tokens during scoped SSSOM regeneration | Fixed: six symmetric rows repaired with the existing CAS publisher; plan applier now preserves this channel | `tests/test_cas_synonym_currency.py` |
| New stock component uses a comma variant absent from its catalog target | Fixed: normalized component-label punctuation, preserving the exact source label in evidence | Partonomy validation and source projection |
| Updated record counts disagree with published recipe membership | Fixed for affected identity families; unchanged families retain their documented prior snapshot | `membership-refresh.json` and membership regression tests |
| Unified builder reads ignored backups and lets an early tombstone own a merged label | Locally mitigated with isolated active input; shared producer fix remains open | `rebuild_unified.py` and `issue-drafts/claw-live-ingredient-index.md` |
| Regenerated MIM artifacts could be mistaken for corrected downstream recipes | Verified NOT complete: 109 erroneous active assignments remain in the inspected CultureMech snapshot | `downstream-remaining-identifiers.json` |
| Correction batch could silently inherit semantic approval for changed records | Fixed: changed records receive identity-only dispositions; all untouched records must match baseline hashes | `current_records.tsv`, `current-review.json`, `validate_followup_review.py` |

The existing procurement-CAS channel on symmetric SSSOM rows is preserved. Its consumption as ontology-node synonyms by downstream software is not certified here; a supplied form is not automatically the identity of a free-acid or other close-match target. The full release remains semantically unapproved.
