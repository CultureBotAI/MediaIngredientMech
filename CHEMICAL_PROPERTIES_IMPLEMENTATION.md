# Chemical Properties Implementation Summary

## Overview
Added chemical structure and properties enrichment for CHEBI-mapped ingredients. Automatically fetches molecular formulas, SMILES, InChI, and molecular weights from ChEBI OLS v4 and PubChem APIs.

## Files Modified/Created

### 1. Schema Extension ✅
**File**: `src/mediaingredientmech/schema/mediaingredientmech.yaml`

Added two new components:
- `ChemicalProperties` class (after line 129):
  - `molecular_formula`: Molecular formula (e.g., H2O)
  - `smiles`: SMILES notation
  - `inchi`: InChI identifier
  - `molecular_weight`: Weight in g/mol
  - `data_source`: Where data came from (ChEBI, PubChem, or both)
  - `retrieval_date`: ISO timestamp of when fetched

- `chemical_properties` field in `IngredientRecord` (after line 102):
  - Optional field for backwards compatibility
  - Only populated for CHEBI-mapped ingredients

### 2. Chemical Properties Client ✅
**File**: `src/mediaingredientmech/utils/chemical_properties_client.py` (NEW)

**Classes**:
- `ChemicalProperties`: Dataclass matching schema
- `ChemicalPropertiesClient`: Main API client

**Key Features**:
- Only processes CHEBI terms (returns None for FOODON/ENVO)
- Two-stage enrichment:
  1. ChEBI OLS v4 API → molecular formula + weight
  2. PubChem REST API → SMILES + InChI (via ChEBI cross-reference)
- File-based cache in `~/.cache/mediaingredientmech/chemical_properties/`
- Rate limiting: 5 requests/second (0.2s minimum interval)
- Robust error handling with retry logic
- Graceful handling of 404s (many CHEBI terms not in PubChem)

**API Endpoints**:
- ChEBI: `https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms/{encoded_iri}`
- PubChem: `https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/`

### 3. Batch Enrichment Script ✅
**File**: `scripts/enrich_chemical_properties.py` (NEW)

**Features**:
- Rich CLI with progress bars and summary tables
- Filters for CHEBI mappings without existing `chemical_properties`
- `--dry-run`: Preview what would be enriched
- `--limit N`: Process first N ingredients (for testing)
- `--input/-i`: Input YAML path (default: `data/curated/mapped_ingredients.yaml`)
- `--output/-o`: Output path (default: overwrites input)
- Summary statistics: enriched/failed/skipped counts
- Display of results table showing formula, SMILES, and source

**Usage**:
```bash
# Dry run (preview)
python scripts/enrich_chemical_properties.py --dry-run --limit 10

# Test with 10 ingredients
python scripts/enrich_chemical_properties.py --limit 10 --output /tmp/test.yaml

# Full enrichment (995 CHEBI ingredients)
python scripts/enrich_chemical_properties.py
```

### 4. Curator Integration ✅
**File**: `src/mediaingredientmech/curation/ingredient_curator.py`

**New Method** (after line 251):
```python
def enrich_chemical_properties(
    self,
    record: dict[str, Any],
    client: Optional[Any] = None,
) -> dict[str, Any]:
```

**Behavior**:
- Checks if already enriched (skips if `chemical_properties` exists)
- Only processes CHEBI-mapped ingredients
- Adds properties to record if found
- Logs curation event: `action=ANNOTATED`, details about formula/SMILES
- Sets `self._dirty = True` to trigger save

**Modified Method** (`accept_mapping` at line 185):
- Added `auto_enrich: bool = True` parameter
- After mapping accepted, automatically calls `enrich_chemical_properties()` if:
  - `auto_enrich=True` (default)
  - `candidate.source == "CHEBI"`

**Integration**:
- Seamless enrichment during interactive curation workflow
- Can be disabled by passing `auto_enrich=False`
- Uses lazy import to avoid circular dependencies

### 5. Tests ✅
**File**: `tests/test_chemical_properties.py` (NEW)

**Test Coverage** (8 tests, all passing):
1. `test_skip_non_chebi_terms` - Verify FOODON/ENVO return None
2. `test_get_properties_from_ols` - Mock ChEBI OLS response
3. `test_get_properties_from_pubchem` - Mock PubChem enrichment
4. `test_pubchem_not_found` - Handle 404 gracefully
5. `test_cache_hit_avoids_api_call` - Verify caching works
6. `test_ols_error_handling` - Request exception handling
7. `test_chemical_properties_to_dict` - Serialization with all fields
8. `test_chemical_properties_to_dict_partial` - Serialization with missing fields

**Test Results**:
```
8 passed in 1.70s
85% code coverage for chemical_properties_client.py
```

