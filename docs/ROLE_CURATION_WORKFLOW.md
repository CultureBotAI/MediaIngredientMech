# Role Curation Workflow

## Overview

This document describes the workflow for curating media ingredient role assignments in MediaIngredientMech. Role curation assigns functional roles (e.g., CARBON_SOURCE, BUFFER, MINERAL) to ingredients based on evidence from CultureMech database annotations and scientific literature.

**Current Status** (as of 2026-03-15):
- **446 ingredients with roles** (44.8% coverage of 996 mapped ingredients)
- **448 total role assignments** (1.0 average per ingredient)
- **Average confidence: 0.998** (extremely high quality)
- **99.8% citation coverage** (447/448 roles have structured evidence)

## Philosophy

### Evidence-Based Assignment

Role curation in MediaIngredientMech follows an **evidence-first** approach:

1. **CultureMech Baseline**: Primary evidence comes from 8,644+ media formulations in CultureMech database
2. **Occurrence-Weighted Confidence**: High-occurrence roles (500+ media) receive higher confidence scores
3. **Property-Based Scoring**: "Defined component" vs "Undefined component" metadata informs confidence
4. **Structured Citations**: All roles include DATABASE_ENTRY citations with occurrence statistics and property excerpts

### Quality Over Quantity

Rather than auto-assigning roles to all 996 ingredients, we prioritize:
- **High-occurrence ingredients first** (top 100 by media usage)
- **Clear, unambiguous roles** (MINERAL, BUFFER) over complex metabolic functions
- **Structured evidence** with occurrence counts and property metadata
- **Manual review** for edge cases and conflicting roles

## Data Sources

### 1. CultureMech Database (Primary)

**Source**: 8,644+ media formulations from global culture collections
**Coverage**: 570 ingredients with role annotations
**Format**: Embedded in synonym text as `"Role: [role_text]; Properties: [properties]"`

**Example**:
```
Role: Mineral source; Properties: Defined component, Inorganic compound, Simple component
```

**Mapping**:
- CultureMech role text (e.g., "Mineral source") → IngredientRoleEnum value (e.g., `MINERAL`)
- See `scripts/analyze_culturemech_roles.py::CULTUREMECH_ROLE_MAPPING` for full mapping table

**Confidence Scoring Rules**:
- "Defined component" + occurrence >500 → **1.0**
- "Defined component" + occurrence 100-500 → **0.95**
- "Defined component" + occurrence <100 → **0.9**
- "Undefined component" → **0.8**

### 2. DOI Literature Review (Future)

**Status**: Infrastructure built (`src/mediaingredientmech/utils/doi_resolver.py`), manual review deferred
**Purpose**: High-priority roles requiring publication-level evidence
**Workflow**: DOI resolution → APA citation generation → RoleCitation format

**When to Use**:
- Novel or unexpected role assignments
- Conflicting evidence between sources
- Roles requiring biochemical/metabolic context

## Role Assignment Schema

### IngredientRoleEnum (18 values)

**Core Nutritional Roles**:
- `CARBON_SOURCE` - Organic carbon for biosynthesis/energy
- `NITROGEN_SOURCE` - Nitrogen for amino acids/nucleotides
- `MINERAL` - Inorganic minerals (phosphate, sulfate, magnesium)
- `TRACE_ELEMENT` - Micronutrients (iron, zinc, cobalt)
- `VITAMIN_SOURCE` - Vitamins or vitamin precursors
- `PROTEIN_SOURCE` - Peptides, proteins, amino acids
- `AMINO_ACID_SOURCE` - Specific amino acids

**Physicochemical Roles**:
- `BUFFER` - pH buffering agents
- `SALT` - Ionic strength and osmotic balance
- `SOLIDIFYING_AGENT` - Gelling agents (agar)

**Metabolic Roles**:
- `ENERGY_SOURCE` - Primary energy substrate
- `ELECTRON_ACCEPTOR` - Terminal electron acceptor (nitrate, oxygen)
- `ELECTRON_DONOR` - Electron donor for chemolithotrophs
- `COFACTOR_PROVIDER` - Enzyme cofactors/prosthetic groups

