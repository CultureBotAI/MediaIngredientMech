---
name: map-media-ingredients
description: Use this skill to map MediaIngredientMech growth-media ingredient names to ontology terms (CHEBI for chemicals, FOODON for biologicals, ENVO for environmental) via exact → normalized → fuzzy → manual matching, with chemical normalization (hydrates, formulas, catalog codes) and synonym preservation. Use when curating unmapped ingredients, adding new ones, or validating existing mappings.
category: workflow
requires_database: false
requires_internet: true
version: 1.1.0
---

# Media Ingredient Ontology Mapping

## Overview

Map microbial growth-media ingredient names to authoritative ontology terms for semantic
integration and knowledge-graph construction. This ensures consistency across datasets,
enables semantic queries, and links to KG-Microbe / CHEBI / FOODON / ENVO. Scope: chemical
compounds (salts, organics), biological materials (extracts, peptones), and environmental
samples (soil, seawater).

## When to Use This Skill

- Adding new ingredients to MediaIngredientMech, or curating unmapped ones from formulations
- Validating existing ontology mappings
- Integrating media data with the KG-Microbe knowledge graph
- Normalizing chemical names with hydrates, catalog codes, or incomplete formulas
- Deciding which ontology (CHEBI vs FOODON vs ENVO) to use

---

## Ontology Selection Guide

| Ingredient Type | Primary Ontology | Examples | When to Use |
|----------------|------------------|----------|-------------|
| Simple chemicals | **CHEBI** | NaCl, glucose, MgSO4•7H2O, K2HPO4 | Pure chemical compounds, salts, ions |
| Biological materials | **FOODON** | yeast extract, peptone, tryptone, beef extract | Biological/food-derived preparations |
| Environmental samples | **ENVO** | soil extract, seawater, sediment | Natural environmental materials |
| Complex mixtures | *often unmappable* | "Vitamin solution A", "Trace metals" | Too generic for a specific mapping |

**Priority order: CHEBI → FOODON → ENVO.** Try the most specific ontology first; fall back to
broader ones.

---

## Chemical Normalization Rules

Many names need normalization before matching — `chemical_normalizer.py` handles these
patterns, and **preserves the original form as a typed synonym**:

1. **Hydrate stripping** (synonym `HYDRATE_FORM`): `MgSO4•7H2O` → `MgSO4` → "magnesium sulfate"; `CaCl2·2H2O` → "calcium chloride".
2. **Incomplete-formula correction** (synonym `INCOMPLETE_FORMULA`): `K2HPO` → `K2HPO4` → "dipotassium phosphate".
3. **Catalog-number removal** (synonym `CATALOG_VARIANT`): `NaCl (Fisher S271-500)` → `NaCl`.
4. **Abbreviation expansion**: `dH2O` → "distilled water"; `NaOAc` → "sodium acetate".
5. **Formula → common name**: built-in `FORMULA_TO_NAME` map (40+ entries, e.g. `NaCl` → "sodium chloride", `MgSO4` → "magnesium sulfate").

---

## Matching Strategies

Escalate from cheapest to most expensive; use the simplest that works. Full code (OAK,
`OntologyClient`, `chemical_normalizer`, OLS) is in
[`reference/matching-strategies.md`](reference/matching-strategies.md).

- **Level 1 — Exact match.** Case-insensitive string match against ontology labels, via OAK
  `basic_search` or `OntologyClient.search(..., sources=["CHEBI"])`.
- **Level 2 — Normalized match.** Apply `normalize_chemical_name` / `generate_search_variants`,
  then `client.search_with_variants(...)` (deduplicates, keeps best scores).
- **Level 3 — Fuzzy match.** OAK lexical search (`l~` prefix) or the EBI OLS web API for
  synonyms/spelling variants. OAK is primary (fast, offline); OLS is secondary (cross-validation).
- **Level 4 — Manual curation.** For complex mixtures, generic/incomplete terms, ambiguous
  names, or novel formulations — mark `NEEDS_EXPERT`.

---

## Workflows

### A. Interactive single ingredient
```bash
python scripts/curate_unmapped.py
```
Normalizes the name, generates variants, searches CHEBI → FOODON → ENVO, presents scored
candidates with media-usage context; user accepts or marks `NEEDS_EXPERT`.

