# `data/ingredients/mapped/4-nitrophenyl_Alpha-D-glucopyranoside.yaml`

## Verdict

Pass with minor issues, minor. The `CHEBI:91122` alpha-D-glucoside synonym
match, retained raw label, microbedecoder provenance, chemistry, SSSOM row, and
aggregate copy pass, but the top-level import note still says the pre-promotion
record had no ontology match and needed curation.

## Identity

- Reviewed record:
  `data/ingredients/mapped/4-nitrophenyl_Alpha-D-glucopyranoside.yaml`.
- Identifier and grounding: `identifier: CHEBI:91122` with
  `ontology_mapping.ontology_id: CHEBI:91122`, source `CHEBI`,
  `mapping_quality: SYNONYM_MATCH`, and `mapping_status: MAPPED`.
- Official OLS/ChEBI check: `CHEBI:91122` is active, resolves to
  `4-nitrophenyl alpha-D-glucoside`, has formula `C12H15NO8`, neutral charge,
  CAS `3767-28-0`, the stored SMILES, the stored InChI, and the IUPAC synonym
  `4-nitrophenyl alpha-D-glucopyranoside`.
- `ingredient_type: SINGLE_INGREDIENT` is present.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/4-nitrophenyl_6-O-phosphono-beta-D-galactoside.yaml data/ingredients/mapped/4-nitrophenyl_Alpha-D-galactoside.yaml data/ingredients/mapped/4-nitrophenyl_Alpha-D-glucopyranoside.yaml data/ingredients/mapped/4-nitrophenyl_Beta-D-galactopyranoside.yaml data/ingredients/mapped/4-nitrophenyl_Beta-D-glucopyranoside.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/4-nitrophenyl_Alpha-D-glucopyranoside.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- Whole-corpus component partonomy, SSSOM invariants, and flat-export coverage
  passed earlier in this all-record review; only SSSOM Rule B4 was skipped
  because the sibling `kg-microbe` ontology transforms are absent.

## Evidence

- The active ChEBI term, formula, SMILES, InChI, and IUPAC synonym all support
  the record's synonym-level grounding from the raw microbedecoder text to
  `CHEBI:91122`.
- The `RAW_TEXT` synonym preserves the upstream label
  `4-nitrophenyl Alpha-D-glucopyranoside`, which differs only in case from the
  official ChEBI synonym and is safe to export as source text.
- The microbedecoder occurrence block records 11 uses from
  `BacDive_Metabolite_utilization` and carries the source accession
  `kgmicrobe.trait:4_nitrophenyl_alpha_d_glucopyranoside`.
- Minor: the top-level `notes` field is the old import note saying no
  CAS-RN or ChEBI/NCIT match existed and that curator review was needed. The
  later `PROMOTED_TO_MAPPED` history event supersedes that note.
- The SSSOM row maps `MIM:4-nitrophenyl_Alpha-D-glucopyranoside` to
  `CHEBI:91122` with `skos:exactMatch`, `semapv:ManualMappingCuration`, and
  no `other` synonym payload.
- The hidden/ignored-inclusive search over `data`, `mappings`, `docs`, and
  `UNIFIED_INGREDIENT_MAPPING.tsv` found the active YAML, aggregate copy,
  SSSOM row, residual grounding row, generated docs, stale advisory rows, and
  ignored aggregate backups.

## Completeness

- Formula, InChI, SMILES, molecular weight, source occurrence counts, and
  `ingredient_type` are populated.
- CAS `3767-28-0` is available on ChEBI but not required for the active
  synonym-level grounding because the structural fields already match.
- No roles, components, environment, or discussion entries need review.

## Recommended Edits

1. Remove or refresh the stale top-level `notes` text in
   `data/ingredients/mapped/4-nitrophenyl_Alpha-D-glucopyranoside.yaml` and
   `data/curated/mapped_ingredients.yaml` so it no longer says the record is
   unmatched and awaiting curator review.
