---
name: review-ingredients
description: Quality assurance and validation for ontology-mapped ingredients using OAK, OLS, and OWL reasoning
version: 1.0.0
tags: [validation, quality-assurance, ontology, oak, ols, owl, chebi, foodon, envo]
author: MediaIngredientMech Team
created: 2026-03-15
---

# Review Ingredients Skill

## Overview

The **Review Ingredients** skill provides comprehensive quality assurance and validation for ontology-mapped ingredients in MediaIngredientMech. It systematically verifies that:

1. **Ontology mappings are correct** - Term exists, label matches, definition appropriate
2. **Identifiers are valid** - Proper CURIE format, dual identifier system consistency
3. **Synonyms are accurate** - Chemical variants preserved, no duplicates
4. **Chemical properties are enriched** - SMILES, InChI, molecular formulas populated
5. **Merge integrity is maintained** - Purity-aware merge rules followed

**Technology Stack:**
- **OAK (Ontology Access Kit)**: Verify terms exist in CHEBI/FOODON/ENVO ontologies
- **EBI OLS v4 API**: Enrich metadata (formulas, SMILES, InChI, definitions)
- **OWL Files**: Enable offline validation and advanced reasoning (cached locally)
- **LinkML Schema**: Validate YAML structure and field constraints

**Current Dataset:** 1,102 total ingredients
- 1,034 mapped ingredients (93.8%) with ontology IDs
- 68 unmapped ingredients (6.2%) - intentionally unmappable

---

## When to Use This Skill

| Scenario | Workflow | Priority |
|----------|----------|----------|
| **Post-curation QA** | Validate newly mapped ingredients before committing | High |
| **Batch validation** | Review all 1,034 mapped ingredients | High |
| **Pre-export check** | Ensure KG export quality before KG-Microbe ingestion | Critical |
| **Periodic maintenance** | Monthly validation after CultureMech updates | Medium |
| **Synonym verification** | Cross-check synonyms with ontology data | Medium |
| **Chemical enrichment** | Populate SMILES, InChI, formulas from OLS | Low |
| **Duplicate detection** | Find potential merge candidates | Low |

**Decision Table:**

```
IF newly mapped batch → Use interactive review
IF full dataset check → Use batch review
IF enrichment needed → Use auto-correct (P3/P4)
IF critical errors → Use batch review with P1 filter
IF synonym issues → Use validate_synonyms.py
```

---

## Review Workflows

### 1. Interactive Review (Single Ingredient)

**Use case:** Verify a specific ingredient after manual curation

```bash
# Review by preferred term
PYTHONPATH=src python scripts/review_ingredient.py "sodium chloride"

# Review by ontology ID
PYTHONPATH=src python scripts/review_ingredient.py --id CHEBI:26710

# Review with auto-correction suggestions
PYTHONPATH=src python scripts/review_ingredient.py "glucose" --suggest-fixes
```

**Output:**
- Rich UI panel showing current mapping
- Validation results (P1-P4 issues)
- Suggested corrections with apply/skip options
- Ontology metadata comparison

### 2. Batch Review (All Ingredients)

**Use case:** Validate entire dataset, generate comprehensive report

```bash
# Review all mapped ingredients
PYTHONPATH=src python scripts/batch_review.py \
  --output reports/validation_$(date +%Y%m%d) \
  --format md,json,html \
  --threads 4

# Filter by priority
PYTHONPATH=src python scripts/batch_review.py --priority P1,P2

# Filter by ontology source
PYTHONPATH=src python scripts/batch_review.py --source CHEBI

# Limit for testing
PYTHONPATH=src python scripts/batch_review.py --limit 10 --dry-run
```

**Output:**
- `validation_report.md`: Human-readable summary with statistics
- `validation_data.json`: Machine-readable issues + corrections
- `dashboard.html`: Interactive sortable/filterable dashboard

### 3. Automated Correction (P3/P4 Safe Issues)

