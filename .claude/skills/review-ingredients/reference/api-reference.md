# API Reference & Output Formats

*Reference for the **review-ingredients** skill — see [`../skill.md`](../skill.md) for the overview, workflows, and rule summary.*

---

## API Reference

### IngredientReviewer Class

**Location:** `src/mediaingredientmech/validation/ingredient_reviewer.py`

#### Constructor

```python
class IngredientReviewer:
    """
    Core validation orchestrator for ingredient quality assurance

    Integrates:
      - OAK for term existence/metadata
      - OLS for chemical properties enrichment
      - LinkML for schema validation
      - Custom rules for domain logic (purity, dual identifiers)
    """

    def __init__(self,
                 use_local_owl: bool = False,
                 owl_cache_dir: str = "ontology/cache",
                 enable_llm: bool = False):
        """
        Args:
            use_local_owl: Use cached OWL files instead of OAK remote
            owl_cache_dir: Directory containing chebi.owl, foodon.owl, etc.
            enable_llm: Enable LLM-assisted semantic comparison (P2.2)
        """
```

#### Core Methods

**review_ingredient(ingredient_record: Dict) -> ReviewResult**

```python
def review_ingredient(self, ingredient_record: Dict) -> ReviewResult:
    """
    Validate single ingredient against all rules (P1-P4)

    Args:
        ingredient_record: Dict from YAML (IngredientRecord)

    Returns:
        ReviewResult with:
          - status: PASS | WARNING | ERROR
          - issues: List[ValidationIssue]
          - suggestions: List[CorrectionSuggestion]
          - metadata: Validation metadata (duration, timestamp)

    Example:
        reviewer = IngredientReviewer()
        result = reviewer.review_ingredient(ingredient_dict)

        if result.status == "ERROR":
            print("P1 critical errors found:")
            for issue in result.issues:
                if issue.priority == "P1":
                    print(f"  - {issue.message}")
    """
```

**batch_review(ingredient_records: List[Dict], priority_filter: List[str] = None) -> BatchReviewResult**

```python
def batch_review(self,
                  ingredient_records: List[Dict],
                  priority_filter: List[str] = None,
                  parallel: bool = True,
                  max_workers: int = 4) -> BatchReviewResult:
    """
    Validate multiple ingredients in parallel

    Args:
        ingredient_records: List of ingredient dicts
        priority_filter: Only report these priorities (e.g., ["P1", "P2"])
        parallel: Use ThreadPoolExecutor for concurrent validation
        max_workers: Number of parallel threads

    Returns:
        BatchReviewResult with:
          - summary: Statistics by priority
          - all_issues: Aggregated ValidationIssue list
          - all_suggestions: Aggregated CorrectionSuggestion list
          - failed: Ingredients that errored during validation

    Example:
        results = reviewer.batch_review(
            mapped_ingredients,
            priority_filter=["P1", "P2"],
            max_workers=8
        )

        print(f"P1 errors: {results.summary['P1']}")
        print(f"P2 warnings: {results.summary['P2']}")
    """
```

**auto_correct(ingredient_record: Dict, correction_types: List[str] = None) -> Dict**

```python
def auto_correct(self,
                  ingredient_record: Dict,
                  correction_types: List[str] = None) -> Dict:
    """
    Auto-apply safe corrections (P3/P4 only)

    Args:
        ingredient_record: Ingredient to correct
        correction_types: Which corrections to apply
          - "chemical_properties": Enrich from OLS
          - "synonyms": Add missing ontology synonyms
          - "curie_format": Normalize CURIE format
          - None: Apply all safe corrections

    Returns:
        Updated ingredient_record dict (does not save to file)

    Example:
        corrected = reviewer.auto_correct(
            ingredient,
            correction_types=["chemical_properties", "synonyms"]
        )

        # Review changes
        print(corrected.get('chemical_properties'))

        # Apply if satisfied
        curator.update_ingredient(corrected)
    """
```

**enrich_from_ols(ontology_id: str) -> Dict**

```python
def enrich_from_ols(self, ontology_id: str) -> Dict:
    """
    Fetch chemical properties from EBI OLS v4 API

    Args:
        ontology_id: CHEBI CURIE (e.g., "CHEBI:26710")

    Returns:
        Dict with chemical_properties section:
          {
            "molecular_formula": "NaCl",
            "smiles": "[Na+].[Cl-]",
            "inchi": "InChI=1S/ClH.Na/h1H;/q;+1/p-1",
            "inchikey": "FAPWRFPIFSIZLT-UHFFFAOYSA-M",
            "monoisotopic_mass": 57.958622,
            "average_mass": 58.443
          }

    Returns None if:
      - Not a CHEBI term
      - OLS API error
      - No chemical properties available

    Example:
        props = reviewer.enrich_from_ols("CHEBI:26710")
        if props:
            ingredient['chemical_properties'] = props
    """
```

#### Helper Methods

**validate_curie(curie: str) -> bool**

```python
def validate_curie(self, curie: str) -> bool:
    """Check if string is valid CURIE format (PREFIX:ID)"""
```

**check_term_exists(ontology_id: str) -> bool**

```python
def check_term_exists(self, ontology_id: str) -> bool:
    """Check if term exists in ontology via OAK"""
```