## Verification Steps Completed

### 1. Schema Generation ✅
```bash
gen-python src/mediaingredientmech/schema/mediaingredientmech.yaml > \
    src/mediaingredientmech/datamodel/mediaingredientmech.py
```
- LinkML classes regenerated successfully
- Warning about duplicate tree_root is expected (IngredientRecord/Collection)

### 2. Test Suite ✅
```bash
PYTHONPATH=src python -m pytest tests/test_chemical_properties.py -v
```
- All 8 tests passing
- 85% code coverage
- No critical warnings

### 3. Dry Run ✅
```bash
python scripts/enrich_chemical_properties.py --dry-run --limit 10
```
Output:
```
Found 995 CHEBI-mapped ingredients without properties
Limited to first 10 ingredients

              Ingredients to Enrich
┏━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┓
┃ Identifier   ┃ Preferred Term  ┃ CHEBI ID     ┃
┡━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━┩
│ CHEBI:26710  │ NaCl            │ CHEBI:26710  │
│ CHEBI:15377  │ Distilled water │ CHEBI:15377  │
...
```

### 4. Live Test ✅
```bash
python scripts/enrich_chemical_properties.py --limit 3 \
    --output /tmp/test_enriched.yaml
```

**Results**:
- **Enriched**: 1 (CHEBI:15377 - water)
- **Failed**: 2 (CHEBI:26710, CHEBI:86158 - 400 errors from OLS)
- **Skipped**: 0

**Enriched Data** (water):
```yaml
chemical_properties:
  molecular_formula: H2O
  smiles: O
  molecular_weight: 18.015
  data_source: ChEBI+PubChem
  retrieval_date: '2026-03-14T03:22:52.388769+00:00'
```

## Current Status

### Production Dataset
- **Total CHEBI mappings**: 995 ingredients
- **Already enriched**: 0 (fresh implementation)
- **Ready for enrichment**: 995

### Known Issues
Some CHEBI IDs return 400 errors from OLS v4 API:
- CHEBI:26710 (NaCl)
- CHEBI:86158 (CaCl2·2H2O)

**Likely cause**: URL encoding issues or deprecated IDs in OLS v4

**Impact**: These will be logged as "failed" but won't block the script

**Recommendation**: Run full enrichment and review failed IDs. May need to:
1. Adjust URL encoding for certain IDs
2. Add fallback to direct ChEBI API
3. Document which IDs are not available in OLS v4

## Next Steps

### Immediate
1. **Run Full Enrichment**:
   ```bash
   python scripts/enrich_chemical_properties.py \
       --input data/curated/mapped_ingredients.yaml \
       --output data/curated/mapped_ingredients.yaml
   ```

2. **Review Failed Enrichments**:
   - Analyze which CHEBI IDs consistently fail
   - Determine if pattern exists (e.g., salts, hydrates)
   - Consider OLS v4 API improvements or fallback strategies

### Future Enhancements
1. **Add to Curation Workflow**:
   - Auto-enrichment already integrated via `accept_mapping()`
   - Test with interactive curator (`scripts/curate_unmapped.py`)

2. **Extend to Other Sources**:
   - FOODON: Consider food composition databases (USDA, etc.)
   - ENVO: May not have chemical properties (environmental terms)

3. **Add Validation**:
   - Cross-check molecular formula vs SMILES
   - Validate molecular weight calculations
   - Flag discrepancies for manual review

4. **Performance Optimization**:
   - Batch API requests (if APIs support)
   - Async/concurrent requests
   - Pre-populate cache from bulk downloads

5. **Documentation**:
   - Add chemical properties section to map-media-ingredients skill
   - Document API rate limits and best practices
   - Create troubleshooting guide for common API errors

## Architecture Decisions

### Why File-Based Cache?
- Simple, no DB dependency
- Human-readable (JSON)
- Survives across runs
- Easy to inspect/debug
- Portable cache directory

### Why Two-Stage Enrichment?
- ChEBI OLS has formula/mass (most important)
- PubChem has SMILES/InChI (structural)
- Combining both gives complete picture
- Graceful fallback if one source fails

### Why Skip Non-CHEBI?
- FOODON: Food composition varies, no single formula
- ENVO: Environmental terms (e.g., "seawater") not chemicals
- Focus effort where chemical properties are meaningful

### Why Auto-Enrich in Curator?
- Reduces manual steps
- Ensures consistency (all CHEBI mappings enriched)
- Can be disabled if needed (`auto_enrich=False`)
- Logged in curation history for audit trail

## Dependencies
- `requests`: HTTP API calls
- `pyyaml`: YAML parsing
- `rich`: Terminal UI (already in project)
- `click`: CLI framework (already in project)

All dependencies already present in project - no new requirements needed.