**Use case:** Auto-fix issues that don't require human review

```bash
# Dry-run to preview changes
PYTHONPATH=src python scripts/auto_correct.py --dry-run

# Apply safe corrections (P3/P4 only)
PYTHONPATH=src python scripts/auto_correct.py --apply

# Enrich chemical properties only
PYTHONPATH=src python scripts/auto_correct.py --apply --types chemical_properties

# Add missing synonyms from ontologies
PYTHONPATH=src python scripts/auto_correct.py --apply --types synonyms
```

**Safe corrections (auto-applied):**
- Enrich missing chemical properties from OLS
- Add missing synonyms from ontology
- Normalize CURIE formats
- Fix whitespace/case in labels

**Unsafe corrections (manual review required):**
- Change ontology ID
- Modify preferred term
- Merge duplicate records
- Change mapping quality level

### 4. Claude Code-Assisted Review

**Use case:** Interactive validation with Claude's assistance

```bash
# Use this skill
/review-ingredients

# Or invoke via Skill tool with specific ingredient
/review-ingredients "calcium chloride dihydrate"
```

**Claude will:**
1. Load ingredient record from YAML
2. Run validation via `IngredientReviewer`
3. Explain issues in plain language
4. Propose corrections with rationale
5. Apply fixes if user approves
6. Update curation_history

---

## Validation Rule Catalog

### Priority Levels

| Level | Description | Action Required | Count Target |
|-------|-------------|-----------------|--------------|
| **P1** | Critical errors blocking KG export | Fix immediately | 0 |
| **P2** | High-priority warnings needing review | Manual review | < 5% |
| **P3** | Medium-priority enrichment opportunities | Auto-correct when possible | < 20% |
| **P4** | Low-priority info/suggestions | Optional improvements | Any |

### Rule Definitions

#### P1 - Critical Errors

**Rule P1.1: Ontology Term Existence**
```yaml
id: P1.1
description: Ontology term does not exist (404 from OAK/OLS)
check: OAK lookup returns None for ontology_id
impact: Broken link in knowledge graph
fix: Re-map to correct term or mark unmappable
```

**Rule P1.2: Invalid CURIE Format**
```yaml
id: P1.2
description: Ontology ID not valid CURIE (e.g., "CHEBI:123" vs "CHEBI123")
check: Regex ^[A-Z]+:\d+$
impact: Parser failures in downstream systems
fix: Auto-correct to valid CURIE format
```

**Rule P1.3: Dual Identifier Mismatch**
```yaml
id: P1.3
description: Sequential ID (id field) doesn't match ontology ID (identifier field)
check: For mapped ingredients, identifier should be ontology_id (not UNMAPPED_X)
impact: Confusion between persistent ID and semantic ID
fix: Update identifier field to match ontology_id
```

**Rule P1.4: Missing Required Fields**
```yaml
id: P1.4
description: Required fields missing (ontology_id, preferred_term)
check: Schema validation via LinkML
impact: Invalid YAML structure
fix: Add missing required fields
```

#### P2 - High-Priority Warnings

**Rule P2.1: Label Mismatch**
```yaml
id: P2.1
description: Ontology label differs significantly from preferred_term
check: Normalized string comparison (ontology label vs preferred_term)
threshold: Edit distance > 5 or token overlap < 0.8
impact: Potential incorrect mapping
fix: Manual review - update preferred_term or re-map
```

**Rule P2.2: Definition Mismatch**
```yaml
id: P2.2
description: Ontology definition semantically different from expected
check: LLM-assisted semantic comparison
impact: Conceptual misalignment
fix: Manual review with domain expert
```

**Rule P2.3: Deprecated Term**
```yaml
id: P2.3
description: Ontology term marked as obsolete/deprecated
check: OWL obsolete annotation or OLS deprecated flag
impact: Future-proofing issues
fix: Map to replacement term (check owl:replacedBy)
```