**get_ontology_label(ontology_id: str) -> Optional[str]**

```python
def get_ontology_label(self, ontology_id: str) -> Optional[str]:
    """Fetch canonical label from ontology"""
```

**compare_labels(label1: str, label2: str) -> float**

```python
def compare_labels(self, label1: str, label2: str) -> float:
    """
    Compare label similarity
    Returns: 0.0 (no match) to 1.0 (exact match)
    """
```

### Supporting Classes

**ReviewResult**

```python
@dataclass
class ReviewResult:
    status: str  # "PASS" | "WARNING" | "ERROR"
    issues: List[ValidationIssue]
    suggestions: List[CorrectionSuggestion]
    metadata: Dict  # {timestamp, duration_ms, rules_checked}
```

**ValidationIssue**

```python
@dataclass
class ValidationIssue:
    priority: str  # "P1" | "P2" | "P3" | "P4"
    rule_id: str  # e.g., "P1.1", "P2.3"
    category: str  # e.g., "label_mismatch", "missing_properties"
    message: str  # Human-readable description
    evidence: Dict  # Supporting data for issue
    ingredient_id: str  # Which ingredient
```

**CorrectionSuggestion**

```python
@dataclass
class CorrectionSuggestion:
    action: str  # "update_field", "enrich_properties", "add_synonym"
    field_path: str  # e.g., "ontology_mapping.ontology_id"
    current_value: Any
    suggested_value: Any
    auto_correctable: bool  # Can be applied without human review
    confidence: float  # 0.0 to 1.0
    rationale: str  # Why this correction
```

---

## Output Formats

### Markdown Report

**File:** `validation_report.md`

```markdown
# Ingredient Validation Report
Generated: 2026-03-15 14:30:00

## Summary Statistics
- Total ingredients reviewed: 1,034
- P1 Critical errors: 0
- P2 High-priority warnings: 12 (1.2%)
- P3 Medium-priority warnings: 234 (22.6%)
- P4 Low-priority info: 456 (44.1%)

## P1 Critical Errors (0)
*No critical errors found*

## P2 High-Priority Warnings (12)

### P2.1 Label Mismatch (8)
1. **calcium chloride**
   - Ontology ID: CHEBI:3312
   - Expected: calcium chloride
   - Ontology label: calcium dichloride
   - Edit distance: 4
   - **Action:** Review - terms are synonymous

2. **glucose**
   - Ontology ID: CHEBI:17234
   - Expected: glucose
   - Ontology label: D-glucose
   - **Action:** Update preferred_term to "D-glucose"

...

### P2.3 Deprecated Terms (4)
1. **ferric chloride**
   - Ontology ID: CHEBI:30063 (deprecated)
   - Replacement: CHEBI:82664 (iron(III) chloride)
   - **Action:** Re-map to CHEBI:82664

...

## P3 Medium-Priority Warnings (234)

### P3.1 Missing Chemical Properties (186)
- 186 CHEBI-mapped ingredients missing SMILES/InChI
- **Action:** Run `auto_correct.py --types chemical_properties`

### P3.2 Missing Synonyms (48)
...
```

### JSON Report

**File:** `validation_data.json`

```json
{
  "metadata": {
    "generated": "2026-03-15T14:30:00Z",
    "total_reviewed": 1034,
    "summary": {
      "P1": 0,
      "P2": 12,
      "P3": 234,
      "P4": 456
    }
  },
  "issues": [
    {
      "ingredient": "glucose",
      "preferred_term": "glucose",
      "ontology_id": "CHEBI:17234",
      "priority": "P2",
      "rule_id": "P2.1",
      "category": "label_mismatch",
      "message": "Ontology label 'D-glucose' differs from preferred term 'glucose'",
      "evidence": {
        "expected_label": "glucose",
        "ontology_label": "D-glucose",
        "edit_distance": 2
      },
      "suggestion": {
        "action": "update_preferred_term",
        "new_value": "D-glucose",
        "auto_correctable": false,
        "confidence": 0.95
      }
    },
    {
      "ingredient": "sodium chloride",
      "preferred_term": "sodium chloride",
      "ontology_id": "CHEBI:26710",
      "priority": "P3",
      "rule_id": "P3.1",
      "category": "missing_chemical_properties",
      "message": "Missing SMILES, InChI, molecular formula",
      "evidence": {
        "has_smiles": false,
        "has_inchi": false,
        "has_formula": false
      },
      "suggestion": {
        "action": "enrich_from_ols",
        "auto_correctable": true,
        "confidence": 1.0,
        "preview": {
          "molecular_formula": "NaCl",
          "smiles": "[Na+].[Cl-]",
          "inchi": "InChI=1S/ClH.Na/h1H;/q;+1/p-1"
        }
      }
    }
  ],
  "corrections": {
    "auto_correctable": 234,
    "manual_review": 12,
    "total": 246
  }
}
```

### HTML Dashboard

**File:** `dashboard.html`

Interactive web dashboard with:
- Sortable table of all issues
- Filterable by priority, category, ontology source
- Click to expand evidence and suggestions
- Export filtered results to CSV
- Apply corrections via JSON export

**Features:**
- DataTables.js for sorting/filtering
- Bootstrap for styling
- Export buttons (CSV, JSON, PDF)
- Progress bars for summary stats

