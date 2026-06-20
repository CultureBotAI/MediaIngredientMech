# External Tool Integrations (KG-Microbe dict · OAK · OLS · OWL)

*Reference for the **review-ingredients** skill — see [`../skill.md`](../skill.md) for the overview, workflows, and rule summary.*

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
