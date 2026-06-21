# Related Tools, Documentation & Implementation API

*Reference for the **map-media-ingredients** skill — see [`../skill.md`](../skill.md) for the overview, normalization rules, strategy levels, and workflows.*

---

## Related Tools and Documentation

### Curation Scripts

- `scripts/analyze_unmapped.py` - Categorize and prioritize ingredients
- `scripts/batch_curate_unmapped.py` - Batch workflow for simple chemicals
- `scripts/curate_unmapped.py` - Interactive single-ingredient curation
- `scripts/prepare_for_claude_curation.py` - Prepare batches for Claude Code
- `scripts/apply_claude_suggestions.py` - Apply Claude Code suggestions
- `scripts/import_from_culturemech.py` - Import from CultureMech
- `scripts/export_to_culturemech.py` - Export to CultureMech

### Core Utilities

- `src/mediaingredientmech/utils/chemical_normalizer.py` - Normalization logic
- `src/mediaingredientmech/utils/ontology_client.py` - OAK integration
- `src/mediaingredientmech/utils/curator.py` - Curation state management

### Documentation

- `docs/UNMAPPED_CURATION.md` - General curation guide
- `docs/CLAUDE_CODE_CURATION.md` - Claude Code workflow guide
- `README.md` - Project overview and setup

### Related Skills

- `search-ingredients-hierarchical.md` (MicroGrowAgents) - Hierarchical ingredient search patterns
- `ingredient-roles` (MIM) - Functional role assignment for mapped ingredients

---

## Implementation References

### Chemical Normalizer

```python
# Core normalization function
from mediaingredientmech.utils.chemical_normalizer import normalize_chemical_name

result = normalize_chemical_name("MgSO4•7H2O")
# Returns: NormalizationResult with original, normalized, variants, applied_rules

# Generate comprehensive search variants
from mediaingredientmech.utils.chemical_normalizer import generate_search_variants

variants = generate_search_variants("CaCl2·2H2O")
# Returns: ['CaCl2·2H2O', 'CaCl2', 'calcium chloride', 'calcium chloride dihydrate']
```

### Ontology Client

```python
from mediaingredientmech.utils.ontology_client import OntologyClient

client = OntologyClient()

# Simple search
results = client.search("glucose", sources=["CHEBI"])

# Multi-variant search with deduplication
variants = ["magnesium sulfate", "MgSO4", "magnesium sulphate"]
results = client.search_with_variants(variants, sources=["CHEBI"], max_results=10)

# Validate term exists
exists = client.validate_term("CHEBI:32599")
```

### Curator

```python
from mediaingredientmech.utils.curator import UnmappedCurator

curator = UnmappedCurator("data/ingredients/unmapped")

# Accept mapping
curator.accept_mapping(
    ingredient_name="MgSO4•7H2O",
    ontology_id="CHEBI:32599",
    ontology_label="magnesium sulfate",
    ontology_source="CHEBI",
    quality="EXACT_MATCH"
)

# Mark as needs expert review
curator.mark_needs_expert(
    ingredient_name="Vitamin solution A",
    notes="Composition not specified"
)
```
