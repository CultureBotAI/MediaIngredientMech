# `data/ingredients/mapped/Bluensomycin.yaml`

## Verdict

Pass. The exact `CHEBI:81193` Bluensomycin identity, reviewed MicrobeDecoder
source occurrence, structure fields, SSSOM row, and aggregate copy all agree.

## Identity

- Reviewed record: `data/ingredients/mapped/Bluensomycin.yaml`.
- Identifier and grounding: `identifier: CHEBI:81193` with
  `ontology_mapping.ontology_id: CHEBI:81193`,
  `ontology_label: Bluensomycin`, `ontology_source: CHEBI`,
  `mapping_quality: EXACT_MATCH`, `ingredient_type: SINGLE_INGREDIENT`, and
  `mapping_status: MAPPED`.
- Live OLS exact search for `Bluensomycin` returns the single ChEBI hit
  `CHEBI:81193`, and the ChEBI term has formula `C21H39N5O14`, CAS
  `11011-72-6`, the same standard InChI, and the same SMILES stored in
  `chemical_properties`.
- PubChem resolves `Bluensomycin` to CID 20055290 with formula `C21H39N5O14`
  and the same standard InChI stored in `chemical_properties`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Bleomycin.yaml data/ingredients/mapped/Bleomycin_Sulfate.yaml data/ingredients/mapped/Blood.yaml data/ingredients/mapped/Bluensomycin.yaml data/ingredients/mapped/Bold_Trace_Stock.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Bleomycin.yaml data/ingredients/mapped/Bleomycin_Sulfate.yaml data/ingredients/mapped/Blood.yaml data/ingredients/mapped/Bluensomycin.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for the four OBO-backed records in this batch.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K. Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- Hidden/ignored-inclusive search over `data/curated`, `mappings`,
  `data/custom`, and `reports`, excluding `data/curated/backups` and generated
  review directories, found the MicrobeDecoder raw label in
  `data/custom/microbedecoder/unmapped_labels.tsv`, the approved import-review
  row in `mappings/microbedecoder_auto_mapped_review.tsv`, the authoritative
  exact SSSOM row at `mappings/ingredient_mappings.sssom.tsv` row 614, and the
  aggregate copy in `data/curated/mapped_ingredients.yaml`.
- The separate `Glebomycin` record also maps to an NCIT Bluensomycin term, but
  hidden/ignored-inclusive local search found no second `CHEBI:81193`
  Bluensomycin ingredient record.
- A parsed comparison against `data/curated/mapped_ingredients.yaml` found
  exactly one aggregate record with the same identifier and preferred term, and
  it is identical to this per-record YAML.

## Completeness

- The exact ChEBI identifier, MicrobeDecoder source occurrence, reviewed
  auto-import evidence, single-ingredient classification, formula, InChI,
  SMILES, SSSOM row, and aggregate copy are populated.

## Recommended Edits

- None.
