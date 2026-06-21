# Matching Strategies — Detailed Code (OAK · OntologyClient · normalizer · OLS)

*Reference for the **map-media-ingredients** skill — see [`../skill.md`](../skill.md) for the overview, normalization rules, strategy levels, and workflows.*

---

## Matching Strategies

### Level 1: Exact Match

Direct string match with ontology labels (case-insensitive).

**Using OAK** (Ontology Access Kit):
```python
from oaklib import get_adapter

# Search CHEBI
adapter = get_adapter("sqlite:obo:chebi")
results = adapter.basic_search("sodium chloride")

for entity_id in results:
    label = adapter.label(entity_id)
    print(f"{entity_id}: {label}")
# Output: CHEBI:26710: sodium chloride
```

**Using OntologyClient**:
```python
from mediaingredientmech.utils.ontology_client import OntologyClient

client = OntologyClient()
results = client.search("glucose", sources=["CHEBI"])

for candidate in results:
    print(f"{candidate.ontology_id}: {candidate.label} (score: {candidate.score})")
```

### Level 2: Normalized Match

Apply chemical normalization, then search with all variants.

**Using chemical_normalizer**:
```python
from mediaingredientmech.utils.chemical_normalizer import (
    normalize_chemical_name,
    generate_search_variants
)

# Normalize
result = normalize_chemical_name("MgSO4•7H2O")
print(f"Original: {result.original}")
print(f"Normalized: {result.normalized}")
print(f"Variants: {result.variants}")
# Variants: ['magnesium sulfate', 'MgSO4', 'magnesium sulphate']

# Search with all variants
client = OntologyClient()
matches = client.search_with_variants(result.variants, sources=["CHEBI"])
```

**Multi-variant search** (deduplicates results, keeps best scores):
```python
# Generate comprehensive search variants
variants = generate_search_variants("MgSO4•7H2O")
# Returns: ['MgSO4•7H2O', 'MgSO4', 'magnesium sulfate', 'magnesium sulphate']

# Search with all variants, deduplicate results
results = client.search_with_variants(variants, sources=["CHEBI"], max_results=10)
```

### Level 3: Fuzzy Match

Use fuzzy/lexical search for synonym matching and spelling variations.

**Using OAK fuzzy search**:
```bash
# Lexical search (prefix: l~)
uv run runoak -i sqlite:obo:chebi info "l~magnesium sulphate"

# Search with synonyms
uv run runoak -i sqlite:obo:chebi search "magnesium sulfate"
```

**Using EBI OLS API** (web-based, requires internet):
```bash
# Basic search
curl "https://www.ebi.ac.uk/ols4/api/search?q=magnesium%20sulfate&ontology=chebi"

# Python wrapper
import requests

def ols_search(query, ontology="chebi"):
    url = "https://www.ebi.ac.uk/ols4/api/search"
    params = {"q": query, "ontology": ontology}
    response = requests.get(url, params=params)
    return response.json()

results = ols_search("magnesium sulfate", "chebi")
for doc in results['response']['docs']:
    print(f"{doc['obo_id']}: {doc['label']}")
```

**When to use OLS vs OAK**:
- **OAK** (primary): Faster, works offline, integrated with curation scripts
- **OLS** (secondary): Cross-validation, broader coverage, web-based exploration

### Level 4: Manual Curation

When automated matching fails, manual expert curation is required.

**Use manual curation when**:
- Complex mixtures ("Vitamin solution A", "Trace metal mix")
- Generic/incomplete terms ("See source", "Mineral salts")
- Ambiguous names requiring context
- Novel/proprietary formulations
