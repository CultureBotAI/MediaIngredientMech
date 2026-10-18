# `data/ingredients/mapped/Eudesmic_Acid.yaml`

## Verdict

Pass. The CAS-to-ChEBI lookup resolves eudesmic acid to active ChEBI
`3,4,5-trimethoxybenzoic acid`, the CAS structure matches PubChem, and the
final SSSOM row publishes only the same CAS RN in `other`.

## Identity

- Reviewed record: `data/ingredients/mapped/Eudesmic_Acid.yaml`.
- Identifier and grounding: `identifier: CHEBI:454991` with matching
  `ontology_mapping.ontology_id`, canonical label
  `3,4,5-trimethoxybenzoic acid`, source `CHEBI`,
  `mapping_quality: CAS_RN_LOOKUP`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- PubChem lookup by CAS RN `118-41-2` resolved to CID 8357 with formula
  `C10H12O5` and the same InChI recorded under `chemical_properties`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Ethylenediamine-NN-disuccinic_acid_EDDS.yaml data/ingredients/mapped/Ethylenediamine_N_N_Prime_Disuccinic_Acid.yaml data/ingredients/mapped/Ethylmalonic_Acid.yaml data/ingredients/mapped/Eudesmic_Acid.yaml data/ingredients/mapped/Eugenol.yaml --out /tmp/mim_edds_batch_strict.tsv`:
  exited 0 for the 5-file batch; the output TSV contained only its header.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Eudesmic_Acid.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.

## Evidence

- The matching `data/curated/mapped_ingredients.yaml` entry carries the same
  ChEBI identifier, CAS RN, formula, InChI, SMILES, CAS lookup grade, and
  regrade history as the per-record YAML.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:Eudesmic_Acid` to `CHEBI:454991` with `skos:exactMatch`; this is the
  record's own-identifier row, so Rule D allows the exact predicate while
  `mapping_quality` preserves `CAS_RN_LOOKUP` provenance.
- The row's only `other` token is `CAS:118-41-2`, which belongs to the same
  neutral eudesmic acid identity.
- A hidden/ignored-inclusive search over `data/ingredients`, `data/curated`,
  `mappings`, and `reports/yaml_record_review` for `MIM:Eudesmic_Acid`,
  `CHEBI:454991`, and `118-41-2` found the active YAML, aggregate copy, final
  SSSOM row, OAK/OLS row-review provenance, and expected generated indexes; it
  did not expose a contradictory active mapping.

## Completeness

- The exact identity, CAS RN, structure fields, and final SSSOM payload are
  populated.
- No unsupported synonyms, roles, components, source occurrences, or
  environmental contexts are asserted.

## Recommended Edits

- None.
