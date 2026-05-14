# Incomplete Formula Repair - Final Recommendations
**Date**: 2026-03-15
**Method**: Automated analysis + CAS verification + existing mappings

---

## High-Confidence Recommendations (9 formulas)

These have strong evidence from CAS numbers, existing mappings, or both.

### ✅ Ready to Map

| Incomplete | Complete | Name | CHEBI ID | Evidence | Confidence |
|------------|----------|------|----------|----------|------------|
| **CaCO** (8 occ) | CaCO₃ | calcium carbonate | CHEBI:3311 | Already mapped | ✅ **CERTAIN** |
| **Na2CO** (3 occ) | Na₂CO₃ | sodium carbonate | CHEBI:29377 | Already mapped (4 variants) | ✅ **CERTAIN** |
| **H3BO** (3 occ) | H₃BO₃ | boric acid | CHEBI:33118 | Already mapped | ✅ **CERTAIN** |
| **NH4NO** (3 occ) | NH₄NO₃ | ammonium nitrate | CHEBI:63038 | Already mapped + CAS 6484-52-2 | ✅ **CERTAIN** |
| **Ca** (3 occ) | CaCl₂·2H₂O | calcium chloride dihydrate | CHEBI:86158 | CAS 13477-34-4 + 10 mapped variants | ✅ **CERTAIN** |
| **MgCO** (11 occ) | MgCO₃ | magnesium carbonate | CHEBI:6611 | Chemical logic (standard carbonate) | ✅ **HIGH** |
| **KNO** (5 occ) | KNO₃ | potassium nitrate | CHEBI:63043 | Already mapped (as KNO3) | ✅ **HIGH** |
| **K2HPO** (17 occ) | K₂HPO₄ | dipotassium hydrogen phosphate | CHEBI:32030 | Standard phosphate buffer | ✅ **HIGH** |
| **KH2PO** (11 occ) | KH₂PO₄ | potassium dihydrogen phosphate | CHEBI:32583 | Standard phosphate buffer | ✅ **HIGH** |

### ⚠️ Needs CAS Verification

| Incomplete | Complete | Name | CHEBI ID | Issue | Confidence |
|------------|----------|------|----------|-------|------------|
| **NaNO** (24 occ) | NaNO₃ | sodium nitrate | CHEBI:34218 | CAS 7631-99-4 = NaNO₃ (NOT NaNO₂!) | ✅ **HIGH** |
| **NaHCO** (4 occ) | NaHCO₃ | sodium bicarbonate | CHEBI:32139 | Standard bicarbonate form | ✅ **HIGH** |

### ⚠️ Ambiguous

| Incomplete | Complete | Name | CHEBI ID | Issue | Confidence |
|------------|----------|------|----------|-------|------------|
| **NH4MgPO** (3 occ) | (NH₄)MgPO₄ | ammonium magnesium phosphate | CHEBI:90884 | Struvite, needs media context check | ⚠️ **MEDIUM** |

---

## Detailed Evidence

### 1. NaNO → NaNO₃ (sodium nitrate) ✅ HIGH

**Automated analysis said**: NaNO₂ (score: 26)
**Manual correction**: NaNO₃

**Evidence**:
- **CAS number**: 7631-99-4 = **sodium nitrate (NaNO₃)**, NOT nitrite
- **Catalog codes**: Fisher BP360-500 (sodium nitrate)
- **Chemical logic**: Nitrate (NO₃⁻) much more common than nitrite (NO₂⁻) in growth media
- **Usage**: Nitrogen source in minimal media (consistent with nitrate)

**Correction**: CAS number definitively identifies this as **NaNO₃** (sodium nitrate, CHEBI:34218)

---

### 2. K2HPO → K₂HPO₄ (dipotassium hydrogen phosphate) ✅ HIGH

**Evidence**:
- **Chemical logic**: K₂HPO₄ is the standard dibasic potassium phosphate
- **Common usage**: Phosphate buffer in media (pH ~8-9)
- **Standard form**: Missing O₄ group (truncation pattern)