**Indicator Roles** (added 2026-03-15):
- `REDOX_INDICATOR` - pH-dependent redox indicators (resazurin)
- `PH_INDICATOR` - pH indicator dyes
- `SELECTIVE_AGENT` - Antimicrobial/selective agents
- `SURFACTANT` - Surfactants/detergents

### RoleAssignment Structure

```yaml
media_roles:
  - role: MINERAL
    confidence: 1.0
    evidence:
      - reference_type: DATABASE_ENTRY
        reference_text: "CultureMech database (6041 occurrences as 'Mineral source')"
        url: "https://github.com/CultureBotAI/CultureMech"
        excerpt: "Role: Mineral source; Properties: Defined component, Inorganic compound, Simple component"
        curator_note: "Widespread use in media formulations (6041 occurrences). High confidence based on 'Defined component' property."
```

**Fields**:
- `role`: IngredientRoleEnum value (required)
- `confidence`: Float 0.0-1.0 (required)
- `evidence`: List of RoleCitation objects (required for quality)
  - `reference_type`: PUBLICATION, DATABASE_ENTRY, EXPERT_ANNOTATION
  - `reference_text`: Citation text with occurrence stats
  - `url`: Link to source
  - `excerpt`: Direct quote from source (role + properties)
  - `curator_note`: Contextual notes about assignment

## Multi-Role Handling

### Independent Confidence Scores

Each role is assigned **independently** with its own confidence score:

**Example: Distilled Water**
```yaml
media_roles:
  - role: MINERAL
    confidence: 1.0
    evidence: [...CultureMech 4105 occurrences as "Mineral source"...]
  - role: SALT  # Solvating media
    confidence: 1.0
    evidence: [...CultureMech 4105 occurrences as "Solvating media"...]
```

### Potentially Conflicting Roles

Some role combinations require additional context:
- **CARBON_SOURCE + ELECTRON_ACCEPTOR**: Rare, but valid for compounds like fumarate
- **BUFFER + SELECTIVE_AGENT**: Requires pH context (e.g., acidic pH inhibits some organisms)

**Validation**: `scripts/validate_roles.py` flags these for manual review

## Workflows

### Workflow 1: CultureMech Analysis (Completed)

**Purpose**: Extract and analyze role data from CultureMech synonyms

**Steps**:
1. Run `scripts/analyze_culturemech_roles.py`:
   - Parses 996 ingredient records for role annotations
   - Generates role distribution CSV
   - Creates top 100 cross-reference with confidence scores
   - Output: `data/analysis/top100_role_crossref.yaml`

2. Review unmapped role texts:
   - Example: "Growth factor" (60 occurrences) - needs mapping decision
   - Update `CULTUREMECH_ROLE_MAPPING` if new enum values warranted

**Outputs**:
- `data/analysis/culturemech_role_distribution.csv` - Role frequency table
- `data/analysis/top100_role_crossref.yaml` - Top 100 ingredient cross-reference

### Workflow 2: Top 100 Role Extraction (Completed)

**Purpose**: Add roles for highest-occurrence ingredients

**Steps**:
1. Dry-run preview:
   ```bash
   PYTHONPATH=src python scripts/extract_top100_roles.py --dry-run
   ```

2. Execute extraction:
   ```bash
   PYTHONPATH=src python scripts/extract_top100_roles.py
   ```

3. Review curation history:
   - Check `data/curated/mapped_ingredients.yaml` for new role assignments
   - Verify confidence scores and citations

**Features**:
- **Deduplication**: Skips roles already present
- **Structured citations**: Includes occurrence counts and property metadata
- **Audit trail**: All changes logged in `curation_history`

### Workflow 3: Citation Enrichment (Completed)

**Purpose**: Upgrade minimal citations with structured CultureMech metadata

**Steps**:
1. Identify generic citations:
   - Pattern: "Imported from CultureMech pipeline" (no occurrence stats)
   - 82 roles upgraded in top 100

2. Run enrichment:
   ```bash
   PYTHONPATH=src python scripts/enrich_existing_roles.py
   ```