**Rule P2.4: Purity Merge Violation**
```yaml
id: P2.4
description: Pure and impure variants merged incorrectly
check: Cross-reference merge history with purity annotations
impact: Loss of purity information critical for media design
fix: Unmerge and create separate records
```

**Rule P2.5: KG-Microbe Dictionary Disagreement**
```yaml
id: P2.5
description: MIM ontology_id disagrees with kg-microbe's unified chemical dictionary
             for the same preferred_term or synonym
check: |
  For each MIM record, look up preferred_term (and each synonym_text) in
  kg-microbe's unified_chemical_mappings.tsv.gz synonym→chebi_id index.
  Flag if kg-microbe maps the same surface form to a different CHEBI ID.
impact: Cross-repo semantic drift. MIM and kg-microbe knowledge graphs will
        disagree on the same chemical, breaking joins on CHEBI ID at KG ingest.
fix: |
  Both sides must be verified — kg-microbe's dict has known TSV-parse bugs
  producing false synonyms (e.g., merged-row pollution attaching "MnCl2"
  synonym to CHEBI:30200 kaempferol glucoside). Reviewer must:
    1. Lookup MIM's ontology_id via OAK/OLS → get canonical label
    2. Lookup kg-microbe's proposed CHEBI via OAK/OLS → get canonical label
    3. Compare both labels against MIM's preferred_term
    4. Pick the winner; update MIM or log an issue upstream against kg-microbe
severity: P2 (possible wrong mapping, needs expert review)
data_source: |
  /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/
    mappings/unified_chemical_mappings.tsv.gz
  Columns: chebi_id, canonical_name, formula, synonyms (pipe-separated),
           xrefs, sources
  Rows: ~164,597
known_false_positive_patterns:
  - Merged-row pollution: when a synonym field contains embedded quotes,
    csv.DictReader may merge the next row, attaching the following row's
    synonyms to the wrong CHEBI ID.
  - Common-cation contamination: short synonyms like "Na+", "K+", "Cl-"
    appear under many CHEBI IDs and never indicate a real equivalence.
  - Ambiguous ion/salt names: "calcium", "magnesium", "iron" without
    anion qualifier.
```

#### P3 - Medium-Priority Warnings

**Rule P3.1: Missing Chemical Properties**
```yaml
id: P3.1
description: SMILES, InChI, or molecular_formula missing for CHEBI terms
check: chemical_properties section empty
impact: Reduced utility for cheminformatics
fix: Auto-enrich from EBI OLS v4 API
```

**Rule P3.2: Missing Synonyms**
```yaml
id: P3.2
description: Ontology has synonyms not in ingredient record
check: Compare ontology synonyms (exact, related, narrow) with record synonyms
impact: Reduced search/matching capability
fix: Auto-add ontology synonyms with source attribution
```

**Rule P3.3: Low Confidence Mapping**
```yaml
id: P3.3
description: Mapping quality < 0.7 or quality level is PROVISIONAL
check: ontology_mapping.confidence or quality field
impact: Uncertain mappings may need expert review
fix: Manual review or LLM-assisted re-validation
```

**Rule P3.4: Ambiguous Quality Level**
```yaml
id: P3.4
description: CLOSE_MATCH quality without purity/catalog notes in reasoning
check: quality=CLOSE_MATCH and reasoning doesn't mention purity/catalog/hydrate
impact: Unclear why match is "close" not "exact"
fix: Enhance reasoning field with normalization details
```

#### P4 - Low-Priority Info

**Rule P4.1: Additional Synonyms Available**
```yaml
id: P4.1
description: Ontology has many more synonyms than in record
check: Ontology synonym count > record synonym count + 5
impact: Potential enrichment opportunity
fix: Review and selectively add relevant synonyms
```

**Rule P4.2: Alternative Ontology Matches**
```yaml
id: P4.2
description: High-scoring matches in other ontologies
check: OAK multi-source search finds score > 0.8 in different source
impact: Potential better fit in different ontology
fix: Manual review of alternative
```

