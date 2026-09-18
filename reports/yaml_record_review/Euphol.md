# `data/ingredients/mapped/Euphol.yaml`

## Verdict

Pass. The CultureBotHT CAS-derived euphol identity agrees with active ChEBI,
PubChem confirms the recorded structure, and the final SSSOM `other` token is
safe.

## Identity

- Reviewed record: `data/ingredients/mapped/Euphol.yaml`.
- Identifier and grounding: `identifier: CHEBI:4940` with matching
  `ontology_mapping.ontology_id`, canonical label `Euphol`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- PubChem lookup by CAS RN `514-47-6` resolved to CID 441678 with formula
  `C30H50O` and the same InChI recorded under `chemical_properties`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Eugon_agar_BD-Difco.yaml data/ingredients/mapped/Euphol.yaml data/ingredients/mapped/Eurocidin.yaml data/ingredients/mapped/Europium_Iii_Chloride.yaml data/ingredients/mapped/Exfoliatin.yaml --out /tmp/mim_eug_batch_strict.tsv`:
  exited 0 for the 5-file batch; the output TSV contained only its header.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Euphol.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.

## Evidence

- The matching `data/curated/mapped_ingredients.yaml` entry carries the same
  ChEBI identifier, CAS RN, formula, InChI, SMILES, and auto-classification
  history as the per-record YAML.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps `MIM:Euphol`
  to `CHEBI:4940` with `skos:exactMatch`; the `CAS:514-47-6` `other` token
  denotes the same compound.
- A hidden/ignored-inclusive search over `data/ingredients`, `data/curated`,
  `mappings`, and `reports/yaml_record_review` for `MIM:Euphol`,
  `CHEBI:4940`, and `514-47-6` found the active YAML, aggregate copy, final
  SSSOM row, row-review provenance, and ignored aggregate backups; it did not
  expose a contradictory active mapping.

## Completeness

- The exact identity, CAS RN, structure fields, and final SSSOM payload are
  populated.
- No unsupported roles, components, source occurrences, or environmental
  contexts are asserted.

## Recommended Edits

- None.
