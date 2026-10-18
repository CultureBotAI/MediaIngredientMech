# `data/ingredients/mapped/2-Nitrophenol.yaml`

## Verdict

Needs curation, minor. The CultureMech residual grounding to `CHEBI:16260` is
exact and synchronized, but the late-created record is missing the
ChEBI-derived `ingredient_type` and chemistry backfill present on older ChEBI
records.

## Identity

- Reviewed record: `data/ingredients/mapped/2-Nitrophenol.yaml`.
- Identifier and grounding: `identifier: CHEBI:16260` with
  `ontology_mapping.ontology_id: CHEBI:16260`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `match_level: EXACT`, and
  `mapping_status: MAPPED`.
- Official ChEBI check: the current EMBL-EBI ChEBI page for `CHEBI:16260`
  resolves to `2-nitrophenol` and lists CAS `88-75-5` and formula `C6H5NO3`.
- Source provenance: the structured mapping evidence and curation history both
  point to `culturemech:output/ingredient_occurrences.tsv`, with one occurrence
  across one CultureMech recipe.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/2-Hydroxypyridine.yaml data/ingredients/mapped/2-Keto-D-gluconic_Acid_Hemicalcium_Salt_Hydrate.yaml data/ingredients/mapped/2-Keto-D-gluconic_Acid_Hemicalcium_Salt_Monohydrate.yaml data/ingredients/mapped/2-Mercaptopyridine_N-oxide_Sodium_Salt.yaml data/ingredients/mapped/2-Nitrophenol.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/2-Nitrophenol.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `scripts/_engine_a_obo_safe.sh data/ingredients/mapped/2-Nitrophenol.yaml "CHEBI FOODON NCIT MESH UBERON ENVO BTO PATO"`:
  passed.
- Whole-corpus checks run earlier in this review pass passed; only the shared
  evidence validator was unavailable because `../culturebotai-claw` is absent.
- Per-record/aggregate comparison against `data/curated/mapped_ingredients.yaml`:
  normalized semantic equality passed.
- `mappings/ingredient_mappings.sssom.tsv` contains the expected exact
  `MIM:2-Nitrophenol` to `CHEBI:16260` row with restored CultureMech
  occurrence-table provenance.

## Evidence

- The active ChEBI target confirms the exact ontology identity.
- Minor: because the record was added after the May auto-classification passes,
  it still has no `ingredient_type` and no ChEBI-derived CAS, formula, InChI, or
  SMILES despite being a mapped single ChEBI chemical.
- The hidden/ignored-inclusive search over YAML, TSV, Markdown, ignored
  backups, and generated review output found the active YAML/aggregate/SSSOM
  rows and no unresolved active duplicate for `CHEBI:16260`.

## Completeness

- Empty component and role slots are acceptable for this single ChEBI chemical.
- `occurrence_statistics` is consistent with the CultureMech residual grounding:
  one occurrence across one recipe.
- Ingredient typing and chemistry backfill remain useful so this late-created
  record has parity with older ChEBI imports.

## Recommended Edits

1. In `data/ingredients/mapped/2-Nitrophenol.yaml`, add
   `ingredient_type: SINGLE_INGREDIENT` and ChEBI-derived CAS/formula/InChI/SMILES
   for `CHEBI:16260`.
2. Regenerate `data/curated/mapped_ingredients.yaml` and docs from the
   maintained YAML.
3. Re-run strict/LinkML validation and SSSOM export checks after the backfill.