**Rule P4.3: Enrichment Opportunities**
```yaml
id: P4.3
description: Additional metadata available (cellular roles, pathways)
check: CHEBI has role annotations, pathway links
impact: Enhanced semantic richness
fix: Optionally add role/pathway links
```

**Rule P4.4: KG-Microbe Synonym Enrichment Candidates**
```yaml
id: P4.4
description: kg-microbe's unified chemical dict has synonyms for this record's
             CHEBI ID that MIM does not yet carry
check: |
  For MIM record with ontology_id=CHEBI:X, fetch the row from
  unified_chemical_mappings.tsv.gz keyed by chebi_id=X. The "synonyms"
  column is pipe-separated. Diff against existing MIM synonym_text values
  (case-insensitive, whitespace-normalized).
impact: Search/matching recall in CultureMech recipe mapping — every missing
        synonym is a potential ingredient that won't resolve to this CHEBI.
fix: |
  Candidates are NOT auto-applied. Each candidate must be round-trip
  verified before adding:
    1. Sanity-check: does the synonym plausibly name this chemical?
       (A synonym like "MnCl2" on kaempferol glucoside fails this check.)
    2. Reverse-lookup: in the kg-microbe TSV, does this synonym also map
       to a DIFFERENT CHEBI? If yes, it's ambiguous — skip or investigate.
    3. If accepted, add with source="kg-microbe/unified_chemical_mappings"
       and synonym_type=EXACT or RELATED per kg-microbe's context.
severity: P4 (enrichment, not correctness)
safety: |
  Do NOT treat kg-microbe synonyms as authoritative. The dict was built
  from multiple upstream sources and has documented parsing bugs.
  Every proposal needs human-in-the-loop review before commit.
```

---

## KG-Microbe Dictionary Integration

### Data Source

**File:** `/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/mappings/unified_chemical_mappings.tsv.gz`

**Schema (tab-separated, gzipped):**
| Column | Description |
|---|---|
| `id` (legacy: `chebi_id`) | CURIE, e.g. `CHEBI:17234` |
| `category` | Biolink category (new column, may be absent in older dumps) |
| `canonical_name` | Primary label for the term |
| `formula` | Molecular formula if available |
| `synonyms` | Pipe-separated (`|`) list of surface forms |
| `xrefs` | Cross-references to other databases |
| `sources` | Which upstream dictionaries contributed |

**Row count:** ~119,421 canonical CHEBI entries (as of 2026-04-18);
the raw TSV has more rows but many are duplicates or non-CHEBI IDs.

**Companion curated data:** `kg-microbe/kg_microbe/transform_utils/metatraits/mappings/*.tsv` — 277 hand-curated rows across 6 TSVs, should be consulted for high-confidence overrides.

### Known Data-Quality Issues (must handle defensively)

1. **CSV row-merge bug**: Using `csv.DictReader` on this file merges rows whose
   fields contain embedded quotes. **Always parse line-by-line with
   `split('\t')`** to avoid false synonym→CHEBI associations.

2. **Field size overflow**: Some synonym lists exceed the default csv field
   limit. Set `csv.field_size_limit(sys.maxsize)` as a safeguard even when
   bypassing DictReader.

3. **Symmetric-synonym pollution**: Short cation/anion tokens (`Na+`, `Cl-`,
   `K+`) appear as "synonyms" under hundreds of CHEBI IDs and carry no
   semantic signal.

4. **Stereochemistry collapse**: Some dict entries treat D- and L- forms,
   and (+)/(-) enantiomers, as synonyms — verify with OAK before accepting.

### Loader Pattern (correct)