3. Validate improvements:
   - Check upgraded citations include occurrence counts
   - Verify property excerpts present

**Before**:
```yaml
evidence:
  - reference_text: "Imported from CultureMech pipeline"
    reference_type: DATABASE_ENTRY
```

**After**:
```yaml
evidence:
  - reference_text: "CultureMech database (1307 occurrences as 'pH dependent redox indicator')"
    reference_type: DATABASE_ENTRY
    url: "https://github.com/CultureBotAI/CultureMech"
    excerpt: "Role: pH dependent redox indicator; Properties: Defined component, Organic compound, Simple component"
    curator_note: "Widespread use in anaerobic media formulations (1307 occurrences). High confidence based on 'Defined component' property."
```

### Workflow 4: Validation and Statistics (Ongoing)

**Purpose**: Quality assurance and progress tracking

**Steps**:
1. Run validation:
   ```bash
   PYTHONPATH=src python scripts/validate_roles.py
   ```

   **Checks**:
   - Enum validity (all roles in `VALID_MEDIA_ROLES`)
   - Citation coverage (all roles have evidence)
   - Confidence consistency (aligns with properties)
   - Multi-role coherence (no unexpected conflicts)

2. Generate statistics:
   ```bash
   PYTHONPATH=src python scripts/generate_role_statistics.py
   ```

   **Outputs**: `data/analysis/role_statistics_report.yaml`
   - Summary metrics (coverage, confidence, citation types)
   - Role distribution histogram
   - Top 20 ingredients by occurrence
   - Confidence score distribution

3. Review validation errors:
   - Example: "Water (base)" has invalid role `SOLVENT` (not in enum)
   - Action: Add to enum or change to `SALT`

## Quality Assurance

### Citation Standards

**Minimum Requirements**:
- ✅ `reference_type` specified (DATABASE_ENTRY, PUBLICATION, etc.)
- ✅ `reference_text` with occurrence stats or publication details
- ✅ `url` to source (GitHub, DOI link)
- ✅ `excerpt` with direct quote from source
- ✅ `curator_note` with context (high occurrence, property-based confidence)

**RED FLAGS**:
- ❌ Empty `reference_text`
- ❌ Generic citations without metadata ("Imported from...")
- ❌ Missing occurrence counts for DATABASE_ENTRY
- ❌ Confidence >0.95 without "Defined component" property

### Validation Checklist

Before committing role changes, run:

```bash
# 1. Validate all role assignments
PYTHONPATH=src python scripts/validate_roles.py

# 2. Generate updated statistics
PYTHONPATH=src python scripts/generate_role_statistics.py

# 3. Review outputs
cat data/analysis/role_statistics_report.yaml

# 4. Check for errors in validation
# - 0 errors: ✅ Proceed
# - Warnings only: ⚠️ Review and decide
# - Errors present: ❌ Fix before commit
```

### Confidence Score Calibration

**High Confidence (0.95-1.0)**:
- "Defined component" in properties
- Occurrence >100 media
- Single, unambiguous role

**Medium Confidence (0.8-0.94)**:
- "Undefined component" or missing properties
- Occurrence <100 media
- Multi-role ingredient with context

**Low Confidence (<0.8)**:
- Provisional assignment pending expert review
- Conflicting evidence from sources
- Novel/unexpected role

## Future Enhancements (Phase 5)

### Remaining 896 Ingredients

**Target**: Achieve >80% coverage (800+ ingredients with roles)

**Approach**:
1. Extend analysis to all 570 ingredients with CultureMech annotations
2. Focus on occurrence >50 media first
3. Manual review for <50 occurrence ingredients

### DOI Literature Review

**High-Priority Roles**:
- ELECTRON_ACCEPTOR/DONOR - requires metabolic context
- COFACTOR_PROVIDER - needs biochemical evidence
- SELECTIVE_AGENT - antimicrobial spectrum details

**Workflow**:
1. Identify ingredients needing DOI citations
2. Search PubMed/CrossRef for relevant publications
3. Use `doi_resolver.py` to fetch metadata
4. Add PUBLICATION citations alongside DATABASE_ENTRY

