---
name: schema-gap-analysis
description: Find gaps between MIM's LinkML schema, its YAML instances, and the code that generates them. Uses linkml-validate (or the strict closed-schema harness ported from CultureMech) as ground truth and reports along three axes (schema / instances / process). Copy-paste runnable.
category: quality
requires_database: false
requires_internet: false
version: 2.2.0
---

# Schema gap analysis (MIM)

The conceptual framework — why three axes (schema / instances / process), what each error class signals, common anti-patterns — lives once at the cross-Mech version in claw:
https://github.com/CultureBotAI/culturebotai-claw/blob/main/.claude/skills/schema-gap-analysis/skill.md

This file is the MIM-specific operational version: every command below is ready to run as-is, with MIM paths baked in.

## Fast path (preferred)

The CultureMech audit machinery is ported (see PR opening this section).
Two recipes replace most of the bash boilerplate below:

```bash
just validate-strict   # closed-schema parallel walk of data/ingredients/** + data/curated/**;
                       # writes reports/instance_validation_failures.tsv with one row per ERROR
                       # categorized (unexpected_field / missing_required / enum_mismatch /
                       # format_mismatch / pattern_mismatch / type_mismatch / range_violation /
                       # other / yaml_parse_error / empty_file / validator_crash).
                       # Excludes data/curated/backups/ and data/snapshots/.

just audit-writers     # inventory every YAML-writing script and check for
                       # write_validated_ingredient + record_curation_event
                       # adoption. Writes reports/pipeline_writers_audit.tsv.
```

Both recipes also live in the `qc` composite (`just qc`). Histogram the
strict-validator TSV with:

```bash
awk -F'\t' 'NR>1 {print $3}' reports/instance_validation_failures.tsv | sort | uniq -c | sort -rn
```

For deeper drill-down (e.g. distinct fields in `unexpected_field` rows):

```bash
awk -F'\t' 'NR>1 && $3=="unexpected_field" {print $4}' \
  reports/instance_validation_failures.tsv | sort | uniq -c | sort -rn
```

The legacy `linkml-validate` invocations below remain useful when you
need to validate a single ad-hoc file outside the standard roots or
inspect raw validator messages with full context.

## Setup

MIM's `justfile` (`just validate-schema` / `just validate-all`) calls `linkml-validate` directly from `PATH`, so the commands below use the same bare invocation. If your local install is in `.venv/`, substitute `.venv/bin/linkml-validate` everywhere (or run `uv run linkml-validate ...`).

```bash
linkml-validate --help    # smoke test
```

If this fails with `command not found`, run `uv sync` (or activate the venv) — MIM's `pyproject.toml` pins `linkml-runtime>=1.7.0,<1.10` so a fresh `uv sync` produces a working `linkml-validate` (the `<1.10` cap exists because linkml-runtime 1.10 removed `Format.JSON`, which linkml 1.9.x imports at module load; bump the cap when bumping `linkml` past 1.9.x).

## Procedure

### 1. Validate canonical collection files

```bash
linkml-validate \
  -s src/mediaingredientmech/schema/mediaingredientmech.yaml \
  -C IngredientCollection \
  data/curated/mapped_ingredients.yaml \
  data/curated/unmapped_ingredients.yaml
```

### 2. Validate one individual per-record YAML

```bash
SAMPLE=$(ls data/ingredients/mapped/*.yaml | head -1)
linkml-validate \
  -s src/mediaingredientmech/schema/mediaingredientmech.yaml \
  -C IngredientRecord "$SAMPLE"
```

### 3. Validate the per-record corpus

```bash
find data/ingredients -name "*.yaml" -print0 \
  | xargs -0 linkml-validate \
      -s src/mediaingredientmech/schema/mediaingredientmech.yaml \
      -C IngredientRecord 2>&1 | tee /tmp/mim_validate.out > /dev/null
grep -c "^\[ERROR\]" /tmp/mim_validate.out  # target: 0
```

### 4. Histogram the errors

Histogram both the collection run **and** the per-record run from step 3 (`/tmp/mim_validate.out`). A gap that lives only in `unmapped_ingredients.yaml`, or only in the per-record corpus, is silently dropped if only one of the two is histogrammed.