```python
import csv
import gzip
import sys
from collections import defaultdict
from pathlib import Path

KG_MICROBE_DICT = Path(
    "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/"
    "kg-microbe/mappings/unified_chemical_mappings.tsv.gz"
)

csv.field_size_limit(sys.maxsize)


def load_kg_microbe_dict():
    """
    Build two indexes:
      by_chebi:   CHEBI_ID -> {canonical_name, synonyms: set[str], formula}
      by_synonym: lowercased synonym -> set[CHEBI_ID]  (1:many, intentional)

    Do NOT use csv.DictReader — the file has embedded quotes that cause
    row merging. Parse line-by-line.
    """
    by_chebi = {}
    by_synonym = defaultdict(set)

    with gzip.open(KG_MICROBE_DICT, "rt", encoding="utf-8") as f:
        header = f.readline().rstrip("\n").split("\t")
        col = {name: i for i, name in enumerate(header)}

        for raw in f:
            parts = raw.rstrip("\n").split("\t")
            if len(parts) < len(header):
                continue  # malformed row, skip defensively

            chebi_id = parts[col["chebi_id"]]
            canonical = parts[col["canonical_name"]]
            formula = parts[col["formula"]] if "formula" in col else ""
            syn_field = parts[col["synonyms"]] if "synonyms" in col else ""

            synonyms = {s.strip() for s in syn_field.split("|") if s.strip()}

            by_chebi[chebi_id] = {
                "canonical_name": canonical,
                "synonyms": synonyms,
                "formula": formula,
            }

            for s in synonyms | {canonical}:
                by_synonym[s.lower()].add(chebi_id)

    return by_chebi, by_synonym
```

### Usage in Review Rules

```python
# P2.5 check: does kg-microbe disagree with MIM's mapping?
def check_kg_microbe_disagreement(ingredient, by_synonym, oak_client):
    mim_chebi = ingredient["ontology_mapping"]["ontology_id"]
    if not mim_chebi.startswith("CHEBI:"):
        return None  # P2.5 only applies to CHEBI

    candidates_from_kg = by_synonym.get(ingredient["preferred_term"].lower(), set())
    # Filter ambiguous tokens
    if len(candidates_from_kg) > 5:
        return None  # too ambiguous (Na+, Cl-, etc.)

    disagreements = candidates_from_kg - {mim_chebi}
    if not disagreements:
        return None

    # Round-trip verify both sides via OAK before calling it a disagreement
    mim_label = oak_client.get_term_info(mim_chebi).get("label", "")
    for other in disagreements:
        other_info = oak_client.get_term_info(other)
        if other_info is None:
            continue  # phantom CHEBI, skip
        yield {
            "rule_id": "P2.5",
            "priority": "P2",
            "category": "kg_microbe_disagreement",
            "mim_chebi": mim_chebi,
            "mim_label": mim_label,
            "kg_microbe_chebi": other,
            "kg_microbe_label": other_info.get("label", ""),
            "surface_form": ingredient["preferred_term"],
        }


# P4.4 check: what synonyms does kg-microbe have that MIM lacks?
def find_synonym_enrichment_candidates(ingredient, by_chebi):
    mim_chebi = ingredient["ontology_mapping"]["ontology_id"]
    kg_entry = by_chebi.get(mim_chebi)
    if not kg_entry:
        return []

    existing = {
        s["synonym_text"].lower() if isinstance(s, dict) else str(s).lower()
        for s in ingredient.get("synonyms", [])
    }
    existing.add(ingredient["preferred_term"].lower())

    candidates = [s for s in kg_entry["synonyms"] if s.lower() not in existing]

    # Ambiguity guard: drop any candidate that kg-microbe also maps elsewhere
    # (caller should supply by_synonym to filter)
    return candidates
```

### Reviewing NEW Mappings Sourced From kg-microbe

When a proposal to ADD or REMAP a MIM record originates from a kg-microbe
dict lookup (not just enrich existing), the reviewer MUST:

