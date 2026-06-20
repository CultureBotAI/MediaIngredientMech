# Supporting Scripts

*Reference for the **review-ingredients** skill — see [`../skill.md`](../skill.md) for the overview, workflows, and rule summary.*

---

## Supporting Scripts

### 1. review_ingredient.py

**Purpose:** Interactive single-ingredient review with Rich UI

**Usage:**
```bash
# Review by preferred term
PYTHONPATH=src python scripts/review_ingredient.py "sodium chloride"

# Review by ontology ID
PYTHONPATH=src python scripts/review_ingredient.py --id CHEBI:26710

# Auto-suggest corrections
PYTHONPATH=src python scripts/review_ingredient.py "glucose" --suggest-fixes

# Apply corrections interactively
PYTHONPATH=src python scripts/review_ingredient.py "calcium chloride" --interactive
```

**Features:**
- Rich panels showing current mapping
- Color-coded validation results (P1=red, P2=yellow, P3=blue, P4=green)
- Interactive correction application
- Side-by-side ontology comparison

**Output Example:**
```
╔════════════════════════════════════════════════════════════╗
║              Ingredient: sodium chloride                    ║
╠════════════════════════════════════════════════════════════╣
║ Status: MAPPED                                              ║
║ Ontology ID: CHEBI:26710                                   ║
║ Quality: EXACT_MATCH (confidence: 0.95)                    ║
║ Match Level: NORMALIZED                                     ║
╚════════════════════════════════════════════════════════════╝

Validation Results: ✓ PASS (1 warning)

 P3 MEDIUM │ Missing Chemical Properties (P3.1)
────────────┼──────────────────────────────────────────────
 Message    │ SMILES, InChI, molecular formula not present
 Suggestion │ Enrich from OLS API (auto-correctable)
 Preview    │ molecular_formula: NaCl
            │ smiles: [Na+].[Cl-]

Apply correction? [y/N]:
```

### 2. batch_review.py

**Purpose:** Batch validate all ingredients, generate comprehensive report

**Usage:**
```bash
# Review all mapped ingredients
PYTHONPATH=src python scripts/batch_review.py \
  --output reports/validation_$(date +%Y%m%d) \
  --format md,json,html

# Filter by priority
PYTHONPATH=src python scripts/batch_review.py --priority P1,P2

# Filter by ontology source
PYTHONPATH=src python scripts/batch_review.py --source CHEBI

# Parallel processing
PYTHONPATH=src python scripts/batch_review.py --threads 8

# Dry-run (no file output)
PYTHONPATH=src python scripts/batch_review.py --limit 10 --dry-run
```

**Options:**
- `--output DIR`: Output directory for reports
- `--format md,json,html`: Which report formats to generate
- `--priority P1,P2,P3,P4`: Filter issues by priority
- `--source CHEBI,FOODON,ENVO`: Filter by ontology source
- `--threads N`: Parallel workers (default: 4)
- `--limit N`: Process only first N ingredients (testing)
- `--dry-run`: Preview without writing files

**Output Files:**
- `validation_report.md`: Human-readable summary
- `validation_data.json`: Machine-readable issues
- `dashboard.html`: Interactive web dashboard
- `corrections_plan.json`: Auto-correctable suggestions

### 3. auto_correct.py

**Purpose:** Auto-fix safe P3/P4 issues without human review

**Usage:**
```bash
# Dry-run to preview changes
PYTHONPATH=src python scripts/auto_correct.py --dry-run

# Apply all safe corrections
PYTHONPATH=src python scripts/auto_correct.py --apply

# Specific correction types
PYTHONPATH=src python scripts/auto_correct.py --apply --types chemical_properties
PYTHONPATH=src python scripts/auto_correct.py --apply --types synonyms

# Limit for testing
PYTHONPATH=src python scripts/auto_correct.py --apply --limit 10

# Specific ontology source
PYTHONPATH=src python scripts/auto_correct.py --apply --source CHEBI
```

**Correction Types:**
- `chemical_properties`: Enrich SMILES, InChI, formulas from OLS
- `synonyms`: Add missing synonyms from ontology
- `curie_format`: Normalize CURIE format (e.g., "CHEBI:123" not "CHEBI 123")
- `whitespace`: Fix extra spaces in labels

**Safety:**
- Only applies P3/P4 corrections
- Never changes ontology IDs
- Never modifies preferred_term (except whitespace)
- Records all changes in curation_history

### 4. apply_corrections.py

**Purpose:** Apply correction plan from JSON file

