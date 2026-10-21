---
name: audit-schema-gaps
description: Compatibility entry point for MediaIngredientMech schema-gap requests. Routes to the canonical schema-gap-analysis skill so validation commands and repository assumptions stay in one maintained place.
category: quality
requires_database: false
requires_internet: false
version: 3.0.0
---

# Audit schema gaps

Use [`schema-gap-analysis`](../schema-gap-analysis/SKILL.md) for the complete and
authoritative three-axis schema, instance, and pipeline audit procedure in
MediaIngredientMech. This alias remains so prompts naming `audit-schema-gaps`
resolve cleanly, while keeping validation commands and repository assumptions
in one maintained skill.

Final record or repository assessments follow
[docs/record-reviews.md](../../../docs/record-reviews.md) and
[docs/record-review-profile.md](../../../docs/record-review-profile.md) via the
canonical `schema-gap-analysis` hand-off to `review-yaml-record` or
`review-yaml-category`. Raw validator and writer-audit outputs are diagnostic
inputs, not a completed scientific review.

For a quick closed-schema and writer check:

```bash
just validate-strict
just audit-writers
```

For all maintained repository quality gates:

```bash
just qc
```

Read live command output and the artifacts those commands regenerate. Do not
infer corpus size, writer coverage, or validation status from prose.
