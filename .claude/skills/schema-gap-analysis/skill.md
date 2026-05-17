---
name: schema-gap-analysis
description: Find gaps between MIM's LinkML schema, its YAML instances, and the code that generates them. Canonical version now lives in the claw repo and applies cross-Mech; this MIM-side stub records the MIM-specific config row + history.
category: quality
requires_database: false
requires_internet: false
version: 2.0.0
---

# schema-gap-analysis — MIM

The canonical, cross-Mech version of this skill now lives at:

```
../culturebotai-claw/.claude/skills/schema-gap-analysis/skill.md
```

It generalises the methodology (linkml-validate as ground truth, three-axis classification, error histograms, process-drift greps) so it can run against any Mech repo. Use that version when invoking the skill.

## MIM-specific config (substitute into the cross-Mech procedure)

| Field | Value |
|---|---|
| `SCHEMA` | `src/mediaingredientmech/schema/mediaingredientmech.yaml` |
| Tree-root class | `IngredientCollection` (curated/ files) / `IngredientRecord` (per-file) |
| Canonical collections | `data/curated/mapped_ingredients.yaml`, `data/curated/unmapped_ingredients.yaml` |
| Per-record YAMLs | `data/ingredients/mapped/*.yaml`, `data/ingredients/unmapped/*.yaml` |
| Custom (tolerant) validator | `src/mediaingredientmech/validation/schema_validator.py` |
| Curator/save module | `src/mediaingredientmech/curation/ingredient_curator.py` |

## MIM-specific reference

- **Last end-to-end pass**: `notes/schema_gap_analysis_2026-05-16.md` — six gap classes the skill surfaced on its first MIM run, plus the PR that closed each.
- **Primary-key history**: described inline in the schema (`IngredientRecord.identifier`'s `description:` block). The `ontology_id` → `identifier` rename happened in PR #19.
- **Process-drift sites worth grepping for changes**: `src/mediaingredientmech/curation/ingredient_curator.py`, `scripts/aggregate_records.py`, every `scripts/enrich_*`, `scripts/apply_*`, `scripts/auto_correct.py`.
