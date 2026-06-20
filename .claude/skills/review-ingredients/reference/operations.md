# Operations: Error Handling · Troubleshooting · Examples · Workflow Integration · Metrics · Roadmap

*Reference for the **review-ingredients** skill — see [`../skill.md`](../skill.md) for the overview, workflows, and rule summary.*

---

## Error Handling

### Retry Logic for API Calls

```python
import time
import requests
from typing import Optional, Callable, Any

def retry_with_backoff(func: Callable,
                        max_retries: int = 3,
                        initial_delay: float = 1.0,
                        backoff_factor: float = 2.0) -> Optional[Any]:
    """
    Retry function with exponential backoff

    Use for OLS API calls, OAK lookups that may timeout
    """
    delay = initial_delay

    for attempt in range(max_retries):
        try:
            return func()
        except requests.exceptions.RequestException as e:
            if attempt == max_retries - 1:
                print(f"Max retries exceeded: {e}")
                return None

            print(f"Attempt {attempt + 1} failed, retrying in {delay}s...")
            time.sleep(delay)
            delay *= backoff_factor

    return None

# Usage
def fetch_ols_data(ontology_id):
    return requests.get(f"https://www.ebi.ac.uk/ols4/api/.../{ontology_id}")

result = retry_with_backoff(lambda: fetch_ols_data("CHEBI:26710"))
```

### Fallback Strategies

**OAK Lookup Failure:**
1. Try local OWL file (if cached)
2. Fall back to OLS API
3. Mark as "validation_pending" if all fail

**OLS API Failure:**
1. Check local cache (previous enrichment)
2. Try PubChem API as alternative
3. Skip enrichment, continue validation

**Batch Processing Failure:**
1. Checkpoint progress every N ingredients
2. Resume from last checkpoint on restart
3. Collect errors, continue with remaining

**Checkpoint Example:**

```python
import json
from pathlib import Path

class CheckpointManager:
    def __init__(self, checkpoint_file: str):
        self.checkpoint_file = Path(checkpoint_file)
        self.state = self.load()

    def load(self):
        if self.checkpoint_file.exists():
            with open(self.checkpoint_file) as f:
                return json.load(f)
        return {"completed": [], "errors": [], "last_index": 0}

    def save(self):
        with open(self.checkpoint_file, 'w') as f:
            json.dump(self.state, f, indent=2)

    def mark_completed(self, item_id: str, index: int):
        self.state["completed"].append(item_id)
        self.state["last_index"] = index
        self.save()

    def mark_error(self, item_id: str, error: str):
        self.state["errors"].append({"id": item_id, "error": error})
        self.save()

# Usage in batch processing
checkpoint = CheckpointManager("progress.json")
start_index = checkpoint.state["last_index"]

for i, ingredient in enumerate(ingredients[start_index:], start=start_index):
    try:
        result = validate_ingredient(ingredient)
        checkpoint.mark_completed(ingredient['id'], i)
    except Exception as e:
        checkpoint.mark_error(ingredient['id'], str(e))
```

---

## Troubleshooting

### Issue: OAK Adapter Fails to Load

**Symptoms:**
```
Error: Could not create adapter for sqlite:obo:chebi
```

**Causes:**
- OWL file not in cache
- Invalid OWL syntax
- OAK version mismatch

**Solutions:**
```bash
# Re-download OWL file
python scripts/download_ontologies.py --force --sources CHEBI

# Verify file integrity
python scripts/download_ontologies.py --verify

# Check OAK version
pip show oaklib

# Try remote adapter instead
# (Edit IngredientReviewer to use OAK remote not local)
```

### Issue: OLS API Rate Limiting (429 Error)

**Symptoms:**
```
requests.exceptions.HTTPError: 429 Client Error: Too Many Requests
```

**Causes:**
- Too many requests in short time
- No delay between calls

**Solutions:**
```bash
# Increase delay in enrich_from_ols.py
PYTHONPATH=src python scripts/enrich_from_ols.py --delay 1.0

# Reduce batch size
PYTHONPATH=src python scripts/enrich_from_ols.py --batch-size 20

# Use cached results
# (Script automatically caches, resume with --resume)
```

### Issue: Label Mismatch False Positives

**Symptoms:**
```
P2.1 Label Mismatch: "calcium chloride" vs "calcium dichloride"
```

**Causes:**
- Synonymous terms (not actually wrong)
- Chemical nomenclature variations

**Solutions:**
1. **Review manually** - If labels are synonymous, accept as-is
2. **Add to whitelist** - Configure IngredientReviewer to allow known synonyms
3. **Update preferred_term** - If ontology label is more standard, use it

