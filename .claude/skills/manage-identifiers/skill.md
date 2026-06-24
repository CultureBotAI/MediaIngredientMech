---
name: manage-identifiers
description: Use this skill to manage MediaIngredientMech record identifiers. In MIM the record `identifier` IS the ontology mapping CURIE (CHEBI / FOODON / cas / kgmicrobe.compound / kgmicrobe.ingredient / mesh / NCIT / MICRO / ENVO) for a mapped ingredient, or an `UNMAPPED_NNNN` placeholder for an unmapped one — there is no separate sequential id. Use when adding or importing ingredient records, minting the next `UNMAPPED_NNNN` placeholder, promoting an unmapped record to its resolved CURIE, or reconciling identifier collisions. (Sequential `RepoName:NNNNNN` ids are a sister-repo scheme — see the cross-repo reference.)
category: workflow
requires_database: false
requires_internet: false
version: 2.0.0
---

# Identifier Management (MediaIngredientMech)

## Overview — MIM uses CURIE identifiers, not sequential ids

MediaIngredientMech is a **multi-file collection**: every ingredient is its own YAML file
under `data/ingredients/mapped/` (mapped) or `data/ingredients/unmapped/` (unmapped). The
identifying field is **`identifier`** (the schema's `identifier: true` slot on
`IngredientRecord`), and its value is:

- **Mapped record** → the ontology mapping **CURIE**, equal to `ontology_mapping.ontology_id`
  (e.g. `identifier: CHEBI:9532`). Prefixes actually in use, by frequency: `CHEBI:` (~1360),
  `cas:` (~248), `kgmicrobe.compound:` (~64), `mesh:` (~61), `MICRO:` (~44), `NCIT:` (~31),
  `FOODON:` (~26), `kgmicrobe.ingredient:` (~25), `ENVO:` (~10).
- **Unmapped record** → an **`UNMAPPED_NNNN`** placeholder (zero-padded 4-digit, e.g.
  `UNMAPPED_0001`); ~380 records.

> **There is no `MediaIngredientMech:NNNNNN` sequential id in MIM.** The legacy separate id
> was removed (`scripts/migrate_drop_legacy_ontology_id.py`); records carry only `identifier`.
> Sister repos **CultureMech** and **CommunityMech** *do* mint sequential `RepoName:NNNNNN`
> ids — that scheme lives in the [cross-repo reference](reference/cross-repo.md), not here.

## When to Use This Skill

- Adding or importing an ingredient record (set its `identifier` correctly)
- Minting the next `UNMAPPED_NNNN` placeholder for a new unmapped ingredient
- Promoting an unmapped record to its resolved CURIE once it's mapped
- Reconciling identifier collisions / duplicates, or auditing identifier↔mapping consistency

---

## Identifier Format

| Record state | `identifier` value | Example |
|---|---|---|
| **Mapped** | the ontology CURIE, `== ontology_mapping.ontology_id` | `CHEBI:26710`, `cas:7647-14-5`, `kgmicrobe.compound:foo` |
| **Unmapped** | `UNMAPPED_NNNN` (4-digit, zero-padded) | `UNMAPPED_0042` |

Schema pattern for CURIE identifiers (`src/mediaingredientmech/schema/mediaingredientmech.yaml`):
`^[A-Za-z][A-Za-z0-9.]*:[A-Za-z0-9][A-Za-z0-9._~-]*$`. The `identifier` of a mapped record
**must equal** its `ontology_mapping.ontology_id` (the id↔label gate checks this).

---

## Core Workflow

Records are one file per ingredient. Choosing/curating the ontology mapping is the
[`map-media-ingredients`](../map-media-ingredients/skill.md) skill; consolidating duplicates is
[`merge-ingredients`](../merge-ingredients/skill.md). This skill is about the **`identifier`
value** itself.

### 1. Mapped record — the identifier IS the CURIE

The identifier is **not** minted sequentially; it is the ontology term selected during mapping.
Set `identifier` to the mapping's CURIE so the two agree:

