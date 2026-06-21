# KG-Microbe / CultureMech Integration

*Reference for the **map-media-ingredients** skill — see [`../skill.md`](../skill.md) for the overview, normalization rules, strategy levels, and workflows.*

---

## KG-Microbe Integration

MediaIngredientMech integrates with **CultureMech** (primary integration point) for KG-Microbe knowledge graph construction.

### Data Flow

```
CultureMech → MediaIngredientMech (curate) → Export back to CultureMech
```

### Import from CultureMech

```bash
# Import ingredients from CultureMech
python scripts/import_from_culturemech.py \
  --culturemech-dir /path/to/CultureMech/data \
  --output data/ingredients
```

### Export to CultureMech

```bash
# Export curated mappings back
python scripts/export_to_culturemech.py \
  --input data/ingredients/mapped \
  --output /path/to/CultureMech/data/ingredients
```

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
