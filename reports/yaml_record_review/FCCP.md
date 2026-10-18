# `data/ingredients/mapped/FCCP.yaml`

## Verdict

Pass. The CultureBotHT CAS lookup resolved to the active ChEBI FCCP term,
PubChem confirms the recorded structure, and the final SSSOM `other` tokens
are safe.

## Identity

- Reviewed record: `data/ingredients/mapped/FCCP.yaml`.
- Identifier and grounding: `identifier: CHEBI:75458` with matching
  `ontology_mapping.ontology_id`, canonical label
  `carbonyl cyanide p-trifluoromethoxyphenylhydrazone`, source `CHEBI`,
  `mapping_quality: CAS_RN_LOOKUP`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- PubChem lookup by CAS RN `370-86-5` resolved to CID 3330 with formula
  `C10H5F3N4O` and the same InChI recorded under `chemical_properties`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Exopolysaccharide.yaml data/ingredients/mapped/FCCP.yaml data/ingredients/mapped/FSL.yaml data/ingredients/mapped/Fad.yaml data/ingredients/mapped/Farm_soil.yaml --out /tmp/mim_f_batch_strict.tsv`:
  exited 0 for the 5-file batch; the output TSV contained only its header.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Exopolysaccharide.yaml data/ingredients/mapped/FCCP.yaml data/ingredients/mapped/Fad.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for the CHEBI subset in this mixed batch.

## Evidence

- The matching `data/curated/mapped_ingredients.yaml` entry carries the same
  ChEBI identifier, CAS RN, formula, InChI, SMILES, exact synonym, and
  regraded CAS-lookup provenance as the per-record YAML.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps `MIM:FCCP` to
  `CHEBI:75458` with `skos:exactMatch`; the
  `{[4-(trifluoromethoxy)phenyl]hydrazono}malononitrile` and `CAS:370-86-5`
  `other` tokens both denote FCCP.
- `mappings/ingredient_mappings_row_review_manifest.tsv` confirms that the
  OAK/OLS row review found no curation action for the CHEBI mapping.
- A hidden/ignored-inclusive search over `data/ingredients`, `data/curated`,
  `mappings`, and `reports/yaml_record_review` for `MIM:FCCP`,
  `CHEBI:75458`, `FCCP`, and `370-86-5` found the active YAML, aggregate copy,
  final SSSOM row, row-review provenance, and ignored aggregate backups; it
  did not expose a contradictory active mapping.

## Completeness

- The CAS lookup identity, CAS RN, structure fields, exact synonym, ingredient
  type, and final SSSOM payload are populated.
- No unsupported roles, components, source occurrences, or environmental
  contexts are asserted.

## Recommended Edits

- None.
