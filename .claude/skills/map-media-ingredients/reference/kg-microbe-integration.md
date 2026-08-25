# KG-Microbe / CultureMech Integration

*Reference for the **map-media-ingredients** skill — see [`../SKILL.md`](../SKILL.md) for the overview, normalization rules, strategy levels, and workflows.*

---

## KG-Microbe Integration

MediaIngredientMech integrates with **CultureMech** (primary integration point) for KG-Microbe knowledge graph construction.

### Data Flow

```
CultureMech → compare/review in MediaIngredientMech → publish MIM artifacts
```

### Inbound updates from CultureMech

There is no supported bulk importer. The legacy entry point is fail-closed
because it overwrote MIM-owned curation with a lossy aggregate projection
(MediaIngredientMech#453). Treat CultureMech output as comparison input, then
apply reviewed changes through focused MIM curation workflows. Stable recipe
references and lossless occurrence edges are tracked in #447 and #449.

### Outbound updates

No supported direct CultureMech exporter exists in this repository. Publish the
normal validated MIM products, and treat any CultureMech update as a separate,
reviewed downstream change with explicit provenance.

### Check Existing Ingredients

Before creating new mappings, check if ingredient already exists in KG-Microbe:

```python
# Search for existing ingredient entities
# Pattern: mediadive.ingredient:*
# Check media_dive_ingredients in CultureMech data

# If found, use existing ID instead of creating duplicate
```

### Link to Media and Organisms

Ingredients in KG-Microbe are linked via:
- **has_part**: Medium → Ingredient relationships
- **Growth requirements**: Organism → Medium → Ingredients
- **Frequency analysis**: How often ingredient appears across media
