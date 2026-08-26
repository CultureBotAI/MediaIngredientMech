# Workflows

Common workflows for MediaIngredientMech, including data import, curation, validation, and CultureMech integration.

## Initial Setup

### Install Dependencies

```bash
just install
```

This installs the package in editable mode with dev dependencies.

### Generate Schema Dataclasses

```bash
just gen-schema
```

Generates Python dataclasses from the LinkML schema into `src/mediaingredientmech/datamodel/`.

### Run quality checks from a linked worktree

The composite gate uses the locked project environment; activating a virtualenv
is not required:

```bash
uv sync --frozen --extra dev
just qc
```

`qc-evidence` uses shared tooling from a local `culturebotai-claw` checkout. It
first looks beside the primary MIM checkout, so the same command works from a
linked Git worktree. For a different layout, point it at the repository root:

```bash
CLAW_ROOT=/path/to/culturebotai-claw just qc-evidence
```

The legacy `CLAW_SRC=/path/to/culturebotai-claw/src` override is also accepted.
An invalid or missing checkout fails with the locations that were checked.
Evidence reports are always written below the active MIM checkout at
`workspace/reports/`, never into the shared tooling checkout.

## CultureMech Intake Status

MIM does not currently have a supported bulk-import workflow. The legacy
`import-data` compatibility recipe and all four CultureMech collection writers
listed in `scripts/README.md` deliberately exit non-zero before reading or
writing files (#453).

The retired implementation projected CultureMech aggregate rows directly over
both curated collections. That projection used obsolete schema fields, dropped
MIM-owned curation and history, derived counts from capped examples, and could
leave a half-updated data surface. A snapshot does not make that operation a
valid synchronization strategy.

Until the stable recipe-reference and occurrence contracts in #447 and #449
land:

1. Treat `data/curated/` and `data/ingredients/` as the authoritative MIM
   curation surfaces.
2. Use CultureMech aggregates only to produce a read-only, partial diagnostic
   report. Their current solution coverage is incomplete (CultureMech #337), so
   absence from an aggregate is not evidence that a source record was removed.
3. Review each proposed addition, target change, or prevalence update.
4. Apply accepted changes through focused curation tooling with history and
   validation.
5. Run `just sync-curated` after per-record edits, then `just qc`.

## Batch Curation Workflow

A typical curation session follows this pattern:

### Step 1: Check Current Status

```bash
just report
```

Review the progress report to see how many ingredients remain unmapped and which categories need attention.

### Step 2: Create a Snapshot

```bash
just snapshot
```

Output:
```
Snapshot created: data/snapshots/20260306_103000
```

### Step 3: Curate Ingredients

```bash
just curate
```

The interactive CLI presents unmapped ingredients sorted by occurrence count. See the [Curation Guide](CURATION_GUIDE.md) for detailed instructions.

### Step 4: Validate Changes

```bash
just validate-all
```

This runs `scripts/validate_all.py`, which checks:
- Schema compliance (all required fields present, correct types)
- Ontology ID format validation (`^[A-Z]+:[0-9]+$`)
- Ontology term existence (via OAK/OLS if configured)
- Status consistency (MAPPED records have ontology_mapping, UNMAPPED do not)

The validator reports separate results for the tracked collection files in
`data/curated/` and the per-record files in `data/ingredients/`, followed by
aggregate error and warning counts. A successful run ends with
`Validation PASSED`.

### Step 5: Generate Report

```bash
just report
```

This runs `scripts/generate_report.py` and shows curation progress statistics.

### Step 6: Commit Changes

If validation passes, commit the curated data:

```bash
git add data/curated/
git commit -m "Curate batch: mapped 15 ingredients"
```

## Validation

### Validate All Data

```bash
just validate-all
```

### Validate Schema Only

```bash
just validate-schema
```

Checks that the LinkML schema itself is syntactically valid.

### What Gets Validated

| Check | Description | Severity |
|-------|-------------|----------|
| Required fields | All required fields are present | Error |
| Type checking | Field values match declared types | Error |
| Enum values | Enum fields contain valid values | Error |
| Ontology ID format | IDs match `^[A-Z]+:[0-9]+$` | Error |
| Status consistency | MAPPED records have ontology_mapping | Error |
| Ontology term existence | Term exists in source ontology | Warning |
| Missing statistics | Records without occurrence_statistics | Warning |
| Orphan synonyms | Synonyms without occurrence counts | Warning |

## Backup and Restore

### Creating Snapshots

```bash
just snapshot
```

Snapshots are stored in `data/snapshots/<timestamp>/` and contain copies of all files in `data/curated/`. The snapshots directory is excluded from git.

### Listing Snapshots

```bash
ls data/snapshots/
```

Output:
```
20260305_090000/
20260306_103000/
20260306_143000/
```

### Restoring from a Snapshot

To restore data from a previous snapshot:

```bash
cp data/snapshots/20260306_103000/*.yaml data/curated/
just validate-all
```

Always validate after restoring to confirm data integrity.

### Backup Strategy

- Create a snapshot before each curation session
- Create a snapshot before applying a reviewed upstream update
- Commit curated data to git regularly
- Git provides the primary version history; snapshots provide quick rollback within a session

## CultureMech Integration

### Data Flow

```
CultureMech                         MediaIngredientMech
-----------                         -------------------
aggregate outputs --compare/report--> tracked curated records
reviewed downstream changes <--------- published MIM artifacts
```

Inbound aggregate synchronization is review-only until a merge-safe replacement
is implemented. The comparison is partial and diagnostic while CultureMech
#337 remains open; it cannot establish removal from the upstream corpus.
CultureMech remains the source of recipe data; MIM remains the source of
ingredient identity curation.

### Outbound CultureMech updates

There is also no supported direct CultureMech exporter in this repository; the
previously documented Python path does not exist. Publish and validate MIM's
normal artifacts, then coordinate any CultureMech change as an explicit,
reviewed downstream update. A future round trip must define conflict handling
and provenance in both directions rather than recreating an untracked file-copy
workflow.

### Keeping Data in Sync

When CultureMech data is updated (new media recipes added, new ingredients discovered):

1. Generate and review a comparison report; do not overwrite curated files.
2. Separate new labels, occurrence changes, and target conflicts.
3. Apply accepted changes with their source evidence and curation history.
4. Synchronize aggregate/per-record projections with `just sync-curated`.
5. Run `just qc` and the ontology-backed validation gates.
6. Publish the reviewed MIM artifacts and coordinate downstream changes.

### Directory Conventions

MediaIngredientMech expects CultureMech data at a sibling path:

```
KG-Microbe/
  CultureMech/
    output/
      mapped_ingredients.yaml
      unmapped_ingredients.yaml
  MediaIngredientMech/
    data/curated/
      mapped_ingredients.yaml
      unmapped_ingredients.yaml
    data/ingredients/
      mapped/
      unmapped/
```

The read-only comparison script uses the sibling checkout by default. Set
`CULTUREMECH_DIR` when comparing against a different checkout.

## Development Workflows

### Running Tests

```bash
just test          # Run all tests
just test-cov      # Run tests with coverage report
```

### Code Quality

```bash
just format        # Format code with black
just lint          # Lint code with ruff
just typecheck     # Type check with mypy
just check         # Run all quality checks (lint + typecheck + test)
```

### Cleaning Up

```bash
just clean         # Remove generated files, caches, and build artifacts
```

## Related Documentation

- [Curation Guide](CURATION_GUIDE.md) - Detailed curation instructions and quality standards
- [Schema Reference](SCHEMA_REFERENCE.md) - Complete data model documentation
