---
name: manage-identifiers
description: Use this skill to manage MediaIngredientMech record identifiers — find the highest existing MIM id, mint the next id, and insert new ingredient records with correct id placement and prefix conventions (MIM / CHEBI / cas / kgmicrobe.*). Use when adding or importing ingredient records, or reconciling id collisions.
category: workflow
requires_database: false
requires_internet: false
version: 1.1.0
---

# Identifier Management (MediaIngredientMech)

## Overview

Maintain stable, sequential record identifiers for MediaIngredientMech so records have
persistent references, link cleanly across repositories, and integrate into the knowledge
graph. IDs never change once assigned and are never reused.

MediaIngredientMech is a **single-file collection**: every ingredient lives in one YAML
file under a collection key (`ingredients`), each with an `id` of the form
`MediaIngredientMech:NNNNNN` (zero-padded 6-digit, `000001`–`999999`).

> The same identifier infrastructure is shared with CultureMech (multi-file + registry)
> and CommunityMech (multi-file). Those collection types, their find/mint/add variants,
> and a copy-paste utility module are documented in the reference files below — use them
> when working cross-repo or setting up a new X-Mech repository.

## When to Use This Skill

- Adding a new ingredient record (or importing a batch)
- Finding the next available ID before minting
- Running batch ID assignment
- Validating ID sequences (duplicates, gaps, format)
- Reconciling ID collisions

---

## Identifier Format

```
MediaIngredientMech:NNNNNN
```

- `MediaIngredientMech` — repository prefix
- `NNNNNN` — zero-padded 6-digit sequential number (`000001`–`999999`)

Zero-padding makes alphabetical sort == numerical sort. The `id` is stable, unique within
the repo, and works directly as an RDF subject/object. (Record `id` is distinct from the
ontology mapping `identifier`, which carries the `CHEBI` / `cas` / `kgmicrobe.*` / `UNMAPPED_*`
value — see [`merge-ingredients`](../merge-ingredients/skill.md) and
[`map-media-ingredients`](../map-media-ingredients/skill.md).)

---

## Core Workflow

**Data file:** `data/curated/unmapped_ingredients.yaml` (collection key: `ingredients`).
Full code for every step — including the multi-file and registry variants — is in
[`reference/finding-highest-id.md`](reference/finding-highest-id.md) and
[`reference/minting-and-adding.md`](reference/minting-and-adding.md).

### 1. Find the highest existing ID

```bash
# quick check
grep -o 'MediaIngredientMech:[0-9]\+' data/curated/unmapped_ingredients.yaml \
  | cut -d: -f2 | sort -n | tail -1
```

```python
highest = find_highest_id_single_file(
    Path('data/curated/unmapped_ingredients.yaml'), 'MediaIngredientMech', 'ingredients')
```

### 2. Mint the next ID

```python
next_id = generate_xmech_id('MediaIngredientMech', highest + 1)   # -> 'MediaIngredientMech:000113'
# generate_xmech_id(prefix, n) == f"{prefix}:{n:06d}"
```

### 3. Add the record (single-file append)

```python
new_record = {
    'id': next_id,                                  # ALWAYS the first field
    'identifier': f'UNMAPPED_{(highest + 1):04d}',  # or CHEBI/cas/kgmicrobe.* once mapped
    'preferred_term': 'New Ingredient Name',
    'synonyms': [],
    'mapping_status': 'UNMAPPED',
    'occurrence_statistics': {'total_occurrences': 1, 'media_count': 1},
    'curation_history': [{
        'timestamp': datetime.now(timezone.utc).isoformat(),
        'curator': 'manual_addition', 'action': 'CREATED',
        'changes': 'New ingredient added manually',
        'new_status': 'UNMAPPED', 'llm_assisted': False,
    }],
    'notes': 'Added manually via identifier management workflow',
}
data['ingredients'].append(new_record)
data['total_count'] = len(data['ingredients'])
data['generation_date'] = datetime.now(timezone.utc).isoformat()
with open(yaml_path, 'w') as f:
    yaml.dump(data, f, default_flow_style=False, sort_keys=False, allow_unicode=True)
```

Key points: `id` first; update `total_count` and `generation_date`; **`sort_keys=False`**
to preserve field order; always include a `curation_history` entry.

### 4. Batch assignment

```bash
python scripts/add_mediaingredientmech_ids.py --dry-run   # preview (always first)
python scripts/add_mediaingredientmech_ids.py             # execute
```

Skips records that already have IDs, assigns sequentially, prints a Rich sample table and
added/skipped stats. `--force-overwrite` exists — use with caution. CultureMech/CommunityMech
batch scripts are covered in [`reference/minting-and-adding.md`](reference/minting-and-adding.md).

---

## Validation

Validate format, find duplicates, and find sequence gaps — full validators and fixes in
[`reference/validation.md`](reference/validation.md):

- **Format:** every `id` matches `^MediaIngredientMech:\d{6}$`.
- **Duplicates:** no two records share an ID (breaks references).
- **Gaps:** sequence is contiguous (gaps are tolerable but avoid creating them).

---

## Best Practices

### DO
- **Run `--dry-run` first** before any batch operation, and validate after changes.
- **Zero-pad** with `{number:06d}`; place `id` first in the YAML.
- **Update metadata** (`total_count`, `generation_date`) on the single file.
- **Preserve ID history** — never reuse a deleted ID.
- **Use the existing scripts** for batches; document manual additions in `curation_history`.

### DON'T
- **Don't assign IDs** without checking the highest first.
- **Don't reuse** IDs from deleted records (breaks cross-references).
- **Don't use `sort_keys=True`** when saving (breaks field order).
- **Don't force-overwrite** existing IDs unless absolutely necessary.
- **Don't create gaps intentionally**, and don't use non-standard formats.

---

## Reference Files

| File | Contents |
|------|----------|
| [`reference/finding-highest-id.md`](reference/finding-highest-id.md) | Finding the highest ID for all three collection types (single-file, multi-file scan, registry) |
| [`reference/minting-and-adding.md`](reference/minting-and-adding.md) | Generic mint function, full add-record workflows (1 single-file, 2 multi-file, 3 multi-file+registry), and all three batch-assignment scripts |
| [`reference/validation.md`](reference/validation.md) | ID-format validator, duplicate finder, gap finder, and common issues + fixes |
| [`reference/cross-repo.md`](reference/cross-repo.md) | Collection-type comparison, CultureMech/CommunityMech quick references, integration with `IngredientCurator` and KGX export, and the future-enhancements/decision-tree material |
| [`reference/utility-module.md`](reference/utility-module.md) | Copy-paste-ready `xmech_id_utils` module covering all collection types |
