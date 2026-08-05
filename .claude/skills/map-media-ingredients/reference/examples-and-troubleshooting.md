# Worked Examples & Troubleshooting

*Reference for the **map-media-ingredients** skill — see [`../SKILL.md`](../SKILL.md) for the overview, normalization rules, strategy levels, and workflows.*

---

## Examples

### Example 1: Simple Chemical with Hydrate

**Input**: `MgSO4•7H2O`

**Process**:
1. Normalize: Strip hydrate → `MgSO4` — **to find the family, not to decide the mapping**
2. Map formula to name: `MgSO4` → `magnesium sulfate`
3. Search CHEBI for the family, then **look for the hydration state you actually have**:
   `magnesium sulfate heptahydrate` → `CHEBI:31795`
4. Accept `CHEBI:31795` with quality `EXACT_MATCH`
5. Save original `MgSO4•7H2O` as synonym type `HYDRATE_FORM`

**Result**:
```yaml
ontology_id: CHEBI:31795
ontology_label: magnesium sulfate heptahydrate
ontology_source: CHEBI
quality: EXACT_MATCH
synonyms:
  - name: MgSO4•7H2O
    type: HYDRATE_FORM
```

> ⚠️ **Do not stop at `CHEBI:32599 magnesium sulfate`.** That is the *anhydrous*
> term, 120.37 g/mol against the heptahydrate's 246.47 — the number a recipe
> depends on. Grounding a hydrate onto its anhydrous parent is the identity
> collapse that produced the families tracked in #218/#225.
>
> **If no hydrate-specific term exists**, the record takes its own
> `cas:<hydrate CAS>` identifier with a `skos:narrowMatch` to the anhydrous
> parent plus the Rule B1 registry row — see MAPPING_SEMANTICS.md Section 3.
> `just report-hydrate-grounding` lists the records still in violation.

### Example 2: Incomplete Formula

**Input**: `K2HPO`

**Process**:
1. Normalize: Fix incomplete formula → `K2HPO4`
2. Map to name: `K2HPO4` → `dipotassium phosphate`
3. Search CHEBI: Find `CHEBI:131527`
4. Accept with quality `SYNONYM_MATCH`
5. Save `K2HPO` as synonym type `INCOMPLETE_FORMULA`

### Example 3: Biological Extract

**Input**: `Yeast extract`

**Process**:
1. No chemical normalization needed
2. Search CHEBI: No good match
3. Search FOODON: Find `FOODON:03411448` (yeast extract)
4. Accept with quality `EXACT_MATCH`

**Why FOODON?** Yeast extract is a biological preparation, not a pure chemical compound.

### Example 4: Environmental Sample

**Input**: `Soil extract`

**Process**:
1. Search CHEBI: No match
2. Search FOODON: No specific match
3. Search ENVO: Find `ENVO:02000034` (soil extract)
4. Accept with quality `EXACT_MATCH`

### Example 5: Complex Mixture (Unmappable)

**Input**: `Vitamin solution A (per source)`

**Process**:
1. Categorize as `COMPLEX_MIXTURE`
2. Search fails: Too generic, composition varies
3. Mark as **unmappable** with status `NEEDS_EXPERT`
4. Rationale: Composition not specified, varies by source

**Best practice**: Document in notes that this should reference source formulation.


---

## Troubleshooting

### No Matches Found

**Problem**: Search returns no results

**Solutions**:
1. Try normalized variants: Use `generate_search_variants()`
2. Check spelling: Common vs British English (sulfate vs sulphate)
3. Try alternative ontologies: CHEBI → FOODON → ENVO
4. Use fuzzy search: OAK `l~` prefix or OLS API
5. Search formula instead of name: "MgSO4" instead of "magnesium sulfate"

### Too Many Matches

**Problem**: Search returns many low-quality matches

**Solutions**:
1. Use more specific term: "D-glucose" instead of "glucose"
2. Include chemical context: "potassium phosphate dibasic" instead of "potassium phosphate"
3. Filter by score: Only consider matches with score ≥ 0.7
4. Use exact match first: Try `basic_search()` before fuzzy search

### Ambiguous Results

**Problem**: Multiple equally good matches

**Solutions**:
1. Check ontology definitions: Read term descriptions
2. Consider biological context: What organisms/media use this?
3. Use most specific term: Species-level over genus-level
4. Mark `NEEDS_EXPERT` if truly ambiguous

### Complex Mixture

**Problem**: Ingredient is a mixture of unknown composition

**Solutions**:
1. Check if composition is defined elsewhere in dataset
2. Search for mixture as a whole (e.g., "Hoagland solution")
3. If composition unknown, mark as **unmappable**
4. Document in notes: "Composition varies by source"