```python
# In ingredient_reviewer.py, add synonym whitelist
KNOWN_SYNONYMS = {
    ("calcium chloride", "calcium dichloride"),
    ("sodium chloride", "sodium chloride (1:1)"),
    # ...
}

def is_known_synonym_pair(label1, label2):
    pair = tuple(sorted([label1.lower(), label2.lower()]))
    return pair in KNOWN_SYNONYMS
```

### Issue: Batch Processing Out of Memory

**Symptoms:**
```
MemoryError: Unable to allocate array
```

**Causes:**
- Loading all 1,034 ingredients into memory
- Parallel processing with too many workers

**Solutions:**
```bash
# Reduce parallel workers
PYTHONPATH=src python scripts/batch_review.py --threads 2

# Process in chunks
for i in {0..1000..100}; do
  PYTHONPATH=src python scripts/batch_review.py --offset $i --limit 100
done

# Use streaming mode (process one at a time)
PYTHONPATH=src python scripts/batch_review.py --streaming
```

### Issue: Chemical Properties Not Found in OLS

**Symptoms:**
```
P3.1 Missing Chemical Properties: No SMILES/InChI available
```

**Causes:**
- CHEBI term has no structure data
- OLS API doesn't include annotation
- Term is not a chemical (e.g., role term)

**Solutions:**
1. **Check CHEBI directly** - Visit CHEBI website, verify if structure exists
2. **Try PubChem** - Fallback API for common chemicals
3. **Accept limitation** - Some terms genuinely lack structure (ions, mixtures)

```python
# Add PubChem fallback in enrich_from_ols()
def enrich_from_ols_or_pubchem(ontology_id):
    # Try OLS first
    props = enrich_from_ols(ontology_id)
    if props:
        return props

    # Fallback to PubChem
    # (Convert CHEBI ID to PubChem CID via PUG REST)
    return enrich_from_pubchem(ontology_id)
```

### Issue: Validation Takes Too Long

**Symptoms:**
- Batch review of 1,034 ingredients takes > 30 minutes

**Optimization:**
```bash
# Use local OWL files (no network calls)
python scripts/download_ontologies.py --all
PYTHONPATH=src python scripts/batch_review.py --use-local-owl

# Increase parallelism
PYTHONPATH=src python scripts/batch_review.py --threads 16

# Skip expensive checks (LLM semantic comparison)
PYTHONPATH=src python scripts/batch_review.py --skip-llm

# Cache OAK lookups
# (IngredientReviewer automatically caches term_info in memory)
```

---

## Examples and Scenarios

### Example 1: Post-Curation Quality Check

**Scenario:** You've just completed a curation session mapping 50 unmapped ingredients. Before committing, validate the new mappings.

```bash
# 1. Review the newly mapped ingredients interactively
for term in "glucose" "sodium chloride" "calcium chloride dihydrate"; do
  PYTHONPATH=src python scripts/review_ingredient.py "$term" --suggest-fixes
done

# 2. Run batch review on all mapped ingredients
PYTHONPATH=src python scripts/batch_review.py \
  --output reports/post_curation_$(date +%Y%m%d) \
  --priority P1,P2 \
  --format md,json

# 3. Check for critical errors
grep "P1" reports/post_curation_*/validation_report.md

# 4. If no P1 errors, auto-enrich P3/P4
PYTHONPATH=src python scripts/auto_correct.py --apply --types chemical_properties

# 5. Commit with confidence
git add data/curated/mapped_ingredients.yaml
git commit -m "Add 50 newly curated ingredients (validated, no P1 errors)"
```

### Example 2: Pre-Export Validation

**Scenario:** Before exporting to KG-Microbe, ensure data quality meets standards.

```bash
# 1. Full batch validation
PYTHONPATH=src python scripts/batch_review.py \
  --output reports/pre_export_$(date +%Y%m%d) \
  --format md,json,html \
  --threads 8

# 2. Review HTML dashboard
open reports/pre_export_*/dashboard.html

# 3. Fix P1 critical errors (if any)
# (Manually review and correct in YAML)

# 4. Auto-correct P3/P4
PYTHONPATH=src python scripts/auto_correct.py --apply

# 5. Re-validate to confirm
PYTHONPATH=src python scripts/batch_review.py --priority P1 --limit 1034

# 6. Export if clean
PYTHONPATH=src python scripts/kgx_export.py
```

### Example 3: Synonym Enrichment

**Scenario:** Improve searchability by adding synonyms from ontologies.

```bash
# 1. Check which ingredients are missing synonyms
PYTHONPATH=src python scripts/validate_synonyms.py --report-only > synonym_report.txt

# 2. Review report
less synonym_report.txt

# 3. Auto-add high-confidence exact synonyms
PYTHONPATH=src python scripts/validate_synonyms.py \
  --add-missing \
  --types EXACT

# 4. Manually review related synonyms (more subjective)
PYTHONPATH=src python scripts/validate_synonyms.py \
  --add-missing \
  --types RELATED \
  --interactive
```

