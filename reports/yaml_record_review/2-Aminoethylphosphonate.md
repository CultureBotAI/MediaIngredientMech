# `data/ingredients/mapped/2-Aminoethylphosphonate.yaml`

## Verdict

Needs curation, minor. The CultureMech residual grounding to `CHEBI:15573` is
exact and synchronized, but the late-created record is missing the
ChEBI-derived `ingredient_type` and chemistry backfill present on older ChEBI
records.

## Identity

- Reviewed record: `data/ingredients/mapped/2-Aminoethylphosphonate.yaml`.
- Identifier and grounding: `identifier: CHEBI:15573` with
  `ontology_mapping.ontology_id: CHEBI:15573`,
  `ontology_mapping.ontology_label: (2-aminoethyl)phosphonic acid`, source
  `CHEBI`, `mapping_quality: SYNONYM_MATCH`,
  `match_level: NORMALIZED`, and `mapping_status: MAPPED`.
- Official ChEBI check: the current EMBL-EBI ChEBI page for `CHEBI:15573`
  resolves to the same 2-aminoethyl phosphonic-acid term and lists formula
  `C2H8NO3P` and InChI
  `InChI=1S/C2H8NO3P/c3-1-2-7(4,5)6/h1-3H2,(H2,4,5,6)`.
- Source provenance: the structured mapping evidence and curation history both
  point to `culturemech:output/ingredient_occurrences.tsv`, with one occurrence
  across one CultureMech recipe.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/2-Acetylpyrrole.yaml data/ingredients/mapped/2-Aminoethylphosphonate.yaml data/ingredients/mapped/2-Azetidinone.yaml data/ingredients/mapped/2-Chlorobenzoic_acid.yaml data/ingredients/mapped/2-Deoxy-D-Ribose.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/2-Aminoethylphosphonate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `scripts/_engine_a_obo_safe.sh data/ingredients/mapped/2-Aminoethylphosphonate.yaml "CHEBI FOODON NCIT MESH UBERON ENVO BTO PATO"`:
  passed.
- Whole-corpus checks run earlier in this review pass passed; only the shared
  evidence validator was unavailable because `../culturebotai-claw` is absent.
- Per-record/aggregate comparison against `data/curated/mapped_ingredients.yaml`:
  normalized semantic equality passed.
- `mappings/ingredient_mappings.sssom.tsv` contains the expected exact
  `MIM:2-Aminoethylphosphonate` to `CHEBI:15573` row with the restored
  CultureMech occurrence-table provenance.

## Evidence

- The active ChEBI target confirms the exact identity and the structured source
  evidence now feeds the production SSSOM row, resolving #541's evidence-loss
  issue for this row.
- Minor: because the record was added after the May auto-classification passes,
  it still has no `ingredient_type` and no ChEBI-derived formula, InChI, or
  SMILES despite being a mapped single ChEBI chemical.
- The hidden/ignored-inclusive search over YAML, TSV, Markdown, ignored
  backups, and generated review output found the active YAML/aggregate/SSSOM
  rows and no unresolved active duplicate for `CHEBI:15573`.

## Completeness

- Empty component and role slots are acceptable for this single ChEBI chemical.
- `occurrence_statistics` is consistent with the CultureMech residual grounding:
  one occurrence across one recipe.
- Ingredient typing and chemistry backfill remain useful so this late-created
  record has parity with older ChEBI imports.

## Recommended Edits

1. In `data/ingredients/mapped/2-Aminoethylphosphonate.yaml`, add
   `ingredient_type: SINGLE_INGREDIENT` and ChEBI-derived formula/InChI/SMILES
   for `CHEBI:15573`.
2. Regenerate `data/curated/mapped_ingredients.yaml` and docs from the
   maintained YAML.
3. Re-run strict/LinkML validation and SSSOM export checks after the backfill.
