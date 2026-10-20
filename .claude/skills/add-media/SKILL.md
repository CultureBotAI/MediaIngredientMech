---
name: add-media
description: "Add or curate a growth medium, stock solution, complex mixture, or media ingredient formulation in MediaIngredientMech. Covers pre-flight duplicate/synonym checks against existing records, primary identifier selection and kgmicrobe.ingredient minting under MAPPING_SEMANTICS.md, StockComponent has-part decomposition with ComponentAssertion provenance, typed CultureMech recipe cross-references (CultureMechReference), guarded YAML writes, SSSOM synchronization, and full QC verification."
category: workflow
requires_database: false
requires_internet: false
version: 1.0.0
tags: [curation, media, stock-solution, partonomy, culturemech, workflow]
---

# Add Media and Formulations (MediaIngredientMech)

## Overview

MediaIngredientMech curates individual chemical ingredients **and** multi-component
media, stock solutions, and complex mixtures that appear as named entries in
microbial growth recipes or phenotype/substrate datasets. Because CultureMech owns
full culturing recipe bodies while MediaIngredientMech owns ingredient identity,
grounding, roles, and partonomy, adding a medium or media ingredient to MIM
follows strict boundaries:

1. **Synonym vs. new record first** — If an existing MIM record already holds the
   target primary `identifier`, add the new surface form as a synonym on that
   record rather than creating a second YAML file on a held CURIE.
2. **Granularity and `ingredient_type`** — Classify the entry as `NAMED_MEDIUM`
   (a whole named medium formulation such as Marine agar 2216 or R2A agar),
   `STOCK_SOLUTION` (a defined pre-mix such as Wolfe's mineral mix or trace
   vitamin solution, paired with `solution_type`), `UNDEFINED_MIXTURE` (peptone,
   yeast extract, soil extract, or source-specific blend), or `SINGLE_INGREDIENT`.
3. **Identifier policy (`MAPPING_SEMANTICS.md` §3)** — Use an exact ontology CURIE
   (`MICRO:`, `FOODON:`, `ENVO:`, `CHEBI:`, `NCIT:`) when one denotes the exact
   formulation; otherwise mint `kgmicrobe.ingredient:<slug>` (for media, stock
   solutions, and complex preparations) or `kgmicrobe.compound:<slug>` (for pure
   compounds), or mint the next `UNMAPPED_NNNN` placeholder when the record must
   remain `UNMAPPED`. Never use a `CultureMech:NNNNNN` ID as a MIM `identifier`.
4. **Component partonomy (`components` + `component_assertion`)** — Decompose
   `NAMED_MEDIUM`, `STOCK_SOLUTION`, and `UNDEFINED_MIXTURE` records into
   `StockComponent` entries only from verifiable recipe or label evidence, and
   validate corpus-wide referential integrity with `just qc-component-partonomy`.
5. **Typed CultureMech linkage (`culturemech_reference`)** — Link to a CultureMech
   recipe by stable ID (`CultureMech:NNNNNN`) with an explicit
   `CultureMechRelationshipEnum` value (`EXACT_FORMULATION`, `VARIANT_OF`,
   `SIMILAR_COMPOSITION`, or `CANDIDATE_UNVERIFIED`) and composition-comparison
   prose in `evidence`.

---

## When to Use This Skill

| Trigger | Action |
|---|---|
| Adding a named growth medium, basal broth, or agar formulation used as an ingredient or substrate | Create or update a `NAMED_MEDIUM` or `UNDEFINED_MIXTURE` record with `kgmicrobe.ingredient:<slug>` (or exact `MICRO:`/`FOODON:` CURIE), `components`, `component_assertion`, and `culturemech_reference`. |
| Adding a pre-mixed mineral, vitamin, trace-metal, cofactor, or buffer stock | Create or update a `STOCK_SOLUTION` record with `solution_type`, `components`, and `component_assertion`. |
| Closing a CultureMech or MicrobeDecoder gap label | Check `docs/data/label_index.csv` first; either attach a `SYNONYM_ADDED` event to an existing record or mint a new record via `scripts/add_culturemech_gap_labels.py` / `scripts/create_records_from_groundings.py`. |
| Decomposing an existing medium or stock record into constituent ingredients | Add `components` and `component_assertion` and verify with `just qc-component-partonomy`. |