### Example 4: Deprecated Term Migration

**Scenario:** CHEBI released new version, some terms deprecated. Find and update them.

```bash
# 1. Download latest CHEBI OWL
python scripts/download_ontologies.py --sources CHEBI --force

# 2. Run validation with local OWL
PYTHONPATH=src python scripts/batch_review.py \
  --use-local-owl \
  --priority P2 \
  --filter-rule P2.3

# 3. Review deprecated terms
grep "P2.3.*Deprecated" reports/*/validation_report.md

# 4. Check replacement terms in OWL
PYTHONPATH=src python -c "
from oaklib import get_adapter
adapter = get_adapter('sqlite:obo:chebi.owl')
replacements = adapter.get_term_replaced_by('CHEBI:30063')
print(f'Replace with: {replacements[0]}')
"

# 5. Manually update ontology IDs in YAML
# (Use IngredientCurator.update_mapping())

# 6. Re-validate
PYTHONPATH=src python scripts/batch_review.py --priority P2 --filter-rule P2.3
```

---

## Integration with Existing Workflows

### Post-Curation Workflow

**Current:**
1. Run `curate_unmapped.py`
2. Accept mappings interactively
3. Save to `mapped_ingredients.yaml`
4. Commit changes

**Enhanced:**
1. Run `curate_unmapped.py`
2. Accept mappings interactively
3. **NEW: Auto-validate on save** (call `IngredientReviewer.review_ingredient()`)
4. **NEW: Block save if P1 errors** (prompt user to fix)
5. Save to `mapped_ingredients.yaml`
6. **NEW: Run batch validation before commit**
7. Commit changes with validation report

**Integration Point:**

```python
# In curate_unmapped.py, after accept_mapping():
from mediaingredientmech.validation.ingredient_reviewer import IngredientReviewer

reviewer = IngredientReviewer()

def save_with_validation(curator, ingredient):
    # Validate before saving
    result = reviewer.review_ingredient(ingredient)

    if any(issue.priority == "P1" for issue in result.issues):
        console.print("[red]❌ P1 critical error - cannot save[/red]")
        for issue in result.issues:
            if issue.priority == "P1":
                console.print(f"  - {issue.message}")
        return False

    # Save if validation passed
    curator.save()

    # Show warnings
    if result.status == "WARNING":
        console.print(f"[yellow]⚠️  {len(result.issues)} warnings[/yellow]")

    return True
```

### Pre-Export Workflow

**Current:**
1. Run `kgx_export.py`
2. Generate nodes.tsv, edges.tsv
3. Ingest into KG-Microbe

**Enhanced:**
1. **NEW: Run batch validation** → Generate report
2. **NEW: Block export if P1 errors** → Show error count
3. Run `kgx_export.py`
4. **NEW: Attach validation report to export metadata**
5. Generate nodes.tsv, edges.tsv
6. Ingest into KG-Microbe with QA provenance

**Integration Point:**

```python
# In kgx_export.py, before export:
from mediaingredientmech.validation.ingredient_reviewer import IngredientReviewer

reviewer = IngredientReviewer()
curator = IngredientCurator()

mapped = curator.get_by_status("MAPPED")
results = reviewer.batch_review(mapped, priority_filter=["P1"])

if results.summary["P1"] > 0:
    print(f"❌ Cannot export: {results.summary['P1']} P1 critical errors")
    print("Run: python scripts/batch_review.py --priority P1")
    sys.exit(1)

print(f"✓ Validation passed: 0 P1 errors, {results.summary['P2']} P2 warnings")
# Proceed with export
```

### Periodic Maintenance Workflow

**Schedule:** Monthly (after CultureMech updates)

```bash
#!/bin/bash
# monthly_validation.sh

DATE=$(date +%Y%m%d)
REPORT_DIR="reports/monthly_$DATE"

# 1. Update ontologies
echo "Downloading latest ontologies..."
python scripts/download_ontologies.py --all

# 2. Run full validation
echo "Running batch validation..."
PYTHONPATH=src python scripts/batch_review.py \
  --output "$REPORT_DIR" \
  --format md,json,html \
  --use-local-owl \
  --threads 8

# 3. Auto-correct safe issues
echo "Auto-correcting P3/P4 issues..."
PYTHONPATH=src python scripts/auto_correct.py --apply

# 4. Generate summary email
echo "Validation complete. Summary:" > "$REPORT_DIR/summary.txt"
grep "Summary Statistics" -A 10 "$REPORT_DIR/validation_report.md" >> "$REPORT_DIR/summary.txt"

# 5. Commit changes
if [ -n "$(git status --porcelain data/curated/)" ]; then
  git add data/curated/
  git commit -m "Monthly validation and auto-correction ($DATE)"
fi

# 6. Send notification
mail -s "MediaIngredientMech Monthly Validation" team@example.com < "$REPORT_DIR/summary.txt"
```

