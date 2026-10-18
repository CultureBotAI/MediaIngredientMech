# `data/ingredients/mapped/4-nitrophenyl_Beta-D-xylopyranoside.yaml`

## Verdict

Pass with minor issues, minor. The `CHEBI:90148` beta-D-xyloside synonym
match, retained raw label, microbedecoder provenance, chemistry, SSSOM row, and
aggregate copy pass, but the top-level import note still says the pre-promotion
record had no ontology match and needed curation.

## Identity

- Reviewed record:
  `data/ingredients/mapped/4-nitrophenyl_Beta-D-xylopyranoside.yaml`.
- Identifier and grounding: `identifier: CHEBI:90148` with
  `ontology_mapping.ontology_id: CHEBI:90148`, source `CHEBI`,
  `mapping_quality: SYNONYM_MATCH`, and `mapping_status: MAPPED`.
- Official OLS/ChEBI check: `CHEBI:90148` is active, resolves to
  `4-nitrophenyl beta-D-xyloside`, has formula `C11H13NO7`, neutral charge,
  CAS `2001-96-9`, the stored SMILES, the stored InChI, and the IUPAC synonym
  `4-nitrophenyl beta-D-xylopyranoside`.
- `ingredient_type: SINGLE_INGREDIENT` is present.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/4-nitrophenyl_Beta-D-glucuronide.yaml data/ingredients/mapped/4-nitrophenyl_Beta-D-xylopyranoside.yaml data/ingredients/mapped/4-nitrophenyl_N-acetyl-beta-D-glucosaminide.yaml data/ingredients/mapped/4-nitrophenyl_Phosphate.yaml data/ingredients/mapped/4-oxopentanoate.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/4-nitrophenyl_Beta-D-xylopyranoside.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- Whole-corpus component partonomy, SSSOM invariants, and flat-export coverage
  passed earlier in this all-record review; only SSSOM Rule B4 was skipped
  because the sibling `kg-microbe` ontology transforms are absent.

## Evidence

- The active ChEBI term, formula, CAS, SMILES, InChI, and IUPAC synonym all
  support the record's synonym-level grounding from the raw microbedecoder text
  to `CHEBI:90148`.
- The `RAW_TEXT` synonym preserves the upstream label
  `4-nitrophenyl Beta-D-xylopyranoside`, which differs only in case from the
  official ChEBI synonym and is safe to export as source text.
- The raw microbedecoder source row in
  `data/custom/microbedecoder/unmapped_labels.tsv` records
  `kgmicrobe.trait:4_nitrophenyl_beta_d_xylopyranoside` with count 7 in
  `BacDive_Metabolite_utilization`, matching `source_occurrences`.
- Minor: the top-level `notes` field is the old import note saying no
  CAS-RN or ChEBI/NCIT match existed and that curator review was needed. The
  later `PROMOTED_TO_MAPPED` history event supersedes that note.
- The SSSOM row maps `MIM:4-nitrophenyl_Beta-D-xylopyranoside` to
  `CHEBI:90148` with `skos:exactMatch`, `semapv:ManualMappingCuration`, and
  no `other` synonym payload.
- The hidden/ignored-inclusive search over `data`, `mappings`, `docs`, and
  `UNIFIED_INGREDIENT_MAPPING.tsv` found the active YAML, aggregate copy,
  microbedecoder source row, SSSOM row, residual grounding row, generated docs,
  and ignored aggregate backups.

## Completeness

- Formula, InChI, SMILES, molecular weight, source occurrence counts, and
  `ingredient_type` are populated.
- No roles, components, environment, or discussion entries need review.

## Recommended Edits

1. Remove or refresh the stale top-level `notes` text in
   `data/ingredients/mapped/4-nitrophenyl_Beta-D-xylopyranoside.yaml` and
   `data/curated/mapped_ingredients.yaml` so it no longer says the record is
   unmatched and awaiting curator review.
