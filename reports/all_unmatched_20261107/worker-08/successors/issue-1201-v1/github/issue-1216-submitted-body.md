The current `data/ingredients/mapped/Na2moo4_X_2_H2o.yaml` owner for CHEBI:75213 retains unsupported formula aliases. Live `main` bytes were retrieved on 2026-11-08 and match the frozen owner SHA256 `d8ecba6c664d94d9d0f0da89410808b99c3d6ad4cfeb55f122b5df2d7d8b5612`.

Four names are currently typed as resolving synonyms:

- `Na2MoSO4 x 2 H2O` and `NaMoO4 x 2 H2O` (`HYDRATE_FORM`).
- `Na2MoSO4` and `NaMoO4` (`EXACT_SYNONYM`).

Seven additional literals are retained as `RAW_TEXT`: `Na2Mo4 x 2 H2O`, `Na2MoO7 x 2 H2O`, `Na2MoO7O4 x 2 H2O`, `Na2MO4.2H2O`, `Na2MoO7・2H2O`, `NaMoO4 · 2H2O`, and `NaMoO4.2H2O`. This report makes no consumer-index resolution claim for these seven RAW_TEXT labels.

[ChEBI:75213](https://www.ebi.ac.uk/chebi/searchId.do?chebiId=CHEBI:75213) identifies sodium molybdate dihydrate. These literal formulas differ in element spelling, sodium/oxygen counts or hydration qualification. The inspected historical merge/backfill assertions and ignored-inclusive review-file search did not provide an exact primary correction establishing universal equivalence for these labels. Chemical plausibility is not a source correction.

Worker08's assigned source case `KG_CASE:b40aaa312b04204d1afd03c737d566904a7525b69913670357f0293eedf84b49` retains `Na2Mo4 x 2 H2O`; the [MediaDive ingredient736 record](https://mediadive.dsmz.de/rest/ingredient/736) does not resolve its original reagent specification. That source hold remains separate from this bounded alias repair.

An unapplied proposal, `if1201-edit-na2moo4_x_2_h2o`, changes only these eleven synonym types to `REJECTED_LABEL` and appends curation history. Original text, provenance, chemistry, roles, occurrence counts and prior history remain. Final payload SHA256: `a81465916836d3c96601136e45f446324ff92091aeb4b9352386afe0760cee97`. Authorship-separated review `IF1201-R3` inspected the full owner and exact delta and accepted the bounded correction. Evidence and review are preserved in worker08's frozen local issue1201 successor bundle, prepared for commit and push on branch `review/all-unmatched-w08-source-review-20261107`.

Follow-up is to apply the bounded rejection through the normal guarded/synchronized review path, and investigate any exact source-specific corrections separately. This issue does not authorize a guessed replacement compound, new owner, global corrected alias, source-hold release or downstream rebuild.

Deduplication: live all-state issue searches for `molybdate`, `Na2MoO7` and `Na2MoSO4` were read. #1179 concerns the distinct JCM1357 manganese/molybdenum source conflict; #375 and #882 concern hydrate-parent/tombstone problems. No returned issue covers this exact eleven-label owner family. Search captures and live owner bytes are retained in the successor bundle.
