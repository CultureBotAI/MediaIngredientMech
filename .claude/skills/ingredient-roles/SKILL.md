---
name: ingredient-roles
description: Extract, assign, enrich, and validate functional roles for MediaIngredientMech ingredients (carbon_source, nitrogen_source, buffer, antibiotic, etc.) from synonyms and existing records
category: workflow
requires_database: false
requires_internet: false
version: 1.0.0
tags: [roles, functional-roles, ingredients, synonyms, chebi, ontology, curation]
---

# Ingredient Roles Skill

## Overview

Functional roles describe what an ingredient *does* in a growth medium
(e.g. `carbon_source`, `nitrogen_source`, `buffer`, `chelator`, `antibiotic`,
`reducing_agent`, `vitamin`, `trace_element`). Roles are defined in the
MediaIngredientMech schema and used by CultureMech's ingredient hierarchy system.

This skill covers:
- **Extraction** — infer roles from synonym text and existing records
- **Enrichment** — add roles to already-mapped ingredients that lack them
- **Validation** — verify roles are valid enum values
- **Reporting** — coverage statistics and role distribution

**Run from `MediaIngredientMech/` directory.**

---

## Standard Workflow

```bash
# 1. Extract roles inferred from synonym text (e.g. "nitrogen source" → nitrogen_source)
python scripts/extract_roles_from_synonyms.py

# 2. Enrich existing mapped ingredients with inferred roles
python scripts/enrich_existing_roles.py

# 3. Validate all role assignments (check enum membership)
python scripts/validate_roles.py

# 4. Generate role coverage statistics
python scripts/generate_role_statistics.py
```

---

## Scripts

| Script | Purpose |
|--------|---------|
| `scripts/extract_roles_from_synonyms.py` | Parse synonym text for role keywords; output candidate assignments |
| `scripts/extract_all_roles.py` | List all role assignments currently in MIM records |
| `scripts/extract_top100_roles.py` | Extract roles for the top 100 most-used ingredients |
| `scripts/enrich_existing_roles.py` | Add inferred roles to ingredient files that lack `functional_role` |
| `scripts/validate_roles.py` | Check all assigned roles against schema enum; report invalid values |
| `scripts/generate_role_statistics.py` | Role frequency distribution report |
| `scripts/analyze_culturemech_roles.py` | Compare role assignments against CultureMech usage context |
| `scripts/import_pfas_roles.py` | Import roles for PFAS compound class |
| `scripts/example_role_queries.py` | Example queries and usage patterns |

---

## Role Enum Values

Roles are defined in the MIM schema. Common values:

| Role | Description |
|------|-------------|
| `carbon_source` | Primary or supplemental carbon |
| `nitrogen_source` | Nitrogen supply |
| `phosphorus_source` | Phosphorus supply |
| `sulfur_source` | Sulfur supply |
| `buffer` | pH stabilization |
| `chelator` | Metal ion chelation (e.g. EDTA) |
| `reducing_agent` | Redox potential control |
| `vitamin` | Vitamin supplement |
| `trace_element` | Micronutrient |
| `antibiotic` | Selective agent |
| `gelling_agent` | Solidifying agent (agar, gellan) |
| `indicator` | pH/redox indicator dye |
| `salt` | Ionic strength / osmolarity |

---

## Extraction Logic

`extract_roles_from_synonyms.py` looks for role keywords in:
- `preferred_term`
- `synonyms[].synonym_text`
- CHEBI ontology annotations (if available)

Examples of keyword → role mappings:
- "carbon source", "C source" → `carbon_source`
- "buffer", "buffering agent" → `buffer`
- "chelating agent", "chelator" → `chelator`
- "reducing agent", "reductant" → `reducing_agent`
- "vitamin", "coenzyme" → `vitamin`

---

## Schema Field

Roles are stored in each MIM ingredient YAML as:

```yaml
functional_role:
  - carbon_source
  - nitrogen_source
```

Or as a single value:
```yaml
functional_role: buffer
```

---

## Integration with CultureMech

CultureMech imports roles via the ingredient hierarchy:
```bash
# In CultureMech — after updating roles in MIM:
just enrich-with-hierarchy
```

The `manage-ingredient-hierarchy` skill in CultureMech reads `functional_role` from
MIM records and populates `ingredient_role` in CultureMech media YAML files.

---

## When to Rerun

- After adding new MIM ingredient records (run extraction + enrichment)
- After MIM schema adds new role enum values (revalidate all)
- Before importing hierarchy into CultureMech (ensure roles are current)

---

## Related Skills

- `map-media-ingredients` (MIM) — ontology mapping that precedes role assignment
- `merge-ingredients` (MIM) — deduplication; roles should be assigned after merging
- `manage-ingredient-hierarchy` (CultureMech) — imports these roles into CultureMech
- `review-ingredients` (MIM) — validation includes role field checking
