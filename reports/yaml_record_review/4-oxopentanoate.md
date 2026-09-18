# `data/ingredients/mapped/4-oxopentanoate.yaml`

## Verdict

Pass, none. The exact `CHEBI:39150` 4-oxopentanoate identity, canonical label,
microbedecoder provenance, anion chemistry, SSSOM row, and aggregate copy pass.

## Identity

- Reviewed record: `data/ingredients/mapped/4-oxopentanoate.yaml`.
- Identifier and grounding: `identifier: CHEBI:39150` with
  `ontology_mapping.ontology_id: CHEBI:39150`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Official OLS/ChEBI check: `CHEBI:39150` is active and resolves to
  `4-oxopentanoate`.
- The current ChEBI page reports formula `C5H7O3`, the stored SMILES, and the
  stored deprotonated InChI for `CHEBI:39150`.
- `ingredient_type: SINGLE_INGREDIENT` is present.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/4-nitrophenyl_Beta-D-glucuronide.yaml data/ingredients/mapped/4-nitrophenyl_Beta-D-xylopyranoside.yaml data/ingredients/mapped/4-nitrophenyl_N-acetyl-beta-D-glucosaminide.yaml data/ingredients/mapped/4-nitrophenyl_Phosphate.yaml data/ingredients/mapped/4-oxopentanoate.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/4-oxopentanoate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- Whole-corpus component partonomy, SSSOM invariants, and flat-export coverage
  passed earlier in this all-record review; only SSSOM Rule B4 was skipped
  because the sibling `kg-microbe` ontology transforms are absent.

## Evidence

- The active ChEBI term, anion formula, SMILES, and InChI all support the exact
  4-oxopentanoate identity.
- The raw microbedecoder source row in
  `data/custom/microbedecoder/unmapped_labels.tsv` records
  `kgmicrobe.trait:4_oxopentanoate` with count 11 in
  `BacDive_Metabolite_utilization`, matching `source_occurrences`.
- The occurrence statistics correctly keep the upstream microbedecoder count
  separate from verified CultureMech recipe counts, which remain
  `total_occurrences: 0` and `media_count: 0`.
- The SSSOM row maps `MIM:4-oxopentanoate` to `CHEBI:39150` with
  `skos:exactMatch`, `semapv:LexicalMatching`, and no `other` synonym payload.
- The hidden/ignored-inclusive search over `data`, `mappings`, `docs`, and
  `UNIFIED_INGREDIENT_MAPPING.tsv` found the active YAML, aggregate copy,
  microbedecoder source row, SSSOM row, generated docs, source review row, and
  ignored aggregate backups.

## Completeness

- Formula, InChI, SMILES, molecular weight, source occurrence counts, and
  `ingredient_type` are populated.
- No synonyms, roles, components, environment, or discussion entries need
  review.

## Recommended Edits

No YAML edit is required for this record.
