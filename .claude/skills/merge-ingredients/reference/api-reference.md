# API Reference & Advanced Usage

*Reference for the **merge-ingredients** skill — see [`../skill.md`](../skill.md) for the overview, strategies, decision summary, and best practices.*

---

## API Reference

### CHEBIDeduplicator

**Initialization**:
```python
from mediaingredientmech.curation.chebi_deduplicator import CHEBIDeduplicator
from mediaingredientmech.curation.ingredient_curator import IngredientCurator

curator = IngredientCurator(data_path="data/curated/unmapped_ingredients.yaml")
curator.load()

dedup = CHEBIDeduplicator(curator)
```

**Methods**:

#### `find_chebi_duplicates() -> dict[str, list[int]]`
Group record indices by shared CHEBI ID.

**Returns**: Dict mapping CHEBI ID to list of record indices (2+ records only).

**Example**:
```python
duplicates = dedup.find_chebi_duplicates()
# {'CHEBI:26710': [5, 12, 30], 'CHEBI:32599': [10, 25]}
```

#### `choose_merge_target(duplicate_group: list[int]) -> int`
Select best record as merge target.

**Args**:
- `duplicate_group`: List of record indices with same CHEBI ID

**Returns**: Index of merge target (highest quality, most occurrences).

**Example**:
```python
target = dedup.choose_merge_target([5, 12, 30])
# 5 (highest quality or most occurrences)
```

#### `should_auto_merge(target_idx: int, source_idx: int) -> tuple[bool, str]`
Determine if records should auto-merge.

**Args**:
- `target_idx`: Merge target record index
- `source_idx`: Source record index

**Returns**: Tuple of (should_merge, reason).

**Example**:
```python
can_merge, reason = dedup.should_auto_merge(5, 12)
# (True, "Same CHEBI ID + same quality (EXACT_MATCH)")
```

#### `merge_duplicates(dry_run: bool = True, auto_merge: bool = False) -> dict`
Find and merge all CHEBI duplicates.

**Args**:
- `dry_run`: Preview only, don't execute merges
- `auto_merge`: Automatically merge records passing auto-merge criteria

**Returns**: Dict with keys:
- `merged`: List of (target_idx, source_indices, chebi_id) tuples
- `flagged`: List of (chebi_id, indices, reason) tuples
- `total_removed`: Count of records marked REJECTED

**Example**:
```python
results = dedup.merge_duplicates(dry_run=False, auto_merge=True)
# {'merged': [(5, [12, 30], 'CHEBI:26710')], 'flagged': [], 'total_removed': 2}
```

#### `validate_no_chebi_duplicates() -> tuple[bool, list[str]]`
Validate no CHEBI duplicates remain.

**Returns**: Tuple of (is_valid, error_messages).

**Example**:
```python
is_valid, errors = dedup.validate_no_chebi_duplicates()
if not is_valid:
    print("Errors:", errors)
```

### SolutionMatcher

**Initialization**:
```python
from mediaingredientmech.curation.solution_matcher import SolutionMatcher

matcher = SolutionMatcher()
```

**Methods**:

#### `detect_type(name: str) -> str`
Detect ingredient type based on name patterns.

**Returns**: SOLUTION, BUFFER, STOCK, TRACE_METAL, MACRO, MICRO, VITAMIN, MINERAL, or CHEMICAL.

**Example**:
```python
matcher.detect_type("Trace metal solution")  # "TRACE_METAL"
matcher.detect_type("KH2PO4 buffer")  # "BUFFER"
matcher.detect_type("NaCl")  # "CHEMICAL"
```

#### `extract_base_name(name: str) -> str`
Extract base chemical name by stripping type suffix.

**Example**:
```python
matcher.extract_base_name("Trace metal solution")  # "Trace metal"
matcher.extract_base_name("KH2PO4 buffer")  # "KH2PO4"
```

#### `match_confidence(name1: str, name2: str) -> float`
Calculate similarity confidence for two names.

**Returns**: Score 0.0-1.0.

