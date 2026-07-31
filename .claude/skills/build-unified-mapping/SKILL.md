---
name: build-unified-mapping
description: Build a single unified ingredient mapping TSV across CultureMech, MediaIngredientMech, and CommunityMech — one row per unique ingredient name with all available identifiers
category: integration
requires_database: false
requires_internet: false
version: 1.0.0
tags: [unified-mapping, cross-repo, integration, tsv, ingredients, chebi, cas-rn, kg-microbe]
---

# Build Unified Ingredient Mapping Skill

## Overview

**Purpose**: Produce a single canonical TSV (and YAML summary) that maps every unique ingredient name observed across CultureMech media to all available identifiers from MediaIngredientMech.

**Output columns**:

| Column | Description |
|--------|-------------|
| `ingredient_name` | Name as it appears in CultureMech media |
| `culturemech_term_id` | Ontology term ID recorded in CultureMech (`term.id`; CHEBI/FOODON) |
| `occurrence_count` | How many CultureMech media use this ingredient |
| `mim_id` | MediaIngredientMech record identifier (CHEBI:XXXXX or UNMAPPED_XXXX) |
| `chebi_id` | ChEBI ontology ID |
| `cas_rn` | CAS Registry Number |
| `kg_microbe_node_id` | KG-Microbe CHEBI node ID (if ingredient present in KG graph) |
| `mapping_status` | MAPPED / UNMAPPED / HAS_TERM_ID_NO_MIM / UNMATCHED_IN_MIM |
| `example_media` | Up to 3 CultureMech media IDs using this ingredient |

**Match logic** (priority order):
1. CultureMech `term.id` (CHEBI) → look up in MIM by CHEBI ID
2. Ingredient name / synonym → look up in MIM name index

## When to Use This Skill

- Generating a snapshot of cross-repo ingredient coverage for reporting
- Identifying which CultureMech ingredients still lack CHEBI or CAS-RN
- Input for downstream KG export or ontology alignment pipelines
- Periodic audit: how many of the ~3,853 CultureMech ingredient names are fully mapped?
- Sharing a flat reference file with collaborators who don't want to parse YAML

## How to Run

```bash
# From culturebotai-claw repo (recommended — it has the script)
cd ~/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw

# Default: both TSV and YAML summary in workspace/
python scripts/build_unified_ingredient_mapping.py

# Custom output path
python scripts/build_unified_ingredient_mapping.py --output workspace/my_mapping.tsv

# TSV only
python scripts/build_unified_ingredient_mapping.py --format tsv

# Or via justfile
just build-unified-mapping
```

**Output files**:
- `workspace/unified_ingredient_mapping.tsv` — full flat table (one row per unique CultureMech ingredient name)
- `workspace/unified_ingredient_mapping.yaml` — summary with status breakdown and top 50 fully-mapped ingredients

## Coverage Expectations (as of 2026-04-09)

| Metric | Count | % of 3,853 unique names |
|--------|-------|------------------------|
| Matched to MIM record | 1,185 | 30% |
| Have CHEBI ID | 1,212 | 31% |
| Have CAS-RN | 1,107 | 28% |
| Have KG-Microbe node ID | 775 | 20% |
| Fully mapped (CHEBI + CAS) | 1,094 | 28% |

The ~70% not matched to MIM are largely: complex trace mineral stocks, undefined buffer solutions, duplicate name variants (hydrate forms), catalog-coded entries, and FEBA-specific formulations that haven't been curated into MIM yet.

## Interpreting `mapping_status`

| Status | Meaning |
|--------|---------|
| `MAPPED` | In MIM with full ontology mapping |
| `UNMAPPED` | In MIM but lacking ontology term (unmapped record) |
| `HAS_TERM_ID_NO_MIM` | CultureMech has a `term.id` but no MIM record |
| `UNMATCHED_IN_MIM` | Not found in MIM by name or CHEBI |

## Increasing Coverage

To increase the match rate:
1. **Add CHEBI IDs to CultureMech media** → `just feba-enrich-ontology` in culturebotai-claw
2. **Add unmapped ingredients to MIM** → `just feba-create-mim-ingredients` in culturebotai-claw
3. **Add CAS-RNs to MIM** → `python scripts/enrich_mim_cas_rn.py` in culturebotai-claw
4. **Re-run this skill** to regenerate the unified mapping

## Workflow

```
1. Run the script
   python scripts/build_unified_ingredient_mapping.py

2. Review coverage
   # Count fully-mapped rows
   awk -F'\t' '$5!="" && $6!=""' workspace/unified_ingredient_mapping.tsv | wc -l

   # Find unmapped high-frequency ingredients
   awk -F'\t' 'NR>1 && $9=="UNMATCHED_IN_MIM" {print $3"\t"$1}' \
     workspace/unified_ingredient_mapping.tsv | sort -rn | head -20

3. Commit the output (optional — it's in workspace/ which is gitignored by default)
   cp workspace/unified_ingredient_mapping.tsv UNIFIED_INGREDIENT_MAPPING.tsv
   git add UNIFIED_INGREDIENT_MAPPING.tsv
   git commit -m "Update unified ingredient mapping"
```

## Related

- **Script**: `../culturebotai-claw/scripts/build_unified_ingredient_mapping.py`
- **Justfile recipe**: `just build-unified-mapping` in culturebotai-claw
- **CAS-RN enrichment**: `../culturebotai-claw/scripts/enrich_mim_cas_rn.py`
- **KG matching**: `../culturebotai-claw/scripts/match_mim_to_kg.py`
- **merge-ingredients skill**: deduplication within MIM (different from this cross-repo join)
- **map-media-ingredients skill**: mapping individual ingredient names to ontology terms
