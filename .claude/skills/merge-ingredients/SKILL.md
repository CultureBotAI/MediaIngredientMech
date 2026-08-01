---
name: merge-ingredients
description: Use this skill to deduplicate and merge MediaIngredientMech ingredient records — when two or more records describe the same ingredient (duplicate CHEBI mappings, name variants, or a placeholder plus its resolved record) and must be consolidated into one, preserving synonyms, occurrence statistics, and curation_history. Covers detection strategies, the merge procedure, and post-merge validation.
---

# Merge Ingredients Skill

## Overview

MediaIngredientMech maintains a non-redundant collection of ingredient records.
Deduplication ensures no duplicate CHEBI IDs, consolidated solutions/buffers, alignment
with CultureMech's 995-ingredient baseline, and full preservation of synonyms, occurrence
statistics, and curation history.

**Key principles:**
- **Primary rule:** same CHEBI ID → MUST merge.
- **Secondary:** high-confidence name similarity for solutions/buffers/stocks (manual review).
- **Audit trail:** every merge recorded in `curation_history`.
- **Quality preservation:** the highest-quality mapping becomes the merge target.

---

## Deduplication Strategies

1. **CHEBI ID-based (primary).** Records sharing a CHEBI ID are the same chemical entity
   and MUST be merged — separate records split occurrence counts and media associations.
   Both names are preserved as synonyms.
2. **Name-based (secondary).** Name similarity ≥ 0.9 for solution/buffer/stock types,
   which vary by suffix ("solution" vs "stock") and concentration. **Flagged for review**,
   not auto-merged.
3. **KG-Microbe reconciliation (exploratory).** Search the CultureMech baseline for
   already-mapped ingredients, alternative names, and import candidates.

Full detection algorithms, target-selection criteria, the merge procedure, confidence
scoring, and concentration normalization are in
[`reference/matching-strategies.md`](reference/matching-strategies.md).

---

## Merge Decision Summary

The full decision-flow diagram and worked conflict-resolution scenarios are in
[`reference/decision-and-conflicts.md`](reference/decision-and-conflicts.md).

**Auto-merge**

| Condition | Reason |
|-----------|--------|
| Same CHEBI + same quality | Identical mapping, safe to consolidate |
| Same CHEBI + target higher quality | Higher-quality target is authoritative |
| Exact normalized name (1.0) + same source | Perfect string match, no ambiguity |

**Flag for review**

| Condition | Reason |
|-----------|--------|
| Same CHEBI + conflicting evidence | Different sources suggest uncertainty |
| Same CHEBI + one is `NEEDS_EXPERT` | Expert review required |
| Name similarity 0.7–0.9 | High but not perfect confidence |
| Different ontology sources | May represent different concepts |

**Never merge**

| Condition | Reason |
|-----------|--------|
| Different CHEBI IDs | Different chemical entities |
| Name similarity < 0.7 | Insufficient confidence |
| One record is `REJECTED` | Already merged / invalid |

---

## Running the Deduplication

```bash
python scripts/deduplicate_ingredients.py --dry-run               # ALWAYS preview first
python scripts/deduplicate_ingredients.py --chebi-only            # primary rule only
python scripts/deduplicate_ingredients.py --include-name-matches  # + name matching
python scripts/deduplicate_ingredients.py --search-kg-microbe     # + KG-Microbe search
python scripts/deduplicate_ingredients.py                         # execute merges
```

Thresholds (`--auto-merge-threshold`, `--name-match-threshold`), custom data paths, and a
full walkthrough of the three-phase output (CHEBI → name → KG-Microbe) and post-merge
validation are in [`reference/script-and-workflow.md`](reference/script-and-workflow.md).

---

## Best Practices

1. **Always start with `--dry-run`** — review the output, then execute.
2. **CHEBI first, names second.** CHEBI duplicates are non-negotiable; name matches need
   domain judgment; KG-Microbe search is exploratory.
3. **Validate after every merge** — run `scripts/validate_mappings.py` and re-check
   `total_count`/`mapped_count`/`unmapped_count`.
4. **Document flagged records** in `data/curation/flagged_duplicates.yaml` (chebi_id,
   record indices, reason, reviewer, resolution).
5. **Preserve original terms** — add every variant name as a `synonym` tagged with
   `synonym_type`, `source: merge`, and `occurrence_count`.
6. **Periodic KG-Microbe sync** — monthly: KGX export → compare with CultureMech baseline
   → import missing high-frequency ingredients.

Commands and the full flagged-record / synonym examples are in
[`reference/script-and-workflow.md`](reference/script-and-workflow.md).

---

## Reference Files

| File | Contents |
|------|----------|
| [`reference/matching-strategies.md`](reference/matching-strategies.md) | CHEBI merge detection/target-selection/procedure/auto-merge conditions, name-based matching (solution detection, confidence scoring, concentration normalization), and KG-Microbe reconciliation |
| [`reference/decision-and-conflicts.md`](reference/decision-and-conflicts.md) | The full decision-flow diagram and four worked conflict-resolution scenarios (quality, evidence, name mismatch, `NEEDS_EXPERT`) |
| [`reference/script-and-workflow.md`](reference/script-and-workflow.md) | `deduplicate_ingredients.py` options, three-phase output interpretation, curation-workflow integration (interactive/batch/periodic), pre/post-merge + audit-trail validation, and the full best-practices command/example blocks (flagged-record log, synonym tagging, periodic KG-Microbe sync) |
| [`reference/examples-and-troubleshooting.md`](reference/examples-and-troubleshooting.md) | Four end-to-end examples and five troubleshooting issues (self-merge, post-merge validation, name false positives, KG-Microbe path, memory) |
| [`reference/api-reference.md`](reference/api-reference.md) | `CHEBIDeduplicator`, `SolutionMatcher`, `KGMicrobeSearcher` APIs, plus advanced usage (custom merge logic, batch processing, CI/CD hook, automated reconciliation) |
