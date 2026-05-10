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
- The LOW/MEDIUM candidate pass was manually triaged in
  `mappings/ingredient_mappings_unknown_term_manual_candidate_review.tsv`.
  It reviewed 20 rows with prior lexical candidates; all remain queued because
  candidates were family/member variants, unrelated lexical hits, organism terms,
  or required external literature evidence beyond OAK/OLS metadata.
- The remaining 33 placeholder rows had no prior OLS candidates in their YAML
  evidence and no normalized local duplicate representative in `data/ingredients/mapped`.
  They are recorded in
  `mappings/ingredient_mappings_unknown_term_nohit_review.tsv`.

## Outcome

- Ingredient YAML changed for nine placeholder promotions and two duplicate retirements.
- Aggregate collections were regenerated from individual YAML records.
- SSSOM was rebuilt, OAK/OLS-reviewed, and published because mapping rows changed.
- Remaining UNKNOWN_TERM rows are either expected non-OBO registry rows, external-prefix false positives already resolved by explicit OLS validation, or kg-microbe placeholders that need future manual curation.

## 2026-05-10 Follow-up Row Review

- All 53 current `kgmicrobe.compound:*` placeholder rows from
  `ingredient_mappings_unknown_term_placeholder_ols_candidates.tsv` are now reflected
  in individual ingredient YAML curation history/notes.
- The 33 no-hit rows in `ingredient_mappings_unknown_term_nohit_review.tsv` were
  annotated as retained placeholders: no exact OLS candidate and no normalized local
  mapped duplicate supported promotion.
- The 20 rows in `ingredient_mappings_unknown_term_manual_candidate_review.tsv` were
  annotated as manually triaged. Eighteen remain `NO_IDENTITY_PROMOTION`, `Bacteriocin
  Isk 1` is `FALCON_REVIEWED_AMBIGUOUS`, and `Destomycin` is
  `OLS_REVIEWED_NO_IDENTITY_PROMOTION`.
- No SSSOM predicate or object changes were made in this follow-up because no reviewed
  row met the evidence threshold for exact identity promotion.
- The mapped aggregate collection was regenerated from individual YAML records after
  annotation. The unmapped aggregate was left unchanged except for avoiding timestamp-only
  churn.

## 2026-05-10 SYNONYM_ENRICH Review

- Added `ingredient_mappings_row_review_manifest.tsv` as the top-level disposition
  manifest for all 2,194 rows in `ingredient_mappings_oak_ols_review.tsv`.
- Added `ingredient_mappings_synonym_enrich_review.tsv` as a row-level disposition
  artifact for all 623 `SYNONYM_ENRICH` rows.
- 619 rows were `ALREADY_REPRESENTED`: every proposed candidate string was already
  present as the ingredient preferred term or a synonym.
- Four rows required mapping repair rather than synonym addition:
  `Disodium_Phosphate_Heptahydrate_(002_M_Stock)`, `EDTA_(acid_Form)`,
  `Sodium_Nitrate_(070_M_Stock)`, and `Soyton`.
- The two stock solution rows now use a `kgmicrobe.ingredient:*` registry identity
  row plus `skos:narrowMatch` to the corrected CHEBI solute term.
- `EDTA_(acid_Form)` was corrected from EDTA tetraanion `CHEBI:42191` to EDTA acid
  `CHEBI:4735`.
- `Soyton` was corrected from unrelated `FOODON:03302071` to a local
  `kgmicrobe.ingredient:soyton` identity pending exact external ontology support.
