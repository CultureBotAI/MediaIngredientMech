# `data/ingredients/mapped/Biochanin_A_Diacetate.yaml`

## Verdict

Pass. The CAS fallback identity, registry SSSOM row, lack of a current CHEBI
term, single-ingredient classification, and aggregate copy all agree.

## Identity

- Reviewed record: `data/ingredients/mapped/Biochanin_A_Diacetate.yaml`.
- Identifier and grounding: `identifier: cas:54443-59-3` with
  `ontology_mapping.ontology_id: cas:54443-59-3`,
  `ontology_label: Biochanin a diacetate`, `ontology_source: CAS`,
  `mapping_quality: FALLBACK_REGISTRY`, `ingredient_type: SINGLE_INGREDIENT`,
  and `mapping_status: MAPPED`.
- Live OLS search in ChEBI finds no `Biochanin a diacetate` class, so the CAS
  registry fallback remains appropriate.
- PubChem resolves CAS `54443-59-3` to formula `C20H16O7` and a
  Biochanin-a-diacetate structure.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Bimuno.yaml data/ingredients/mapped/Biochanin_A_Diacetate.yaml data/ingredients/mapped/Biotin.yaml data/ingredients/mapped/Biotin_Vitamin_Solution.yaml data/ingredients/mapped/Biphenyl.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Bimuno.yaml data/ingredients/mapped/Biotin.yaml data/ingredients/mapped/Biphenyl.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for the NCIT/CHEBI records in this batch.
- Engine A term validation is intentionally skipped for this CAS registry
  record; `cas:` is not an OBO prefix. The previous full-corpus SSSOM validator
  passed, with Rule B4 skipped because sibling kg-microbe ontology transforms
  were absent.

## Evidence

- Hidden/ignored-inclusive search over `data/curated`, `mappings`,
  `data/custom`, and `reports`, excluding `data/curated/backups` and generated
  review directories, found the authoritative exact CAS registry SSSOM row at
  `mappings/ingredient_mappings.sssom.tsv` row 596, the expected CAS registry
  triage row in `mappings/ingredient_mappings_unknown_term_triage.tsv`, and the
  aggregate copy in `data/curated/mapped_ingredients.yaml`.
- A parsed comparison against `data/curated/mapped_ingredients.yaml` found
  exactly one aggregate record with the same identifier and preferred term, and
  it is identical to this per-record YAML.

## Completeness

- The CAS primary identifier, CAS chemical property, single-ingredient
  classification, registry SSSOM row, zero occurrence count, and aggregate copy
  are populated.
- No parent CHEBI row should be forced unless a curator identifies a precise
  broader class; the bounded live ChEBI search did not find a form-specific
  exact term.

## Recommended Edits

- None.
