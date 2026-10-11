# Correct certainty of 17 recipe-token reconciliation observations

- Review: 20261011T030852Z-mim-token-scope-reassessment
- Repository: culturebotai/MediaIngredientMech
- Started UTC: 2026-10-11T03:06:05Z
- Finished UTC: 2026-10-11T03:08:52Z
- Reviewer: Codex (self_review)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Append 17 deferred/provisional successors after auditing the prior token heuristic. Historical reports, source labels, and all other findings are unchanged. Source-context science is not completed.

## Scope And Provenance

Certainty of 17 exported-context-token findings, not whole-record identity or scientific review.

Selection: All 17 exported-context-tokens findings in the 13 initial all-MIM reconciliation batches.
Coverage: full; 17 reviewed / 17 in the declared population.
Source: working_tree at Git base 0cc2b4e354ecc4f005eb7ef833ca23fdc64041a3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-88ed3645c26c14b6 | data/ingredients/mapped/4-vinylphenol.yaml | maintained | 4-vinylphenol |
| record-205c79d137874075 | data/ingredients/mapped/Artificial_seawater.yaml | maintained | Artificial_seawater |
| record-9122c364d42e8559 | data/ingredients/mapped/DL_Vitamins.yaml | maintained | DL_Vitamins |
| record-797da68010f27377 | data/ingredients/mapped/Desulfovibrio_Trace_Elements.yaml | maintained | Desulfovibrio_Trace_Elements |
| record-099e2c8a2a9f8f68 | data/ingredients/mapped/Fatty_Acid_Mixture_See_Medium_No_266.yaml | maintained | Fatty_Acid_Mixture_See_Medium_No_266 |
| record-7059116102e92505 | data/ingredients/mapped/Mineral_Solution_See_Medium_No_976.yaml | maintained | Mineral_Solution_See_Medium_No_976 |
| record-4253636d94bcf2f1 | data/ingredients/mapped/Modified_Trace_Vitamins.yaml | maintained | Modified_Trace_Vitamins |
| record-62f485f9f7517526 | data/ingredients/mapped/Peptone.yaml | maintained | Peptone |
| record-4190c0ee5976447a | data/ingredients/mapped/Potassium_Phosphate_Buffer.yaml | maintained | Potassium_Phosphate_Buffer |
| record-59776f859c41300d | data/ingredients/mapped/Riboflavin.yaml | maintained | Riboflavin |
| record-c6cdd023283a1f0a | data/ingredients/mapped/Sludge_fluid.yaml | maintained | Sludge_fluid |
| record-3245d67aff586e82 | data/ingredients/mapped/Soil_Extract.yaml | maintained | Soil_Extract |
| record-341efa75278b5e50 | data/ingredients/mapped/Trace_Element_Solution_See_Medium_No_187.yaml | maintained | Trace_Element_Solution_See_Medium_No_187 |
| record-78ea6a14a080dbf0 | data/ingredients/mapped/Trace_Metal_Mix_A5.yaml | maintained | Trace_Metal_Mix_A5 |
| record-4b03942a3427132e | data/ingredients/mapped/Trace_Mineral_Solution.yaml | maintained | Trace_Mineral_Solution |
| record-7c55027f9d88edd0 | data/ingredients/mapped/Trace_Minerals.yaml | maintained | Trace_Minerals |
| record-4efe2f6907f0d4fc | data/ingredients/mapped/Yeast_Extract.yaml | maintained | Yeast_Extract |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Exact predecessor pair validation | passed | True | record-88ed3645c26c14b6, record-205c79d137874075, record-9122c364d42e8559, record-797da68010f27377, record-099e2c8a2a9f8f68, record-7059116102e92505, record-4253636d94bcf2f1, record-62f485f9f7517526, record-4190c0ee5976447a, record-59776f859c41300d, record-c6cdd023283a1f0a, record-3245d67aff586e82, record-341efa75278b5e50, record-78ea6a14a080dbf0, record-4b03942a3427132e, record-7c55027f9d88edd0, record-4efe2f6907f0d4fc | read_review verified every selected predecessor YAML/Markdown pair and retained provenance before authoring. |
| Explicit predecessor and competing-head audit | passed | True | record-88ed3645c26c14b6, record-205c79d137874075, record-9122c364d42e8559, record-797da68010f27377, record-099e2c8a2a9f8f68, record-7059116102e92505, record-4253636d94bcf2f1, record-62f485f9f7517526, record-4190c0ee5976447a, record-59776f859c41300d, record-c6cdd023283a1f0a, record-3245d67aff586e82, record-341efa75278b5e50, record-78ea6a14a080dbf0, record-4b03942a3427132e, record-7c55027f9d88edd0, record-4efe2f6907f0d4fc | All 651 pre-existing occurrences across the ignored-inclusive structured inventory had unique issue keys and no predecessors. Each of these 17 successors cites its exact prior occurrence and retains its target. The default sibling CLAW reviews module was unavailable; this was an explicit local audit, not a claim of schema-level lineage validation. |
| Exact-subject export presence | passed | True | record-88ed3645c26c14b6, record-205c79d137874075, record-9122c364d42e8559, record-797da68010f27377, record-099e2c8a2a9f8f68, record-7059116102e92505, record-4253636d94bcf2f1, record-62f485f9f7517526, record-4190c0ee5976447a, record-59776f859c41300d, record-c6cdd023283a1f0a, record-3245d67aff586e82, record-341efa75278b5e50, record-78ea6a14a080dbf0, record-4b03942a3427132e, record-7c55027f9d88edd0, record-4efe2f6907f0d4fc | Parsed current records and exact-subject SSSOM rows. Each target still has at least one of the recipe-pointer/truncated-concentration source tokens. Presence does not prove invalid synonym scope. |
| Primary source-context adjudication | skipped | True | record-88ed3645c26c14b6, record-205c79d137874075, record-9122c364d42e8559, record-797da68010f27377, record-099e2c8a2a9f8f68, record-7059116102e92505, record-4253636d94bcf2f1, record-62f485f9f7517526, record-4190c0ee5976447a, record-59776f859c41300d, record-c6cdd023283a1f0a, record-3245d67aff586e82, record-341efa75278b5e50, record-78ea6a14a080dbf0, record-4b03942a3427132e, record-7c55027f9d88edd0, record-4efe2f6907f0d4fc | Exact recipe/preparation and ontology evidence were not freshly adjudicated. No token was rejected, removed, or scientifically approved. |

## Scientific And Domain Assessments

### Certainty correction for the exact token observation

nomenclature: unknown. Targets: record-88ed3645c26c14b6.

Token presence remains reproducible, but the earlier pattern-based observation did not establish whether the exact source label denotes this subject or a different preparation. Fresh source-context adjudication is required before a confirmed defect or label removal. This successor corrects certainty only; it does not establish that the token is valid or that another identity allegation is fixed. The historical report separately alleges trace-mineral/4-vinylphenol identity conflation. That stronger claim remains in the original report and narrative reassessment; the recipe-pointer heuristic neither adjudicates nor retires it.

### Certainty correction for the exact token observation

nomenclature: unknown. Targets: record-205c79d137874075.

Token presence remains reproducible, but the earlier pattern-based observation did not establish whether the exact source label denotes this subject or a different preparation. Fresh source-context adjudication is required before a confirmed defect or label removal. This successor corrects certainty only; it does not establish that the token is valid or that another identity allegation is fixed. The historical report actually passes the record and explicitly accepts the raw source surface; attributing an unresolved token concern to that report was incorrect. No new source evidence was supplied to overturn its scoped conclusion.

### Certainty correction for the exact token observation

nomenclature: unknown. Targets: record-9122c364d42e8559.

Token presence remains reproducible, but the earlier pattern-based observation did not establish whether the exact source label denotes this subject or a different preparation. Fresh source-context adjudication is required before a confirmed defect or label removal. This successor corrects certainty only; it does not establish that the token is valid or that another identity allegation is fixed. The historical report actually passes the record and explicitly accepts the raw source surface; attributing an unresolved token concern to that report was incorrect. No new source evidence was supplied to overturn its scoped conclusion.

### Certainty correction for the exact token observation

nomenclature: unknown. Targets: record-797da68010f27377.

Token presence remains reproducible, but the earlier pattern-based observation did not establish whether the exact source label denotes this subject or a different preparation. Fresh source-context adjudication is required before a confirmed defect or label removal. This successor corrects certainty only; it does not establish that the token is valid or that another identity allegation is fixed.

### Certainty correction for the exact token observation

nomenclature: unknown. Targets: record-099e2c8a2a9f8f68.

Token presence remains reproducible, but the earlier pattern-based observation did not establish whether the exact source label denotes this subject or a different preparation. Fresh source-context adjudication is required before a confirmed defect or label removal. This successor corrects certainty only; it does not establish that the token is valid or that another identity allegation is fixed.

### Certainty correction for the exact token observation

nomenclature: unknown. Targets: record-7059116102e92505.

Token presence remains reproducible, but the earlier pattern-based observation did not establish whether the exact source label denotes this subject or a different preparation. Fresh source-context adjudication is required before a confirmed defect or label removal. This successor corrects certainty only; it does not establish that the token is valid or that another identity allegation is fixed. A damaged spelling is observable, but the mapping contract permits damaged raw source forms when they still resolve to the same substance; malformed punctuation alone does not settle identity scope.

### Certainty correction for the exact token observation

nomenclature: unknown. Targets: record-4253636d94bcf2f1.

Token presence remains reproducible, but the earlier pattern-based observation did not establish whether the exact source label denotes this subject or a different preparation. Fresh source-context adjudication is required before a confirmed defect or label removal. This successor corrects certainty only; it does not establish that the token is valid or that another identity allegation is fixed.

### Certainty correction for the exact token observation

nomenclature: unknown. Targets: record-62f485f9f7517526.

Token presence remains reproducible, but the earlier pattern-based observation did not establish whether the exact source label denotes this subject or a different preparation. Fresh source-context adjudication is required before a confirmed defect or label removal. This successor corrects certainty only; it does not establish that the token is valid or that another identity allegation is fixed. A damaged spelling is observable, but the mapping contract permits damaged raw source forms when they still resolve to the same substance; malformed punctuation alone does not settle identity scope.

### Certainty correction for the exact token observation

nomenclature: unknown. Targets: record-4190c0ee5976447a.

Token presence remains reproducible, but the earlier pattern-based observation did not establish whether the exact source label denotes this subject or a different preparation. Fresh source-context adjudication is required before a confirmed defect or label removal. This successor corrects certainty only; it does not establish that the token is valid or that another identity allegation is fixed.

### Certainty correction for the exact token observation

nomenclature: unknown. Targets: record-59776f859c41300d.

Token presence remains reproducible, but the earlier pattern-based observation did not establish whether the exact source label denotes this subject or a different preparation. Fresh source-context adjudication is required before a confirmed defect or label removal. This successor corrects certainty only; it does not establish that the token is valid or that another identity allegation is fixed.

### Certainty correction for the exact token observation

nomenclature: unknown. Targets: record-c6cdd023283a1f0a.

Token presence remains reproducible, but the earlier pattern-based observation did not establish whether the exact source label denotes this subject or a different preparation. Fresh source-context adjudication is required before a confirmed defect or label removal. This successor corrects certainty only; it does not establish that the token is valid or that another identity allegation is fixed.

### Certainty correction for the exact token observation

nomenclature: unknown. Targets: record-3245d67aff586e82.

Token presence remains reproducible, but the earlier pattern-based observation did not establish whether the exact source label denotes this subject or a different preparation. Fresh source-context adjudication is required before a confirmed defect or label removal. This successor corrects certainty only; it does not establish that the token is valid or that another identity allegation is fixed.

### Certainty correction for the exact token observation

nomenclature: unknown. Targets: record-341efa75278b5e50.

Token presence remains reproducible, but the earlier pattern-based observation did not establish whether the exact source label denotes this subject or a different preparation. Fresh source-context adjudication is required before a confirmed defect or label removal. This successor corrects certainty only; it does not establish that the token is valid or that another identity allegation is fixed. A damaged spelling is observable, but the mapping contract permits damaged raw source forms when they still resolve to the same substance; malformed punctuation alone does not settle identity scope.

### Certainty correction for the exact token observation

nomenclature: unknown. Targets: record-78ea6a14a080dbf0.

Token presence remains reproducible, but the earlier pattern-based observation did not establish whether the exact source label denotes this subject or a different preparation. Fresh source-context adjudication is required before a confirmed defect or label removal. This successor corrects certainty only; it does not establish that the token is valid or that another identity allegation is fixed.

### Certainty correction for the exact token observation

nomenclature: unknown. Targets: record-4b03942a3427132e.

Token presence remains reproducible, but the earlier pattern-based observation did not establish whether the exact source label denotes this subject or a different preparation. Fresh source-context adjudication is required before a confirmed defect or label removal. This successor corrects certainty only; it does not establish that the token is valid or that another identity allegation is fixed.

### Certainty correction for the exact token observation

nomenclature: unknown. Targets: record-7c55027f9d88edd0.

Token presence remains reproducible, but the earlier pattern-based observation did not establish whether the exact source label denotes this subject or a different preparation. Fresh source-context adjudication is required before a confirmed defect or label removal. This successor corrects certainty only; it does not establish that the token is valid or that another identity allegation is fixed.

### Certainty correction for the exact token observation

nomenclature: unknown. Targets: record-4efe2f6907f0d4fc.

Token presence remains reproducible, but the earlier pattern-based observation did not establish whether the exact source label denotes this subject or a different preparation. Fresh source-context adjudication is required before a confirmed defect or label removal. This successor corrects certainty only; it does not establish that the token is valid or that another identity allegation is fixed. A damaged spelling is observable, but the mapping contract permits damaged raw source forms when they still resolve to the same substance; malformed punctuation alone does not settle identity scope.

## Findings

### scope-f-be91e29ea6694d28: Adjudicate source scope of exported tokens: 4-vinylphenol

major / deferred / provisional; issue key: mim-reconciliation-exported-context-tokens-88ed3645c26c14b6.

Token presence remains reproducible, but the earlier pattern-based observation did not establish whether the exact source label denotes this subject or a different preparation. Fresh source-context adjudication is required before a confirmed defect or label removal. This successor corrects certainty only; it does not establish that the token is valid or that another identity allegation is fixed. The historical report separately alleges trace-mineral/4-vinylphenol identity conflation. That stronger claim remains in the original report and narrative reassessment; the recipe-pointer heuristic neither adjudicates nor retires it.

Disposition: Token presence remains reproducible, but the earlier pattern-based observation did not establish whether the exact source label denotes this subject or a different preparation. Fresh source-context adjudication is required before a confirmed defect or label removal. This successor corrects certainty only; it does not establish that the token is valid or that another identity allegation is fixed. The historical report separately alleges trace-mineral/4-vinylphenol identity conflation. That stronger claim remains in the original report and narrative reassessment; the recipe-pointer heuristic neither adjudicates nor retires it.

### scope-f-e1004757f90e8c13: Adjudicate source scope of exported tokens: Artificial seawater

major / deferred / provisional; issue key: mim-reconciliation-exported-context-tokens-205c79d137874075.

Token presence remains reproducible, but the earlier pattern-based observation did not establish whether the exact source label denotes this subject or a different preparation. Fresh source-context adjudication is required before a confirmed defect or label removal. This successor corrects certainty only; it does not establish that the token is valid or that another identity allegation is fixed. The historical report actually passes the record and explicitly accepts the raw source surface; attributing an unresolved token concern to that report was incorrect. No new source evidence was supplied to overturn its scoped conclusion.

Disposition: Token presence remains reproducible, but the earlier pattern-based observation did not establish whether the exact source label denotes this subject or a different preparation. Fresh source-context adjudication is required before a confirmed defect or label removal. This successor corrects certainty only; it does not establish that the token is valid or that another identity allegation is fixed. The historical report actually passes the record and explicitly accepts the raw source surface; attributing an unresolved token concern to that report was incorrect. No new source evidence was supplied to overturn its scoped conclusion.

### scope-f-838d67873b6673db: Adjudicate source scope of exported tokens: DL vitamins

major / deferred / provisional; issue key: mim-reconciliation-exported-context-tokens-9122c364d42e8559.

Token presence remains reproducible, but the earlier pattern-based observation did not establish whether the exact source label denotes this subject or a different preparation. Fresh source-context adjudication is required before a confirmed defect or label removal. This successor corrects certainty only; it does not establish that the token is valid or that another identity allegation is fixed. The historical report actually passes the record and explicitly accepts the raw source surface; attributing an unresolved token concern to that report was incorrect. No new source evidence was supplied to overturn its scoped conclusion.

Disposition: Token presence remains reproducible, but the earlier pattern-based observation did not establish whether the exact source label denotes this subject or a different preparation. Fresh source-context adjudication is required before a confirmed defect or label removal. This successor corrects certainty only; it does not establish that the token is valid or that another identity allegation is fixed. The historical report actually passes the record and explicitly accepts the raw source surface; attributing an unresolved token concern to that report was incorrect. No new source evidence was supplied to overturn its scoped conclusion.

### scope-f-320ccfb6bddc74ee: Adjudicate source scope of exported tokens: Desulfovibrio trace elements

major / deferred / provisional; issue key: mim-reconciliation-exported-context-tokens-797da68010f27377.

Token presence remains reproducible, but the earlier pattern-based observation did not establish whether the exact source label denotes this subject or a different preparation. Fresh source-context adjudication is required before a confirmed defect or label removal. This successor corrects certainty only; it does not establish that the token is valid or that another identity allegation is fixed.

Disposition: Token presence remains reproducible, but the earlier pattern-based observation did not establish whether the exact source label denotes this subject or a different preparation. Fresh source-context adjudication is required before a confirmed defect or label removal. This successor corrects certainty only; it does not establish that the token is valid or that another identity allegation is fixed.

### scope-f-853c7e2e707eedfc: Adjudicate source scope of exported tokens: Fatty acid mixture (see Medium No. 266)

major / deferred / provisional; issue key: mim-reconciliation-exported-context-tokens-099e2c8a2a9f8f68.

Token presence remains reproducible, but the earlier pattern-based observation did not establish whether the exact source label denotes this subject or a different preparation. Fresh source-context adjudication is required before a confirmed defect or label removal. This successor corrects certainty only; it does not establish that the token is valid or that another identity allegation is fixed.

Disposition: Token presence remains reproducible, but the earlier pattern-based observation did not establish whether the exact source label denotes this subject or a different preparation. Fresh source-context adjudication is required before a confirmed defect or label removal. This successor corrects certainty only; it does not establish that the token is valid or that another identity allegation is fixed.

### scope-f-43e56706181e97b8: Adjudicate source scope of exported tokens: Mineral solution see Medium No. 976

major / deferred / provisional; issue key: mim-reconciliation-exported-context-tokens-7059116102e92505.

Token presence remains reproducible, but the earlier pattern-based observation did not establish whether the exact source label denotes this subject or a different preparation. Fresh source-context adjudication is required before a confirmed defect or label removal. This successor corrects certainty only; it does not establish that the token is valid or that another identity allegation is fixed. A damaged spelling is observable, but the mapping contract permits damaged raw source forms when they still resolve to the same substance; malformed punctuation alone does not settle identity scope.

Disposition: Token presence remains reproducible, but the earlier pattern-based observation did not establish whether the exact source label denotes this subject or a different preparation. Fresh source-context adjudication is required before a confirmed defect or label removal. This successor corrects certainty only; it does not establish that the token is valid or that another identity allegation is fixed. A damaged spelling is observable, but the mapping contract permits damaged raw source forms when they still resolve to the same substance; malformed punctuation alone does not settle identity scope.

### scope-f-d3696f2daf45c433: Adjudicate source scope of exported tokens: Modified trace vitamins

major / deferred / provisional; issue key: mim-reconciliation-exported-context-tokens-4253636d94bcf2f1.

Token presence remains reproducible, but the earlier pattern-based observation did not establish whether the exact source label denotes this subject or a different preparation. Fresh source-context adjudication is required before a confirmed defect or label removal. This successor corrects certainty only; it does not establish that the token is valid or that another identity allegation is fixed.

Disposition: Token presence remains reproducible, but the earlier pattern-based observation did not establish whether the exact source label denotes this subject or a different preparation. Fresh source-context adjudication is required before a confirmed defect or label removal. This successor corrects certainty only; it does not establish that the token is valid or that another identity allegation is fixed.

### scope-f-5982691d4b3d176b: Adjudicate source scope of exported tokens: Peptone

major / deferred / provisional; issue key: mim-reconciliation-exported-context-tokens-62f485f9f7517526.

Token presence remains reproducible, but the earlier pattern-based observation did not establish whether the exact source label denotes this subject or a different preparation. Fresh source-context adjudication is required before a confirmed defect or label removal. This successor corrects certainty only; it does not establish that the token is valid or that another identity allegation is fixed. A damaged spelling is observable, but the mapping contract permits damaged raw source forms when they still resolve to the same substance; malformed punctuation alone does not settle identity scope.

Disposition: Token presence remains reproducible, but the earlier pattern-based observation did not establish whether the exact source label denotes this subject or a different preparation. Fresh source-context adjudication is required before a confirmed defect or label removal. This successor corrects certainty only; it does not establish that the token is valid or that another identity allegation is fixed. A damaged spelling is observable, but the mapping contract permits damaged raw source forms when they still resolve to the same substance; malformed punctuation alone does not settle identity scope.

### scope-f-f582ea830b4f370d: Adjudicate source scope of exported tokens: Potassium phosphate buffer

major / deferred / provisional; issue key: mim-reconciliation-exported-context-tokens-4190c0ee5976447a.

Token presence remains reproducible, but the earlier pattern-based observation did not establish whether the exact source label denotes this subject or a different preparation. Fresh source-context adjudication is required before a confirmed defect or label removal. This successor corrects certainty only; it does not establish that the token is valid or that another identity allegation is fixed.

Disposition: Token presence remains reproducible, but the earlier pattern-based observation did not establish whether the exact source label denotes this subject or a different preparation. Fresh source-context adjudication is required before a confirmed defect or label removal. This successor corrects certainty only; it does not establish that the token is valid or that another identity allegation is fixed.

### scope-f-b7808e84d7886285: Adjudicate source scope of exported tokens: Riboflavin

major / deferred / provisional; issue key: mim-reconciliation-exported-context-tokens-59776f859c41300d.

Token presence remains reproducible, but the earlier pattern-based observation did not establish whether the exact source label denotes this subject or a different preparation. Fresh source-context adjudication is required before a confirmed defect or label removal. This successor corrects certainty only; it does not establish that the token is valid or that another identity allegation is fixed.

Disposition: Token presence remains reproducible, but the earlier pattern-based observation did not establish whether the exact source label denotes this subject or a different preparation. Fresh source-context adjudication is required before a confirmed defect or label removal. This successor corrects certainty only; it does not establish that the token is valid or that another identity allegation is fixed.

### scope-f-2680803ffb7b7f40: Adjudicate source scope of exported tokens: Sludge fluid

major / deferred / provisional; issue key: mim-reconciliation-exported-context-tokens-c6cdd023283a1f0a.

Token presence remains reproducible, but the earlier pattern-based observation did not establish whether the exact source label denotes this subject or a different preparation. Fresh source-context adjudication is required before a confirmed defect or label removal. This successor corrects certainty only; it does not establish that the token is valid or that another identity allegation is fixed.

Disposition: Token presence remains reproducible, but the earlier pattern-based observation did not establish whether the exact source label denotes this subject or a different preparation. Fresh source-context adjudication is required before a confirmed defect or label removal. This successor corrects certainty only; it does not establish that the token is valid or that another identity allegation is fixed.

### scope-f-ef4889c5708c1269: Adjudicate source scope of exported tokens: Soil extract

major / deferred / provisional; issue key: mim-reconciliation-exported-context-tokens-3245d67aff586e82.

Token presence remains reproducible, but the earlier pattern-based observation did not establish whether the exact source label denotes this subject or a different preparation. Fresh source-context adjudication is required before a confirmed defect or label removal. This successor corrects certainty only; it does not establish that the token is valid or that another identity allegation is fixed.

Disposition: Token presence remains reproducible, but the earlier pattern-based observation did not establish whether the exact source label denotes this subject or a different preparation. Fresh source-context adjudication is required before a confirmed defect or label removal. This successor corrects certainty only; it does not establish that the token is valid or that another identity allegation is fixed.

### scope-f-3b7b7b7cd4c70ace: Adjudicate source scope of exported tokens: Trace element solution see Medium No. 187

major / deferred / provisional; issue key: mim-reconciliation-exported-context-tokens-341efa75278b5e50.

Token presence remains reproducible, but the earlier pattern-based observation did not establish whether the exact source label denotes this subject or a different preparation. Fresh source-context adjudication is required before a confirmed defect or label removal. This successor corrects certainty only; it does not establish that the token is valid or that another identity allegation is fixed. A damaged spelling is observable, but the mapping contract permits damaged raw source forms when they still resolve to the same substance; malformed punctuation alone does not settle identity scope.

Disposition: Token presence remains reproducible, but the earlier pattern-based observation did not establish whether the exact source label denotes this subject or a different preparation. Fresh source-context adjudication is required before a confirmed defect or label removal. This successor corrects certainty only; it does not establish that the token is valid or that another identity allegation is fixed. A damaged spelling is observable, but the mapping contract permits damaged raw source forms when they still resolve to the same substance; malformed punctuation alone does not settle identity scope.

### scope-f-612aa67bad26d26a: Adjudicate source scope of exported tokens: Trace metal mix A5

major / deferred / provisional; issue key: mim-reconciliation-exported-context-tokens-78ea6a14a080dbf0.

Token presence remains reproducible, but the earlier pattern-based observation did not establish whether the exact source label denotes this subject or a different preparation. Fresh source-context adjudication is required before a confirmed defect or label removal. This successor corrects certainty only; it does not establish that the token is valid or that another identity allegation is fixed.

Disposition: Token presence remains reproducible, but the earlier pattern-based observation did not establish whether the exact source label denotes this subject or a different preparation. Fresh source-context adjudication is required before a confirmed defect or label removal. This successor corrects certainty only; it does not establish that the token is valid or that another identity allegation is fixed.

### scope-f-54e5335934e0ba03: Adjudicate source scope of exported tokens: Trace mineral solution

major / deferred / provisional; issue key: mim-reconciliation-exported-context-tokens-4b03942a3427132e.

Token presence remains reproducible, but the earlier pattern-based observation did not establish whether the exact source label denotes this subject or a different preparation. Fresh source-context adjudication is required before a confirmed defect or label removal. This successor corrects certainty only; it does not establish that the token is valid or that another identity allegation is fixed.

Disposition: Token presence remains reproducible, but the earlier pattern-based observation did not establish whether the exact source label denotes this subject or a different preparation. Fresh source-context adjudication is required before a confirmed defect or label removal. This successor corrects certainty only; it does not establish that the token is valid or that another identity allegation is fixed.

### scope-f-0fa9eaef6cc34337: Adjudicate source scope of exported tokens: Trace minerals

major / deferred / provisional; issue key: mim-reconciliation-exported-context-tokens-7c55027f9d88edd0.

Token presence remains reproducible, but the earlier pattern-based observation did not establish whether the exact source label denotes this subject or a different preparation. Fresh source-context adjudication is required before a confirmed defect or label removal. This successor corrects certainty only; it does not establish that the token is valid or that another identity allegation is fixed.

Disposition: Token presence remains reproducible, but the earlier pattern-based observation did not establish whether the exact source label denotes this subject or a different preparation. Fresh source-context adjudication is required before a confirmed defect or label removal. This successor corrects certainty only; it does not establish that the token is valid or that another identity allegation is fixed.

### scope-f-397b1df68e373137: Adjudicate source scope of exported tokens: Yeast extract

major / deferred / provisional; issue key: mim-reconciliation-exported-context-tokens-4efe2f6907f0d4fc.

Token presence remains reproducible, but the earlier pattern-based observation did not establish whether the exact source label denotes this subject or a different preparation. Fresh source-context adjudication is required before a confirmed defect or label removal. This successor corrects certainty only; it does not establish that the token is valid or that another identity allegation is fixed. A damaged spelling is observable, but the mapping contract permits damaged raw source forms when they still resolve to the same substance; malformed punctuation alone does not settle identity scope.

Disposition: Token presence remains reproducible, but the earlier pattern-based observation did not establish whether the exact source label denotes this subject or a different preparation. Fresh source-context adjudication is required before a confirmed defect or label removal. This successor corrects certainty only; it does not establish that the token is valid or that another identity allegation is fixed. A damaged spelling is observable, but the mapping contract permits damaged raw source forms when they still resolve to the same substance; malformed punctuation alone does not settle identity scope.

## Recommended Actions And Acceptance Checks

### scope-f-be91e29ea6694d28

Inspect the exact originating source label and preparation before deciding synonym scope.

- Read the exact recipe or source row and document whether the label denotes this subject, a different preparation, or an instruction fragment.
- Preserve valid RAW_TEXT and catalog names; reject a resolving label only with claim-level scope evidence.
- Save a successor with this exact issue key and occurrence; address independent identity allegations separately.

### scope-f-e1004757f90e8c13

Inspect the exact originating source label and preparation before deciding synonym scope.

- Read the exact recipe or source row and document whether the label denotes this subject, a different preparation, or an instruction fragment.
- Preserve valid RAW_TEXT and catalog names; reject a resolving label only with claim-level scope evidence.
- Save a successor with this exact issue key and occurrence; address independent identity allegations separately.

### scope-f-838d67873b6673db

Inspect the exact originating source label and preparation before deciding synonym scope.

- Read the exact recipe or source row and document whether the label denotes this subject, a different preparation, or an instruction fragment.
- Preserve valid RAW_TEXT and catalog names; reject a resolving label only with claim-level scope evidence.
- Save a successor with this exact issue key and occurrence; address independent identity allegations separately.

### scope-f-320ccfb6bddc74ee

Inspect the exact originating source label and preparation before deciding synonym scope.

- Read the exact recipe or source row and document whether the label denotes this subject, a different preparation, or an instruction fragment.
- Preserve valid RAW_TEXT and catalog names; reject a resolving label only with claim-level scope evidence.
- Save a successor with this exact issue key and occurrence; address independent identity allegations separately.

### scope-f-853c7e2e707eedfc

Inspect the exact originating source label and preparation before deciding synonym scope.

- Read the exact recipe or source row and document whether the label denotes this subject, a different preparation, or an instruction fragment.
- Preserve valid RAW_TEXT and catalog names; reject a resolving label only with claim-level scope evidence.
- Save a successor with this exact issue key and occurrence; address independent identity allegations separately.

### scope-f-43e56706181e97b8

Inspect the exact originating source label and preparation before deciding synonym scope.

- Read the exact recipe or source row and document whether the label denotes this subject, a different preparation, or an instruction fragment.
- Preserve valid RAW_TEXT and catalog names; reject a resolving label only with claim-level scope evidence.
- Save a successor with this exact issue key and occurrence; address independent identity allegations separately.

### scope-f-d3696f2daf45c433

Inspect the exact originating source label and preparation before deciding synonym scope.

- Read the exact recipe or source row and document whether the label denotes this subject, a different preparation, or an instruction fragment.
- Preserve valid RAW_TEXT and catalog names; reject a resolving label only with claim-level scope evidence.
- Save a successor with this exact issue key and occurrence; address independent identity allegations separately.

### scope-f-5982691d4b3d176b

Inspect the exact originating source label and preparation before deciding synonym scope.

- Read the exact recipe or source row and document whether the label denotes this subject, a different preparation, or an instruction fragment.
- Preserve valid RAW_TEXT and catalog names; reject a resolving label only with claim-level scope evidence.
- Save a successor with this exact issue key and occurrence; address independent identity allegations separately.

### scope-f-f582ea830b4f370d

Inspect the exact originating source label and preparation before deciding synonym scope.

- Read the exact recipe or source row and document whether the label denotes this subject, a different preparation, or an instruction fragment.
- Preserve valid RAW_TEXT and catalog names; reject a resolving label only with claim-level scope evidence.
- Save a successor with this exact issue key and occurrence; address independent identity allegations separately.

### scope-f-b7808e84d7886285

Inspect the exact originating source label and preparation before deciding synonym scope.

- Read the exact recipe or source row and document whether the label denotes this subject, a different preparation, or an instruction fragment.
- Preserve valid RAW_TEXT and catalog names; reject a resolving label only with claim-level scope evidence.
- Save a successor with this exact issue key and occurrence; address independent identity allegations separately.

### scope-f-2680803ffb7b7f40

Inspect the exact originating source label and preparation before deciding synonym scope.

- Read the exact recipe or source row and document whether the label denotes this subject, a different preparation, or an instruction fragment.
- Preserve valid RAW_TEXT and catalog names; reject a resolving label only with claim-level scope evidence.
- Save a successor with this exact issue key and occurrence; address independent identity allegations separately.

### scope-f-ef4889c5708c1269

Inspect the exact originating source label and preparation before deciding synonym scope.

- Read the exact recipe or source row and document whether the label denotes this subject, a different preparation, or an instruction fragment.
- Preserve valid RAW_TEXT and catalog names; reject a resolving label only with claim-level scope evidence.
- Save a successor with this exact issue key and occurrence; address independent identity allegations separately.

### scope-f-3b7b7b7cd4c70ace

Inspect the exact originating source label and preparation before deciding synonym scope.

- Read the exact recipe or source row and document whether the label denotes this subject, a different preparation, or an instruction fragment.
- Preserve valid RAW_TEXT and catalog names; reject a resolving label only with claim-level scope evidence.
- Save a successor with this exact issue key and occurrence; address independent identity allegations separately.

### scope-f-612aa67bad26d26a

Inspect the exact originating source label and preparation before deciding synonym scope.

- Read the exact recipe or source row and document whether the label denotes this subject, a different preparation, or an instruction fragment.
- Preserve valid RAW_TEXT and catalog names; reject a resolving label only with claim-level scope evidence.
- Save a successor with this exact issue key and occurrence; address independent identity allegations separately.

### scope-f-54e5335934e0ba03

Inspect the exact originating source label and preparation before deciding synonym scope.

- Read the exact recipe or source row and document whether the label denotes this subject, a different preparation, or an instruction fragment.
- Preserve valid RAW_TEXT and catalog names; reject a resolving label only with claim-level scope evidence.
- Save a successor with this exact issue key and occurrence; address independent identity allegations separately.

### scope-f-0fa9eaef6cc34337

Inspect the exact originating source label and preparation before deciding synonym scope.

- Read the exact recipe or source row and document whether the label denotes this subject, a different preparation, or an instruction fragment.
- Preserve valid RAW_TEXT and catalog names; reject a resolving label only with claim-level scope evidence.
- Save a successor with this exact issue key and occurrence; address independent identity allegations separately.

### scope-f-397b1df68e373137

Inspect the exact originating source label and preparation before deciding synonym scope.

- Read the exact recipe or source row and document whether the label denotes this subject, a different preparation, or an instruction fragment.
- Preserve valid RAW_TEXT and catalog names; reject a resolving label only with claim-level scope evidence.
- Save a successor with this exact issue key and occurrence; address independent identity allegations separately.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-823412d1eacb6795 | MAPPING_SEMANTICS.md; Sections on REJECTED_LABEL and the damaged-label RAW_TEXT carve-out | supports | Raw spellings may remain resolvable when they denote the same substance. Wrong-identity labels must not resolve. A recipe-pointer pattern alone does not adjudicate that distinction. |
| ev-f983f8801d1e4699 | reviews/structured/20261011T024630Z-mim-reconcile-all-batch-02/review.yaml; findings[finding_id=f-be91e29ea6694d28] | context_only | Exact earlier occurrence has open/confirmed status, based on exported-token presence and historical report text. |
| ev-d8b130cb30e86aec | data/ingredients/mapped/4-vinylphenol.yaml; identifier, ontology_mapping, synonyms and curation_history | partial | {"candidate_labels": [{"source": "sssom_other_backfill", "synonym_text": "Trace minerals (see Medium No.151", "synonym_type": "RAW_TEXT"}, {"source": "sssom_other_backfill", "synonym_text": "Trace minerals(see Medium No.151)", "synonym_type": "RAW_TEXT"}], "history": [{"action": "CREATED_FROM_CAS_LOOKUP", "changes": "Created from CultureBotHT CAS-RN=2628-17-3; CHEBI resolved via OAK CHEBI sqlite (cas xref); Imported from CultureBotHT. CAS-RN\u2192CHEBI mapping resolved via OAK CHEBI sqlite (cas xref). ", "curator": "audit_cas_chebi_followup", "llm_assisted": false, "new_status": "MAPPED", "timestamp": "2026-04-29T06:34:31.158938+00:00"}, {"action": "AUTO_CLASSIFY_INGREDIENT_TYPE", "changes": "set ingredient_type=SINGLE_INGREDIENT (CHEBI primary)", "curator": "auto_classify_ingredient_type", "llm_assisted": false, "timestamp": "2026-05-01T07:35:31.933265+00:00"}, {"action": "AUTO_BACKFILL_CHEBI_CHEMISTRY", "changes": "molecular_formula=C8H8O; inchi=InChI=1S/C8H8O/c1-2-7-3-5-8(9)6-4-7/h2-6,9H,1H2; smiles=C=Cc1ccc(O)cc1", "curator": "auto_classify_ingredient_type", "llm_assisted": false, "timestamp": "2026-05-01T08:08:27.759520+00:00"}, {"action": "AUTO_CLASSIFY_INGREDIENT_TYPE", "changes": "set ingredient_type=SINGLE_INGREDIENT (chemical structure populated (molecular_formula))", "curator": "auto_classify_ingredient_type", "llm_assisted": false, "timestamp": "2026-05-02T03:12:12.131604+00:00"}, {"action": "REGRADED_EXACT_TO_SYNONYM", "changes": "mapping_quality EXACT_MATCH -&gt; SYNONYM_MATCH (#317). The record's label does not equal the term's primary label '4-hydroxystyrene'; it matches the ChEBI synonym '4-vinylphenol' on CHEBI:1883. The schema defines EXACT_MATCH as a direct match to the term and SYNONYM_MATCH as a match to a known synonym, so the recorded grade overstated. ontology_id is unchanged \u2014 the term is correct. The SSSOM predicate is unaffected (both grades emit skos:exactMatch).", "curator": "regrade_synonym_matches", "llm_assisted": false, "timestamp": "2026-08-10T00:00:00+00:00"}, {"action": "REGRADED_TO_CAS_RN_LOOKUP", "changes": "mapping_quality SYNONYM_MATCH -&gt; CAS_RN_LOOKUP (#317). The record was created by an explicit CAS-to-ChEBI lookup and its current CAS RN 2628-17-3 uniquely resolves by ChEBI xref to CHEBI:1883 '4-hydroxystyrene'. CAS_RN_LOOKUP records the method that established this mapping; a lexical grade would discard that provenance. ontology_id is unchanged. The own-identifier SSSOM predicate remains skos:exactMatch under Rule D (#438), independently of mapping quality.", "curator": "regrade_synonym_matches", "llm_assisted": false, "timestamp": "2026-08-24T00:00:00+00:00"}, {"action": "ADDED_SYNONYMS", "changes": "Recovered 1 surface form(s) that the published SSSOM &#96;other&#96; carried but no curated record did, so a rebuild would have dropped them from KGX: 'Trace minerals (see Medium No.151'. Tokens already present on the kg-microbe ontology node were left out as redundant (#520).", "curator": "claude_sssom_surface_form_backfill", "llm_assisted": false, "timestamp": "2026-09-02T17:40:44.716277+00:00"}, {"action": "ADDED_SYNONYMS", "changes": "Recovered 1 surface form(s) that the published SSSOM &#96;other&#96; carried but no curated record did, so a rebuild would have dropped them from KGX: 'Trace minerals(see Medium No.151)'. Tokens already present on the kg-microbe ontology node were left out as redundant (#520).", "curator": "claude_sssom_surface_form_backfill", "llm_assisted": false, "timestamp": "2026-09-02T22:41:49.137449+00:00"}], "identifier": "CHEBI:1883", "mapping": {"evidence": [{"evidence_type": "DATABASE_MATCH", "notes": "Imported from CultureBotHT. CAS-RN\u2192CHEBI mapping resolved via OAK CHEBI sqlite (cas xref). ", "source": "CultureBotHT"}], "mapping_quality": "CAS_RN_LOOKUP", "ontology_id": "CHEBI:1883", "ontology_label": "4-hydroxystyrene", "ontology_source": "CHEBI"}} |
| ev-0de8553689e72bef | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:4-vinylphenol | supports | [{"comment": "", "confidence": "0.9", "data_row": 215, "mapping_date": "2026-09-02", "mapping_justification": "semapv:ManualMappingCuration", "object_id": "CHEBI:1883", "object_label": "4-hydroxystyrene", "object_source": "obo:chebi.owl", "other": "4-ethenylphenol&#124;Trace minerals (see Medium No.151&#124;Trace minerals(see Medium No.151)&#124;CAS:2628-17-3", "predicate_id": "skos:exactMatch", "source": "MIM:CultureBotHT&#124;MIM:curator=claude_sssom_surface_form_backfill&#124;kgm:chebi_xrefs&#124;kgm:mediadive_compounds&#124;kgm:mediaingredientmech_reviewed&#124;kgm:mediaingredientmech_reviewed[curator=audit_cas_chebi_followup]&#124;kgm:mediaingredientmech_reviewed[curator=auto_classify_ingredient_type]&#124;kgm:mediaingredientmech_reviewed[curator=regrade_synonym_matches]&#124;kgm:primary_mappings[kegg_compound]", "subject_id": "MIM:4-vinylphenol", "subject_label": "4-vinylphenol", "validation_method": "OAK+OLS:chebi&#124;CONFIRMED&#124;2026-07-07"}] |
| ev-93f74be01346ddd4 | reports/yaml_record_review/4-vinylphenol.md; Complete historical report, including Verdict and Recommended Edits | context_only | Historical interpretation was read in full; it is not fresh source adjudication. |
| ev-8fab9fb02ee4454f | reviews/structured/20261011T024631Z-mim-reconcile-all-batch-03/review.yaml; findings[finding_id=f-e1004757f90e8c13] | context_only | Exact earlier occurrence has open/confirmed status, based on exported-token presence and historical report text. |
| ev-f5500c887f4dc734 | data/ingredients/mapped/Artificial_seawater.yaml; identifier, ontology_mapping, synonyms and curation_history | partial | {"candidate_labels": [{"source": "culturemech:output/ingredient_occurrences.tsv", "synonym_text": "Artificial seawater (see below)", "synonym_type": "RAW_TEXT"}, {"source": "culturemech:output/ingredient_occurrences.tsv", "synonym_text": "Artificial seawater (see Medium No. 736 )", "synonym_type": "RAW_TEXT"}], "history": [{"action": "CREATED_FROM_CULTUREMECH_RESIDUAL", "changes": "Created from a CultureMech recipe ingredient MIM held no record for (19 mentions across 19 recipes). Grounded to MICRO:0001715 ('artificial seawater') on an exact match of the canonical label to the query 'Artificial seawater'. Source: culturemech:output/ingredient_occurrences.tsv.", "curator": "claude_culturemech_residual_grounding", "llm_assisted": false, "new_status": "MAPPED", "timestamp": "2026-08-30T10:35:03.361102+00:00"}, {"action": "ADDED_SYNONYMS", "changes": "Added 2 CultureMech recipe surface form(s) that folded onto this record's published label but were absent from MIM's label index, so CultureMech could not resolve them: 'Artificial seawater (see below)' (x7 CultureMech mentions); 'Artificial seawater (see Medium No. 736 )' (x1 CultureMech mentions). Source: culturemech:output/ingredient_occurrences.tsv.", "curator": "claude_culturemech_alias_backfill", "llm_assisted": false, "timestamp": "2026-08-30T10:41:26.546472+00:00"}, {"action": "CORRECTED", "changes": "Added ontology_mapping.evidence recording the CultureMech occurrence table as the source of this grounding. The provenance was already in this record's CREATED_FROM_CULTUREMECH_RESIDUAL history entry but absent from the structured field the SSSOM builder reads, so a rebuild dropped MIM:culturemech:output/ingredient_occurrences.tsv from the published row (#541).", "curator": "claude_restore_culturemech_evidence", "llm_assisted": false, "timestamp": "2026-09-06T07:34:56.956907+00:00"}], "identifier": "MICRO:0001715", "mapping": {"evidence": [{"evidence_type": "LEXICAL_MATCH", "notes": "Surface form appears in CultureMech's occurrence table and was grounded to MICRO:0001715 on an exact match against the ontology label. Restored from the record's own creation history (#541); the residual importer wrote this provenance only into the published SSSOM.", "source": "culturemech:output/ingredient_occurrences.tsv"}], "mapping_quality": "EXACT_MATCH", "match_level": "EXACT", "ontology_id": "MICRO:0001715", "ontology_label": "artificial seawater", "ontology_source": "MICRO"}} |
| ev-16c562c2dbdbab95 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Artificial_seawater | supports | [{"comment": "", "confidence": "0.99", "data_row": 435, "mapping_date": "2026-09-06", "mapping_justification": "semapv:LexicalMatching", "object_id": "MICRO:0001715", "object_label": "artificial seawater", "object_source": "obo:micro.owl", "other": "Artificial seawater (see below)&#124;Artificial seawater (see Medium No. 736 )", "predicate_id": "skos:exactMatch", "source": "MIM:culturemech:output/ingredient_occurrences.tsv&#124;MIM:curator=claude_restore_culturemech_evidence", "subject_id": "MIM:Artificial_seawater", "subject_label": "Artificial seawater", "validation_method": "manual:claude_culturemech_residual_grounding&#124;CREATED&#124;2026-08-30"}] |
| ev-8ca93b32516cbb52 | reports/yaml_record_review/Artificial_seawater.md; Complete historical report, including Verdict and Recommended Edits | context_only | Historical interpretation was read in full; it is not fresh source adjudication. |
| ev-e6798c510d069e5f | reviews/structured/20261011T024633Z-mim-reconcile-all-batch-05/review.yaml; findings[finding_id=f-838d67873b6673db] | context_only | Exact earlier occurrence has open/confirmed status, based on exported-token presence and historical report text. |
| ev-f0c42034b2f08a1d | data/ingredients/mapped/DL_Vitamins.yaml; identifier, ontology_mapping, synonyms and curation_history | partial | {"candidate_labels": [{"source": "culturemech:output/ingredient_occurrences.tsv", "synonym_text": "DL vitamins (see below)", "synonym_type": "RAW_TEXT"}], "history": [{"action": "CREATED_AS_UNMAPPED", "changes": "Imported from CultureBotHT (consolidated_media.json (media-only)). Used in 6 CultureBot media; samples: SCFM, Hans_Basal_Media, Hans_Basal_Media_plus_0.2x_20AA_mix\u2026. No CAS-RN or CHEBI mapping available; curator review needed.", "curator": "audit_add_remaining_culturebotht", "llm_assisted": false, "new_status": "UNMAPPED", "timestamp": "2026-04-29T06:51:33.117170+00:00"}, {"action": "CLASSIFIED_STOCK_SOLUTION", "changes": "Classified as a vitamin stock/pre-mix and left unmapped pending component-level recipe curation.", "curator": "mediaingredientmech-agentic-curation", "llm_assisted": true, "new_status": "UNMAPPED", "previous_status": "UNMAPPED", "timestamp": "2026-05-11T09:30:00Z"}, {"action": "PROMOTED_TO_MAPPED", "changes": "Promoted UNMAPPED_0277 -&gt; kgmicrobe.ingredient:dl_vitamins \"DL vitamins\" (FALLBACK_REGISTRY); mapping_status UNMAPPED -&gt; MAPPED, SSSOM row added.", "curator": "promote_resolved_unmapped", "llm_assisted": false, "new_status": "MAPPED", "previous_status": "UNMAPPED", "timestamp": "2026-08-06T00:00:00+00:00"}, {"action": "ADDED_SYNONYMS", "changes": "Added 1 CultureMech recipe surface form(s) that folded onto this record's published label but were absent from MIM's label index, so CultureMech could not resolve them: 'DL vitamins (see below)' (x1 CultureMech mentions). Source: culturemech:output/ingredient_occurrences.tsv.", "curator": "claude_culturemech_alias_backfill", "llm_assisted": false, "timestamp": "2026-08-30T04:48:06.233536+00:00"}, {"action": "ANNOTATED", "changes": "Transcribed the CultureBotHT Mixes-tab recipe for DL vitamins and added complete component partonomy for its 10 vitamin-stock constituents plus a source-backed vitamin role.", "curator": "mediaingredientmech-agentic-curation", "llm_assisted": true, "llm_model": "gpt-5", "new_status": "MAPPED", "timestamp": "2026-09-08T00:00:00+00:00"}], "identifier": "kgmicrobe.ingredient:dl_vitamins", "mapping": {"evidence": [{"evidence_type": "DATABASE_MATCH", "notes": "DL vitamins is a named, recurring multi-component preparation (6 media). Searched CHEBI, NCIT, MeSH, FOODON and ENVO by label and synonym with normalisation: no term denotes it, and none could -- it is a lab preparation rather than a substance. Takes the STOCK_SOLUTION convention used by the existing mapped records: a kgmicrobe.ingredient: mint, with no parent because a multi-component mix does not narrow to any single compound (#114).", "source": "MIM curation (#114)"}], "mapping_quality": "FALLBACK_REGISTRY", "ontology_id": "kgmicrobe.ingredient:dl_vitamins", "ontology_label": "DL vitamins", "ontology_source": "kgmicrobe.ingredient"}} |
| ev-82824a1888d907ee | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:DL_Vitamins | supports | [{"comment": "", "confidence": "0.9", "data_row": 993, "mapping_date": "2026-08-30", "mapping_justification": "semapv:ManualMappingCuration", "object_id": "kgmicrobe.ingredient:dl_vitamins", "object_label": "DL vitamins", "object_source": "kgm:ingredient", "other": "DL vitamins (see below)", "predicate_id": "skos:exactMatch", "source": "MIM:MIM curation (#114)&#124;MIM:curator=claude_culturemech_alias_backfill", "subject_id": "MIM:DL_Vitamins", "subject_label": "DL vitamins", "validation_method": "none&#124;UNKNOWN_TERM&#124;2026-09-02"}] |
| ev-0bef314ac38155d7 | reports/yaml_record_review/DL_Vitamins.md; Complete historical report, including Verdict and Recommended Edits | context_only | Historical interpretation was read in full; it is not fresh source adjudication. |
| ev-9477d91976d0a888 | reviews/structured/20261011T024633Z-mim-reconcile-all-batch-05/review.yaml; findings[finding_id=f-320ccfb6bddc74ee] | context_only | Exact earlier occurrence has open/confirmed status, based on exported-token presence and historical report text. |
| ev-4d30788725c98994 | data/ingredients/mapped/Desulfovibrio_Trace_Elements.yaml; identifier, ontology_mapping, synonyms and curation_history | partial | {"candidate_labels": [{"source": "culturemech:output/ingredient_occurrences.tsv", "synonym_text": "Trace elements (see below)", "synonym_type": "RAW_TEXT"}], "history": [{"action": "CREATED_AS_UNMAPPED", "changes": "Imported from CultureBotHT (consolidated_media.json (media-only)). Used in 3 CultureBot media; samples: MoLS4, Dv_base_medium, MoLS4_no_vitamins. No CAS-RN or CHEBI mapping available; curator review needed.", "curator": "audit_add_remaining_culturebotht", "llm_assisted": false, "new_status": "UNMAPPED", "timestamp": "2026-04-29T06:51:33.117170+00:00"}, {"action": "AUTO_UPGRADE_TO_MESH", "changes": "primary UNMAPPED_0294 \u2192 mesh:D014131 (strategy=stem-match)", "curator": "resolve_unmapped_v2", "llm_assisted": false, "timestamp": "2026-05-02T03:18:21.917940+00:00"}, {"action": "ANNOTATED", "changes": "Added media role: TRACE_ELEMENT (confidence: 0.60)", "curator": "claude_in_session_curation", "timestamp": "2026-06-09T04:56:30.247868+00:00"}, {"action": "ANNOTATED", "changes": "Migrated legacy media_roles to role facets (#128): TRACE_ELEMENT -&gt; nutritional_roles.TRACE_ELEMENT", "curator": "migrate_media_roles_to_facets", "timestamp": "2026-07-20T00:00:00+00:00"}, {"action": "ADDED_SYNONYMS", "changes": "Added 1 CultureMech recipe surface form(s) that folded onto this record's published label but were absent from MIM's label index, so CultureMech could not resolve them: 'Trace elements (see below)' (x1 CultureMech mentions). Source: culturemech:output/ingredient_occurrences.tsv.", "curator": "claude_culturemech_alias_backfill", "llm_assisted": false, "timestamp": "2026-08-30T04:48:06.233536+00:00"}], "identifier": "mesh:D014131", "mapping": {"evidence": [{"evidence_type": "DATABASE_MATCH", "notes": "Auto-upgraded from UNMAPPED_0294; matched via 'Desulfovibrio trace elements'; stem-substring", "source": "MESH via OLS (resolve_unmapped_v2 strategy=stem-match)"}], "mapping_quality": "LEXICAL_MATCH", "ontology_id": "mesh:D014131", "ontology_label": "Trace Elements", "ontology_source": "MESH"}} |
| ev-a255c9d3059064fe | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Desulfovibrio_Trace_Elements | supports | [{"comment": "", "confidence": "0.9", "data_row": 1021, "mapping_date": "2026-08-30", "mapping_justification": "semapv:LexicalMatching", "object_id": "mesh:D014131", "object_label": "Trace Elements", "object_source": "registry:mesh", "other": "Trace elements (see below)", "predicate_id": "skos:exactMatch", "source": "MIM:MESH via OLS (resolve_unmapped_v2 strategy=stem-match)&#124;MIM:curator=claude_culturemech_alias_backfill", "subject_id": "MIM:Desulfovibrio_Trace_Elements", "subject_label": "Desulfovibrio trace elements", "validation_method": "none&#124;UNKNOWN_TERM&#124;2026-07-07"}] |
| ev-e7674a969ec8d8cb | reports/yaml_record_review/Desulfovibrio_Trace_Elements.md; Complete historical report, including Verdict and Recommended Edits | context_only | Historical interpretation was read in full; it is not fresh source adjudication. |
| ev-997c904ed0a9e395 | reviews/structured/20261011T024634Z-mim-reconcile-all-batch-06/review.yaml; findings[finding_id=f-853c7e2e707eedfc] | context_only | Exact earlier occurrence has open/confirmed status, based on exported-token presence and historical report text. |
| ev-66223de2980eb719 | data/ingredients/mapped/Fatty_Acid_Mixture_See_Medium_No_266.yaml; identifier, ontology_mapping, synonyms and curation_history | partial | {"candidate_labels": [{"source": "culturemech:output/ingredient_occurrences.tsv", "synonym_text": "Fatty acid mixture (see below)", "synonym_type": "RAW_TEXT"}], "history": [{"action": "IMPORTED", "changes": "Initial import from CultureMech pipeline", "curator": "import_from_culturemech", "llm_assisted": false, "new_status": "MAPPED", "timestamp": "2026-03-09T06:54:18.022301+00:00"}, {"action": "ADDED_SYNONYMS", "changes": "Added 8 synonyms from kg-microbe P4.4 enrichment: Fatty acid, Fettsaeure, Fettsaeuren, acide gras, acides gras, ... (3 more)", "curator": "cbclaw_kg_microbe_sweep", "llm_assisted": true, "new_status": "MAPPED", "timestamp": "2026-04-18T00:00:00+00:00"}, {"action": "AUTO_CLASSIFY_INGREDIENT_TYPE", "changes": "set ingredient_type=DEFINED_MEDIUM (name matches medium pattern 'Medium No')", "curator": "auto_classify_ingredient_type", "llm_assisted": false, "timestamp": "2026-05-01T07:35:33.505726+00:00"}, {"action": "AUTO_BACKFILL_CHEBI_CHEMISTRY", "changes": "molecular_formula=CHO2R; smiles=*C(=O)O", "curator": "auto_classify_ingredient_type", "llm_assisted": false, "timestamp": "2026-05-01T08:08:29.482671+00:00"}, {"action": "CLASSIFY_AS_STOCK_SOLUTION", "changes": "name pattern 'see Medium No.' indicates pre-mixed defined solution", "curator": "auto_classify_stock_solution", "llm_assisted": false, "timestamp": "2026-05-01T19:58:08.951391+00:00"}, {"action": "AUTO_CLASSIFY_INGREDIENT_TYPE", "changes": "set ingredient_type=SINGLE_INGREDIENT (chemical structure populated (molecular_formula))", "curator": "auto_classify_ingredient_type", "llm_assisted": false, "timestamp": "2026-05-02T03:12:14.341135+00:00"}, {"action": "CORRECTED", "changes": "ontology_label 'Fatty acid mixture (see Medium No. 266)' -&gt; 'fatty acid': synced to canonical CHEBI label (preferred_term 'Fatty acid mixture (see Medium No. 266)' unchanged).", "curator": "correct_stale_ontology_labels.py", "timestamp": "2026-06-09T05:23:46.762837+00:00"}, {"action": "CORRECTED", "changes": "occurrence_statistics 2/2 -&gt; 4/4 (media_count/total_occurrences), derived from distinct CultureMech recipe ids in the #337 occurrence table. The prior values came from the importer retired in #453, whose media_count counted a list truncated to 50 examples (#449). [source=ingredient_occurrences.tsv culturemech_rev=15a4da5c08 rows=194137 distinct_recipes=15257]", "curator": "refresh_occurrence_statistics", "timestamp": "2026-08-27T03:16:39.518810+00:00"}, {"action": "ADDED_SYNONYMS", "changes": "Added 2 CultureMech recipe surface form(s) that folded onto this record's published label but were absent from MIM's label index, so CultureMech could not resolve them: 'Fatty acid mixture' (x3 CultureMech mentions); 'Fatty acid mixture (see below)' (x1 CultureMech mentions). Source: culturemech:output/ingredient_occurrences.tsv.", "curator": "claude_culturemech_alias_backfill", "llm_assisted": false, "timestamp": "2026-08-30T04:48:06.233536+00:00"}], "identifier": "CHEBI:35366", "mapping": {"evidence": [{"evidence_type": "DATABASE_MATCH", "notes": "Imported from CultureMech pipeline, quality=DIRECT_MATCH", "source": "CultureMech"}], "mapping_quality": "EXACT_MATCH", "ontology_id": "CHEBI:35366", "ontology_label": "fatty acid", "ontology_source": "CHEBI"}} |
| ev-6b0f037f5dc84aa9 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Fatty_Acid_Mixture_See_Medium_No_266 | supports | [{"comment": "", "confidence": "0.99", "data_row": 1165, "mapping_date": "2026-08-30", "mapping_justification": "semapv:LexicalMatching", "object_id": "CHEBI:35366", "object_label": "fatty acid", "object_source": "obo:chebi.owl", "other": "Fettsaeure&#124;Fettsaeuren&#124;acide gras&#124;acides gras&#124;acido graso&#124;acidos grasos&#124;fatty acids&#124;Fatty acid mixture&#124;Fatty acid mixture (see below)", "predicate_id": "skos:exactMatch", "source": "MIM:CultureMech&#124;MIM:curator=claude_culturemech_alias_backfill&#124;kgm:chebi_xrefs&#124;kgm:culturebotai_reviewed&#124;kgm:mediaingredientmech_reviewed&#124;kgm:mediaingredientmech_reviewed[curator=auto_classify_ingredient_type]&#124;kgm:mediaingredientmech_reviewed[curator=auto_classify_stock_solution]&#124;kgm:mediaingredientmech_reviewed[curator=cbclaw_kg_microbe_sweep]&#124;kgm:mediaingredientmech_reviewed[curator=correct_stale_ontology_labels.py]&#124;kgm:primary_mappings[kegg_compound]", "subject_id": "MIM:Fatty_Acid_Mixture_See_Medium_No_266", "subject_label": "Fatty acid mixture (see Medium No. 266)", "validation_method": "OAK+OLS:chebi&#124;SYNONYM_ENRICH&#124;2026-07-07"}] |
| ev-abc54f67fc204f62 | reports/yaml_record_review/Fatty_Acid_Mixture_See_Medium_No_266.md; Complete historical report, including Verdict and Recommended Edits | context_only | Historical interpretation was read in full; it is not fresh source adjudication. |
| ev-b91360770608ed24 | reviews/structured/20261011T024636Z-mim-reconcile-all-batch-08/review.yaml; findings[finding_id=f-43e56706181e97b8] | context_only | Exact earlier occurrence has open/confirmed status, based on exported-token presence and historical report text. |
| ev-423b314156ab28a8 | data/ingredients/mapped/Mineral_Solution_See_Medium_No_976.yaml; identifier, ontology_mapping, synonyms and curation_history | partial | {"candidate_labels": [{"source": "culturemech:output/ingredient_occurrences.tsv", "synonym_text": "Mineral solution (see Medium No. 976", "synonym_type": "RAW_TEXT"}], "history": [{"action": "CREATED_AS_UNMAPPED", "changes": "Imported from mim-queue (source_id=mediadive.ingredient:1958); no CAS-RN or CHEBI/NCIT match. Curator review needed.", "curator": "audit_import_ingredients[mim-queue]", "llm_assisted": false, "new_status": "UNMAPPED", "timestamp": "2026-04-30T18:43:03.698454+00:00"}, {"action": "CLASSIFY_AS_STOCK_SOLUTION", "changes": "name pattern 'see Medium No.' indicates pre-mixed defined solution", "curator": "auto_classify_stock_solution", "llm_assisted": false, "timestamp": "2026-05-01T19:58:07.078790+00:00"}, {"action": "AUTO_CLASSIFY_INGREDIENT_TYPE", "changes": "set ingredient_type=STOCK_SOLUTION (name matches solution pattern 'Mineral solution')", "curator": "auto_classify_ingredient_type", "llm_assisted": false, "timestamp": "2026-05-02T03:12:19.749949+00:00"}, {"action": "PROMOTED_TO_MAPPED", "changes": "Promoted UNMAPPED_0447 -&gt; kgmicrobe.ingredient:mineral_solution_see_medium_no_976 (FALLBACK_REGISTRY). A named multi-component preparation. Searched CHEBI, NCIT, MeSH, FOODON and ENVO by label and synonym: no term denotes it, and none could -- a preparation is not a substance. Takes the STOCK_SOLUTION convention: a kgmicrobe.ingredient: mint with no parent, because a multi-component mix does not narrow to any single compound (#288).", "curator": "issue_288_stock_solutions", "llm_assisted": true, "new_status": "MAPPED", "previous_status": "UNMAPPED", "timestamp": "2026-08-06T00:00:00+00:00"}, {"action": "FLAGGED_NEEDS_EXPERT", "changes": "Reverted the mint and flagged NEEDS_EXPERT instead. \"Mineral solution see Medium No. 976\" is a CROSS-REFERENCE to another medium, not the name of a substance -- minting an identifier for it would give a pointer its own identity. The #288 batch minted it because it filtered on ingredient_type STOCK_SOLUTION without reading the label. The referenced medium should be resolved and this record either replaced by that mineral solution or retired (#288).", "curator": "issue_288_stock_solutions", "llm_assisted": true, "new_status": "NEEDS_EXPERT", "previous_status": "MAPPED", "timestamp": "2026-08-06T00:00:00+00:00"}, {"action": "ANNOTATED", "changes": "Edison LITERATURE (PaperQA3) identity research; report at research/ingredients/Mineral_Solution_See_Medium_No_976-edison-literature.md (local artifact \u2014 research/ is gitignored, so the findings are quoted here rather than linked). Report reached no single bolded verdict; see the report. No ontology CURIE was proposed. Recorded as provenance only \u2014 no grounding applied from this run. Edison's recommendations are deliberately conservative, and a plausible identifier promoted by a mechanism that never decided anything is what #203 and #263 exist to undo. Any CURIE above is a curator's to accept or reject.", "curator": "edison_literature_identity", "llm_assisted": true, "timestamp": "2026-08-06T00:00:00+00:00"}, {"action": "PROMOTED_TO_MAPPED", "changes": "UNMAPPED_0447 -&gt; kgmicrobe.ingredient:mineral_solution_see_medium_no_976 (FALLBACK_REGISTRY). Minted under the #288 STOCK_SOLUTION convention: a MediaDive cross-reference to the mineral/trace-elements solution of DSMZ Medium 976. The corpus already treats this shape as a stock solution rather than retiring it \u2014 &#96;Trace element solution see Medium No. 187&#96; and &#96;Vitamin solution see Medium No. 403&#96; are both live kgmicrobe.ingredient mints under the #288 convention \u2014 so this follows its siblings. The composition is not transcribed here: it lives in the referenced medium, and #288's rule is to mint the named preparation rather than inline someone else's recipe.", "curator": "retire_assay_labels", "llm_assisted": false, "new_status": "MAPPED", "previous_status": "NEEDS_EXPERT", "timestamp": "2026-08-15T00:00:00+00:00"}, {"action": "ADDED_SYNONYMS", "changes": "Added 1 CultureMech recipe surface form(s) that folded onto this record's published label but were absent from MIM's label index, so CultureMech could not resolve them: 'Mineral solution (see Medium No. 976' (x1 CultureMech mentions). Source: culturemech:output/ingredient_occurrences.tsv.", "curator": "claude_culturemech_alias_backfill", "llm_assisted": false, "timestamp": "2026-08-30T04:48:06.233536+00:00"}], "identifier": "kgmicrobe.ingredient:mineral_solution_see_medium_no_976", "mapping": {"evidence": [{"evidence_type": "MANUAL_CURATION", "notes": "Minted under the #288 STOCK_SOLUTION convention: a MediaDive cross-reference to the mineral/trace-elements solution of DSMZ Medium 976. The corpus already treats this shape as a stock solution rather than retiring it \u2014 &#96;Trace element solution see Medium No. 187&#96; and &#96;Vitamin solution see Medium No. 403&#96; are both live kgmicrobe.ingredient mints under the #288 convention \u2014 so this follows its siblings. The composition is not transcribed here: it lives in the referenced medium, and #288's rule is to mint the named preparation rather than inline someone else's recipe.", "source": "MIM curation (#213/#308)"}], "mapping_quality": "FALLBACK_REGISTRY", "ontology_id": "kgmicrobe.ingredient:mineral_solution_see_medium_no_976", "ontology_label": "Mineral solution see Medium No. 976", "ontology_source": "kgmicrobe.ingredient"}} |
| ev-f25801a7e385fb14 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Mineral_Solution_See_Medium_No_976 | supports | [{"comment": "", "confidence": "0.9", "data_row": 1881, "mapping_date": "2026-08-30", "mapping_justification": "semapv:ManualMappingCuration", "object_id": "kgmicrobe.ingredient:mineral_solution_see_medium_no_976", "object_label": "Mineral solution see Medium No. 976", "object_source": "kgm:ingredient", "other": "Mineral solution (see Medium No. 976", "predicate_id": "skos:exactMatch", "source": "MIM:MIM curation (#213/#308)&#124;MIM:curator=claude_culturemech_alias_backfill", "subject_id": "MIM:Mineral_Solution_See_Medium_No_976", "subject_label": "Mineral solution see Medium No. 976", "validation_method": "manual:retire_assay_labels&#124;PROMOTED&#124;2026-08-15"}] |
| ev-5458c3c3defc38d0 | reports/yaml_record_review/Mineral_Solution_See_Medium_No_976.md; Complete historical report, including Verdict and Recommended Edits | context_only | Historical interpretation was read in full; it is not fresh source adjudication. |
| ev-a1a7bf32cb2806bb | reviews/structured/20261011T024636Z-mim-reconcile-all-batch-08/review.yaml; findings[finding_id=f-d3696f2daf45c433] | context_only | Exact earlier occurrence has open/confirmed status, based on exported-token presence and historical report text. |
| ev-5830b871d91efa8c | data/ingredients/mapped/Modified_Trace_Vitamins.yaml; identifier, ontology_mapping, synonyms and curation_history | partial | {"candidate_labels": [{"source": "culturemech:output/ingredient_occurrences.tsv", "synonym_text": "Modified trace vitamins (see below)", "synonym_type": "RAW_TEXT"}], "history": [{"action": "CREATED_AS_UNMAPPED", "changes": "Imported from mim-queue (source_id=mediadive.ingredient:2017); no CAS-RN or CHEBI/NCIT match. Curator review needed.", "curator": "audit_import_ingredients[mim-queue]", "llm_assisted": false, "new_status": "UNMAPPED", "timestamp": "2026-04-30T18:43:03.698454+00:00"}, {"action": "CLASSIFIED_STOCK_SOLUTION", "changes": "Classified as a modified trace vitamin stock mixture and left unmapped pending component list and formulation-specific curation.", "curator": "mediaingredientmech-agentic-curation", "llm_assisted": true, "new_status": "UNMAPPED", "previous_status": "UNMAPPED", "timestamp": "2026-05-11T08:03:00Z"}, {"action": "PROMOTED_TO_MAPPED", "changes": "Promoted UNMAPPED_0452 -&gt; kgmicrobe.ingredient:modified_trace_vitamins (FALLBACK_REGISTRY). A named multi-component preparation. Searched CHEBI, NCIT, MeSH, FOODON and ENVO by label and synonym: no term denotes it, and none could -- a preparation is not a substance. Takes the STOCK_SOLUTION convention: a kgmicrobe.ingredient: mint with no parent, because a multi-component mix does not narrow to any single compound (#288).", "curator": "issue_288_stock_solutions", "llm_assisted": true, "new_status": "MAPPED", "previous_status": "UNMAPPED", "timestamp": "2026-08-06T00:00:00+00:00"}, {"action": "CORRECTED", "changes": "occurrence_statistics 0/0 -&gt; 2/2 (media_count/total_occurrences), derived from distinct CultureMech recipe ids in the #337 occurrence table. The prior values came from the importer retired in #453, whose media_count counted a list truncated to 50 examples (#449). [source=ingredient_occurrences.tsv culturemech_rev=15a4da5c08 rows=194137 distinct_recipes=15257]", "curator": "refresh_occurrence_statistics", "timestamp": "2026-08-27T03:16:39.520286+00:00"}, {"action": "ADDED_SYNONYMS", "changes": "Added 1 CultureMech recipe surface form(s) that folded onto this record's published label but were absent from MIM's label index, so CultureMech could not resolve them: 'Modified trace vitamins (see below)' (x1 CultureMech mentions). Source: culturemech:output/ingredient_occurrences.tsv.", "curator": "claude_culturemech_alias_backfill", "llm_assisted": false, "timestamp": "2026-08-30T04:48:06.233536+00:00"}], "identifier": "kgmicrobe.ingredient:modified_trace_vitamins", "mapping": {"evidence": [{"evidence_type": "MANUAL_CURATION", "notes": "A named multi-component preparation. Searched CHEBI, NCIT, MeSH, FOODON and ENVO by label and synonym: no term denotes it, and none could -- a preparation is not a substance. Takes the STOCK_SOLUTION convention: a kgmicrobe.ingredient: mint with no parent, because a multi-component mix does not narrow to any single compound (#288).", "source": "MIM curation (#288)"}], "mapping_quality": "FALLBACK_REGISTRY", "ontology_id": "kgmicrobe.ingredient:modified_trace_vitamins", "ontology_label": "Modified trace vitamins", "ontology_source": "kgmicrobe.ingredient"}} |
| ev-7c6192e7f288bdf0 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Modified_Trace_Vitamins | supports | [{"comment": "", "confidence": "0.9", "data_row": 1903, "mapping_date": "2026-08-30", "mapping_justification": "semapv:ManualMappingCuration", "object_id": "kgmicrobe.ingredient:modified_trace_vitamins", "object_label": "Modified trace vitamins", "object_source": "kgm:ingredient", "other": "Modified trace vitamins (see below)", "predicate_id": "skos:exactMatch", "source": "MIM:MIM curation (#288)&#124;MIM:curator=claude_culturemech_alias_backfill", "subject_id": "MIM:Modified_Trace_Vitamins", "subject_label": "Modified trace vitamins", "validation_method": "none&#124;UNKNOWN_TERM&#124;2026-09-02"}] |
| ev-1659306e55f45a0b | reports/yaml_record_review/Modified_Trace_Vitamins.md; Complete historical report, including Verdict and Recommended Edits | context_only | Historical interpretation was read in full; it is not fresh source adjudication. |
| ev-54e6930eaaa55145 | reviews/structured/20261011T024637Z-mim-reconcile-all-batch-09/review.yaml; findings[finding_id=f-5982691d4b3d176b] | context_only | Exact earlier occurrence has open/confirmed status, based on exported-token presence and historical report text. |
| ev-0bdc1c0fd578d2ef | data/ingredients/mapped/Peptone.yaml; identifier, ontology_mapping, synonyms and curation_history | partial | {"candidate_labels": [{"source": "microbedecoder", "synonym_text": "Peptone (0.01 %", "synonym_type": "RAW_TEXT"}], "history": [{"action": "AUTO_CREATE_FROM_MICRO", "changes": "created with primary MICRO:0000178", "curator": "foodon_pass", "llm_assisted": false, "timestamp": "2026-05-01T19:55:09.679469+00:00"}, {"action": "AUTO_CLASSIFY_INGREDIENT_TYPE", "changes": "set ingredient_type=UNDEFINED_MIXTURE (name matches complex pattern 'Peptone')", "curator": "auto_classify_ingredient_type", "llm_assisted": false, "timestamp": "2026-05-02T03:12:17.686332+00:00"}, {"action": "ANNOTATED", "changes": "Added media role: PROTEIN_SOURCE (confidence: 0.80)", "curator": "infer_roles_from_name_lists", "timestamp": "2026-06-03T02:06:01.747135+00:00"}, {"action": "CORRECTED", "changes": "Backfilled missing occurrence_statistics (0/0): ontology-derived record with no tracked media occurrences.", "curator": "audit_occurrence_stats", "timestamp": "2026-06-08T23:23:58.335580+00:00"}, {"action": "ANNOTATED", "changes": "Migrated legacy media_roles to role facets (#128): PROTEIN_SOURCE -&gt; nutritional_roles.PROTEIN_SOURCE", "curator": "migrate_media_roles_to_facets", "timestamp": "2026-07-20T00:00:00+00:00"}, {"action": "MERGED_FROM_UNMAPPED_DUPLICATE", "changes": "Absorbed UNMAPPED_0718 'Peptones' as a RAW_TEXT synonym -- plural of the already-mapped peptone record. No new SSSOM row; MICRO:0000178 is already mapped. Source: kgmicrobe.compound:peptones.", "curator": "microbedecoder-residual-dispositions", "llm_assisted": true, "timestamp": "2026-08-05T00:01:30.894952+00:00"}, {"action": "MERGED_FROM_UNMAPPED_DUPLICATE", "changes": "Absorbed UNMAPPED_0835 'Peptone (0.01 %' as a RAW_TEXT synonym -- concentration-truncated duplicate of peptone. No new SSSOM row; MICRO:0000178 is already mapped. Source: kgmicrobe.trait:peptone_0_01.", "curator": "microbedecoder-residual-dispositions", "llm_assisted": true, "timestamp": "2026-08-05T00:01:30.894952+00:00"}, {"action": "CORRECTED", "changes": "occurrence_statistics 0/0 -&gt; 2251/2255 (media_count/total_occurrences), derived from distinct CultureMech recipe ids in the #337 occurrence table. The prior values came from the importer retired in #453, whose media_count counted a list truncated to 50 examples (#449). [source=ingredient_occurrences.tsv culturemech_rev=15a4da5c08 rows=194137 distinct_recipes=15257]", "curator": "refresh_occurrence_statistics", "timestamp": "2026-08-27T03:16:39.519680+00:00"}], "identifier": "MICRO:0000178", "mapping": {"evidence": [{"evidence_type": "DATABASE_MATCH", "notes": "Auto-created from foodon_pass; label-exact (micro)", "source": "MICRO via OLS search"}], "mapping_quality": "EXACT_MATCH", "ontology_id": "MICRO:0000178", "ontology_label": "peptone", "ontology_source": "MICRO"}} |
| ev-a926e5411d840793 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Peptone | supports | [{"comment": "", "confidence": "0.99", "data_row": 2220, "mapping_date": "2026-08-27", "mapping_justification": "semapv:LexicalMatching", "object_id": "MICRO:0000178", "object_label": "peptone", "object_source": "obo:micro.owl", "other": "Peptones&#124;Peptone (0.01 %", "predicate_id": "skos:exactMatch", "source": "MIM:MICRO via OLS search&#124;MIM:curator=refresh_occurrence_statistics", "subject_id": "MIM:Peptone", "subject_label": "Peptone", "validation_method": "none&#124;UNKNOWN_TERM&#124;2026-07-07"}] |
| ev-f56ebea344bcd264 | reports/yaml_record_review/Peptone.md; Complete historical report, including Verdict and Recommended Edits | context_only | Historical interpretation was read in full; it is not fresh source adjudication. |
| ev-8bb59eaf8b6e66f4 | reviews/structured/20261011T024638Z-mim-reconcile-all-batch-10/review.yaml; findings[finding_id=f-f582ea830b4f370d] | context_only | Exact earlier occurrence has open/confirmed status, based on exported-token presence and historical report text. |
| ev-745bc0e8e18adc16 | data/ingredients/mapped/Potassium_Phosphate_Buffer.yaml; identifier, ontology_mapping, synonyms and curation_history | partial | {"candidate_labels": [{"source": "culturemech:output/ingredient_occurrences.tsv", "synonym_text": "Potassium phosphate buffer* (see below)", "synonym_type": "RAW_TEXT"}], "history": [{"action": "CREATED_AS_UNMAPPED", "changes": "Imported from CultureBotHT (consolidated_media.json (media-only)). Used in 2 CultureBot media; samples: Mega, TYG. No CAS-RN or CHEBI mapping available; curator review needed.", "curator": "audit_add_remaining_culturebotht", "llm_assisted": false, "new_status": "UNMAPPED", "timestamp": "2026-04-29T06:51:33.117170+00:00"}, {"action": "AUTO_CLASSIFY_INGREDIENT_TYPE", "changes": "set ingredient_type=STOCK_SOLUTION (name matches solution pattern 'phosphate buffer')", "curator": "auto_classify_ingredient_type", "llm_assisted": false, "timestamp": "2026-05-02T03:12:19.854401+00:00"}, {"action": "AUTO_UPGRADE_TO_NCIT", "changes": "primary UNMAPPED_0274 \u2192 NCIT:C29321 (strategy=stem-match)", "curator": "resolve_unmapped_v2", "llm_assisted": false, "timestamp": "2026-05-02T03:18:21.960132+00:00"}, {"action": "CORRECTED", "changes": "Changed identifier from NCIT:C29321 to kgmicrobe.ingredient:potassium_phosphate_buffer and retained NCIT:C29321 only as CLOSE_MATCH. Potassium phosphate buffer is a formulation variant, not identical to the generic phosphate buffer class.", "curator": "ingredient_mapping_review_2026_05_05", "llm_assisted": false, "new_status": "MAPPED", "previous_status": "MAPPED", "timestamp": "2026-05-05T00:00:00+00:00"}, {"action": "ANNOTATED", "changes": "Added media role: BUFFER (confidence: 0.80)", "curator": "infer_roles_from_name_lists", "timestamp": "2026-06-03T02:06:01.748066+00:00"}, {"action": "ANNOTATED", "changes": "Migrated legacy media_roles to role facets (#128): BUFFER -&gt; physicochemical_roles.BUFFER", "curator": "migrate_media_roles_to_facets", "timestamp": "2026-07-20T00:00:00+00:00"}, {"action": "CORRECTED", "changes": "occurrence_statistics 2/2 -&gt; 44/44 (media_count/total_occurrences), derived from distinct CultureMech recipe ids in the #337 occurrence table. The prior values came from the importer retired in #453, whose media_count counted a list truncated to 50 examples (#449). [source=ingredient_occurrences.tsv culturemech_rev=15a4da5c08 rows=194137 distinct_recipes=15257]", "curator": "refresh_occurrence_statistics", "timestamp": "2026-08-27T03:16:39.519736+00:00"}, {"action": "ADDED_SYNONYMS", "changes": "Added 4 CultureMech recipe surface form(s) that folded onto this record's published label but were absent from MIM's label index, so CultureMech could not resolve them: 'Potassium phosphate buffer (0.01 M, pH 7.2)' (x1 CultureMech mentions); 'Potassium phosphate buffer (0.02 M, pH 7.0)' (x1 CultureMech mentions); 'Potassium phosphate buffer (1 M, pH 7.1)' (x1 CultureMech mentions); 'Potassium phosphate buffer* (see below)' (x1 CultureMech mentions). Source: culturemech:output/ingredient_occurrences.tsv.", "curator": "claude_culturemech_alias_backfill", "llm_assisted": false, "timestamp": "2026-08-30T04:48:06.233536+00:00"}], "identifier": "kgmicrobe.ingredient:potassium_phosphate_buffer", "mapping": {"evidence": [{"evidence_type": "CURATOR_JUDGMENT", "notes": "Potassium phosphate buffer is a formulation variant, not identical to the generic phosphate buffer class.", "source": "ingredient_mapping_review_2026-05-05"}], "mapping_quality": "CLOSE_MATCH", "ontology_id": "NCIT:C29321", "ontology_label": "Phosphate Buffer", "ontology_source": "NCIT"}} |
| ev-7d01fe3478491965 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Potassium_Phosphate_Buffer | supports | [{"comment": "", "confidence": "0.9", "data_row": 2327, "mapping_date": "2026-08-30", "mapping_justification": "semapv:ManualMappingCuration", "object_id": "NCIT:C29321", "object_label": "Phosphate Buffer", "object_source": "obo:ncit.owl", "other": "Potassium phosphate buffer (0.01 M, pH 7.2)&#124;Potassium phosphate buffer (0.02 M, pH 7.0)&#124;Potassium phosphate buffer (1 M, pH 7.1)&#124;Potassium phosphate buffer* (see below)", "predicate_id": "skos:closeMatch", "source": "MIM:ingredient_mapping_review_2026-05-05&#124;MIM:curator=claude_culturemech_alias_backfill", "subject_id": "MIM:Potassium_Phosphate_Buffer", "subject_label": "Potassium phosphate buffer", "validation_method": "none&#124;UNKNOWN_TERM&#124;2026-07-07"}, {"comment": "Registry/identity row preserving kgmicrobe.ingredient:potassium_phosphate_buffer alongside parent NCIT:C29321.", "confidence": "0.99", "data_row": 2328, "mapping_date": "2026-08-30", "mapping_justification": "semapv:ManualMappingCuration", "object_id": "kgmicrobe.ingredient:potassium_phosphate_buffer", "object_label": "Potassium phosphate buffer", "object_source": "kgm:ingredient", "other": "", "predicate_id": "skos:exactMatch", "source": "MIM:ingredient_mapping_review_2026-05-05&#124;MIM:curator=claude_culturemech_alias_backfill", "subject_id": "MIM:Potassium_Phosphate_Buffer", "subject_label": "Potassium phosphate buffer", "validation_method": "none&#124;UNKNOWN_TERM&#124;2026-07-07"}] |
| ev-a692d3e165ce1613 | reports/yaml_record_review/Potassium_Phosphate_Buffer.md; Complete historical report, including Verdict and Recommended Edits | context_only | Historical interpretation was read in full; it is not fresh source adjudication. |
| ev-032b61a7a21ed47b | reviews/structured/20261011T024638Z-mim-reconcile-all-batch-10/review.yaml; findings[finding_id=f-b7808e84d7886285] | context_only | Exact earlier occurrence has open/confirmed status, based on exported-token presence and historical report text. |
| ev-d59510b4ad4c4456 | data/ingredients/mapped/Riboflavin.yaml; identifier, ontology_mapping, synonyms and curation_history | partial | {"candidate_labels": [{"source": "culturemech:output/ingredient_occurrences.tsv", "synonym_text": "Riboflavin (see below)", "synonym_type": "RAW_TEXT"}], "history": [{"action": "IMPORTED", "changes": "Initial import from CultureMech pipeline", "curator": "import_from_culturemech", "llm_assisted": false, "new_status": "MAPPED", "timestamp": "2026-03-09T06:54:18.022301+00:00"}, {"action": "ADDED_CAS_RN", "changes": "Added CAS-RN:83-88-5 from PubChem API via name lookup (Riboflavin)", "curator": "fetch_cas_rn_from_pubchem", "llm_assisted": false, "new_status": "MAPPED", "timestamp": "2026-04-05T19:53:48.746601+00:00"}, {"action": "ADDED_CAS_RN", "changes": "Added CAS-RN:83-88-5 from CultureBotHT compounds_to_cas.csv (matched: riboflavin)", "curator": "fetch_cas_rn_from_culturebot_csv", "llm_assisted": false, "new_status": "MAPPED", "timestamp": "2026-04-05T21:48:45.703391+00:00"}, {"action": "CAS_RN_ADDED", "changes": "Added CAS-RN 83-88-5 from PubChem (via CHEBI:17015)", "curator": "enrich_mim_cas_rn_batch", "llm_assisted": false, "new_status": "MAPPED", "timestamp": "2026-04-09T00:32:50.689620+00:00"}, {"action": "ADDED_SYNONYMS", "changes": "Added 20 synonyms from kg-microbe P4.4 enrichment: 1-deoxy-1-(7,8-dimethyl-2,4-dioxo-3,4-dihydrobenzo[g]pteridin-10(2H)-yl)-D-ribitol, 1-deoxy-1-(7,8-dimethyl-2,4-dioxo-3,4-dihydrobenzo[g]pteridin-10(2H)-yl)pentitol, 5-deoxy-5-(7,8-dimethyl-2,4-dioxo-3,4-dihydrobenzo[g]pteridin-10(2H)-yl)-D-ribitol, 6,7-dimethyl-9-D-ribitylisoalloxazine, 7,8-dimethyl-10-(D-ribo-2,3,4,5-tetrahydroxypentyl)benzo[g]pteridine-2,4(3H,10H)-dione, ... (15 more)", "curator": "cbclaw_kg_microbe_sweep", "llm_assisted": true, "new_status": "MAPPED", "timestamp": "2026-04-18T00:00:00+00:00"}, {"action": "MERGED_FROM_DUPLICATES", "changes": "Absorbed 2 duplicate MIM record(s) into this one: Riboflavine.yaml, Riboflavin_2.yaml. Synonyms, curation_history, and occurrence counts were unioned/summed; winner selected by highest occurrence count with preferred_term readability tie-break.", "curator": "audit_mim_merge", "llm_assisted": false, "new_status": "MAPPED", "timestamp": "2026-04-19T07:39:23.955331+00:00"}, {"action": "AUTO_CLASSIFY_INGREDIENT_TYPE", "changes": "set ingredient_type=SINGLE_INGREDIENT (CHEBI primary)", "curator": "auto_classify_ingredient_type", "llm_assisted": false, "timestamp": "2026-05-01T07:35:36.069178+00:00"}, {"action": "AUTO_BACKFILL_CHEBI_CHEMISTRY", "changes": "molecular_formula=C17H20N4O6; inchi=InChI=1S/C17H20N4O6/c1-7-3-9-10(4-8(7)2)21(5-11(23; smiles=Cc1cc2nc3c(=O)nc(=O)nc-3n(C[C@H](O)[C@H](O)[C@H](O", "curator": "auto_classify_ingredient_type", "llm_assisted": false, "timestamp": "2026-05-01T08:08:32.160107+00:00"}, {"action": "APPLY_EVIDENCE_PROPOSAL", "changes": "added pmid=40609532 from propose-evidence batch", "curator": "auto_classify_ingredient_type", "llm_assisted": false, "timestamp": "2026-05-01T08:09:48.123437+00:00"}, {"action": "AUTO_CLASSIFY_INGREDIENT_TYPE", "changes": "set ingredient_type=SINGLE_INGREDIENT (chemical structure populated (molecular_formula))", "curator": "auto_classify_ingredient_type", "llm_assisted": false, "timestamp": "2026-05-02T03:12:18.114359+00:00"}, {"action": "ANNOTATED", "changes": "Added media role: VITAMIN_SOURCE (confidence: 1.00)", "curator": "extract_roles_from_synonyms", "timestamp": "2026-05-29T23:35:36.112742+00:00"}, {"action": "CORRECTED", "changes": "ontology_label 'Riboflavin' -&gt; 'riboflavin': synced to canonical CHEBI label (preferred_term 'Riboflavin' unchanged).", "curator": "correct_stale_ontology_labels.py", "timestamp": "2026-06-09T05:23:46.827070+00:00"}, {"action": "ANNOTATED", "changes": "Migrated legacy media_roles to role facets (#128): VITAMIN_SOURCE -&gt; nutritional_roles.VITAMIN_SOURCE", "curator": "migrate_media_roles_to_facets", "timestamp": "2026-07-20T00:00:00+00:00"}, {"action": "CORRECTED", "changes": "occurrence_statistics 85/1837 -&gt; 2122/2123 (media_count/total_occurrences), derived from distinct CultureMech recipe ids in the #337 occurrence table. The prior values came from the importer retired in #453, whose media_count counted a list truncated to 50 examples (#449). [source=ingredient_occurrences.tsv culturemech_rev=15a4da5c08 rows=194137 distinct_recipes=15257]", "curator": "refresh_occurrence_statistics", "timestamp": "2026-08-27T03:16:39.519802+00:00"}, {"action": "ADDED_SYNONYMS", "changes": "Added 4 CultureMech recipe surface form(s) that folded onto this record's published label but were absent from MIM's label index, so CultureMech could not resolve them: 'Riboflavin (Vitamine B2)' (x4 CultureMech mentions); 'Riboflavin (Vitamin B2)' (x2 CultureMech mentions); 'Riboflavin (0.2 mg/ml)' (x1 CultureMech mentions); 'Riboflavin (see below)' (x1 CultureMech mentions). Source: culturemech:output/ingredient_occurrences.tsv.", "curator": "claude_culturemech_alias_backfill", "llm_assisted": false, "timestamp": "2026-08-30T04:48:06.233536+00:00"}, {"action": "ADDED_SYNONYMS", "changes": "Added 1 CultureMech recipe surface form(s) that folded onto this record's published label but were absent from MIM's label index, so CultureMech could not resolve them: 'Riboflavin (0.05 \u03bcg/mL)' (x1 CultureMech mentions). Source: culturemech:output/ingredient_occurrences.tsv.", "curator": "claude_culturemech_alias_backfill", "llm_assisted": false, "timestamp": "2026-08-31T23:56:54.854807+00:00"}], "identifier": "CHEBI:17015", "mapping": {"evidence": [{"evidence_type": "DATABASE_MATCH", "notes": "Imported from CultureMech pipeline, quality=DIRECT_MATCH", "source": "CultureMech"}, {"evidence_type": "LITERATURE", "explanation": "Auto-proposed; curator should rephrase or remove.", "pmid": "40609532", "snippet": "We found that the abundance of Bacteroides cellulosilyticus affects tumor heterogeneity by producing riboflavin that inhibits CERS3 activity, thus delaying CRC progression.", "source": "PubMed search ('Riboflavin')", "supports": "SUPPORT"}], "mapping_quality": "EXACT_MATCH", "ontology_id": "CHEBI:17015", "ontology_label": "riboflavin", "ontology_source": "CHEBI"}} |
| ev-1dfdb8319038a4fb | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Riboflavin | supports | [{"comment": "ENRICH_SYNONYM: kg-microbe is 'riboflavin' plus qualifier ('(1-)')", "confidence": "0.95", "data_row": 2429, "mapping_date": "2026-08-31", "mapping_justification": "semapv:LexicalMatching", "object_id": "CHEBI:17015", "object_label": "riboflavin", "object_source": "obo:chebi.owl", "other": "1-deoxy-1-(7,8-dimethyl-2,4-dioxo-3,4-dihydrobenzo[g]pteridin-10(2H)-yl)-D-ribitol&#124;1-deoxy-1-(7,8-dimethyl-2,4-dioxo-3,4-dihydrobenzo[g]pteridin-10(2H)-yl)pentitol&#124;5-deoxy-5-(7,8-dimethyl-2,4-dioxo-3,4-dihydrobenzo[g]pteridin-10(2H)-yl)-D-ribitol&#124;6,7-dimethyl-9-D-ribitylisoalloxazine&#124;7,8-dimethyl-10-(D-ribo-2,3,4,5-tetrahydroxypentyl)benzo[g]pteridine-2,4(3H,10H)-dione&#124;7,8-dimethyl-10-(D-ribo-2,3,4,5-tetrahydroxypentyl)isoalloxazine&#124;7,8-dimethyl-10-[(2S,3S,4R)-2,3,4,5-tetrahydroxypentyl]benzo[g]pteridine-2,4(3H,10H)-dione&#124;7,8-dimethyl-10-ribitylisoalloxazine&#124;Aqua-Flave&#124;Beflavin&#124;Beflavine&#124;Bisulase&#124;Dermadram&#124;E101&#124;Fiboflavin&#124;Flavaxin&#124;Flavin Bb&#124;Flaxain&#124;Hyflavin&#124;Riboflavine&#124;Riboflavine (B2)&#124;Riboflavin (Vitamine B2)&#124;Riboflavin (Vitamin B2)&#124;Riboflavin (0.2 mg/ml)&#124;Riboflavin (see below)&#124;Riboflavin (0.05 \u03bcg/mL)&#124;CAS:83-88-5", "predicate_id": "skos:exactMatch", "source": "MIM:CultureMech&#124;MIM:PubMed search ('Riboflavin')&#124;MIM:curator=claude_culturemech_alias_backfill&#124;kgm:chebi_xrefs&#124;kgm:culturebotai_reviewed&#124;kgm:mediadive_compounds&#124;kgm:mediaingredientmech_reviewed&#124;kgm:mediaingredientmech_reviewed[curator=audit_mim_merge]&#124;kgm:mediaingredientmech_reviewed[curator=auto_classify_ingredient_type]&#124;kgm:mediaingredientmech_reviewed[curator=correct_stale_ontology_labels.py]&#124;kgm:mediaingredientmech_reviewed[curator=migrate_media_roles_to_facets]&#124;kgm:primary_mappings[kegg_compound]", "subject_id": "MIM:Riboflavin", "subject_label": "Riboflavin", "validation_method": "OAK+OLS:chebi&#124;SYNONYM_ENRICH&#124;2026-07-07"}] |
| ev-a809b48a4c5a84c5 | reports/yaml_record_review/Riboflavin.md; Complete historical report, including Verdict and Recommended Edits | context_only | Historical interpretation was read in full; it is not fresh source adjudication. |
| ev-6c06e714e86355c6 | reviews/structured/20261011T024638Z-mim-reconcile-all-batch-11/review.yaml; findings[finding_id=f-2680803ffb7b7f40] | context_only | Exact earlier occurrence has open/confirmed status, based on exported-token presence and historical report text. |
| ev-b62c98e3d0a1e1d5 | data/ingredients/mapped/Sludge_fluid.yaml; identifier, ontology_mapping, synonyms and curation_history | partial | {"candidate_labels": [{"source": "culturemech:output/ingredient_occurrences.tsv", "synonym_text": "Sludge fluid (see below)", "synonym_type": "RAW_TEXT"}], "history": [{"action": "CREATED_FROM_CULTUREMECH_RESIDUAL", "changes": "Created from a CultureMech recipe ingredient MIM held no record for (2 mentions across 2 recipes). Grounded to MICRO:0000521 ('sludge fluid') on an exact match of the canonical label to the query 'Sludge fluid'. Source: culturemech:output/ingredient_occurrences.tsv.", "curator": "claude_culturemech_residual_grounding", "llm_assisted": false, "new_status": "MAPPED", "timestamp": "2026-08-30T10:35:03.361102+00:00"}, {"action": "ADDED_SYNONYMS", "changes": "Added 1 CultureMech recipe surface form(s) that folded onto this record's published label but were absent from MIM's label index, so CultureMech could not resolve them: 'Sludge fluid (see below)' (x1 CultureMech mentions). Source: culturemech:output/ingredient_occurrences.tsv.", "curator": "claude_culturemech_alias_backfill", "llm_assisted": false, "timestamp": "2026-08-30T10:41:26.546472+00:00"}, {"action": "CORRECTED", "changes": "Added ontology_mapping.evidence recording the CultureMech occurrence table as the source of this grounding. The provenance was already in this record's CREATED_FROM_CULTUREMECH_RESIDUAL history entry but absent from the structured field the SSSOM builder reads, so a rebuild dropped MIM:culturemech:output/ingredient_occurrences.tsv from the published row (#541).", "curator": "claude_restore_culturemech_evidence", "llm_assisted": false, "timestamp": "2026-09-06T07:34:56.956907+00:00"}], "identifier": "MICRO:0000521", "mapping": {"evidence": [{"evidence_type": "LEXICAL_MATCH", "notes": "Surface form appears in CultureMech's occurrence table and was grounded to MICRO:0000521 on an exact match against the ontology label. Restored from the record's own creation history (#541); the residual importer wrote this provenance only into the published SSSOM.", "source": "culturemech:output/ingredient_occurrences.tsv"}], "mapping_quality": "EXACT_MATCH", "match_level": "EXACT", "ontology_id": "MICRO:0000521", "ontology_label": "sludge fluid", "ontology_source": "MICRO"}} |
| ev-d4f1e238a85e0e57 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Sludge_fluid | supports | [{"comment": "", "confidence": "0.99", "data_row": 2521, "mapping_date": "2026-09-06", "mapping_justification": "semapv:LexicalMatching", "object_id": "MICRO:0000521", "object_label": "sludge fluid", "object_source": "obo:micro.owl", "other": "Sludge fluid (see below)", "predicate_id": "skos:exactMatch", "source": "MIM:culturemech:output/ingredient_occurrences.tsv&#124;MIM:curator=claude_restore_culturemech_evidence", "subject_id": "MIM:Sludge_fluid", "subject_label": "Sludge fluid", "validation_method": "manual:claude_culturemech_residual_grounding&#124;CREATED&#124;2026-08-30"}] |
| ev-de40a4caf98a1085 | reports/yaml_record_review/Sludge_fluid.md; Complete historical report, including Verdict and Recommended Edits | context_only | Historical interpretation was read in full; it is not fresh source adjudication. |
| ev-4f670ddc934d5e74 | reviews/structured/20261011T024638Z-mim-reconcile-all-batch-11/review.yaml; findings[finding_id=f-ef4889c5708c1269] | context_only | Exact earlier occurrence has open/confirmed status, based on exported-token presence and historical report text. |
| ev-927f64381fa816f2 | data/ingredients/mapped/Soil_Extract.yaml; identifier, ontology_mapping, synonyms and curation_history | partial | {"candidate_labels": [{"source": "culturemech:output/ingredient_occurrences.tsv", "synonym_text": "Soil extract (see below)", "synonym_type": "RAW_TEXT"}], "history": [{"action": "CREATED_AS_UNMAPPED", "changes": "Imported from mim-queue (source_id=mediadive.ingredient:180); no CAS-RN or CHEBI/NCIT match. Curator review needed.", "curator": "audit_import_ingredients[mim-queue]", "llm_assisted": false, "new_status": "UNMAPPED", "timestamp": "2026-04-30T18:43:03.698454+00:00"}, {"action": "AUTO_UPGRADE_TO_MICRO", "changes": "primary UNMAPPED_0529 \u2192 MICRO:0000457 (label-exact)", "curator": "auto_classify_ingredient_type", "llm_assisted": false, "timestamp": "2026-05-01T19:50:45.145149+00:00"}, {"action": "AUTO_CLASSIFY_INGREDIENT_TYPE", "changes": "set ingredient_type=UNDEFINED_MIXTURE (name matches complex pattern 'Soil')", "curator": "auto_classify_ingredient_type", "llm_assisted": false, "timestamp": "2026-05-02T03:12:18.544149+00:00"}, {"action": "ANNOTATED", "changes": "Added 1 environmental_context entries (issue #1, Phase 3 initial pass).", "curator": "env_context_phase3_initial", "timestamp": "2026-05-24T04:03:54.899342+00:00"}, {"action": "CORRECTED", "changes": "occurrence_statistics 0/0 -&gt; 17/17 (media_count/total_occurrences), derived from distinct CultureMech recipe ids in the #337 occurrence table. The prior values came from the importer retired in #453, whose media_count counted a list truncated to 50 examples (#449). [source=ingredient_occurrences.tsv culturemech_rev=15a4da5c08 rows=194137 distinct_recipes=15257]", "curator": "refresh_occurrence_statistics", "timestamp": "2026-08-27T03:16:39.519889+00:00"}, {"action": "ADDED_SYNONYMS", "changes": "Added 2 CultureMech recipe surface form(s) that folded onto this record's published label but were absent from MIM's label index, so CultureMech could not resolve them: 'Soil extract (see below)' (x3 CultureMech mentions); 'Soil extract (SE1)' (x1 CultureMech mentions). Source: culturemech:output/ingredient_occurrences.tsv.", "curator": "claude_culturemech_alias_backfill", "llm_assisted": false, "timestamp": "2026-08-30T04:48:06.233536+00:00"}], "identifier": "MICRO:0000457", "mapping": {"evidence": [{"evidence_type": "DATABASE_MATCH", "notes": "Auto-upgraded from 'UNMAPPED_0529'; match=label-exact", "source": "MICRO via OLS search"}], "mapping_quality": "EXACT_MATCH", "ontology_id": "MICRO:0000457", "ontology_label": "soil extract", "ontology_source": "MICRO"}} |
| ev-1edf0a1870e81e81 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Soil_Extract | supports | [{"comment": "", "confidence": "0.99", "data_row": 2615, "mapping_date": "2026-08-30", "mapping_justification": "semapv:LexicalMatching", "object_id": "MICRO:0000457", "object_label": "soil extract", "object_source": "obo:micro.owl", "other": "Soil extract (see below)&#124;Soil extract (SE1)", "predicate_id": "skos:exactMatch", "source": "MIM:MICRO via OLS search&#124;MIM:curator=claude_culturemech_alias_backfill", "subject_id": "MIM:Soil_Extract", "subject_label": "Soil extract", "validation_method": "none&#124;UNKNOWN_TERM&#124;2026-07-07"}] |
| ev-cefe2423553074dc | reports/yaml_record_review/Soil_Extract.md; Complete historical report, including Verdict and Recommended Edits | context_only | Historical interpretation was read in full; it is not fresh source adjudication. |
| ev-61509143d0ecf84a | reviews/structured/20261011T024638Z-mim-reconcile-all-batch-11/review.yaml; findings[finding_id=f-3b7b7b7cd4c70ace] | context_only | Exact earlier occurrence has open/confirmed status, based on exported-token presence and historical report text. |
| ev-cb42f25983a0ad30 | data/ingredients/mapped/Trace_Element_Solution_See_Medium_No_187.yaml; identifier, ontology_mapping, synonyms and curation_history | partial | {"candidate_labels": [{"source": "culturemech:output/ingredient_occurrences.tsv", "synonym_text": "Trace element solution (see Medium No. 187", "synonym_type": "RAW_TEXT"}], "history": [{"action": "CREATED_AS_UNMAPPED", "changes": "Imported from mim-queue (source_id=mediadive.ingredient:1886); no CAS-RN or CHEBI/NCIT match. Curator review needed.", "curator": "audit_import_ingredients[mim-queue]", "llm_assisted": false, "new_status": "UNMAPPED", "timestamp": "2026-04-30T18:43:03.698454+00:00"}, {"action": "CLASSIFY_AS_STOCK_SOLUTION", "changes": "name pattern 'see Medium No.' indicates pre-mixed defined solution", "curator": "auto_classify_stock_solution", "llm_assisted": false, "timestamp": "2026-05-01T19:58:06.857978+00:00"}, {"action": "AUTO_CLASSIFY_INGREDIENT_TYPE", "changes": "set ingredient_type=STOCK_SOLUTION (name matches solution pattern 'Trace element')", "curator": "auto_classify_ingredient_type", "llm_assisted": false, "timestamp": "2026-05-02T03:12:19.961419+00:00"}, {"action": "AUTO_UPGRADE_TO_NCIT", "changes": "primary UNMAPPED_0549 \u2192 NCIT:C896 (strategy=stem-match)", "curator": "resolve_unmapped_v2", "llm_assisted": false, "timestamp": "2026-05-02T03:18:21.989902+00:00"}, {"action": "CORRECTED", "changes": "Changed identifier from NCIT:C896 to kgmicrobe.ingredient:trace_element_solution_see_medium_no_187 and retained NCIT:C896 only as CLOSE_MATCH. Named trace element solution is a formulation, not identical to the generic trace element class.", "curator": "ingredient_mapping_review_2026_05_05", "llm_assisted": false, "new_status": "MAPPED", "previous_status": "MAPPED", "timestamp": "2026-05-05T00:00:00+00:00"}, {"action": "ADDED_SYNONYMS", "changes": "Added 1 CultureMech recipe surface form(s) that folded onto this record's published label but were absent from MIM's label index, so CultureMech could not resolve them: 'Trace element solution (see Medium No. 187' (x1 CultureMech mentions). Source: culturemech:output/ingredient_occurrences.tsv.", "curator": "claude_culturemech_alias_backfill", "llm_assisted": false, "timestamp": "2026-08-30T04:48:06.233536+00:00"}], "identifier": "kgmicrobe.ingredient:trace_element_solution_see_medium_no_187", "mapping": {"evidence": [{"evidence_type": "CURATOR_JUDGMENT", "notes": "Named trace element solution is a formulation, not identical to the generic trace element class.", "source": "ingredient_mapping_review_2026-05-05"}], "mapping_quality": "CLOSE_MATCH", "ontology_id": "NCIT:C896", "ontology_label": "Trace Element", "ontology_source": "NCIT"}} |
| ev-775e49cc5333c85a | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Trace_Element_Solution_See_Medium_No_187 | supports | [{"comment": "", "confidence": "0.9", "data_row": 2802, "mapping_date": "2026-08-30", "mapping_justification": "semapv:ManualMappingCuration", "object_id": "NCIT:C896", "object_label": "Trace Element", "object_source": "obo:ncit.owl", "other": "Trace element solution (see Medium No. 187", "predicate_id": "skos:closeMatch", "source": "MIM:ingredient_mapping_review_2026-05-05&#124;MIM:curator=claude_culturemech_alias_backfill", "subject_id": "MIM:Trace_Element_Solution_See_Medium_No_187", "subject_label": "Trace element solution see Medium No. 187", "validation_method": "none&#124;UNKNOWN_TERM&#124;2026-07-07"}, {"comment": "Registry/identity row preserving kgmicrobe.ingredient:trace_element_solution_see_medium_no_187 alongside parent NCIT:C896.", "confidence": "0.99", "data_row": 2803, "mapping_date": "2026-08-30", "mapping_justification": "semapv:ManualMappingCuration", "object_id": "kgmicrobe.ingredient:trace_element_solution_see_medium_no_187", "object_label": "Trace element solution see Medium No. 187", "object_source": "kgm:ingredient", "other": "", "predicate_id": "skos:exactMatch", "source": "MIM:ingredient_mapping_review_2026-05-05&#124;MIM:curator=claude_culturemech_alias_backfill", "subject_id": "MIM:Trace_Element_Solution_See_Medium_No_187", "subject_label": "Trace element solution see Medium No. 187", "validation_method": "none&#124;UNKNOWN_TERM&#124;2026-07-07"}] |
| ev-a18de57ffdc5d750 | reports/yaml_record_review/Trace_Element_Solution_See_Medium_No_187.md; Complete historical report, including Verdict and Recommended Edits | context_only | Historical interpretation was read in full; it is not fresh source adjudication. |
| ev-666a0e05df6eee3c | reviews/structured/20261011T024638Z-mim-reconcile-all-batch-11/review.yaml; findings[finding_id=f-612aa67bad26d26a] | context_only | Exact earlier occurrence has open/confirmed status, based on exported-token presence and historical report text. |
| ev-995ddb5e1dd7c309 | data/ingredients/mapped/Trace_Metal_Mix_A5.yaml; identifier, ontology_mapping, synonyms and curation_history | partial | {"candidate_labels": [{"source": "culturemech:output/ingredient_occurrences.tsv", "synonym_text": "Trace Metal Mix A5 (see below)", "synonym_type": "RAW_TEXT"}], "history": [{"action": "CREATED_AS_UNMAPPED", "changes": "Imported from CultureBotHT (consolidated_media.json (media-only)). Used in 7 CultureBot media; samples: BG11C, BG11, BG11R\u2026. No CAS-RN or CHEBI mapping available; curator review needed.", "curator": "audit_add_remaining_culturebotht", "llm_assisted": false, "new_status": "UNMAPPED", "timestamp": "2026-04-29T06:51:33.117170+00:00"}, {"action": "AUTO_UPGRADE_TO_MICRO", "changes": "primary UNMAPPED_0258 \u2192 MICRO:0001349 via name normalization to 'Trace metal mix A5'", "curator": "resolve_unmapped", "llm_assisted": false, "timestamp": "2026-05-02T00:41:18.463553+00:00"}, {"action": "AUTO_CLASSIFY_INGREDIENT_TYPE", "changes": "set ingredient_type=STOCK_SOLUTION (name matches solution pattern 'Trace metal')", "curator": "auto_classify_ingredient_type", "llm_assisted": false, "timestamp": "2026-05-02T03:12:18.924925+00:00"}, {"action": "ANNOTATED", "changes": "Added media role: TRACE_ELEMENT (confidence: 0.60)", "curator": "claude_in_session_curation", "timestamp": "2026-06-09T04:56:30.248262+00:00"}, {"action": "ANNOTATED", "changes": "Migrated legacy media_roles to role facets (#128): TRACE_ELEMENT -&gt; nutritional_roles.TRACE_ELEMENT", "curator": "migrate_media_roles_to_facets", "timestamp": "2026-07-20T00:00:00+00:00"}, {"action": "CORRECTED", "changes": "occurrence_statistics 7/7 -&gt; 2/2 (media_count/total_occurrences), derived from distinct CultureMech recipe ids in the #337 occurrence table. The prior values came from the importer retired in #453, whose media_count counted a list truncated to 50 examples (#449). [source=ingredient_occurrences.tsv culturemech_rev=15a4da5c08 rows=194137 distinct_recipes=15257]", "curator": "refresh_occurrence_statistics", "timestamp": "2026-08-27T03:16:39.519991+00:00"}, {"action": "ADDED_SYNONYMS", "changes": "Added 1 CultureMech recipe surface form(s) that folded onto this record's published label but were absent from MIM's label index, so CultureMech could not resolve them: 'Trace Metal Mix A5 (see below)' (x1 CultureMech mentions). Source: culturemech:output/ingredient_occurrences.tsv.", "curator": "claude_culturemech_alias_backfill", "llm_assisted": false, "timestamp": "2026-08-30T04:48:06.233536+00:00"}], "identifier": "MICRO:0001349", "mapping": {"evidence": [{"evidence_type": "DATABASE_MATCH", "notes": "Auto-upgraded from UNMAPPED_0258; matched via 'Trace metal mix A5' (name normalization); label-exact", "source": "MICRO via OLS search (resolve_unmapped)"}], "mapping_quality": "EXACT_MATCH", "ontology_id": "MICRO:0001349", "ontology_label": "trace metal mix A5", "ontology_source": "MICRO"}} |
| ev-3e284f13241fa94e | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Trace_Metal_Mix_A5 | supports | [{"comment": "", "confidence": "0.99", "data_row": 2804, "mapping_date": "2026-08-30", "mapping_justification": "semapv:LexicalMatching", "object_id": "MICRO:0001349", "object_label": "trace metal mix A5", "object_source": "obo:micro.owl", "other": "Trace Metal Mix A5 (see below)", "predicate_id": "skos:exactMatch", "source": "MIM:MICRO via OLS search (resolve_unmapped)&#124;MIM:curator=claude_culturemech_alias_backfill", "subject_id": "MIM:Trace_Metal_Mix_A5", "subject_label": "Trace metal mix A5", "validation_method": "none&#124;UNKNOWN_TERM&#124;2026-07-07"}] |
| ev-a6e7432b5d0fbcfb | reports/yaml_record_review/Trace_Metal_Mix_A5.md; Complete historical report, including Verdict and Recommended Edits | context_only | Historical interpretation was read in full; it is not fresh source adjudication. |
| ev-28bce6da08c8c14e | reviews/structured/20261011T024639Z-mim-reconcile-all-batch-12/review.yaml; findings[finding_id=f-54e5335934e0ba03] | context_only | Exact earlier occurrence has open/confirmed status, based on exported-token presence and historical report text. |
| ev-41b7b72cded4e05c | data/ingredients/mapped/Trace_Mineral_Solution.yaml; identifier, ontology_mapping, synonyms and curation_history | partial | {"candidate_labels": [{"source": "culturemech:output/ingredient_occurrences.tsv", "synonym_text": "Trace mineral solution (see Medium No. 151 )", "synonym_type": "RAW_TEXT"}, {"source": "culturemech:output/ingredient_occurrences.tsv", "synonym_text": "Trace mineral solution (see Medium No. 852 )", "synonym_type": "RAW_TEXT"}, {"source": "culturemech:output/ingredient_occurrences.tsv", "synonym_text": "Trace mineral solution (see Medium No.852)", "synonym_type": "RAW_TEXT"}, {"source": "culturemech:output/ingredient_occurrences.tsv", "synonym_text": "Trace mineral solution (see below)", "synonym_type": "RAW_TEXT"}], "history": [{"action": "CREATED_AS_UNMAPPED", "changes": "Imported from mim-queue (source_id=mediadive.ingredient:897); no CAS-RN or CHEBI/NCIT match. Curator review needed.", "curator": "audit_import_ingredients[mim-queue]", "llm_assisted": false, "new_status": "UNMAPPED", "timestamp": "2026-04-30T18:43:03.698454+00:00"}, {"action": "AUTO_CLASSIFY_INGREDIENT_TYPE", "changes": "set ingredient_type=STOCK_SOLUTION (name matches solution pattern 'mineral solution')", "curator": "auto_classify_ingredient_type", "llm_assisted": false, "timestamp": "2026-05-02T03:12:19.966568+00:00"}, {"action": "PROMOTED_TO_MAPPED", "changes": "Promoted UNMAPPED_0551 -&gt; kgmicrobe.ingredient:trace_mineral_solution (FALLBACK_REGISTRY). A named multi-component preparation. Searched CHEBI, NCIT, MeSH, FOODON and ENVO by label and synonym: no term denotes it, and none could -- a preparation is not a substance. Takes the STOCK_SOLUTION convention: a kgmicrobe.ingredient: mint with no parent, because a multi-component mix does not narrow to any single compound (#288).", "curator": "issue_288_stock_solutions", "llm_assisted": true, "new_status": "MAPPED", "previous_status": "UNMAPPED", "timestamp": "2026-08-06T00:00:00+00:00"}, {"action": "CORRECTED", "changes": "occurrence_statistics 0/0 -&gt; 2/2 (media_count/total_occurrences), derived from distinct CultureMech recipe ids in the #337 occurrence table. The prior values came from the importer retired in #453, whose media_count counted a list truncated to 50 examples (#449). [source=ingredient_occurrences.tsv culturemech_rev=15a4da5c08 rows=194137 distinct_recipes=15257]", "curator": "refresh_occurrence_statistics", "timestamp": "2026-08-27T03:16:39.520310+00:00"}, {"action": "ADDED_SYNONYMS", "changes": "Added 5 CultureMech recipe surface form(s) that folded onto this record's published label but were absent from MIM's label index, so CultureMech could not resolve them: 'Trace mineral solution (see Medium No. 151 )' (x2 CultureMech mentions); 'Trace mineral solution (see Medium No. 852 )' (x1 CultureMech mentions); 'Trace mineral solution (see Medium No.852)' (x1 CultureMech mentions); 'Trace mineral solution (see below)' (x1 CultureMech mentions); 'Trace mineral solution**' (x1 CultureMech mentions). Source: culturemech:output/ingredient_occurrences.tsv.", "curator": "claude_culturemech_alias_backfill", "llm_assisted": false, "timestamp": "2026-08-30T04:48:06.233536+00:00"}], "identifier": "kgmicrobe.ingredient:trace_mineral_solution", "mapping": {"evidence": [{"evidence_type": "MANUAL_CURATION", "notes": "A named multi-component preparation. Searched CHEBI, NCIT, MeSH, FOODON and ENVO by label and synonym: no term denotes it, and none could -- a preparation is not a substance. Takes the STOCK_SOLUTION convention: a kgmicrobe.ingredient: mint with no parent, because a multi-component mix does not narrow to any single compound (#288).", "source": "MIM curation (#288)"}], "mapping_quality": "FALLBACK_REGISTRY", "ontology_id": "kgmicrobe.ingredient:trace_mineral_solution", "ontology_label": "Trace mineral solution", "ontology_source": "kgmicrobe.ingredient"}} |
| ev-3f611fd20092d7d4 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Trace_Mineral_Solution | supports | [{"comment": "", "confidence": "0.9", "data_row": 2807, "mapping_date": "2026-08-30", "mapping_justification": "semapv:ManualMappingCuration", "object_id": "kgmicrobe.ingredient:trace_mineral_solution", "object_label": "Trace mineral solution", "object_source": "kgm:ingredient", "other": "Trace mineral solution (see Medium No. 151 )&#124;Trace mineral solution (see Medium No. 852 )&#124;Trace mineral solution (see Medium No.852)&#124;Trace mineral solution (see below)&#124;Trace mineral solution**", "predicate_id": "skos:exactMatch", "source": "MIM:MIM curation (#288)&#124;MIM:curator=claude_culturemech_alias_backfill", "subject_id": "MIM:Trace_Mineral_Solution", "subject_label": "Trace mineral solution", "validation_method": "none&#124;UNKNOWN_TERM&#124;2026-09-02"}] |
| ev-ff886fb7448948d4 | reports/yaml_record_review/Trace_Mineral_Solution.md; Complete historical report, including Verdict and Recommended Edits | context_only | Historical interpretation was read in full; it is not fresh source adjudication. |
| ev-e098338a3394e86d | reviews/structured/20261011T024639Z-mim-reconcile-all-batch-12/review.yaml; findings[finding_id=f-0fa9eaef6cc34337] | context_only | Exact earlier occurrence has open/confirmed status, based on exported-token presence and historical report text. |
| ev-2c39d54a6bcf5e1b | data/ingredients/mapped/Trace_Minerals.yaml; identifier, ontology_mapping, synonyms and curation_history | partial | {"candidate_labels": [{"source": "culturemech:output/ingredient_occurrences.tsv", "synonym_text": "Trace minerals (see below)", "synonym_type": "RAW_TEXT"}], "history": [{"action": "CREATED_AS_UNMAPPED", "changes": "Imported from mim-queue (source_id=mediadive.ingredient:1031); no CAS-RN or CHEBI/NCIT match. Curator review needed.", "curator": "audit_import_ingredients[mim-queue]", "llm_assisted": false, "new_status": "UNMAPPED", "timestamp": "2026-04-30T18:43:03.698454+00:00"}, {"action": "REVIEWED_NON_IDENTITY_PARENT", "changes": "Reviewed OAK/OLS audit candidate MESH:D014131 Trace Elements; left unmapped because the source label denotes a trace-mineral ingredient/preparation, not identity with the full trace-elements ontology class.", "curator": "mediaingredientmech-agentic-curation", "llm_assisted": true, "new_status": "UNMAPPED", "previous_status": "UNMAPPED", "timestamp": "2026-05-11T07:50:00Z"}, {"action": "CLASSIFIED_STOCK_SOLUTION", "changes": "Classified as a trace-mineral stock/pre-mix and left unmapped pending component-level recipe curation.", "curator": "mediaingredientmech-agentic-curation", "llm_assisted": true, "new_status": "UNMAPPED", "previous_status": "UNMAPPED", "timestamp": "2026-05-11T19:50:00Z"}, {"action": "PROMOTED_TO_MAPPED", "changes": "Promoted UNMAPPED_0552 -&gt; kgmicrobe.ingredient:trace_minerals (FALLBACK_REGISTRY). A named multi-component preparation. Searched CHEBI, NCIT, MeSH, FOODON and ENVO by label and synonym: no term denotes it, and none could -- a preparation is not a substance. Takes the STOCK_SOLUTION convention: a kgmicrobe.ingredient: mint with no parent, because a multi-component mix does not narrow to any single compound (#288).", "curator": "issue_288_stock_solutions", "llm_assisted": true, "new_status": "MAPPED", "previous_status": "UNMAPPED", "timestamp": "2026-08-06T00:00:00+00:00"}, {"action": "CORRECTED", "changes": "occurrence_statistics 0/0 -&gt; 3/3 (media_count/total_occurrences), derived from distinct CultureMech recipe ids in the #337 occurrence table. The prior values came from the importer retired in #453, whose media_count counted a list truncated to 50 examples (#449). [source=ingredient_occurrences.tsv culturemech_rev=15a4da5c08 rows=194137 distinct_recipes=15257]", "curator": "refresh_occurrence_statistics", "timestamp": "2026-08-27T03:16:39.520312+00:00"}, {"action": "ADDED_SYNONYMS", "changes": "Added 2 CultureMech recipe surface form(s) that folded onto this record's published label but were absent from MIM's label index, so CultureMech could not resolve them: 'Trace minerals (see below)' (x2 CultureMech mentions); 'Trace minerals*' (x1 CultureMech mentions). Source: culturemech:output/ingredient_occurrences.tsv.", "curator": "claude_culturemech_alias_backfill", "llm_assisted": false, "timestamp": "2026-08-30T04:48:06.233536+00:00"}], "identifier": "kgmicrobe.ingredient:trace_minerals", "mapping": {"evidence": [{"evidence_type": "MANUAL_CURATION", "notes": "A named multi-component preparation. Searched CHEBI, NCIT, MeSH, FOODON and ENVO by label and synonym: no term denotes it, and none could -- a preparation is not a substance. Takes the STOCK_SOLUTION convention: a kgmicrobe.ingredient: mint with no parent, because a multi-component mix does not narrow to any single compound (#288).", "source": "MIM curation (#288)"}], "mapping_quality": "FALLBACK_REGISTRY", "ontology_id": "kgmicrobe.ingredient:trace_minerals", "ontology_label": "Trace minerals", "ontology_source": "kgmicrobe.ingredient"}} |
| ev-ec1703c8dacbdf80 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Trace_Minerals | supports | [{"comment": "", "confidence": "0.9", "data_row": 2808, "mapping_date": "2026-08-30", "mapping_justification": "semapv:ManualMappingCuration", "object_id": "kgmicrobe.ingredient:trace_minerals", "object_label": "Trace minerals", "object_source": "kgm:ingredient", "other": "Trace minerals (see below)&#124;Trace minerals*", "predicate_id": "skos:exactMatch", "source": "MIM:MIM curation (#288)&#124;MIM:curator=claude_culturemech_alias_backfill", "subject_id": "MIM:Trace_Minerals", "subject_label": "Trace minerals", "validation_method": "none&#124;UNKNOWN_TERM&#124;2026-09-02"}] |
| ev-649d543ff1a236ba | reports/yaml_record_review/Trace_Minerals.md; Complete historical report, including Verdict and Recommended Edits | context_only | Historical interpretation was read in full; it is not fresh source adjudication. |
| ev-0701e78e991c4118 | reviews/structured/20261011T024639Z-mim-reconcile-all-batch-12/review.yaml; findings[finding_id=f-397b1df68e373137] | context_only | Exact earlier occurrence has open/confirmed status, based on exported-token presence and historical report text. |
| ev-5175fd560468ba85 | data/ingredients/mapped/Yeast_Extract.yaml; identifier, ontology_mapping, synonyms and curation_history | partial | {"candidate_labels": [{"source": "microbedecoder", "synonym_text": "Yeast Extract (0.01 %", "synonym_type": "RAW_TEXT"}], "history": [{"action": "IMPORTED", "changes": "Initial import from CultureMech pipeline", "curator": "import_from_culturemech", "llm_assisted": false, "new_status": "UNMAPPED", "timestamp": "2026-03-09T06:54:18.022301+00:00"}, {"action": "ADDED_CAS_RN", "changes": "Added CAS-RN:8013-01-2 from CultureBotHT compound mappings", "curator": "integrate_cas_rn_from_culturebot_ht", "llm_assisted": false, "new_status": "UNMAPPED", "timestamp": "2026-04-05T17:53:47.291847+00:00"}, {"action": "MAPPED", "changes": "Promoted commercial food-mixture surface forms with FOODON:03315426 (yeast extract). Added brand/catalog variants as synonyms.", "curator": "foodon_promotion_cbclaw", "llm_assisted": true, "new_status": "MAPPED", "timestamp": "2026-04-18T04:19:36+00:00"}, {"action": "AUTO_CLASSIFY_INGREDIENT_TYPE", "changes": "set ingredient_type=UNDEFINED_MIXTURE (name matches complex pattern 'Yeast')", "curator": "auto_classify_ingredient_type", "llm_assisted": false, "timestamp": "2026-05-01T07:35:36.939492+00:00"}, {"action": "AUTO_CLASSIFY_INGREDIENT_TYPE", "changes": "set ingredient_type=UNDEFINED_MIXTURE (name matches complex pattern 'Yeast')", "curator": "auto_classify_ingredient_type", "llm_assisted": false, "timestamp": "2026-05-02T03:12:19.307519+00:00"}, {"action": "ANNOTATED", "changes": "Added media role: PROTEIN_SOURCE (confidence: 0.80)", "curator": "infer_roles_from_name_lists", "timestamp": "2026-06-03T02:06:01.753916+00:00"}, {"action": "ANNOTATED", "changes": "Migrated legacy media_roles to role facets (#128): PROTEIN_SOURCE -&gt; nutritional_roles.PROTEIN_SOURCE", "curator": "migrate_media_roles_to_facets", "timestamp": "2026-07-20T00:00:00+00:00"}, {"action": "MERGED_FROM_UNMAPPED_DUPLICATE", "changes": "Absorbed UNMAPPED_0700 'Yeast Extract (0.01 %' as a RAW_TEXT synonym -- concentration-truncated duplicate of yeast extract. No new SSSOM row; FOODON:03315426 is already mapped. Source: kgmicrobe.trait:yeast_extract_0_01.", "curator": "microbedecoder-residual-dispositions", "llm_assisted": true, "timestamp": "2026-08-05T00:01:30.894952+00:00"}, {"action": "CORRECTED", "changes": "occurrence_statistics 5/5 -&gt; 7617/7697 (media_count/total_occurrences), derived from distinct CultureMech recipe ids in the #337 occurrence table. The prior values came from the importer retired in #453, whose media_count counted a list truncated to 50 examples (#449). [source=ingredient_occurrences.tsv culturemech_rev=15a4da5c08 rows=194137 distinct_recipes=15257]", "curator": "refresh_occurrence_statistics", "timestamp": "2026-08-27T03:16:39.520171+00:00"}, {"action": "ADDED_SYNONYMS", "changes": "Added 1 CultureMech recipe surface form(s) that folded onto this record's published label but were absent from MIM's label index, so CultureMech could not resolve them: 'Fresh Baker\u2019s Yeast Extract' (x1 CultureMech mentions). Source: culturemech:output/ingredient_occurrences.tsv.", "curator": "claude_culturemech_alias_backfill", "llm_assisted": false, "timestamp": "2026-08-30T04:48:06.233536+00:00"}], "identifier": "FOODON:03315426", "mapping": {"evidence": [{"evidence_type": "CURATOR_JUDGMENT", "notes": "Commercial food mixture - FOODON is correct parent ontology (not CHEBI, since yeast extract is a multi-component food extract, not a single chemical).", "source": "cbclaw_foodon_promotion"}], "mapping_quality": "EXACT_MATCH", "ontology_id": "FOODON:03315426", "ontology_label": "yeast extract", "ontology_source": "FOODON"}} |
| ev-c84617d1a202e069 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Yeast_Extract | supports | [{"comment": "", "confidence": "0.99", "data_row": 2949, "mapping_date": "2026-08-30", "mapping_justification": "semapv:LexicalMatching", "object_id": "FOODON:03315426", "object_label": "yeast extract", "object_source": "obo:foodon.owl", "other": "Yeast extract(Bacto, Difco)&#124;Yeast extract(CAS: 8013-01-2)&#124;Yeast extract (BD-Difco)&#124;Bacto Yeast Extract (Difco)&#124;Yeast extract (OXOID)&#124;Bacto yeast extract&#124;Yeast extract (Difco)&#124;Yeast extract (BD--Difco)&#124;Yeast Extract (BD 212750)&#124;Yeast extract (Difco or Oxoid)&#124;Yeast extract (BD Bacto)&#124;Bacto Yeast  Extract (Difco)&#124;Yeast extract (BD-BBL)&#124;Yeast extract (Oxoid LP0021, BD 212750)&#124;Yeast Extract (BD 211928)&#124;Difco Bacto-yeast extract&#124;Dried yeast extract S (Wako)&#124;Yeast Extract (BD, 212750)&#124;Yeast extract(Oxoid)&#124;Yeast extract (BBL)&#124;Bacto-yeast extract&#124;Yeast Extract(Difco)&#124;yeast extract (BD Difco)&#124;yeast extract (Nacalai Tesque, Kyoto, Japan)&#124;Yeast Extract (Hardy C7340)&#124;Liquid yeast extract (Flow)&#124;Fresh Baker's Yeast Extract&#124;Yeast Extract (0.01 %&#124;Fresh Baker\u2019s Yeast Extract&#124;CAS:8013-01-2", "predicate_id": "skos:exactMatch", "source": "MIM:cbclaw_foodon_promotion&#124;MIM:curator=claude_culturemech_alias_backfill", "subject_id": "MIM:Yeast_Extract", "subject_label": "Yeast extract", "validation_method": "OLS:foodon&#124;SYNONYM_ENRICH&#124;2026-07-07"}] |
| ev-ef345ac5a6dc1108 | reports/yaml_record_review/Yeast_Extract.md; Complete historical report, including Verdict and Recommended Edits | context_only | Historical interpretation was read in full; it is not fresh source adjudication. |

## Limits And Additional Notes

- Only certainty of the selected observations is corrected. Other historical identity, role, component, source-count and provenance allegations remain in their original scope.
- Artificial_seawater and DL_Vitamins historical reports explicitly accept their raw labels; the initial extraction invented a historical concern for those targets.
- The exact current exported labels are known, but whether each denotes the same substance requires source-level interpretation. No ingredient bytes or native release dispositions changed.
- Full scientific review and ontology B4 are not claimed by this partial reconciliation.
- Addresses review-process issue #861 in PR #860. It does not resolve the scientific curation backlog #718.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T030852Z-mim-token-scope-reassessment
kind: batch
repository: culturebotai/MediaIngredientMech
title: Correct certainty of 17 recipe-token reconciliation observations
started_at: '2026-10-11T03:06:05Z'
finished_at: '2026-10-11T03:08:52Z'
reviewer:
  identity: Codex
  kind: agent
  independence: self_review
  independence_basis: Same assistant authored the initial reconciliation. This is
    adversarial self-review of its inference, not independent scientific approval.
skill: reconcile-review-records
completion: partial
verdict: needs_curation
scientific_review: false
summary: Append 17 deferred/provisional successors after auditing the prior token
  heuristic. Historical reports, source labels, and all other findings are unchanged.
  Source-context science is not completed.
source:
  git_revision: 0cc2b4e354ecc4f005eb7ef833ca23fdc64041a3
  state: working_tree
  inputs:
  - path: .claude/skills/reconcile-review-records/SKILL.md
    sha256: b45405da1bf37b79e38a40c0d4cc87266015cccf2df09b3bc7b5f9478181ca8e
    role: context
  - path: MAPPING_SEMANTICS.md
    sha256: 39d678299c584cf6bc2625e4083afaa789ccfb461d676299115ba302c2f10679
    role: context
  - path: data/ingredients/mapped/4-vinylphenol.yaml
    sha256: 8d4c406e24cbb343fb17cd6345b6628caf2e27ca07510c73c8ff2376a815c0f9
    role: target
  - path: data/ingredients/mapped/Artificial_seawater.yaml
    sha256: 9efeac859a634d9d5daf17c7da4e058b51ce7538b0b802fa6ac2b7f6f602e708
    role: target
  - path: data/ingredients/mapped/DL_Vitamins.yaml
    sha256: 41a6ce40ee3f2a5a705f041f6d20d72ecd977a2dea42c477dc997191d1be44ad
    role: target
  - path: data/ingredients/mapped/Desulfovibrio_Trace_Elements.yaml
    sha256: 93db08d82a87268e9c970192268b222cd7f518ef64f468aeceea672e329a20ea
    role: target
  - path: data/ingredients/mapped/Fatty_Acid_Mixture_See_Medium_No_266.yaml
    sha256: 00aa192a2ce2f4acb1b752d3a478ca4e661c8e15e2f0039c9b22b608a10a7e6c
    role: target
  - path: data/ingredients/mapped/Mineral_Solution_See_Medium_No_976.yaml
    sha256: 911de800edd62dc119f74d48432257ba1f22c2be95ebeb37f8e79385aecdd238
    role: target
  - path: data/ingredients/mapped/Modified_Trace_Vitamins.yaml
    sha256: 4eedaddb0efbc29c6dead6ef2bd378ec59070ecea3146b66e77bcea55a204a2c
    role: target
  - path: data/ingredients/mapped/Peptone.yaml
    sha256: e00551197758fb417846becc5c14e931f614bc00887609b8749d734ad2f8d4aa
    role: target
  - path: data/ingredients/mapped/Potassium_Phosphate_Buffer.yaml
    sha256: 9a33ce5d93f8928878ab1309f834d49f505d27abf4d5ee41e23b79a40a2ac40e
    role: target
  - path: data/ingredients/mapped/Riboflavin.yaml
    sha256: b79fe5e134e627e7c95d6190e54c52b04f9d81a61ad381cb136b986430d80644
    role: target
  - path: data/ingredients/mapped/Sludge_fluid.yaml
    sha256: 45eed06b9f478903bfb4849c19b5656aca154018619b1db3d08152b5212e489c
    role: target
  - path: data/ingredients/mapped/Soil_Extract.yaml
    sha256: 6983e9a7a4460eb605e05eaed32f6c08397e2555ce1356d98fb5d301b592e848
    role: target
  - path: data/ingredients/mapped/Trace_Element_Solution_See_Medium_No_187.yaml
    sha256: eea23f3c73fe8d5993d5292436d12776dde1308bcedf2a4916d1ca553b6cf40d
    role: target
  - path: data/ingredients/mapped/Trace_Metal_Mix_A5.yaml
    sha256: 5982838d016b9e668006fa6cd8108c3930358970b2156b2a1596425af3ab4ef2
    role: target
  - path: data/ingredients/mapped/Trace_Mineral_Solution.yaml
    sha256: 03837875ebc88c1ab82387c244b383de83a01bc77f4fd60cd75fbbecdcd31f81
    role: target
  - path: data/ingredients/mapped/Trace_Minerals.yaml
    sha256: 9a1b033572d1f6462d4de4d9f07d655e34f98fe37d82c2449d4a48cc2dadd1bc
    role: target
  - path: data/ingredients/mapped/Yeast_Extract.yaml
    sha256: e7cdc5aa92020487a97c08814514fa48b852ff48c78a1d1890b69afaaf372d28
    role: target
  - path: docs/record-reviews.md
    sha256: 452a19ab688276747b7c4308523a14d4d99c1c39ef6909ae8a90b85b7a9b3e9b
    role: context
  - path: mappings/ingredient_mappings.sssom.tsv
    sha256: 2eae181f31d6433c20ffdb9dc2f8c8d7ad0a17a46a3189dea8c307fbc1c7b40e
    role: context
  - path: reports/yaml_record_review/4-vinylphenol.md
    sha256: 2214bfc494f21e540ca4c95362b07f22597d870efc1ef0937d619d09bb58e1b8
    role: context
  - path: reports/yaml_record_review/Artificial_seawater.md
    sha256: 678c1882c36eb0a94f762d006e36deb3a61b751b7d424573a723abe497e8c936
    role: context
  - path: reports/yaml_record_review/DL_Vitamins.md
    sha256: e5d9436f54deaa206abe6a293a0f86a784f0fc6406f2bf28ef415ba1ac7fe1b7
    role: context
  - path: reports/yaml_record_review/Desulfovibrio_Trace_Elements.md
    sha256: f655ff5e9d199deb38ad4e8e7e7ddb2aa844aecc6d1ec3efb037bbfade3e6aba
    role: context
  - path: reports/yaml_record_review/Fatty_Acid_Mixture_See_Medium_No_266.md
    sha256: 1699420fb78c42ed15355504b4a30c60190cf49a03fd7ce28b1129af4a0737dd
    role: context
  - path: reports/yaml_record_review/Mineral_Solution_See_Medium_No_976.md
    sha256: 75b5bf9ce1cf58d7f737fc163464400e4c8e6f66d2e610e439c0594b1e71c1bb
    role: context
  - path: reports/yaml_record_review/Modified_Trace_Vitamins.md
    sha256: 1bfc880ed06f1c6448af8e81cef6be73c4e8dfc3230d00e4ab8241c3de76ee7d
    role: context
  - path: reports/yaml_record_review/Peptone.md
    sha256: ff7ee8ae08e2406bcca09345d75c8024a56f48457839ff026e9bf007b4f2e4fe
    role: context
  - path: reports/yaml_record_review/Potassium_Phosphate_Buffer.md
    sha256: 884a3c1ac80ea7503bc943cac7d9eef7ff8d329cc1b7da000b75ab605e4019e0
    role: context
  - path: reports/yaml_record_review/Riboflavin.md
    sha256: 9dd8b2a901c40593a896669ad82303310aafb787ae2f8c505cbaa93fd256e8fc
    role: context
  - path: reports/yaml_record_review/Sludge_fluid.md
    sha256: 644b8e24ff48c5a4f36eb61fb433068aceaebb59b6cc9b0970535705b399fdbf
    role: context
  - path: reports/yaml_record_review/Soil_Extract.md
    sha256: ae5ccc882afbb6dc1bede0c3b61e54987fe5116620d05dd4794692387a263a84
    role: context
  - path: reports/yaml_record_review/Trace_Element_Solution_See_Medium_No_187.md
    sha256: 9d6913d60ca5135c4cd8074f78886386638a460bae5393725ce8f4aa35fc2f55
    role: context
  - path: reports/yaml_record_review/Trace_Metal_Mix_A5.md
    sha256: fd88d90adbbb3033d82b606fa92e4793b6a9590f36d8bae2ac5819b09aa09534
    role: context
  - path: reports/yaml_record_review/Trace_Mineral_Solution.md
    sha256: 95f2187e644085226dc05c4e6c0a2b3fc440fc600205141bc84c41b066625b34
    role: context
  - path: reports/yaml_record_review/Trace_Minerals.md
    sha256: ca899d0e1e9ffdc149ed07abe32a65e07f563cffb61c30cddb9fbe01b22b47e5
    role: context
  - path: reports/yaml_record_review/Yeast_Extract.md
    sha256: e1920c4292a8d9d9155fcb45d62306b5f2f645732eac0501e49b634c3d4c6d73
    role: context
  - path: reviews/structured/20261011T024630Z-mim-reconcile-all-batch-02/review.md
    sha256: b86932a538ba4a744974af7bba1cbd77e39ee21ecd220ee7fd296e00d1b58938
    role: context
  - path: reviews/structured/20261011T024630Z-mim-reconcile-all-batch-02/review.yaml
    sha256: 799a1a80fa398851bced286dd0f68a97e6a22f7090d53677678dc13b92c6f076
    role: context
  - path: reviews/structured/20261011T024631Z-mim-reconcile-all-batch-03/review.md
    sha256: 4b4a89615214f3d370fa73020f466ad005aec2176aae045584336938090c38ca
    role: context
  - path: reviews/structured/20261011T024631Z-mim-reconcile-all-batch-03/review.yaml
    sha256: 6b3844c17bf3608ea8f73f824efec195e906ab8d2703fef4cd97fda04f0e65bf
    role: context
  - path: reviews/structured/20261011T024633Z-mim-reconcile-all-batch-05/review.md
    sha256: b318fb1870fd5251b729bc0bc79ed9d463404894e2e3190a8fed18eb3bde2055
    role: context
  - path: reviews/structured/20261011T024633Z-mim-reconcile-all-batch-05/review.yaml
    sha256: 7549030a5b50ed98868ff3497507fdfbfecd07cd858c76738f734521fa9d3603
    role: context
  - path: reviews/structured/20261011T024634Z-mim-reconcile-all-batch-06/review.md
    sha256: 0023ee7e1c55a01980108594056181014f1528c79a096c330d3ec0340c7f8404
    role: context
  - path: reviews/structured/20261011T024634Z-mim-reconcile-all-batch-06/review.yaml
    sha256: 14c3200be95fdc87fca16bb71628432f3c9aaf8a65356ed494efc776ebe8aa11
    role: context
  - path: reviews/structured/20261011T024636Z-mim-reconcile-all-batch-08/review.md
    sha256: 9f882e541be36654f04c95192bffd2105544672c853cc3c0c6205520f84a41b7
    role: context
  - path: reviews/structured/20261011T024636Z-mim-reconcile-all-batch-08/review.yaml
    sha256: 4dd969b7020555cc2250a236d6fded134bedf3add1e1c5c72d269e98f9ae001b
    role: context
  - path: reviews/structured/20261011T024637Z-mim-reconcile-all-batch-09/review.md
    sha256: 8f13cc72cba534c63a486860528b78d2e42ddf07b148d5edae5c0d295ff2fb52
    role: context
  - path: reviews/structured/20261011T024637Z-mim-reconcile-all-batch-09/review.yaml
    sha256: cf46750874f1303863883723934bbe8b09ece8d62b1785ceab64bb0342a3cf11
    role: context
  - path: reviews/structured/20261011T024638Z-mim-reconcile-all-batch-10/review.md
    sha256: b8884743b84ec8c56ccb0364502b5b97e374f72d7c8d5fdda2271357b8ac19e6
    role: context
  - path: reviews/structured/20261011T024638Z-mim-reconcile-all-batch-10/review.yaml
    sha256: 8c3aa2fca1269d1dbbf6117e85dea5b0de5047a8505841641245bd7ee99b936d
    role: context
  - path: reviews/structured/20261011T024638Z-mim-reconcile-all-batch-11/review.md
    sha256: 6e37512f3247b9edb4fc3d7b6332b6e8d9ea08348698caaf62122e332321621e
    role: context
  - path: reviews/structured/20261011T024638Z-mim-reconcile-all-batch-11/review.yaml
    sha256: a417d1bfc777756925990a4ecae1a6b539746c3606d042df7e1c29a218c62f8b
    role: context
  - path: reviews/structured/20261011T024639Z-mim-reconcile-all-batch-12/review.md
    sha256: 78ae241413c327e3a1e4c98b7b8c2e8e5d1669cd8c9915baf892433ff9f47928
    role: context
  - path: reviews/structured/20261011T024639Z-mim-reconcile-all-batch-12/review.yaml
    sha256: 20e55e956f704a8c90164bf2749b9ddf6c35d94cdcbab538776d0675aa150899
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/record_review.py
    sha256: 95a4ec41e38ec47ba3578e76838c46a0adbf47e49ad3636524735d08cfcb1c4d
    role: context
targets:
- target_id: record-88ed3645c26c14b6
  path: data/ingredients/mapped/4-vinylphenol.yaml
  label: 4-vinylphenol
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/4-vinylphenol.yaml
    role: maintained ingredient
- target_id: record-205c79d137874075
  path: data/ingredients/mapped/Artificial_seawater.yaml
  label: Artificial_seawater
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Artificial_seawater.yaml
    role: maintained ingredient
- target_id: record-9122c364d42e8559
  path: data/ingredients/mapped/DL_Vitamins.yaml
  label: DL_Vitamins
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/DL_Vitamins.yaml
    role: maintained ingredient
- target_id: record-797da68010f27377
  path: data/ingredients/mapped/Desulfovibrio_Trace_Elements.yaml
  label: Desulfovibrio_Trace_Elements
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Desulfovibrio_Trace_Elements.yaml
    role: maintained ingredient
- target_id: record-099e2c8a2a9f8f68
  path: data/ingredients/mapped/Fatty_Acid_Mixture_See_Medium_No_266.yaml
  label: Fatty_Acid_Mixture_See_Medium_No_266
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Fatty_Acid_Mixture_See_Medium_No_266.yaml
    role: maintained ingredient
- target_id: record-7059116102e92505
  path: data/ingredients/mapped/Mineral_Solution_See_Medium_No_976.yaml
  label: Mineral_Solution_See_Medium_No_976
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Mineral_Solution_See_Medium_No_976.yaml
    role: maintained ingredient
- target_id: record-4253636d94bcf2f1
  path: data/ingredients/mapped/Modified_Trace_Vitamins.yaml
  label: Modified_Trace_Vitamins
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Modified_Trace_Vitamins.yaml
    role: maintained ingredient
- target_id: record-62f485f9f7517526
  path: data/ingredients/mapped/Peptone.yaml
  label: Peptone
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Peptone.yaml
    role: maintained ingredient
- target_id: record-4190c0ee5976447a
  path: data/ingredients/mapped/Potassium_Phosphate_Buffer.yaml
  label: Potassium_Phosphate_Buffer
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Potassium_Phosphate_Buffer.yaml
    role: maintained ingredient
- target_id: record-59776f859c41300d
  path: data/ingredients/mapped/Riboflavin.yaml
  label: Riboflavin
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Riboflavin.yaml
    role: maintained ingredient
- target_id: record-c6cdd023283a1f0a
  path: data/ingredients/mapped/Sludge_fluid.yaml
  label: Sludge_fluid
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Sludge_fluid.yaml
    role: maintained ingredient
- target_id: record-3245d67aff586e82
  path: data/ingredients/mapped/Soil_Extract.yaml
  label: Soil_Extract
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Soil_Extract.yaml
    role: maintained ingredient
- target_id: record-341efa75278b5e50
  path: data/ingredients/mapped/Trace_Element_Solution_See_Medium_No_187.yaml
  label: Trace_Element_Solution_See_Medium_No_187
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Trace_Element_Solution_See_Medium_No_187.yaml
    role: maintained ingredient
- target_id: record-78ea6a14a080dbf0
  path: data/ingredients/mapped/Trace_Metal_Mix_A5.yaml
  label: Trace_Metal_Mix_A5
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Trace_Metal_Mix_A5.yaml
    role: maintained ingredient
- target_id: record-4b03942a3427132e
  path: data/ingredients/mapped/Trace_Mineral_Solution.yaml
  label: Trace_Mineral_Solution
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Trace_Mineral_Solution.yaml
    role: maintained ingredient
- target_id: record-7c55027f9d88edd0
  path: data/ingredients/mapped/Trace_Minerals.yaml
  label: Trace_Minerals
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Trace_Minerals.yaml
    role: maintained ingredient
- target_id: record-4efe2f6907f0d4fc
  path: data/ingredients/mapped/Yeast_Extract.yaml
  label: Yeast_Extract
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Yeast_Extract.yaml
    role: maintained ingredient
scope:
  description: Certainty of 17 exported-context-token findings, not whole-record identity
    or scientific review.
  selection: All 17 exported-context-tokens findings in the 13 initial all-MIM reconciliation
    batches.
  coverage: full
  population_size: 17
  reviewed_target_ids:
  - record-88ed3645c26c14b6
  - record-205c79d137874075
  - record-9122c364d42e8559
  - record-797da68010f27377
  - record-099e2c8a2a9f8f68
  - record-7059116102e92505
  - record-4253636d94bcf2f1
  - record-62f485f9f7517526
  - record-4190c0ee5976447a
  - record-59776f859c41300d
  - record-c6cdd023283a1f0a
  - record-3245d67aff586e82
  - record-341efa75278b5e50
  - record-78ea6a14a080dbf0
  - record-4b03942a3427132e
  - record-7c55027f9d88edd0
  - record-4efe2f6907f0d4fc
checks:
- check_id: pairs
  name: Exact predecessor pair validation
  status: passed
  required: true
  summary: read_review verified every selected predecessor YAML/Markdown pair and
    retained provenance before authoring.
  target_ids:
  - record-88ed3645c26c14b6
  - record-205c79d137874075
  - record-9122c364d42e8559
  - record-797da68010f27377
  - record-099e2c8a2a9f8f68
  - record-7059116102e92505
  - record-4253636d94bcf2f1
  - record-62f485f9f7517526
  - record-4190c0ee5976447a
  - record-59776f859c41300d
  - record-c6cdd023283a1f0a
  - record-3245d67aff586e82
  - record-341efa75278b5e50
  - record-78ea6a14a080dbf0
  - record-4b03942a3427132e
  - record-7c55027f9d88edd0
  - record-4efe2f6907f0d4fc
- check_id: lineage
  name: Explicit predecessor and competing-head audit
  status: passed
  required: true
  summary: All 651 pre-existing occurrences across the ignored-inclusive structured
    inventory had unique issue keys and no predecessors. Each of these 17 successors
    cites its exact prior occurrence and retains its target. The default sibling CLAW
    reviews module was unavailable; this was an explicit local audit, not a claim
    of schema-level lineage validation.
  target_ids:
  - record-88ed3645c26c14b6
  - record-205c79d137874075
  - record-9122c364d42e8559
  - record-797da68010f27377
  - record-099e2c8a2a9f8f68
  - record-7059116102e92505
  - record-4253636d94bcf2f1
  - record-62f485f9f7517526
  - record-4190c0ee5976447a
  - record-59776f859c41300d
  - record-c6cdd023283a1f0a
  - record-3245d67aff586e82
  - record-341efa75278b5e50
  - record-78ea6a14a080dbf0
  - record-4b03942a3427132e
  - record-7c55027f9d88edd0
  - record-4efe2f6907f0d4fc
- check_id: presence
  name: Exact-subject export presence
  status: passed
  required: true
  summary: Parsed current records and exact-subject SSSOM rows. Each target still
    has at least one of the recipe-pointer/truncated-concentration source tokens.
    Presence does not prove invalid synonym scope.
  target_ids:
  - record-88ed3645c26c14b6
  - record-205c79d137874075
  - record-9122c364d42e8559
  - record-797da68010f27377
  - record-099e2c8a2a9f8f68
  - record-7059116102e92505
  - record-4253636d94bcf2f1
  - record-62f485f9f7517526
  - record-4190c0ee5976447a
  - record-59776f859c41300d
  - record-c6cdd023283a1f0a
  - record-3245d67aff586e82
  - record-341efa75278b5e50
  - record-78ea6a14a080dbf0
  - record-4b03942a3427132e
  - record-7c55027f9d88edd0
  - record-4efe2f6907f0d4fc
- check_id: sources
  name: Primary source-context adjudication
  status: skipped
  required: true
  summary: Exact recipe/preparation and ontology evidence were not freshly adjudicated.
    No token was rejected, removed, or scientifically approved.
  target_ids:
  - record-88ed3645c26c14b6
  - record-205c79d137874075
  - record-9122c364d42e8559
  - record-797da68010f27377
  - record-099e2c8a2a9f8f68
  - record-7059116102e92505
  - record-4253636d94bcf2f1
  - record-62f485f9f7517526
  - record-4190c0ee5976447a
  - record-59776f859c41300d
  - record-c6cdd023283a1f0a
  - record-3245d67aff586e82
  - record-341efa75278b5e50
  - record-78ea6a14a080dbf0
  - record-4b03942a3427132e
  - record-7c55027f9d88edd0
  - record-4efe2f6907f0d4fc
evidence:
- evidence_id: ev-823412d1eacb6795
  kind: record_content
  reference: MAPPING_SEMANTICS.md
  locator: Sections on REJECTED_LABEL and the damaged-label RAW_TEXT carve-out
  accessed_at: '2026-10-11T03:08:52Z'
  support: supports
  summary: Raw spellings may remain resolvable when they denote the same substance.
    Wrong-identity labels must not resolve. A recipe-pointer pattern alone does not
    adjudicate that distinction.
  snapshot_sha256: 39d678299c584cf6bc2625e4083afaa789ccfb461d676299115ba302c2f10679
- evidence_id: ev-f983f8801d1e4699
  kind: prior_review
  reference: reviews/structured/20261011T024630Z-mim-reconcile-all-batch-02/review.yaml
  locator: findings[finding_id=f-be91e29ea6694d28]
  accessed_at: '2026-10-11T03:08:52Z'
  support: context_only
  summary: Exact earlier occurrence has open/confirmed status, based on exported-token
    presence and historical report text.
  snapshot_sha256: 799a1a80fa398851bced286dd0f68a97e6a22f7090d53677678dc13b92c6f076
  quote: '{"category": "nomenclature", "certainty": "confirmed", "description": "Historical
    tokens are still present on the exact-subject SSSOM rows: [{\"reason\":\"unresolved
    recipe cross-reference in a resolving synonym\",\"token\":\"Trace minerals (see
    Medium No.151\"},{\"reason\":\"unresolved recipe cross-reference in a resolving
    synonym\",\"token\":\"Trace minerals(see Medium No.151)\"}]. Truncated concentration
    strings and context-dependent instructions need scoped curation. This check does
    not reject catalog/RAW_TEXT synonyms as a class.", "evidence_ids": ["ev-bd1a1d6f224cb9f2",
    "ev-5411f74c8ccead5d"], "external_issues": ["https://github.com/CultureBotAI/MediaIngredientMech/issues/718"],
    "field_paths": ["synonyms", "SSSOM.other"], "finding_id": "f-be91e29ea6694d28",
    "issue_key": "mim-reconciliation-exported-context-tokens-88ed3645c26c14b6", "owner_paths":
    [{"path": "data/ingredients/mapped/4-vinylphenol.yaml", "repository": "CultureBotAI/MediaIngredientMech",
    "role": "maintained ingredient"}], "severity": "major", "status": "open", "tags":
    ["reconciliation", "bundle-by-owner", "exported-context-tokens"], "target_ids":
    ["record-88ed3645c26c14b6"], "title": "Review nonportable exported tokens: 4-vinylphenol"}'
- evidence_id: ev-d8b130cb30e86aec
  kind: record_content
  reference: data/ingredients/mapped/4-vinylphenol.yaml
  locator: identifier, ontology_mapping, synonyms and curation_history
  accessed_at: '2026-10-11T03:08:52Z'
  support: partial
  summary: '{"candidate_labels": [{"source": "sssom_other_backfill", "synonym_text":
    "Trace minerals (see Medium No.151", "synonym_type": "RAW_TEXT"}, {"source": "sssom_other_backfill",
    "synonym_text": "Trace minerals(see Medium No.151)", "synonym_type": "RAW_TEXT"}],
    "history": [{"action": "CREATED_FROM_CAS_LOOKUP", "changes": "Created from CultureBotHT
    CAS-RN=2628-17-3; CHEBI resolved via OAK CHEBI sqlite (cas xref); Imported from
    CultureBotHT. CAS-RN\u2192CHEBI mapping resolved via OAK CHEBI sqlite (cas xref).
    ", "curator": "audit_cas_chebi_followup", "llm_assisted": false, "new_status":
    "MAPPED", "timestamp": "2026-04-29T06:34:31.158938+00:00"}, {"action": "AUTO_CLASSIFY_INGREDIENT_TYPE",
    "changes": "set ingredient_type=SINGLE_INGREDIENT (CHEBI primary)", "curator":
    "auto_classify_ingredient_type", "llm_assisted": false, "timestamp": "2026-05-01T07:35:31.933265+00:00"},
    {"action": "AUTO_BACKFILL_CHEBI_CHEMISTRY", "changes": "molecular_formula=C8H8O;
    inchi=InChI=1S/C8H8O/c1-2-7-3-5-8(9)6-4-7/h2-6,9H,1H2; smiles=C=Cc1ccc(O)cc1",
    "curator": "auto_classify_ingredient_type", "llm_assisted": false, "timestamp":
    "2026-05-01T08:08:27.759520+00:00"}, {"action": "AUTO_CLASSIFY_INGREDIENT_TYPE",
    "changes": "set ingredient_type=SINGLE_INGREDIENT (chemical structure populated
    (molecular_formula))", "curator": "auto_classify_ingredient_type", "llm_assisted":
    false, "timestamp": "2026-05-02T03:12:12.131604+00:00"}, {"action": "REGRADED_EXACT_TO_SYNONYM",
    "changes": "mapping_quality EXACT_MATCH -> SYNONYM_MATCH (#317). The record''s
    label does not equal the term''s primary label ''4-hydroxystyrene''; it matches
    the ChEBI synonym ''4-vinylphenol'' on CHEBI:1883. The schema defines EXACT_MATCH
    as a direct match to the term and SYNONYM_MATCH as a match to a known synonym,
    so the recorded grade overstated. ontology_id is unchanged \u2014 the term is
    correct. The SSSOM predicate is unaffected (both grades emit skos:exactMatch).",
    "curator": "regrade_synonym_matches", "llm_assisted": false, "timestamp": "2026-08-10T00:00:00+00:00"},
    {"action": "REGRADED_TO_CAS_RN_LOOKUP", "changes": "mapping_quality SYNONYM_MATCH
    -> CAS_RN_LOOKUP (#317). The record was created by an explicit CAS-to-ChEBI lookup
    and its current CAS RN 2628-17-3 uniquely resolves by ChEBI xref to CHEBI:1883
    ''4-hydroxystyrene''. CAS_RN_LOOKUP records the method that established this mapping;
    a lexical grade would discard that provenance. ontology_id is unchanged. The own-identifier
    SSSOM predicate remains skos:exactMatch under Rule D (#438), independently of
    mapping quality.", "curator": "regrade_synonym_matches", "llm_assisted": false,
    "timestamp": "2026-08-24T00:00:00+00:00"}, {"action": "ADDED_SYNONYMS", "changes":
    "Recovered 1 surface form(s) that the published SSSOM `other` carried but no curated
    record did, so a rebuild would have dropped them from KGX: ''Trace minerals (see
    Medium No.151''. Tokens already present on the kg-microbe ontology node were left
    out as redundant (#520).", "curator": "claude_sssom_surface_form_backfill", "llm_assisted":
    false, "timestamp": "2026-09-02T17:40:44.716277+00:00"}, {"action": "ADDED_SYNONYMS",
    "changes": "Recovered 1 surface form(s) that the published SSSOM `other` carried
    but no curated record did, so a rebuild would have dropped them from KGX: ''Trace
    minerals(see Medium No.151)''. Tokens already present on the kg-microbe ontology
    node were left out as redundant (#520).", "curator": "claude_sssom_surface_form_backfill",
    "llm_assisted": false, "timestamp": "2026-09-02T22:41:49.137449+00:00"}], "identifier":
    "CHEBI:1883", "mapping": {"evidence": [{"evidence_type": "DATABASE_MATCH", "notes":
    "Imported from CultureBotHT. CAS-RN\u2192CHEBI mapping resolved via OAK CHEBI
    sqlite (cas xref). ", "source": "CultureBotHT"}], "mapping_quality": "CAS_RN_LOOKUP",
    "ontology_id": "CHEBI:1883", "ontology_label": "4-hydroxystyrene", "ontology_source":
    "CHEBI"}}'
  snapshot_sha256: 8d4c406e24cbb343fb17cd6345b6628caf2e27ca07510c73c8ff2376a815c0f9
- evidence_id: ev-0de8553689e72bef
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:4-vinylphenol
  accessed_at: '2026-10-11T03:08:52Z'
  support: supports
  summary: '[{"comment": "", "confidence": "0.9", "data_row": 215, "mapping_date":
    "2026-09-02", "mapping_justification": "semapv:ManualMappingCuration", "object_id":
    "CHEBI:1883", "object_label": "4-hydroxystyrene", "object_source": "obo:chebi.owl",
    "other": "4-ethenylphenol|Trace minerals (see Medium No.151|Trace minerals(see
    Medium No.151)|CAS:2628-17-3", "predicate_id": "skos:exactMatch", "source": "MIM:CultureBotHT|MIM:curator=claude_sssom_surface_form_backfill|kgm:chebi_xrefs|kgm:mediadive_compounds|kgm:mediaingredientmech_reviewed|kgm:mediaingredientmech_reviewed[curator=audit_cas_chebi_followup]|kgm:mediaingredientmech_reviewed[curator=auto_classify_ingredient_type]|kgm:mediaingredientmech_reviewed[curator=regrade_synonym_matches]|kgm:primary_mappings[kegg_compound]",
    "subject_id": "MIM:4-vinylphenol", "subject_label": "4-vinylphenol", "validation_method":
    "OAK+OLS:chebi|CONFIRMED|2026-07-07"}]'
  snapshot_sha256: 2eae181f31d6433c20ffdb9dc2f8c8d7ad0a17a46a3189dea8c307fbc1c7b40e
- evidence_id: ev-93f74be01346ddd4
  kind: prior_review
  reference: reports/yaml_record_review/4-vinylphenol.md
  locator: Complete historical report, including Verdict and Recommended Edits
  accessed_at: '2026-10-11T03:08:52Z'
  support: context_only
  summary: Historical interpretation was read in full; it is not fresh source adjudication.
  snapshot_sha256: 2214bfc494f21e540ca4c95362b07f22597d870efc1ef0937d619d09bb58e1b8
  quote: "# `data/ingredients/mapped/4-vinylphenol.yaml`\n\n## Verdict\n\nNeeds curation,\
    \ major. The CAS-backed `CHEBI:1883` 4-hydroxystyrene identity,\nCAS, chemistry,\
    \ and SSSOM exact-match row pass, but two trace-minerals source\nlabels are stored\
    \ and exported as exact synonyms of the chemical.\n\n## Identity\n\n- Reviewed\
    \ record: `data/ingredients/mapped/4-vinylphenol.yaml`.\n- Identifier and grounding:\
    \ `identifier: CHEBI:1883` with\n  `ontology_mapping.ontology_id: CHEBI:1883`,\
    \ source `CHEBI`,\n  `mapping_quality: CAS_RN_LOOKUP`, and `mapping_status: MAPPED`.\n\
    - Official OLS/ChEBI check: `CHEBI:1883` is active and resolves to\n  `4-hydroxystyrene`.\n\
    - The current ChEBI page reports CAS `2628-17-3`, formula `C8H8O`, the stored\n\
    \  SMILES, and the stored InChI for `CHEBI:1883`.\n- `ingredient_type: SINGLE_INGREDIENT`\
    \ is present.\n\n## Validation\n\n- `uv run --frozen python scripts/validate_strict.py\
    \ data/ingredients/mapped/4-vinylphenol.yaml data/ingredients/mapped/4_Carbon_Mix.yaml\
    \ data/ingredients/mapped/4h-pyran-4-one.yaml data/ingredients/mapped/5-Aminolevulinic_Acid.yaml\
    \ data/ingredients/mapped/5-Azacytidine.yaml`:\n  passed; 5 files scanned, 0 ERROR\
    \ rows.\n- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/4-vinylphenol.yaml\
    \ -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord\
    \ --labels`:\n  passed.\n- `uv run --frozen python scripts/validate_component_partonomy.py`:\
    \ passed;\n  2951 records, 83 decompositions, 505 components, 0 violations.\n\n\
    ## Evidence\n\n- The active ChEBI term, CAS, formula, SMILES, InChI, and exact\
    \ synonym\n  `4-vinylphenol` support the CAS-based grounding to `CHEBI:1883`.\n\
    - The explicit CAS regrade is appropriate: the record was created through\n  CultureBotHT\
    \ CAS `2628-17-3` resolving by ChEBI xref to `CHEBI:1883`, so\n  `CAS_RN_LOOKUP`\
    \ preserves the mapping method better than a lexical grade.\n- The exact ChEBI\
    \ synonym `4-ethenylphenol` is acceptable.\n- Major: `Trace minerals (see Medium\
    \ No.151` and\n  `Trace minerals(see Medium No.151)` are media note fragments,\
    \ not names for\n  4-vinylphenol. They leak through the aggregate copy, SSSOM\
    \ `other`, generated\n  ingredient JSON, and generated `label_index` as synonyms\
    \ for `CHEBI:1883`.\n- The hidden/ignored-inclusive search over `data`, `mappings`,\
    \ `docs`,\n  `UNIFIED_INGREDIENT_MAPPING.tsv`, `src`, `scripts`, `tests`, `conf`,\n\
    \  `.github`, and `.claude` found the active YAML, aggregate copy, SSSOM row,\n\
    \  generated docs, row-review outputs, stale advisory rows, and ignored\n  aggregate\
    \ backups for this identifier and the bad trace-minerals strings.\n\n## Completeness\n\
    \n- CAS, formula, InChI, SMILES, `ingredient_type`, and the legitimate\n  `4-ethenylphenol`\
    \ exact synonym are populated.\n- No roles, components, environment, or discussion\
    \ entries need review.\n\n## Recommended Edits\n\n1. Remove or reject the two\
    \ `Trace minerals...` `RAW_TEXT` synonyms in\n   `data/ingredients/mapped/4-vinylphenol.yaml`\
    \ and\n   `data/curated/mapped_ingredients.yaml`, then regenerate SSSOM and docs\
    \ so\n   those medium-note fragments no longer publish as exact synonym labels.\n"
- evidence_id: ev-8fab9fb02ee4454f
  kind: prior_review
  reference: reviews/structured/20261011T024631Z-mim-reconcile-all-batch-03/review.yaml
  locator: findings[finding_id=f-e1004757f90e8c13]
  accessed_at: '2026-10-11T03:08:52Z'
  support: context_only
  summary: Exact earlier occurrence has open/confirmed status, based on exported-token
    presence and historical report text.
  snapshot_sha256: 6b3844c17bf3608ea8f73f824efec195e906ab8d2703fef4cd97fda04f0e65bf
  quote: '{"category": "nomenclature", "certainty": "confirmed", "description": "Historical
    tokens are still present on the exact-subject SSSOM rows: [{\"reason\":\"unresolved
    recipe cross-reference in a resolving synonym\",\"token\":\"Artificial seawater
    (see Medium No. 736 )\"},{\"reason\":\"unresolved recipe cross-reference in a
    resolving synonym\",\"token\":\"Artificial seawater (see below)\"}]. Truncated
    concentration strings and context-dependent instructions need scoped curation.
    This check does not reject catalog/RAW_TEXT synonyms as a class.", "evidence_ids":
    ["ev-a3370b8d14b4ebe5", "ev-91c2182d00c37a4a"], "external_issues": ["https://github.com/CultureBotAI/MediaIngredientMech/issues/718"],
    "field_paths": ["synonyms", "SSSOM.other"], "finding_id": "f-e1004757f90e8c13",
    "issue_key": "mim-reconciliation-exported-context-tokens-205c79d137874075", "owner_paths":
    [{"path": "data/ingredients/mapped/Artificial_seawater.yaml", "repository": "CultureBotAI/MediaIngredientMech",
    "role": "maintained ingredient"}], "severity": "major", "status": "open", "tags":
    ["reconciliation", "bundle-by-owner", "exported-context-tokens"], "target_ids":
    ["record-205c79d137874075"], "title": "Review nonportable exported tokens: Artificial
    seawater"}'
- evidence_id: ev-f5500c887f4dc734
  kind: record_content
  reference: data/ingredients/mapped/Artificial_seawater.yaml
  locator: identifier, ontology_mapping, synonyms and curation_history
  accessed_at: '2026-10-11T03:08:52Z'
  support: partial
  summary: '{"candidate_labels": [{"source": "culturemech:output/ingredient_occurrences.tsv",
    "synonym_text": "Artificial seawater (see below)", "synonym_type": "RAW_TEXT"},
    {"source": "culturemech:output/ingredient_occurrences.tsv", "synonym_text": "Artificial
    seawater (see Medium No. 736 )", "synonym_type": "RAW_TEXT"}], "history": [{"action":
    "CREATED_FROM_CULTUREMECH_RESIDUAL", "changes": "Created from a CultureMech recipe
    ingredient MIM held no record for (19 mentions across 19 recipes). Grounded to
    MICRO:0001715 (''artificial seawater'') on an exact match of the canonical label
    to the query ''Artificial seawater''. Source: culturemech:output/ingredient_occurrences.tsv.",
    "curator": "claude_culturemech_residual_grounding", "llm_assisted": false, "new_status":
    "MAPPED", "timestamp": "2026-08-30T10:35:03.361102+00:00"}, {"action": "ADDED_SYNONYMS",
    "changes": "Added 2 CultureMech recipe surface form(s) that folded onto this record''s
    published label but were absent from MIM''s label index, so CultureMech could
    not resolve them: ''Artificial seawater (see below)'' (x7 CultureMech mentions);
    ''Artificial seawater (see Medium No. 736 )'' (x1 CultureMech mentions). Source:
    culturemech:output/ingredient_occurrences.tsv.", "curator": "claude_culturemech_alias_backfill",
    "llm_assisted": false, "timestamp": "2026-08-30T10:41:26.546472+00:00"}, {"action":
    "CORRECTED", "changes": "Added ontology_mapping.evidence recording the CultureMech
    occurrence table as the source of this grounding. The provenance was already in
    this record''s CREATED_FROM_CULTUREMECH_RESIDUAL history entry but absent from
    the structured field the SSSOM builder reads, so a rebuild dropped MIM:culturemech:output/ingredient_occurrences.tsv
    from the published row (#541).", "curator": "claude_restore_culturemech_evidence",
    "llm_assisted": false, "timestamp": "2026-09-06T07:34:56.956907+00:00"}], "identifier":
    "MICRO:0001715", "mapping": {"evidence": [{"evidence_type": "LEXICAL_MATCH", "notes":
    "Surface form appears in CultureMech''s occurrence table and was grounded to MICRO:0001715
    on an exact match against the ontology label. Restored from the record''s own
    creation history (#541); the residual importer wrote this provenance only into
    the published SSSOM.", "source": "culturemech:output/ingredient_occurrences.tsv"}],
    "mapping_quality": "EXACT_MATCH", "match_level": "EXACT", "ontology_id": "MICRO:0001715",
    "ontology_label": "artificial seawater", "ontology_source": "MICRO"}}'
  snapshot_sha256: 9efeac859a634d9d5daf17c7da4e058b51ce7538b0b802fa6ac2b7f6f602e708
- evidence_id: ev-16c562c2dbdbab95
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Artificial_seawater
  accessed_at: '2026-10-11T03:08:52Z'
  support: supports
  summary: '[{"comment": "", "confidence": "0.99", "data_row": 435, "mapping_date":
    "2026-09-06", "mapping_justification": "semapv:LexicalMatching", "object_id":
    "MICRO:0001715", "object_label": "artificial seawater", "object_source": "obo:micro.owl",
    "other": "Artificial seawater (see below)|Artificial seawater (see Medium No.
    736 )", "predicate_id": "skos:exactMatch", "source": "MIM:culturemech:output/ingredient_occurrences.tsv|MIM:curator=claude_restore_culturemech_evidence",
    "subject_id": "MIM:Artificial_seawater", "subject_label": "Artificial seawater",
    "validation_method": "manual:claude_culturemech_residual_grounding|CREATED|2026-08-30"}]'
  snapshot_sha256: 2eae181f31d6433c20ffdb9dc2f8c8d7ad0a17a46a3189dea8c307fbc1c7b40e
- evidence_id: ev-8ca93b32516cbb52
  kind: prior_review
  reference: reports/yaml_record_review/Artificial_seawater.md
  locator: Complete historical report, including Verdict and Recommended Edits
  accessed_at: '2026-10-11T03:08:52Z'
  support: context_only
  summary: Historical interpretation was read in full; it is not fresh source adjudication.
  snapshot_sha256: 678c1882c36eb0a94f762d006e36deb3a61b751b7d424573a723abe497e8c936
  quote: "# `data/ingredients/mapped/Artificial_seawater.yaml`\n\n## Verdict\n\nPass.\
    \ The record exactly denotes MICRO `artificial seawater`, and its raw\nCultureMech\
    \ variants are retained only as source surface forms.\n\n## Identity\n\n- Reviewed\
    \ record: `data/ingredients/mapped/Artificial_seawater.yaml`.\n- Identifier and\
    \ grounding: `identifier: MICRO:0001715` with\n  `ontology_mapping.ontology_id:\
    \ MICRO:0001715`, `ontology_source: MICRO`,\n  `mapping_quality: EXACT_MATCH`,\
    \ `match_level: EXACT`, and\n  `mapping_status: MAPPED`.\n- OLS resolves `MICRO:0001715`\
    \ to non-obsolete `artificial seawater` with a\n  definition for an inorganic\
    \ salts solution that mimics sea water and the\n  exact synonym `synthetic seawater`.\n\
    - The two synonyms are raw CultureMech labels with parenthetical recipe\n  navigation\
    \ text; they are not asserted as exact ontology aliases.\n\n## Validation\n\n\
    - `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Arsenate.yaml\
    \ data/ingredients/mapped/Artepaulin.yaml data/ingredients/mapped/Artificial_Sea_Salt.yaml\
    \ data/ingredients/mapped/Artificial_seawater.yaml data/ingredients/mapped/Ascomycin.yaml`:\n\
    \  passed; 5 files scanned, 0 ERROR rows.\n- `uv run linkml-term-validator validate-data\
    \ data/ingredients/mapped/Artificial_seawater.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml\
    \ -t IngredientRecord --labels`:\n  failed in the MICRO sqlite adapter with `sqlite3.OperationalError:\
    \ no such\n  table: rdfs_label_statement`. This matches the repository contract:\n\
    \  `just validate-terms` skips MICRO and leaves it to Engine B/product\n  validation\
    \ or explicit OLS checks.\n- OLS4 lookup for `MICRO:0001715`: resolved the exact\
    \ stored term and label.\n- `uv run --frozen python scripts/validate_component_partonomy.py`:\
    \ passed;\n  2951 records, 83 decompositions, 505 components, 0 violations.\n\
    - `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules\n\
    \  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because\n\
    \  the sibling kg-microbe ontology transforms were absent.\n- `uv run --frozen\
    \ python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`:\n\
    \  passed; all id/label pairs corresponded and 104 non-blocking plausibility\n\
    \  warnings were reported.\n- `uv run --frozen python scripts/check_flat_export_coverage.py`:\
    \ passed; docs\n  data were fresh and every curated label was resolvable.\n\n\
    ## Evidence\n\n- `mappings/culturemech_residual_groundings.tsv` has the maintained\
    \ residual\n  decisions that folded `Artificial seawater`,\n  `Artificial seawater\
    \ (see below)`, `Artificial Seawater`, and\n  `Artificial seawater (see Medium\
    \ No. 736 )` to `MICRO:0001715`.\n- `mappings/ingredient_mappings.sssom.tsv` row\
    \ 482 maps\n  `MIM:Artificial_seawater` to `MICRO:0001715` with `skos:exactMatch`\
    \ and keeps\n  the two parenthetical strings in `other`.\n- A hidden, ignored-inclusive\
    \ search across the active checkout, excluding\n  stale `data/curated/backups`\
    \ and review output, found the same identity in\n  the per-record YAML, aggregate\
    \ YAML, SSSOM, CultureMech residual TSVs, and\n  generated docs products.\n\n\
    ## Completeness\n\n- Occurrence counts are populated: 19 total mentions across\
    \ 19 CultureMech\n  recipes.\n- The record correctly leaves components, roles,\
    \ environment, datasets, and\n  discussions empty; it is only publishing a resolved\
    \ CultureMech residual\n  ingredient and two raw label variants.\n- No CAS or\
    \ chemical structure fields are expected for this MICRO mixture.\n\n## Recommended\
    \ Edits\n\n- None.\n"
- evidence_id: ev-e6798c510d069e5f
  kind: prior_review
  reference: reviews/structured/20261011T024633Z-mim-reconcile-all-batch-05/review.yaml
  locator: findings[finding_id=f-838d67873b6673db]
  accessed_at: '2026-10-11T03:08:52Z'
  support: context_only
  summary: Exact earlier occurrence has open/confirmed status, based on exported-token
    presence and historical report text.
  snapshot_sha256: 7549030a5b50ed98868ff3497507fdfbfecd07cd858c76738f734521fa9d3603
  quote: '{"category": "nomenclature", "certainty": "confirmed", "description": "Historical
    tokens are still present on the exact-subject SSSOM rows: [{\"reason\":\"unresolved
    recipe cross-reference in a resolving synonym\",\"token\":\"DL vitamins (see below)\"}].
    Truncated concentration strings and context-dependent instructions need scoped
    curation. This check does not reject catalog/RAW_TEXT synonyms as a class.", "evidence_ids":
    ["ev-f2a088cb2fbda7be", "ev-ca75a3fbc1babe57"], "external_issues": ["https://github.com/CultureBotAI/MediaIngredientMech/issues/718"],
    "field_paths": ["synonyms", "SSSOM.other"], "finding_id": "f-838d67873b6673db",
    "issue_key": "mim-reconciliation-exported-context-tokens-9122c364d42e8559", "owner_paths":
    [{"path": "data/ingredients/mapped/DL_Vitamins.yaml", "repository": "CultureBotAI/MediaIngredientMech",
    "role": "maintained ingredient"}], "severity": "major", "status": "open", "tags":
    ["reconciliation", "bundle-by-owner", "exported-context-tokens"], "target_ids":
    ["record-9122c364d42e8559"], "title": "Review nonportable exported tokens: DL
    vitamins"}'
- evidence_id: ev-f0c42034b2f08a1d
  kind: record_content
  reference: data/ingredients/mapped/DL_Vitamins.yaml
  locator: identifier, ontology_mapping, synonyms and curation_history
  accessed_at: '2026-10-11T03:08:52Z'
  support: partial
  summary: '{"candidate_labels": [{"source": "culturemech:output/ingredient_occurrences.tsv",
    "synonym_text": "DL vitamins (see below)", "synonym_type": "RAW_TEXT"}], "history":
    [{"action": "CREATED_AS_UNMAPPED", "changes": "Imported from CultureBotHT (consolidated_media.json
    (media-only)). Used in 6 CultureBot media; samples: SCFM, Hans_Basal_Media, Hans_Basal_Media_plus_0.2x_20AA_mix\u2026.
    No CAS-RN or CHEBI mapping available; curator review needed.", "curator": "audit_add_remaining_culturebotht",
    "llm_assisted": false, "new_status": "UNMAPPED", "timestamp": "2026-04-29T06:51:33.117170+00:00"},
    {"action": "CLASSIFIED_STOCK_SOLUTION", "changes": "Classified as a vitamin stock/pre-mix
    and left unmapped pending component-level recipe curation.", "curator": "mediaingredientmech-agentic-curation",
    "llm_assisted": true, "new_status": "UNMAPPED", "previous_status": "UNMAPPED",
    "timestamp": "2026-05-11T09:30:00Z"}, {"action": "PROMOTED_TO_MAPPED", "changes":
    "Promoted UNMAPPED_0277 -> kgmicrobe.ingredient:dl_vitamins \"DL vitamins\" (FALLBACK_REGISTRY);
    mapping_status UNMAPPED -> MAPPED, SSSOM row added.", "curator": "promote_resolved_unmapped",
    "llm_assisted": false, "new_status": "MAPPED", "previous_status": "UNMAPPED",
    "timestamp": "2026-08-06T00:00:00+00:00"}, {"action": "ADDED_SYNONYMS", "changes":
    "Added 1 CultureMech recipe surface form(s) that folded onto this record''s published
    label but were absent from MIM''s label index, so CultureMech could not resolve
    them: ''DL vitamins (see below)'' (x1 CultureMech mentions). Source: culturemech:output/ingredient_occurrences.tsv.",
    "curator": "claude_culturemech_alias_backfill", "llm_assisted": false, "timestamp":
    "2026-08-30T04:48:06.233536+00:00"}, {"action": "ANNOTATED", "changes": "Transcribed
    the CultureBotHT Mixes-tab recipe for DL vitamins and added complete component
    partonomy for its 10 vitamin-stock constituents plus a source-backed vitamin role.",
    "curator": "mediaingredientmech-agentic-curation", "llm_assisted": true, "llm_model":
    "gpt-5", "new_status": "MAPPED", "timestamp": "2026-09-08T00:00:00+00:00"}], "identifier":
    "kgmicrobe.ingredient:dl_vitamins", "mapping": {"evidence": [{"evidence_type":
    "DATABASE_MATCH", "notes": "DL vitamins is a named, recurring multi-component
    preparation (6 media). Searched CHEBI, NCIT, MeSH, FOODON and ENVO by label and
    synonym with normalisation: no term denotes it, and none could -- it is a lab
    preparation rather than a substance. Takes the STOCK_SOLUTION convention used
    by the existing mapped records: a kgmicrobe.ingredient: mint, with no parent because
    a multi-component mix does not narrow to any single compound (#114).", "source":
    "MIM curation (#114)"}], "mapping_quality": "FALLBACK_REGISTRY", "ontology_id":
    "kgmicrobe.ingredient:dl_vitamins", "ontology_label": "DL vitamins", "ontology_source":
    "kgmicrobe.ingredient"}}'
  snapshot_sha256: 41a6ce40ee3f2a5a705f041f6d20d72ecd977a2dea42c477dc997191d1be44ad
- evidence_id: ev-82824a1888d907ee
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:DL_Vitamins
  accessed_at: '2026-10-11T03:08:52Z'
  support: supports
  summary: '[{"comment": "", "confidence": "0.9", "data_row": 993, "mapping_date":
    "2026-08-30", "mapping_justification": "semapv:ManualMappingCuration", "object_id":
    "kgmicrobe.ingredient:dl_vitamins", "object_label": "DL vitamins", "object_source":
    "kgm:ingredient", "other": "DL vitamins (see below)", "predicate_id": "skos:exactMatch",
    "source": "MIM:MIM curation (#114)|MIM:curator=claude_culturemech_alias_backfill",
    "subject_id": "MIM:DL_Vitamins", "subject_label": "DL vitamins", "validation_method":
    "none|UNKNOWN_TERM|2026-09-02"}]'
  snapshot_sha256: 2eae181f31d6433c20ffdb9dc2f8c8d7ad0a17a46a3189dea8c307fbc1c7b40e
- evidence_id: ev-0bef314ac38155d7
  kind: prior_review
  reference: reports/yaml_record_review/DL_Vitamins.md
  locator: Complete historical report, including Verdict and Recommended Edits
  accessed_at: '2026-10-11T03:08:52Z'
  support: context_only
  summary: Historical interpretation was read in full; it is not fresh source adjudication.
  snapshot_sha256: e5d9436f54deaa206abe6a293a0f86a784f0fc6406f2bf28ef415ba1ac7fe1b7
  quote: "# `data/ingredients/mapped/DL_Vitamins.yaml`\n\n## Verdict\n\nPass. `DL\
    \ vitamins` is modeled as a local kg-microbe stock solution rather than\nas one\
    \ vitamin compound, the CultureBotHT Mixes tab supports the ten listed\nvitamin\
    \ components and the vitamin-source role, and the final SSSOM row\npublishes only\
    \ a true same-stock source label in `other`.\n\n## Identity\n\n- Reviewed record:\
    \ `data/ingredients/mapped/DL_Vitamins.yaml`.\n- Identifier and grounding:\n \
    \ `identifier: kgmicrobe.ingredient:dl_vitamins` with the same\n  `ontology_mapping.ontology_id`,\
    \ source `kgmicrobe.ingredient`,\n  `mapping_quality: FALLBACK_REGISTRY`, and\
    \ `mapping_status: MAPPED`.\n- The local identity is appropriate because `DL vitamins`\
    \ is a named\n  multi-component CultureBotHT vitamin stock and the record's curation\
    \ evidence\n  documents searches of CHEBI, NCIT, MeSH, FOODON, and ENVO that found\
    \ no term\n  for the full preparation.\n- The record is typed as `ingredient_type:\
    \ STOCK_SOLUTION` and\n  `solution_type: VITAMIN_MIX`, so it does not collapse\
    \ the mix onto any single\n  component vitamin.\n\n## Validation\n\n- `uv run\
    \ --frozen python scripts/validate_strict.py data/ingredients/mapped/DL-Tyrosine.yaml\
    \ data/ingredients/mapped/DL-glyceraldehyde.yaml data/ingredients/mapped/DL_Vitamins.yaml\
    \ data/ingredients/mapped/DNA_From_Salmon.yaml data/ingredients/mapped/D_-carvone.yaml`:\n\
    \  passed; 5 files scanned, 0 ERROR rows.\n- `uv run --frozen linkml-term-validator\
    \ validate-data data/ingredients/mapped/DL-Tyrosine.yaml data/ingredients/mapped/DL-glyceraldehyde.yaml\
    \ data/ingredients/mapped/DL_Vitamins.yaml data/ingredients/mapped/DNA_From_Salmon.yaml\
    \ data/ingredients/mapped/D_-carvone.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml\
    \ -t IngredientRecord --labels`:\n  failed when non-OBO fallback targets were\
    \ included.\n- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/DL-Tyrosine.yaml\
    \ data/ingredients/mapped/DL-glyceraldehyde.yaml data/ingredients/mapped/D_-carvone.yaml\
    \ -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord\
    \ --labels`:\n  passed the 3-file ChEBI subset after skipping this\n  `kgmicrobe.ingredient:`\
    \ fallback and `DNA_From_Salmon`.\n- `uv run --frozen python scripts/validate_component_partonomy.py`:\
    \ passed in\n  the unchanged full-corpus validation run.\n- `uv run --frozen python\
    \ scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`:\n\
    \  passed; all id-label pairs corresponded, with full-corpus plausibility\n  warnings\
    \ only.\n- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed\
    \ Rules\n  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because\n\
    \  the sibling kg-microbe ontology transforms were absent.\n\n## Evidence\n\n\
    - The CultureBotHT Mixes CSV defines a 100X DL vitamins recipe with the ten\n\
    \  component rows recorded in YAML: d-Biotin `0.02 mg/L`, Folic Acid\n  `0.02\
    \ mg/L`, Pyridoxine HCl `0.1 mg/L`, Riboflavin `0.05 mg/L`,\n  Thiamine `0.05\
    \ mg/L`, Nicotinic Acid `0.05 mg/L`, Pantothenic Acid\n  `0.05 mg/L`, Vitamin\
    \ B12 `0.001 mg/L`, p-Amino Benzoic Acid `0.05 mg/L`,\n  and DL-6,8-thioctic acid\
    \ `0.05 mg/L`.\n- The `VITAMIN_SOURCE` role has `DATABASE_ENTRY` evidence scoped\
    \ to the same\n  Mixes tab, and the cited recipe is a vitamin premix.\n- The final\
    \ `mappings/ingredient_mappings.sssom.tsv` row maps\n  `MIM:DL_Vitamins` to `kgmicrobe.ingredient:dl_vitamins`\
    \ with\n  `skos:exactMatch`.\n- The final SSSOM `other` token `DL vitamins (see\
    \ below)` is a CultureMech\n  occurrence surface for this same stock solution\
    \ and is not an instruction or\n  non-identity note.\n\n## Completeness\n\n- The\
    \ hidden/ignored-inclusive exact-identifier search over active `data`,\n  `mappings`,\
    \ `docs`, `scripts`, and `tests` found no second primary record for\n  `kgmicrobe.ingredient:dl_vitamins`.\n\
    - The component assertion is marked `COMPLETE`, and all ten component IDs are\n\
    \  catalog references rather than external component-only identities.\n- No CAS,\
    \ formula, or ChEBI parent is required for the full stock mixture.\n\n## Recommended\
    \ Edits\n\n- None.\n"
- evidence_id: ev-9477d91976d0a888
  kind: prior_review
  reference: reviews/structured/20261011T024633Z-mim-reconcile-all-batch-05/review.yaml
  locator: findings[finding_id=f-320ccfb6bddc74ee]
  accessed_at: '2026-10-11T03:08:52Z'
  support: context_only
  summary: Exact earlier occurrence has open/confirmed status, based on exported-token
    presence and historical report text.
  snapshot_sha256: 7549030a5b50ed98868ff3497507fdfbfecd07cd858c76738f734521fa9d3603
  quote: '{"category": "nomenclature", "certainty": "confirmed", "description": "Historical
    tokens are still present on the exact-subject SSSOM rows: [{\"reason\":\"unresolved
    recipe cross-reference in a resolving synonym\",\"token\":\"Trace elements (see
    below)\"}]. Truncated concentration strings and context-dependent instructions
    need scoped curation. This check does not reject catalog/RAW_TEXT synonyms as
    a class.", "evidence_ids": ["ev-ee7e48ee832f8a11", "ev-42f981730201a7f4"], "external_issues":
    ["https://github.com/CultureBotAI/MediaIngredientMech/issues/718"], "field_paths":
    ["synonyms", "SSSOM.other"], "finding_id": "f-320ccfb6bddc74ee", "issue_key":
    "mim-reconciliation-exported-context-tokens-797da68010f27377", "owner_paths":
    [{"path": "data/ingredients/mapped/Desulfovibrio_Trace_Elements.yaml", "repository":
    "CultureBotAI/MediaIngredientMech", "role": "maintained ingredient"}], "severity":
    "major", "status": "open", "tags": ["reconciliation", "bundle-by-owner", "exported-context-tokens"],
    "target_ids": ["record-797da68010f27377"], "title": "Review nonportable exported
    tokens: Desulfovibrio trace elements"}'
- evidence_id: ev-4d30788725c98994
  kind: record_content
  reference: data/ingredients/mapped/Desulfovibrio_Trace_Elements.yaml
  locator: identifier, ontology_mapping, synonyms and curation_history
  accessed_at: '2026-10-11T03:08:52Z'
  support: partial
  summary: '{"candidate_labels": [{"source": "culturemech:output/ingredient_occurrences.tsv",
    "synonym_text": "Trace elements (see below)", "synonym_type": "RAW_TEXT"}], "history":
    [{"action": "CREATED_AS_UNMAPPED", "changes": "Imported from CultureBotHT (consolidated_media.json
    (media-only)). Used in 3 CultureBot media; samples: MoLS4, Dv_base_medium, MoLS4_no_vitamins.
    No CAS-RN or CHEBI mapping available; curator review needed.", "curator": "audit_add_remaining_culturebotht",
    "llm_assisted": false, "new_status": "UNMAPPED", "timestamp": "2026-04-29T06:51:33.117170+00:00"},
    {"action": "AUTO_UPGRADE_TO_MESH", "changes": "primary UNMAPPED_0294 \u2192 mesh:D014131
    (strategy=stem-match)", "curator": "resolve_unmapped_v2", "llm_assisted": false,
    "timestamp": "2026-05-02T03:18:21.917940+00:00"}, {"action": "ANNOTATED", "changes":
    "Added media role: TRACE_ELEMENT (confidence: 0.60)", "curator": "claude_in_session_curation",
    "timestamp": "2026-06-09T04:56:30.247868+00:00"}, {"action": "ANNOTATED", "changes":
    "Migrated legacy media_roles to role facets (#128): TRACE_ELEMENT -> nutritional_roles.TRACE_ELEMENT",
    "curator": "migrate_media_roles_to_facets", "timestamp": "2026-07-20T00:00:00+00:00"},
    {"action": "ADDED_SYNONYMS", "changes": "Added 1 CultureMech recipe surface form(s)
    that folded onto this record''s published label but were absent from MIM''s label
    index, so CultureMech could not resolve them: ''Trace elements (see below)'' (x1
    CultureMech mentions). Source: culturemech:output/ingredient_occurrences.tsv.",
    "curator": "claude_culturemech_alias_backfill", "llm_assisted": false, "timestamp":
    "2026-08-30T04:48:06.233536+00:00"}], "identifier": "mesh:D014131", "mapping":
    {"evidence": [{"evidence_type": "DATABASE_MATCH", "notes": "Auto-upgraded from
    UNMAPPED_0294; matched via ''Desulfovibrio trace elements''; stem-substring",
    "source": "MESH via OLS (resolve_unmapped_v2 strategy=stem-match)"}], "mapping_quality":
    "LEXICAL_MATCH", "ontology_id": "mesh:D014131", "ontology_label": "Trace Elements",
    "ontology_source": "MESH"}}'
  snapshot_sha256: 93db08d82a87268e9c970192268b222cd7f518ef64f468aeceea672e329a20ea
- evidence_id: ev-a255c9d3059064fe
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Desulfovibrio_Trace_Elements
  accessed_at: '2026-10-11T03:08:52Z'
  support: supports
  summary: '[{"comment": "", "confidence": "0.9", "data_row": 1021, "mapping_date":
    "2026-08-30", "mapping_justification": "semapv:LexicalMatching", "object_id":
    "mesh:D014131", "object_label": "Trace Elements", "object_source": "registry:mesh",
    "other": "Trace elements (see below)", "predicate_id": "skos:exactMatch", "source":
    "MIM:MESH via OLS (resolve_unmapped_v2 strategy=stem-match)|MIM:curator=claude_culturemech_alias_backfill",
    "subject_id": "MIM:Desulfovibrio_Trace_Elements", "subject_label": "Desulfovibrio
    trace elements", "validation_method": "none|UNKNOWN_TERM|2026-07-07"}]'
  snapshot_sha256: 2eae181f31d6433c20ffdb9dc2f8c8d7ad0a17a46a3189dea8c307fbc1c7b40e
- evidence_id: ev-e7674a969ec8d8cb
  kind: prior_review
  reference: reports/yaml_record_review/Desulfovibrio_Trace_Elements.md
  locator: Complete historical report, including Verdict and Recommended Edits
  accessed_at: '2026-10-11T03:08:52Z'
  support: context_only
  summary: Historical interpretation was read in full; it is not fresh source adjudication.
  snapshot_sha256: f655ff5e9d199deb38ad4e8e7e7ddb2aa844aecc6d1ec3efb037bbfade3e6aba
  quote: "# `data/ingredients/mapped/Desulfovibrio_Trace_Elements.yaml`\n\n## Verdict\n\
    \nNeeds curation. `mesh:D014131` is a valid MeSH term for the generic class\n\
    `Trace Elements`, but the MIM subject is a recipe-local\n`Desulfovibrio trace\
    \ elements` stock or reagent group. The current exactMatch\ntherefore erases specificity,\
    \ omits stock components, and publishes\n`Trace elements (see below)` as an unsafe\
    \ final SSSOM synonym.\n\n## Identity\n\n- Reviewed record:\n  `data/ingredients/mapped/Desulfovibrio_Trace_Elements.yaml`.\n\
    - Current grounding: `identifier: mesh:D014131` with\n  `ontology_mapping.ontology_id:\
    \ mesh:D014131`, label `Trace Elements`,\n  source `MESH`, `mapping_quality: LEXICAL_MATCH`,\
    \ and\n  `mapping_status: MAPPED`.\n- Live prefix-specific OLS resolves `mesh:D014131`\
    \ exactly to MeSH\n  `Trace Elements`, and a live exact MeSH search for\n  `Desulfovibrio\
    \ trace elements` returned no class.\n- The source label is a named Desulfovibrio\
    \ trace-elements preparation, not\n  the generic MeSH trace-element class. This\
    \ should be a local\n  `kgmicrobe.ingredient:desulfovibrio_trace_elements` identity\
    \ if no\n  formulation-specific ontology term exists.\n\n## Validation\n\n- `uv\
    \ run --frozen python scripts/validate_strict.py data/ingredients/mapped/Destomycin.yaml\
    \ data/ingredients/mapped/Desulfovibrio_Trace_Elements.yaml data/ingredients/mapped/Deuterated_Glucose.yaml\
    \ data/ingredients/mapped/Dextran.yaml data/ingredients/mapped/Dextrin.yaml`:\n\
    \  passed; 5 files scanned, 0 ERROR rows.\n- `uv run --frozen linkml-term-validator\
    \ validate-data ...` over the mixed\n  five-record batch aborted before the MeSH\
    \ record at the local\n  `kgmicrobe.compound:destomycin` registry identifier.\n\
    - `curl -L ... q=Trace Elements&ontology=mesh&exact=true`: live OLS returned\n\
    \  exact `mesh:D014131`.\n- `curl -L ... q=Desulfovibrio trace elements&ontology=mesh&exact=true`:\
    \ live\n  OLS returned 0 rows.\n- `uv run --frozen python scripts/validate_sssom_invariants.py`:\
    \ passed Rules\n  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped\
    \ because\n  the sibling kg-microbe ontology transforms were absent.\n- `uv run\
    \ --frozen python scripts/validate_component_partonomy.py`: passed;\n  the full\
    \ corpus had 2,951 records, 83 decompositions, 505 components, and 0\n  violations.\n\
    \n## Evidence\n\n- `mappings/ingredient_mappings_external_prefix_ols_validation.tsv`\
    \ confirms\n  that `mesh:D014131` resolves through prefix-specific OLS, but that\
    \ only\n  validates the target CURIE. It does not support treating a named\n \
    \ Desulfovibrio trace-element preparation as exact identity with the generic\n\
    \  MeSH class.\n- The hidden/ignored-inclusive exact search over `data/ingredients`,\n\
    \  `data/curated`, `mappings`, `docs/data`, `src`, and `scripts` found no\n  component\
    \ list for this stock record and no exact OLS hit for\n  `Desulfovibrio trace\
    \ elements`.\n- The final `mappings/ingredient_mappings.sssom.tsv` row maps\n\
    \  `MIM:Desulfovibrio_Trace_Elements` to `mesh:D014131` with\n  `skos:exactMatch`\
    \ and `Trace elements (see below)` in `other`. That `other`\n  token is a recipe-local\
    \ pointer, not a real synonym for the modeled MIM\n  subject.\n- `mappings/culturemech_residual_triage.tsv`\
    \ still carries\n  `Trace elements (see below)` as a stale unresolved alias even\
    \ though the\n  alias is now on this record and leaks into final SSSOM.\n- Major:\
    \ `nutritional_roles.TRACE_ELEMENT` is supported only by an in-session\n  `COMPUTATIONAL_PREDICTION`\
    \ role assignment and needs source-backed role\n  evidence if it is retained.\n\
    \n## Completeness\n\n- The occurrence count and raw source labels preserve the\
    \ legacy CultureBotHT\n  provenance: the record was created from `consolidated_media.json`,\
    \ used in 3\n  CultureBot media, and names `MoLS4`, `Dv_base_medium`, and\n  `MoLS4_no_vitamins`\
    \ as samples.\n- Major: the stock has no `components` or `component_assertion`,\
    \ so a reader\n  cannot recover which trace elements are meant.\n\n## Recommended\
    \ Edits\n\n- Major: retarget\n  `data/ingredients/mapped/Desulfovibrio_Trace_Elements.yaml`\
    \ to a local\n  stock identity such as\n  `kgmicrobe.ingredient:desulfovibrio_trace_elements`,\
    \ keep\n  `mesh:D014131` at most as a `NARROW_MATCH` parent, synchronize\n  `data/curated/mapped_ingredients.yaml`,\
    \ and regenerate SSSOM so a\n  registry/identity row is emitted beside the MeSH\
    \ parent row.\n- Major: add source-backed `components` and a `component_assertion`\
    \ from the\n  maintained CultureBotHT or CultureMech formulation evidence, or\
    \ document the\n  formulation as unresolved in `discussions` if the exact stock\
    \ recipe cannot\n  be recovered.\n- Major: remove `Trace elements (see below)`\
    \ from final SSSOM `other` by\n  demoting it out of active synonym export or by\
    \ proving it is a true alias for\n  this exact stock.\n- Major: source or remove\
    \ `nutritional_roles.TRACE_ELEMENT`.\n"
- evidence_id: ev-997c904ed0a9e395
  kind: prior_review
  reference: reviews/structured/20261011T024634Z-mim-reconcile-all-batch-06/review.yaml
  locator: findings[finding_id=f-853c7e2e707eedfc]
  accessed_at: '2026-10-11T03:08:52Z'
  support: context_only
  summary: Exact earlier occurrence has open/confirmed status, based on exported-token
    presence and historical report text.
  snapshot_sha256: 14c3200be95fdc87fca16bb71628432f3c9aaf8a65356ed494efc776ebe8aa11
  quote: '{"category": "nomenclature", "certainty": "confirmed", "description": "Historical
    tokens are still present on the exact-subject SSSOM rows: [{\"reason\":\"unresolved
    recipe cross-reference in a resolving synonym\",\"token\":\"Fatty acid mixture
    (see below)\"}]. Truncated concentration strings and context-dependent instructions
    need scoped curation. This check does not reject catalog/RAW_TEXT synonyms as
    a class.", "evidence_ids": ["ev-e116f44d24e1e32b", "ev-c4a82578b9a0228b"], "external_issues":
    ["https://github.com/CultureBotAI/MediaIngredientMech/issues/718"], "field_paths":
    ["synonyms", "SSSOM.other"], "finding_id": "f-853c7e2e707eedfc", "issue_key":
    "mim-reconciliation-exported-context-tokens-099e2c8a2a9f8f68", "owner_paths":
    [{"path": "data/ingredients/mapped/Fatty_Acid_Mixture_See_Medium_No_266.yaml",
    "repository": "CultureBotAI/MediaIngredientMech", "role": "maintained ingredient"}],
    "severity": "major", "status": "open", "tags": ["reconciliation", "bundle-by-owner",
    "exported-context-tokens"], "target_ids": ["record-099e2c8a2a9f8f68"], "title":
    "Review nonportable exported tokens: Fatty acid mixture (see Medium No. 266)"}'
- evidence_id: ev-66223de2980eb719
  kind: record_content
  reference: data/ingredients/mapped/Fatty_Acid_Mixture_See_Medium_No_266.yaml
  locator: identifier, ontology_mapping, synonyms and curation_history
  accessed_at: '2026-10-11T03:08:52Z'
  support: partial
  summary: '{"candidate_labels": [{"source": "culturemech:output/ingredient_occurrences.tsv",
    "synonym_text": "Fatty acid mixture (see below)", "synonym_type": "RAW_TEXT"}],
    "history": [{"action": "IMPORTED", "changes": "Initial import from CultureMech
    pipeline", "curator": "import_from_culturemech", "llm_assisted": false, "new_status":
    "MAPPED", "timestamp": "2026-03-09T06:54:18.022301+00:00"}, {"action": "ADDED_SYNONYMS",
    "changes": "Added 8 synonyms from kg-microbe P4.4 enrichment: Fatty acid, Fettsaeure,
    Fettsaeuren, acide gras, acides gras, ... (3 more)", "curator": "cbclaw_kg_microbe_sweep",
    "llm_assisted": true, "new_status": "MAPPED", "timestamp": "2026-04-18T00:00:00+00:00"},
    {"action": "AUTO_CLASSIFY_INGREDIENT_TYPE", "changes": "set ingredient_type=DEFINED_MEDIUM
    (name matches medium pattern ''Medium No'')", "curator": "auto_classify_ingredient_type",
    "llm_assisted": false, "timestamp": "2026-05-01T07:35:33.505726+00:00"}, {"action":
    "AUTO_BACKFILL_CHEBI_CHEMISTRY", "changes": "molecular_formula=CHO2R; smiles=*C(=O)O",
    "curator": "auto_classify_ingredient_type", "llm_assisted": false, "timestamp":
    "2026-05-01T08:08:29.482671+00:00"}, {"action": "CLASSIFY_AS_STOCK_SOLUTION",
    "changes": "name pattern ''see Medium No.'' indicates pre-mixed defined solution",
    "curator": "auto_classify_stock_solution", "llm_assisted": false, "timestamp":
    "2026-05-01T19:58:08.951391+00:00"}, {"action": "AUTO_CLASSIFY_INGREDIENT_TYPE",
    "changes": "set ingredient_type=SINGLE_INGREDIENT (chemical structure populated
    (molecular_formula))", "curator": "auto_classify_ingredient_type", "llm_assisted":
    false, "timestamp": "2026-05-02T03:12:14.341135+00:00"}, {"action": "CORRECTED",
    "changes": "ontology_label ''Fatty acid mixture (see Medium No. 266)'' -> ''fatty
    acid'': synced to canonical CHEBI label (preferred_term ''Fatty acid mixture (see
    Medium No. 266)'' unchanged).", "curator": "correct_stale_ontology_labels.py",
    "timestamp": "2026-06-09T05:23:46.762837+00:00"}, {"action": "CORRECTED", "changes":
    "occurrence_statistics 2/2 -> 4/4 (media_count/total_occurrences), derived from
    distinct CultureMech recipe ids in the #337 occurrence table. The prior values
    came from the importer retired in #453, whose media_count counted a list truncated
    to 50 examples (#449). [source=ingredient_occurrences.tsv culturemech_rev=15a4da5c08
    rows=194137 distinct_recipes=15257]", "curator": "refresh_occurrence_statistics",
    "timestamp": "2026-08-27T03:16:39.518810+00:00"}, {"action": "ADDED_SYNONYMS",
    "changes": "Added 2 CultureMech recipe surface form(s) that folded onto this record''s
    published label but were absent from MIM''s label index, so CultureMech could
    not resolve them: ''Fatty acid mixture'' (x3 CultureMech mentions); ''Fatty acid
    mixture (see below)'' (x1 CultureMech mentions). Source: culturemech:output/ingredient_occurrences.tsv.",
    "curator": "claude_culturemech_alias_backfill", "llm_assisted": false, "timestamp":
    "2026-08-30T04:48:06.233536+00:00"}], "identifier": "CHEBI:35366", "mapping":
    {"evidence": [{"evidence_type": "DATABASE_MATCH", "notes": "Imported from CultureMech
    pipeline, quality=DIRECT_MATCH", "source": "CultureMech"}], "mapping_quality":
    "EXACT_MATCH", "ontology_id": "CHEBI:35366", "ontology_label": "fatty acid", "ontology_source":
    "CHEBI"}}'
  snapshot_sha256: 00aa192a2ce2f4acb1b752d3a478ca4e661c8e15e2f0039c9b22b608a10a7e6c
- evidence_id: ev-6b0f037f5dc84aa9
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Fatty_Acid_Mixture_See_Medium_No_266
  accessed_at: '2026-10-11T03:08:52Z'
  support: supports
  summary: '[{"comment": "", "confidence": "0.99", "data_row": 1165, "mapping_date":
    "2026-08-30", "mapping_justification": "semapv:LexicalMatching", "object_id":
    "CHEBI:35366", "object_label": "fatty acid", "object_source": "obo:chebi.owl",
    "other": "Fettsaeure|Fettsaeuren|acide gras|acides gras|acido graso|acidos grasos|fatty
    acids|Fatty acid mixture|Fatty acid mixture (see below)", "predicate_id": "skos:exactMatch",
    "source": "MIM:CultureMech|MIM:curator=claude_culturemech_alias_backfill|kgm:chebi_xrefs|kgm:culturebotai_reviewed|kgm:mediaingredientmech_reviewed|kgm:mediaingredientmech_reviewed[curator=auto_classify_ingredient_type]|kgm:mediaingredientmech_reviewed[curator=auto_classify_stock_solution]|kgm:mediaingredientmech_reviewed[curator=cbclaw_kg_microbe_sweep]|kgm:mediaingredientmech_reviewed[curator=correct_stale_ontology_labels.py]|kgm:primary_mappings[kegg_compound]",
    "subject_id": "MIM:Fatty_Acid_Mixture_See_Medium_No_266", "subject_label": "Fatty
    acid mixture (see Medium No. 266)", "validation_method": "OAK+OLS:chebi|SYNONYM_ENRICH|2026-07-07"}]'
  snapshot_sha256: 2eae181f31d6433c20ffdb9dc2f8c8d7ad0a17a46a3189dea8c307fbc1c7b40e
- evidence_id: ev-abc54f67fc204f62
  kind: prior_review
  reference: reports/yaml_record_review/Fatty_Acid_Mixture_See_Medium_No_266.md
  locator: Complete historical report, including Verdict and Recommended Edits
  accessed_at: '2026-10-11T03:08:52Z'
  support: context_only
  summary: Historical interpretation was read in full; it is not fresh source adjudication.
  snapshot_sha256: 1699420fb78c42ed15355504b4a30c60190cf49a03fd7ce28b1129af4a0737dd
  quote: "# `data/ingredients/mapped/Fatty_Acid_Mixture_See_Medium_No_266.yaml`\n\n\
    ## Verdict\n\nNeeds curation, with major identity and final-SSSOM synonym issues.\
    \ The target\nChEBI term is the generic fatty acid class, while the MIM source\
    \ label denotes\na recipe-specific fatty acid mixture or stock, and mixture surface\
    \ forms are\npublished as exact `other` synonyms.\n\n## Identity\n\n- Reviewed\
    \ record:\n  `data/ingredients/mapped/Fatty_Acid_Mixture_See_Medium_No_266.yaml`.\n\
    - Identifier and grounding: `identifier: CHEBI:35366` with matching\n  `ontology_mapping.ontology_id`,\
    \ canonical label `fatty acid`, source\n  `CHEBI`, `mapping_quality: EXACT_MATCH`,\
    \ `mapping_status: MAPPED`, and\n  `ingredient_type: SINGLE_INGREDIENT`.\n- The\
    \ record has 4 CultureMech recipe occurrences, refreshed from the #337\n  occurrence\
    \ table.\n\n## Validation\n\n- `uv run --frozen python scripts/validate_strict.py\
    \ data/ingredients/mapped/Fastidious_Anaerobe_Broth_With_Meat_Granules.yaml data/ingredients/mapped/Fatty_Acid_Mixture_See_Medium_No_266.yaml\
    \ data/ingredients/mapped/Fe2_So43_X_N_H2o.yaml data/ingredients/mapped/Fe4_Po42.yaml\
    \ data/ingredients/mapped/Fe_Iii-edta.yaml --out /tmp/mim_fe_batch_strict.tsv`:\n\
    \  exited 0 for the 5-file batch; the output TSV contained only its header.\n\
    - `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Fatty_Acid_Mixture_See_Medium_No_266.yaml\
    \ data/ingredients/mapped/Fe4_Po42.yaml data/ingredients/mapped/Fe_Iii-edta.yaml\
    \ -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord\
    \ --labels`:\n  passed for the CHEBI-primary subset in this mixed batch.\n\n##\
    \ Evidence\n\n- The matching `data/curated/mapped_ingredients.yaml` entry carries\
    \ the same\n  ChEBI identifier, generic fatty-acid structure pattern, CultureMech\
    \ alias\n  backfill history, and occurrence counts as the per-record YAML.\n-\
    \ The final `mappings/ingredient_mappings.sssom.tsv` row maps\n  `MIM:Fatty_Acid_Mixture_See_Medium_No_266`\
    \ to `CHEBI:35366` with\n  `skos:exactMatch`.\n- Major: the preferred term says\
    \ this is a fatty acid mixture that references\n  Medium No. 266, but the record\
    \ asserts exact identity to the generic\n  `fatty acid` ChEBI class and overwrote\
    \ an earlier `STOCK_SOLUTION`\n  classification with `SINGLE_INGREDIENT`.\n- Major:\
    \ the final SSSOM `other` column exports `Fatty acid mixture` and\n  `Fatty acid\
    \ mixture (see below)`. Those are mixture or recipe-reference\n  surfaces, not\
    \ exact synonyms of CHEBI fatty acid.\n- A hidden/ignored-inclusive search over\
    \ `data/ingredients`, `data/curated`,\n  `mappings`, and `reports/yaml_record_review`\
    \ for\n  `MIM:Fatty_Acid_Mixture_See_Medium_No_266`, `CHEBI:35366`, and the fatty\n\
    \  acid mixture labels found the active YAML, aggregate copy, final SSSOM row,\n\
    \  row-review provenance, CultureMech residual alias rows, CultureMech recipe\n\
    \  memberships, and ignored aggregate backups.\n\n## Completeness\n\n- The CultureMech\
    \ occurrences are populated.\n- The exact identity, type, generic structure fields,\
    \ and final SSSOM synonyms\n  need repair before this row is semantically safe.\n\
    \n## Recommended Edits\n\n- Major: review the four CultureMech occurrences and\
    \ either mint a local\n  fatty-acid-mixture stock identity or link the label to\
    \ the concrete Medium\n  No. 266 mixture it references.\n- Major: if `CHEBI:35366`\
    \ is retained, downgrade it to a broader parent rather\n  than an exact identity,\
    \ remove the mixture labels from exact `other`\n  synonym export, choose the correct\
    \ `ingredient_type`, sync\n  `data/curated/mapped_ingredients.yaml`, regenerate\n\
    \  `mappings/ingredient_mappings.sssom.tsv`, and rerun strict validation plus\n\
    \  the final SSSOM invariant gates.\n"
- evidence_id: ev-b91360770608ed24
  kind: prior_review
  reference: reviews/structured/20261011T024636Z-mim-reconcile-all-batch-08/review.yaml
  locator: findings[finding_id=f-43e56706181e97b8]
  accessed_at: '2026-10-11T03:08:52Z'
  support: context_only
  summary: Exact earlier occurrence has open/confirmed status, based on exported-token
    presence and historical report text.
  snapshot_sha256: 4dd969b7020555cc2250a236d6fded134bedf3add1e1c5c72d269e98f9ae001b
  quote: '{"category": "nomenclature", "certainty": "confirmed", "description": "Historical
    tokens are still present on the exact-subject SSSOM rows: [{\"reason\":\"unresolved
    recipe cross-reference in a resolving synonym\",\"token\":\"Mineral solution (see
    Medium No. 976\"}]. Truncated concentration strings and context-dependent instructions
    need scoped curation. This check does not reject catalog/RAW_TEXT synonyms as
    a class.", "evidence_ids": ["ev-471a63cbca315ea9", "ev-63629b77a7cf13de"], "external_issues":
    ["https://github.com/CultureBotAI/MediaIngredientMech/issues/718"], "field_paths":
    ["synonyms", "SSSOM.other"], "finding_id": "f-43e56706181e97b8", "issue_key":
    "mim-reconciliation-exported-context-tokens-7059116102e92505", "owner_paths":
    [{"path": "data/ingredients/mapped/Mineral_Solution_See_Medium_No_976.yaml", "repository":
    "CultureBotAI/MediaIngredientMech", "role": "maintained ingredient"}], "severity":
    "major", "status": "open", "tags": ["reconciliation", "bundle-by-owner", "exported-context-tokens"],
    "target_ids": ["record-7059116102e92505"], "title": "Review nonportable exported
    tokens: Mineral solution see Medium No. 976"}'
- evidence_id: ev-423b314156ab28a8
  kind: record_content
  reference: data/ingredients/mapped/Mineral_Solution_See_Medium_No_976.yaml
  locator: identifier, ontology_mapping, synonyms and curation_history
  accessed_at: '2026-10-11T03:08:52Z'
  support: partial
  summary: '{"candidate_labels": [{"source": "culturemech:output/ingredient_occurrences.tsv",
    "synonym_text": "Mineral solution (see Medium No. 976", "synonym_type": "RAW_TEXT"}],
    "history": [{"action": "CREATED_AS_UNMAPPED", "changes": "Imported from mim-queue
    (source_id=mediadive.ingredient:1958); no CAS-RN or CHEBI/NCIT match. Curator
    review needed.", "curator": "audit_import_ingredients[mim-queue]", "llm_assisted":
    false, "new_status": "UNMAPPED", "timestamp": "2026-04-30T18:43:03.698454+00:00"},
    {"action": "CLASSIFY_AS_STOCK_SOLUTION", "changes": "name pattern ''see Medium
    No.'' indicates pre-mixed defined solution", "curator": "auto_classify_stock_solution",
    "llm_assisted": false, "timestamp": "2026-05-01T19:58:07.078790+00:00"}, {"action":
    "AUTO_CLASSIFY_INGREDIENT_TYPE", "changes": "set ingredient_type=STOCK_SOLUTION
    (name matches solution pattern ''Mineral solution'')", "curator": "auto_classify_ingredient_type",
    "llm_assisted": false, "timestamp": "2026-05-02T03:12:19.749949+00:00"}, {"action":
    "PROMOTED_TO_MAPPED", "changes": "Promoted UNMAPPED_0447 -> kgmicrobe.ingredient:mineral_solution_see_medium_no_976
    (FALLBACK_REGISTRY). A named multi-component preparation. Searched CHEBI, NCIT,
    MeSH, FOODON and ENVO by label and synonym: no term denotes it, and none could
    -- a preparation is not a substance. Takes the STOCK_SOLUTION convention: a kgmicrobe.ingredient:
    mint with no parent, because a multi-component mix does not narrow to any single
    compound (#288).", "curator": "issue_288_stock_solutions", "llm_assisted": true,
    "new_status": "MAPPED", "previous_status": "UNMAPPED", "timestamp": "2026-08-06T00:00:00+00:00"},
    {"action": "FLAGGED_NEEDS_EXPERT", "changes": "Reverted the mint and flagged NEEDS_EXPERT
    instead. \"Mineral solution see Medium No. 976\" is a CROSS-REFERENCE to another
    medium, not the name of a substance -- minting an identifier for it would give
    a pointer its own identity. The #288 batch minted it because it filtered on ingredient_type
    STOCK_SOLUTION without reading the label. The referenced medium should be resolved
    and this record either replaced by that mineral solution or retired (#288).",
    "curator": "issue_288_stock_solutions", "llm_assisted": true, "new_status": "NEEDS_EXPERT",
    "previous_status": "MAPPED", "timestamp": "2026-08-06T00:00:00+00:00"}, {"action":
    "ANNOTATED", "changes": "Edison LITERATURE (PaperQA3) identity research; report
    at research/ingredients/Mineral_Solution_See_Medium_No_976-edison-literature.md
    (local artifact \u2014 research/ is gitignored, so the findings are quoted here
    rather than linked). Report reached no single bolded verdict; see the report.
    No ontology CURIE was proposed. Recorded as provenance only \u2014 no grounding
    applied from this run. Edison''s recommendations are deliberately conservative,
    and a plausible identifier promoted by a mechanism that never decided anything
    is what #203 and #263 exist to undo. Any CURIE above is a curator''s to accept
    or reject.", "curator": "edison_literature_identity", "llm_assisted": true, "timestamp":
    "2026-08-06T00:00:00+00:00"}, {"action": "PROMOTED_TO_MAPPED", "changes": "UNMAPPED_0447
    -> kgmicrobe.ingredient:mineral_solution_see_medium_no_976 (FALLBACK_REGISTRY).
    Minted under the #288 STOCK_SOLUTION convention: a MediaDive cross-reference to
    the mineral/trace-elements solution of DSMZ Medium 976. The corpus already treats
    this shape as a stock solution rather than retiring it \u2014 `Trace element solution
    see Medium No. 187` and `Vitamin solution see Medium No. 403` are both live kgmicrobe.ingredient
    mints under the #288 convention \u2014 so this follows its siblings. The composition
    is not transcribed here: it lives in the referenced medium, and #288''s rule is
    to mint the named preparation rather than inline someone else''s recipe.", "curator":
    "retire_assay_labels", "llm_assisted": false, "new_status": "MAPPED", "previous_status":
    "NEEDS_EXPERT", "timestamp": "2026-08-15T00:00:00+00:00"}, {"action": "ADDED_SYNONYMS",
    "changes": "Added 1 CultureMech recipe surface form(s) that folded onto this record''s
    published label but were absent from MIM''s label index, so CultureMech could
    not resolve them: ''Mineral solution (see Medium No. 976'' (x1 CultureMech mentions).
    Source: culturemech:output/ingredient_occurrences.tsv.", "curator": "claude_culturemech_alias_backfill",
    "llm_assisted": false, "timestamp": "2026-08-30T04:48:06.233536+00:00"}], "identifier":
    "kgmicrobe.ingredient:mineral_solution_see_medium_no_976", "mapping": {"evidence":
    [{"evidence_type": "MANUAL_CURATION", "notes": "Minted under the #288 STOCK_SOLUTION
    convention: a MediaDive cross-reference to the mineral/trace-elements solution
    of DSMZ Medium 976. The corpus already treats this shape as a stock solution rather
    than retiring it \u2014 `Trace element solution see Medium No. 187` and `Vitamin
    solution see Medium No. 403` are both live kgmicrobe.ingredient mints under the
    #288 convention \u2014 so this follows its siblings. The composition is not transcribed
    here: it lives in the referenced medium, and #288''s rule is to mint the named
    preparation rather than inline someone else''s recipe.", "source": "MIM curation
    (#213/#308)"}], "mapping_quality": "FALLBACK_REGISTRY", "ontology_id": "kgmicrobe.ingredient:mineral_solution_see_medium_no_976",
    "ontology_label": "Mineral solution see Medium No. 976", "ontology_source": "kgmicrobe.ingredient"}}'
  snapshot_sha256: 911de800edd62dc119f74d48432257ba1f22c2be95ebeb37f8e79385aecdd238
- evidence_id: ev-f25801a7e385fb14
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Mineral_Solution_See_Medium_No_976
  accessed_at: '2026-10-11T03:08:52Z'
  support: supports
  summary: '[{"comment": "", "confidence": "0.9", "data_row": 1881, "mapping_date":
    "2026-08-30", "mapping_justification": "semapv:ManualMappingCuration", "object_id":
    "kgmicrobe.ingredient:mineral_solution_see_medium_no_976", "object_label": "Mineral
    solution see Medium No. 976", "object_source": "kgm:ingredient", "other": "Mineral
    solution (see Medium No. 976", "predicate_id": "skos:exactMatch", "source": "MIM:MIM
    curation (#213/#308)|MIM:curator=claude_culturemech_alias_backfill", "subject_id":
    "MIM:Mineral_Solution_See_Medium_No_976", "subject_label": "Mineral solution see
    Medium No. 976", "validation_method": "manual:retire_assay_labels|PROMOTED|2026-08-15"}]'
  snapshot_sha256: 2eae181f31d6433c20ffdb9dc2f8c8d7ad0a17a46a3189dea8c307fbc1c7b40e
- evidence_id: ev-5458c3c3defc38d0
  kind: prior_review
  reference: reports/yaml_record_review/Mineral_Solution_See_Medium_No_976.md
  locator: Complete historical report, including Verdict and Recommended Edits
  accessed_at: '2026-10-11T03:08:52Z'
  support: context_only
  summary: Historical interpretation was read in full; it is not fresh source adjudication.
  snapshot_sha256: 75b5bf9ce1cf58d7f737fc163464400e4c8e6f66d2e610e439c0594b1e71c1bb
  quote: "# `data/ingredients/mapped/Mineral_Solution_See_Medium_No_976.yaml`\n\n\
    ## Verdict\n\nNeeds curation. The local DSMZ Medium 976 mineral-solution cross-reference,\n\
    fallback registry mapping, #213/#308 remapping, and final exact row pass, but\
    \ a\nmalformed open-parenthesis surface still publishes in final SSSOM `other`.\n\
    \nSeverity: major.\n\n## Identity\n\n- Reviewed record:\n  `data/ingredients/mapped/Mineral_Solution_See_Medium_No_976.yaml`.\n\
    - Identifier and grounding:\n  `identifier: kgmicrobe.ingredient:mineral_solution_see_medium_no_976`\
    \ with\n  `ontology_mapping.ontology_id:\n  kgmicrobe.ingredient:mineral_solution_see_medium_no_976`,\
    \ source\n  `kgmicrobe.ingredient`, `mapping_quality: FALLBACK_REGISTRY`,\n  `mapping_status:\
    \ MAPPED`, and `ingredient_type: STOCK_SOLUTION`.\n- Occurrences: the record carries\
    \ a stale 0/0 occurrence count even though the\n  2026-08-30 alias backfill and\
    \ residual triage both record one CultureMech\n  mention of its malformed surface.\n\
    \n## Validation\n\n- `uv run --frozen python scripts/validate_strict.py` on the\
    \ 5-file batch from\n  `Mineral_3B_Solution_Minus_Phosphorus` through `Minerals`:\
    \ exited 0 and\n  wrote zero ERROR rows.\n- Direct Engine A term validation was\
    \ skipped for this local registry record\n  because its primary `kgmicrobe.ingredient`\
    \ identifier is outside the OBO\n  subset used for the batch.\n\n## Evidence\n\
    \n- `mappings/unmapped_ingredients_ols_exact_audit.tsv` recorded no exact OLS\
    \ hit\n  before the fallback registry promotion.\n- The #213/#308 curation reaccepted\
    \ a local identifier for this MediaDive\n  cross-reference under the #288 stock-solution\
    \ convention used by its\n  existing cross-reference siblings.\n- A fresh exact\
    \ EBI OLS4 lookup returned no same-label external class.\n- The final SSSOM publishes\
    \ one `skos:exactMatch` row from\n  `MIM:Mineral_Solution_See_Medium_No_976` to\n\
    \  `kgmicrobe.ingredient:mineral_solution_see_medium_no_976`.\n\n## Completeness\n\
    \n- The local fallback identity and final exact row agree.\n- The final SSSOM\
    \ `other` field still exports\n  `Mineral solution (see Medium No. 976`, which\
    \ is an unbalanced raw\n  CultureMech parse artifact rather than a clean synonym.\n\
    - The 0/0 occurrence count is stale relative to the x1 CultureMech mention\n \
    \ that was recovered by the alias backfill.\n\n## Recommended Edits\n\n- Major:\
    \ mark `Mineral solution (see Medium No. 976` as `REJECTED_LABEL`, or\n  otherwise\
    \ keep it out of final SSSOM `other` while preserving it only as a\n  resolver\
    \ alias if needed.\n- Minor: refresh `occurrence_statistics` from the post-alias\
    \ CultureMech\n  occurrence table so the record no longer reports 0/0.\n"
- evidence_id: ev-a1a7bf32cb2806bb
  kind: prior_review
  reference: reviews/structured/20261011T024636Z-mim-reconcile-all-batch-08/review.yaml
  locator: findings[finding_id=f-d3696f2daf45c433]
  accessed_at: '2026-10-11T03:08:52Z'
  support: context_only
  summary: Exact earlier occurrence has open/confirmed status, based on exported-token
    presence and historical report text.
  snapshot_sha256: 4dd969b7020555cc2250a236d6fded134bedf3add1e1c5c72d269e98f9ae001b
  quote: '{"category": "nomenclature", "certainty": "confirmed", "description": "Historical
    tokens are still present on the exact-subject SSSOM rows: [{\"reason\":\"unresolved
    recipe cross-reference in a resolving synonym\",\"token\":\"Modified trace vitamins
    (see below)\"}]. Truncated concentration strings and context-dependent instructions
    need scoped curation. This check does not reject catalog/RAW_TEXT synonyms as
    a class.", "evidence_ids": ["ev-a8586fb48ab7ffa9", "ev-e485d8da83247c1c"], "external_issues":
    ["https://github.com/CultureBotAI/MediaIngredientMech/issues/718"], "field_paths":
    ["synonyms", "SSSOM.other"], "finding_id": "f-d3696f2daf45c433", "issue_key":
    "mim-reconciliation-exported-context-tokens-4253636d94bcf2f1", "owner_paths":
    [{"path": "data/ingredients/mapped/Modified_Trace_Vitamins.yaml", "repository":
    "CultureBotAI/MediaIngredientMech", "role": "maintained ingredient"}], "severity":
    "major", "status": "open", "tags": ["reconciliation", "bundle-by-owner", "exported-context-tokens"],
    "target_ids": ["record-4253636d94bcf2f1"], "title": "Review nonportable exported
    tokens: Modified trace vitamins"}'
- evidence_id: ev-5830b871d91efa8c
  kind: record_content
  reference: data/ingredients/mapped/Modified_Trace_Vitamins.yaml
  locator: identifier, ontology_mapping, synonyms and curation_history
  accessed_at: '2026-10-11T03:08:52Z'
  support: partial
  summary: '{"candidate_labels": [{"source": "culturemech:output/ingredient_occurrences.tsv",
    "synonym_text": "Modified trace vitamins (see below)", "synonym_type": "RAW_TEXT"}],
    "history": [{"action": "CREATED_AS_UNMAPPED", "changes": "Imported from mim-queue
    (source_id=mediadive.ingredient:2017); no CAS-RN or CHEBI/NCIT match. Curator
    review needed.", "curator": "audit_import_ingredients[mim-queue]", "llm_assisted":
    false, "new_status": "UNMAPPED", "timestamp": "2026-04-30T18:43:03.698454+00:00"},
    {"action": "CLASSIFIED_STOCK_SOLUTION", "changes": "Classified as a modified trace
    vitamin stock mixture and left unmapped pending component list and formulation-specific
    curation.", "curator": "mediaingredientmech-agentic-curation", "llm_assisted":
    true, "new_status": "UNMAPPED", "previous_status": "UNMAPPED", "timestamp": "2026-05-11T08:03:00Z"},
    {"action": "PROMOTED_TO_MAPPED", "changes": "Promoted UNMAPPED_0452 -> kgmicrobe.ingredient:modified_trace_vitamins
    (FALLBACK_REGISTRY). A named multi-component preparation. Searched CHEBI, NCIT,
    MeSH, FOODON and ENVO by label and synonym: no term denotes it, and none could
    -- a preparation is not a substance. Takes the STOCK_SOLUTION convention: a kgmicrobe.ingredient:
    mint with no parent, because a multi-component mix does not narrow to any single
    compound (#288).", "curator": "issue_288_stock_solutions", "llm_assisted": true,
    "new_status": "MAPPED", "previous_status": "UNMAPPED", "timestamp": "2026-08-06T00:00:00+00:00"},
    {"action": "CORRECTED", "changes": "occurrence_statistics 0/0 -> 2/2 (media_count/total_occurrences),
    derived from distinct CultureMech recipe ids in the #337 occurrence table. The
    prior values came from the importer retired in #453, whose media_count counted
    a list truncated to 50 examples (#449). [source=ingredient_occurrences.tsv culturemech_rev=15a4da5c08
    rows=194137 distinct_recipes=15257]", "curator": "refresh_occurrence_statistics",
    "timestamp": "2026-08-27T03:16:39.520286+00:00"}, {"action": "ADDED_SYNONYMS",
    "changes": "Added 1 CultureMech recipe surface form(s) that folded onto this record''s
    published label but were absent from MIM''s label index, so CultureMech could
    not resolve them: ''Modified trace vitamins (see below)'' (x1 CultureMech mentions).
    Source: culturemech:output/ingredient_occurrences.tsv.", "curator": "claude_culturemech_alias_backfill",
    "llm_assisted": false, "timestamp": "2026-08-30T04:48:06.233536+00:00"}], "identifier":
    "kgmicrobe.ingredient:modified_trace_vitamins", "mapping": {"evidence": [{"evidence_type":
    "MANUAL_CURATION", "notes": "A named multi-component preparation. Searched CHEBI,
    NCIT, MeSH, FOODON and ENVO by label and synonym: no term denotes it, and none
    could -- a preparation is not a substance. Takes the STOCK_SOLUTION convention:
    a kgmicrobe.ingredient: mint with no parent, because a multi-component mix does
    not narrow to any single compound (#288).", "source": "MIM curation (#288)"}],
    "mapping_quality": "FALLBACK_REGISTRY", "ontology_id": "kgmicrobe.ingredient:modified_trace_vitamins",
    "ontology_label": "Modified trace vitamins", "ontology_source": "kgmicrobe.ingredient"}}'
  snapshot_sha256: 4eedaddb0efbc29c6dead6ef2bd378ec59070ecea3146b66e77bcea55a204a2c
- evidence_id: ev-7c6192e7f288bdf0
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Modified_Trace_Vitamins
  accessed_at: '2026-10-11T03:08:52Z'
  support: supports
  summary: '[{"comment": "", "confidence": "0.9", "data_row": 1903, "mapping_date":
    "2026-08-30", "mapping_justification": "semapv:ManualMappingCuration", "object_id":
    "kgmicrobe.ingredient:modified_trace_vitamins", "object_label": "Modified trace
    vitamins", "object_source": "kgm:ingredient", "other": "Modified trace vitamins
    (see below)", "predicate_id": "skos:exactMatch", "source": "MIM:MIM curation (#288)|MIM:curator=claude_culturemech_alias_backfill",
    "subject_id": "MIM:Modified_Trace_Vitamins", "subject_label": "Modified trace
    vitamins", "validation_method": "none|UNKNOWN_TERM|2026-09-02"}]'
  snapshot_sha256: 2eae181f31d6433c20ffdb9dc2f8c8d7ad0a17a46a3189dea8c307fbc1c7b40e
- evidence_id: ev-1659306e55f45a0b
  kind: prior_review
  reference: reports/yaml_record_review/Modified_Trace_Vitamins.md
  locator: Complete historical report, including Verdict and Recommended Edits
  accessed_at: '2026-10-11T03:08:52Z'
  support: context_only
  summary: Historical interpretation was read in full; it is not fresh source adjudication.
  snapshot_sha256: 1bfc880ed06f1c6448af8e81cef6be73c4e8dfc3230d00e4ab8241c3de76ee7d
  quote: "# `data/ingredients/mapped/Modified_Trace_Vitamins.yaml`\n\n## Verdict\n\
    \nNeeds curation. The local Modified trace vitamins stock identity, occurrence\n\
    count, fallback registry mapping, and final exact row pass, but `see below`\n\
    recipe text still publishes in final SSSOM `other`.\n\nSeverity: major.\n\n##\
    \ Identity\n\n- Reviewed record: `data/ingredients/mapped/Modified_Trace_Vitamins.yaml`.\n\
    - Identifier and grounding:\n  `identifier: kgmicrobe.ingredient:modified_trace_vitamins`\
    \ with\n  `ontology_mapping.ontology_id:\n  kgmicrobe.ingredient:modified_trace_vitamins`,\
    \ source\n  `kgmicrobe.ingredient`, `mapping_quality: FALLBACK_REGISTRY`,\n  `mapping_status:\
    \ MAPPED`, and `ingredient_type: STOCK_SOLUTION`.\n- Occurrences: two CultureMech\
    \ recipe occurrences.\n\n## Validation\n\n- `uv run --frozen python scripts/validate_strict.py`\
    \ on the 5-file batch from\n  `Mnso4_X_7_H2o` through `Modified_Trace_Vitamins`:\
    \ exited 0 and wrote zero\n  ERROR rows.\n- Direct Engine A term validation was\
    \ skipped for this local registry record\n  because its primary `kgmicrobe.ingredient`\
    \ identifier is outside the OBO\n  subset used for the batch.\n\n## Evidence\n\
    \n- `mappings/unmapped_ingredients_ols_exact_audit.tsv` recorded no exact OLS\
    \ hit\n  before the fallback registry promotion.\n- #288 curation kept this as\
    \ a local mint because the label denotes a named\n  multi-component vitamin preparation\
    \ rather than an external ontology\n  substance.\n- A fresh exact EBI OLS4 lookup\
    \ returned no same-label external class.\n- The final SSSOM publishes one `skos:exactMatch`\
    \ row from\n  `MIM:Modified_Trace_Vitamins` to the local registry identifier.\n\
    \n## Completeness\n\n- The local stock identity, 2/2 occurrence count, fallback\
    \ registry rationale,\n  and final exact row agree.\n- The final SSSOM `other`\
    \ field still exports `Modified trace vitamins (see\n  below)`, which is recipe\
    \ navigation text rather than a clean synonym.\n\n## Recommended Edits\n\n- Major:\
    \ mark `Modified trace vitamins (see below)` as `REJECTED_LABEL`, or\n  otherwise\
    \ preserve it only as a resolver alias while filtering it from final\n  SSSOM\
    \ `other`.\n"
- evidence_id: ev-54e6930eaaa55145
  kind: prior_review
  reference: reviews/structured/20261011T024637Z-mim-reconcile-all-batch-09/review.yaml
  locator: findings[finding_id=f-5982691d4b3d176b]
  accessed_at: '2026-10-11T03:08:52Z'
  support: context_only
  summary: Exact earlier occurrence has open/confirmed status, based on exported-token
    presence and historical report text.
  snapshot_sha256: cf46750874f1303863883723934bbe8b09ece8d62b1785ceab64bb0342a3cf11
  quote: '{"category": "nomenclature", "certainty": "confirmed", "description": "Historical
    tokens are still present on the exact-subject SSSOM rows: [{\"reason\":\"truncated
    concentration-qualified label with unbalanced parentheses\",\"token\":\"Peptone
    (0.01 %\"}]. Truncated concentration strings and context-dependent instructions
    need scoped curation. This check does not reject catalog/RAW_TEXT synonyms as
    a class.", "evidence_ids": ["ev-8ead32467e428cda", "ev-4f5362bb32478943"], "external_issues":
    ["https://github.com/CultureBotAI/MediaIngredientMech/issues/718"], "field_paths":
    ["synonyms", "SSSOM.other"], "finding_id": "f-5982691d4b3d176b", "issue_key":
    "mim-reconciliation-exported-context-tokens-62f485f9f7517526", "owner_paths":
    [{"path": "data/ingredients/mapped/Peptone.yaml", "repository": "CultureBotAI/MediaIngredientMech",
    "role": "maintained ingredient"}], "severity": "major", "status": "open", "tags":
    ["reconciliation", "bundle-by-owner", "exported-context-tokens"], "target_ids":
    ["record-62f485f9f7517526"], "title": "Review nonportable exported tokens: Peptone"}'
- evidence_id: ev-0bdc1c0fd578d2ef
  kind: record_content
  reference: data/ingredients/mapped/Peptone.yaml
  locator: identifier, ontology_mapping, synonyms and curation_history
  accessed_at: '2026-10-11T03:08:52Z'
  support: partial
  summary: '{"candidate_labels": [{"source": "microbedecoder", "synonym_text": "Peptone
    (0.01 %", "synonym_type": "RAW_TEXT"}], "history": [{"action": "AUTO_CREATE_FROM_MICRO",
    "changes": "created with primary MICRO:0000178", "curator": "foodon_pass", "llm_assisted":
    false, "timestamp": "2026-05-01T19:55:09.679469+00:00"}, {"action": "AUTO_CLASSIFY_INGREDIENT_TYPE",
    "changes": "set ingredient_type=UNDEFINED_MIXTURE (name matches complex pattern
    ''Peptone'')", "curator": "auto_classify_ingredient_type", "llm_assisted": false,
    "timestamp": "2026-05-02T03:12:17.686332+00:00"}, {"action": "ANNOTATED", "changes":
    "Added media role: PROTEIN_SOURCE (confidence: 0.80)", "curator": "infer_roles_from_name_lists",
    "timestamp": "2026-06-03T02:06:01.747135+00:00"}, {"action": "CORRECTED", "changes":
    "Backfilled missing occurrence_statistics (0/0): ontology-derived record with
    no tracked media occurrences.", "curator": "audit_occurrence_stats", "timestamp":
    "2026-06-08T23:23:58.335580+00:00"}, {"action": "ANNOTATED", "changes": "Migrated
    legacy media_roles to role facets (#128): PROTEIN_SOURCE -> nutritional_roles.PROTEIN_SOURCE",
    "curator": "migrate_media_roles_to_facets", "timestamp": "2026-07-20T00:00:00+00:00"},
    {"action": "MERGED_FROM_UNMAPPED_DUPLICATE", "changes": "Absorbed UNMAPPED_0718
    ''Peptones'' as a RAW_TEXT synonym -- plural of the already-mapped peptone record.
    No new SSSOM row; MICRO:0000178 is already mapped. Source: kgmicrobe.compound:peptones.",
    "curator": "microbedecoder-residual-dispositions", "llm_assisted": true, "timestamp":
    "2026-08-05T00:01:30.894952+00:00"}, {"action": "MERGED_FROM_UNMAPPED_DUPLICATE",
    "changes": "Absorbed UNMAPPED_0835 ''Peptone (0.01 %'' as a RAW_TEXT synonym --
    concentration-truncated duplicate of peptone. No new SSSOM row; MICRO:0000178
    is already mapped. Source: kgmicrobe.trait:peptone_0_01.", "curator": "microbedecoder-residual-dispositions",
    "llm_assisted": true, "timestamp": "2026-08-05T00:01:30.894952+00:00"}, {"action":
    "CORRECTED", "changes": "occurrence_statistics 0/0 -> 2251/2255 (media_count/total_occurrences),
    derived from distinct CultureMech recipe ids in the #337 occurrence table. The
    prior values came from the importer retired in #453, whose media_count counted
    a list truncated to 50 examples (#449). [source=ingredient_occurrences.tsv culturemech_rev=15a4da5c08
    rows=194137 distinct_recipes=15257]", "curator": "refresh_occurrence_statistics",
    "timestamp": "2026-08-27T03:16:39.519680+00:00"}], "identifier": "MICRO:0000178",
    "mapping": {"evidence": [{"evidence_type": "DATABASE_MATCH", "notes": "Auto-created
    from foodon_pass; label-exact (micro)", "source": "MICRO via OLS search"}], "mapping_quality":
    "EXACT_MATCH", "ontology_id": "MICRO:0000178", "ontology_label": "peptone", "ontology_source":
    "MICRO"}}'
  snapshot_sha256: e00551197758fb417846becc5c14e931f614bc00887609b8749d734ad2f8d4aa
- evidence_id: ev-a926e5411d840793
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Peptone
  accessed_at: '2026-10-11T03:08:52Z'
  support: supports
  summary: '[{"comment": "", "confidence": "0.99", "data_row": 2220, "mapping_date":
    "2026-08-27", "mapping_justification": "semapv:LexicalMatching", "object_id":
    "MICRO:0000178", "object_label": "peptone", "object_source": "obo:micro.owl",
    "other": "Peptones|Peptone (0.01 %", "predicate_id": "skos:exactMatch", "source":
    "MIM:MICRO via OLS search|MIM:curator=refresh_occurrence_statistics", "subject_id":
    "MIM:Peptone", "subject_label": "Peptone", "validation_method": "none|UNKNOWN_TERM|2026-07-07"}]'
  snapshot_sha256: 2eae181f31d6433c20ffdb9dc2f8c8d7ad0a17a46a3189dea8c307fbc1c7b40e
- evidence_id: ev-f56ebea344bcd264
  kind: prior_review
  reference: reports/yaml_record_review/Peptone.md
  locator: Complete historical report, including Verdict and Recommended Edits
  accessed_at: '2026-10-11T03:08:52Z'
  support: context_only
  summary: Historical interpretation was read in full; it is not fresh source adjudication.
  snapshot_sha256: ff7ee8ae08e2406bcca09345d75c8024a56f48457839ff026e9bf007b4f2e4fe
  quote: "# `data/ingredients/mapped/Peptone.yaml`\n\n## Verdict\n\nNeeds curation;\
    \ major. The generic Peptone identity resolves to\n`MICRO:0000178`, but the `PROTEIN_SOURCE`\
    \ role is only a provisional name-list\nprediction and final SSSOM exports a concentration-truncated\
    \ raw synonym.\n\n## Identity\n\n- Reviewed record: `data/ingredients/mapped/Peptone.yaml`.\n\
    - Identifier and grounding: `identifier: MICRO:0000178` with\n  `ontology_mapping.ontology_id:\
    \ MICRO:0000178`, label `peptone`, source\n  `MICRO`, `mapping_quality: EXACT_MATCH`,\
    \ `mapping_status: MAPPED`, and\n  `ingredient_type: UNDEFINED_MIXTURE`.\n- Occurrences:\
    \ 2,255 total occurrences across 2,251 CultureMech recipes, plus\n  48 MicrobeDecoder\
    \ `BacDive_Metabolite_utilization` occurrences.\n\n## Validation\n\n- `uv run\
    \ --frozen python scripts/validate_strict.py` exited 0 across this\n  five-record\
    \ batch and wrote zero ERROR rows.\n- A fresh prefix-specific OLS4 search resolves\
    \ `MICRO:0000178` to `peptone`.\n- `mappings/ingredient_mappings_unknown_term_triage.tsv`\
    \ classifies the final\n  SSSOM `UNKNOWN_TERM` grade as a missing-prefix validator\
    \ coverage issue, not\n  as a bad term.\n- The final SSSOM row was inspected directly\
    \ and maps `MIM:Peptone` exactly to\n  `MICRO:0000178`.\n\n## Evidence\n\n- The\
    \ MICRO primary identifier and mapping target denote peptone.\n- `Peptones` is\
    \ a harmless plural raw synonym from a reviewed MicrobeDecoder\n  duplicate merge.\n\
    - Major: `Peptone (0.01 %` is a concentration-truncated source string, not a\n\
    \  real peptone synonym, but final SSSOM exports it in `other`.\n- Major: the\
    \ `PROTEIN_SOURCE` role is supported only by\n  `COMPUTATIONAL_PREDICTION` evidence\
    \ from `infer_roles_from_name_lists`.\n\n## Completeness\n\n- The exact MICRO\
    \ identity is complete enough.\n- Role evidence and the final synonym surface\
    \ remain incomplete while the\n  provisional nutritional role and concentration-truncated\
    \ `other` token are\n  still present.\n\n## Recommended Edits\n\n- Major: in `data/ingredients/mapped/Peptone.yaml`,\
    \ retype or suppress\n  `Peptone (0.01 %` so it remains occurrence provenance\
    \ only and no longer\n  appears in `mappings/ingredient_mappings.sssom.tsv`.\n\
    - Major: replace `nutritional_roles.PROTEIN_SOURCE` with source-backed\n  evidence\
    \ or remove the provisional role facet until it is curated.\n"
- evidence_id: ev-8bb59eaf8b6e66f4
  kind: prior_review
  reference: reviews/structured/20261011T024638Z-mim-reconcile-all-batch-10/review.yaml
  locator: findings[finding_id=f-f582ea830b4f370d]
  accessed_at: '2026-10-11T03:08:52Z'
  support: context_only
  summary: Exact earlier occurrence has open/confirmed status, based on exported-token
    presence and historical report text.
  snapshot_sha256: 8c3aa2fca1269d1dbbf6117e85dea5b0de5047a8505841641245bd7ee99b936d
  quote: '{"category": "nomenclature", "certainty": "confirmed", "description": "Historical
    tokens are still present on the exact-subject SSSOM rows: [{\"reason\":\"unresolved
    recipe cross-reference in a resolving synonym\",\"token\":\"Potassium phosphate
    buffer* (see below)\"}]. Truncated concentration strings and context-dependent
    instructions need scoped curation. This check does not reject catalog/RAW_TEXT
    synonyms as a class.", "evidence_ids": ["ev-afd6d431ee989359", "ev-8ff94a6ea1085255"],
    "external_issues": ["https://github.com/CultureBotAI/MediaIngredientMech/issues/718"],
    "field_paths": ["synonyms", "SSSOM.other"], "finding_id": "f-f582ea830b4f370d",
    "issue_key": "mim-reconciliation-exported-context-tokens-4190c0ee5976447a", "owner_paths":
    [{"path": "data/ingredients/mapped/Potassium_Phosphate_Buffer.yaml", "repository":
    "CultureBotAI/MediaIngredientMech", "role": "maintained ingredient"}], "severity":
    "major", "status": "open", "tags": ["reconciliation", "bundle-by-owner", "exported-context-tokens"],
    "target_ids": ["record-4190c0ee5976447a"], "title": "Review nonportable exported
    tokens: Potassium phosphate buffer"}'
- evidence_id: ev-745bc0e8e18adc16
  kind: record_content
  reference: data/ingredients/mapped/Potassium_Phosphate_Buffer.yaml
  locator: identifier, ontology_mapping, synonyms and curation_history
  accessed_at: '2026-10-11T03:08:52Z'
  support: partial
  summary: '{"candidate_labels": [{"source": "culturemech:output/ingredient_occurrences.tsv",
    "synonym_text": "Potassium phosphate buffer* (see below)", "synonym_type": "RAW_TEXT"}],
    "history": [{"action": "CREATED_AS_UNMAPPED", "changes": "Imported from CultureBotHT
    (consolidated_media.json (media-only)). Used in 2 CultureBot media; samples: Mega,
    TYG. No CAS-RN or CHEBI mapping available; curator review needed.", "curator":
    "audit_add_remaining_culturebotht", "llm_assisted": false, "new_status": "UNMAPPED",
    "timestamp": "2026-04-29T06:51:33.117170+00:00"}, {"action": "AUTO_CLASSIFY_INGREDIENT_TYPE",
    "changes": "set ingredient_type=STOCK_SOLUTION (name matches solution pattern
    ''phosphate buffer'')", "curator": "auto_classify_ingredient_type", "llm_assisted":
    false, "timestamp": "2026-05-02T03:12:19.854401+00:00"}, {"action": "AUTO_UPGRADE_TO_NCIT",
    "changes": "primary UNMAPPED_0274 \u2192 NCIT:C29321 (strategy=stem-match)", "curator":
    "resolve_unmapped_v2", "llm_assisted": false, "timestamp": "2026-05-02T03:18:21.960132+00:00"},
    {"action": "CORRECTED", "changes": "Changed identifier from NCIT:C29321 to kgmicrobe.ingredient:potassium_phosphate_buffer
    and retained NCIT:C29321 only as CLOSE_MATCH. Potassium phosphate buffer is a
    formulation variant, not identical to the generic phosphate buffer class.", "curator":
    "ingredient_mapping_review_2026_05_05", "llm_assisted": false, "new_status": "MAPPED",
    "previous_status": "MAPPED", "timestamp": "2026-05-05T00:00:00+00:00"}, {"action":
    "ANNOTATED", "changes": "Added media role: BUFFER (confidence: 0.80)", "curator":
    "infer_roles_from_name_lists", "timestamp": "2026-06-03T02:06:01.748066+00:00"},
    {"action": "ANNOTATED", "changes": "Migrated legacy media_roles to role facets
    (#128): BUFFER -> physicochemical_roles.BUFFER", "curator": "migrate_media_roles_to_facets",
    "timestamp": "2026-07-20T00:00:00+00:00"}, {"action": "CORRECTED", "changes":
    "occurrence_statistics 2/2 -> 44/44 (media_count/total_occurrences), derived from
    distinct CultureMech recipe ids in the #337 occurrence table. The prior values
    came from the importer retired in #453, whose media_count counted a list truncated
    to 50 examples (#449). [source=ingredient_occurrences.tsv culturemech_rev=15a4da5c08
    rows=194137 distinct_recipes=15257]", "curator": "refresh_occurrence_statistics",
    "timestamp": "2026-08-27T03:16:39.519736+00:00"}, {"action": "ADDED_SYNONYMS",
    "changes": "Added 4 CultureMech recipe surface form(s) that folded onto this record''s
    published label but were absent from MIM''s label index, so CultureMech could
    not resolve them: ''Potassium phosphate buffer (0.01 M, pH 7.2)'' (x1 CultureMech
    mentions); ''Potassium phosphate buffer (0.02 M, pH 7.0)'' (x1 CultureMech mentions);
    ''Potassium phosphate buffer (1 M, pH 7.1)'' (x1 CultureMech mentions); ''Potassium
    phosphate buffer* (see below)'' (x1 CultureMech mentions). Source: culturemech:output/ingredient_occurrences.tsv.",
    "curator": "claude_culturemech_alias_backfill", "llm_assisted": false, "timestamp":
    "2026-08-30T04:48:06.233536+00:00"}], "identifier": "kgmicrobe.ingredient:potassium_phosphate_buffer",
    "mapping": {"evidence": [{"evidence_type": "CURATOR_JUDGMENT", "notes": "Potassium
    phosphate buffer is a formulation variant, not identical to the generic phosphate
    buffer class.", "source": "ingredient_mapping_review_2026-05-05"}], "mapping_quality":
    "CLOSE_MATCH", "ontology_id": "NCIT:C29321", "ontology_label": "Phosphate Buffer",
    "ontology_source": "NCIT"}}'
  snapshot_sha256: 9a33ce5d93f8928878ab1309f834d49f505d27abf4d5ee41e23b79a40a2ac40e
- evidence_id: ev-7d01fe3478491965
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Potassium_Phosphate_Buffer
  accessed_at: '2026-10-11T03:08:52Z'
  support: supports
  summary: '[{"comment": "", "confidence": "0.9", "data_row": 2327, "mapping_date":
    "2026-08-30", "mapping_justification": "semapv:ManualMappingCuration", "object_id":
    "NCIT:C29321", "object_label": "Phosphate Buffer", "object_source": "obo:ncit.owl",
    "other": "Potassium phosphate buffer (0.01 M, pH 7.2)|Potassium phosphate buffer
    (0.02 M, pH 7.0)|Potassium phosphate buffer (1 M, pH 7.1)|Potassium phosphate
    buffer* (see below)", "predicate_id": "skos:closeMatch", "source": "MIM:ingredient_mapping_review_2026-05-05|MIM:curator=claude_culturemech_alias_backfill",
    "subject_id": "MIM:Potassium_Phosphate_Buffer", "subject_label": "Potassium phosphate
    buffer", "validation_method": "none|UNKNOWN_TERM|2026-07-07"}, {"comment": "Registry/identity
    row preserving kgmicrobe.ingredient:potassium_phosphate_buffer alongside parent
    NCIT:C29321.", "confidence": "0.99", "data_row": 2328, "mapping_date": "2026-08-30",
    "mapping_justification": "semapv:ManualMappingCuration", "object_id": "kgmicrobe.ingredient:potassium_phosphate_buffer",
    "object_label": "Potassium phosphate buffer", "object_source": "kgm:ingredient",
    "other": "", "predicate_id": "skos:exactMatch", "source": "MIM:ingredient_mapping_review_2026-05-05|MIM:curator=claude_culturemech_alias_backfill",
    "subject_id": "MIM:Potassium_Phosphate_Buffer", "subject_label": "Potassium phosphate
    buffer", "validation_method": "none|UNKNOWN_TERM|2026-07-07"}]'
  snapshot_sha256: 2eae181f31d6433c20ffdb9dc2f8c8d7ad0a17a46a3189dea8c307fbc1c7b40e
- evidence_id: ev-a692d3e165ce1613
  kind: prior_review
  reference: reports/yaml_record_review/Potassium_Phosphate_Buffer.md
  locator: Complete historical report, including Verdict and Recommended Edits
  accessed_at: '2026-10-11T03:08:52Z'
  support: context_only
  summary: Historical interpretation was read in full; it is not fresh source adjudication.
  snapshot_sha256: 884a3c1ac80ea7503bc943cac7d9eef7ff8d329cc1b7da000b75ab605e4019e0
  quote: '# `data/ingredients/mapped/Potassium_Phosphate_Buffer.yaml`


    **Verdict**: needs curation, major issue.


    **Identity**: `Potassium phosphate buffer` is preserved as the local exact identity
    `kgmicrobe.ingredient:potassium_phosphate_buffer` with a `CLOSE_MATCH` parent
    row to `NCIT:C29321` / `Phosphate Buffer`. That row shape correctly avoids equating
    a potassium-buffer formulation family with the generic NCIT phosphate-buffer class.


    **Validation**: `uv run --frozen python scripts/validate_strict.py ... Potassium_Phosphate_Buffer.yaml
    ...` passed for the 5-file batch with 0 ERROR rows. `uv run --frozen linkml-term-validator
    validate-data data/ingredients/mapped/Potassium_Phosphate_Buffer.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml
    -t IngredientRecord --labels` passed.


    **Evidence**: The 2026-05-05 curation event supports keeping the local exact identity
    plus NCIT close row, and final SSSOM rows 2401 and 2402 preserve both surfaces.
    However, row 2401 still exports concentration- and pH-qualified recipe text, plus
    `Potassium phosphate buffer* (see below)`, as `other` synonyms. Those labels are
    formulation-specific recipe surfaces, not general names for the exact local registry
    subject. The active `physicochemical_roles.BUFFER` assertion is still only a `COMPUTATIONAL_PREDICTION`
    from the `infer_roles_from_name_lists` rule with the curator note `Provisional
    role from a curated name-pattern rule; review recommended.`


    **Completeness**: The record has 44 source occurrences and the correct local identity
    shape, but it has no component or concentration model that can represent the distinct
    0.01 M, 0.02 M, and 1 M pH-specific formulations now living as raw synonyms. An
    ignored/hidden local search over `data/ingredients`, `data/curated`, `mappings`,
    `reports`, `scripts`, `src`, `tests`, `docs`, and `UNIFIED_INGREDIENT_MAPPING.tsv`
    found the expected final NCIT close row, local exact row, and corresponding Sodium_Potassium_Phosphate_Buffer
    sibling pattern.


    **Recommended Edits**: In `data/ingredients/mapped/Potassium_Phosphate_Buffer.yaml`,
    move the pH- and molarity-qualified labels out of active synonyms or teach the
    SSSOM builder to filter them from `other`. Replace the provisional `BUFFER` role
    with source-backed evidence or remove it, and add component/concentration recipes
    if a source can define each buffer formulation. Synchronize `data/curated/mapped_ingredients.yaml`,
    regenerate SSSOM, and rerun strict validation plus `scripts/validate_sssom_invariants.py`.

    '
- evidence_id: ev-032b61a7a21ed47b
  kind: prior_review
  reference: reviews/structured/20261011T024638Z-mim-reconcile-all-batch-10/review.yaml
  locator: findings[finding_id=f-b7808e84d7886285]
  accessed_at: '2026-10-11T03:08:52Z'
  support: context_only
  summary: Exact earlier occurrence has open/confirmed status, based on exported-token
    presence and historical report text.
  snapshot_sha256: 8c3aa2fca1269d1dbbf6117e85dea5b0de5047a8505841641245bd7ee99b936d
  quote: '{"category": "nomenclature", "certainty": "confirmed", "description": "Historical
    tokens are still present on the exact-subject SSSOM rows: [{\"reason\":\"unresolved
    recipe cross-reference in a resolving synonym\",\"token\":\"Riboflavin (see below)\"}].
    Truncated concentration strings and context-dependent instructions need scoped
    curation. This check does not reject catalog/RAW_TEXT synonyms as a class.", "evidence_ids":
    ["ev-b92552c1f537a179", "ev-659fa61b579bfe7b"], "external_issues": ["https://github.com/CultureBotAI/MediaIngredientMech/issues/718"],
    "field_paths": ["synonyms", "SSSOM.other"], "finding_id": "f-b7808e84d7886285",
    "issue_key": "mim-reconciliation-exported-context-tokens-59776f859c41300d", "owner_paths":
    [{"path": "data/ingredients/mapped/Riboflavin.yaml", "repository": "CultureBotAI/MediaIngredientMech",
    "role": "maintained ingredient"}], "severity": "major", "status": "open", "tags":
    ["reconciliation", "bundle-by-owner", "exported-context-tokens"], "target_ids":
    ["record-59776f859c41300d"], "title": "Review nonportable exported tokens: Riboflavin"}'
- evidence_id: ev-d59510b4ad4c4456
  kind: record_content
  reference: data/ingredients/mapped/Riboflavin.yaml
  locator: identifier, ontology_mapping, synonyms and curation_history
  accessed_at: '2026-10-11T03:08:52Z'
  support: partial
  summary: '{"candidate_labels": [{"source": "culturemech:output/ingredient_occurrences.tsv",
    "synonym_text": "Riboflavin (see below)", "synonym_type": "RAW_TEXT"}], "history":
    [{"action": "IMPORTED", "changes": "Initial import from CultureMech pipeline",
    "curator": "import_from_culturemech", "llm_assisted": false, "new_status": "MAPPED",
    "timestamp": "2026-03-09T06:54:18.022301+00:00"}, {"action": "ADDED_CAS_RN", "changes":
    "Added CAS-RN:83-88-5 from PubChem API via name lookup (Riboflavin)", "curator":
    "fetch_cas_rn_from_pubchem", "llm_assisted": false, "new_status": "MAPPED", "timestamp":
    "2026-04-05T19:53:48.746601+00:00"}, {"action": "ADDED_CAS_RN", "changes": "Added
    CAS-RN:83-88-5 from CultureBotHT compounds_to_cas.csv (matched: riboflavin)",
    "curator": "fetch_cas_rn_from_culturebot_csv", "llm_assisted": false, "new_status":
    "MAPPED", "timestamp": "2026-04-05T21:48:45.703391+00:00"}, {"action": "CAS_RN_ADDED",
    "changes": "Added CAS-RN 83-88-5 from PubChem (via CHEBI:17015)", "curator": "enrich_mim_cas_rn_batch",
    "llm_assisted": false, "new_status": "MAPPED", "timestamp": "2026-04-09T00:32:50.689620+00:00"},
    {"action": "ADDED_SYNONYMS", "changes": "Added 20 synonyms from kg-microbe P4.4
    enrichment: 1-deoxy-1-(7,8-dimethyl-2,4-dioxo-3,4-dihydrobenzo[g]pteridin-10(2H)-yl)-D-ribitol,
    1-deoxy-1-(7,8-dimethyl-2,4-dioxo-3,4-dihydrobenzo[g]pteridin-10(2H)-yl)pentitol,
    5-deoxy-5-(7,8-dimethyl-2,4-dioxo-3,4-dihydrobenzo[g]pteridin-10(2H)-yl)-D-ribitol,
    6,7-dimethyl-9-D-ribitylisoalloxazine, 7,8-dimethyl-10-(D-ribo-2,3,4,5-tetrahydroxypentyl)benzo[g]pteridine-2,4(3H,10H)-dione,
    ... (15 more)", "curator": "cbclaw_kg_microbe_sweep", "llm_assisted": true, "new_status":
    "MAPPED", "timestamp": "2026-04-18T00:00:00+00:00"}, {"action": "MERGED_FROM_DUPLICATES",
    "changes": "Absorbed 2 duplicate MIM record(s) into this one: Riboflavine.yaml,
    Riboflavin_2.yaml. Synonyms, curation_history, and occurrence counts were unioned/summed;
    winner selected by highest occurrence count with preferred_term readability tie-break.",
    "curator": "audit_mim_merge", "llm_assisted": false, "new_status": "MAPPED", "timestamp":
    "2026-04-19T07:39:23.955331+00:00"}, {"action": "AUTO_CLASSIFY_INGREDIENT_TYPE",
    "changes": "set ingredient_type=SINGLE_INGREDIENT (CHEBI primary)", "curator":
    "auto_classify_ingredient_type", "llm_assisted": false, "timestamp": "2026-05-01T07:35:36.069178+00:00"},
    {"action": "AUTO_BACKFILL_CHEBI_CHEMISTRY", "changes": "molecular_formula=C17H20N4O6;
    inchi=InChI=1S/C17H20N4O6/c1-7-3-9-10(4-8(7)2)21(5-11(23; smiles=Cc1cc2nc3c(=O)nc(=O)nc-3n(C[C@H](O)[C@H](O)[C@H](O",
    "curator": "auto_classify_ingredient_type", "llm_assisted": false, "timestamp":
    "2026-05-01T08:08:32.160107+00:00"}, {"action": "APPLY_EVIDENCE_PROPOSAL", "changes":
    "added pmid=40609532 from propose-evidence batch", "curator": "auto_classify_ingredient_type",
    "llm_assisted": false, "timestamp": "2026-05-01T08:09:48.123437+00:00"}, {"action":
    "AUTO_CLASSIFY_INGREDIENT_TYPE", "changes": "set ingredient_type=SINGLE_INGREDIENT
    (chemical structure populated (molecular_formula))", "curator": "auto_classify_ingredient_type",
    "llm_assisted": false, "timestamp": "2026-05-02T03:12:18.114359+00:00"}, {"action":
    "ANNOTATED", "changes": "Added media role: VITAMIN_SOURCE (confidence: 1.00)",
    "curator": "extract_roles_from_synonyms", "timestamp": "2026-05-29T23:35:36.112742+00:00"},
    {"action": "CORRECTED", "changes": "ontology_label ''Riboflavin'' -> ''riboflavin'':
    synced to canonical CHEBI label (preferred_term ''Riboflavin'' unchanged).", "curator":
    "correct_stale_ontology_labels.py", "timestamp": "2026-06-09T05:23:46.827070+00:00"},
    {"action": "ANNOTATED", "changes": "Migrated legacy media_roles to role facets
    (#128): VITAMIN_SOURCE -> nutritional_roles.VITAMIN_SOURCE", "curator": "migrate_media_roles_to_facets",
    "timestamp": "2026-07-20T00:00:00+00:00"}, {"action": "CORRECTED", "changes":
    "occurrence_statistics 85/1837 -> 2122/2123 (media_count/total_occurrences), derived
    from distinct CultureMech recipe ids in the #337 occurrence table. The prior values
    came from the importer retired in #453, whose media_count counted a list truncated
    to 50 examples (#449). [source=ingredient_occurrences.tsv culturemech_rev=15a4da5c08
    rows=194137 distinct_recipes=15257]", "curator": "refresh_occurrence_statistics",
    "timestamp": "2026-08-27T03:16:39.519802+00:00"}, {"action": "ADDED_SYNONYMS",
    "changes": "Added 4 CultureMech recipe surface form(s) that folded onto this record''s
    published label but were absent from MIM''s label index, so CultureMech could
    not resolve them: ''Riboflavin (Vitamine B2)'' (x4 CultureMech mentions); ''Riboflavin
    (Vitamin B2)'' (x2 CultureMech mentions); ''Riboflavin (0.2 mg/ml)'' (x1 CultureMech
    mentions); ''Riboflavin (see below)'' (x1 CultureMech mentions). Source: culturemech:output/ingredient_occurrences.tsv.",
    "curator": "claude_culturemech_alias_backfill", "llm_assisted": false, "timestamp":
    "2026-08-30T04:48:06.233536+00:00"}, {"action": "ADDED_SYNONYMS", "changes": "Added
    1 CultureMech recipe surface form(s) that folded onto this record''s published
    label but were absent from MIM''s label index, so CultureMech could not resolve
    them: ''Riboflavin (0.05 \u03bcg/mL)'' (x1 CultureMech mentions). Source: culturemech:output/ingredient_occurrences.tsv.",
    "curator": "claude_culturemech_alias_backfill", "llm_assisted": false, "timestamp":
    "2026-08-31T23:56:54.854807+00:00"}], "identifier": "CHEBI:17015", "mapping":
    {"evidence": [{"evidence_type": "DATABASE_MATCH", "notes": "Imported from CultureMech
    pipeline, quality=DIRECT_MATCH", "source": "CultureMech"}, {"evidence_type": "LITERATURE",
    "explanation": "Auto-proposed; curator should rephrase or remove.", "pmid": "40609532",
    "snippet": "We found that the abundance of Bacteroides cellulosilyticus affects
    tumor heterogeneity by producing riboflavin that inhibits CERS3 activity, thus
    delaying CRC progression.", "source": "PubMed search (''Riboflavin'')", "supports":
    "SUPPORT"}], "mapping_quality": "EXACT_MATCH", "ontology_id": "CHEBI:17015", "ontology_label":
    "riboflavin", "ontology_source": "CHEBI"}}'
  snapshot_sha256: b79fe5e134e627e7c95d6190e54c52b04f9d81a61ad381cb136b986430d80644
- evidence_id: ev-1dfdb8319038a4fb
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Riboflavin
  accessed_at: '2026-10-11T03:08:52Z'
  support: supports
  summary: '[{"comment": "ENRICH_SYNONYM: kg-microbe is ''riboflavin'' plus qualifier
    (''(1-)'')", "confidence": "0.95", "data_row": 2429, "mapping_date": "2026-08-31",
    "mapping_justification": "semapv:LexicalMatching", "object_id": "CHEBI:17015",
    "object_label": "riboflavin", "object_source": "obo:chebi.owl", "other": "1-deoxy-1-(7,8-dimethyl-2,4-dioxo-3,4-dihydrobenzo[g]pteridin-10(2H)-yl)-D-ribitol|1-deoxy-1-(7,8-dimethyl-2,4-dioxo-3,4-dihydrobenzo[g]pteridin-10(2H)-yl)pentitol|5-deoxy-5-(7,8-dimethyl-2,4-dioxo-3,4-dihydrobenzo[g]pteridin-10(2H)-yl)-D-ribitol|6,7-dimethyl-9-D-ribitylisoalloxazine|7,8-dimethyl-10-(D-ribo-2,3,4,5-tetrahydroxypentyl)benzo[g]pteridine-2,4(3H,10H)-dione|7,8-dimethyl-10-(D-ribo-2,3,4,5-tetrahydroxypentyl)isoalloxazine|7,8-dimethyl-10-[(2S,3S,4R)-2,3,4,5-tetrahydroxypentyl]benzo[g]pteridine-2,4(3H,10H)-dione|7,8-dimethyl-10-ribitylisoalloxazine|Aqua-Flave|Beflavin|Beflavine|Bisulase|Dermadram|E101|Fiboflavin|Flavaxin|Flavin
    Bb|Flaxain|Hyflavin|Riboflavine|Riboflavine (B2)|Riboflavin (Vitamine B2)|Riboflavin
    (Vitamin B2)|Riboflavin (0.2 mg/ml)|Riboflavin (see below)|Riboflavin (0.05 \u03bcg/mL)|CAS:83-88-5",
    "predicate_id": "skos:exactMatch", "source": "MIM:CultureMech|MIM:PubMed search
    (''Riboflavin'')|MIM:curator=claude_culturemech_alias_backfill|kgm:chebi_xrefs|kgm:culturebotai_reviewed|kgm:mediadive_compounds|kgm:mediaingredientmech_reviewed|kgm:mediaingredientmech_reviewed[curator=audit_mim_merge]|kgm:mediaingredientmech_reviewed[curator=auto_classify_ingredient_type]|kgm:mediaingredientmech_reviewed[curator=correct_stale_ontology_labels.py]|kgm:mediaingredientmech_reviewed[curator=migrate_media_roles_to_facets]|kgm:primary_mappings[kegg_compound]",
    "subject_id": "MIM:Riboflavin", "subject_label": "Riboflavin", "validation_method":
    "OAK+OLS:chebi|SYNONYM_ENRICH|2026-07-07"}]'
  snapshot_sha256: 2eae181f31d6433c20ffdb9dc2f8c8d7ad0a17a46a3189dea8c307fbc1c7b40e
- evidence_id: ev-a809b48a4c5a84c5
  kind: prior_review
  reference: reports/yaml_record_review/Riboflavin.md
  locator: Complete historical report, including Verdict and Recommended Edits
  accessed_at: '2026-10-11T03:08:52Z'
  support: context_only
  summary: Historical interpretation was read in full; it is not fresh source adjudication.
  snapshot_sha256: 9dd8b2a901c40593a896669ad82303310aafb787ae2f8c505cbaa93fd256e8fc
  quote: '# `data/ingredients/mapped/Riboflavin.yaml`


    **Verdict**: needs curation, major issue.


    **Identity**: `Riboflavin` maps exactly to active, defining `CHEBI:17015` /

    `riboflavin`. Fresh OLS4 lookup resolved the ChEBI term with CAS `83-88-5`,

    formula `C17H20N4O6`, and the same InChI as the YAML; fresh PubChem lookup by

    the stored CAS resolved CID 493570 with the same formula and InChI.


    **Validation**: `uv run --frozen python scripts/validate_strict.py

    data/ingredients/mapped/Rhodomycin_A.yaml

    data/ingredients/mapped/Rhodomycin_B.yaml data/ingredients/mapped/Ribitol.yaml

    data/ingredients/mapped/Riboflavin.yaml

    data/ingredients/mapped/Ribonucleic_Acid_From_Torula_Yeast_Type_VI.yaml` passed

    for the 5-file batch with 0 ERROR rows. Direct

    `linkml-term-validator validate-data` with `--labels` passed for the same 5

    files.


    **Evidence**: The exact ChEBI identity, CAS, chemical properties, refreshed

    2123-occurrence count, and CultureMech `VITAMIN_SOURCE` role pass. The

    per-record YAML also agrees with the regenerated aggregate row when keyed by

    `(identifier, preferred_term)`.


    Final SSSOM row 2507 still exports raw recipe labels in `other`: `Riboflavin

    (0.2 mg/ml)`, `Riboflavin (see below)`, and the raw 0.05 microgram/mL

    CultureMech label. These are concentration- or recipe-pointer strings, not

    true alternate names for `CHEBI:17015`.


    The auto-proposed PMID 40609532 mapping evidence is also out of scope. PubMed

    resolves the article to a 2025 Cell Metabolism study of microbial riboflavin,

    ceramide synthase 3, and colorectal cancer; it mentions riboflavin, but it does

    not support this CultureMech ingredient-to-ChEBI identity claim.


    **Completeness**: The exact chemical identity is complete enough, and the

    vitamin role has CultureMech database evidence. The unsafe data is confined to

    three raw occurrence synonyms plus the irrelevant PubMed mapping-evidence row.


    **Recommended Edits**: Remove the concentration-qualified and `see below`

    CultureMech labels from active exported synonyms and drop or replace the

    auto-proposed PubMed evidence under `ontology_mapping.evidence`. Regenerate

    final SSSOM and confirm row 2507 no longer exports non-synonym recipe text in

    `other`.

    '
- evidence_id: ev-6c06e714e86355c6
  kind: prior_review
  reference: reviews/structured/20261011T024638Z-mim-reconcile-all-batch-11/review.yaml
  locator: findings[finding_id=f-2680803ffb7b7f40]
  accessed_at: '2026-10-11T03:08:52Z'
  support: context_only
  summary: Exact earlier occurrence has open/confirmed status, based on exported-token
    presence and historical report text.
  snapshot_sha256: a417d1bfc777756925990a4ecae1a6b539746c3606d042df7e1c29a218c62f8b
  quote: '{"category": "nomenclature", "certainty": "confirmed", "description": "Historical
    tokens are still present on the exact-subject SSSOM rows: [{\"reason\":\"unresolved
    recipe cross-reference in a resolving synonym\",\"token\":\"Sludge fluid (see
    below)\"}]. Truncated concentration strings and context-dependent instructions
    need scoped curation. This check does not reject catalog/RAW_TEXT synonyms as
    a class.", "evidence_ids": ["ev-1cd51dd628156c5b", "ev-585a6ebb79a21665"], "external_issues":
    ["https://github.com/CultureBotAI/MediaIngredientMech/issues/718"], "field_paths":
    ["synonyms", "SSSOM.other"], "finding_id": "f-2680803ffb7b7f40", "issue_key":
    "mim-reconciliation-exported-context-tokens-c6cdd023283a1f0a", "owner_paths":
    [{"path": "data/ingredients/mapped/Sludge_fluid.yaml", "repository": "CultureBotAI/MediaIngredientMech",
    "role": "maintained ingredient"}], "severity": "major", "status": "open", "tags":
    ["reconciliation", "bundle-by-owner", "exported-context-tokens"], "target_ids":
    ["record-c6cdd023283a1f0a"], "title": "Review nonportable exported tokens: Sludge
    fluid"}'
- evidence_id: ev-b62c98e3d0a1e1d5
  kind: record_content
  reference: data/ingredients/mapped/Sludge_fluid.yaml
  locator: identifier, ontology_mapping, synonyms and curation_history
  accessed_at: '2026-10-11T03:08:52Z'
  support: partial
  summary: '{"candidate_labels": [{"source": "culturemech:output/ingredient_occurrences.tsv",
    "synonym_text": "Sludge fluid (see below)", "synonym_type": "RAW_TEXT"}], "history":
    [{"action": "CREATED_FROM_CULTUREMECH_RESIDUAL", "changes": "Created from a CultureMech
    recipe ingredient MIM held no record for (2 mentions across 2 recipes). Grounded
    to MICRO:0000521 (''sludge fluid'') on an exact match of the canonical label to
    the query ''Sludge fluid''. Source: culturemech:output/ingredient_occurrences.tsv.",
    "curator": "claude_culturemech_residual_grounding", "llm_assisted": false, "new_status":
    "MAPPED", "timestamp": "2026-08-30T10:35:03.361102+00:00"}, {"action": "ADDED_SYNONYMS",
    "changes": "Added 1 CultureMech recipe surface form(s) that folded onto this record''s
    published label but were absent from MIM''s label index, so CultureMech could
    not resolve them: ''Sludge fluid (see below)'' (x1 CultureMech mentions). Source:
    culturemech:output/ingredient_occurrences.tsv.", "curator": "claude_culturemech_alias_backfill",
    "llm_assisted": false, "timestamp": "2026-08-30T10:41:26.546472+00:00"}, {"action":
    "CORRECTED", "changes": "Added ontology_mapping.evidence recording the CultureMech
    occurrence table as the source of this grounding. The provenance was already in
    this record''s CREATED_FROM_CULTUREMECH_RESIDUAL history entry but absent from
    the structured field the SSSOM builder reads, so a rebuild dropped MIM:culturemech:output/ingredient_occurrences.tsv
    from the published row (#541).", "curator": "claude_restore_culturemech_evidence",
    "llm_assisted": false, "timestamp": "2026-09-06T07:34:56.956907+00:00"}], "identifier":
    "MICRO:0000521", "mapping": {"evidence": [{"evidence_type": "LEXICAL_MATCH", "notes":
    "Surface form appears in CultureMech''s occurrence table and was grounded to MICRO:0000521
    on an exact match against the ontology label. Restored from the record''s own
    creation history (#541); the residual importer wrote this provenance only into
    the published SSSOM.", "source": "culturemech:output/ingredient_occurrences.tsv"}],
    "mapping_quality": "EXACT_MATCH", "match_level": "EXACT", "ontology_id": "MICRO:0000521",
    "ontology_label": "sludge fluid", "ontology_source": "MICRO"}}'
  snapshot_sha256: 45eed06b9f478903bfb4849c19b5656aca154018619b1db3d08152b5212e489c
- evidence_id: ev-d4f1e238a85e0e57
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Sludge_fluid
  accessed_at: '2026-10-11T03:08:52Z'
  support: supports
  summary: '[{"comment": "", "confidence": "0.99", "data_row": 2521, "mapping_date":
    "2026-09-06", "mapping_justification": "semapv:LexicalMatching", "object_id":
    "MICRO:0000521", "object_label": "sludge fluid", "object_source": "obo:micro.owl",
    "other": "Sludge fluid (see below)", "predicate_id": "skos:exactMatch", "source":
    "MIM:culturemech:output/ingredient_occurrences.tsv|MIM:curator=claude_restore_culturemech_evidence",
    "subject_id": "MIM:Sludge_fluid", "subject_label": "Sludge fluid", "validation_method":
    "manual:claude_culturemech_residual_grounding|CREATED|2026-08-30"}]'
  snapshot_sha256: 2eae181f31d6433c20ffdb9dc2f8c8d7ad0a17a46a3189dea8c307fbc1c7b40e
- evidence_id: ev-de40a4caf98a1085
  kind: prior_review
  reference: reports/yaml_record_review/Sludge_fluid.md
  locator: Complete historical report, including Verdict and Recommended Edits
  accessed_at: '2026-10-11T03:08:52Z'
  support: context_only
  summary: Historical interpretation was read in full; it is not fresh source adjudication.
  snapshot_sha256: 644b8e24ff48c5a4f36eb61fb433068aceaebb59b6cc9b0970535705b399fdbf
  quote: '# `data/ingredients/mapped/Sludge_fluid.yaml`


    **Verdict**: needs curation, major issue.


    **Identity**: `Sludge fluid` maps exactly to active, defining `MICRO:0000521`
    /

    `sludge fluid`. Fresh OLS4 lookup resolved the MICRO term by exact CURIE and

    exact label, matching the restored CultureMech occurrence-table grounding.


    **Validation**: `uv run --frozen python scripts/validate_strict.py

    data/ingredients/mapped/Sludge.yaml

    data/ingredients/mapped/Sludge_fluid.yaml

    data/ingredients/mapped/Sn-Glycerol_3-phosphate_Lithium_Salt.yaml

    data/ingredients/mapped/Sn-glycero-3-phosphocholine.yaml

    data/ingredients/mapped/Sn-glycerol_3-phosphate_Bis_Cyclohexylammonium_Salt.yaml`

    passed for the 5-file batch with 0 ERROR rows. Direct

    `linkml-term-validator validate-data` with `--labels` passed for the ENVO and

    3 CHEBI files; `Sludge_fluid` was skipped because `MICRO` is outside the Engine

    A OBO term-validation subset.


    **Evidence**: The exact MICRO identity, occurrence count, and structured

    CultureMech evidence pass. The per-record YAML agrees with the regenerated

    aggregate row when keyed by `(identifier, preferred_term)`.


    The final SSSOM row needs synonym cleanup. Row 2600 exports `Sludge fluid (see

    below)` as `other`; that is a conditional recipe instruction fragment, not an

    exact synonym of the MICRO sludge-fluid term.


    **Completeness**: The exact MICRO identity and occurrence counts agree. The

    conditional CultureMech surface form needs to be filtered from final SSSOM or

    removed from the exported synonym set.


    **Recommended Edits**: Remove `Sludge fluid (see below)` from

    `data/ingredients/mapped/Sludge_fluid.yaml` or update the SSSOM synonym policy

    to exclude conditional raw-text labels, then rebuild final SSSOM and confirm row

    2600 has an empty `other` field.

    '
- evidence_id: ev-4f670ddc934d5e74
  kind: prior_review
  reference: reviews/structured/20261011T024638Z-mim-reconcile-all-batch-11/review.yaml
  locator: findings[finding_id=f-ef4889c5708c1269]
  accessed_at: '2026-10-11T03:08:52Z'
  support: context_only
  summary: Exact earlier occurrence has open/confirmed status, based on exported-token
    presence and historical report text.
  snapshot_sha256: a417d1bfc777756925990a4ecae1a6b539746c3606d042df7e1c29a218c62f8b
  quote: '{"category": "nomenclature", "certainty": "confirmed", "description": "Historical
    tokens are still present on the exact-subject SSSOM rows: [{\"reason\":\"unresolved
    recipe cross-reference in a resolving synonym\",\"token\":\"Soil extract (see
    below)\"}]. Truncated concentration strings and context-dependent instructions
    need scoped curation. This check does not reject catalog/RAW_TEXT synonyms as
    a class.", "evidence_ids": ["ev-bab4ffe1afd610f2", "ev-6c7c43be0fc3aa35"], "external_issues":
    ["https://github.com/CultureBotAI/MediaIngredientMech/issues/718"], "field_paths":
    ["synonyms", "SSSOM.other"], "finding_id": "f-ef4889c5708c1269", "issue_key":
    "mim-reconciliation-exported-context-tokens-3245d67aff586e82", "owner_paths":
    [{"path": "data/ingredients/mapped/Soil_Extract.yaml", "repository": "CultureBotAI/MediaIngredientMech",
    "role": "maintained ingredient"}], "severity": "major", "status": "open", "tags":
    ["reconciliation", "bundle-by-owner", "exported-context-tokens"], "target_ids":
    ["record-3245d67aff586e82"], "title": "Review nonportable exported tokens: Soil
    extract"}'
- evidence_id: ev-927f64381fa816f2
  kind: record_content
  reference: data/ingredients/mapped/Soil_Extract.yaml
  locator: identifier, ontology_mapping, synonyms and curation_history
  accessed_at: '2026-10-11T03:08:52Z'
  support: partial
  summary: '{"candidate_labels": [{"source": "culturemech:output/ingredient_occurrences.tsv",
    "synonym_text": "Soil extract (see below)", "synonym_type": "RAW_TEXT"}], "history":
    [{"action": "CREATED_AS_UNMAPPED", "changes": "Imported from mim-queue (source_id=mediadive.ingredient:180);
    no CAS-RN or CHEBI/NCIT match. Curator review needed.", "curator": "audit_import_ingredients[mim-queue]",
    "llm_assisted": false, "new_status": "UNMAPPED", "timestamp": "2026-04-30T18:43:03.698454+00:00"},
    {"action": "AUTO_UPGRADE_TO_MICRO", "changes": "primary UNMAPPED_0529 \u2192 MICRO:0000457
    (label-exact)", "curator": "auto_classify_ingredient_type", "llm_assisted": false,
    "timestamp": "2026-05-01T19:50:45.145149+00:00"}, {"action": "AUTO_CLASSIFY_INGREDIENT_TYPE",
    "changes": "set ingredient_type=UNDEFINED_MIXTURE (name matches complex pattern
    ''Soil'')", "curator": "auto_classify_ingredient_type", "llm_assisted": false,
    "timestamp": "2026-05-02T03:12:18.544149+00:00"}, {"action": "ANNOTATED", "changes":
    "Added 1 environmental_context entries (issue #1, Phase 3 initial pass).", "curator":
    "env_context_phase3_initial", "timestamp": "2026-05-24T04:03:54.899342+00:00"},
    {"action": "CORRECTED", "changes": "occurrence_statistics 0/0 -> 17/17 (media_count/total_occurrences),
    derived from distinct CultureMech recipe ids in the #337 occurrence table. The
    prior values came from the importer retired in #453, whose media_count counted
    a list truncated to 50 examples (#449). [source=ingredient_occurrences.tsv culturemech_rev=15a4da5c08
    rows=194137 distinct_recipes=15257]", "curator": "refresh_occurrence_statistics",
    "timestamp": "2026-08-27T03:16:39.519889+00:00"}, {"action": "ADDED_SYNONYMS",
    "changes": "Added 2 CultureMech recipe surface form(s) that folded onto this record''s
    published label but were absent from MIM''s label index, so CultureMech could
    not resolve them: ''Soil extract (see below)'' (x3 CultureMech mentions); ''Soil
    extract (SE1)'' (x1 CultureMech mentions). Source: culturemech:output/ingredient_occurrences.tsv.",
    "curator": "claude_culturemech_alias_backfill", "llm_assisted": false, "timestamp":
    "2026-08-30T04:48:06.233536+00:00"}], "identifier": "MICRO:0000457", "mapping":
    {"evidence": [{"evidence_type": "DATABASE_MATCH", "notes": "Auto-upgraded from
    ''UNMAPPED_0529''; match=label-exact", "source": "MICRO via OLS search"}], "mapping_quality":
    "EXACT_MATCH", "ontology_id": "MICRO:0000457", "ontology_label": "soil extract",
    "ontology_source": "MICRO"}}'
  snapshot_sha256: 6983e9a7a4460eb605e05eaed32f6c08397e2555ce1356d98fb5d301b592e848
- evidence_id: ev-1edf0a1870e81e81
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Soil_Extract
  accessed_at: '2026-10-11T03:08:52Z'
  support: supports
  summary: '[{"comment": "", "confidence": "0.99", "data_row": 2615, "mapping_date":
    "2026-08-30", "mapping_justification": "semapv:LexicalMatching", "object_id":
    "MICRO:0000457", "object_label": "soil extract", "object_source": "obo:micro.owl",
    "other": "Soil extract (see below)|Soil extract (SE1)", "predicate_id": "skos:exactMatch",
    "source": "MIM:MICRO via OLS search|MIM:curator=claude_culturemech_alias_backfill",
    "subject_id": "MIM:Soil_Extract", "subject_label": "Soil extract", "validation_method":
    "none|UNKNOWN_TERM|2026-07-07"}]'
  snapshot_sha256: 2eae181f31d6433c20ffdb9dc2f8c8d7ad0a17a46a3189dea8c307fbc1c7b40e
- evidence_id: ev-cefe2423553074dc
  kind: prior_review
  reference: reports/yaml_record_review/Soil_Extract.md
  locator: Complete historical report, including Verdict and Recommended Edits
  accessed_at: '2026-10-11T03:08:52Z'
  support: context_only
  summary: Historical interpretation was read in full; it is not fresh source adjudication.
  snapshot_sha256: ae5ccc882afbb6dc1bede0c3b61e54987fe5116620d05dd4794692387a263a84
  quote: "# `data/ingredients/mapped/Soil_Extract.yaml`\n\n## Verdict\n\nNeeds curation\
    \ - major. The exact `MICRO:0000457` soil extract identity,\nundefined-mixture\
    \ type, environmental context, and occurrence count pass, but\nfinal SSSOM publishes\
    \ recipe-specific parenthetical text as exact synonyms.\n\n## Identity\n\n- Reviewed\
    \ record: `data/ingredients/mapped/Soil_Extract.yaml`.\n- Identifier and grounding:\
    \ `identifier: MICRO:0000457` with\n  `ontology_mapping.ontology_id: MICRO:0000457`,\
    \ label `soil extract`, source\n  `MICRO`, `mapping_quality: EXACT_MATCH`, `mapping_status:\
    \ MAPPED`, and\n  `ingredient_type: UNDEFINED_MIXTURE`.\n- Occurrences: 17 source\
    \ occurrences across 17 CultureMech media.\n\n## Validation\n\n- `uv run --frozen\
    \ python scripts/validate_strict.py` on the 5-file batch from\n  `Soil_Extract`\
    \ through `Sorbose`: exited 0 and wrote zero ERROR rows.\n- Direct Engine A term\
    \ validation was skipped for this record because `MICRO`\n  is outside the OBO\
    \ allowlist for `linkml-term-validator`; fresh\n  prefix-specific EBI OLS4 lookup\
    \ resolved `MICRO:0000457`.\n- Local aggregate comparison found this per-record\
    \ file synchronized with its\n  keyed row in `data/curated/mapped_ingredients.yaml`.\n\
    \n## Evidence\n\n- Fresh EBI OLS4 lookup resolves active `MICRO:0000457` with\
    \ label\n  `soil extract`, matching the exact MICRO grounding.\n- The environmental\
    \ context links the extract to `ENVO:00001998` soil with\n  `NATURAL_SOURCE`,\
    \ which matches the source material named by the ingredient.\n- Major: final SSSOM\
    \ publishes `Soil extract (see below)` and\n  `Soil extract (SE1)` in `other`.\
    \ The first is an instruction pointer and the\n  second is a recipe-local variant\
    \ label, not a general exact synonym of soil\n  extract.\n\n## Completeness\n\n\
    - The MICRO ID, label, mixture type, soil environmental context, exact row, and\n\
    \  occurrence count agree.\n- The only consequential gap is demoting the two CultureMech\
    \ occurrence labels\n  so they remain searchable locally without publishing as\
    \ exact final synonyms.\n\n## Recommended Edits\n\n- Major: in `data/ingredients/mapped/Soil_Extract.yaml`,\
    \ retype or suppress the\n  `Soil extract (see below)` and `Soil extract (SE1)`\
    \ occurrence labels so final\n  SSSOM no longer emits them in `other`.\n"
- evidence_id: ev-61509143d0ecf84a
  kind: prior_review
  reference: reviews/structured/20261011T024638Z-mim-reconcile-all-batch-11/review.yaml
  locator: findings[finding_id=f-3b7b7b7cd4c70ace]
  accessed_at: '2026-10-11T03:08:52Z'
  support: context_only
  summary: Exact earlier occurrence has open/confirmed status, based on exported-token
    presence and historical report text.
  snapshot_sha256: a417d1bfc777756925990a4ecae1a6b539746c3606d042df7e1c29a218c62f8b
  quote: '{"category": "nomenclature", "certainty": "confirmed", "description": "Historical
    tokens are still present on the exact-subject SSSOM rows: [{\"reason\":\"unresolved
    recipe cross-reference in a resolving synonym\",\"token\":\"Trace element solution
    (see Medium No. 187\"}]. Truncated concentration strings and context-dependent
    instructions need scoped curation. This check does not reject catalog/RAW_TEXT
    synonyms as a class.", "evidence_ids": ["ev-e9a77a2c0d4af0d8", "ev-1ae06c3a3a72a5b0"],
    "external_issues": ["https://github.com/CultureBotAI/MediaIngredientMech/issues/718"],
    "field_paths": ["synonyms", "SSSOM.other"], "finding_id": "f-3b7b7b7cd4c70ace",
    "issue_key": "mim-reconciliation-exported-context-tokens-341efa75278b5e50", "owner_paths":
    [{"path": "data/ingredients/mapped/Trace_Element_Solution_See_Medium_No_187.yaml",
    "repository": "CultureBotAI/MediaIngredientMech", "role": "maintained ingredient"}],
    "severity": "major", "status": "open", "tags": ["reconciliation", "bundle-by-owner",
    "exported-context-tokens"], "target_ids": ["record-341efa75278b5e50"], "title":
    "Review nonportable exported tokens: Trace element solution see Medium No. 187"}'
- evidence_id: ev-cb42f25983a0ad30
  kind: record_content
  reference: data/ingredients/mapped/Trace_Element_Solution_See_Medium_No_187.yaml
  locator: identifier, ontology_mapping, synonyms and curation_history
  accessed_at: '2026-10-11T03:08:52Z'
  support: partial
  summary: '{"candidate_labels": [{"source": "culturemech:output/ingredient_occurrences.tsv",
    "synonym_text": "Trace element solution (see Medium No. 187", "synonym_type":
    "RAW_TEXT"}], "history": [{"action": "CREATED_AS_UNMAPPED", "changes": "Imported
    from mim-queue (source_id=mediadive.ingredient:1886); no CAS-RN or CHEBI/NCIT
    match. Curator review needed.", "curator": "audit_import_ingredients[mim-queue]",
    "llm_assisted": false, "new_status": "UNMAPPED", "timestamp": "2026-04-30T18:43:03.698454+00:00"},
    {"action": "CLASSIFY_AS_STOCK_SOLUTION", "changes": "name pattern ''see Medium
    No.'' indicates pre-mixed defined solution", "curator": "auto_classify_stock_solution",
    "llm_assisted": false, "timestamp": "2026-05-01T19:58:06.857978+00:00"}, {"action":
    "AUTO_CLASSIFY_INGREDIENT_TYPE", "changes": "set ingredient_type=STOCK_SOLUTION
    (name matches solution pattern ''Trace element'')", "curator": "auto_classify_ingredient_type",
    "llm_assisted": false, "timestamp": "2026-05-02T03:12:19.961419+00:00"}, {"action":
    "AUTO_UPGRADE_TO_NCIT", "changes": "primary UNMAPPED_0549 \u2192 NCIT:C896 (strategy=stem-match)",
    "curator": "resolve_unmapped_v2", "llm_assisted": false, "timestamp": "2026-05-02T03:18:21.989902+00:00"},
    {"action": "CORRECTED", "changes": "Changed identifier from NCIT:C896 to kgmicrobe.ingredient:trace_element_solution_see_medium_no_187
    and retained NCIT:C896 only as CLOSE_MATCH. Named trace element solution is a
    formulation, not identical to the generic trace element class.", "curator": "ingredient_mapping_review_2026_05_05",
    "llm_assisted": false, "new_status": "MAPPED", "previous_status": "MAPPED", "timestamp":
    "2026-05-05T00:00:00+00:00"}, {"action": "ADDED_SYNONYMS", "changes": "Added 1
    CultureMech recipe surface form(s) that folded onto this record''s published label
    but were absent from MIM''s label index, so CultureMech could not resolve them:
    ''Trace element solution (see Medium No. 187'' (x1 CultureMech mentions). Source:
    culturemech:output/ingredient_occurrences.tsv.", "curator": "claude_culturemech_alias_backfill",
    "llm_assisted": false, "timestamp": "2026-08-30T04:48:06.233536+00:00"}], "identifier":
    "kgmicrobe.ingredient:trace_element_solution_see_medium_no_187", "mapping": {"evidence":
    [{"evidence_type": "CURATOR_JUDGMENT", "notes": "Named trace element solution
    is a formulation, not identical to the generic trace element class.", "source":
    "ingredient_mapping_review_2026-05-05"}], "mapping_quality": "CLOSE_MATCH", "ontology_id":
    "NCIT:C896", "ontology_label": "Trace Element", "ontology_source": "NCIT"}}'
  snapshot_sha256: eea23f3c73fe8d5993d5292436d12776dde1308bcedf2a4916d1ca553b6cf40d
- evidence_id: ev-775e49cc5333c85a
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Trace_Element_Solution_See_Medium_No_187
  accessed_at: '2026-10-11T03:08:52Z'
  support: supports
  summary: '[{"comment": "", "confidence": "0.9", "data_row": 2802, "mapping_date":
    "2026-08-30", "mapping_justification": "semapv:ManualMappingCuration", "object_id":
    "NCIT:C896", "object_label": "Trace Element", "object_source": "obo:ncit.owl",
    "other": "Trace element solution (see Medium No. 187", "predicate_id": "skos:closeMatch",
    "source": "MIM:ingredient_mapping_review_2026-05-05|MIM:curator=claude_culturemech_alias_backfill",
    "subject_id": "MIM:Trace_Element_Solution_See_Medium_No_187", "subject_label":
    "Trace element solution see Medium No. 187", "validation_method": "none|UNKNOWN_TERM|2026-07-07"},
    {"comment": "Registry/identity row preserving kgmicrobe.ingredient:trace_element_solution_see_medium_no_187
    alongside parent NCIT:C896.", "confidence": "0.99", "data_row": 2803, "mapping_date":
    "2026-08-30", "mapping_justification": "semapv:ManualMappingCuration", "object_id":
    "kgmicrobe.ingredient:trace_element_solution_see_medium_no_187", "object_label":
    "Trace element solution see Medium No. 187", "object_source": "kgm:ingredient",
    "other": "", "predicate_id": "skos:exactMatch", "source": "MIM:ingredient_mapping_review_2026-05-05|MIM:curator=claude_culturemech_alias_backfill",
    "subject_id": "MIM:Trace_Element_Solution_See_Medium_No_187", "subject_label":
    "Trace element solution see Medium No. 187", "validation_method": "none|UNKNOWN_TERM|2026-07-07"}]'
  snapshot_sha256: 2eae181f31d6433c20ffdb9dc2f8c8d7ad0a17a46a3189dea8c307fbc1c7b40e
- evidence_id: ev-a18de57ffdc5d750
  kind: prior_review
  reference: reports/yaml_record_review/Trace_Element_Solution_See_Medium_No_187.md
  locator: Complete historical report, including Verdict and Recommended Edits
  accessed_at: '2026-10-11T03:08:52Z'
  support: context_only
  summary: Historical interpretation was read in full; it is not fresh source adjudication.
  snapshot_sha256: 9d6913d60ca5135c4cd8074f78886386638a460bae5393725ce8f4aa35fc2f55
  quote: "# `data/ingredients/mapped/Trace_Element_Solution_See_Medium_No_187.yaml`\n\
    \n## Verdict\n\nNeeds curation, major. The local stock-solution identity and NCIT\
    \ close match\nare synchronized, but the record has no component transcription\
    \ and the final\nSSSOM close row exports a malformed recipe-reference alias.\n\
    \n## Identity\n\n- Reviewed record:\n  `data/ingredients/mapped/Trace_Element_Solution_See_Medium_No_187.yaml`.\n\
    - Identifier and grounding: `identifier:\n  kgmicrobe.ingredient:trace_element_solution_see_medium_no_187`,\
    \ close parent\n  `ontology_mapping.ontology_id: NCIT:C896`, label `Trace Element`,\
    \ source\n  `NCIT`, `mapping_quality: CLOSE_MATCH`, `mapping_status: MAPPED`,\n\
    \  `kg_microbe_node_id:\n  kgmicrobe.ingredient:trace_element_solution_see_medium_no_187`,\
    \ and\n  `ingredient_type: STOCK_SOLUTION`.\n- Synonyms: raw mim-queue source\
    \ form plus malformed raw CultureMech source\n  form `Trace element solution (see\
    \ Medium No. 187`.\n- Occurrences: no CultureMech recipe occurrences in the split\
    \ occurrence\n  snapshot.\n- Components: none.\n\n## Validation\n\n- `uv run --frozen\
    \ python scripts/validate_strict.py` on the 5-file batch from\n  `Trace_Element_Solution_SL-10`\
    \ through `Trace_Metals_Solution`: exited 0 and\n  wrote zero ERROR rows.\n- Direct\
    \ old Engine A/OBO term validation was skipped for this row because\n  `NCIT`\
    \ and `kgmicrobe.ingredient` are outside the CHEBI-focused OBO term\n  subset.\n\
    - Local aggregate comparison found this per-record file synchronized with its\n\
    \  keyed row in `data/curated/mapped_ingredients.yaml`.\n\n## Evidence\n\n- Fresh\
    \ exact OLS4 search for `Trace Element` returns `NCIT:C896` with label\n  `Trace\
    \ Element`; the May review correctly keeps it as a close category\n  rather than\
    \ as the exact identity.\n- The final SSSOM has a close row to `NCIT:C896` and\
    \ an exact identity row for\n  `kgmicrobe.ingredient:trace_element_solution_see_medium_no_187`.\n\
    - The NCIT close row exports `Trace element solution (see Medium No. 187` in\n\
    \  `other`.\n\n## Issues\n\n### Major: a malformed recipe-reference alias reaches\
    \ final SSSOM\n\n`Trace element solution (see Medium No. 187` is a raw CultureMech\
    \ source\nsurface with the parenthetical still open. It is a recipe cross-reference,\
    \ not\na real synonym of either the NCIT trace-element category or the local stock\n\
    identity, so it should not be emitted as a final `other` token.\n\n### Major:\
    \ the named stock solution is still missing components\n\nThe record is deliberately\
    \ minted as a local stock-solution identity, but there\nis no `components` block\
    \ or `component_assertion`. The `see Medium No. 187`\nsurface points at a source\
    \ recipe that should be transcribed before this can\nbehave like a complete trace-metal\
    \ stock record.\n\n## Completeness\n\n- The local identity, close NCIT parent,\
    \ aggregate copy, and final SSSOM rows\n  are synchronized.\n- The raw cross-reference\
    \ synonym and missing stock composition remain\n  unresolved.\n\n## Recommended\
    \ Edits\n\n- Transcribe the Medium No. 187 trace-element solution into reviewed\n\
    \  components, and mark the raw `see Medium` alias so the SSSOM exporter filters\n\
    \  it out of final `other`.\n"
- evidence_id: ev-666a0e05df6eee3c
  kind: prior_review
  reference: reviews/structured/20261011T024638Z-mim-reconcile-all-batch-11/review.yaml
  locator: findings[finding_id=f-612aa67bad26d26a]
  accessed_at: '2026-10-11T03:08:52Z'
  support: context_only
  summary: Exact earlier occurrence has open/confirmed status, based on exported-token
    presence and historical report text.
  snapshot_sha256: a417d1bfc777756925990a4ecae1a6b539746c3606d042df7e1c29a218c62f8b
  quote: '{"category": "nomenclature", "certainty": "confirmed", "description": "Historical
    tokens are still present on the exact-subject SSSOM rows: [{\"reason\":\"unresolved
    recipe cross-reference in a resolving synonym\",\"token\":\"Trace Metal Mix A5
    (see below)\"}]. Truncated concentration strings and context-dependent instructions
    need scoped curation. This check does not reject catalog/RAW_TEXT synonyms as
    a class.", "evidence_ids": ["ev-8a6a1ce8b70c223e", "ev-23742d2f5e375858"], "external_issues":
    ["https://github.com/CultureBotAI/MediaIngredientMech/issues/718"], "field_paths":
    ["synonyms", "SSSOM.other"], "finding_id": "f-612aa67bad26d26a", "issue_key":
    "mim-reconciliation-exported-context-tokens-78ea6a14a080dbf0", "owner_paths":
    [{"path": "data/ingredients/mapped/Trace_Metal_Mix_A5.yaml", "repository": "CultureBotAI/MediaIngredientMech",
    "role": "maintained ingredient"}], "severity": "major", "status": "open", "tags":
    ["reconciliation", "bundle-by-owner", "exported-context-tokens"], "target_ids":
    ["record-78ea6a14a080dbf0"], "title": "Review nonportable exported tokens: Trace
    metal mix A5"}'
- evidence_id: ev-995ddb5e1dd7c309
  kind: record_content
  reference: data/ingredients/mapped/Trace_Metal_Mix_A5.yaml
  locator: identifier, ontology_mapping, synonyms and curation_history
  accessed_at: '2026-10-11T03:08:52Z'
  support: partial
  summary: '{"candidate_labels": [{"source": "culturemech:output/ingredient_occurrences.tsv",
    "synonym_text": "Trace Metal Mix A5 (see below)", "synonym_type": "RAW_TEXT"}],
    "history": [{"action": "CREATED_AS_UNMAPPED", "changes": "Imported from CultureBotHT
    (consolidated_media.json (media-only)). Used in 7 CultureBot media; samples: BG11C,
    BG11, BG11R\u2026. No CAS-RN or CHEBI mapping available; curator review needed.",
    "curator": "audit_add_remaining_culturebotht", "llm_assisted": false, "new_status":
    "UNMAPPED", "timestamp": "2026-04-29T06:51:33.117170+00:00"}, {"action": "AUTO_UPGRADE_TO_MICRO",
    "changes": "primary UNMAPPED_0258 \u2192 MICRO:0001349 via name normalization
    to ''Trace metal mix A5''", "curator": "resolve_unmapped", "llm_assisted": false,
    "timestamp": "2026-05-02T00:41:18.463553+00:00"}, {"action": "AUTO_CLASSIFY_INGREDIENT_TYPE",
    "changes": "set ingredient_type=STOCK_SOLUTION (name matches solution pattern
    ''Trace metal'')", "curator": "auto_classify_ingredient_type", "llm_assisted":
    false, "timestamp": "2026-05-02T03:12:18.924925+00:00"}, {"action": "ANNOTATED",
    "changes": "Added media role: TRACE_ELEMENT (confidence: 0.60)", "curator": "claude_in_session_curation",
    "timestamp": "2026-06-09T04:56:30.248262+00:00"}, {"action": "ANNOTATED", "changes":
    "Migrated legacy media_roles to role facets (#128): TRACE_ELEMENT -> nutritional_roles.TRACE_ELEMENT",
    "curator": "migrate_media_roles_to_facets", "timestamp": "2026-07-20T00:00:00+00:00"},
    {"action": "CORRECTED", "changes": "occurrence_statistics 7/7 -> 2/2 (media_count/total_occurrences),
    derived from distinct CultureMech recipe ids in the #337 occurrence table. The
    prior values came from the importer retired in #453, whose media_count counted
    a list truncated to 50 examples (#449). [source=ingredient_occurrences.tsv culturemech_rev=15a4da5c08
    rows=194137 distinct_recipes=15257]", "curator": "refresh_occurrence_statistics",
    "timestamp": "2026-08-27T03:16:39.519991+00:00"}, {"action": "ADDED_SYNONYMS",
    "changes": "Added 1 CultureMech recipe surface form(s) that folded onto this record''s
    published label but were absent from MIM''s label index, so CultureMech could
    not resolve them: ''Trace Metal Mix A5 (see below)'' (x1 CultureMech mentions).
    Source: culturemech:output/ingredient_occurrences.tsv.", "curator": "claude_culturemech_alias_backfill",
    "llm_assisted": false, "timestamp": "2026-08-30T04:48:06.233536+00:00"}], "identifier":
    "MICRO:0001349", "mapping": {"evidence": [{"evidence_type": "DATABASE_MATCH",
    "notes": "Auto-upgraded from UNMAPPED_0258; matched via ''Trace metal mix A5''
    (name normalization); label-exact", "source": "MICRO via OLS search (resolve_unmapped)"}],
    "mapping_quality": "EXACT_MATCH", "ontology_id": "MICRO:0001349", "ontology_label":
    "trace metal mix A5", "ontology_source": "MICRO"}}'
  snapshot_sha256: 5982838d016b9e668006fa6cd8108c3930358970b2156b2a1596425af3ab4ef2
- evidence_id: ev-3e284f13241fa94e
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Trace_Metal_Mix_A5
  accessed_at: '2026-10-11T03:08:52Z'
  support: supports
  summary: '[{"comment": "", "confidence": "0.99", "data_row": 2804, "mapping_date":
    "2026-08-30", "mapping_justification": "semapv:LexicalMatching", "object_id":
    "MICRO:0001349", "object_label": "trace metal mix A5", "object_source": "obo:micro.owl",
    "other": "Trace Metal Mix A5 (see below)", "predicate_id": "skos:exactMatch",
    "source": "MIM:MICRO via OLS search (resolve_unmapped)|MIM:curator=claude_culturemech_alias_backfill",
    "subject_id": "MIM:Trace_Metal_Mix_A5", "subject_label": "Trace metal mix A5",
    "validation_method": "none|UNKNOWN_TERM|2026-07-07"}]'
  snapshot_sha256: 2eae181f31d6433c20ffdb9dc2f8c8d7ad0a17a46a3189dea8c307fbc1c7b40e
- evidence_id: ev-a6e7432b5d0fbcfb
  kind: prior_review
  reference: reports/yaml_record_review/Trace_Metal_Mix_A5.md
  locator: Complete historical report, including Verdict and Recommended Edits
  accessed_at: '2026-10-11T03:08:52Z'
  support: context_only
  summary: Historical interpretation was read in full; it is not fresh source adjudication.
  snapshot_sha256: fd88d90adbbb3033d82b606fa92e4793b6a9590f36d8bae2ac5819b09aa09534
  quote: "# `data/ingredients/mapped/Trace_Metal_Mix_A5.yaml`\n\n## Verdict\n\nNeeds\
    \ curation, major. The exact MICRO identity and occurrence count are\nsynchronized,\
    \ but a `see below` source alias leaks into final SSSOM and the\n`TRACE_ELEMENT`\
    \ role is still provisional in-session LLM evidence.\n\n## Identity\n\n- Reviewed\
    \ record: `data/ingredients/mapped/Trace_Metal_Mix_A5.yaml`.\n- Identifier and\
    \ grounding: `identifier: MICRO:0001349` with matching\n  `ontology_mapping.ontology_id`,\
    \ label `trace metal mix A5`, source `MICRO`,\n  `mapping_quality: EXACT_MATCH`,\
    \ `mapping_status: MAPPED`, and\n  `ingredient_type: STOCK_SOLUTION`.\n- Synonyms:\
    \ raw CultureBotHT source form plus raw CultureMech source form\n  `Trace Metal\
    \ Mix A5 (see below)`.\n- Occurrences: 2 CultureMech recipe occurrences in 2 media.\n\
    - Roles: one `nutritional_roles.TRACE_ELEMENT` facet at confidence `0.6`.\n\n\
    ## Validation\n\n- `uv run --frozen python scripts/validate_strict.py` on the\
    \ 5-file batch from\n  `Trace_Element_Solution_SL-10` through `Trace_Metals_Solution`:\
    \ exited 0 and\n  wrote zero ERROR rows.\n- Direct old Engine A/OBO term validation\
    \ was skipped for this MICRO row\n  because `MICRO` is outside the CHEBI-focused\
    \ OBO term subset.\n- Local aggregate comparison found this per-record file synchronized\
    \ with its\n  keyed row in `data/curated/mapped_ingredients.yaml`.\n\n## Evidence\n\
    \n- Fresh exact OLS4 search for `Trace metal mix A5` returns `MICRO:0001349` with\n\
    \  label `trace metal mix A5`.\n- The final SSSOM row has\n  `MIM:Trace_Metal_Mix_A5\
    \ skos:exactMatch MICRO:0001349` and exports\n  `Trace Metal Mix A5 (see below)`\
    \ in `other`.\n\n## Issues\n\n### Major: `see below` is not a true synonym\n\n\
    The final `other` token `Trace Metal Mix A5 (see below)` is a recipe-local\ninstruction,\
    \ not an alternate label for the MICRO stock-solution term.\n\n### Major: `TRACE_ELEMENT`\
    \ is provisional LLM evidence\n\nThe only role assertion is still the June in-session\
    \ Claude prediction with the\ncurator note `Provisional in-session LLM role assignment;\
    \ review recommended.`\nThe exact MICRO identity establishes the stock solution\
    \ label, but it does not\nprovide independent role evidence.\n\n## Completeness\n\
    \n- The MICRO identity, occurrence count, aggregate row, and final SSSOM row\n\
    \  agree.\n- The final raw alias and provisional role facet still require curation.\n\
    \n## Recommended Edits\n\n- Filter `Trace Metal Mix A5 (see below)` out of final\
    \ SSSOM `other`.\n- Replace the provisional role evidence with curated recipe\
    \ or ontology\n  evidence, or remove `nutritional_roles` until that evidence is\
    \ available.\n"
- evidence_id: ev-28bce6da08c8c14e
  kind: prior_review
  reference: reviews/structured/20261011T024639Z-mim-reconcile-all-batch-12/review.yaml
  locator: findings[finding_id=f-54e5335934e0ba03]
  accessed_at: '2026-10-11T03:08:52Z'
  support: context_only
  summary: Exact earlier occurrence has open/confirmed status, based on exported-token
    presence and historical report text.
  snapshot_sha256: 20e55e956f704a8c90164bf2749b9ddf6c35d94cdcbab538776d0675aa150899
  quote: '{"category": "nomenclature", "certainty": "confirmed", "description": "Historical
    tokens are still present on the exact-subject SSSOM rows: [{\"reason\":\"unresolved
    recipe cross-reference in a resolving synonym\",\"token\":\"Trace mineral solution
    (see Medium No. 151 )\"},{\"reason\":\"unresolved recipe cross-reference in a
    resolving synonym\",\"token\":\"Trace mineral solution (see Medium No.852)\"}].
    Truncated concentration strings and context-dependent instructions need scoped
    curation. This check does not reject catalog/RAW_TEXT synonyms as a class.", "evidence_ids":
    ["ev-0eefc9d77ca437e5", "ev-702e1b26f74fa1cf"], "external_issues": ["https://github.com/CultureBotAI/MediaIngredientMech/issues/718"],
    "field_paths": ["synonyms", "SSSOM.other"], "finding_id": "f-54e5335934e0ba03",
    "issue_key": "mim-reconciliation-exported-context-tokens-4b03942a3427132e", "owner_paths":
    [{"path": "data/ingredients/mapped/Trace_Mineral_Solution.yaml", "repository":
    "CultureBotAI/MediaIngredientMech", "role": "maintained ingredient"}], "severity":
    "major", "status": "open", "tags": ["reconciliation", "bundle-by-owner", "exported-context-tokens"],
    "target_ids": ["record-4b03942a3427132e"], "title": "Review nonportable exported
    tokens: Trace mineral solution"}'
- evidence_id: ev-41b7b72cded4e05c
  kind: record_content
  reference: data/ingredients/mapped/Trace_Mineral_Solution.yaml
  locator: identifier, ontology_mapping, synonyms and curation_history
  accessed_at: '2026-10-11T03:08:52Z'
  support: partial
  summary: '{"candidate_labels": [{"source": "culturemech:output/ingredient_occurrences.tsv",
    "synonym_text": "Trace mineral solution (see Medium No. 151 )", "synonym_type":
    "RAW_TEXT"}, {"source": "culturemech:output/ingredient_occurrences.tsv", "synonym_text":
    "Trace mineral solution (see Medium No. 852 )", "synonym_type": "RAW_TEXT"}, {"source":
    "culturemech:output/ingredient_occurrences.tsv", "synonym_text": "Trace mineral
    solution (see Medium No.852)", "synonym_type": "RAW_TEXT"}, {"source": "culturemech:output/ingredient_occurrences.tsv",
    "synonym_text": "Trace mineral solution (see below)", "synonym_type": "RAW_TEXT"}],
    "history": [{"action": "CREATED_AS_UNMAPPED", "changes": "Imported from mim-queue
    (source_id=mediadive.ingredient:897); no CAS-RN or CHEBI/NCIT match. Curator review
    needed.", "curator": "audit_import_ingredients[mim-queue]", "llm_assisted": false,
    "new_status": "UNMAPPED", "timestamp": "2026-04-30T18:43:03.698454+00:00"}, {"action":
    "AUTO_CLASSIFY_INGREDIENT_TYPE", "changes": "set ingredient_type=STOCK_SOLUTION
    (name matches solution pattern ''mineral solution'')", "curator": "auto_classify_ingredient_type",
    "llm_assisted": false, "timestamp": "2026-05-02T03:12:19.966568+00:00"}, {"action":
    "PROMOTED_TO_MAPPED", "changes": "Promoted UNMAPPED_0551 -> kgmicrobe.ingredient:trace_mineral_solution
    (FALLBACK_REGISTRY). A named multi-component preparation. Searched CHEBI, NCIT,
    MeSH, FOODON and ENVO by label and synonym: no term denotes it, and none could
    -- a preparation is not a substance. Takes the STOCK_SOLUTION convention: a kgmicrobe.ingredient:
    mint with no parent, because a multi-component mix does not narrow to any single
    compound (#288).", "curator": "issue_288_stock_solutions", "llm_assisted": true,
    "new_status": "MAPPED", "previous_status": "UNMAPPED", "timestamp": "2026-08-06T00:00:00+00:00"},
    {"action": "CORRECTED", "changes": "occurrence_statistics 0/0 -> 2/2 (media_count/total_occurrences),
    derived from distinct CultureMech recipe ids in the #337 occurrence table. The
    prior values came from the importer retired in #453, whose media_count counted
    a list truncated to 50 examples (#449). [source=ingredient_occurrences.tsv culturemech_rev=15a4da5c08
    rows=194137 distinct_recipes=15257]", "curator": "refresh_occurrence_statistics",
    "timestamp": "2026-08-27T03:16:39.520310+00:00"}, {"action": "ADDED_SYNONYMS",
    "changes": "Added 5 CultureMech recipe surface form(s) that folded onto this record''s
    published label but were absent from MIM''s label index, so CultureMech could
    not resolve them: ''Trace mineral solution (see Medium No. 151 )'' (x2 CultureMech
    mentions); ''Trace mineral solution (see Medium No. 852 )'' (x1 CultureMech mentions);
    ''Trace mineral solution (see Medium No.852)'' (x1 CultureMech mentions); ''Trace
    mineral solution (see below)'' (x1 CultureMech mentions); ''Trace mineral solution**''
    (x1 CultureMech mentions). Source: culturemech:output/ingredient_occurrences.tsv.",
    "curator": "claude_culturemech_alias_backfill", "llm_assisted": false, "timestamp":
    "2026-08-30T04:48:06.233536+00:00"}], "identifier": "kgmicrobe.ingredient:trace_mineral_solution",
    "mapping": {"evidence": [{"evidence_type": "MANUAL_CURATION", "notes": "A named
    multi-component preparation. Searched CHEBI, NCIT, MeSH, FOODON and ENVO by label
    and synonym: no term denotes it, and none could -- a preparation is not a substance.
    Takes the STOCK_SOLUTION convention: a kgmicrobe.ingredient: mint with no parent,
    because a multi-component mix does not narrow to any single compound (#288).",
    "source": "MIM curation (#288)"}], "mapping_quality": "FALLBACK_REGISTRY", "ontology_id":
    "kgmicrobe.ingredient:trace_mineral_solution", "ontology_label": "Trace mineral
    solution", "ontology_source": "kgmicrobe.ingredient"}}'
  snapshot_sha256: 03837875ebc88c1ab82387c244b383de83a01bc77f4fd60cd75fbbecdcd31f81
- evidence_id: ev-3f611fd20092d7d4
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Trace_Mineral_Solution
  accessed_at: '2026-10-11T03:08:52Z'
  support: supports
  summary: '[{"comment": "", "confidence": "0.9", "data_row": 2807, "mapping_date":
    "2026-08-30", "mapping_justification": "semapv:ManualMappingCuration", "object_id":
    "kgmicrobe.ingredient:trace_mineral_solution", "object_label": "Trace mineral
    solution", "object_source": "kgm:ingredient", "other": "Trace mineral solution
    (see Medium No. 151 )|Trace mineral solution (see Medium No. 852 )|Trace mineral
    solution (see Medium No.852)|Trace mineral solution (see below)|Trace mineral
    solution**", "predicate_id": "skos:exactMatch", "source": "MIM:MIM curation (#288)|MIM:curator=claude_culturemech_alias_backfill",
    "subject_id": "MIM:Trace_Mineral_Solution", "subject_label": "Trace mineral solution",
    "validation_method": "none|UNKNOWN_TERM|2026-09-02"}]'
  snapshot_sha256: 2eae181f31d6433c20ffdb9dc2f8c8d7ad0a17a46a3189dea8c307fbc1c7b40e
- evidence_id: ev-ff886fb7448948d4
  kind: prior_review
  reference: reports/yaml_record_review/Trace_Mineral_Solution.md
  locator: Complete historical report, including Verdict and Recommended Edits
  accessed_at: '2026-10-11T03:08:52Z'
  support: context_only
  summary: Historical interpretation was read in full; it is not fresh source adjudication.
  snapshot_sha256: 95f2187e644085226dc05c4e6c0a2b3fc440fc600205141bc84c41b066625b34
  quote: "# `data/ingredients/mapped/Trace_Mineral_Solution.yaml`\n\n## Verdict\n\n\
    Needs curation, major. The local stock-solution identity is synchronized, but\n\
    all five raw CultureMech note variants leak into final SSSOM `other`.\n\n## Identity\n\
    \n- Reviewed record: `data/ingredients/mapped/Trace_Mineral_Solution.yaml`.\n\
    - Identifier and grounding: `identifier:\n  kgmicrobe.ingredient:trace_mineral_solution`\
    \ with matching\n  `ontology_mapping.ontology_id`, label `Trace mineral solution`,\
    \ source\n  `kgmicrobe.ingredient`, `mapping_quality: FALLBACK_REGISTRY`,\n  `mapping_status:\
    \ MAPPED`, and `ingredient_type: STOCK_SOLUTION`.\n- Synonyms: raw mim-queue source\
    \ form plus five raw CultureMech forms carrying\n  `see Medium`, `see below`,\
    \ or double-asterisk recipe notes.\n- Occurrences: 2 CultureMech recipe occurrences\
    \ in 2 media.\n\n## Validation\n\n- `uv run --frozen python scripts/validate_strict.py`\
    \ on the 5-file batch from\n  `Trace_Mineral_Solution` through `Trans-aconitic_Acid`:\
    \ exited 0 and wrote\n  zero ERROR rows.\n- Direct old Engine A/OBO term validation\
    \ was skipped for this row because\n  `kgmicrobe.ingredient` is a non-OBO local\
    \ registry prefix.\n- Local aggregate comparison found this per-record file synchronized\
    \ with its\n  keyed row in `data/curated/mapped_ingredients.yaml`.\n\n## Evidence\n\
    \n- The August issue 288 curation minted a local `kgmicrobe.ingredient` identity\n\
    \  after searching ChEBI, NCIT, MeSH, FOODON, and ENVO and retaining no parent\n\
    \  because a generic trace-mineral solution is a named multi-component\n  preparation.\n\
    - The final SSSOM row has\n  `MIM:Trace_Mineral_Solution skos:exactMatch\n  kgmicrobe.ingredient:trace_mineral_solution`\
    \ and exports five raw\n  CultureMech labels in `other`, including Medium No.\
    \ 151, Medium No. 852,\n  `see below`, and double-asterisk variants.\n\n## Issues\n\
    \n### Major: recipe cross-references and footnotes reach final `other`\n\n`Trace\
    \ mineral solution (see Medium No. 151 )`, `Trace mineral solution (see\nMedium\
    \ No. 852 )`, `Trace mineral solution (see Medium No.852)`, `Trace\nmineral solution\
    \ (see below)`, and `Trace mineral solution**` are recipe-local\ninstructions\
    \ or footnoted surfaces. They are occurrence aliases, not true\nsynonyms of the\
    \ local stock identity, and should not be exported.\n\n## Completeness\n\n- The\
    \ local identity, fallback registry mapping, occurrence count, aggregate\n  copy,\
    \ and final exact row agree.\n- No roles, components, parent ontology rows, or\
    \ chemical properties are\n  asserted.\n- The only issue is the leaked raw CultureMech\
    \ aliases.\n\n## Recommended Edits\n\n- Mark the five CultureMech aliases as non-exportable\
    \ raw source text so the\n  final SSSOM `other` column is empty for this row.\n"
- evidence_id: ev-e098338a3394e86d
  kind: prior_review
  reference: reviews/structured/20261011T024639Z-mim-reconcile-all-batch-12/review.yaml
  locator: findings[finding_id=f-0fa9eaef6cc34337]
  accessed_at: '2026-10-11T03:08:52Z'
  support: context_only
  summary: Exact earlier occurrence has open/confirmed status, based on exported-token
    presence and historical report text.
  snapshot_sha256: 20e55e956f704a8c90164bf2749b9ddf6c35d94cdcbab538776d0675aa150899
  quote: '{"category": "nomenclature", "certainty": "confirmed", "description": "Historical
    tokens are still present on the exact-subject SSSOM rows: [{\"reason\":\"unresolved
    recipe cross-reference in a resolving synonym\",\"token\":\"Trace minerals (see
    below)\"}]. Truncated concentration strings and context-dependent instructions
    need scoped curation. This check does not reject catalog/RAW_TEXT synonyms as
    a class.", "evidence_ids": ["ev-f3047b74cd613a2a", "ev-02edadefe666dbc3"], "external_issues":
    ["https://github.com/CultureBotAI/MediaIngredientMech/issues/718"], "field_paths":
    ["synonyms", "SSSOM.other"], "finding_id": "f-0fa9eaef6cc34337", "issue_key":
    "mim-reconciliation-exported-context-tokens-7c55027f9d88edd0", "owner_paths":
    [{"path": "data/ingredients/mapped/Trace_Minerals.yaml", "repository": "CultureBotAI/MediaIngredientMech",
    "role": "maintained ingredient"}], "severity": "major", "status": "open", "tags":
    ["reconciliation", "bundle-by-owner", "exported-context-tokens"], "target_ids":
    ["record-7c55027f9d88edd0"], "title": "Review nonportable exported tokens: Trace
    minerals"}'
- evidence_id: ev-2c39d54a6bcf5e1b
  kind: record_content
  reference: data/ingredients/mapped/Trace_Minerals.yaml
  locator: identifier, ontology_mapping, synonyms and curation_history
  accessed_at: '2026-10-11T03:08:52Z'
  support: partial
  summary: '{"candidate_labels": [{"source": "culturemech:output/ingredient_occurrences.tsv",
    "synonym_text": "Trace minerals (see below)", "synonym_type": "RAW_TEXT"}], "history":
    [{"action": "CREATED_AS_UNMAPPED", "changes": "Imported from mim-queue (source_id=mediadive.ingredient:1031);
    no CAS-RN or CHEBI/NCIT match. Curator review needed.", "curator": "audit_import_ingredients[mim-queue]",
    "llm_assisted": false, "new_status": "UNMAPPED", "timestamp": "2026-04-30T18:43:03.698454+00:00"},
    {"action": "REVIEWED_NON_IDENTITY_PARENT", "changes": "Reviewed OAK/OLS audit
    candidate MESH:D014131 Trace Elements; left unmapped because the source label
    denotes a trace-mineral ingredient/preparation, not identity with the full trace-elements
    ontology class.", "curator": "mediaingredientmech-agentic-curation", "llm_assisted":
    true, "new_status": "UNMAPPED", "previous_status": "UNMAPPED", "timestamp": "2026-05-11T07:50:00Z"},
    {"action": "CLASSIFIED_STOCK_SOLUTION", "changes": "Classified as a trace-mineral
    stock/pre-mix and left unmapped pending component-level recipe curation.", "curator":
    "mediaingredientmech-agentic-curation", "llm_assisted": true, "new_status": "UNMAPPED",
    "previous_status": "UNMAPPED", "timestamp": "2026-05-11T19:50:00Z"}, {"action":
    "PROMOTED_TO_MAPPED", "changes": "Promoted UNMAPPED_0552 -> kgmicrobe.ingredient:trace_minerals
    (FALLBACK_REGISTRY). A named multi-component preparation. Searched CHEBI, NCIT,
    MeSH, FOODON and ENVO by label and synonym: no term denotes it, and none could
    -- a preparation is not a substance. Takes the STOCK_SOLUTION convention: a kgmicrobe.ingredient:
    mint with no parent, because a multi-component mix does not narrow to any single
    compound (#288).", "curator": "issue_288_stock_solutions", "llm_assisted": true,
    "new_status": "MAPPED", "previous_status": "UNMAPPED", "timestamp": "2026-08-06T00:00:00+00:00"},
    {"action": "CORRECTED", "changes": "occurrence_statistics 0/0 -> 3/3 (media_count/total_occurrences),
    derived from distinct CultureMech recipe ids in the #337 occurrence table. The
    prior values came from the importer retired in #453, whose media_count counted
    a list truncated to 50 examples (#449). [source=ingredient_occurrences.tsv culturemech_rev=15a4da5c08
    rows=194137 distinct_recipes=15257]", "curator": "refresh_occurrence_statistics",
    "timestamp": "2026-08-27T03:16:39.520312+00:00"}, {"action": "ADDED_SYNONYMS",
    "changes": "Added 2 CultureMech recipe surface form(s) that folded onto this record''s
    published label but were absent from MIM''s label index, so CultureMech could
    not resolve them: ''Trace minerals (see below)'' (x2 CultureMech mentions); ''Trace
    minerals*'' (x1 CultureMech mentions). Source: culturemech:output/ingredient_occurrences.tsv.",
    "curator": "claude_culturemech_alias_backfill", "llm_assisted": false, "timestamp":
    "2026-08-30T04:48:06.233536+00:00"}], "identifier": "kgmicrobe.ingredient:trace_minerals",
    "mapping": {"evidence": [{"evidence_type": "MANUAL_CURATION", "notes": "A named
    multi-component preparation. Searched CHEBI, NCIT, MeSH, FOODON and ENVO by label
    and synonym: no term denotes it, and none could -- a preparation is not a substance.
    Takes the STOCK_SOLUTION convention: a kgmicrobe.ingredient: mint with no parent,
    because a multi-component mix does not narrow to any single compound (#288).",
    "source": "MIM curation (#288)"}], "mapping_quality": "FALLBACK_REGISTRY", "ontology_id":
    "kgmicrobe.ingredient:trace_minerals", "ontology_label": "Trace minerals", "ontology_source":
    "kgmicrobe.ingredient"}}'
  snapshot_sha256: 9a1b033572d1f6462d4de4d9f07d655e34f98fe37d82c2449d4a48cc2dadd1bc
- evidence_id: ev-ec1703c8dacbdf80
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Trace_Minerals
  accessed_at: '2026-10-11T03:08:52Z'
  support: supports
  summary: '[{"comment": "", "confidence": "0.9", "data_row": 2808, "mapping_date":
    "2026-08-30", "mapping_justification": "semapv:ManualMappingCuration", "object_id":
    "kgmicrobe.ingredient:trace_minerals", "object_label": "Trace minerals", "object_source":
    "kgm:ingredient", "other": "Trace minerals (see below)|Trace minerals*", "predicate_id":
    "skos:exactMatch", "source": "MIM:MIM curation (#288)|MIM:curator=claude_culturemech_alias_backfill",
    "subject_id": "MIM:Trace_Minerals", "subject_label": "Trace minerals", "validation_method":
    "none|UNKNOWN_TERM|2026-09-02"}]'
  snapshot_sha256: 2eae181f31d6433c20ffdb9dc2f8c8d7ad0a17a46a3189dea8c307fbc1c7b40e
- evidence_id: ev-649d543ff1a236ba
  kind: prior_review
  reference: reports/yaml_record_review/Trace_Minerals.md
  locator: Complete historical report, including Verdict and Recommended Edits
  accessed_at: '2026-10-11T03:08:52Z'
  support: context_only
  summary: Historical interpretation was read in full; it is not fresh source adjudication.
  snapshot_sha256: ca899d0e1e9ffdc149ed07abe32a65e07f563cffb61c30cddb9fbe01b22b47e5
  quote: "# `data/ingredients/mapped/Trace_Minerals.yaml`\n\n## Verdict\n\nNeeds curation,\
    \ major. The local trace-mineral stock/pre-mix identity is\nsynchronized, but\
    \ `see below` and starred raw source labels leak into final\nSSSOM `other`.\n\n\
    ## Identity\n\n- Reviewed record: `data/ingredients/mapped/Trace_Minerals.yaml`.\n\
    - Identifier and grounding: `identifier:\n  kgmicrobe.ingredient:trace_minerals`\
    \ with matching\n  `ontology_mapping.ontology_id`, label `Trace minerals`, source\n\
    \  `kgmicrobe.ingredient`, `mapping_quality: FALLBACK_REGISTRY`,\n  `mapping_status:\
    \ MAPPED`, `ingredient_type: STOCK_SOLUTION`, and\n  `solution_type: TRACE_METAL_MIX`.\n\
    - Synonyms: raw mim-queue source form plus raw CultureMech forms `Trace\n  minerals\
    \ (see below)` and `Trace minerals*`.\n- Occurrences: 3 CultureMech recipe occurrences\
    \ in 3 media.\n\n## Validation\n\n- `uv run --frozen python scripts/validate_strict.py`\
    \ on the 5-file batch from\n  `Trace_Mineral_Solution` through `Trans-aconitic_Acid`:\
    \ exited 0 and wrote\n  zero ERROR rows.\n- Direct old Engine A/OBO term validation\
    \ was skipped for this row because\n  `kgmicrobe.ingredient` is a non-OBO local\
    \ registry prefix.\n- Local aggregate comparison found this per-record file synchronized\
    \ with its\n  keyed row in `data/curated/mapped_ingredients.yaml`.\n\n## Evidence\n\
    \n- The May review rejected identity to the broad MeSH `Trace Elements` class,\n\
    \  and the August issue 288 curation minted a local identity for this\n  trace-mineral\
    \ stock/pre-mix.\n- The final SSSOM row has\n  `MIM:Trace_Minerals skos:exactMatch\
    \ kgmicrobe.ingredient:trace_minerals`\n  and exports `Trace minerals (see below)|Trace\
    \ minerals*` in `other`.\n\n## Issues\n\n### Major: recipe notes reach final `other`\n\
    \nBoth final `other` tokens are raw CultureMech occurrence labels. `see below`\n\
    is a recipe cross-reference and `*` is a footnote marker, so neither is a true\n\
    synonym of the local stock identity.\n\n## Completeness\n\n- The local identity,\
    \ fallback registry mapping, occurrence count, aggregate\n  copy, and final exact\
    \ row agree.\n- No roles, components, parent ontology rows, or chemical properties\
    \ are\n  asserted.\n- The only issue is the leaked raw CultureMech aliases.\n\n\
    ## Recommended Edits\n\n- Mark `Trace minerals (see below)` and `Trace minerals*`\
    \ as non-exportable raw\n  source text so the final SSSOM `other` column is empty\
    \ for this row.\n"
- evidence_id: ev-0701e78e991c4118
  kind: prior_review
  reference: reviews/structured/20261011T024639Z-mim-reconcile-all-batch-12/review.yaml
  locator: findings[finding_id=f-397b1df68e373137]
  accessed_at: '2026-10-11T03:08:52Z'
  support: context_only
  summary: Exact earlier occurrence has open/confirmed status, based on exported-token
    presence and historical report text.
  snapshot_sha256: 20e55e956f704a8c90164bf2749b9ddf6c35d94cdcbab538776d0675aa150899
  quote: '{"category": "nomenclature", "certainty": "confirmed", "description": "Historical
    tokens are still present on the exact-subject SSSOM rows: [{\"reason\":\"truncated
    concentration-qualified label with unbalanced parentheses\",\"token\":\"Yeast
    Extract (0.01 %\"}]. Truncated concentration strings and context-dependent instructions
    need scoped curation. This check does not reject catalog/RAW_TEXT synonyms as
    a class.", "evidence_ids": ["ev-d8b50ecf394b7a07", "ev-b4b66e47d09fff06"], "external_issues":
    ["https://github.com/CultureBotAI/MediaIngredientMech/issues/718"], "field_paths":
    ["synonyms", "SSSOM.other"], "finding_id": "f-397b1df68e373137", "issue_key":
    "mim-reconciliation-exported-context-tokens-4efe2f6907f0d4fc", "owner_paths":
    [{"path": "data/ingredients/mapped/Yeast_Extract.yaml", "repository": "CultureBotAI/MediaIngredientMech",
    "role": "maintained ingredient"}], "severity": "major", "status": "open", "tags":
    ["reconciliation", "bundle-by-owner", "exported-context-tokens"], "target_ids":
    ["record-4efe2f6907f0d4fc"], "title": "Review nonportable exported tokens: Yeast
    extract"}'
- evidence_id: ev-5175fd560468ba85
  kind: record_content
  reference: data/ingredients/mapped/Yeast_Extract.yaml
  locator: identifier, ontology_mapping, synonyms and curation_history
  accessed_at: '2026-10-11T03:08:52Z'
  support: partial
  summary: '{"candidate_labels": [{"source": "microbedecoder", "synonym_text": "Yeast
    Extract (0.01 %", "synonym_type": "RAW_TEXT"}], "history": [{"action": "IMPORTED",
    "changes": "Initial import from CultureMech pipeline", "curator": "import_from_culturemech",
    "llm_assisted": false, "new_status": "UNMAPPED", "timestamp": "2026-03-09T06:54:18.022301+00:00"},
    {"action": "ADDED_CAS_RN", "changes": "Added CAS-RN:8013-01-2 from CultureBotHT
    compound mappings", "curator": "integrate_cas_rn_from_culturebot_ht", "llm_assisted":
    false, "new_status": "UNMAPPED", "timestamp": "2026-04-05T17:53:47.291847+00:00"},
    {"action": "MAPPED", "changes": "Promoted commercial food-mixture surface forms
    with FOODON:03315426 (yeast extract). Added brand/catalog variants as synonyms.",
    "curator": "foodon_promotion_cbclaw", "llm_assisted": true, "new_status": "MAPPED",
    "timestamp": "2026-04-18T04:19:36+00:00"}, {"action": "AUTO_CLASSIFY_INGREDIENT_TYPE",
    "changes": "set ingredient_type=UNDEFINED_MIXTURE (name matches complex pattern
    ''Yeast'')", "curator": "auto_classify_ingredient_type", "llm_assisted": false,
    "timestamp": "2026-05-01T07:35:36.939492+00:00"}, {"action": "AUTO_CLASSIFY_INGREDIENT_TYPE",
    "changes": "set ingredient_type=UNDEFINED_MIXTURE (name matches complex pattern
    ''Yeast'')", "curator": "auto_classify_ingredient_type", "llm_assisted": false,
    "timestamp": "2026-05-02T03:12:19.307519+00:00"}, {"action": "ANNOTATED", "changes":
    "Added media role: PROTEIN_SOURCE (confidence: 0.80)", "curator": "infer_roles_from_name_lists",
    "timestamp": "2026-06-03T02:06:01.753916+00:00"}, {"action": "ANNOTATED", "changes":
    "Migrated legacy media_roles to role facets (#128): PROTEIN_SOURCE -> nutritional_roles.PROTEIN_SOURCE",
    "curator": "migrate_media_roles_to_facets", "timestamp": "2026-07-20T00:00:00+00:00"},
    {"action": "MERGED_FROM_UNMAPPED_DUPLICATE", "changes": "Absorbed UNMAPPED_0700
    ''Yeast Extract (0.01 %'' as a RAW_TEXT synonym -- concentration-truncated duplicate
    of yeast extract. No new SSSOM row; FOODON:03315426 is already mapped. Source:
    kgmicrobe.trait:yeast_extract_0_01.", "curator": "microbedecoder-residual-dispositions",
    "llm_assisted": true, "timestamp": "2026-08-05T00:01:30.894952+00:00"}, {"action":
    "CORRECTED", "changes": "occurrence_statistics 5/5 -> 7617/7697 (media_count/total_occurrences),
    derived from distinct CultureMech recipe ids in the #337 occurrence table. The
    prior values came from the importer retired in #453, whose media_count counted
    a list truncated to 50 examples (#449). [source=ingredient_occurrences.tsv culturemech_rev=15a4da5c08
    rows=194137 distinct_recipes=15257]", "curator": "refresh_occurrence_statistics",
    "timestamp": "2026-08-27T03:16:39.520171+00:00"}, {"action": "ADDED_SYNONYMS",
    "changes": "Added 1 CultureMech recipe surface form(s) that folded onto this record''s
    published label but were absent from MIM''s label index, so CultureMech could
    not resolve them: ''Fresh Baker\u2019s Yeast Extract'' (x1 CultureMech mentions).
    Source: culturemech:output/ingredient_occurrences.tsv.", "curator": "claude_culturemech_alias_backfill",
    "llm_assisted": false, "timestamp": "2026-08-30T04:48:06.233536+00:00"}], "identifier":
    "FOODON:03315426", "mapping": {"evidence": [{"evidence_type": "CURATOR_JUDGMENT",
    "notes": "Commercial food mixture - FOODON is correct parent ontology (not CHEBI,
    since yeast extract is a multi-component food extract, not a single chemical).",
    "source": "cbclaw_foodon_promotion"}], "mapping_quality": "EXACT_MATCH", "ontology_id":
    "FOODON:03315426", "ontology_label": "yeast extract", "ontology_source": "FOODON"}}'
  snapshot_sha256: e7cdc5aa92020487a97c08814514fa48b852ff48c78a1d1890b69afaaf372d28
- evidence_id: ev-c84617d1a202e069
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Yeast_Extract
  accessed_at: '2026-10-11T03:08:52Z'
  support: supports
  summary: '[{"comment": "", "confidence": "0.99", "data_row": 2949, "mapping_date":
    "2026-08-30", "mapping_justification": "semapv:LexicalMatching", "object_id":
    "FOODON:03315426", "object_label": "yeast extract", "object_source": "obo:foodon.owl",
    "other": "Yeast extract(Bacto, Difco)|Yeast extract(CAS: 8013-01-2)|Yeast extract
    (BD-Difco)|Bacto Yeast Extract (Difco)|Yeast extract (OXOID)|Bacto yeast extract|Yeast
    extract (Difco)|Yeast extract (BD--Difco)|Yeast Extract (BD 212750)|Yeast extract
    (Difco or Oxoid)|Yeast extract (BD Bacto)|Bacto Yeast  Extract (Difco)|Yeast extract
    (BD-BBL)|Yeast extract (Oxoid LP0021, BD 212750)|Yeast Extract (BD 211928)|Difco
    Bacto-yeast extract|Dried yeast extract S (Wako)|Yeast Extract (BD, 212750)|Yeast
    extract(Oxoid)|Yeast extract (BBL)|Bacto-yeast extract|Yeast Extract(Difco)|yeast
    extract (BD Difco)|yeast extract (Nacalai Tesque, Kyoto, Japan)|Yeast Extract
    (Hardy C7340)|Liquid yeast extract (Flow)|Fresh Baker''s Yeast Extract|Yeast Extract
    (0.01 %|Fresh Baker\u2019s Yeast Extract|CAS:8013-01-2", "predicate_id": "skos:exactMatch",
    "source": "MIM:cbclaw_foodon_promotion|MIM:curator=claude_culturemech_alias_backfill",
    "subject_id": "MIM:Yeast_Extract", "subject_label": "Yeast extract", "validation_method":
    "OLS:foodon|SYNONYM_ENRICH|2026-07-07"}]'
  snapshot_sha256: 2eae181f31d6433c20ffdb9dc2f8c8d7ad0a17a46a3189dea8c307fbc1c7b40e
- evidence_id: ev-ef345ac5a6dc1108
  kind: prior_review
  reference: reports/yaml_record_review/Yeast_Extract.md
  locator: Complete historical report, including Verdict and Recommended Edits
  accessed_at: '2026-10-11T03:08:52Z'
  support: context_only
  summary: Historical interpretation was read in full; it is not fresh source adjudication.
  snapshot_sha256: e1920c4292a8d9d9155fcb45d62306b5f2f645732eac0501e49b634c3d4c6d73
  quote: "# `data/ingredients/mapped/Yeast_Extract.yaml`\n\n## Verdict\n\nNeeds curation.\
    \ The exact `FOODON:03315426` yeast extract identity, aggregate\nrow, and final\
    \ exact SSSOM predicate pass, but final SSSOM exports many\nvendor/catalog variants\
    \ plus a truncated concentration string, and the\n`PROTEIN_SOURCE` role is still\
    \ a provisional name-pattern inference.\n\n## Identity\n\n- Reviewed record: `data/ingredients/mapped/Yeast_Extract.yaml`.\n\
    - Identifier and grounding: `identifier: FOODON:03315426` with matching\n  `ontology_mapping.ontology_id`,\
    \ label `yeast extract`, source `FOODON`,\n  `mapping_quality: EXACT_MATCH`, `mapping_status:\
    \ MAPPED`, and\n  `ingredient_type: UNDEFINED_MIXTURE`.\n- CAS RN: `8013-01-2`.\n\
    - Synonyms: raw CultureMech and MicrobeDecoder strings, exact yeast-extract\n\
    \  synonyms, related Fresh Baker labels, and many manual catalog variants.\n-\
    \ Occurrences: 7,697 total occurrences across 7,617 CultureMech media, plus 46\n\
    \  MicrobeDecoder metabolite-utilization occurrences.\n- Role: `PROTEIN_SOURCE`\
    \ with provisional curated name-pattern evidence.\n\n## Validation\n\n- `uv run\
    \ --frozen python scripts/validate_strict.py` on the 5-file batch from\n  `Xylotriose`\
    \ through `Yeast_Extract_Gluconate`: exited 0 and wrote zero ERROR\n  rows.\n\
    - Local aggregate comparison found this per-record file synchronized with its\n\
    \  keyed row in `data/curated/mapped_ingredients.yaml`.\n- Engine A label validation\
    \ was limited to the CHEBI-primary record in this\n  batch; this FoodOn row has\
    \ no CHEBI/OBO adapter for that focused check.\n\n## Evidence\n\n- Fresh OLS4\
    \ exact-label search for `yeast extract` in FoodOn found active\n  `FOODON:03315426`\
    \ with label `yeast extract`.\n- The final SSSOM row correctly has\n  `MIM:Yeast_Extract\
    \ skos:exactMatch FOODON:03315426`.\n- The final SSSOM row filters the exact duplicate\
    \ `Yeast Extract` and\n  `yeast extract` strings but still exports raw and catalog-qualified\
    \ labels.\n\n## Issues\n\n- Major: the final exact `FOODON:03315426` row exports\
    \ many vendor/catalog\n  labels as `other` synonyms, including BD, Difco, Oxoid,\
    \ BBL, Nacalai Tesque,\n  Hardy, Wako, and Flow product-specific strings.\n- Major:\
    \ the same final row exports the truncated concentration string\n  `Yeast Extract\
    \ (0.01 %`, which is not a complete or reusable synonym.\n- Major: the same final\
    \ row also exports source-decorated raw strings such as\n  `Yeast extract(CAS:\
    \ 8013-01-2)` and the duplicate Fresh Baker label with a\n  non-ASCII curly apostrophe.\n\
    - Major: `nutritional_roles.PROTEIN_SOURCE` rests on\n  `COMPUTATIONAL_PREDICTION`\
    \ evidence whose note says the curated name-pattern\n  rule is provisional and\
    \ still needs review.\n\n## Completeness\n\n- The exact FoodOn mapping, occurrence\
    \ count, aggregate copy, and final SSSOM\n  predicate agree.\n- The final synonym\
    \ set needs to be reduced to true yeast-extract labels.\n\n## Recommended Edits\n\
    \n- Remove or suppress raw CAS-decorated, concentration-truncated, non-ASCII\n\
    \  duplicate, and vendor/catalog-specific labels from final SSSOM `other`.\n-\
    \ Replace or remove this record's `PROTEIN_SOURCE` role; keep it only if a\n \
    \ maintained source supports yeast extract as a protein source in media.\n- Rebuild\
    \ SSSOM and rerun strict validation, SSSOM invariant validation, and the\n  cross-record\
    \ `other` synonym audit.\n"
assessments:
- assessment_id: scope-f-be91e29ea6694d28
  area: nomenclature
  topic: Certainty correction for the exact token observation
  outcome: unknown
  summary: Token presence remains reproducible, but the earlier pattern-based observation
    did not establish whether the exact source label denotes this subject or a different
    preparation. Fresh source-context adjudication is required before a confirmed
    defect or label removal. This successor corrects certainty only; it does not establish
    that the token is valid or that another identity allegation is fixed. The historical
    report separately alleges trace-mineral/4-vinylphenol identity conflation. That
    stronger claim remains in the original report and narrative reassessment; the
    recipe-pointer heuristic neither adjudicates nor retires it.
  target_ids:
  - record-88ed3645c26c14b6
  evidence_ids:
  - ev-823412d1eacb6795
  - ev-f983f8801d1e4699
  - ev-d8b130cb30e86aec
  - ev-0de8553689e72bef
  - ev-93f74be01346ddd4
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Source-scope question only, not a disposition of the complete historical
      report.
    evidence_ids:
    - ev-823412d1eacb6795
    - ev-f983f8801d1e4699
    - ev-d8b130cb30e86aec
    - ev-0de8553689e72bef
    - ev-93f74be01346ddd4
- assessment_id: scope-f-e1004757f90e8c13
  area: nomenclature
  topic: Certainty correction for the exact token observation
  outcome: unknown
  summary: Token presence remains reproducible, but the earlier pattern-based observation
    did not establish whether the exact source label denotes this subject or a different
    preparation. Fresh source-context adjudication is required before a confirmed
    defect or label removal. This successor corrects certainty only; it does not establish
    that the token is valid or that another identity allegation is fixed. The historical
    report actually passes the record and explicitly accepts the raw source surface;
    attributing an unresolved token concern to that report was incorrect. No new source
    evidence was supplied to overturn its scoped conclusion.
  target_ids:
  - record-205c79d137874075
  evidence_ids:
  - ev-823412d1eacb6795
  - ev-8fab9fb02ee4454f
  - ev-f5500c887f4dc734
  - ev-16c562c2dbdbab95
  - ev-8ca93b32516cbb52
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Source-scope question only, not a disposition of the complete historical
      report.
    evidence_ids:
    - ev-823412d1eacb6795
    - ev-8fab9fb02ee4454f
    - ev-f5500c887f4dc734
    - ev-16c562c2dbdbab95
    - ev-8ca93b32516cbb52
- assessment_id: scope-f-838d67873b6673db
  area: nomenclature
  topic: Certainty correction for the exact token observation
  outcome: unknown
  summary: Token presence remains reproducible, but the earlier pattern-based observation
    did not establish whether the exact source label denotes this subject or a different
    preparation. Fresh source-context adjudication is required before a confirmed
    defect or label removal. This successor corrects certainty only; it does not establish
    that the token is valid or that another identity allegation is fixed. The historical
    report actually passes the record and explicitly accepts the raw source surface;
    attributing an unresolved token concern to that report was incorrect. No new source
    evidence was supplied to overturn its scoped conclusion.
  target_ids:
  - record-9122c364d42e8559
  evidence_ids:
  - ev-823412d1eacb6795
  - ev-e6798c510d069e5f
  - ev-f0c42034b2f08a1d
  - ev-82824a1888d907ee
  - ev-0bef314ac38155d7
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Source-scope question only, not a disposition of the complete historical
      report.
    evidence_ids:
    - ev-823412d1eacb6795
    - ev-e6798c510d069e5f
    - ev-f0c42034b2f08a1d
    - ev-82824a1888d907ee
    - ev-0bef314ac38155d7
- assessment_id: scope-f-320ccfb6bddc74ee
  area: nomenclature
  topic: Certainty correction for the exact token observation
  outcome: unknown
  summary: Token presence remains reproducible, but the earlier pattern-based observation
    did not establish whether the exact source label denotes this subject or a different
    preparation. Fresh source-context adjudication is required before a confirmed
    defect or label removal. This successor corrects certainty only; it does not establish
    that the token is valid or that another identity allegation is fixed.
  target_ids:
  - record-797da68010f27377
  evidence_ids:
  - ev-823412d1eacb6795
  - ev-9477d91976d0a888
  - ev-4d30788725c98994
  - ev-a255c9d3059064fe
  - ev-e7674a969ec8d8cb
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Source-scope question only, not a disposition of the complete historical
      report.
    evidence_ids:
    - ev-823412d1eacb6795
    - ev-9477d91976d0a888
    - ev-4d30788725c98994
    - ev-a255c9d3059064fe
    - ev-e7674a969ec8d8cb
- assessment_id: scope-f-853c7e2e707eedfc
  area: nomenclature
  topic: Certainty correction for the exact token observation
  outcome: unknown
  summary: Token presence remains reproducible, but the earlier pattern-based observation
    did not establish whether the exact source label denotes this subject or a different
    preparation. Fresh source-context adjudication is required before a confirmed
    defect or label removal. This successor corrects certainty only; it does not establish
    that the token is valid or that another identity allegation is fixed.
  target_ids:
  - record-099e2c8a2a9f8f68
  evidence_ids:
  - ev-823412d1eacb6795
  - ev-997c904ed0a9e395
  - ev-66223de2980eb719
  - ev-6b0f037f5dc84aa9
  - ev-abc54f67fc204f62
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Source-scope question only, not a disposition of the complete historical
      report.
    evidence_ids:
    - ev-823412d1eacb6795
    - ev-997c904ed0a9e395
    - ev-66223de2980eb719
    - ev-6b0f037f5dc84aa9
    - ev-abc54f67fc204f62
- assessment_id: scope-f-43e56706181e97b8
  area: nomenclature
  topic: Certainty correction for the exact token observation
  outcome: unknown
  summary: Token presence remains reproducible, but the earlier pattern-based observation
    did not establish whether the exact source label denotes this subject or a different
    preparation. Fresh source-context adjudication is required before a confirmed
    defect or label removal. This successor corrects certainty only; it does not establish
    that the token is valid or that another identity allegation is fixed. A damaged
    spelling is observable, but the mapping contract permits damaged raw source forms
    when they still resolve to the same substance; malformed punctuation alone does
    not settle identity scope.
  target_ids:
  - record-7059116102e92505
  evidence_ids:
  - ev-823412d1eacb6795
  - ev-b91360770608ed24
  - ev-423b314156ab28a8
  - ev-f25801a7e385fb14
  - ev-5458c3c3defc38d0
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Source-scope question only, not a disposition of the complete historical
      report.
    evidence_ids:
    - ev-823412d1eacb6795
    - ev-b91360770608ed24
    - ev-423b314156ab28a8
    - ev-f25801a7e385fb14
    - ev-5458c3c3defc38d0
- assessment_id: scope-f-d3696f2daf45c433
  area: nomenclature
  topic: Certainty correction for the exact token observation
  outcome: unknown
  summary: Token presence remains reproducible, but the earlier pattern-based observation
    did not establish whether the exact source label denotes this subject or a different
    preparation. Fresh source-context adjudication is required before a confirmed
    defect or label removal. This successor corrects certainty only; it does not establish
    that the token is valid or that another identity allegation is fixed.
  target_ids:
  - record-4253636d94bcf2f1
  evidence_ids:
  - ev-823412d1eacb6795
  - ev-a1a7bf32cb2806bb
  - ev-5830b871d91efa8c
  - ev-7c6192e7f288bdf0
  - ev-1659306e55f45a0b
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Source-scope question only, not a disposition of the complete historical
      report.
    evidence_ids:
    - ev-823412d1eacb6795
    - ev-a1a7bf32cb2806bb
    - ev-5830b871d91efa8c
    - ev-7c6192e7f288bdf0
    - ev-1659306e55f45a0b
- assessment_id: scope-f-5982691d4b3d176b
  area: nomenclature
  topic: Certainty correction for the exact token observation
  outcome: unknown
  summary: Token presence remains reproducible, but the earlier pattern-based observation
    did not establish whether the exact source label denotes this subject or a different
    preparation. Fresh source-context adjudication is required before a confirmed
    defect or label removal. This successor corrects certainty only; it does not establish
    that the token is valid or that another identity allegation is fixed. A damaged
    spelling is observable, but the mapping contract permits damaged raw source forms
    when they still resolve to the same substance; malformed punctuation alone does
    not settle identity scope.
  target_ids:
  - record-62f485f9f7517526
  evidence_ids:
  - ev-823412d1eacb6795
  - ev-54e6930eaaa55145
  - ev-0bdc1c0fd578d2ef
  - ev-a926e5411d840793
  - ev-f56ebea344bcd264
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Source-scope question only, not a disposition of the complete historical
      report.
    evidence_ids:
    - ev-823412d1eacb6795
    - ev-54e6930eaaa55145
    - ev-0bdc1c0fd578d2ef
    - ev-a926e5411d840793
    - ev-f56ebea344bcd264
- assessment_id: scope-f-f582ea830b4f370d
  area: nomenclature
  topic: Certainty correction for the exact token observation
  outcome: unknown
  summary: Token presence remains reproducible, but the earlier pattern-based observation
    did not establish whether the exact source label denotes this subject or a different
    preparation. Fresh source-context adjudication is required before a confirmed
    defect or label removal. This successor corrects certainty only; it does not establish
    that the token is valid or that another identity allegation is fixed.
  target_ids:
  - record-4190c0ee5976447a
  evidence_ids:
  - ev-823412d1eacb6795
  - ev-8bb59eaf8b6e66f4
  - ev-745bc0e8e18adc16
  - ev-7d01fe3478491965
  - ev-a692d3e165ce1613
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Source-scope question only, not a disposition of the complete historical
      report.
    evidence_ids:
    - ev-823412d1eacb6795
    - ev-8bb59eaf8b6e66f4
    - ev-745bc0e8e18adc16
    - ev-7d01fe3478491965
    - ev-a692d3e165ce1613
- assessment_id: scope-f-b7808e84d7886285
  area: nomenclature
  topic: Certainty correction for the exact token observation
  outcome: unknown
  summary: Token presence remains reproducible, but the earlier pattern-based observation
    did not establish whether the exact source label denotes this subject or a different
    preparation. Fresh source-context adjudication is required before a confirmed
    defect or label removal. This successor corrects certainty only; it does not establish
    that the token is valid or that another identity allegation is fixed.
  target_ids:
  - record-59776f859c41300d
  evidence_ids:
  - ev-823412d1eacb6795
  - ev-032b61a7a21ed47b
  - ev-d59510b4ad4c4456
  - ev-1dfdb8319038a4fb
  - ev-a809b48a4c5a84c5
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Source-scope question only, not a disposition of the complete historical
      report.
    evidence_ids:
    - ev-823412d1eacb6795
    - ev-032b61a7a21ed47b
    - ev-d59510b4ad4c4456
    - ev-1dfdb8319038a4fb
    - ev-a809b48a4c5a84c5
- assessment_id: scope-f-2680803ffb7b7f40
  area: nomenclature
  topic: Certainty correction for the exact token observation
  outcome: unknown
  summary: Token presence remains reproducible, but the earlier pattern-based observation
    did not establish whether the exact source label denotes this subject or a different
    preparation. Fresh source-context adjudication is required before a confirmed
    defect or label removal. This successor corrects certainty only; it does not establish
    that the token is valid or that another identity allegation is fixed.
  target_ids:
  - record-c6cdd023283a1f0a
  evidence_ids:
  - ev-823412d1eacb6795
  - ev-6c06e714e86355c6
  - ev-b62c98e3d0a1e1d5
  - ev-d4f1e238a85e0e57
  - ev-de40a4caf98a1085
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Source-scope question only, not a disposition of the complete historical
      report.
    evidence_ids:
    - ev-823412d1eacb6795
    - ev-6c06e714e86355c6
    - ev-b62c98e3d0a1e1d5
    - ev-d4f1e238a85e0e57
    - ev-de40a4caf98a1085
- assessment_id: scope-f-ef4889c5708c1269
  area: nomenclature
  topic: Certainty correction for the exact token observation
  outcome: unknown
  summary: Token presence remains reproducible, but the earlier pattern-based observation
    did not establish whether the exact source label denotes this subject or a different
    preparation. Fresh source-context adjudication is required before a confirmed
    defect or label removal. This successor corrects certainty only; it does not establish
    that the token is valid or that another identity allegation is fixed.
  target_ids:
  - record-3245d67aff586e82
  evidence_ids:
  - ev-823412d1eacb6795
  - ev-4f670ddc934d5e74
  - ev-927f64381fa816f2
  - ev-1edf0a1870e81e81
  - ev-cefe2423553074dc
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Source-scope question only, not a disposition of the complete historical
      report.
    evidence_ids:
    - ev-823412d1eacb6795
    - ev-4f670ddc934d5e74
    - ev-927f64381fa816f2
    - ev-1edf0a1870e81e81
    - ev-cefe2423553074dc
- assessment_id: scope-f-3b7b7b7cd4c70ace
  area: nomenclature
  topic: Certainty correction for the exact token observation
  outcome: unknown
  summary: Token presence remains reproducible, but the earlier pattern-based observation
    did not establish whether the exact source label denotes this subject or a different
    preparation. Fresh source-context adjudication is required before a confirmed
    defect or label removal. This successor corrects certainty only; it does not establish
    that the token is valid or that another identity allegation is fixed. A damaged
    spelling is observable, but the mapping contract permits damaged raw source forms
    when they still resolve to the same substance; malformed punctuation alone does
    not settle identity scope.
  target_ids:
  - record-341efa75278b5e50
  evidence_ids:
  - ev-823412d1eacb6795
  - ev-61509143d0ecf84a
  - ev-cb42f25983a0ad30
  - ev-775e49cc5333c85a
  - ev-a18de57ffdc5d750
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Source-scope question only, not a disposition of the complete historical
      report.
    evidence_ids:
    - ev-823412d1eacb6795
    - ev-61509143d0ecf84a
    - ev-cb42f25983a0ad30
    - ev-775e49cc5333c85a
    - ev-a18de57ffdc5d750
- assessment_id: scope-f-612aa67bad26d26a
  area: nomenclature
  topic: Certainty correction for the exact token observation
  outcome: unknown
  summary: Token presence remains reproducible, but the earlier pattern-based observation
    did not establish whether the exact source label denotes this subject or a different
    preparation. Fresh source-context adjudication is required before a confirmed
    defect or label removal. This successor corrects certainty only; it does not establish
    that the token is valid or that another identity allegation is fixed.
  target_ids:
  - record-78ea6a14a080dbf0
  evidence_ids:
  - ev-823412d1eacb6795
  - ev-666a0e05df6eee3c
  - ev-995ddb5e1dd7c309
  - ev-3e284f13241fa94e
  - ev-a6e7432b5d0fbcfb
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Source-scope question only, not a disposition of the complete historical
      report.
    evidence_ids:
    - ev-823412d1eacb6795
    - ev-666a0e05df6eee3c
    - ev-995ddb5e1dd7c309
    - ev-3e284f13241fa94e
    - ev-a6e7432b5d0fbcfb
- assessment_id: scope-f-54e5335934e0ba03
  area: nomenclature
  topic: Certainty correction for the exact token observation
  outcome: unknown
  summary: Token presence remains reproducible, but the earlier pattern-based observation
    did not establish whether the exact source label denotes this subject or a different
    preparation. Fresh source-context adjudication is required before a confirmed
    defect or label removal. This successor corrects certainty only; it does not establish
    that the token is valid or that another identity allegation is fixed.
  target_ids:
  - record-4b03942a3427132e
  evidence_ids:
  - ev-823412d1eacb6795
  - ev-28bce6da08c8c14e
  - ev-41b7b72cded4e05c
  - ev-3f611fd20092d7d4
  - ev-ff886fb7448948d4
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Source-scope question only, not a disposition of the complete historical
      report.
    evidence_ids:
    - ev-823412d1eacb6795
    - ev-28bce6da08c8c14e
    - ev-41b7b72cded4e05c
    - ev-3f611fd20092d7d4
    - ev-ff886fb7448948d4
- assessment_id: scope-f-0fa9eaef6cc34337
  area: nomenclature
  topic: Certainty correction for the exact token observation
  outcome: unknown
  summary: Token presence remains reproducible, but the earlier pattern-based observation
    did not establish whether the exact source label denotes this subject or a different
    preparation. Fresh source-context adjudication is required before a confirmed
    defect or label removal. This successor corrects certainty only; it does not establish
    that the token is valid or that another identity allegation is fixed.
  target_ids:
  - record-7c55027f9d88edd0
  evidence_ids:
  - ev-823412d1eacb6795
  - ev-e098338a3394e86d
  - ev-2c39d54a6bcf5e1b
  - ev-ec1703c8dacbdf80
  - ev-649d543ff1a236ba
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Source-scope question only, not a disposition of the complete historical
      report.
    evidence_ids:
    - ev-823412d1eacb6795
    - ev-e098338a3394e86d
    - ev-2c39d54a6bcf5e1b
    - ev-ec1703c8dacbdf80
    - ev-649d543ff1a236ba
- assessment_id: scope-f-397b1df68e373137
  area: nomenclature
  topic: Certainty correction for the exact token observation
  outcome: unknown
  summary: Token presence remains reproducible, but the earlier pattern-based observation
    did not establish whether the exact source label denotes this subject or a different
    preparation. Fresh source-context adjudication is required before a confirmed
    defect or label removal. This successor corrects certainty only; it does not establish
    that the token is valid or that another identity allegation is fixed. A damaged
    spelling is observable, but the mapping contract permits damaged raw source forms
    when they still resolve to the same substance; malformed punctuation alone does
    not settle identity scope.
  target_ids:
  - record-4efe2f6907f0d4fc
  evidence_ids:
  - ev-823412d1eacb6795
  - ev-0701e78e991c4118
  - ev-5175fd560468ba85
  - ev-c84617d1a202e069
  - ev-ef345ac5a6dc1108
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Source-scope question only, not a disposition of the complete historical
      report.
    evidence_ids:
    - ev-823412d1eacb6795
    - ev-0701e78e991c4118
    - ev-5175fd560468ba85
    - ev-c84617d1a202e069
    - ev-ef345ac5a6dc1108
findings:
- finding_id: scope-f-be91e29ea6694d28
  issue_key: mim-reconciliation-exported-context-tokens-88ed3645c26c14b6
  category: nomenclature
  severity: major
  status: deferred
  certainty: provisional
  title: 'Adjudicate source scope of exported tokens: 4-vinylphenol'
  description: Token presence remains reproducible, but the earlier pattern-based
    observation did not establish whether the exact source label denotes this subject
    or a different preparation. Fresh source-context adjudication is required before
    a confirmed defect or label removal. This successor corrects certainty only; it
    does not establish that the token is valid or that another identity allegation
    is fixed. The historical report separately alleges trace-mineral/4-vinylphenol
    identity conflation. That stronger claim remains in the original report and narrative
    reassessment; the recipe-pointer heuristic neither adjudicates nor retires it.
  target_ids:
  - record-88ed3645c26c14b6
  evidence_ids:
  - ev-823412d1eacb6795
  - ev-f983f8801d1e4699
  - ev-d8b130cb30e86aec
  - ev-0de8553689e72bef
  - ev-93f74be01346ddd4
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/4-vinylphenol.yaml
    role: maintained ingredient
  field_paths:
  - synonyms
  - SSSOM.other
  tags:
  - reconciliation
  - bundle-by-owner
  - exported-context-tokens
  external_issues:
  - https://github.com/CultureBotAI/MediaIngredientMech/issues/718
  - https://github.com/CultureBotAI/MediaIngredientMech/issues/861
  disposition_reason: Token presence remains reproducible, but the earlier pattern-based
    observation did not establish whether the exact source label denotes this subject
    or a different preparation. Fresh source-context adjudication is required before
    a confirmed defect or label removal. This successor corrects certainty only; it
    does not establish that the token is valid or that another identity allegation
    is fixed. The historical report separately alleges trace-mineral/4-vinylphenol
    identity conflation. That stronger claim remains in the original report and narrative
    reassessment; the recipe-pointer heuristic neither adjudicates nor retires it.
  previous_occurrences:
  - repository: CultureBotAI/MediaIngredientMech
    review_id: 20261011T024630Z-mim-reconcile-all-batch-02
    finding_id: f-be91e29ea6694d28
- finding_id: scope-f-e1004757f90e8c13
  issue_key: mim-reconciliation-exported-context-tokens-205c79d137874075
  category: nomenclature
  severity: major
  status: deferred
  certainty: provisional
  title: 'Adjudicate source scope of exported tokens: Artificial seawater'
  description: Token presence remains reproducible, but the earlier pattern-based
    observation did not establish whether the exact source label denotes this subject
    or a different preparation. Fresh source-context adjudication is required before
    a confirmed defect or label removal. This successor corrects certainty only; it
    does not establish that the token is valid or that another identity allegation
    is fixed. The historical report actually passes the record and explicitly accepts
    the raw source surface; attributing an unresolved token concern to that report
    was incorrect. No new source evidence was supplied to overturn its scoped conclusion.
  target_ids:
  - record-205c79d137874075
  evidence_ids:
  - ev-823412d1eacb6795
  - ev-8fab9fb02ee4454f
  - ev-f5500c887f4dc734
  - ev-16c562c2dbdbab95
  - ev-8ca93b32516cbb52
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Artificial_seawater.yaml
    role: maintained ingredient
  field_paths:
  - synonyms
  - SSSOM.other
  tags:
  - reconciliation
  - bundle-by-owner
  - exported-context-tokens
  external_issues:
  - https://github.com/CultureBotAI/MediaIngredientMech/issues/718
  - https://github.com/CultureBotAI/MediaIngredientMech/issues/861
  disposition_reason: Token presence remains reproducible, but the earlier pattern-based
    observation did not establish whether the exact source label denotes this subject
    or a different preparation. Fresh source-context adjudication is required before
    a confirmed defect or label removal. This successor corrects certainty only; it
    does not establish that the token is valid or that another identity allegation
    is fixed. The historical report actually passes the record and explicitly accepts
    the raw source surface; attributing an unresolved token concern to that report
    was incorrect. No new source evidence was supplied to overturn its scoped conclusion.
  previous_occurrences:
  - repository: CultureBotAI/MediaIngredientMech
    review_id: 20261011T024631Z-mim-reconcile-all-batch-03
    finding_id: f-e1004757f90e8c13
- finding_id: scope-f-838d67873b6673db
  issue_key: mim-reconciliation-exported-context-tokens-9122c364d42e8559
  category: nomenclature
  severity: major
  status: deferred
  certainty: provisional
  title: 'Adjudicate source scope of exported tokens: DL vitamins'
  description: Token presence remains reproducible, but the earlier pattern-based
    observation did not establish whether the exact source label denotes this subject
    or a different preparation. Fresh source-context adjudication is required before
    a confirmed defect or label removal. This successor corrects certainty only; it
    does not establish that the token is valid or that another identity allegation
    is fixed. The historical report actually passes the record and explicitly accepts
    the raw source surface; attributing an unresolved token concern to that report
    was incorrect. No new source evidence was supplied to overturn its scoped conclusion.
  target_ids:
  - record-9122c364d42e8559
  evidence_ids:
  - ev-823412d1eacb6795
  - ev-e6798c510d069e5f
  - ev-f0c42034b2f08a1d
  - ev-82824a1888d907ee
  - ev-0bef314ac38155d7
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/DL_Vitamins.yaml
    role: maintained ingredient
  field_paths:
  - synonyms
  - SSSOM.other
  tags:
  - reconciliation
  - bundle-by-owner
  - exported-context-tokens
  external_issues:
  - https://github.com/CultureBotAI/MediaIngredientMech/issues/718
  - https://github.com/CultureBotAI/MediaIngredientMech/issues/861
  disposition_reason: Token presence remains reproducible, but the earlier pattern-based
    observation did not establish whether the exact source label denotes this subject
    or a different preparation. Fresh source-context adjudication is required before
    a confirmed defect or label removal. This successor corrects certainty only; it
    does not establish that the token is valid or that another identity allegation
    is fixed. The historical report actually passes the record and explicitly accepts
    the raw source surface; attributing an unresolved token concern to that report
    was incorrect. No new source evidence was supplied to overturn its scoped conclusion.
  previous_occurrences:
  - repository: CultureBotAI/MediaIngredientMech
    review_id: 20261011T024633Z-mim-reconcile-all-batch-05
    finding_id: f-838d67873b6673db
- finding_id: scope-f-320ccfb6bddc74ee
  issue_key: mim-reconciliation-exported-context-tokens-797da68010f27377
  category: nomenclature
  severity: major
  status: deferred
  certainty: provisional
  title: 'Adjudicate source scope of exported tokens: Desulfovibrio trace elements'
  description: Token presence remains reproducible, but the earlier pattern-based
    observation did not establish whether the exact source label denotes this subject
    or a different preparation. Fresh source-context adjudication is required before
    a confirmed defect or label removal. This successor corrects certainty only; it
    does not establish that the token is valid or that another identity allegation
    is fixed.
  target_ids:
  - record-797da68010f27377
  evidence_ids:
  - ev-823412d1eacb6795
  - ev-9477d91976d0a888
  - ev-4d30788725c98994
  - ev-a255c9d3059064fe
  - ev-e7674a969ec8d8cb
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Desulfovibrio_Trace_Elements.yaml
    role: maintained ingredient
  field_paths:
  - synonyms
  - SSSOM.other
  tags:
  - reconciliation
  - bundle-by-owner
  - exported-context-tokens
  external_issues:
  - https://github.com/CultureBotAI/MediaIngredientMech/issues/718
  - https://github.com/CultureBotAI/MediaIngredientMech/issues/861
  disposition_reason: Token presence remains reproducible, but the earlier pattern-based
    observation did not establish whether the exact source label denotes this subject
    or a different preparation. Fresh source-context adjudication is required before
    a confirmed defect or label removal. This successor corrects certainty only; it
    does not establish that the token is valid or that another identity allegation
    is fixed.
  previous_occurrences:
  - repository: CultureBotAI/MediaIngredientMech
    review_id: 20261011T024633Z-mim-reconcile-all-batch-05
    finding_id: f-320ccfb6bddc74ee
- finding_id: scope-f-853c7e2e707eedfc
  issue_key: mim-reconciliation-exported-context-tokens-099e2c8a2a9f8f68
  category: nomenclature
  severity: major
  status: deferred
  certainty: provisional
  title: 'Adjudicate source scope of exported tokens: Fatty acid mixture (see Medium
    No. 266)'
  description: Token presence remains reproducible, but the earlier pattern-based
    observation did not establish whether the exact source label denotes this subject
    or a different preparation. Fresh source-context adjudication is required before
    a confirmed defect or label removal. This successor corrects certainty only; it
    does not establish that the token is valid or that another identity allegation
    is fixed.
  target_ids:
  - record-099e2c8a2a9f8f68
  evidence_ids:
  - ev-823412d1eacb6795
  - ev-997c904ed0a9e395
  - ev-66223de2980eb719
  - ev-6b0f037f5dc84aa9
  - ev-abc54f67fc204f62
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Fatty_Acid_Mixture_See_Medium_No_266.yaml
    role: maintained ingredient
  field_paths:
  - synonyms
  - SSSOM.other
  tags:
  - reconciliation
  - bundle-by-owner
  - exported-context-tokens
  external_issues:
  - https://github.com/CultureBotAI/MediaIngredientMech/issues/718
  - https://github.com/CultureBotAI/MediaIngredientMech/issues/861
  disposition_reason: Token presence remains reproducible, but the earlier pattern-based
    observation did not establish whether the exact source label denotes this subject
    or a different preparation. Fresh source-context adjudication is required before
    a confirmed defect or label removal. This successor corrects certainty only; it
    does not establish that the token is valid or that another identity allegation
    is fixed.
  previous_occurrences:
  - repository: CultureBotAI/MediaIngredientMech
    review_id: 20261011T024634Z-mim-reconcile-all-batch-06
    finding_id: f-853c7e2e707eedfc
- finding_id: scope-f-43e56706181e97b8
  issue_key: mim-reconciliation-exported-context-tokens-7059116102e92505
  category: nomenclature
  severity: major
  status: deferred
  certainty: provisional
  title: 'Adjudicate source scope of exported tokens: Mineral solution see Medium
    No. 976'
  description: Token presence remains reproducible, but the earlier pattern-based
    observation did not establish whether the exact source label denotes this subject
    or a different preparation. Fresh source-context adjudication is required before
    a confirmed defect or label removal. This successor corrects certainty only; it
    does not establish that the token is valid or that another identity allegation
    is fixed. A damaged spelling is observable, but the mapping contract permits damaged
    raw source forms when they still resolve to the same substance; malformed punctuation
    alone does not settle identity scope.
  target_ids:
  - record-7059116102e92505
  evidence_ids:
  - ev-823412d1eacb6795
  - ev-b91360770608ed24
  - ev-423b314156ab28a8
  - ev-f25801a7e385fb14
  - ev-5458c3c3defc38d0
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Mineral_Solution_See_Medium_No_976.yaml
    role: maintained ingredient
  field_paths:
  - synonyms
  - SSSOM.other
  tags:
  - reconciliation
  - bundle-by-owner
  - exported-context-tokens
  external_issues:
  - https://github.com/CultureBotAI/MediaIngredientMech/issues/718
  - https://github.com/CultureBotAI/MediaIngredientMech/issues/861
  disposition_reason: Token presence remains reproducible, but the earlier pattern-based
    observation did not establish whether the exact source label denotes this subject
    or a different preparation. Fresh source-context adjudication is required before
    a confirmed defect or label removal. This successor corrects certainty only; it
    does not establish that the token is valid or that another identity allegation
    is fixed. A damaged spelling is observable, but the mapping contract permits damaged
    raw source forms when they still resolve to the same substance; malformed punctuation
    alone does not settle identity scope.
  previous_occurrences:
  - repository: CultureBotAI/MediaIngredientMech
    review_id: 20261011T024636Z-mim-reconcile-all-batch-08
    finding_id: f-43e56706181e97b8
- finding_id: scope-f-d3696f2daf45c433
  issue_key: mim-reconciliation-exported-context-tokens-4253636d94bcf2f1
  category: nomenclature
  severity: major
  status: deferred
  certainty: provisional
  title: 'Adjudicate source scope of exported tokens: Modified trace vitamins'
  description: Token presence remains reproducible, but the earlier pattern-based
    observation did not establish whether the exact source label denotes this subject
    or a different preparation. Fresh source-context adjudication is required before
    a confirmed defect or label removal. This successor corrects certainty only; it
    does not establish that the token is valid or that another identity allegation
    is fixed.
  target_ids:
  - record-4253636d94bcf2f1
  evidence_ids:
  - ev-823412d1eacb6795
  - ev-a1a7bf32cb2806bb
  - ev-5830b871d91efa8c
  - ev-7c6192e7f288bdf0
  - ev-1659306e55f45a0b
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Modified_Trace_Vitamins.yaml
    role: maintained ingredient
  field_paths:
  - synonyms
  - SSSOM.other
  tags:
  - reconciliation
  - bundle-by-owner
  - exported-context-tokens
  external_issues:
  - https://github.com/CultureBotAI/MediaIngredientMech/issues/718
  - https://github.com/CultureBotAI/MediaIngredientMech/issues/861
  disposition_reason: Token presence remains reproducible, but the earlier pattern-based
    observation did not establish whether the exact source label denotes this subject
    or a different preparation. Fresh source-context adjudication is required before
    a confirmed defect or label removal. This successor corrects certainty only; it
    does not establish that the token is valid or that another identity allegation
    is fixed.
  previous_occurrences:
  - repository: CultureBotAI/MediaIngredientMech
    review_id: 20261011T024636Z-mim-reconcile-all-batch-08
    finding_id: f-d3696f2daf45c433
- finding_id: scope-f-5982691d4b3d176b
  issue_key: mim-reconciliation-exported-context-tokens-62f485f9f7517526
  category: nomenclature
  severity: major
  status: deferred
  certainty: provisional
  title: 'Adjudicate source scope of exported tokens: Peptone'
  description: Token presence remains reproducible, but the earlier pattern-based
    observation did not establish whether the exact source label denotes this subject
    or a different preparation. Fresh source-context adjudication is required before
    a confirmed defect or label removal. This successor corrects certainty only; it
    does not establish that the token is valid or that another identity allegation
    is fixed. A damaged spelling is observable, but the mapping contract permits damaged
    raw source forms when they still resolve to the same substance; malformed punctuation
    alone does not settle identity scope.
  target_ids:
  - record-62f485f9f7517526
  evidence_ids:
  - ev-823412d1eacb6795
  - ev-54e6930eaaa55145
  - ev-0bdc1c0fd578d2ef
  - ev-a926e5411d840793
  - ev-f56ebea344bcd264
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Peptone.yaml
    role: maintained ingredient
  field_paths:
  - synonyms
  - SSSOM.other
  tags:
  - reconciliation
  - bundle-by-owner
  - exported-context-tokens
  external_issues:
  - https://github.com/CultureBotAI/MediaIngredientMech/issues/718
  - https://github.com/CultureBotAI/MediaIngredientMech/issues/861
  disposition_reason: Token presence remains reproducible, but the earlier pattern-based
    observation did not establish whether the exact source label denotes this subject
    or a different preparation. Fresh source-context adjudication is required before
    a confirmed defect or label removal. This successor corrects certainty only; it
    does not establish that the token is valid or that another identity allegation
    is fixed. A damaged spelling is observable, but the mapping contract permits damaged
    raw source forms when they still resolve to the same substance; malformed punctuation
    alone does not settle identity scope.
  previous_occurrences:
  - repository: CultureBotAI/MediaIngredientMech
    review_id: 20261011T024637Z-mim-reconcile-all-batch-09
    finding_id: f-5982691d4b3d176b
- finding_id: scope-f-f582ea830b4f370d
  issue_key: mim-reconciliation-exported-context-tokens-4190c0ee5976447a
  category: nomenclature
  severity: major
  status: deferred
  certainty: provisional
  title: 'Adjudicate source scope of exported tokens: Potassium phosphate buffer'
  description: Token presence remains reproducible, but the earlier pattern-based
    observation did not establish whether the exact source label denotes this subject
    or a different preparation. Fresh source-context adjudication is required before
    a confirmed defect or label removal. This successor corrects certainty only; it
    does not establish that the token is valid or that another identity allegation
    is fixed.
  target_ids:
  - record-4190c0ee5976447a
  evidence_ids:
  - ev-823412d1eacb6795
  - ev-8bb59eaf8b6e66f4
  - ev-745bc0e8e18adc16
  - ev-7d01fe3478491965
  - ev-a692d3e165ce1613
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Potassium_Phosphate_Buffer.yaml
    role: maintained ingredient
  field_paths:
  - synonyms
  - SSSOM.other
  tags:
  - reconciliation
  - bundle-by-owner
  - exported-context-tokens
  external_issues:
  - https://github.com/CultureBotAI/MediaIngredientMech/issues/718
  - https://github.com/CultureBotAI/MediaIngredientMech/issues/861
  disposition_reason: Token presence remains reproducible, but the earlier pattern-based
    observation did not establish whether the exact source label denotes this subject
    or a different preparation. Fresh source-context adjudication is required before
    a confirmed defect or label removal. This successor corrects certainty only; it
    does not establish that the token is valid or that another identity allegation
    is fixed.
  previous_occurrences:
  - repository: CultureBotAI/MediaIngredientMech
    review_id: 20261011T024638Z-mim-reconcile-all-batch-10
    finding_id: f-f582ea830b4f370d
- finding_id: scope-f-b7808e84d7886285
  issue_key: mim-reconciliation-exported-context-tokens-59776f859c41300d
  category: nomenclature
  severity: major
  status: deferred
  certainty: provisional
  title: 'Adjudicate source scope of exported tokens: Riboflavin'
  description: Token presence remains reproducible, but the earlier pattern-based
    observation did not establish whether the exact source label denotes this subject
    or a different preparation. Fresh source-context adjudication is required before
    a confirmed defect or label removal. This successor corrects certainty only; it
    does not establish that the token is valid or that another identity allegation
    is fixed.
  target_ids:
  - record-59776f859c41300d
  evidence_ids:
  - ev-823412d1eacb6795
  - ev-032b61a7a21ed47b
  - ev-d59510b4ad4c4456
  - ev-1dfdb8319038a4fb
  - ev-a809b48a4c5a84c5
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Riboflavin.yaml
    role: maintained ingredient
  field_paths:
  - synonyms
  - SSSOM.other
  tags:
  - reconciliation
  - bundle-by-owner
  - exported-context-tokens
  external_issues:
  - https://github.com/CultureBotAI/MediaIngredientMech/issues/718
  - https://github.com/CultureBotAI/MediaIngredientMech/issues/861
  disposition_reason: Token presence remains reproducible, but the earlier pattern-based
    observation did not establish whether the exact source label denotes this subject
    or a different preparation. Fresh source-context adjudication is required before
    a confirmed defect or label removal. This successor corrects certainty only; it
    does not establish that the token is valid or that another identity allegation
    is fixed.
  previous_occurrences:
  - repository: CultureBotAI/MediaIngredientMech
    review_id: 20261011T024638Z-mim-reconcile-all-batch-10
    finding_id: f-b7808e84d7886285
- finding_id: scope-f-2680803ffb7b7f40
  issue_key: mim-reconciliation-exported-context-tokens-c6cdd023283a1f0a
  category: nomenclature
  severity: major
  status: deferred
  certainty: provisional
  title: 'Adjudicate source scope of exported tokens: Sludge fluid'
  description: Token presence remains reproducible, but the earlier pattern-based
    observation did not establish whether the exact source label denotes this subject
    or a different preparation. Fresh source-context adjudication is required before
    a confirmed defect or label removal. This successor corrects certainty only; it
    does not establish that the token is valid or that another identity allegation
    is fixed.
  target_ids:
  - record-c6cdd023283a1f0a
  evidence_ids:
  - ev-823412d1eacb6795
  - ev-6c06e714e86355c6
  - ev-b62c98e3d0a1e1d5
  - ev-d4f1e238a85e0e57
  - ev-de40a4caf98a1085
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Sludge_fluid.yaml
    role: maintained ingredient
  field_paths:
  - synonyms
  - SSSOM.other
  tags:
  - reconciliation
  - bundle-by-owner
  - exported-context-tokens
  external_issues:
  - https://github.com/CultureBotAI/MediaIngredientMech/issues/718
  - https://github.com/CultureBotAI/MediaIngredientMech/issues/861
  disposition_reason: Token presence remains reproducible, but the earlier pattern-based
    observation did not establish whether the exact source label denotes this subject
    or a different preparation. Fresh source-context adjudication is required before
    a confirmed defect or label removal. This successor corrects certainty only; it
    does not establish that the token is valid or that another identity allegation
    is fixed.
  previous_occurrences:
  - repository: CultureBotAI/MediaIngredientMech
    review_id: 20261011T024638Z-mim-reconcile-all-batch-11
    finding_id: f-2680803ffb7b7f40
- finding_id: scope-f-ef4889c5708c1269
  issue_key: mim-reconciliation-exported-context-tokens-3245d67aff586e82
  category: nomenclature
  severity: major
  status: deferred
  certainty: provisional
  title: 'Adjudicate source scope of exported tokens: Soil extract'
  description: Token presence remains reproducible, but the earlier pattern-based
    observation did not establish whether the exact source label denotes this subject
    or a different preparation. Fresh source-context adjudication is required before
    a confirmed defect or label removal. This successor corrects certainty only; it
    does not establish that the token is valid or that another identity allegation
    is fixed.
  target_ids:
  - record-3245d67aff586e82
  evidence_ids:
  - ev-823412d1eacb6795
  - ev-4f670ddc934d5e74
  - ev-927f64381fa816f2
  - ev-1edf0a1870e81e81
  - ev-cefe2423553074dc
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Soil_Extract.yaml
    role: maintained ingredient
  field_paths:
  - synonyms
  - SSSOM.other
  tags:
  - reconciliation
  - bundle-by-owner
  - exported-context-tokens
  external_issues:
  - https://github.com/CultureBotAI/MediaIngredientMech/issues/718
  - https://github.com/CultureBotAI/MediaIngredientMech/issues/861
  disposition_reason: Token presence remains reproducible, but the earlier pattern-based
    observation did not establish whether the exact source label denotes this subject
    or a different preparation. Fresh source-context adjudication is required before
    a confirmed defect or label removal. This successor corrects certainty only; it
    does not establish that the token is valid or that another identity allegation
    is fixed.
  previous_occurrences:
  - repository: CultureBotAI/MediaIngredientMech
    review_id: 20261011T024638Z-mim-reconcile-all-batch-11
    finding_id: f-ef4889c5708c1269
- finding_id: scope-f-3b7b7b7cd4c70ace
  issue_key: mim-reconciliation-exported-context-tokens-341efa75278b5e50
  category: nomenclature
  severity: major
  status: deferred
  certainty: provisional
  title: 'Adjudicate source scope of exported tokens: Trace element solution see Medium
    No. 187'
  description: Token presence remains reproducible, but the earlier pattern-based
    observation did not establish whether the exact source label denotes this subject
    or a different preparation. Fresh source-context adjudication is required before
    a confirmed defect or label removal. This successor corrects certainty only; it
    does not establish that the token is valid or that another identity allegation
    is fixed. A damaged spelling is observable, but the mapping contract permits damaged
    raw source forms when they still resolve to the same substance; malformed punctuation
    alone does not settle identity scope.
  target_ids:
  - record-341efa75278b5e50
  evidence_ids:
  - ev-823412d1eacb6795
  - ev-61509143d0ecf84a
  - ev-cb42f25983a0ad30
  - ev-775e49cc5333c85a
  - ev-a18de57ffdc5d750
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Trace_Element_Solution_See_Medium_No_187.yaml
    role: maintained ingredient
  field_paths:
  - synonyms
  - SSSOM.other
  tags:
  - reconciliation
  - bundle-by-owner
  - exported-context-tokens
  external_issues:
  - https://github.com/CultureBotAI/MediaIngredientMech/issues/718
  - https://github.com/CultureBotAI/MediaIngredientMech/issues/861
  disposition_reason: Token presence remains reproducible, but the earlier pattern-based
    observation did not establish whether the exact source label denotes this subject
    or a different preparation. Fresh source-context adjudication is required before
    a confirmed defect or label removal. This successor corrects certainty only; it
    does not establish that the token is valid or that another identity allegation
    is fixed. A damaged spelling is observable, but the mapping contract permits damaged
    raw source forms when they still resolve to the same substance; malformed punctuation
    alone does not settle identity scope.
  previous_occurrences:
  - repository: CultureBotAI/MediaIngredientMech
    review_id: 20261011T024638Z-mim-reconcile-all-batch-11
    finding_id: f-3b7b7b7cd4c70ace
- finding_id: scope-f-612aa67bad26d26a
  issue_key: mim-reconciliation-exported-context-tokens-78ea6a14a080dbf0
  category: nomenclature
  severity: major
  status: deferred
  certainty: provisional
  title: 'Adjudicate source scope of exported tokens: Trace metal mix A5'
  description: Token presence remains reproducible, but the earlier pattern-based
    observation did not establish whether the exact source label denotes this subject
    or a different preparation. Fresh source-context adjudication is required before
    a confirmed defect or label removal. This successor corrects certainty only; it
    does not establish that the token is valid or that another identity allegation
    is fixed.
  target_ids:
  - record-78ea6a14a080dbf0
  evidence_ids:
  - ev-823412d1eacb6795
  - ev-666a0e05df6eee3c
  - ev-995ddb5e1dd7c309
  - ev-3e284f13241fa94e
  - ev-a6e7432b5d0fbcfb
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Trace_Metal_Mix_A5.yaml
    role: maintained ingredient
  field_paths:
  - synonyms
  - SSSOM.other
  tags:
  - reconciliation
  - bundle-by-owner
  - exported-context-tokens
  external_issues:
  - https://github.com/CultureBotAI/MediaIngredientMech/issues/718
  - https://github.com/CultureBotAI/MediaIngredientMech/issues/861
  disposition_reason: Token presence remains reproducible, but the earlier pattern-based
    observation did not establish whether the exact source label denotes this subject
    or a different preparation. Fresh source-context adjudication is required before
    a confirmed defect or label removal. This successor corrects certainty only; it
    does not establish that the token is valid or that another identity allegation
    is fixed.
  previous_occurrences:
  - repository: CultureBotAI/MediaIngredientMech
    review_id: 20261011T024638Z-mim-reconcile-all-batch-11
    finding_id: f-612aa67bad26d26a
- finding_id: scope-f-54e5335934e0ba03
  issue_key: mim-reconciliation-exported-context-tokens-4b03942a3427132e
  category: nomenclature
  severity: major
  status: deferred
  certainty: provisional
  title: 'Adjudicate source scope of exported tokens: Trace mineral solution'
  description: Token presence remains reproducible, but the earlier pattern-based
    observation did not establish whether the exact source label denotes this subject
    or a different preparation. Fresh source-context adjudication is required before
    a confirmed defect or label removal. This successor corrects certainty only; it
    does not establish that the token is valid or that another identity allegation
    is fixed.
  target_ids:
  - record-4b03942a3427132e
  evidence_ids:
  - ev-823412d1eacb6795
  - ev-28bce6da08c8c14e
  - ev-41b7b72cded4e05c
  - ev-3f611fd20092d7d4
  - ev-ff886fb7448948d4
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Trace_Mineral_Solution.yaml
    role: maintained ingredient
  field_paths:
  - synonyms
  - SSSOM.other
  tags:
  - reconciliation
  - bundle-by-owner
  - exported-context-tokens
  external_issues:
  - https://github.com/CultureBotAI/MediaIngredientMech/issues/718
  - https://github.com/CultureBotAI/MediaIngredientMech/issues/861
  disposition_reason: Token presence remains reproducible, but the earlier pattern-based
    observation did not establish whether the exact source label denotes this subject
    or a different preparation. Fresh source-context adjudication is required before
    a confirmed defect or label removal. This successor corrects certainty only; it
    does not establish that the token is valid or that another identity allegation
    is fixed.
  previous_occurrences:
  - repository: CultureBotAI/MediaIngredientMech
    review_id: 20261011T024639Z-mim-reconcile-all-batch-12
    finding_id: f-54e5335934e0ba03
- finding_id: scope-f-0fa9eaef6cc34337
  issue_key: mim-reconciliation-exported-context-tokens-7c55027f9d88edd0
  category: nomenclature
  severity: major
  status: deferred
  certainty: provisional
  title: 'Adjudicate source scope of exported tokens: Trace minerals'
  description: Token presence remains reproducible, but the earlier pattern-based
    observation did not establish whether the exact source label denotes this subject
    or a different preparation. Fresh source-context adjudication is required before
    a confirmed defect or label removal. This successor corrects certainty only; it
    does not establish that the token is valid or that another identity allegation
    is fixed.
  target_ids:
  - record-7c55027f9d88edd0
  evidence_ids:
  - ev-823412d1eacb6795
  - ev-e098338a3394e86d
  - ev-2c39d54a6bcf5e1b
  - ev-ec1703c8dacbdf80
  - ev-649d543ff1a236ba
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Trace_Minerals.yaml
    role: maintained ingredient
  field_paths:
  - synonyms
  - SSSOM.other
  tags:
  - reconciliation
  - bundle-by-owner
  - exported-context-tokens
  external_issues:
  - https://github.com/CultureBotAI/MediaIngredientMech/issues/718
  - https://github.com/CultureBotAI/MediaIngredientMech/issues/861
  disposition_reason: Token presence remains reproducible, but the earlier pattern-based
    observation did not establish whether the exact source label denotes this subject
    or a different preparation. Fresh source-context adjudication is required before
    a confirmed defect or label removal. This successor corrects certainty only; it
    does not establish that the token is valid or that another identity allegation
    is fixed.
  previous_occurrences:
  - repository: CultureBotAI/MediaIngredientMech
    review_id: 20261011T024639Z-mim-reconcile-all-batch-12
    finding_id: f-0fa9eaef6cc34337
- finding_id: scope-f-397b1df68e373137
  issue_key: mim-reconciliation-exported-context-tokens-4efe2f6907f0d4fc
  category: nomenclature
  severity: major
  status: deferred
  certainty: provisional
  title: 'Adjudicate source scope of exported tokens: Yeast extract'
  description: Token presence remains reproducible, but the earlier pattern-based
    observation did not establish whether the exact source label denotes this subject
    or a different preparation. Fresh source-context adjudication is required before
    a confirmed defect or label removal. This successor corrects certainty only; it
    does not establish that the token is valid or that another identity allegation
    is fixed. A damaged spelling is observable, but the mapping contract permits damaged
    raw source forms when they still resolve to the same substance; malformed punctuation
    alone does not settle identity scope.
  target_ids:
  - record-4efe2f6907f0d4fc
  evidence_ids:
  - ev-823412d1eacb6795
  - ev-0701e78e991c4118
  - ev-5175fd560468ba85
  - ev-c84617d1a202e069
  - ev-ef345ac5a6dc1108
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Yeast_Extract.yaml
    role: maintained ingredient
  field_paths:
  - synonyms
  - SSSOM.other
  tags:
  - reconciliation
  - bundle-by-owner
  - exported-context-tokens
  external_issues:
  - https://github.com/CultureBotAI/MediaIngredientMech/issues/718
  - https://github.com/CultureBotAI/MediaIngredientMech/issues/861
  disposition_reason: Token presence remains reproducible, but the earlier pattern-based
    observation did not establish whether the exact source label denotes this subject
    or a different preparation. Fresh source-context adjudication is required before
    a confirmed defect or label removal. This successor corrects certainty only; it
    does not establish that the token is valid or that another identity allegation
    is fixed. A damaged spelling is observable, but the mapping contract permits damaged
    raw source forms when they still resolve to the same substance; malformed punctuation
    alone does not settle identity scope.
  previous_occurrences:
  - repository: CultureBotAI/MediaIngredientMech
    review_id: 20261011T024639Z-mim-reconcile-all-batch-12
    finding_id: f-397b1df68e373137
actions:
- action_id: scope-f-be91e29ea6694d28
  description: Inspect the exact originating source label and preparation before deciding
    synonym scope.
  finding_ids:
  - scope-f-be91e29ea6694d28
  target_ids:
  - record-88ed3645c26c14b6
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/4-vinylphenol.yaml
    role: maintained ingredient
  acceptance_checks:
  - Read the exact recipe or source row and document whether the label denotes this
    subject, a different preparation, or an instruction fragment.
  - Preserve valid RAW_TEXT and catalog names; reject a resolving label only with
    claim-level scope evidence.
  - Save a successor with this exact issue key and occurrence; address independent
    identity allegations separately.
- action_id: scope-f-e1004757f90e8c13
  description: Inspect the exact originating source label and preparation before deciding
    synonym scope.
  finding_ids:
  - scope-f-e1004757f90e8c13
  target_ids:
  - record-205c79d137874075
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Artificial_seawater.yaml
    role: maintained ingredient
  acceptance_checks:
  - Read the exact recipe or source row and document whether the label denotes this
    subject, a different preparation, or an instruction fragment.
  - Preserve valid RAW_TEXT and catalog names; reject a resolving label only with
    claim-level scope evidence.
  - Save a successor with this exact issue key and occurrence; address independent
    identity allegations separately.
- action_id: scope-f-838d67873b6673db
  description: Inspect the exact originating source label and preparation before deciding
    synonym scope.
  finding_ids:
  - scope-f-838d67873b6673db
  target_ids:
  - record-9122c364d42e8559
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/DL_Vitamins.yaml
    role: maintained ingredient
  acceptance_checks:
  - Read the exact recipe or source row and document whether the label denotes this
    subject, a different preparation, or an instruction fragment.
  - Preserve valid RAW_TEXT and catalog names; reject a resolving label only with
    claim-level scope evidence.
  - Save a successor with this exact issue key and occurrence; address independent
    identity allegations separately.
- action_id: scope-f-320ccfb6bddc74ee
  description: Inspect the exact originating source label and preparation before deciding
    synonym scope.
  finding_ids:
  - scope-f-320ccfb6bddc74ee
  target_ids:
  - record-797da68010f27377
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Desulfovibrio_Trace_Elements.yaml
    role: maintained ingredient
  acceptance_checks:
  - Read the exact recipe or source row and document whether the label denotes this
    subject, a different preparation, or an instruction fragment.
  - Preserve valid RAW_TEXT and catalog names; reject a resolving label only with
    claim-level scope evidence.
  - Save a successor with this exact issue key and occurrence; address independent
    identity allegations separately.
- action_id: scope-f-853c7e2e707eedfc
  description: Inspect the exact originating source label and preparation before deciding
    synonym scope.
  finding_ids:
  - scope-f-853c7e2e707eedfc
  target_ids:
  - record-099e2c8a2a9f8f68
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Fatty_Acid_Mixture_See_Medium_No_266.yaml
    role: maintained ingredient
  acceptance_checks:
  - Read the exact recipe or source row and document whether the label denotes this
    subject, a different preparation, or an instruction fragment.
  - Preserve valid RAW_TEXT and catalog names; reject a resolving label only with
    claim-level scope evidence.
  - Save a successor with this exact issue key and occurrence; address independent
    identity allegations separately.
- action_id: scope-f-43e56706181e97b8
  description: Inspect the exact originating source label and preparation before deciding
    synonym scope.
  finding_ids:
  - scope-f-43e56706181e97b8
  target_ids:
  - record-7059116102e92505
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Mineral_Solution_See_Medium_No_976.yaml
    role: maintained ingredient
  acceptance_checks:
  - Read the exact recipe or source row and document whether the label denotes this
    subject, a different preparation, or an instruction fragment.
  - Preserve valid RAW_TEXT and catalog names; reject a resolving label only with
    claim-level scope evidence.
  - Save a successor with this exact issue key and occurrence; address independent
    identity allegations separately.
- action_id: scope-f-d3696f2daf45c433
  description: Inspect the exact originating source label and preparation before deciding
    synonym scope.
  finding_ids:
  - scope-f-d3696f2daf45c433
  target_ids:
  - record-4253636d94bcf2f1
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Modified_Trace_Vitamins.yaml
    role: maintained ingredient
  acceptance_checks:
  - Read the exact recipe or source row and document whether the label denotes this
    subject, a different preparation, or an instruction fragment.
  - Preserve valid RAW_TEXT and catalog names; reject a resolving label only with
    claim-level scope evidence.
  - Save a successor with this exact issue key and occurrence; address independent
    identity allegations separately.
- action_id: scope-f-5982691d4b3d176b
  description: Inspect the exact originating source label and preparation before deciding
    synonym scope.
  finding_ids:
  - scope-f-5982691d4b3d176b
  target_ids:
  - record-62f485f9f7517526
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Peptone.yaml
    role: maintained ingredient
  acceptance_checks:
  - Read the exact recipe or source row and document whether the label denotes this
    subject, a different preparation, or an instruction fragment.
  - Preserve valid RAW_TEXT and catalog names; reject a resolving label only with
    claim-level scope evidence.
  - Save a successor with this exact issue key and occurrence; address independent
    identity allegations separately.
- action_id: scope-f-f582ea830b4f370d
  description: Inspect the exact originating source label and preparation before deciding
    synonym scope.
  finding_ids:
  - scope-f-f582ea830b4f370d
  target_ids:
  - record-4190c0ee5976447a
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Potassium_Phosphate_Buffer.yaml
    role: maintained ingredient
  acceptance_checks:
  - Read the exact recipe or source row and document whether the label denotes this
    subject, a different preparation, or an instruction fragment.
  - Preserve valid RAW_TEXT and catalog names; reject a resolving label only with
    claim-level scope evidence.
  - Save a successor with this exact issue key and occurrence; address independent
    identity allegations separately.
- action_id: scope-f-b7808e84d7886285
  description: Inspect the exact originating source label and preparation before deciding
    synonym scope.
  finding_ids:
  - scope-f-b7808e84d7886285
  target_ids:
  - record-59776f859c41300d
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Riboflavin.yaml
    role: maintained ingredient
  acceptance_checks:
  - Read the exact recipe or source row and document whether the label denotes this
    subject, a different preparation, or an instruction fragment.
  - Preserve valid RAW_TEXT and catalog names; reject a resolving label only with
    claim-level scope evidence.
  - Save a successor with this exact issue key and occurrence; address independent
    identity allegations separately.
- action_id: scope-f-2680803ffb7b7f40
  description: Inspect the exact originating source label and preparation before deciding
    synonym scope.
  finding_ids:
  - scope-f-2680803ffb7b7f40
  target_ids:
  - record-c6cdd023283a1f0a
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Sludge_fluid.yaml
    role: maintained ingredient
  acceptance_checks:
  - Read the exact recipe or source row and document whether the label denotes this
    subject, a different preparation, or an instruction fragment.
  - Preserve valid RAW_TEXT and catalog names; reject a resolving label only with
    claim-level scope evidence.
  - Save a successor with this exact issue key and occurrence; address independent
    identity allegations separately.
- action_id: scope-f-ef4889c5708c1269
  description: Inspect the exact originating source label and preparation before deciding
    synonym scope.
  finding_ids:
  - scope-f-ef4889c5708c1269
  target_ids:
  - record-3245d67aff586e82
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Soil_Extract.yaml
    role: maintained ingredient
  acceptance_checks:
  - Read the exact recipe or source row and document whether the label denotes this
    subject, a different preparation, or an instruction fragment.
  - Preserve valid RAW_TEXT and catalog names; reject a resolving label only with
    claim-level scope evidence.
  - Save a successor with this exact issue key and occurrence; address independent
    identity allegations separately.
- action_id: scope-f-3b7b7b7cd4c70ace
  description: Inspect the exact originating source label and preparation before deciding
    synonym scope.
  finding_ids:
  - scope-f-3b7b7b7cd4c70ace
  target_ids:
  - record-341efa75278b5e50
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Trace_Element_Solution_See_Medium_No_187.yaml
    role: maintained ingredient
  acceptance_checks:
  - Read the exact recipe or source row and document whether the label denotes this
    subject, a different preparation, or an instruction fragment.
  - Preserve valid RAW_TEXT and catalog names; reject a resolving label only with
    claim-level scope evidence.
  - Save a successor with this exact issue key and occurrence; address independent
    identity allegations separately.
- action_id: scope-f-612aa67bad26d26a
  description: Inspect the exact originating source label and preparation before deciding
    synonym scope.
  finding_ids:
  - scope-f-612aa67bad26d26a
  target_ids:
  - record-78ea6a14a080dbf0
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Trace_Metal_Mix_A5.yaml
    role: maintained ingredient
  acceptance_checks:
  - Read the exact recipe or source row and document whether the label denotes this
    subject, a different preparation, or an instruction fragment.
  - Preserve valid RAW_TEXT and catalog names; reject a resolving label only with
    claim-level scope evidence.
  - Save a successor with this exact issue key and occurrence; address independent
    identity allegations separately.
- action_id: scope-f-54e5335934e0ba03
  description: Inspect the exact originating source label and preparation before deciding
    synonym scope.
  finding_ids:
  - scope-f-54e5335934e0ba03
  target_ids:
  - record-4b03942a3427132e
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Trace_Mineral_Solution.yaml
    role: maintained ingredient
  acceptance_checks:
  - Read the exact recipe or source row and document whether the label denotes this
    subject, a different preparation, or an instruction fragment.
  - Preserve valid RAW_TEXT and catalog names; reject a resolving label only with
    claim-level scope evidence.
  - Save a successor with this exact issue key and occurrence; address independent
    identity allegations separately.
- action_id: scope-f-0fa9eaef6cc34337
  description: Inspect the exact originating source label and preparation before deciding
    synonym scope.
  finding_ids:
  - scope-f-0fa9eaef6cc34337
  target_ids:
  - record-7c55027f9d88edd0
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Trace_Minerals.yaml
    role: maintained ingredient
  acceptance_checks:
  - Read the exact recipe or source row and document whether the label denotes this
    subject, a different preparation, or an instruction fragment.
  - Preserve valid RAW_TEXT and catalog names; reject a resolving label only with
    claim-level scope evidence.
  - Save a successor with this exact issue key and occurrence; address independent
    identity allegations separately.
- action_id: scope-f-397b1df68e373137
  description: Inspect the exact originating source label and preparation before deciding
    synonym scope.
  finding_ids:
  - scope-f-397b1df68e373137
  target_ids:
  - record-4efe2f6907f0d4fc
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Yeast_Extract.yaml
    role: maintained ingredient
  acceptance_checks:
  - Read the exact recipe or source row and document whether the label denotes this
    subject, a different preparation, or an instruction fragment.
  - Preserve valid RAW_TEXT and catalog names; reject a resolving label only with
    claim-level scope evidence.
  - Save a successor with this exact issue key and occurrence; address independent
    identity allegations separately.
limitations:
- Only certainty of the selected observations is corrected. Other historical identity,
  role, component, source-count and provenance allegations remain in their original
  scope.
- Artificial_seawater and DL_Vitamins historical reports explicitly accept their raw
  labels; the initial extraction invented a historical concern for those targets.
- The exact current exported labels are known, but whether each denotes the same substance
  requires source-level interpretation. No ingredient bytes or native release dispositions
  changed.
- Full scientific review and ontology B4 are not claimed by this partial reconciliation.
tags:
- reconciliation
- certainty-correction
- partial-scientific-coverage
notes:
- 'Addresses review-process issue #861 in PR #860. It does not resolve the scientific
  curation backlog #718.'
```