**Example**:
```python
matcher.match_confidence("Trace metal solution", "Trace metal buffer")  # 0.9
matcher.match_confidence("Macro solution", "Micronutrient solution")  # 0.2
```

#### `find_solution_duplicates(records: list[dict], threshold: float = 0.9) -> list[tuple[int, int, float]]`
Find potential duplicate solution/buffer/stock records.

**Returns**: List of (idx1, idx2, confidence) tuples.

**Example**:
```python
duplicates = matcher.find_solution_duplicates(curator.records, threshold=0.85)
# [(10, 25, 0.95), (15, 32, 0.87)]
```

### KGMicrobeSearcher

**Initialization**:
```python
from mediaingredientmech.utils.kg_microbe_searcher import KGMicrobeSearcher
from pathlib import Path

searcher = KGMicrobeSearcher(
    Path("/path/to/CultureMech/output/mapped_ingredients.yaml")
)
```

**Methods**:

#### `search_by_chebi_id(chebi_id: str) -> list[dict]`
Find CultureMech records with matching CHEBI ID.

**Example**:
```python
matches = searcher.search_by_chebi_id("CHEBI:26710")
# [{'preferred_term': 'NaCl', 'ontology_id': 'CHEBI:26710', ...}]
```

#### `search_by_name(name: str, threshold: float = 0.8) -> list[tuple[dict, float]]`
Fuzzy name search with similarity scores.

**Example**:
```python
matches = searcher.search_by_name("sodium chloride", threshold=0.7)
# [({'preferred_term': 'NaCl', ...}, 0.9), ...]
```

#### `find_matches(ingredient_record: dict) -> dict`
Find all potential matches for an ingredient record.

**Returns**: Dict with 'chebi_matches' and 'name_matches'.

**Example**:
```python
matches = searcher.find_matches(curator.records[5])
# {'chebi_matches': [...], 'name_matches': [...]}
```

#### `get_statistics() -> dict`
Get statistics about CultureMech data.

**Example**:
```python
stats = searcher.get_statistics()
# {'total_records': 995, 'unique_chebi_ids': 823, 'source_breakdown': {...}}
```

---

## Advanced Usage

### Custom Merge Logic

**Extend CHEBIDeduplicator**:
```python
class CustomDeduplicator(CHEBIDeduplicator):
    def choose_merge_target(self, duplicate_group: list[int]) -> int:
        # Custom logic: prefer records with more synonyms
        def score(idx):
            record = self.curator.records[idx]
            synonym_count = len(record.get('synonyms', []) or [])
            return (synonym_count, super().score_record(idx))

        return max(duplicate_group, key=score)
```

### Batch Processing

**Process multiple files**:
```python
import glob
from pathlib import Path

for file_path in glob.glob("data/batches/*.yaml"):
    curator = IngredientCurator(data_path=Path(file_path))
    curator.load()

    dedup = CHEBIDeduplicator(curator)
    results = dedup.merge_duplicates(dry_run=False)

    if results['merged']:
        curator.save()
        print(f"Processed {file_path}: {results['total_removed']} merged")
```

### Integration with CI/CD

**Pre-commit hook**:
```bash
#!/bin/bash
# .git/hooks/pre-commit

# Run deduplication check
python scripts/deduplicate_ingredients.py --dry-run > /tmp/dedup_check.txt

# Check for duplicates
if grep -q "Merged groups: [1-9]" /tmp/dedup_check.txt; then
    echo "ERROR: CHEBI duplicates detected. Run deduplication before committing."
    cat /tmp/dedup_check.txt
    exit 1
fi
```

### Automated Reconciliation

**Nightly sync**:
```python
import schedule
import time

def daily_reconciliation():
    # Run deduplication
    os.system("python scripts/deduplicate_ingredients.py")

    # Search KG-Microbe
    os.system("python scripts/deduplicate_ingredients.py --search-kg-microbe")

    # Send report
    send_email_report()

schedule.every().day.at("02:00").do(daily_reconciliation)

while True:
    schedule.run_pending()
    time.sleep(3600)
```

---

