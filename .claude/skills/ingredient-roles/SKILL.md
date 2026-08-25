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
MediaIngredientMech schema. MIM does not currently expose an ingredient-variant
hierarchy or a supported role-propagation hand-off to CultureMech.

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

# 2. Generate the cross-reference required by the enrichment step
python scripts/analyze_culturemech_roles.py

# 3. Enrich existing mapped ingredients with inferred roles
python scripts/enrich_existing_roles.py

# 4. Validate all role assignments (check enum membership)
python scripts/validate_roles.py

# 5. Generate role coverage statistics
python scripts/generate_role_statistics.py
```

---

## Scripts

| Script | Purpose |
|--------|---------|
| `scripts/extract_roles_from_synonyms.py` | Parse synonym text for role keywords; output candidate assignments |
| `scripts/extract_all_roles.py` | List all role assignments currently in MIM records |
| `scripts/extract_top100_roles.py` | Extract roles for the top 100 most-used ingredients |
| `scripts/enrich_existing_roles.py` | Enrich existing assignments across the three role facets |
| `scripts/validate_roles.py` | Check all assigned roles against schema enum; report invalid values |
| `scripts/generate_role_statistics.py` | Role frequency distribution report |
| `scripts/analyze_culturemech_roles.py` | Compare role assignments against CultureMech usage context |
| `scripts/import_pfas_roles.py` | Import roles for PFAS compound class |
| `scripts/example_role_queries.py` | Example queries and usage patterns |

---

## Role Enum Values

Roles are defined in the MIM schema. Common values:

| Role | Facet | Description |
|------|-------|-------------|
| `CARBON_SOURCE` | nutritional | Primary or supplemental carbon |
| `NITROGEN_SOURCE` | nutritional | Nitrogen supply |
| `PHOSPHATE_SOURCE` | nutritional | Phosphate supply |
| `SULFUR_SOURCE` | nutritional | Sulfur supply |
| `VITAMIN_SOURCE` | nutritional | Vitamin supplement |
| `TRACE_ELEMENT` | nutritional | Micronutrient |
| `BUFFER` | physicochemical | pH stabilization |
| `CHELATOR` | physicochemical | Metal-ion chelation |
| `REDUCING_AGENT` | physicochemical | Redox-potential control |
| `SOLIDIFYING_AGENT` | physicochemical | Solidifying agent |
| `SELECTIVE_AGENT` | physicochemical | Selective or antimicrobial action |
| `ELECTRON_DONOR` | cellular metabolic | Donates electrons in organism context |
| `ELECTRON_ACCEPTOR` | cellular metabolic | Accepts electrons in organism context |

---

## Extraction Logic

`extract_roles_from_synonyms.py` looks for role keywords in:
- `preferred_term`
- `synonyms[].synonym_text`
- CHEBI ontology annotations (if available)

Examples of keyword → role mappings:
- "carbon source", "C source" → `CARBON_SOURCE`
- "buffer", "buffering agent" → `BUFFER`
- "chelating agent", "chelator" → `CHELATOR`
- "reducing agent", "reductant" → `REDUCING_AGENT`
- "vitamin", "coenzyme" → `VITAMIN_SOURCE`

---

## Schema Field

Roles are structured assignments in one of three orthogonal facet slots:

```yaml
nutritional_roles:
  - role: CARBON_SOURCE
    confidence: 0.9
physicochemical_roles:
  - role: BUFFER
    confidence: 0.9
cellular_metabolic_roles:
  - role: ELECTRON_DONOR
    confidence: 0.8
```

---

## Integration with CultureMech

No maintained cross-repository command currently propagates these roles. Treat
MIM role assignments as curated source data; coordinate and validate any future
CultureMech consumer before describing it as an operational hand-off. The stale
historical hierarchy command is documented in issue #186.

---

## When to Rerun

- After adding new MIM ingredient records (run extraction + enrichment)
- After MIM schema adds new role enum values (revalidate all)
- Before publishing or consuming roles through a reviewed cross-repository workflow

---

## Related Skills

- `map-media-ingredients` (MIM) — ontology mapping that precedes role assignment
- `merge-ingredients` (MIM) — deduplication; roles should be assigned after merging
- `review-ingredients` (MIM) — validation includes role field checking
