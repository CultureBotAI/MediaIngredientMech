# Merge Decision Flowchart

Visual guide for deciding whether to merge two ingredient records.

---

## Quick Decision Tree

```
START: Should I merge Record A and Record B?
│
├─ Do they have the same CHEBI ID?
│  ├─ NO ──> ❌ STOP - Don't merge
│  └─ YES ──> Continue ↓
│
├─ Do they have the same ingredient_type (or both unset)?
│  ├─ NO ──> ❌ STOP - Don't merge
│  └─ YES ──> Continue ↓
│
├─ Is either record a DEFINED_MEDIUM?
│  ├─ YES ──> ❌ STOP - Don't merge
│  └─ NO ──> Continue ↓
│
├─ Run detect_complex_medium() on both:
│  │
│  ├─ Either is complex media (conf >= 0.75)?
│  │  ├─ YES ──> ❌ STOP - Don't merge
│  │  └─ NO ──> Continue ↓
│  │
│  └─ Pattern classification:
│     │
│     ├─ Case variation only?
│     │  └─ ✅ SAFE TO MERGE
│     │
│     ├─ Chemical synonyms (same formula/abbreviation)?
│     │  └─ ✅ SAFE TO MERGE
│     │
│     ├─ Abbreviation + full name?
│     │  └─ ✅ SAFE TO MERGE
│     │
│     ├─ Hydrate variants?
│     │  └─ ⚠️ FLAG FOR REVIEW (consider hierarchy)
│     │
│     ├─ Stereoisomers (D/L prefix)?
│     │  └─ ⚠️ FLAG FOR REVIEW (consider hierarchy)
│     │
│     └─ Unclear pattern?
│        └─ ⚠️ FLAG FOR MANUAL REVIEW
```

---

## Detailed Flow with Examples

### Phase 1: Prerequisites

```
┌─────────────────────────────────────────────────────┐
│  Check 1: Same Ontology ID                         │
│                                                     │
│  ✓ NaCl (CHEBI:26710) + sodium chloride (CHEBI:26710) │
│  ✗ Glucose (CHEBI:17634) + Fructose (CHEBI:28645) │
└─────────────────────────────────────────────────────┘
                         │
                    PASS │ FAIL → STOP
                         ▼
┌─────────────────────────────────────────────────────┐
│  Check 2: Compatible ingredient_type                │
│                                                     │
│  ✓ Both SINGLE_INGREDIENT                          │
│  ✓ Both unset                                       │
│  ✗ SINGLE_INGREDIENT vs DEFINED_MEDIUM             │
└─────────────────────────────────────────────────────┘
                         │
                    PASS │ FAIL → STOP
                         ▼
```

### Phase 2: Complex Media Detection

```
┌─────────────────────────────────────────────────────┐
│  Check 3: detect_complex_medium() on Record A      │
│                                                     │
│  Input: "Agar" (CHEBI:2509)                        │
│  Result: is_complex=False, conf=0.0                │
│  Status: ✓ PASS                                     │
└─────────────────────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────┐
│  Check 4: detect_complex_medium() on Record B      │
│                                                     │
│  Input: "R2A agar" (CHEBI:2509)                    │
│  Result: is_complex=True, conf=0.95                │
│         reason="Known medium name: R2A agar"       │
│  Status: ✗ FAIL → STOP                             │
└─────────────────────────────────────────────────────┘
         │                           │
    PASS │                      FAIL │ → STOP (Don't merge)
         ▼
```

### Phase 3: Pattern Matching