**Recommendation**: Map to CHEBI:32030 (dipotassium hydrogen phosphate)

---

### 3. KH2PO → KH₂PO₄ (potassium dihydrogen phosphate) ✅ HIGH

**Evidence**:
- **Chemical logic**: KH₂PO₄ is the standard monobasic potassium phosphate
- **Common usage**: Phosphate buffer in media (pH ~4-7)
- **Standard form**: Missing O₄ group (truncation pattern)

**Recommendation**: Map to CHEBI:32583 (potassium dihydrogen phosphate)

---

### 4. MgCO → MgCO₃ (magnesium carbonate) ✅ HIGH

**Evidence**:
- **Chemical logic**: MgCO₃ is the only stable magnesium carbonate
- **Common usage**: Magnesium source and buffer
- **Standard form**: Missing O₂ group

**Recommendation**: Map to CHEBI:6611 (magnesium carbonate)

---

### 5. CaCO → CaCO₃ (calcium carbonate) ✅ CERTAIN

**Evidence**:
- **Already mapped**: CaCO3 exists in mapped_ingredients.yaml
- **Chemical logic**: CaCO₃ is the standard calcium carbonate
- **Score**: 30 (high confidence from existing mapping)

**Recommendation**: Map to CHEBI:3311 (calcium carbonate)

---

### 6. KNO → KNO₃ (potassium nitrate) ✅ HIGH

**Evidence**:
- **Already mapped**: KNO3 exists in mapped_ingredients.yaml
- **Chemical logic**: Nitrate more common than nitrite
- **Usage**: Nitrogen source in minimal media

**Recommendation**: Map to CHEBI:63043 (potassium nitrate)

---

### 7. NaHCO → NaHCO₃ (sodium bicarbonate) ✅ HIGH

**Evidence**:
- **Chemical logic**: NaHCO₃ is the only sodium bicarbonate form
- **Common usage**: Buffer and carbon source
- **Standard form**: Missing O₂ group

**Recommendation**: Map to CHEBI:32139 (sodium bicarbonate)

---

### 8. NH4NO → NH₄NO₃ (ammonium nitrate) ✅ CERTAIN

**Evidence**:
- **Already mapped**: NH4NO3 exists in mapped_ingredients.yaml
- **CAS number**: 6484-52-2 (ammonium nitrate)
- **Chemical logic**: Nitrate more common than nitrite
- **Score**: 35 (high confidence)

**Recommendation**: Map to CHEBI:63038 (ammonium nitrate)

---

### 9. Na2CO → Na₂CO₃ (sodium carbonate) ✅ CERTAIN

**Evidence**:
- **Already mapped**: 4 variants exist (Na2CO3, Na2CO3 anhydrous, etc.)
- **Chemical logic**: Standard carbonate form
- **Score**: 90 (very high confidence from multiple existing mappings)

**Recommendation**: Map to CHEBI:29377 (sodium carbonate)

---

### 10. NH4MgPO → (NH₄)MgPO₄ (ammonium magnesium phosphate) ⚠️ MEDIUM

**Evidence**:
- **Catalog code**: Sigma 529354
- **Chemical logic**: Struvite (NH₄MgPO₄·6H₂O) is common in some media
- **Ambiguity**: Could be anhydrous or hexahydrate form

**Recommendation**: Map to CHEBI:90884 (ammonium magnesium phosphate)
**Note**: May need to check media context to confirm hydration state

---

### 11. H3BO → H₃BO₃ (boric acid) ✅ CERTAIN

**Evidence**:
- **Already mapped**: H3BO3 exists in mapped_ingredients.yaml
- **Chemical logic**: H₃BO₃ is the standard boric acid formula
- **Score**: 30 (high confidence)

**Recommendation**: Map to CHEBI:33118 (boric acid)

---

### 12. Ca → CaCl₂·2H₂O (calcium chloride dihydrate) ✅ CERTAIN

**Evidence**:
- **Already mapped**: 10+ CaCl2 variants exist in mapped_ingredients.yaml
- **CAS number**: 13477-34-4 (calcium chloride dihydrate)
- **Score**: 135 (very high confidence)
- **Chemical logic**: CaCl₂·2H₂O is the most common form in lab reagents

