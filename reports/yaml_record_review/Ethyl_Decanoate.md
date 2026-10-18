# `data/ingredients/mapped/Ethyl_Decanoate.yaml`

## Verdict

Pass. The CultureBotHT CAS-derived ethyl decanoate identity agrees with active
ChEBI, the recorded structure matches PubChem, and the final SSSOM row carries
only the same CAS RN in `other`.

## Identity

- Reviewed record: `data/ingredients/mapped/Ethyl_Decanoate.yaml`.
- Identifier and grounding: `identifier: CHEBI:87430` with matching
  `ontology_mapping.ontology_id`, canonical label `ethyl decanoate`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- PubChem lookup by CAS RN `110-38-3` resolved to CID 8048 with formula
  `C12H24O2` and the same InChI recorded under `chemical_properties`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Ethyl_Decanoate.yaml data/ingredients/mapped/Ethyl_Methyl_Sulfide.yaml data/ingredients/mapped/Ethyl_octanoate.yaml data/ingredients/mapped/Ethylene_Glycol.yaml data/ingredients/mapped/Ethylenediamine-NN-disuccinic_Acid.yaml --out /tmp/mim_ethyl_batch_strict.tsv`:
  exited 0 for the 5-file batch; the output TSV contained only its header.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Ethyl_Decanoate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.

## Evidence

- The matching `data/curated/mapped_ingredients.yaml` entry carries the same
  ChEBI identifier, CAS RN, formula, InChI, and SMILES as the per-record YAML.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:Ethyl_Decanoate` to `CHEBI:87430` with `skos:exactMatch` and
  `CAS:110-38-3`, which belongs to ethyl decanoate, as its only `other` token.
- A hidden/ignored-inclusive search over `data/ingredients`, `data/curated`,
  `mappings`, and `reports/yaml_record_review` for `MIM:Ethyl_Decanoate`,
  `CHEBI:87430`, and `110-38-3` found the active YAML, aggregate copy, final
  SSSOM row, OAK/OLS row-review provenance, and expected generated indexes; it
  did not expose a contradictory active mapping.

## Completeness

- The exact identity, CAS RN, structure fields, and final SSSOM payload are
  populated.
- No unsupported synonyms, roles, components, source occurrences, or
  environmental contexts are asserted.

## Recommended Edits

- None.
