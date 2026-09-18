# `data/ingredients/mapped/Ethylene_Glycol.yaml`

## Verdict

Needs curation, with a major role-evidence issue. The ChEBI identity, CAS RN,
structure, CultureMech occurrences, and final SSSOM synonym payload pass, but
`CARBON_SOURCE` is asserted only from provisional in-session LLM reasoning.

## Identity

- Reviewed record: `data/ingredients/mapped/Ethylene_Glycol.yaml`.
- Identifier and grounding: `identifier: CHEBI:30742` with matching
  `ontology_mapping.ontology_id`, canonical label `ethylene glycol`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, 26
  CultureMech occurrences, and `ingredient_type: SINGLE_INGREDIENT`.
- PubChem lookup by CAS RN `107-21-1` resolved to CID 174 with formula
  `C2H6O2` and the same InChI recorded under `chemical_properties`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Ethyl_Decanoate.yaml data/ingredients/mapped/Ethyl_Methyl_Sulfide.yaml data/ingredients/mapped/Ethyl_octanoate.yaml data/ingredients/mapped/Ethylene_Glycol.yaml data/ingredients/mapped/Ethylenediamine-NN-disuccinic_Acid.yaml --out /tmp/mim_ethyl_batch_strict.tsv`:
  exited 0 for the 5-file batch; the output TSV contained only its header.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Ethylene_Glycol.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.

## Evidence

- The matching `data/curated/mapped_ingredients.yaml` entry carries the same
  ChEBI identifier, CAS RN, formula, InChI, SMILES, active synonyms, refreshed
  occurrence count, and carbon-source role as the per-record YAML.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:Ethylene_Glycol` to `CHEBI:30742` with `skos:exactMatch`; every `other`
  token is either an active synonym on the MIM record or `CAS:107-21-1`.
- `mappings/culturemech_recipe_membership.tsv` has 26 rows for `CHEBI:30742`,
  matching `occurrence_statistics`.
- Major: `nutritional_roles.CARBON_SOURCE` is asserted only from
  `COMPUTATIONAL_PREDICTION` with `reference_text: Assigned by in-session
  Claude reasoning (no external API)` and a provisional curator note. That
  evidence does not by itself establish a source-backed carbon-source role for
  ethylene glycol.
- A hidden/ignored-inclusive search over `data/ingredients`, `data/curated`,
  `mappings`, and `reports/yaml_record_review` for `MIM:Ethylene_Glycol`,
  `CHEBI:30742`, and `107-21-1` found the active YAML, aggregate copy, final
  SSSOM row, CultureMech occurrence rows, OAK/OLS row-review provenance, and
  ignored aggregate backups; it did not expose a contradictory active mapping.

## Completeness

- The exact identity, CAS RN, structure fields, occurrence count, exact
  synonyms, and final SSSOM payload are populated.
- Components and environmental contexts are correctly empty.

## Recommended Edits

- Major: in `data/ingredients/mapped/Ethylene_Glycol.yaml`, either replace the
  computational `CARBON_SOURCE` evidence with direct, source-backed media-role
  evidence for ethylene glycol, or remove the role facet; then sync
  `data/curated/mapped_ingredients.yaml` and rerun strict validation plus the
  final SSSOM gates.