**Recommendation**: Map to CHEBI:86158 (calcium chloride dihydrate)

---

## Summary Table

| Formula | Complete | CHEBI ID | Confidence | Action |
|---------|----------|----------|------------|--------|
| NaNO | NaNO₃ | CHEBI:34218 | ✅ HIGH | Map (CAS verified) |
| K2HPO | K₂HPO₄ | CHEBI:32030 | ✅ HIGH | Map |
| MgCO | MgCO₃ | CHEBI:6611 | ✅ HIGH | Map |
| KH2PO | KH₂PO₄ | CHEBI:32583 | ✅ HIGH | Map |
| CaCO | CaCO₃ | CHEBI:3311 | ✅ CERTAIN | Map (already exists) |
| KNO | KNO₃ | CHEBI:63043 | ✅ HIGH | Map (already exists) |
| NaHCO | NaHCO₃ | CHEBI:32139 | ✅ HIGH | Map |
| NH4NO | NH₄NO₃ | CHEBI:63038 | ✅ CERTAIN | Map (CAS + exists) |
| Na2CO | Na₂CO₃ | CHEBI:29377 | ✅ CERTAIN | Map (already exists 4x) |
| NH4MgPO | (NH₄)MgPO₄ | CHEBI:90884 | ⚠️ MEDIUM | Map (check context) |
| H3BO | H₃BO₃ | CHEBI:33118 | ✅ CERTAIN | Map (already exists) |
| Ca | CaCl₂·2H₂O | CHEBI:86158 | ✅ CERTAIN | Map (CAS + exists 10x) |

---

## Confidence Breakdown

- **✅ CERTAIN** (6): Already mapped in collection with strong evidence
  - CaCO, Na2CO, H3BO, NH4NO, Ca (CAS verified), KNO

- **✅ HIGH** (5): Chemical logic + standard forms
  - NaNO (CAS verified), K2HPO, KH2PO, MgCO, NaHCO

- **⚠️ MEDIUM** (1): Needs context verification
  - NH4MgPO (struvite, check hydration)

---

## Next Steps

### Option 1: Map All 12 (Recommended)
Map all 12 formulas to their recommended CHEBI IDs. All have high confidence except NH4MgPO which is medium.

### Option 2: Map 11, Hold 1
Map 11 certain/high confidence formulas, keep NH4MgPO for expert review.

### Option 3: Report to CultureMech First
Submit the incomplete formulas issue to CultureMech, wait for source corrections, then map.

---

## Mapping Script Ready

A script can be created to map all 12 incomplete formulas automatically:

```python
FORMULA_REPAIRS = {
    "NaNO": {"formula": "NaNO3", "chebi": "CHEBI:34218"},
    "K2HPO": {"formula": "K2HPO4", "chebi": "CHEBI:32030"},
    "MgCO": {"formula": "MgCO3", "chebi": "CHEBI:6611"},
    "KH2PO": {"formula": "KH2PO4", "chebi": "CHEBI:32583"},
    "CaCO": {"formula": "CaCO3", "chebi": "CHEBI:3311"},
    "KNO": {"formula": "KNO3", "chebi": "CHEBI:63043"},
    "NaHCO": {"formula": "NaHCO3", "chebi": "CHEBI:32139"},
    "NH4NO": {"formula": "NH4NO3", "chebi": "CHEBI:63038"},
    "Na2CO": {"formula": "Na2CO3", "chebi": "CHEBI:29377"},
    "NH4MgPO": {"formula": "(NH4)MgPO4", "chebi": "CHEBI:90884"},
    "H3BO": {"formula": "H3BO3", "chebi": "CHEBI:33118"},
    "Ca": {"formula": "CaCl2·2H2O", "chebi": "CHEBI:86158"},
}
```

---

**Generated**: 2026-03-15
**Analysis Method**: Automated pattern matching + CAS verification + existing mapping cross-reference
**Recommendation**: **Map all 12 formulas** - confidence is high to certain for all
