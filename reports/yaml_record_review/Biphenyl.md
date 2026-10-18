# `data/ingredients/mapped/Biphenyl.yaml`

## Verdict

Pass. The exact `CHEBI:17097` biphenyl identity, reviewed MicrobeDecoder
provenance, structure fields, SSSOM row, occurrence count, and aggregate copy
all agree.

## Identity

- Reviewed record: `data/ingredients/mapped/Biphenyl.yaml`.
- Identifier and grounding: `identifier: CHEBI:17097` with
  `ontology_mapping.ontology_id: CHEBI:17097`,
  `ontology_label: biphenyl`, `ontology_source: CHEBI`,
  `mapping_quality: EXACT_MATCH`, `ingredient_type: SINGLE_INGREDIENT`, and
  `mapping_status: MAPPED`.
- PubChem resolves biphenyl to formula `C12H10` and the same standard InChI
  stored under `chemical_properties`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Bimuno.yaml data/ingredients/mapped/Biochanin_A_Diacetate.yaml data/ingredients/mapped/Biotin.yaml data/ingredients/mapped/Biotin_Vitamin_Solution.yaml data/ingredients/mapped/Biphenyl.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Bimuno.yaml data/ingredients/mapped/Biotin.yaml data/ingredients/mapped/Biphenyl.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for the NCIT/CHEBI records in this batch.
- Engine A term validation is intentionally skipped for the CAS registry record
  and the `kgmicrobe.ingredient` record. The previous full-corpus SSSOM
  validator passed, with Rule B4 skipped because sibling kg-microbe ontology
  transforms were absent.

## Evidence

- Hidden/ignored-inclusive search over `data/curated`, `mappings`,
  `data/custom`, and `reports`, excluding `data/curated/backups` and generated
  review directories, found the authoritative exact SSSOM row at
  `mappings/ingredient_mappings.sssom.tsv` row 600, the approved
  `mappings/microbedecoder_auto_mapped_review.tsv` row, and the aggregate copy
  in `data/curated/mapped_ingredients.yaml`.
- `mappings/culturemech_recipe_membership.tsv` contains 4 rows for
  `CHEBI:17097`, matching the record's refreshed 4/4 medium and total
  occurrence counts.
- A parsed comparison against `data/curated/mapped_ingredients.yaml` found
  exactly one aggregate record with the same identifier and preferred term, and
  it is identical to this per-record YAML.

## Completeness

- The exact CHEBI identifier, single-ingredient classification, formula, InChI,
  SMILES, SSSOM row, occurrence statistics, and aggregate copy are populated.

## Recommended Edits

- None.
