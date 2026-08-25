---
name: manage-identifiers
description: Use this skill to manage MediaIngredientMech record identifiers. In MIM the record `identifier` is the primary ontology, registry, or local identity CURIE for a mapped ingredient, or an `UNMAPPED_NNNN` placeholder for an unmapped one; it may differ from the separate ontology grounding target and there is no sequential MIM id. Use when adding or importing records, minting placeholders, promoting an unmapped record, or reconciling identifier collisions. Sequential `RepoName:NNNNNN` ids, where used, belong to sister-repository contracts.
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

- **Mapped record** → its primary ontology, registry, or local identity **CURIE**
  (e.g. `identifier: CHEBI:9532` or `kgmicrobe.compound:sugars`). It often equals
  `ontology_mapping.ontology_id`, but registry/local identities legitimately
  differ from ontology grounding targets at any evidence-backed mapping quality.
  Prefixes in use include `CHEBI:`,
  `cas:` (~248), `kgmicrobe.compound:` (~64), `mesh:` (~61), `MICRO:` (~44), `NCIT:` (~31),
  `FOODON:` (~26), `kgmicrobe.ingredient:` (~25), `ENVO:` (~10).
- **Unmapped record** → an **`UNMAPPED_NNNN`** placeholder (zero-padded 4-digit, e.g.
  `UNMAPPED_0001`); ~380 records.

> **There is no `MediaIngredientMech:NNNNNN` sequential id in MIM.** The legacy separate id
> was removed (`scripts/migrate_drop_legacy_ontology_id.py`); records carry only `identifier`.
> Sister repositories may define their own sequential `RepoName:NNNNNN` ids;
> consult each repository's current schema and identifier instructions. MIM's
> retired copy of that generic guidance is historical material in `ATTIC/`.

## When to Use This Skill

- Adding or importing an ingredient record (set its `identifier` correctly)
- Minting the next `UNMAPPED_NNNN` placeholder for a new unmapped ingredient
- Promoting an unmapped record to its resolved CURIE once it's mapped
- Reconciling identifier collisions / duplicates, or auditing identifier↔mapping consistency

---

## Identifier Format

| Record state | `identifier` value | Example |
|---|---|---|
| **Mapped** | primary ontology, registry, or local identity CURIE | `CHEBI:26710`, `cas:7647-14-5`, `kgmicrobe.compound:foo` |
| **Unmapped** | `UNMAPPED_NNNN` (4-digit, zero-padded) | `UNMAPPED_0042` |

Schema pattern for CURIE identifiers (`src/mediaingredientmech/schema/mediaingredientmech.yaml`):
`^[A-Za-z][A-Za-z0-9.]*:[A-Za-z0-9][A-Za-z0-9._~-]*$`. Consult
`MAPPING_SEMANTICS.md` before choosing between a direct ontology identity and a
registry/local identity with separate ontology grounding.

---

## Core Workflow

Records are one file per ingredient. Choosing/curating the ontology mapping is the
[`map-media-ingredients`](../map-media-ingredients/SKILL.md) skill; consolidating duplicates is
[`merge-ingredients`](../merge-ingredients/SKILL.md). This skill is about the **`identifier`
value** itself.

### 1. Mapped record — choose the primary identity

The identifier is **not** minted sequentially. For a direct ontology identity,
it is the selected ontology term and the two fields agree:

```yaml
identifier: CHEBI:26710          # == ontology_mapping.ontology_id
preferred_term: sodium chloride
ontology_mapping:
  ontology_id: CHEBI:26710
  ontology_label: sodium chloride
  ontology_source: CHEBI
```

For a registry/local identity, keep that primary identifier and record the
ontology grounding independently, with the correct mapping quality:

```yaml
identifier: kgmicrobe.compound:sugars
preferred_term: Sugars
ontology_mapping:
  ontology_id: CHEBI:16646
  ontology_label: carbohydrate
  ontology_source: CHEBI
  mapping_quality: NARROW_MATCH
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

### 3. Promote an unmapped record to its primary identity

When an `UNMAPPED_NNNN` ingredient is resolved, change `identifier` from the
placeholder to the evidence-backed ontology, registry, or local identity CURIE,
flip `mapping_status`, move the file from `unmapped/` to `mapped/`, and append a
`curation_history` entry recording the transition. Populate ontology grounding
separately under `MAPPING_SEMANTICS.md`; never silently drop provenance.

---

## Validation

- **Format:** every `identifier` is a valid CURIE (schema pattern above) **or** `UNMAPPED_NNNN`.
- **Mapped state:** a mapped record must not retain an `UNMAPPED_NNNN` placeholder;
  equality with the ontology grounding is not required.
- **Duplicate-family control:** ontology identifiers can be shared by known
  duplicate families; `mappings/duplicate_identifier_baseline.tsv` records the
  accepted baseline and QC rejects unreviewed drift. Do not treat `identifier`
  as a unique document address.
- **Gate:** `just validate-strict` (closed-schema), `just validate-terms[-all]`, and
  `just validate-products` (Engine B id↔label) enforce the above.

---

## Best Practices

### DO
- **Choose the mapped identifier from identity evidence** and treat ontology
  grounding as a separate decision when a registry/local identity is needed.
- **Mint `UNMAPPED_NNNN` as highest+1**, zero-padded to 4 digits, scanning all record files.
- **Append `curation_history`** on every identifier assignment or change; save `sort_keys=False`.
- **Preserve provenance** when promoting `UNMAPPED_NNNN` → CURIE (record it in history).

### DON'T
- **Don't invent `MediaIngredientMech:NNNNNN` ids** — MIM does not use a sequential record id.
- **Don't force equality** between `identifier` and ontology grounding when
  `MAPPING_SEMANTICS.md` requires a distinct registry/identity row.
- **Don't reuse a retired `UNMAPPED_NNNN`** number, and don't renumber existing placeholders.
- **Don't use `sort_keys=True`** when saving (breaks field order).

---

## Sister-repository identifiers

Do not copy MIM identifier rules into another repository. CultureMech,
CommunityMech, and other X-Mech projects own their current record-addressing
contracts. Check their live schema and instructions before minting an id.
