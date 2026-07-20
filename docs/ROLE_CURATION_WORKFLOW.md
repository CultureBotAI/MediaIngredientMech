# Role Curation Workflow

## Overview

This document describes the workflow for curating media ingredient role assignments in MediaIngredientMech. Role curation assigns functional roles (e.g., CARBON_SOURCE, BUFFER, ELECTRON_ACCEPTOR) to ingredients based on evidence from CultureMech database annotations and scientific literature.

Roles are recorded on **three orthogonal facets** — `nutritional_roles`, `physicochemical_roles`, and `cellular_metabolic_roles` — each with its own enum and its own curator writer method. The single flat `media_roles` slot and its `IngredientRoleEnum` were retired in issue #128; see [Role Assignment Schema](#role-assignment-schema).

**Status snapshot** (as of 2026-03-15, before the #128 facet migration):
- **446 ingredients with roles** (44.8% coverage of 996 mapped ingredients)
- **448 total role assignments** (1.0 average per ingredient)
- **Average confidence: 0.998** (extremely high quality)
- **99.8% citation coverage** (447/448 roles have structured evidence)

For current numbers run `scripts/validate_roles.py`, which reports counts broken down by facet.

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
- **Clear, unambiguous roles** (MINERAL_SOURCE, BUFFER) over complex metabolic functions
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
- CultureMech role text (e.g., "Mineral source") → facet enum value (e.g., `MINERAL_SOURCE` on `nutritional_roles`)
- See `scripts/analyze_culturemech_roles.py::CULTUREMECH_ROLE_MAPPING` for full mapping table
- Two CultureMech role texts, "Salt" and "Solvating media", are deliberately **left unmapped**: they only ever produced the retired `SALT` value, and every such assignment in the corpus turned out to be a mis-assignment. Do not route them to `OSMOTIC_AGENT` — that value should be assigned on its own merits, not as a `SALT` substitute.

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

### Three role facets

Roles are split across three independent slots on `IngredientRecord`. The facets answer different questions, so an ingredient may legitimately carry values on more than one of them.

**1. `nutritional_roles` (NutritionalRoleEnum)** — *what element or macronutrient does this ingredient SUPPLY?*

- `CARBON_SOURCE` - Organic carbon for biosynthesis/energy
- `NITROGEN_SOURCE` - Nitrogen for amino acids/nucleotides
- `SULFUR_SOURCE` - Sulfur for cysteine/methionine/Fe-S clusters
- `PHOSPHATE_SOURCE` - Phosphate for nucleotides/phospholipids
- `IRON_SOURCE` - Iron specifically
- `TRACE_ELEMENT` - Micronutrient metals (zinc, cobalt, molybdenum)
- `MINERAL_SOURCE` - Residual bucket for bulk cations (Mg, Ca, K, Na) not covered by a more specific value
- `VITAMIN_SOURCE` - Vitamins or vitamin precursors
- `AMINO_ACID_SOURCE` - Specific amino acids
- `PROTEIN_SOURCE` - Peptides and proteins
- `COFACTOR_PROVIDER` - Supplies enzyme cofactors/prosthetic groups
- `ENERGY_SOURCE` - Primary energy substrate
- `LIGHT_SOURCE` - Light as energy input (phototrophs)

**2. `physicochemical_roles` (PhysicochemicalRoleEnum)** — *what chemical or physical function does it perform IN THE MEDIUM?*

- `BUFFER` - pH buffering agents
- `SOLIDIFYING_AGENT` - Gelling agents (agar)
- `CHELATOR` - Metal chelation (EDTA, NTA)
- `SURFACTANT` - Surfactants/detergents
- `REDUCING_AGENT` - Lowers redox potential (cysteine, sulfide, DTT)
- `OXIDIZING_AGENT` - Raises redox potential
- `PH_INDICATOR` - pH indicator dyes
- `REDOX_INDICATOR` - Redox indicators (resazurin)
- `SELECTIVE_AGENT` - Antimicrobial/selective agents
- `ANTIFOAM` - Foam suppression
- `OSMOTIC_AGENT` - Sets medium osmolarity/water activity
- `PRECIPITATION_INHIBITOR` - Keeps components in solution

**3. `cellular_metabolic_roles` (CellularMetabolicRoleEnum)** — *what does it do inside or on the cultured microbe?* These are frequently **organism-conditional**, so assign them only with organism context in the evidence.

- `SUBSTRATE` - Metabolized substrate
- `ELECTRON_DONOR` - Electron donor for chemolithotrophs
- `ELECTRON_ACCEPTOR` - Terminal electron acceptor (nitrate, fumarate)
- `COFACTOR` - Acts as an enzyme cofactor
- `PROSTHETIC_GROUP_PRECURSOR` - Precursor of a prosthetic group (heme, cobalamin)
- `MEMBRANE_COMPONENT` - Incorporated into membranes
- `OSMOPROTECTANT` - Accumulated intracellularly against osmotic stress
- `INDUCER` - Induces expression of a pathway
- `INHIBITOR` - Inhibits growth or a specific process
- `QUENCHER` - Quenches a reactive species

**Retired values — do not assign**:
- `MINERAL` was a curator catch-all. Replace it with the specific element source: `TRACE_ELEMENT`, `IRON_SOURCE`, `SULFUR_SOURCE`, `PHOSPHATE_SOURCE`, or `MINERAL_SOURCE` as the residual bucket for bulk cations.
- `SALT` is gone with no replacement. Every `SALT` assignment in the corpus was a mis-assignment (solvents and acids, not ionic-strength contributors) and they were dropped rather than remapped. `OSMOTIC_AGENT` is **not** a drop-in substitute.
- `SOLVENT` was never a valid enum value in any facet.

Note the deliberate `OSMOTIC_AGENT` / `OSMOPROTECTANT` split: the first is a medium-side property, the second an intracellular, organism-conditional one. They share a CHEBI mapping, so an automated classifier must not fan one annotation out to both facets.

### Role assignment structure

Each facet holds a list of assignments with the same shape:

```yaml
nutritional_roles:
  - role: MINERAL_SOURCE
    confidence: 1.0
    evidence:
      - reference_type: DATABASE_ENTRY
        reference_text: "CultureMech database (6041 occurrences as 'Mineral source')"
        url: "https://github.com/CultureBotAI/CultureMech"
        excerpt: "Role: Mineral source; Properties: Defined component, Inorganic compound, Simple component"
        curator_note: "Widespread use in media formulations (6041 occurrences). High confidence based on 'Defined component' property."
```

**Fields**:
- `role`: value from the facet's own enum (required)
- `confidence`: Float 0.0-1.0 (required)
- `evidence`: List of RoleCitation objects (required for quality)
  - `reference_type`: PUBLICATION, DATABASE_ENTRY, EXPERT_ANNOTATION
  - `reference_text`: Citation text with occurrence stats
  - `url`: Link to source
  - `excerpt`: Direct quote from source (role + properties)
  - `curator_note`: Contextual notes about assignment

### Writing roles

There is one writer per facet. They all take the same keyword arguments the retired `add_media_role()` took (`role`, `confidence`, `doi`, `pmid`, `reference_text`, `reference_type`, `url`, `excerpt`, `curator_note`, `notes`) and raise `ValueError` if the role is not a member of that facet's enum:

```python
curator.add_nutritional_role(record, "SULFUR_SOURCE", confidence=0.9, ...)
curator.add_physicochemical_role(record, "REDUCING_AGENT", confidence=0.95, ...)
curator.add_cellular_metabolic_role(record, "ELECTRON_ACCEPTOR", confidence=0.9, ...)
```

If a script infers a role name without knowing its facet, route it with the helper — every value is unique across the three enums, so the name determines the facet:

```python
from mediaingredientmech.utils.role_facets import add_role, facet_slot_for

facet_slot_for("BUFFER")            # -> 'physicochemical_roles'
add_role(curator, record, "BUFFER", confidence=0.95)
```

### Reading roles

Do not read the facet lists individually; iterate them:

```python
from mediaingredientmech.utils.role_iteration import (
    ALL_ROLE_SLOTS,
    FACET_ROLE_SLOTS,
    iter_role_assignments,
)

for slot, assignment in iter_role_assignments(record, slots=FACET_ROLE_SLOTS):
    print(slot, assignment["role"], assignment["confidence"])
```

`FACET_ROLE_SLOTS` is the three ingredient facets. `ALL_ROLE_SLOTS` (the default) additionally includes `community_organism_roles`, which describes organisms rather than ingredients — pass `FACET_ROLE_SLOTS` explicitly when you mean ingredient roles only.

## Multi-Role Handling

### Independent confidence scores

Each role is assigned **independently** with its own confidence score, whether it sits on the same facet as another role or a different one.

**Example: L-cysteine** — supplies two elements nutritionally, and separately lowers the redox potential of the medium:
```yaml
nutritional_roles:
  - role: AMINO_ACID_SOURCE
    confidence: 0.95
    evidence: [...]
  - role: SULFUR_SOURCE
    confidence: 0.9
    evidence: [...]
physicochemical_roles:
  - role: REDUCING_AGENT
    confidence: 1.0
    evidence: [...CultureMech, "Role: Reducing agent" in anaerobic media...]
```

### Choosing the right facet

The facets are orthogonal, so ask the three questions separately rather than picking a single "best" role:

| Question | Facet |
|----------|-------|
| What element/nutrient does it supply? | `nutritional_roles` |
| What does it do to the medium itself? | `physicochemical_roles` |
| What does it do inside/on the organism? | `cellular_metabolic_roles` |

An ingredient answering only one question gets only one facet populated — an empty facet is the normal case, not a gap to be filled.

### Potentially conflicting roles

Some role combinations require additional context:
- **CARBON_SOURCE + ELECTRON_ACCEPTOR** (nutritional + cellular-metabolic): rare, but valid for compounds like fumarate
- **BUFFER + SELECTIVE_AGENT** (both physicochemical): requires pH context (e.g., acidic pH inhibits some organisms)
- **OSMOTIC_AGENT + OSMOPROTECTANT**: assign the cellular-metabolic side only with organism-specific evidence of intracellular accumulation

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
   - Enum validity (each role belongs to the enum of the facet it sits on)
   - Citation coverage (all roles have evidence)
   - Confidence consistency (aligns with properties)
   - Multi-role coherence (no unexpected conflicts)

   Counts are reported per facet as well as in aggregate, and `community_organism_roles` is tallied separately from the three ingredient facets.

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
   - Example: "Water (base)" has invalid role `SOLVENT` (not a value in any facet enum)
   - Action: drop the assignment, or replace it with a value that genuinely applies — `SOLVENT` has no facet equivalent, and neither does the retired `SALT`

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
**Action**: Map ChEBI roles onto the facet enums via their `mappings:` annotations, auto-populate where confident. Not every ChEBI role has a facet equivalent — "solvent" does not, and such roles should be dropped rather than forced onto the nearest-looking value. Where one CHEBI term maps into two facets (CHEBI:25728 osmolyte → `OSMOTIC_AGENT` and `OSMOPROTECTANT`), emit only the medium-side value unless organism context is available.

## Troubleshooting

### Issue: Validation Error - Invalid Role Enum

**Symptom**: `Invalid nutritional role at index 0: SOLVENT` (or `Invalid physicochemical role ...` / `Invalid cellular-metabolic role ...`)

**Cause**: The role value is not a member of the enum owning the facet it was written to — either it is not a valid value at all, or it is valid but belongs to a different facet.

**Fix**:
1. Check whether the value belongs to another facet: `facet_slot_for(role)` in `src/mediaingredientmech/utils/role_facets.py` names the correct slot. If so, move the assignment there (or write it via `add_role()`, which routes automatically).
2. If the value is retired (`MINERAL`, `SALT`) or never existed (`SOLVENT`), do not resurrect it. Replace `MINERAL` with the specific element source (`TRACE_ELEMENT`, `IRON_SOURCE`, `SULFUR_SOURCE`, `PHOSPHATE_SOURCE`, or `MINERAL_SOURCE`); drop `SALT` and `SOLVENT` assignments outright.
3. Only if the role is genuinely new and unrepresented, add it to the appropriate enum in `src/mediaingredientmech/schema/mediaingredientmech.yaml` and to the matching `VALID_*_ROLES` set in `src/mediaingredientmech/curation/ingredient_curator.py`. Names must stay unique across the three enums or facet routing breaks.

### Issue: Low Citation Coverage

**Symptom**: "Roles with citations: 250/500 (50%)"

**Cause**: Missing evidence entries in role assignments

**Fix**:
1. Run `scripts/enrich_existing_roles.py` to upgrade generic citations
2. For remaining gaps, add manual citations using the facet writer for the role (`curator.add_nutritional_role()`, `curator.add_physicochemical_role()`, or `curator.add_cellular_metabolic_role()`)

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
- `src/mediaingredientmech/utils/role_facets.py` - Route a role name to its facet writer
- `src/mediaingredientmech/utils/role_iteration.py` - Iterate role assignments across facets
- `src/mediaingredientmech/curation/ingredient_curator.py` - Core curation logic

## References

1. **CultureMech Repository**: https://github.com/CultureBotAI/CultureMech
2. **MediaIngredientMech Schema**: `src/mediaingredientmech/schema/mediaingredientmech.yaml`
3. **Role Enum Documentation**: `NutritionalRoleEnum`, `PhysicochemicalRoleEnum`, and `CellularMetabolicRoleEnum` in the schema
4. **Crossref API**: https://api.crossref.org/ (for DOI resolution)

## Change Log

### 2026-03-15: Initial Role Curation Implementation

> **Superseded by the issue #128 facet migration.** The entries below describe the
> original single-axis `IngredientRoleEnum` / `media_roles` design as it was at the
> time. That enum, the `RoleAssignment` class, and the `media_roles` slot no longer
> exist; roles now live on the three facets described in
> [Role Assignment Schema](#role-assignment-schema). Kept as history.

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
