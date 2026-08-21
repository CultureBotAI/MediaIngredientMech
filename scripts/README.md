# Script support policy

The `scripts/` directory contains both current command implementations and the
historical programs that produced earlier curation migrations. A file being
present here does not by itself mean it is safe to run against current data.

## Supported command surface

The `justfile` is the public command index. Prefer `just <recipe>` over invoking
a Python file directly: recipes pin arguments, select the correct data surface,
and compose required synchronization or validation steps. The maintained
surface currently includes these groups:

| Purpose | Stable recipes / implementations |
|---|---|
| Schema and data validation | `validate-all`, `validate-strict`, `validate-products`, `validate-individual` |
| Data consistency | `qc`, `qc-roundtrip`, `qc-sssom`, `qc-duplicate-ids`, `qc-flat-coverage` |
| Collection synchronization | `sync-curated`, `sync-individual`, `export-individual` |
| Curation | `curate`, `report`, `snapshot` |
| Published products | `build-docs`, `export-browser`, `export-lists`, `export-indexes`, `generate-visualizations` |
| Research | `research-ingredient*`, `research-provider*`, `apply-role-research-results` |
| Identifier maintenance | `curie-aliases`, `curie-check`, `curie-validate`, `curie-verify-micro` |

Scripts reached by those recipes are maintained even when their filename looks
like a generic `check_` or `generate_` utility. CI workflow entry points are
also maintained.

## Historical migration and repair scripts

Names beginning with `fix_`, `migrate_`, `repair_`, `reground_`, `regrade_`,
`demote_`, `retire_`, or a narrowly named `merge_` usually encode a completed
data migration. Treat them as reproducibility artifacts:

- do not run them merely because their name resembles the current task;
- read the linked issue/history and inspect hard-coded identifiers first;
- require a dry-run or a new focused test before reuse;
- prefer a maintained generic command when one exists.

The same caution applies to dated/batch-specific `add_`, `apply_`, `map_`, and
`update_` scripts. Moving these files en masse would break historical links and
tests, so physical archival should happen only from a reviewed manifest in a
separate change. This policy makes their status explicit without disguising a
large rename as cleanup.

## Inventory snapshot

At the 2026-08-20 review, Git tracked 152 Python scripts. A name-based first
pass grouped 25 as audit/validation, 11 as product generation, 5 as research,
37 as clear historical migration/repair candidates, and 74 requiring individual
classification. The authoritative maintained subset is the recipe/CI surface
above; the remaining 74 are the next human inventory queue.

When promoting a script to maintained status:

1. put reusable behavior in `src/mediaingredientmech/`;
2. add focused tests;
3. add a `just` recipe or package entry point;
4. route YAML writes through validated writers and record curation history;
5. update agent instruction references.

## Backup policy

Committed `*.bak`, `*.backup*`, `*.pre-merge-*`, and `*.pre-dedup-*` copies are
not supported data surfaces. Use Git history for committed states and
`just snapshot` for temporary local recovery. The canonical collections remain
`data/curated/mapped_ingredients.yaml` and
`data/curated/unmapped_ingredients.yaml`.