### Interactive Curation UI

**Features**:
- Web-based role assignment interface
- Side-by-side evidence comparison (CultureMech vs PubMed)
- Batch approval for high-confidence assignments
- Export to KGX format for KG-Microbe integration

### ChEBI Role Cross-Reference

**Goal**: Import biochemical roles from ChEBI ontology

**Example**: CHEBI:15377 (water) has role "solvent" in ChEBI
**Action**: Map ChEBI roles to IngredientRoleEnum, auto-populate where confident

## Troubleshooting

### Issue: Validation Error - Invalid Role Enum

**Symptom**: `Invalid media role at index 0: SOLVENT`

**Cause**: Role value not in `VALID_MEDIA_ROLES` set

**Fix**:
1. Check if role should be added to enum (`src/mediaingredientmech/schema/mediaingredientmech.yaml`)
2. Update `VALID_MEDIA_ROLES` in `src/mediaingredientmech/curation/ingredient_curator.py`
3. Or change role value to existing enum (e.g., SOLVENT → SALT)

### Issue: Low Citation Coverage

**Symptom**: "Roles with citations: 250/500 (50%)"

**Cause**: Missing evidence entries in role assignments

**Fix**:
1. Run `scripts/enrich_existing_roles.py` to upgrade generic citations
2. For remaining gaps, add manual citations using `curator.add_media_role()`

### Issue: Confidence Inconsistency

**Symptom**: Warning about "Defined component" with low confidence

**Cause**: Manual override or incorrect property parsing

**Fix**:
1. Check cross-reference data for ingredient
2. Verify occurrence count and properties
3. Recalculate confidence using rules in "Data Sources" section

## File Locations

**Scripts**:
- `scripts/analyze_culturemech_roles.py` - CultureMech data extraction
- `scripts/extract_top100_roles.py` - Top 100 role assignment
- `scripts/enrich_existing_roles.py` - Citation enrichment
- `scripts/validate_roles.py` - Validation checks
- `scripts/generate_role_statistics.py` - Statistics reporting

**Data**:
- `data/curated/mapped_ingredients.yaml` - Main ingredient database
- `data/analysis/culturemech_role_distribution.csv` - Role frequency
- `data/analysis/top100_role_crossref.yaml` - Top 100 cross-reference
- `data/analysis/role_statistics_report.yaml` - Comprehensive statistics

**Utilities**:
- `src/mediaingredientmech/utils/doi_resolver.py` - DOI resolution client
- `src/mediaingredientmech/curation/ingredient_curator.py` - Core curation logic

## References

1. **CultureMech Repository**: https://github.com/CultureBotAI/CultureMech
2. **MediaIngredientMech Schema**: `src/mediaingredientmech/schema/mediaingredientmech.yaml`
3. **Role Enum Documentation**: Lines 466-502 in schema
4. **Crossref API**: https://api.crossref.org/ (for DOI resolution)

## Change Log

### 2026-03-15: Initial Role Curation Implementation

**Phase 1: Schema Extensions**
- Added 4 new IngredientRoleEnum values: REDOX_INDICATOR, PH_INDICATOR, SELECTIVE_AGENT, SURFACTANT
- Updated VALID_MEDIA_ROLES in ingredient_curator.py

**Phase 2: DOI Infrastructure**
- Created doi_resolver.py with Crossref API integration
- Caching and rate limiting implemented
- Ready for future DOI literature review

**Phase 3: Top 100 Curation**
- Analyzed 570 ingredients with CultureMech role annotations
- Extracted roles for top 100 high-occurrence ingredients
- Added 18 new role assignments (82 already existed)
- Enriched 82 existing citations with structured metadata

**Phase 4: Validation and Statistics**
- Generated comprehensive statistics report
- 446 ingredients with roles (44.8% coverage)
- 448 total roles, 99.8% citation coverage
- Average confidence: 0.998

**Metrics**:
- Analysis time: ~2 hours
- Lines of code added: ~2000
- Data quality: Production-ready