---

## Validation Metrics and Quality Trends

### Key Metrics to Track

1. **P1 Error Rate**: Critical errors / total ingredients (target: 0%)
2. **P2 Warning Rate**: High-priority warnings / total (target: < 1%)
3. **Enrichment Coverage**: Ingredients with chemical properties / CHEBI-mapped (target: > 95%)
4. **Synonym Completeness**: Avg synonyms per ingredient (target: > 3)
5. **Validation Pass Rate**: Ingredients with zero issues (target: > 80%)

### Trend Dashboard

```python
# Track metrics over time in validation_history.json
{
  "2026-03-15": {
    "total_ingredients": 1034,
    "P1_errors": 0,
    "P2_warnings": 12,
    "P3_warnings": 234,
    "P4_info": 456,
    "enrichment_coverage": 0.92,
    "avg_synonyms": 2.8
  },
  "2026-04-15": {
    "total_ingredients": 1098,
    "P1_errors": 0,
    "P2_warnings": 8,
    "P3_warnings": 189,
    "P4_info": 423,
    "enrichment_coverage": 0.97,
    "avg_synonyms": 3.4
  }
}
```

### Quality Score Formula

```python
def calculate_quality_score(validation_summary):
    """
    Calculate overall quality score (0-100)

    Weights:
      - P1 errors: -50 points each
      - P2 warnings: -5 points each
      - P3 warnings: -1 point each
      - Enrichment coverage: +20 points
      - Synonym completeness: +10 points
    """
    base_score = 100

    base_score -= validation_summary["P1"] * 50
    base_score -= validation_summary["P2"] * 5
    base_score -= validation_summary["P3"] * 1

    base_score += validation_summary["enrichment_coverage"] * 20
    base_score += min(validation_summary["avg_synonyms"] / 5, 1.0) * 10

    return max(0, min(100, base_score))
```

---

## Advanced Features (Future Enhancements)

### 1. Machine Learning-Assisted Validation

**Idea:** Train classifier to predict P2 label mismatches

```python
# Features: edit distance, token overlap, SMILES similarity
# Labels: "correct mapping" vs "incorrect mapping"
# Model: Random Forest or BERT-based

from sklearn.ensemble import RandomForestClassifier

def train_mismatch_detector(training_data):
    X = extract_features(training_data)  # edit distance, etc.
    y = [t['is_correct'] for t in training_data]

    model = RandomForestClassifier()
    model.fit(X, y)
    return model

def predict_mismatch(model, ingredient, ontology_label):
    features = extract_features_single(ingredient, ontology_label)
    probability = model.predict_proba([features])[0][1]
    return probability > 0.7  # Likely mismatch
```

### 2. Ontology Version Diff

**Idea:** Detect changes between ontology versions

```bash
# Compare CHEBI v2024-01 vs v2024-03
python scripts/ontology_diff.py \
  --old ontology/cache/chebi_v2024-01.owl \
  --new ontology/cache/chebi_v2024-03.owl \
  --report reports/chebi_diff_2024-03.md
```

**Output:**
- New terms added
- Terms deprecated
- Label changes
- Definition changes
- Impacted MediaIngredientMech ingredients

### 3. Cross-Repository Validation

**Idea:** Validate consistency with CultureMech mappings

```python
# Check if MediaIngredientMech and CultureMech agree on mappings
def compare_with_culturemech(ingredient_name):
    mim_mapping = curator.get_by_preferred_term(ingredient_name)
    cm_mapping = load_culturemech_mapping(ingredient_name)

    if mim_mapping['ontology_id'] != cm_mapping['ontology_id']:
        print(f"⚠️  Conflict: {ingredient_name}")
        print(f"  MediaIngredientMech: {mim_mapping['ontology_id']}")
        print(f"  CultureMech: {cm_mapping['ontology_id']}")

        # Suggest resolution (e.g., defer to higher confidence)
```

### 4. Real-Time Validation in Curation UI

**Idea:** Validate as user types in `curate_unmapped.py`

```python
# In curate_unmapped.py, add live validation:
from mediaingredientmech.validation.ingredient_reviewer import IngredientReviewer

reviewer = IngredientReviewer()

def on_accept_mapping(ingredient, ontology_id):
    # Validate in real-time
    temp_ingredient = ingredient.copy()
    temp_ingredient['ontology_mapping'] = {'ontology_id': ontology_id}

    result = reviewer.review_ingredient(temp_ingredient)

    if result.status == "ERROR":
        console.print("[red]⚠️  Validation failed[/red]")
        show_issues(result.issues)
        return False  # Block acceptance

    return True  # Allow acceptance
```
