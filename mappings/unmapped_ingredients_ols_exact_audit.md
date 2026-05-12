# Unmapped Ingredient OLS Exact Audit

- Input directory: `data/ingredients/unmapped`
- Unmapped records audited: 466
- Method: EBI OLS4 exact search across `chebi, foodon, envo, ncit, mesh, micro, bto, uberon`; query variants include preferred term, filename label, Greek-letter transliteration, and local chemical-normalizer variants.

## Per-Ingredient Candidate Status

| Status | Count |
|---|---:|
| no_exact_candidate | 415 |
| has_synonym_exact_candidate | 40 |
| has_label_exact_candidate | 11 |

## Row Match Types

| Match type | Rows |
|---|---:|
| NO_EXACT_OLS_HIT | 415 |
| SYNONYM_EXACT | 81 |
| LABEL_EXACT | 15 |

## Category Breakdown

| Category | Records |
|---|---:|
| UNKNOWN | 216 |
| SIMPLE_CHEMICAL | 162 |
| COMPLEX_MIXTURE | 79 |
| INCOMPLETE | 5 |
| PLACEHOLDER | 2 |
| ENVIRONMENTAL | 2 |

## High-Confidence Label-Exact Candidates

| Ingredient | Candidate | OLS label | Missing exact synonyms |
|---|---|---|---|
| Biotin (Vitamin B7) | `CHEBI:15956` | biotin | biotin|Biotin (Vitamin B7) |
| Biotin (Vitamin B7) | `NCIT:C309` | Biotin | Biotin|Biotin (Vitamin B7) |
| Biotin (Vitamin B7) | `mesh:D001710` | Biotin | Biotin|Biotin (Vitamin B7) |
| dH2O | `ENVO:00003065` | distilled water | distilled water|dH2O |
| Iron (as FeCl3 in EDTA) | `NCIT:C598` | Iron | Iron|Iron (as FeCl3 in EDTA) |
| Iron (as FeCl3 in EDTA) | `mesh:D007501` | Iron | Iron|Iron (as FeCl3 in EDTA) |
| K2HPO | `FOODON:03413082` | dipotassium phosphate | dipotassium phosphate|K2HPO |
| L-α-Phosphatidylcholine | `CHEBI:86658` | L-alpha-Phosphatidylcholine | L-alpha-Phosphatidylcholine|L-α-Phosphatidylcholine |
| NaHCO | `mesh:D017693` | Sodium Bicarbonate | Sodium Bicarbonate|NaHCO |
| Titanium(III) citrate | `mesh:C419387` | titanium citrate | titanium citrate|Titanium(III) citrate |
| Vitamin B | `CHEBI:176843` | vitamin B12 | Vitamin B |
| Vitamin B12 (cyanocobalamin) | `CHEBI:176843` | vitamin B12 | vitamin B12|Vitamin B12 (cyanocobalamin) |
| Xylan (hemicellulose substrate) | `CHEBI:37166` | xylan | xylan|Xylan (hemicellulose substrate) |
| Xyloglucan (hepta+octa+nona saccharides) | `CHEBI:18233` | xyloglucan | xyloglucan|Xyloglucan (hepta+octa+nona saccharides) |
| Xyloglucan (hepta+octa+nona saccharides) | `mesh:C029353` | xyloglucan | xyloglucan|Xyloglucan (hepta+octa+nona saccharides) |

## Notes

- This audit does not mutate YAML. `LABEL_EXACT` rows are the safest mapping candidates; `SYNONYM_EXACT` rows require manual review because OLS matched a synonym rather than the canonical label.
- `missing_exact_synonyms` lists standard labels or matched exact synonym strings absent from the current YAML synonym list and should be considered during accepted mappings.
