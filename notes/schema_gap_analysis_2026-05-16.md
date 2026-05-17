# Schema / instance / process gap analysis

**Date**: 2026-05-16
**Tool**: `linkml-validate` (linkml 1.9.3, linkml-runtime pinned to 1.9.x)
**Schema**: `src/mediaingredientmech/schema/mediaingredientmech.yaml`
**Data**: 1870 mapped + 398 unmapped + 2268 individual records (`data/curated/` + `data/ingredients/`)

This is a snapshot of the divergences `linkml-validate` finds when run against
the current schema and curated data. The methodology lives in
`.claude/skills/schema-gap-analysis/SKILL.md`; this file records what it
turned up this session so we don't rediscover the same gaps next time.

## Findings ranked by blast radius

| # | Error | Axis | Records affected | Fix sketch |
|---|---|---|---:|---|
| 1 | `'ontology_id' is a required property` and `Additional properties are not allowed ('identifier')` | Schema | 4536 (2268 of each) | Rename the schema slot: data uses `identifier`; schema slot is `ontology_id`. (Note: LinkML `aliases:` is descriptive metadata only — it does NOT make `linkml-validate` accept an alternate YAML key. Slot rename is the actual fix.) |
| 2 | `does not match '^[A-Z]+:[0-9]+$'` on `ontology_mapping.ontology_id` | Schema | 316 | The custom validator was broadened to `^[A-Za-z][A-Za-z0-9.]*:[A-Za-z0-9][A-Za-z0-9._~-]*$` (note the `~` — kg-microbe locals like `disodium_phosphate_heptahydrate_~28002_m_stock~29` use it). Apply the same broadening to the schema `pattern:` on `OntologyMapping.ontology_id`. |
| 3 | `is not a 'date-time'` (naive timestamps without offset) | Process | 1541 | `accept_mapping()`, `ingredient_reviewer.py`, several `scripts/*` use `datetime.now()` instead of `datetime.now(timezone.utc)`. Fix the generators; one-shot rewrite of affected records is optional. |
| 4 | `Additional properties are not allowed ('pubchem_cid')` on `chemical_properties` | Schema | 185 | Add `pubchem_cid` to `ChemicalProperties` as `range: integer` + `minimum_value: 1` — PubChem CIDs are positive ints in the data; a string + pattern would fail every value because LinkML patterns apply only to strings. |
| 5 | `does not match '^CHEBI:[0-9]+$'` on `kg_microbe_node_id` | Schema | 31 | Pattern too narrow; current data has non-CHEBI prefixes here too. Broaden similarly to (2). |
| 6 | `Additional properties are not allowed ('cas_rn')` on `ontology_mapping.evidence[]` | Schema | 44 | Add `cas_rn` to `MappingEvidence` (range: string, pattern `^\d+-\d+-\d+$`) — already defined on `ChemicalProperties`. |

Total error count: 6653 across 2275 files (every issue above is systematic — none are isolated record bugs). Item 1 contributes two errors per record (missing required slot + unexpected key) which is why its row total is 4536, and the grand total is the sum of all six rows.

## Process-axis hot spots

`grep -rn 'datetime.now()' src/ scripts/ --include='*.py' | grep -v timezone`
turns up these generators writing naive timestamps:

- `src/mediaingredientmech/validation/ingredient_reviewer.py` (3 sites)
- `src/mediaingredientmech/export/report_generator.py`
- `scripts/download_ontologies.py`
- `scripts/batch_curate.py` (2 sites)
- `scripts/batch_curate_unmapped.py` (2 sites)
- and ~10 more under `scripts/`

The collection-level `generation_date` written by `scripts/aggregate_records.py`
is already timezone-aware; only record-level / event-level timestamps are
affected.

## Suggested remediation order (historical — superseded by Resolution below)

> **Note (2026-05-16):** an earlier version of step 2 below recommended
> `aliases: [identifier]` on the slot rather than a rename. That is wrong:
> LinkML aliases are descriptive metadata and do not change which YAML
> keys validate. The Resolution section that follows used a slot rename
> instead. The original text is left in place for traceability.

1. **Schema first (no migration risk)**: items 2, 4, 5, 6 — broaden patterns
   and add missing slots. After this, the only remaining errors are #1 and #3.
2. **Identifier slot alias (item 1)**: ~~add `aliases: [identifier]` to the
   `IngredientRecord.ontology_id` slot rather than renaming~~ — superseded.
   The actual fix is to rename the schema slot from `ontology_id` to
   `identifier` (and update every reader / writer in the codebase). See
   PR #19.
3. **Generator fixes (item 3)**: switch `datetime.now()` → `datetime.now(timezone.utc)`
   in every site grep finds. Optional follow-up: a one-shot pass over
   `data/curated/` + `data/ingredients/` to retrofit the existing naive
   timestamps with `+00:00` so historical records also validate.

## Not addressed yet

- The `OntologyMapping.ontology_label` field is required by the schema but
  several records have `ontology_label: null` in the source YAML. Run a
  separate `grep "ontology_label: null"` pass before fixing #1, because
  those will become visible once the slot-name issue stops dominating the
  error output.

## Resolution (2026-05-16, same day)

Every numbered class above was remediated immediately, one PR per gap:

| # | PR  | Class                                            | Errors |
|---|-----|--------------------------------------------------|-------:|
|   | —   | *baseline*                                       |  6653  |
| 4,6 | #17 | Add `pubchem_cid` + `cas_rn` slots             |  6424  |
| 2,5 | #18 | Broaden CURIE patterns (`OntologyMapping.ontology_id` + `kg_microbe_node_id`) | 6077 |
| 1   | #19 | Rename `IngredientRecord.ontology_id` → `identifier` + 17 broken readers | 1541 |
| 3a  | #20 | Generators emit timezone-aware timestamps (code) |  1541  |
| 3b  | #21 | Retrofit 3082 existing naive timestamps (data)   | **0**  |

`linkml-validate` against both curated collections is now clean. The
`ontology_label: null` follow-up flagged in "Not addressed yet" above did
not surface in the post-#19 histogram — either the count is zero or those
errors fall under a different class than this analysis split out. Worth
re-running the `/schema-gap-analysis` skill periodically (e.g. before
SSSOM republishes) to catch new drift.
