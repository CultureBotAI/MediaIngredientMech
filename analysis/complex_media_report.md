# Complex Media Detection Report

**Generated**: 2026-08-25 01:34:53
**Data source**: data/curated/mapped_ingredients.yaml
**Total records loaded**: 2566
**Records eligible and analyzed**: 122

## Summary

- **High confidence complex media**: 0
- **Medium confidence complex media**: 0
- **Total suspected complex media**: 0
- **Single ingredients**: 0
- **Uncertain**: 122

## Recommendations

### Immediate Actions

1. **Review high-confidence entries** - These should likely be reclassified as `DEFINED_MEDIUM`
2. **Check CHEBI mappings** - Complex media should not be mapped to pure chemical CHEBI terms
3. **Cross-reference CultureMech** - Find full recipe formulations for these media

### Review Steps

```bash
# Produce the read-only detection report
python scripts/identify_complex_media.py

# Cross-reference with CultureMech
python scripts/cross_reference_culturemech.py --complex-media-only
```

Apply any accepted correction through a current validated curation workflow; the detector does not mutate records.

## Special Cases Requiring Expert Review
