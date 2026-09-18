# `data/ingredients/mapped/4-nitrophenyl_6-O-phosphono-beta-D-galactoside.yaml`

## Verdict

Pass, none. The exact `CHEBI:90128` phosphate-galactoside identity, canonical
label, microbedecoder provenance, ChEBI-derived chemistry, SSSOM row, and
aggregate copy pass.

## Identity

- Reviewed record:
  `data/ingredients/mapped/4-nitrophenyl_6-O-phosphono-beta-D-galactoside.yaml`.
- Identifier and grounding: `identifier: CHEBI:90128` with
  `ontology_mapping.ontology_id: CHEBI:90128`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Official OLS/ChEBI check: `CHEBI:90128` is active, resolves to
  `4-nitrophenyl 6-O-phosphono-beta-D-galactoside`, has formula
  `C12H16NO11P`, neutral charge, the stored SMILES, the stored InChI, and the
  IUPAC synonym `4-nitrophenyl 6-O-phosphono-beta-D-galactopyranoside`.
- `ingredient_type: SINGLE_INGREDIENT` is present.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/4-nitrophenyl_6-O-phosphono-beta-D-galactoside.yaml data/ingredients/mapped/4-nitrophenyl_Alpha-D-galactoside.yaml data/ingredients/mapped/4-nitrophenyl_Alpha-D-glucopyranoside.yaml data/ingredients/mapped/4-nitrophenyl_Beta-D-galactopyranoside.yaml data/ingredients/mapped/4-nitrophenyl_Beta-D-glucopyranoside.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/4-nitrophenyl_6-O-phosphono-beta-D-galactoside.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- Whole-corpus component partonomy, SSSOM invariants, and flat-export coverage
  passed earlier in this all-record review; only SSSOM Rule B4 was skipped
  because the sibling `kg-microbe` ontology transforms are absent.

## Evidence

- The current ChEBI term, formula, SMILES, and InChI all support the exact
  4-nitrophenyl 6-O-phosphono-beta-D-galactoside identity.
- The microbedecoder occurrence block records 2 uses from
  `BacDive_Metabolite_utilization` and carries the source accession
  `kgmicrobe.trait:4_nitrophenyl_6_o_phosphono_beta_d_galactoside`.
- The occurrence statistics correctly keep the upstream microbedecoder count
  separate from verified CultureMech recipe counts, which remain
  `total_occurrences: 0` and `media_count: 0`.
- The SSSOM row maps
  `MIM:4-nitrophenyl_6-O-phosphono-beta-D-galactoside` to `CHEBI:90128` with
  `skos:exactMatch`, `semapv:LexicalMatching`, and no `other` synonym payload.
- The hidden/ignored-inclusive search over `data`, `mappings`, `docs`, and
  `UNIFIED_INGREDIENT_MAPPING.tsv` found the active YAML, aggregate copy, SSSOM
  row, generated docs, source review row, and ignored aggregate backups.

## Completeness

- Formula, InChI, SMILES, molecular weight, source occurrence counts, and
  `ingredient_type` are populated.
- ChEBI exposes no CAS registry number for this term in the inspected official
  response; no CAS omission needs curation.
- No synonyms, roles, components, environment, or discussion entries need
  review.

## Recommended Edits

No YAML edit is required for this record.
