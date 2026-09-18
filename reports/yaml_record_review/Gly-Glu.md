# `data/ingredients/mapped/Gly-Glu.yaml`

## Verdict

Pass. The CultureBotHT exact match to active `CHEBI:73801` Gly-Glu is
structurally consistent, the MicrobeDecoder `Glycyl-l-glutamate` duplicate was
absorbed as the same neutral dipeptide, and the final SSSOM row exports only
same-record synonyms and CAS payload.

## Identity

- Reviewed record: `data/ingredients/mapped/Gly-Glu.yaml`.
- Identifier and grounding: `identifier: CHEBI:73801` with matching
  `ontology_mapping.ontology_id`, canonical label `Gly-Glu`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS-RN `7412-78-4`, formula `C7H12N2O5`, InChI, and
  SMILES.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Gly-Glu.yaml data/ingredients/mapped/Glycerate.yaml data/ingredients/mapped/Glycerol.yaml data/ingredients/mapped/Glycerol_2.yaml data/ingredients/mapped/Glycerol_3-phosphate.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Gly-Glu.yaml data/ingredients/mapped/Glycerate.yaml data/ingredients/mapped/Glycerol.yaml data/ingredients/mapped/Glycerol_2.yaml data/ingredients/mapped/Glycerol_3-phosphate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for all five ChEBI-primary records in the batch.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed;
  2951 records, 83 decompositions, 505 components, 0 violations.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 skipped because the
  sibling kg-microbe ontology transforms are not checked out.

## Evidence

- The matching aggregate `data/curated/mapped_ingredients.yaml` entry carries
  the same ChEBI exact match, CAS RN, formula, InChI, SMILES, exact synonym, and
  singleton type as the per-record YAML.
- OLS4 resolves `CHEBI:73801` as `Gly-Glu`, matching the YAML
  `ontology_mapping`.
- PubChem resolves CAS `7412-78-4` to formula `C7H12N2O5` and the same InChI as
  the record.
- The #213 duplicate absorption records that `Glycyl-l-glutamate` is the same
  neutral dipeptide represented by `CHEBI:73801`, not the `Gly-Glu(1-)` anion.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps `MIM:Gly-Glu` to
  `CHEBI:73801` by `skos:exactMatch` and keeps
  `glycyl-L-glutamic acid`, `Glycyl-l-glutamate`, and `CAS:7412-78-4` in
  `other`, all true synonyms for this subject.
- A hidden/ignored-inclusive search over `data`, `src`, `tests`, `mappings`,
  `reports`, and `.claude` found the active YAML, aggregate copies, final SSSOM
  row, OAK/OLS row-review confirmation, generated indexes, old batch validation
  reports, and ignored aggregate backups.

## Completeness

- The exact ChEBI identity, CAS RN, formula, InChI, SMILES, exact synonyms,
  ingredient type, and final SSSOM row are populated.

## Recommended Edits

- None.