```bash
SCHEMA=src/mediaingredientmech/schema/mediaingredientmech.yaml
COLS="data/curated/mapped_ingredients.yaml data/curated/unmapped_ingredients.yaml"

# Re-run the collection validation, capturing to /tmp/mim_collections.out
linkml-validate -s $SCHEMA -C IngredientCollection $COLS \
  > /tmp/mim_collections.out 2>&1

# Combine collection + per-record output (per-record already captured in step 3
# at /tmp/mim_validate.out; re-run step 3 first if it's missing/stale).
cat /tmp/mim_collections.out /tmp/mim_validate.out > /tmp/mim_all.out

grep -oE "Additional properties are not allowed \('[^']+'" /tmp/mim_all.out \
  | sort | uniq -c | sort -rn

grep -oE "'[^']+' is a required property" /tmp/mim_all.out \
  | sort | uniq -c | sort -rn

grep -oE "does not match '[^']+'" /tmp/mim_all.out \
  | sort | uniq -c | sort -rn

grep -oE "is not a '[^']+'" /tmp/mim_all.out \
  | sort | uniq -c | sort -rn
```

### 5. Cross-check generator drift (Axis 3)

Three calibrated greps for MIM:

```bash
# Naive datetimes — every `datetime.now()` that produces ISO-8601 output.
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
# don't false-positive on scripts that merely *mention* the filename.
grep -rnE 'open\([^)]*(mapped|unmapped)_ingredients\.yaml[^)]*["\047][wa][bt]?["\047]' \
  scripts/ src/ --include='*.py'
```

### 6. Decide and apply fixes

For each distinct error class, pick the axis and fix accordingly:

- **Schema axis** (hundreds-to-thousands of records fail same way): edit `src/mediaingredientmech/schema/mediaingredientmech.yaml`.
- **Instance axis** (small number, looks like typos): round-trip through `src/mediaingredientmech/curation/ingredient_curator.py` (`load → save`) so canonical YAML formatting + `generation_date`/`total_count` metadata are recomputed correctly. **Don't `sed`-fix.**
- **Process axis** (clustered by source tool, same wrong shape): patch the offender in `src/mediaingredientmech/` or `scripts/aggregate_*.py`, `scripts/enrich_*.py`, `scripts/apply_*.py`, `scripts/auto_correct.py`. Then optionally rewrite affected records.

### 7. Re-validate

```bash
linkml-validate \
  -s src/mediaingredientmech/schema/mediaingredientmech.yaml \
  -C IngredientCollection \
  data/curated/mapped_ingredients.yaml \
  data/curated/unmapped_ingredients.yaml
# target: "No issues found"
```

## MIM-specific gap classes (history)

| Error | Class | Resolution | Reference |
|---|---|---|---|
| `'ontology_id' is a required property` (×thousands) | Schema axis: slot renamed | Renamed `ontology_id` → `identifier`; LinkML `aliases:` is descriptive only, doesn't actually accept alternate YAML keys | PR #19 |
| Six other classes from the first end-to-end pass | mixed | See `notes/schema_gap_analysis_2026-05-16.md` for the per-class breakdown + closing PRs | 2026-05-16 audit |

## Pointers

- Strict closed-schema harness (preferred entrypoint): `scripts/validate_strict.py` (`just validate-strict`)
- Writer audit (process-axis inventory): `scripts/audit_writers.py` (`just audit-writers`)
- Write-time validation gate (use in any new writer script): `src/mediaingredientmech/validation/write_validated.py` (`write_validated_ingredient`)
- Curation-event helper (use to leave an audit trail): `src/mediaingredientmech/curate/curation_event.py` (`record_curation_event`)
- Custom (tolerant) validator the skill is calibrated against: `src/mediaingredientmech/validation/schema_validator.py`
- Schema: `src/mediaingredientmech/schema/mediaingredientmech.yaml`
- Curator (use for instance-axis fixes): `src/mediaingredientmech/curation/ingredient_curator.py`
- Last full audit notes: `notes/schema_gap_analysis_2026-05-16.md`
- Cross-Mech framework + new-Mech bootstrap template: [claw/.claude/skills/schema-gap-analysis](https://github.com/CultureBotAI/culturebotai-claw/blob/main/.claude/skills/schema-gap-analysis/skill.md)