```
┌─────────────────────────────────────────────────────┐
│  Pattern 1: Case Variation                         │
│                                                     │
│  Compare: "Folic acid" vs "folic acid"             │
│  Normalized: "folic acid" == "folic acid"          │
│  Decision: ✅ MERGE (100% safe)                     │
└─────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────┐
│  Pattern 2: Chemical Synonyms                      │
│                                                     │
│  Compare: "NaCl" vs "sodium chloride"              │
│  Analysis: Formula + systematic name               │
│  Shared CHEBI: ✓                                    │
│  Decision: ✅ MERGE (90% safe)                      │
└─────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────┐
│  Pattern 3: Hydrate Variant                        │
│                                                     │
│  Compare: "CaCl2" vs "CaCl2·2H2O"                  │
│  Analysis: Different hydration states              │
│  Decision: ⚠️ REVIEW (may need hierarchy)          │
└─────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────┐
│  Pattern 4: Stereoisomers                          │
│                                                     │
│  Compare: "Biotin" vs "D-biotin"                   │
│  Analysis: Stereochemistry difference              │
│  Decision: ⚠️ REVIEW (may need hierarchy)          │
└─────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────┐
│  Pattern 5: Unclear                                │
│                                                     │
│  Compare: "Nicotinic acid" vs "niacin"             │
│  Analysis: No clear pattern detected               │
│  Decision: ⚠️ MANUAL REVIEW                        │
└─────────────────────────────────────────────────────┘
```

---

## Color-Coded Decision Guide

🟢 **GREEN - Safe to Merge**
- Case variations (Water/water/WATER)
- Chemical synonyms (NaCl/sodium chloride)
- Abbreviations (H2O/water)

🟡 **YELLOW - Needs Review**
- Hydrate variants (MgSO4/MgSO4·7H2O)
- Stereoisomers (biotin/D-biotin)
- Unclear patterns (requires expert judgment)

🔴 **RED - Do NOT Merge**
- Complex media detected (R2A agar ≠ Agar)
- Different ingredient_type
- Different CHEBI IDs

---

## Common Mistakes to Avoid

### ❌ Mistake 1: CHEBI ID Matching Only

**What happened:**
```
Agar (CHEBI:2509)
├─ agar ✓
├─ R2A agar ✗ (this is a defined medium!)
├─ Marine agar 2216 ✗ (this is a defined medium!)
└─ Oatmeal agar ✗ (this is a defined medium!)
```

**Why it's wrong:** Same CHEBI doesn't mean same thing when one is a recipe

**Prevention:** Always run complex media detection

### ❌ Mistake 2: Ignoring Stereochemistry

**What happened:**
```
Biotin (parent)
└─ D-biotin ✗ (specific stereoisomer)
```

**Why it's wrong:** D-biotin and L-biotin have different biological activity

**Prevention:** Check for D/L prefixes, use hierarchy instead

### ❌ Mistake 3: Merging Water Variants

**What happened:**
```
Water (general)
├─ tap water ✗ (contains minerals)
├─ distilled water ✗ (purified)
└─ double distilled water ✗ (ultra-pure)
```

**Why it's wrong:** Different purity levels affect media composition

**Prevention:** Purity qualifiers indicate variants, use hierarchy

---

## Quick Reference Table

| Pattern | Example | Decision | Rationale |
|---------|---------|----------|-----------|
| Case only | Water / water | ✅ MERGE | Identical except capitalization |
| Chemical synonym | NaCl / sodium chloride | ✅ MERGE | Same chemical, different names |
| Abbreviation | H2O / water | ✅ MERGE | Standard abbreviation |
| Hydrate | CaCl2 / CaCl2·2H2O | ⚠️ REVIEW | Different molecular weight |
| Stereoisomer | biotin / D-biotin | ⚠️ REVIEW | Different chirality |
| Purity level | water / distilled water | ⚠️ REVIEW | Different purity |
| Complex media | agar / R2A agar | ❌ STOP | Recipe vs ingredient |
| Different type | SINGLE vs DEFINED | ❌ STOP | Different categories |
| Different CHEBI | glucose / fructose | ❌ STOP | Different chemicals |

---

## Implementation Checklist

When implementing merge logic, ensure:

- [ ] CHEBI ID matching (necessary but not sufficient)
- [ ] ingredient_type consistency check
- [ ] Complex media detection via `detect_complex_medium()`
- [ ] Pattern classification (case/synonym/abbreviation/etc.)
- [ ] Confidence thresholds (0.75 for complex media blocking)
- [ ] Manual review flagging for unclear cases
- [ ] Audit trail with merge reason documentation
- [ ] Post-merge validation script

---

**See Also:**
- `docs/MERGE_CURATION_GUIDE.md` - Detailed curation rules
- `analysis/merge_pattern_analysis.md` - Real data analysis
- `scripts/identify_complex_media.py` - Detection algorithm
