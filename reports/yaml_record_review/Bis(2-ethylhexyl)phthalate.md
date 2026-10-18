# `data/ingredients/mapped/Bis(2-ethylhexyl)phthalate.yaml`

## Verdict

Needs curation, minor. The exact `CHEBI:17747` bis(2-ethylhexyl)
phthalate identity, MicrobeDecoder raw label, structure fields, SSSOM row, and
aggregate copy all agree, but top-level `notes` still describe the old unmapped
state.

## Identity

- Reviewed record:
  `data/ingredients/mapped/Bis(2-ethylhexyl)phthalate.yaml`.
- Identifier and grounding: `identifier: CHEBI:17747` with
  `ontology_mapping.ontology_id: CHEBI:17747`,
  `ontology_label: bis(2-ethylhexyl) phthalate`,
  `ontology_source: CHEBI`, `mapping_quality: SYNONYM_MATCH`,
  `ingredient_type: SINGLE_INGREDIENT`, and `mapping_status: MAPPED`.
- Live OLS exact search for the raw `Bis(2-ethylhexyl)phthalate` label returns
  the single ChEBI hit `CHEBI:17747`, whose canonical label is
  `bis(2-ethylhexyl) phthalate` and whose synonym list includes the unspaced
  raw label.
- The OLS term and PubChem name lookup both return formula `C24H38O4` and the
  same standard InChI stored in `chemical_properties`.

## Validation

- `uv run --frozen python scripts/validate_strict.py 'data/ingredients/mapped/Bis(2-ethylhexyl)phthalate.yaml' data/ingredients/mapped/Bis-4-nitrophenyl-phenyl_Phosphonate.yaml data/ingredients/mapped/Bis-4-nitrophenyl-phosphorylcholine.yaml data/ingredients/mapped/Bis-4-nitrophenyl_Phosphate.yaml data/ingredients/mapped/Bis-tris.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data 'data/ingredients/mapped/Bis(2-ethylhexyl)phthalate.yaml' data/ingredients/mapped/Bis-4-nitrophenyl_Phosphate.yaml data/ingredients/mapped/Bis-tris.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for the three CHEBI-backed records in this batch.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K. Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- Hidden/ignored-inclusive search over `data/curated`, `mappings`,
  `data/custom`, and `reports`, excluding `data/curated/backups` and generated
  review directories, found the MicrobeDecoder raw label in
  `data/custom/microbedecoder/unmapped_labels.tsv`, the authoritative exact
  SSSOM row at `mappings/ingredient_mappings.sssom.tsv` row 601, and the
  aggregate copy in `data/curated/mapped_ingredients.yaml`.
- The local SSSOM row maps
  `MIM:Bis~282-ethylhexyl~29phthalate` to `CHEBI:17747` with
  `skos:exactMatch`, matching the primary `identifier` and
  `ontology_mapping`.
- A parsed comparison against `data/curated/mapped_ingredients.yaml` found
  exactly one aggregate record with the same identifier and preferred term, and
  it is identical to this per-record YAML.

## Completeness

- The exact ChEBI identifier, raw MicrobeDecoder synonym, single-ingredient
  classification, formula, InChI, SMILES, SSSOM row, source occurrence count,
  and aggregate copy are populated.
- Minor gap: top-level `notes` still say no CAS-RN or CHEBI/NCIT match was
  available and curator review was needed, even though the record has been
  promoted to `CHEBI:17747`.

## Recommended Edits

- Minor: replace the stale import note in
  `data/ingredients/mapped/Bis(2-ethylhexyl)phthalate.yaml` with a current
  sentence naming the accepted `CHEBI:17747` synonym match, then run
  `just sync-curated` and focused strict/term validation.
