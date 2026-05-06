# UNKNOWN_TERM SSSOM Triage Summary

Date: 2026-05-06

Input artifacts:
- `mappings/ingredient_mappings.sssom.tsv`
- `../culturebotai-claw/workspace/reports/sssom_synonym_review.tsv`
- `mappings/ingredient_mappings_unknown_term_triage.tsv`
- `mappings/ingredient_mappings_external_prefix_ols_validation.tsv`

## Current UNKNOWN_TERM Coverage

- Current SSSOM UNKNOWN_TERM rows: 690
- Triage rows match current SSSOM UNKNOWN_TERM subject/object pairs exactly.

### Prefix Counts

| Prefix | Rows |
|---|---:|
| `BTO` | 1 |
| `MICRO` | 47 |
| `NCIT` | 61 |
| `cas` | 249 |
| `kgmicrobe.compound` | 219 |
| `kgmicrobe.ingredient` | 29 |
| `mesh` | 84 |

### Triage Buckets

| Bucket | Rows | Disposition |
|---|---:|---|
| CAS and kg-microbe registry identifiers | 444 | Valid registry rows; no YAML/SSSOM repair needed. |
| External ontology prefixes missed by serial reviewer | 193 | External OLS validation resolves all exact CURIEs; no mapping repair needed. |
| kg-microbe placeholder rows needing promotion review | 53 | No exact OLS candidate remains after this pass; keep as manual placeholder queue. |

## Placeholder Promotion Search

A focused EBI OLS exact label/synonym search was run for the 64 original `kgmicrobe.compound` placeholder rows across `chebi`, `mesh`, `ncit`, `micro`, `bto`, and `foodon`.

- 10 placeholder subjects had exact OLS candidates; 8 were promoted to external MeSH/NCIT mappings and 2 were retired as duplicates of existing mapped representatives (`Beta-Lipomycin`, `Etamycin`).
- Current placeholder rows remaining in manual queue: 53
- Current queue artifact: `mappings/ingredient_mappings_unknown_term_placeholder_ols_candidates.tsv`.

## Follow-up OAK/OLS Normalized Review

- The companion placeholder-upgrade workflow scanned 65 current `kgmicrobe.compound:*`
  primaries through CHEBI, NCIT, MICRO, MeSH, FOODON, and ENVO; no additional
  exact label/synonym hits were found by that automated workflow.
- Manual follow-up of the chemically specific LOW-confidence rows found one
  punctuation-normalized CHEBI identity: `Poly_L_Lysine_Polymer` was promoted
  from `kgmicrobe.compound:poly_l_lysine_polymer` to `CHEBI:61490`
  (`poly(L-lysine) polymer`) after OAK/OLS validation.
- A subsequent all-ontology EBI OLS search-response scan over the 53 remaining
  placeholder labels, filtered to CHEBI, NCIT, MeSH, MICRO, BTO, FOODON, and
  ENVO and compared with punctuation-insensitive label/synonym normalization,
  found 0 additional identity candidates.

## Outcome

- Ingredient YAML changed for nine placeholder promotions and two duplicate retirements.
- Aggregate collections were regenerated from individual YAML records.
- SSSOM was rebuilt, OAK/OLS-reviewed, and published because mapping rows changed.
- Remaining UNKNOWN_TERM rows are either expected non-OBO registry rows, external-prefix false positives already resolved by explicit OLS validation, or kg-microbe placeholders that need future manual curation.
