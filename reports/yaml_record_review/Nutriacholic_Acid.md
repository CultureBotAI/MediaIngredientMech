# `data/ingredients/mapped/Nutriacholic_Acid.yaml`

## Verdict

Pass. The promoted MicrobeDecoder record now exact-maps to active
`CHEBI:82679` through the ChEBI synonym `Nutriacholic acid`; the old Edison
UNMAPPED recommendation is stale.

## Identity

- Reviewed record: `data/ingredients/mapped/Nutriacholic_Acid.yaml`.
- Identifier and grounding: `identifier: CHEBI:82679` with
  `ontology_mapping.ontology_id: CHEBI:82679`, label `7-oxolithocholic acid`,
  source `CHEBI`, `mapping_quality: SYNONYM_MATCH`, `mapping_status: MAPPED`,
  and `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: one MicrobeDecoder `BacDive_Metabolite_production` source-column
  occurrence and zero CultureMech media occurrences.

## Validation

- `uv run --frozen python scripts/validate_strict.py` exited 0 across this
  five-record batch and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.

## Evidence

- A fresh EBI OLS4 lookup resolves `CHEBI:82679` as active
  `7-oxolithocholic acid`, lists `Nutriacholic acid` as a synonym, and reports
  formula `C24H38O4` plus the same InChI and SMILES stored in the YAML.
- `mappings/record_research_validation.tsv` still has a P1
  `STATUS_CONFLICT` for the pre-promotion Edison report, but the later
  `promote_resolved_unmapped` entry documents promotion from `UNMAPPED_0833`
  to `CHEBI:82679` after the synonym was checked in `#213`.
- The final SSSOM row maps `MIM:Nutriacholic_Acid` exactly to `CHEBI:82679`,
  has no `other` tokens, and carries the manual promotion stamp.
- No unsupported roles, components, supplied forms, or environmental contexts
  are asserted.

## Completeness

- The active ChEBI term, synonym-backed label, formula, structure, and final
  SSSOM row agree.
- The ignored and hidden-inclusive search over `data/curated`, `mappings`,
  `reports`, `scripts`, `src`, and `tests` found no current blocking review
  row beyond the stale Edison status conflict described above.

## Recommended Edits

- None for this record.