```yaml
identifier: CHEBI:26710          # == ontology_mapping.ontology_id
preferred_term: sodium chloride
ontology_mapping:
  ontology_id: CHEBI:26710
  ontology_label: sodium chloride
  ontology_source: CHEBI
```

### 2. Unmapped record — mint the next `UNMAPPED_NNNN`

Find the highest existing placeholder across all record files, then add 1:

```bash
# quick check
grep -rhoE 'UNMAPPED_[0-9]{4}' data/ingredients/ | sort -u | tail -1
```

```python
import re, pathlib
nums = [int(m.group(1))
        for p in pathlib.Path('data/ingredients').rglob('*.yaml')
        for m in re.finditer(r'^identifier:\s*UNMAPPED_(\d{4})', p.read_text(), re.M)]
next_id = f"UNMAPPED_{(max(nums, default=0) + 1):04d}"
```

Write the new record as its own file `data/ingredients/unmapped/<slug>.yaml` with
`identifier: <next_id>`, `mapping_status: UNMAPPED`, and a `curation_history` entry. Save with
`sort_keys=False` to preserve field order.

### 3. Promote an unmapped record to its CURIE

When an `UNMAPPED_NNNN` ingredient gets an ontology mapping, change `identifier` from the
placeholder to the CURIE (matching `ontology_mapping.ontology_id`), flip `mapping_status`,
move the file from `unmapped/` to `mapped/`, and append a `curation_history` entry recording
the old placeholder → new CURIE transition. Never silently drop the provenance.

---

## Validation

- **Format:** every `identifier` is a valid CURIE (schema pattern above) **or** `UNMAPPED_NNNN`.
- **Consistency:** for mapped records, `identifier == ontology_mapping.ontology_id`.
- **Uniqueness:** no two records share an `identifier` (collisions break cross-references).
- **Gate:** `just validate-strict` (closed-schema), `just validate-terms[-all]`, and
  `just validate-products` (Engine B id↔label) enforce the above.

---

## Best Practices

### DO
- **Mapped identifier = the ontology CURIE** (equal to `ontology_mapping.ontology_id`).
- **Mint `UNMAPPED_NNNN` as highest+1**, zero-padded to 4 digits, scanning all record files.
- **Append `curation_history`** on every identifier assignment or change; save `sort_keys=False`.
- **Preserve provenance** when promoting `UNMAPPED_NNNN` → CURIE (record it in history).

### DON'T
- **Don't invent `MediaIngredientMech:NNNNNN` ids** — MIM does not use a sequential record id.
- **Don't let `identifier` diverge** from `ontology_mapping.ontology_id` on a mapped record.
- **Don't reuse a retired `UNMAPPED_NNNN`** number, and don't renumber existing placeholders.
- **Don't use `sort_keys=True`** when saving (breaks field order).

---

## Reference Files (sister-repo sequential-id scheme — not MIM's model)

> These describe the **sequential `RepoName:NNNNNN`** identifier scheme used by **CultureMech**
> and **CommunityMech** (and the generic X-Mech template). They do **not** apply to MIM, whose
> model is the CURIE / `UNMAPPED_NNNN` `identifier` described above. Use them when working in
> those sister repos or bootstrapping a new X-Mech repository.

| File | Contents |
|------|----------|
| [`reference/finding-highest-id.md`](reference/finding-highest-id.md) | Finding the highest sequential id (single-file, multi-file scan, registry) |
| [`reference/minting-and-adding.md`](reference/minting-and-adding.md) | Generic mint function and add-record workflows + batch-assignment scripts for the sequential scheme |
| [`reference/validation.md`](reference/validation.md) | Sequential-id format validator, duplicate finder, gap finder |
| [`reference/cross-repo.md`](reference/cross-repo.md) | Collection-type comparison, CultureMech/CommunityMech quick references, integration, decision tree |
| [`reference/utility-module.md`](reference/utility-module.md) | Copy-paste `xmech_id_utils` module for the sequential scheme |