**Usage:**
```bash
# Apply corrections from batch review
PYTHONPATH=src python scripts/apply_corrections.py \
  corrections_plan.json \
  --validate

# Dry-run
PYTHONPATH=src python scripts/apply_corrections.py \
  corrections_plan.json \
  --dry-run

# Filter by priority
PYTHONPATH=src python scripts/apply_corrections.py \
  corrections_plan.json \
  --priority P3,P4
```

**Input Format (`corrections_plan.json`):**
```json
{
  "corrections": [
    {
      "ingredient_id": "MediaIngredientMech:000123",
      "preferred_term": "glucose",
      "action": "enrich_properties",
      "changes": {
        "chemical_properties": {
          "molecular_formula": "C6H12O6",
          "smiles": "C([C@@H]1[C@H]([C@@H]([C@H](C(O1)O)O)O)O)O"
        }
      },
      "auto_correctable": true,
      "confidence": 1.0
    }
  ]
}
```

**Validation:**
- Checks ingredient exists
- Verifies changes are safe (no ontology ID changes for P3/P4)
- Confirms auto_correctable flag
- Validates data types match schema

### 5. download_ontologies.py

**Purpose:** Download and cache OWL files from OBO Foundry

**Usage:**
```bash
# Check current cache status
python scripts/download_ontologies.py --check-only

# Download specific ontologies
python scripts/download_ontologies.py --sources CHEBI FOODON

# Download all
python scripts/download_ontologies.py --all

# Force re-download
python scripts/download_ontologies.py --force --sources CHEBI

# Verify integrity
python scripts/download_ontologies.py --verify
```

**Features:**
- Downloads from OBO Foundry
- Computes MD5 checksums
- Updates manifest.json with version info
- Validates OWL syntax
- Shows file size and version

**Manifest Format:**
```json
{
  "chebi": {
    "url": "http://purl.obolibrary.org/obo/chebi.owl",
    "downloaded": "2026-03-15T10:30:00Z",
    "version": "v2024-03-01",
    "md5": "abc123def456...",
    "size_mb": 245.3,
    "status": "valid"
  }
}
```

### 6. validate_synonyms.py

**Purpose:** Cross-check ingredient synonyms with ontology synonyms

**Usage:**
```bash
# Check all ingredients
PYTHONPATH=src python scripts/validate_synonyms.py

# Add missing synonyms automatically
PYTHONPATH=src python scripts/validate_synonyms.py --add-missing

# Report only (no changes)
PYTHONPATH=src python scripts/validate_synonyms.py --report-only

# Specific ingredient
PYTHONPATH=src python scripts/validate_synonyms.py --ingredient "glucose"
```

**Output:**
```
Synonym Validation Report
=========================

Ingredient: glucose (CHEBI:17234)
---------------------------------
Ontology synonyms (10):
  - D-glucose ✓ (in record)
  - dextrose ✓ (in record)
  - Glc
  - grape sugar
  - blood sugar
  - glucose
  - D-gluco-hexose
  ...

Missing from record (5):
  + Glc [EXACT]
  + grape sugar [RELATED]
  + blood sugar [RELATED]
  + D-gluco-hexose [RELATED]

Add missing synonyms? [y/N]:
```

### 7. enrich_from_ols.py

**Purpose:** Batch enrich all CHEBI-mapped ingredients from OLS

**Usage:**
```bash
# Enrich all CHEBI terms
PYTHONPATH=src python scripts/enrich_from_ols.py

# Batch size and rate limiting
PYTHONPATH=src python scripts/enrich_from_ols.py \
  --batch-size 50 \
  --delay 0.5

# Resume from checkpoint
PYTHONPATH=src python scripts/enrich_from_ols.py --resume

# Dry-run
PYTHONPATH=src python scripts/enrich_from_ols.py --dry-run --limit 10
```

**Features:**
- Rate-limited API calls (avoid 429 errors)
- Checkpoint/resume for large batches
- Progress bar with ETA
- Caches successful enrichments
- Records failures for retry

**Output:**
```
Enriching CHEBI-mapped ingredients from OLS...
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 500/995 50% ETA: 00:08:30

✓ CHEBI:26710 (sodium chloride) - enriched
✓ CHEBI:17234 (glucose) - enriched
✗ CHEBI:12345 - OLS API error (retrying...)
...

Summary:
  Total: 995
  Enriched: 987 (99.2%)
  Failed: 8 (0.8%)

Failed ingredients saved to: enrichment_failures.json
```
