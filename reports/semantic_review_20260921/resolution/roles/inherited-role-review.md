# Role-level inheritance review (#720)

The final adversarial audit found that a record-level identity PASS could retain
a narrower biological role introduced by the legacy role migration. In
`Bacl2.yaml` and `Sncl2_X_2_H2o.yaml`, the only source role is `Mineral`, while
`TRACE_ELEMENT` means a micronutrient required in trace amounts. The archived
reviews checked chemical identity and field completeness; they do not establish
that biological requirement. A database citation and an unchanged file do not
close this evidence gap.

The complete audit covers all 138 historically inherited positive role
assertions. `inherited-role-review.json` records each exact source record hash,
assertion hash, edge and source position, original source evidence, historical
review path/hash, disposition, and reasoning.

Twenty-four semantic promotions require additional claim-level evidence and
are excluded from the supported graph: 17 trace-element, four iron-source,
one phosphate-source and one sulfur-source assertions inferred from a generic
mineral class, plus the DL-alpha-lipoic-acid vitamin assertion inferred from
`Growth factor`. These are unresolved roles, not declarations that the proposed
biology is false. Their unchanged source claims remain in the backlog.

The other 114 roles retain conditional eligibility: 70 preserve the same role
stated by the ingredient-specific source, 43 have the archived review's
identified recipe/stock constituent support, and one retains the scoped Soytone
primary study. Recipe-derived roles retain their compositional interpretation;
they do not establish that every organism utilizes every constituent. Occurrence
counts and confidence values are not the approval basis. This review adds no new
growth experiments or literature claims.

Eligibility is an explicit frozen decision, not a classifier for future data.
The builder requires exact record bytes, assertion, edge, source position and
archived reasoning before inheriting any role approval. Missing, changed, or
unreviewed roles cannot inherit a record's positive verdict. The eight new
cellular-role repairs have separate full-record-bound primary-evidence plans.

Thirty-one builder regression tests passed, including missing role review,
unverified promotion, changed ingredient, duplicate position and changed
historical reasoning. `historical-evidence-portability.json` records an exact
archive reproduction in an isolated root containing only the archived review
JSON, with no original ignored report files. It reproduced 1,455 reports and
2,108 historical assertion candidates byte for byte; the role-scope filter still
excludes the 24 unresolved promotions from those candidates.

After upstream merge `f6a95295`, sodium thiosulfate's receipt was refreshed only
after proving that removing our exact role correction and curation event yields
the complete upstream record. The upstream synonym retirement is preserved;
the chemical identity and scoped role are unchanged. See
`upstream-integration-receipt.json`.
