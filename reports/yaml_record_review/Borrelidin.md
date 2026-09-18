# `data/ingredients/mapped/Borrelidin.yaml`

## Verdict

Needs curation, minor. The exact `CHEBI:78661` borrelidin identity, reviewed
MicrobeDecoder source occurrence, ChEBI structure fields, SSSOM row, and
aggregate copy all agree, but `chemical_properties.data_source` overstates
PubChem support for the stored stereochemical InChI.

## Identity

- Reviewed record: `data/ingredients/mapped/Borrelidin.yaml`.
- Identifier and grounding: `identifier: CHEBI:78661` with
  `ontology_mapping.ontology_id: CHEBI:78661`,
  `ontology_label: borrelidin`, `ontology_source: CHEBI`,
  `mapping_quality: EXACT_MATCH`, `ingredient_type: SINGLE_INGREDIENT`, and
  `mapping_status: MAPPED`.
- Live OLS exact search for `Borrelidin` returns `CHEBI:78661`; the ChEBI term
  has formula `C28H43NO6` and the same standard InChI and SMILES stored in
  `chemical_properties`.
- PubChem resolves `Borrelidin` to formula `C28H43NO6`, but its standard InChI
  has different stereochemistry than `CHEBI:78661` and the current MIM record.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Boldine.yaml data/ingredients/mapped/Borate.yaml data/ingredients/mapped/Borneol.yaml data/ingredients/mapped/Boron_Stock.yaml data/ingredients/mapped/Borrelidin.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Boldine.yaml data/ingredients/mapped/Borate.yaml data/ingredients/mapped/Borneol.yaml data/ingredients/mapped/Borrelidin.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for the four CHEBI-backed records in this batch.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K. Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- Hidden/ignored-inclusive search over `data/curated`, `mappings`,
  `data/custom`, and `reports`, excluding `data/curated/backups` and generated
  review directories, found the MicrobeDecoder raw label in
  `data/custom/microbedecoder/unmapped_labels.tsv`, the approved import-review
  row in `mappings/microbedecoder_auto_mapped_review.tsv`, the authoritative
  exact SSSOM row at `mappings/ingredient_mappings.sssom.tsv` row 620, and the
  aggregate copy in `data/curated/mapped_ingredients.yaml`.
- The local SSSOM row maps `MIM:Borrelidin` to `CHEBI:78661` with
  `skos:exactMatch`, matching the primary `identifier` and
  `ontology_mapping`.
- A parsed comparison against `data/curated/mapped_ingredients.yaml` found
  exactly one aggregate record with the same identifier and preferred term, and
  it is identical to this per-record YAML.

## Completeness

- The exact ChEBI identifier, MicrobeDecoder source occurrence, reviewed
  auto-import evidence, single-ingredient classification, formula, InChI,
  SMILES, SSSOM row, and aggregate copy are populated.
- Minor gap: `chemical_properties.data_source: ChEBI+PubChem` should be
  narrowed or the PubChem conflict should be documented, because the current
  stored InChI and SMILES are ChEBI-derived rather than supported by PubChem's
  current `Borrelidin` name result.

## Recommended Edits

- Minor: update the borrelidin chemical-property provenance in
  `data/ingredients/mapped/Borrelidin.yaml` so it cites ChEBI only or records
  the PubChem stereochemistry conflict, then run `just sync-curated` and
  focused strict/term validation.
