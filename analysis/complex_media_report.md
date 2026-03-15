# Complex Media Detection Report

**Generated**: 2026-03-14 19:03:49
**Data source**: data/curated/mapped_ingredients.yaml
**Total records analyzed**: 995

## Summary

- **High confidence complex media**: 0
- **Medium confidence complex media**: 0
- **Total suspected complex media**: 0
- **Single ingredients**: 1
- **Uncertain**: 496

## Recommendations

### Immediate Actions

1. **Review high-confidence entries** - These should likely be reclassified as `DEFINED_MEDIUM`
2. **Check CHEBI mappings** - Complex media should not be mapped to pure chemical CHEBI terms
3. **Cross-reference CultureMech** - Find full recipe formulations for these media

### Reclassification Steps

```bash
# Interactive review
python scripts/identify_complex_media.py --interactive

# Auto-reclassify high confidence (dry run first)
python scripts/identify_complex_media.py --auto-reclassify --dry-run

# Cross-reference with CultureMech
python scripts/cross_reference_culturemech.py --complex-media-only
```

## Special Cases Requiring Expert Review
