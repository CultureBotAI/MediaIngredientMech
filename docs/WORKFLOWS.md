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

## Data Import

### Import from CultureMech

```bash
just import-data
```

This runs `scripts/import_from_culturemech.py`, which:

1. Reads mapped ingredients from `CultureMech/output/mapped_ingredients.yaml` (995 records)
2. Reads unmapped ingredients from `CultureMech/output/unmapped_ingredients.yaml` (136 records)
3. Converts each ingredient into an IngredientRecord with:
   - Mapped ingredients: `mapping_status: MAPPED`, populated `ontology_mapping`
   - Unmapped ingredients: `mapping_status: UNMAPPED`, no `ontology_mapping`
4. Aggregates synonyms from raw text variants
5. Populates occurrence statistics from media recipe counts
6. Creates initial CurationEvent with `action: IMPORTED`
7. Writes output to `data/curated/ingredients.yaml`

### Expected Output Structure

After import, `data/curated/ingredients.yaml` contains an IngredientCollection:

```yaml
generation_date: "2026-03-06T10:00:00"
total_count: 1131
mapped_count: 995
unmapped_count: 136
ingredients:
  - identifier: CHEBI:26710
    preferred_term: sodium chloride
    mapping_status: MAPPED
    ontology_mapping:
      ontology_id: CHEBI:26710
      ontology_label: sodium chloride
      ontology_source: CHEBI
      mapping_quality: EXACT_MATCH
    synonyms:
      - synonym_text: NaCl
        synonym_type: ABBREVIATION
        source: CultureMech
    occurrence_statistics:
      total_occurrences: 2341
      media_count: 2341
    curation_history:
      - timestamp: "2026-03-06T10:00:00"
        curator: system
        action: IMPORTED
        changes: "Imported from CultureMech mapped_ingredients.yaml"
        new_status: MAPPED
  # ... more records
```

### Re-importing

Running `just import-data` again overwrites existing data. Always create a snapshot first:

```bash
just snapshot
just import-data
```

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

Expected output:
```
Validating data/curated/ingredients.yaml...
Checked 1131 records.
Errors: 0
Warnings: 2
  - WARN: CHEBI:99999 not found in CHEBI (record: CHEBI:99999)
  - WARN: Missing occurrence_statistics for 3 records
```

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
- Create a snapshot before re-importing data
- Commit curated data to git regularly
- Git provides the primary version history; snapshots provide quick rollback within a session

## CultureMech Integration

### Data Flow

```
CultureMech                    MediaIngredientMech
-----------                    -------------------
output/mapped_ingredients.yaml   --import-->  data/curated/ingredients.yaml
output/unmapped_ingredients.yaml --import-->       (curate and validate)
                                              data/curated/ingredients.yaml
input/ingredient_mappings.yaml <--export--        (validated mappings)
```

### Import from CultureMech

```bash
just import-data
```

Reads from the CultureMech output directory and creates IngredientRecords. See the Data Import section above for details.

### Round-Trip Export to CultureMech

After curating and validating ingredients, export the mappings back to CultureMech format:

```bash
python scripts/export_to_culturemech.py
```

This produces a file compatible with CultureMech's expected input format, containing:
- All MAPPED ingredients with their ontology IDs and labels
- Updated synonym lists
- Mapping quality metadata

### Keeping Data in Sync

When CultureMech data is updated (new media recipes added, new ingredients discovered):

1. Create a snapshot of current curated data
2. Re-run import: `just import-data`
3. The import script preserves existing curation history for known ingredients
4. New ingredients appear as UNMAPPED
5. Validate and curate the new entries
6. Export updated mappings back to CultureMech

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
      ingredients.yaml
```

If CultureMech is in a different location, set the `CULTUREMECH_DIR` environment variable before importing.

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