1. **Verify the CHEBI exists** via OAK (`P1.1` rule, applied preemptively).
2. **Verify the label semantically matches** MIM's preferred_term (`P2.1`).
3. **Check for ambiguity**: if the same surface form maps to ≥2 CHEBI IDs
   in kg-microbe, escalate to manual review even if OAK verification passes.
4. **Log provenance**: the ingredient's `curation_history` entry must cite
   `source: kg-microbe/unified_chemical_mappings` and include the exact
   surface form that triggered the match.
5. **Sanity-check with CultureBotHT CAS-RN** if available — a matching CAS
   number is strong positive evidence that the proposed CHEBI is correct.

Known false-positive incidents to guard against (record these in review
notes when you see the pattern):

- `CHEBI:78018` (dodecylphosphocholine, a detergent) was historically
  imported as `Trypticase`/`Bacto-tryptone` via a CAS→CHEBI pipeline bug.
  Peptones belong in FOODON, not CHEBI.
- `CHEBI:131531` (pyridoxamine HCl) vs `CHEBI:30961` (pyridoxine HCl) —
  the two vitamin B6 hydrochlorides are routinely confused.
- kg-microbe synonym rows polluted by embedded quotes may attach
  e.g. "MnCl2" as a synonym of `CHEBI:30200` (a flavonoid glycoside).

---

## OAK Integration Patterns

### Basic Term Lookup

```python
from mediaingredientmech.utils.ontology_client import OntologyClient

# Initialize OAK client
oak_client = OntologyClient()

# Lookup single term
term_info = oak_client.get_term_info("CHEBI:26710")
if term_info is None:
    print("P1.1 ERROR: Term does not exist")
else:
    print(f"Label: {term_info['label']}")
    print(f"Definition: {term_info.get('definition', 'N/A')}")
    print(f"Deprecated: {term_info.get('deprecated', False)}")
```

### Batch Term Validation

```python
from mediaingredientmech.curation.ingredient_curator import IngredientCurator

curator = IngredientCurator()
oak_client = OntologyClient()

# Load all mapped ingredients
mapped = curator.get_by_status("MAPPED")

missing_terms = []
deprecated_terms = []

for ingredient in mapped:
    ontology_id = ingredient.get('ontology_mapping', {}).get('ontology_id')
    if not ontology_id:
        continue

    term_info = oak_client.get_term_info(ontology_id)

    if term_info is None:
        missing_terms.append(ingredient['preferred_term'])
    elif term_info.get('deprecated'):
        deprecated_terms.append({
            'term': ingredient['preferred_term'],
            'id': ontology_id,
            'replacement': term_info.get('replaced_by')
        })

print(f"P1.1 errors: {len(missing_terms)}")
print(f"P2.3 warnings: {len(deprecated_terms)}")
```

### Synonym Comparison

```python
def compare_synonyms(ingredient_record, ontology_id):
    """Compare ingredient synonyms with ontology synonyms"""
    oak_client = OntologyClient()

    # Get ontology synonyms
    term_info = oak_client.get_term_info(ontology_id)
    if not term_info:
        return {"error": "Term not found"}

    ontology_syns = set(term_info.get('synonyms', []))

    # Get record synonyms (just the text, not metadata)
    record_syns = set()
    for syn in ingredient_record.get('synonyms', []):
        if isinstance(syn, dict):
            record_syns.add(syn.get('text', ''))
        else:
            record_syns.add(syn)

    # Compare
    missing = ontology_syns - record_syns
    extra = record_syns - ontology_syns

    return {
        'ontology_only': list(missing),
        'record_only': list(extra),
        'shared': list(ontology_syns & record_syns)
    }
```

---

## EBI OLS API Integration

### Chemical Properties Enrichment