**Do not** use this skill for:
- Authoring a standalone culturing protocol with preparation steps, pH adjustments, or autoclaving instructions — those belong in CultureMech.
- Attaching `causal_graphs` to a `NAMED_MEDIUM` record — schema rules forbid `causal_graphs` on `NAMED_MEDIUM` because constituent records carry the mechanisms (`src/mediaingredientmech/schema/mediaingredientmech.yaml`).

---

## Workflow

### Step 1 — Pre-Flight: Search Existing Records & Prevent Duplicate Identifiers

Before creating any file in `data/ingredients/mapped/` or `data/ingredients/unmapped/`,
check whether the medium or ingredient is already represented by label, synonym,
or `identifier`:

```bash
# Search the generated label index for preferred terms and synonyms
grep -i "marine agar" docs/data/label_index.csv

# Check whether a candidate CURIE is already held by an active record
grep -rn "^identifier: kgmicrobe.ingredient:marine_agar_2216" data/ingredients/
```

- **If an active record already holds the target `identifier`:** Do **not** create
  a second YAML file (which would violate `mappings/duplicate_identifier_baseline.tsv`).
  Instead, add the new surface string to `synonyms:` on the existing record and
  append a `SYNONYM_ADDED` or `ADDED_SYNONYMS` event in `curation_history`.
- **If an unmapped record (`UNMAPPED_NNNN`) already exists for the medium:**
  Promote that file from `data/ingredients/unmapped/` to `data/ingredients/mapped/`
  following [`manage-identifiers`](../manage-identifiers/SKILL.md) rather than
  creating a duplicate file.

---

### Step 2 — Choose `identifier`, `ontology_mapping`, and `ingredient_type`

Follow `MAPPING_SEMANTICS.md` §3 and `src/mediaingredientmech/schema/mediaingredientmech.yaml`:

1. **Classification (`ingredient_type` and `solution_type`)**:
   - `NAMED_MEDIUM`: Whole named medium formulation or recipe (e.g., R2A agar, LB broth, Difco Marine Broth). Must **not** carry `causal_graphs`.
   - `STOCK_SOLUTION`: Pre-mixed solution of defined ingredients (e.g., ATCC Wolfe's mineral mix, trace vitamins solution). Also set `solution_type` (`VITAMIN_MIX`, `TRACE_METAL_MIX`, `AMINO_ACID_MIX`, `BUFFER_SOLUTION`, `CARBON_SOURCE_MIX`, `MINERAL_STOCK`, `COFACTOR_MIX`, `COMPLEX_UNDEFINED`, or `OTHER`).
   - `UNDEFINED_MIXTURE`: Complex mixture or source-specific blend with variable/undefined composition (e.g., peptone, yeast extract, or a multi-component medium treated as an undefined mixture).
   - `SINGLE_INGREDIENT`: Single chemical substance.

2. **Primary `identifier` & `ontology_mapping`**:
   - **Exact ontology term exists**: Use `CHEBI:`, `FOODON:`, `MICRO:`, `ENVO:`, or `NCIT:` as `identifier` and `ontology_mapping.ontology_id` with `mapping_quality: EXACT_MATCH` (or `SYNONYM_MATCH` / `CAS_RN_LOOKUP`). Do **not** map a specific numbered formulation (e.g., Marine Agar 2216) to a merely similar `MICRO:` term unless composition equivalence is verified.
   - **Named medium, stock solution, or complex preparation with no exact ontology term**: Mint `kgmicrobe.ingredient:<slug>` (lowercase, underscore-separated ASCII slug matching the file stem):
     ```yaml
     identifier: kgmicrobe.ingredient:atcc_wolfes_mineral_mix
     preferred_term: ATCC Wolfe's mineral mix
     mapping_status: MAPPED
     ingredient_type: STOCK_SOLUTION
     solution_type: MINERAL_STOCK
     ontology_mapping:
       ontology_id: kgmicrobe.ingredient:atcc_wolfes_mineral_mix
       ontology_label: ATCC Wolfe's mineral mix
       ontology_source: kgmicrobe.ingredient
       mapping_quality: FALLBACK_REGISTRY
       evidence:
       - evidence_type: MANUAL_CURATION
         source: MIM curation
         notes: Named multi-component mineral stock solution; minted under kgmicrobe.ingredient because no single CHEBI/FOODON/MICRO term denotes this exact preparation.
     ```
   - **Broader ontology parent exists (`skos:broadMatch`)**: If anchoring the record to a broader parent term in `ontology_mapping.ontology_id` (`mapping_quality: BROAD_MATCH` or `NARROW_MATCH`), keep `identifier: kgmicrobe.ingredient:<slug>` (or `cas:<rn>`) and ensure `mappings/ingredient_mappings.sssom.tsv` includes **both** the `skos:broadMatch` row to the OBO parent and the mandatory Rule B1 `skos:exactMatch` registry sibling row to `kgmicrobe.ingredient:<slug>`.
   - **Unresolvable / awaiting expert curation**: Mint the next sequential `UNMAPPED_NNNN` placeholder (see [`manage-identifiers`](../manage-identifiers/SKILL.md)), set `mapping_status: UNMAPPED`, and place the file in `data/ingredients/unmapped/<Slug>.yaml`. <!-- refcheck: ignore -->

---

### Step 3 — Populate Component Partonomy (`components` + `component_assertion`)

When verifiable constituent information exists for a `NAMED_MEDIUM`,
`STOCK_SOLUTION`, or `UNDEFINED_MIXTURE`, populate `components` and
`component_assertion`. Both slots are governed by bidirectional schema rules and
`src/mediaingredientmech/validation/component_partonomy.py`:

- **Invariants enforced by `just qc-component-partonomy`**:
  1. `components` requires `component_assertion` (`MISSING_ASSERTION`), and `component_assertion` is forbidden when `components` is empty (`ORPHAN_ASSERTION`).
  2. `ingredient_type` **must** be one of `NAMED_MEDIUM`, `STOCK_SOLUTION`, or `UNDEFINED_MIXTURE` (`INVALID_PARENT_TYPE`).
  3. Every `StockComponent` requires `component_name` and `reference_scope` (`MIM_CATALOG`, `EXTERNAL_TERM`, or `UNMAPPED`).
  4. When `reference_scope: MIM_CATALOG`, `component_id` must be the `identifier` of an active (non-`REJECTED`) MIM record, and `component_name` (case- and whitespace-normalized) **must** match that target record's `preferred_term`, `ontology_mapping.ontology_label`, or one of its `synonyms[].synonym_text` values (`UNRESOLVED_MIM_REFERENCE`, `REFERENCE_LABEL_MISMATCH`).
  5. When `reference_scope: EXTERNAL_TERM`, `component_id` must be a valid CURIE that is **not** currently held by any active MIM record (`STALE_EXTERNAL_SCOPE`).
  6. When `reference_scope: UNMAPPED`, `component_id` must be omitted (`UNMAPPED_WITH_ID`).
  7. A record cannot reference its own `identifier` or parent labels as a component (`SELF_REFERENCE`, `SELF_REFERENCE_NAME`), nor repeat `component_id` or `component_name` within the same `components` list (`DUPLICATE_COMPONENT_ID`, `DUPLICATE_COMPONENT_NAME`).
  8. `concentration_value` and `concentration_unit` must either both be present or both be omitted (`INCOMPLETE_CONCENTRATION`).

Example (`data/ingredients/mapped/Marine_agar_2216.yaml` pattern):

```yaml
components:
- component_name: Peptone
  component_id: MICRO:0000178
  reference_scope: MIM_CATALOG
  concentration_value: '5.0'
  concentration_unit: G_PER_L
- component_name: Yeast Extract
  component_id: FOODON:03315426
  reference_scope: MIM_CATALOG
  concentration_value: '1.0'
  concentration_unit: G_PER_L
- component_name: Sodium Chloride
  component_id: CHEBI:26710
  reference_scope: MIM_CATALOG
  concentration_value: '19.45'
  concentration_unit: G_PER_L
- component_name: Agar
  component_id: CHEBI:2509
  reference_scope: MIM_CATALOG
  concentration_value: '15.0'
  concentration_unit: G_PER_L
- component_name: Distilled water
  component_id: CHEBI:15377
  reference_scope: MIM_CATALOG
  concentration_value: '1.0'
  concentration_unit: L_PER_L
component_assertion:
  method: RECIPE_TRANSCRIPTION
  completeness: COMPLETE
  evidence:
  - evidence_type: RECIPE_SOURCE
    source: https://www.atcc.org/~/media/5a4142bda5cf458b9131902a1791833d.ashx
    source_record: ATCC Medium 2887 Marine Agar/Broth 2216
    notes: ATCC Medium 2887 lists the Difco Marine Agar 2216 formula with per-liter quantities.
```

Allowed enum values (`src/mediaingredientmech/schema/mediaingredientmech.yaml`):
- `component_assertion.method`: `LABEL_ENUMERATION`, `ABBREVIATION_EXPANSION`, `CURATED_INTERPRETATION`, `RECIPE_TRANSCRIPTION`
- `component_assertion.completeness`: `COMPLETE`, `PARTIAL`, `UNKNOWN`
- `component_assertion.evidence[].evidence_type`: `SOURCE_LABEL`, `CURATED_DATASET`, `MANUAL_CURATION`, `RECIPE_SOURCE`, `PUBLICATION`

---

### Step 4 — Link to CultureMech (`culturemech_reference`) & Occurrence Stats

When a MIM medium or stock record corresponds to a recipe in CultureMech:

1. **Never use `CultureMech:NNNNNN` as the MIM `identifier`.**
2. **Use `culturemech_reference`** (`CultureMechReference`) to record a typed link
   verified by composition (see `data/ingredients/mapped/GYPS.yaml` and
   `data/ingredients/mapped/BHI.yaml`):
   ```yaml
   culturemech_reference:
     medium_id: CultureMech:002799
     medium_name: gyps_medium
     relationship: SIMILAR_COMPOSITION
     source_path: data/normalized_yaml/bacterial/gyps_medium.yaml
     evidence: Compared source-specific formulation with CultureMech:002799; both specify glucose 5 g/L, yeast extract 0.5 g/L, peptone 1 g/L, and sea salts 30 g/L, while differing in buffer and sulfur addition.
   ```
   - `relationship` values:
     - `EXACT_FORMULATION`: Asserted **only** when constituent composition and quantities were compared and match.
     - `VARIANT_OF`: Documented modification/variant of the target recipe.
     - `SIMILAR_COMPOSITION`: Substantial overlap with specific differences documented in `evidence`.
     - `CANDIDATE_UNVERIFIED`: Candidate recipe link recorded when composition comparison cannot yet be completed.
3. **Occurrence statistics (`occurrence_statistics`)**:
   - Set `total_occurrences` and `media_count` (0 if sourced only from non-CultureMech datasets, with upstream counts placed under `source_occurrences`).
   - When refreshing CultureMech recipe membership across the corpus from a CultureMech checkout's `ingredient_occurrences.tsv`, run:
     ```bash
     just build-membership
     ```

---

### Step 5 — Write Through the Guarded Curation Path

Always write individual records via `write_validated_ingredient` and record a
`CurationEvent` via `record_curation_event` from
`src/mediaingredientmech/curation/ingredient_curator.py` (which validates against
`IngredientRecord` in `src/mediaingredientmech/schema/mediaingredientmech.yaml`
before touching disk and preserves field ordering with `sort_keys=False`):

```python
from pathlib import Path
from mediaingredientmech.curation.ingredient_curator import (
    record_curation_event,
    write_validated_ingredient,
)

record = {
    "identifier": "kgmicrobe.ingredient:example_medium",
    "preferred_term": "Example medium",
    "mapping_status": "MAPPED",
    "ingredient_type": "NAMED_MEDIUM",
    "ontology_mapping": {
        "ontology_id": "kgmicrobe.ingredient:example_medium",
        "ontology_label": "Example medium",
        "ontology_source": "kgmicrobe.ingredient",
        "mapping_quality": "FALLBACK_REGISTRY",
        "evidence": [
            {
                "evidence_type": "MANUAL_CURATION",
                "source": "MIM curation",
                "notes": "Named medium formulation minted under kgmicrobe.ingredient.",
            }
        ],
    },
    "synonyms": [
        {
            "synonym_text": "Example medium",
            "synonym_type": "RAW_TEXT",
            "source": "culturemech",
        }
    ],
    "occurrence_statistics": {
        "total_occurrences": 1,
        "media_count": 1,
    },
    "curation_history": [],
}

record_curation_event(
    record,
    curator="add-media",
    action="CREATED",
    changes="Created NAMED_MEDIUM record for Example medium.",
    new_status="MAPPED",
    llm_assisted=True,
)

write_validated_ingredient(
    Path("data/ingredients/mapped/Example_Medium.yaml"),  # <!-- refcheck: ignore -->
    record,
)
```

For batch creation from reviewed TSV groundings or CultureMech gap tables, use the
existing guarded scripts instead of ad-hoc writers:
- `scripts/create_records_from_groundings.py` (`--groundings`, `--candidates`, `--curator`, `--action`, `--dry-run`)
- `scripts/add_culturemech_gap_labels.py` (`--occurrences`, `--dry-run`)

---

### Step 6 — Synchronize Derived Surfaces, SSSOM, and Run QC

Every record addition or modification in `data/ingredients/{mapped,unmapped}/`
must be synchronized across the monoliths, SSSOM mapping table, indexes, and
browser surfaces before committing:

```bash
# 1. Rebuild data/curated/{mapped,unmapped}_ingredients.yaml from data/ingredients/
just sync-curated

# 2. Validate component partonomy across the synced curated collections
just qc-component-partonomy

# 3. Export label/synonym indexes, lists, browser JSON, and visualizations
just export-indexes
just export-lists
just export-browser
just generate-visualizations

# 4. If mappings/ingredient_mappings.sssom.tsv changed, bump its version header
just bump-sssom-header

# 5. Run strict schema, product, and full repository QC gates
just validate-strict
just validate-products
just qc
```

If you edited or added agent skill documentation under `.claude/skills/`, also run:

```bash
just check-instruction-refs
```

---

## Anti-Patterns

- **Never use `CultureMech:NNNNNN` as `identifier` or `ontology_mapping.ontology_id`.** CultureMech IDs belong in `culturemech_reference.medium_id` or in evidence notes.
- **Never create a second record for an already-held `identifier`.** Check `docs/data/label_index.csv` and `data/ingredients/` first; add a synonym to the existing record instead.
- **Never populate `components` without `component_assertion`**, or on a `SINGLE_INGREDIENT` record (`just qc-component-partonomy` will exit 2).
- **Never set `reference_scope: MIM_CATALOG` unless `component_id` resolves to an active MIM record AND `component_name` matches one of that record's recognized labels/synonyms.**
- **Never attach `causal_graphs` to a `NAMED_MEDIUM` record.** Mechanisms live on the constituent ingredient records.
- **Never assert `relationship: EXACT_FORMULATION` in `culturemech_reference` from a name match alone.** Compare the constituent list and concentrations first, or use `CANDIDATE_UNVERIFIED` / `SIMILAR_COMPOSITION`.

---

## Related Skills

- [`manage-identifiers`](../manage-identifiers/SKILL.md) — Primary `identifier` policy, `kgmicrobe.*` vs. ontology CURIEs, and `UNMAPPED_NNNN` minting/promotion.
- [`map-media-ingredients`](../map-media-ingredients/SKILL.md) — Ontology search and grounding workflow across ChEBI, FOODON, MICRO, ENVO, and NCIT.
- [`curate-yaml-record`](../curate-yaml-record/SKILL.md) — Guarded YAML editing, `write_validated_ingredient`, and surface synchronization.
- [`merge-ingredients`](../merge-ingredients/SKILL.md) — Consolidating duplicate ingredient records and updating `mappings/mim_curie_aliases.tsv`.
- [`ingredient-roles`](../ingredient-roles/SKILL.md) — Assigning `nutritional_roles`, `physicochemical_roles`, and `cellular_metabolic_roles`.
