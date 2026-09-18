# `data/ingredients/mapped/Blasticidin_S.yaml`

## Verdict

Pass. The exact `CHEBI:15353` blasticidin S identity, reviewed MicrobeDecoder
source occurrence, structure fields, SSSOM row, and aggregate copy all agree.

## Identity

- Reviewed record: `data/ingredients/mapped/Blasticidin_S.yaml`.
- Identifier and grounding: `identifier: CHEBI:15353` with
  `ontology_mapping.ontology_id: CHEBI:15353`,
  `ontology_label: blasticidin S`, `ontology_source: CHEBI`,
  `mapping_quality: EXACT_MATCH`, `ingredient_type: SINGLE_INGREDIENT`, and
  `mapping_status: MAPPED`.
- Live OLS exact search for `Blasticidin S` returns `CHEBI:15353`, and the
  ChEBI term has formula `C17H26N8O5`, CAS `2079-00-7`, the same standard
  InChI, and the same SMILES stored in `chemical_properties`.
- PubChem resolves `Blasticidin S` to CID 170012 with formula `C17H26N8O5`
  and the same standard InChI stored in `chemical_properties`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Bis_3-aminopropylamine.yaml data/ingredients/mapped/Bisabolene.yaml data/ingredients/mapped/Bismuth_Iii_Chloride.yaml data/ingredients/mapped/Blasticidin_A.yaml data/ingredients/mapped/Blasticidin_S.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Bis_3-aminopropylamine.yaml data/ingredients/mapped/Bisabolene.yaml data/ingredients/mapped/Blasticidin_A.yaml data/ingredients/mapped/Blasticidin_S.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
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
  exact SSSOM row at `mappings/ingredient_mappings.sssom.tsv` row 610, and the
  aggregate copy in `data/curated/mapped_ingredients.yaml`.
- The local SSSOM row maps `MIM:Blasticidin_S` to `CHEBI:15353` with
  `skos:exactMatch`, matching the primary `identifier` and
  `ontology_mapping`.
- A parsed comparison against `data/curated/mapped_ingredients.yaml` found
  exactly one aggregate record with the same identifier and preferred term, and
  it is identical to this per-record YAML.

## Completeness

- The exact ChEBI identifier, MicrobeDecoder source occurrence, reviewed
  auto-import evidence, single-ingredient classification, formula, InChI,
  SMILES, SSSOM row, and aggregate copy are populated.

## Recommended Edits

- None.