```python
import requests
from typing import Dict, Optional

def enrich_from_ols(ontology_id: str) -> Optional[Dict]:
    """
    Fetch chemical properties from EBI OLS v4 API

    Returns dict with:
      - molecular_formula
      - smiles
      - inchi
      - inchikey
      - monoisotopic_mass
      - average_mass
    """
    if not ontology_id.startswith("CHEBI:"):
        return None

    chebi_id = ontology_id.replace("CHEBI:", "")
    url = f"https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FCHEBI_{chebi_id}"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()

        # Extract properties from annotation
        annotation = data.get('annotation', {})

        properties = {}

        # Molecular formula
        if 'formula' in annotation:
            properties['molecular_formula'] = annotation['formula'][0]

        # SMILES
        if 'smiles' in annotation:
            properties['smiles'] = annotation['smiles'][0]

        # InChI
        if 'inchi' in annotation:
            properties['inchi'] = annotation['inchi'][0]

        # InChIKey
        if 'inchikey' in annotation:
            properties['inchikey'] = annotation['inchikey'][0]

        # Masses
        if 'monoisotopicMass' in annotation:
            properties['monoisotopic_mass'] = float(annotation['monoisotopicMass'][0])

        if 'averageMass' in annotation:
            properties['average_mass'] = float(annotation['averageMass'][0])

        return properties if properties else None

    except Exception as e:
        print(f"OLS fetch failed for {ontology_id}: {e}")
        return None
```

### Batch Enrichment with Rate Limiting

```python
import time
from typing import List, Dict

def batch_enrich_ols(ingredient_records: List[Dict],
                      batch_size: int = 50,
                      delay: float = 0.5) -> Dict[str, Dict]:
    """
    Batch enrich ingredients from OLS with rate limiting

    Args:
        ingredient_records: List of ingredient dicts
        batch_size: Process this many before checkpoint
        delay: Seconds to wait between requests

    Returns:
        Dict mapping ontology_id to enriched properties
    """
    enriched = {}

    chebi_records = [
        r for r in ingredient_records
        if r.get('ontology_mapping', {}).get('ontology_id', '').startswith('CHEBI:')
    ]

    print(f"Enriching {len(chebi_records)} CHEBI-mapped ingredients...")

    for i, record in enumerate(chebi_records):
        ontology_id = record['ontology_mapping']['ontology_id']

        properties = enrich_from_ols(ontology_id)
        if properties:
            enriched[ontology_id] = properties

        # Rate limiting
        time.sleep(delay)

        # Progress update
        if (i + 1) % batch_size == 0:
            print(f"Progress: {i + 1}/{len(chebi_records)}")

    print(f"Successfully enriched {len(enriched)}/{len(chebi_records)} records")
    return enriched
```

---

## OWL File Management

### Download Strategy

**OBO Foundry URLs:**
- CHEBI: `http://purl.obolibrary.org/obo/chebi.owl`
- FOODON: `http://purl.obolibrary.org/obo/foodon.owl`
- ENVO: `http://purl.obolibrary.org/obo/envo.owl`

**Cache Location:** `ontology/cache/`

**Manifest Format (`manifest.json`):**
```json
{
  "chebi": {
    "url": "http://purl.obolibrary.org/obo/chebi.owl",
    "downloaded": "2026-03-15T10:30:00Z",
    "version": "v2024-03-01",
    "md5": "abc123...",
    "size_mb": 245.3
  },
  "foodon": {
    "url": "http://purl.obolibrary.org/obo/foodon.owl",
    "downloaded": "2026-03-15T10:35:00Z",
    "version": "v2024-02-15",
    "md5": "def456...",
    "size_mb": 89.7
  },
  "envo": {
    "url": "http://purl.obolibrary.org/obo/envo.owl",
    "downloaded": "2026-03-15T10:40:00Z",
    "version": "v2024-03-10",
    "md5": "ghi789...",
    "size_mb": 34.2
  }
}
```

### Download Script Usage

```bash
# Check current cache status
python scripts/download_ontologies.py --check-only

# Download specific ontologies
python scripts/download_ontologies.py --sources CHEBI FOODON

# Download all supported ontologies
python scripts/download_ontologies.py --all

# Force re-download (ignore cache)
python scripts/download_ontologies.py --force --sources CHEBI

# Verify integrity
python scripts/download_ontologies.py --verify
```

