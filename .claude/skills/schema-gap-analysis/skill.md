---
name: schema-gap-analysis
description: Find gaps and inconsistencies between the LinkML schema, the YAML instance records, and the code that generates them — using linkml-validate as ground truth and reporting along three axes (schema, instances, process).
category: quality
requires_database: false
requires_internet: false
version: 1.0.0
---

# Schema gap analysis

## When to use

Run this skill when:

- You suspect the schema and the live data have drifted apart (e.g. the custom
  `scripts/validate_all.py` reports clean while curation tooling is happily
  writing keys the schema doesn't declare).
- A new field is being added in code and you want to know whether the schema
  needs updating, the data needs migrating, or both.
- A new contributor asks "is this YAML valid?" and the answer needs to be more
  rigorous than "the project's custom validator says yes."

The custom validator in `src/mediaingredientmech/validation/schema_validator.py`
was deliberately built to be tolerant (open enums, broadened CURIE pattern,
accepts both `identifier` and `ontology_id` as the primary key). That's good
for CI ergonomics, but it hides real schema-vs-data divergence. This skill
uses **`linkml-validate`** — the upstream tool — as a stricter ground truth.

## Setup

LinkML is normally installed in `.venv/`, but two things bite:

**1. `pip` is sometimes missing from the venv.** Bootstrap it if needed:

```bash
.venv/bin/python -m ensurepip
```

**2. Version mismatch between `linkml` and `linkml-runtime` is the most
common breakage.** As of 2026-05-16 the venv ships `linkml 1.9.3` and
`linkml-runtime 1.10.0`; runtime 1.10 dropped `Format.JSON` which 1.9.x
imports at module load, so `linkml-validate` aborts on import with
`AttributeError: type object 'Format' has no attribute 'JSON'`. Pin the
runtime back to 1.9.x:

```bash
.venv/bin/python -m pip install "linkml-runtime>=1.9,<1.10"
.venv/bin/linkml-validate --help  # smoke test
```

(Upgrading `linkml` to a release that ships with 1.10-runtime is the
permanent fix; until then, pinning the runtime is the simplest path.
Setup is one-time: once the pin is in `.venv/`, every subsequent
invocation of the skill works without reinstalling.)

## The three-axis perspective

Every error `linkml-validate` reports fits one of these classes. Always ask
"which axis owns the fix?" before patching anything.

### Axis 1 — schema

The schema (`src/mediaingredientmech/schema/mediaingredientmech.yaml`) is
wrong: a slot is missing, a pattern is too strict, or a name has drifted
from what tooling has standardized on. Fix is to edit the schema; data and
generators stay the same.

Signs:

- Hundreds-to-thousands of records fail the same way (the data is
  consistent, the schema is not).
- The field name in the error is one you can see in the actual data files
  and recognize as canonical.
- The pattern in the error is older than recent design discussions
  (e.g. `^[A-Z]+:[0-9]+$` predating multi-prefix CURIE support).

### Axis 2 — instance records

The data is wrong: a record has a typo, an unexpected key from a one-off
script, or a malformed value. Fix is to migrate the affected records.

Signs:

- A small number of records fail; most don't.
- The field name is suspicious (typo, abandoned experimental key).
- The value is malformed in a way that suggests human entry, not tooling
  (e.g. a single bad timestamp among thousands of well-formed ones).

### Axis 3 — process

The generator code is wrong: it emits structurally valid YAML that
nonetheless violates the schema. Fix is to update the script(s) so future
runs produce conformant output, then optionally rewrite affected data.

Signs:

- Errors cluster by source tool (every record imported by
  `import_from_culturemech.py`, every event written by `accept_mapping`).
- A field that is otherwise correct is consistently in the wrong shape
  (naive vs. aware timestamps; lowercase vs. SCREAMING_SNAKE_CASE labels).
- `git blame` on the offending line in the generator points at a single
  commit that introduced the divergence.

## Procedure

1. **Make linkml-validate runnable** (see Setup).
2. **Validate the canonical collection files.** These are the simplest
   single-shot validation targets and surface the bulk of issues:

   ```bash
   .venv/bin/linkml-validate \
     -s src/mediaingredientmech/schema/mediaingredientmech.yaml \
     -C IngredientCollection \
     data/curated/mapped_ingredients.yaml \
     data/curated/unmapped_ingredients.yaml
   ```

3. **Validate one individual record** to confirm the same issues affect
   on-disk per-ingredient files (different file shape, same schema class):

   ```bash
   SAMPLE=$(ls data/ingredients/mapped/*.yaml | head -1)
   .venv/bin/linkml-validate \
     -s src/mediaingredientmech/schema/mediaingredientmech.yaml \
     -C IngredientRecord "$SAMPLE"
   ```

4. **Histogram the errors** so you see the distinct issue classes, not the
   thousands of per-record repetitions. Run against **both** canonical
   collections — a gap that lives only in `unmapped_ingredients.yaml` is
   silently dropped if only `mapped_ingredients.yaml` is histogrammed:

   ```bash
   SCHEMA=src/mediaingredientmech/schema/mediaingredientmech.yaml
   COLS="data/curated/mapped_ingredients.yaml data/curated/unmapped_ingredients.yaml"

   .venv/bin/linkml-validate -s $SCHEMA -C IngredientCollection $COLS 2>&1 \
     | grep -oE "Additional properties are not allowed \('[^']+'" \
     | sort | uniq -c | sort -rn

   .venv/bin/linkml-validate -s $SCHEMA -C IngredientCollection $COLS 2>&1 \
     | grep -oE "does not match '[^']+'" \
     | sort | uniq -c | sort -rn

   .venv/bin/linkml-validate -s $SCHEMA -C IngredientCollection $COLS 2>&1 \
     | grep -oE "is not a '[^']+'" \
     | sort | uniq -c | sort -rn

   .venv/bin/linkml-validate -s $SCHEMA -C IngredientCollection $COLS 2>&1 \
     | grep -c "is a required property"
   ```

5. **For each distinct class, decide the axis** using the heuristics
   above. Capture findings; don't change anything yet.

6. **Cross-check the process axis.** The biggest blind spots come from
   generator code that has slowly drifted. Three targeted greps catch the
   most common patterns without producing noise:

   ```bash
   # Naive datetimes (no timezone) — every `datetime.now()` that's
   # NOT for a `.strftime(...)` filename/display call (which doesn't
   # end up in validated YAML). The `\.isoformat\b` filter restricts
   # to writes that produce ISO-8601 strings (the schema's `date-time`
   # format).
   grep -rnE 'datetime\.now\(\)\.isoformat\b' \
     src/ scripts/ --include='*.py' \
     | grep -v "timezone"

   # Saves that drop collection metadata: yaml.dump receives a literal
   # one-key {"ingredients": ...} dict, which throws away
   # generation_date / total_count / mapped_count / unmapped_count.
   # Should be empty in current code.
   grep -rnE 'yaml\.dump\(\s*\{\s*["\047]ingredients["\047]\s*:' \
     src/ scripts/ --include='*.py'

   # Direct WRITES to a canonical curated collection file that skip
   # IngredientCurator. Match `open(..., "w"/"a")` literally so we
   # don't false-positive on scripts that merely *mention* the
   # filename (which the earlier "any mention" version of this grep
   # did — analyze/categorize/prepare-style scripts that read the
   # file or print its name kept showing up).
   grep -rnE 'open\([^)]*(mapped|unmapped)_ingredients\.yaml[^)]*["\047][wa][bt]?["\047]' \
     scripts/ src/ --include='*.py'
   ```

   The earlier version of this step used a single noisy
   `grep yaml.dump | grep -v default_flow_style` that surfaced six
   call sites of which only one had ever been the real bug. The three
   greps above are calibrated against the actual fix history of this
   repo. Even so, the first one (naive `datetime.now()`) can
   occasionally surface a filename/display call site that doesn't go
   to validated YAML (e.g. `report_generator.py` writing
   `"generated_at"` into a top-level JSON report) — read the line
   before classifying it as a process-axis bug.

7. **Decide and apply fixes.** Usually a mix: rename/alias the canonical
   slot on the schema, broaden patterns, add missing slots, fix the
   handful of malformed records, and patch the offending generators
   (timezone, action label, key name) so the next regeneration is clean.

8. **Re-run linkml-validate.** Exit code 0 with no errors is the target.
   Until then, document remaining divergences in a project memory file so
   they don't get rediscovered every session.

## Common gap classes seen in this repo

| Error fragment | Likely class | Typical fix |
|---|---|---|
| `'X' is a required property` for thousands of records | Schema axis: slot is named wrong | Rename the slot in the schema to match what the data carries (note: LinkML `aliases:` is descriptive metadata only — it does NOT make `linkml-validate` accept an alternate YAML key; rename is the actual fix). See PR #19 for an example. |
| `Additional properties are not allowed ('X' was unexpected)` for thousands | Schema axis: slot missing from the schema entirely | Add the slot to the appropriate class |
| `Additional properties are not allowed ('X' was unexpected)` for a handful | Instance axis (typo) or process axis (one tool emits a wrong key) | Migrate records / fix generator |
| `does not match '<regex>'` | Schema axis if the regex hasn't caught up to legitimate values; instance axis if a single record is malformed | Broaden the schema pattern or correct the record |
| `is not a 'date-time'` | Process axis: generator emits naive datetimes | Replace `datetime.now()` with `datetime.now(timezone.utc)` |
| `Invalid value 'X' for enum Y` | Schema axis if Y is an organically growing vocabulary; process axis if a tool emits typos | Enumerate observed values OR convert the slot to `range: string` with a pattern, depending on whether the vocabulary is bounded |

## Anti-patterns

- **Don't patch the custom validator alone.** It's already permissive; the
  whole point of running linkml-validate is to find what the custom
  validator hides.
- **Don't silently rename a slot in the schema without also updating
  `src/mediaingredientmech/`** — `_check_required`, `_validate_*` helpers,
  and tests still reference the old name. `git grep` the slot name before
  renaming.
- **Don't fix instance records with `sed`.** Round-trip through
  `IngredientCurator.load()/save()` so the canonical YAML formatting is
  preserved and the collection-level metadata (`generation_date`,
  `total_count`, etc.) is correctly recomputed.
- **Don't add fields to the schema without aliasing.** If the new field
  partially overlaps with an existing one (e.g. `cas_rn` on both
  `ChemicalProperties` and `MappingEvidence`), make sure both classes
  declare it explicitly or factor a common slot.

## Pointers

- Custom validator (intentionally tolerant): `src/mediaingredientmech/validation/schema_validator.py`.
- Schema: `src/mediaingredientmech/schema/mediaingredientmech.yaml`.
- Generators that affect curated YAML shape: `src/mediaingredientmech/curation/ingredient_curator.py`, `scripts/aggregate_records.py`, every `scripts/enrich_*`, `scripts/apply_*`, `scripts/auto_correct.py`.
- Most recent end-to-end remediation pass: `notes/schema_gap_analysis_2026-05-16.md` (the six gap classes the skill turned up, plus the PR that closed each).
- Primary-key history is described inline in the schema (`IngredientRecord.identifier`'s `description:` block) — the `ontology_id` → `identifier` rename happened in PR #19.