### B. Batch curation (auto-curable simple chemicals)
```bash
python scripts/analyze_unmapped.py                                    # categorize first
python scripts/batch_curate_unmapped.py --category SIMPLE_CHEMICAL \
  --auto-normalize --min-confidence 0.9 --dry-run                     # preview
python scripts/batch_curate_unmapped.py --category SIMPLE_CHEMICAL \
  --auto-normalize --min-confidence 0.9                               # apply
```
Best for `SIMPLE_CHEMICAL` with clear normalization patterns and score ≥ 0.9. Auto-normalizes
with synonym preservation, multi-variant dedup, dry-run, and provenance tracking.

### C. Claude Code-assisted curation (complex cases, zero API cost)
```bash
python scripts/prepare_for_claude_curation.py --category UNKNOWN --limit 20 --output notes/batch_001.md
# Open notes/batch_001.md and ask Claude Code to suggest ontology mappings →
python scripts/apply_claude_suggestions.py --suggestions notes/batch_001_suggestions.yaml --validate
```
Full reasoning/audit trail for ambiguous cases. See `docs/CLAUDE_CODE_CURATION.md`.

---

## Quality Guidelines

| Quality Level | Meaning |
|--------------|---------|
| `EXACT_MATCH` | String matches the ontology label exactly |
| `SYNONYM_MATCH` | Matches a known ontology synonym |
| `CLOSE_MATCH` | Semantically equivalent, different phrasing |
| `MANUAL_CURATION` | Expert judgment required |
| `LLM_ASSISTED` | Claude Code / LLM suggested |
| `NEEDS_EXPERT` | Requires domain-expert review |

All mappings record curator (automated/manual/LLM), timestamp, and reasoning.

## Categorization System

`scripts/analyze_unmapped.py` assigns categories + mappability scores to prioritize effort:

| Category | Description | Mappability | Strategy |
|----------|-------------|-------------|----------|
| `SIMPLE_CHEMICAL` | Salts, common organics | High (80–100) | Batch curation |
| `COMPLEX_MIXTURE` | Vitamin/metal solutions | Low (10–30) | Often unmappable |
| `ENVIRONMENTAL` | Soil, seawater | Medium (50–70) | Try ENVO |
| `INCOMPLETE` | Generic terms | Low (20–40) | Manual review |
| `PLACEHOLDER` | "See source" | Very low (0–10) | Leave unmapped |
| `UNKNOWN` | Uncategorized | Medium (40–60) | Claude Code-assisted |

---

## Best Practices

### DO
- **Normalize before searching**; try multiple ontologies (CHEBI → FOODON → ENVO).
- **Use the most specific term** ("D-glucose" > "glucose" > "sugar").
- **Record provenance** and **preserve original forms** (hydrates, catalogs) as synonyms.
- **Validate** that the term exists and the definition matches; **check KG-Microbe first** to reuse existing entities.

### DON'T
- **Don't force mappings** for complex mixtures, or **use generic terms** when a specific one exists.
- **Don't skip normalization** for chemicals, or **ignore synonym preservation**.
- **Don't guess at low confidence** — mark `NEEDS_EXPERT`; and **don't create duplicates**.

---

## Reference Files

| File | Contents |
|------|----------|
| [`reference/matching-strategies.md`](reference/matching-strategies.md) | Full code for all 4 matching levels — OAK `basic_search`, `OntologyClient.search`/`search_with_variants`, `chemical_normalizer`, OAK `l~` fuzzy search, and the EBI OLS API wrapper |
| [`reference/kg-microbe-integration.md`](reference/kg-microbe-integration.md) | CultureMech import/export scripts, checking existing KG-Microbe ingredients, and how ingredients link to media/organisms |
| [`reference/examples-and-troubleshooting.md`](reference/examples-and-troubleshooting.md) | Five worked examples (hydrate, incomplete formula, biological extract, environmental, unmappable mixture) and troubleshooting (no/too-many/ambiguous matches, complex mixtures) |
| [`reference/tools-and-api.md`](reference/tools-and-api.md) | Curation scripts, core utilities, docs, related skills, and the `chemical_normalizer`/`OntologyClient`/`UnmappedCurator` implementation API |
