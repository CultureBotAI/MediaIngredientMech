# `data/ingredients/mapped/4-nitrophenyl_Phosphate.yaml`

## Verdict

Pass, none. The exact `CHEBI:17440` 4-nitrophenyl phosphate identity,
canonical label, microbedecoder provenance, ChEBI-derived chemistry, SSSOM row,
and aggregate copy pass.

## Identity

- Reviewed record: `data/ingredients/mapped/4-nitrophenyl_Phosphate.yaml`.
- Identifier and grounding: `identifier: CHEBI:17440` with
  `ontology_mapping.ontology_id: CHEBI:17440`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Official OLS/ChEBI check: `CHEBI:17440` is active, resolves to
  `4-nitrophenyl phosphate`, has formula `C6H6NO6P`, neutral charge, CAS
  `330-13-2`, the stored SMILES, and the stored InChI.
- `ingredient_type: SINGLE_INGREDIENT` is present.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/4-nitrophenyl_Beta-D-glucuronide.yaml data/ingredients/mapped/4-nitrophenyl_Beta-D-xylopyranoside.yaml data/ingredients/mapped/4-nitrophenyl_N-acetyl-beta-D-glucosaminide.yaml data/ingredients/mapped/4-nitrophenyl_Phosphate.yaml data/ingredients/mapped/4-oxopentanoate.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/4-nitrophenyl_Phosphate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- Whole-corpus component partonomy, SSSOM invariants, and flat-export coverage
  passed earlier in this all-record review; only SSSOM Rule B4 was skipped
  because the sibling `kg-microbe` ontology transforms are absent.

## Evidence

- The active ChEBI term, formula, CAS, SMILES, and InChI all support the exact
  neutral 4-nitrophenyl phosphate identity.
- The raw microbedecoder source row in
  `data/custom/microbedecoder/unmapped_labels.tsv` records
  `kgmicrobe.trait:4_nitrophenyl_phosphate` with count 1 in
  `BacDive_Metabolite_utilization`, matching `source_occurrences`.
- The occurrence statistics correctly keep the upstream microbedecoder count
  separate from verified CultureMech recipe counts, which remain
  `total_occurrences: 0` and `media_count: 0`.
- The SSSOM row maps `MIM:4-nitrophenyl_Phosphate` to `CHEBI:17440` with
  `skos:exactMatch`, `semapv:LexicalMatching`, and no `other` synonym payload.
- The hidden/ignored-inclusive search over `data`, `mappings`, `docs`, and
  `UNIFIED_INGREDIENT_MAPPING.tsv` found the active YAML, aggregate copy,
  microbedecoder source row, SSSOM row, generated docs, source review row, and
  ignored aggregate backups.

## Completeness

- Formula, InChI, SMILES, molecular weight, source occurrence counts, and
  `ingredient_type` are populated.
- CAS `330-13-2` is available on ChEBI but is not required for the active
  exact-label grounding because the structural fields already match.
- No synonyms, roles, components, environment, or discussion entries need
  review.

## Recommended Edits

No YAML edit is required for this record.
