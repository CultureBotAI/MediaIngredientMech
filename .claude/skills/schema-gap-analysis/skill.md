---
name: schema-gap-analysis
description: Find gaps between MIM's LinkML schema, its YAML instances, and the code that generates them. Uses linkml-validate as ground truth and reports along three axes (schema / instances / process). Copy-paste runnable.
category: quality
requires_database: false
requires_internet: false
version: 2.1.0
---

# Schema gap analysis (MIM)

The conceptual framework — why three axes (schema / instances / process), what each error class signals, common anti-patterns — lives once at the cross-Mech version in claw:
https://github.com/CultureBotAI/culturebotai-claw/blob/main/.claude/skills/schema-gap-analysis/skill.md

This file is the MIM-specific operational version: every command below is ready to run as-is, with MIM paths baked in.

## Setup

LinkML lives in `.venv/`. Two known bumps:

```bash
# (1) pip missing in .venv — bootstrap if needed
.venv/bin/python -m ensurepip

# (2) linkml-validate aborts with `AttributeError: Format has no attribute 'JSON'`
# — pin linkml-runtime to a 1.9.x release (linkml 1.9.x imports Format.JSON
# at module load and runtime 1.10 dropped it).
.venv/bin/python -m pip install "linkml-runtime>=1.9,<1.10"
.venv/bin/linkml-validate --help  # smoke test
```

## Procedure

### 1. Validate canonical collection files

```bash
.venv/bin/linkml-validate \
  -s src/mediaingredientmech/schema/mediaingredientmech.yaml \
  -C IngredientCollection \
  data/curated/mapped_ingredients.yaml \
  data/curated/unmapped_ingredients.yaml
```

### 2. Validate one individual per-record YAML

```bash
SAMPLE=$(ls data/ingredients/mapped/*.yaml | head -1)
.venv/bin/linkml-validate \
  -s src/mediaingredientmech/schema/mediaingredientmech.yaml \
  -C IngredientRecord "$SAMPLE"
```

### 3. Validate the per-record corpus

```bash
find data/ingredients -name "*.yaml" -print0 \
  | xargs -0 .venv/bin/linkml-validate \
      -s src/mediaingredientmech/schema/mediaingredientmech.yaml \
      -C IngredientRecord 2>&1 | tee /tmp/mim_validate.out > /dev/null
grep -c "^\[ERROR\]" /tmp/mim_validate.out  # target: 0
```

### 4. Histogram the errors

Run against both collections **and** per-record output combined — a gap that lives only in `unmapped_ingredients.yaml` is silently dropped if only mapped is histogrammed.

```bash
SCHEMA=src/mediaingredientmech/schema/mediaingredientmech.yaml
COLS="data/curated/mapped_ingredients.yaml data/curated/unmapped_ingredients.yaml"

.venv/bin/linkml-validate -s $SCHEMA -C IngredientCollection $COLS 2>&1 \
  | grep -oE "Additional properties are not allowed \('[^']+'" \
  | sort | uniq -c | sort -rn

.venv/bin/linkml-validate -s $SCHEMA -C IngredientCollection $COLS 2>&1 \
  | grep -oE "'[^']+' is a required property" \
  | sort | uniq -c | sort -rn

.venv/bin/linkml-validate -s $SCHEMA -C IngredientCollection $COLS 2>&1 \
  | grep -oE "does not match '[^']+'" \
  | sort | uniq -c | sort -rn

.venv/bin/linkml-validate -s $SCHEMA -C IngredientCollection $COLS 2>&1 \
  | grep -oE "is not a '[^']+'" \
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
.venv/bin/linkml-validate \
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

- Custom (tolerant) validator the skill is calibrated against: `src/mediaingredientmech/validation/schema_validator.py`
- Schema: `src/mediaingredientmech/schema/mediaingredientmech.yaml`
- Curator (use for instance-axis fixes): `src/mediaingredientmech/curation/ingredient_curator.py`
- Last full audit notes: `notes/schema_gap_analysis_2026-05-16.md`
- Cross-Mech framework + new-Mech bootstrap template: [claw/.claude/skills/schema-gap-analysis](https://github.com/CultureBotAI/culturebotai-claw/blob/main/.claude/skills/schema-gap-analysis/skill.md)