### OWL Reasoning Examples

```python
from oaklib import get_adapter

# Load local OWL file
adapter = get_adapter("sqlite:obo:chebi.owl")

# Check if term is obsolete
term_id = "CHEBI:26710"
obsolete = adapter.is_obsolete(term_id)

# Get replacement term
if obsolete:
    replacements = adapter.get_term_replaced_by(term_id)
    print(f"Use {replacements[0]} instead")

# Get all subclasses (descendants)
descendants = list(adapter.descendants(term_id))

# Get parent classes
ancestors = list(adapter.ancestors(term_id))
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

## Best Practices

### DO ✅

1. **Run batch validation before KG export**
   - Ensures no P1 errors propagate to knowledge graph
   - Generates audit trail for downstream consumers

2. **Use auto-correct for P3/P4 only**
   - Chemical properties enrichment is safe (read-only OLS data)
   - Synonym addition from ontologies is low-risk
   - Always review P1/P2 manually

3. **Cache OWL files locally**
   - Faster validation (no network calls)
   - Enables offline work
   - Version control for reproducibility

4. **Track validation history**
   - Add validation events to curation_history
   - Record which rules passed/failed over time
   - Monitor quality trends

5. **Batch process with checkpoints**
   - Resume on failure without re-processing
   - Parallel processing for speed (4-8 threads)
   - Rate-limit API calls (0.5-1s delay)

6. **Verify corrections before applying**
   - Use `--dry-run` first
   - Review JSON correction plan
   - Test on small subset

### DON'T ❌

1. **Don't auto-correct P1/P2 issues**
   - Label mismatches may indicate incorrect mapping
   - Deprecated terms need manual replacement review
   - Dual identifier issues may have complex causes

2. **Don't skip validation for "trusted" sources**
   - CultureMech imports still need validation
   - Expert curations can have typos
   - Ontologies evolve (terms deprecated)

3. **Don't over-enrich**
   - Only add synonyms that improve search
   - Avoid cluttering records with rarely-used synonyms
   - Focus on common chemical names, not IUPAC variants

4. **Don't ignore P2 warnings**
   - Label mismatches often indicate semantic issues
   - Purity merge violations corrupt data integrity
   - Deprecated terms will break in future

5. **Don't run full batch without sampling**
   - Test on 10-20 ingredients first
   - Verify output format is as expected
   - Check performance (runtime, memory)

6. **Don't hardcode API endpoints**
   - Use config file for URLs
   - Support fallback endpoints
   - Handle API version changes gracefully

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

---

## Conclusion

The **Review Ingredients** skill provides comprehensive quality assurance for MediaIngredientMech's ontology mappings. By integrating OAK, OLS, OWL reasoning, and domain-specific rules, it ensures:

- **Zero critical errors** (P1) before KG export
- **High-quality mappings** with validated labels and definitions
- **Enriched metadata** (SMILES, InChI, synonyms) for all CHEBI terms
- **Consistent purity tracking** via merge integrity checks
- **Automated corrections** for safe issues (P3/P4)
- **Audit trail** via validation reports and curation history

**Next Steps:**
1. Implement core validation class (`ingredient_reviewer.py`)
2. Create supporting scripts (7 total)
3. Run full batch validation on 1,034 mapped ingredients
4. Fix any P1 critical errors
5. Auto-enrich P3/P4 issues
6. Integrate into ongoing curation workflow

**Estimated Impact:**
- **Time saved**: 80% reduction in manual QA (automated validation)
- **Error prevention**: 100% P1 error detection before export
- **Data enrichment**: 95%+ CHEBI terms with chemical properties
- **Synonym coverage**: 50% increase in average synonyms per ingredient

This skill transforms validation from manual spot-checking to systematic, automated quality assurance across the entire dataset.
