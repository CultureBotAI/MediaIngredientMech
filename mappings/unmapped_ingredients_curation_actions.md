# Unmapped Ingredient Curation Actions

Date: 2026-05-06

This note records the high-confidence changes applied from
`mappings/unmapped_ingredients_ols_exact_audit.tsv`. The audit searched unmapped
ingredient labels and synonyms against local/OLS-backed ontology candidates; only
locally supported identity mappings were applied here.

## Applied

| Unmapped record | Action | Mapped representative | Evidence |
| --- | --- | --- | --- |
| `Biotin_(Vitamin_B7).yaml` | Retired duplicate and added exact synonym | `Biotin.yaml` / `CHEBI:15956` | Existing mapped Biotin record and OLS exact match to biotin |
| `Dh2o.yaml` | Retired duplicate and summed occurrence counts | `Distilled_Water.yaml` / `CHEBI:15377` | Existing exact synonym `dH2O` on mapped distilled water record |
| `K2hpo.yaml` | Retired duplicate, added source variants, and summed occurrence counts | `K2hpo4.yaml` / `CHEBI:131527` | Existing mapped K2HPO4 record and source synonym `K2HPO4(Sigma P 3786)` |
| `Nahco.yaml` | Retired duplicate, added source variant, and summed occurrence counts | `Nahco3.yaml` / `CHEBI:32139` | Existing mapped NaHCO3 record and source synonym `NaHCO3(Fisher S 233)` |
| `Vitamin_B12_(cyanocobalamin).yaml` | Retired duplicate and added exact synonym | `Vitamin_B12.yaml` / `CHEBI:176843` | Existing mapped vitamin B12 record and OLS exact match |
| `Xylan_(hemicellulose_Substrate).yaml` | Retired duplicate and added exact synonym | `Xylan.yaml` / `CHEBI:37166` | Existing mapped xylan record and OLS exact match |
| `L-alpha-Phosphatidylcholine` source record | Promoted to mapped record after label normalization | `L-alpha-Phosphatidylcholine.yaml` / `CHEBI:86658` | OLS exact label match after Greek-letter transliteration |

## Left For Later Curation

| Unmapped record | Reason |
| --- | --- |
| `Iron_(as_FeCl3_In_EDTA).yaml` | Formulation-specific source label; not identity-equivalent to generic iron |
| `Titanium(III)_Citrate.yaml` | Candidate is broader/generic titanium citrate; oxidation and salt details need manual review |
| `Vitamin_B.yaml` | Label is ambiguous and the vitamin B12 candidate is not a safe identity mapping |
| `Xyloglucan_(heptaoctanona_Saccharides).yaml` | Source label is a specific saccharide mixture/substrate, not clearly identical to generic xyloglucan |
