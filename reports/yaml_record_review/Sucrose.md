# `data/ingredients/mapped/Sucrose.yaml`

## Verdict

Needs curation - major. The exact `CHEBI:17992` identity, CAS, sucrose
structure, CultureMech carbon-source evidence, and occurrence count pass, but
`d-salicin` is exported as a sucrose synonym and provisional role facets remain.

## Identity

- Reviewed record: `data/ingredients/mapped/Sucrose.yaml`.
- Identifier and grounding: `identifier: CHEBI:17992` with
  `ontology_mapping.ontology_id: CHEBI:17992`, label `sucrose`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS `57-50-1`, formula `C12H22O11`, and ChEBI/PubChem
  InChI/SMILES values for sucrose.
- Occurrences: 233 occurrences across 233 CultureMech media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Sucrose` through `Sugars`: exited 0 and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI record.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh OLS4 lookup resolves active `CHEBI:17992` with label `sucrose`, CAS xref
  `57-50-1`, formula `C12H22O11`, and all exported sugar/saccharose names
  except `d-salicin`.
- PubChem resolves CAS `57-50-1` to `Sucrose` with the same formula and InChI.
- `mappings/culturemech_recipe_membership.tsv` has the 233 expected
  `CHEBI:17992` recipe rows, agreeing with `total_occurrences: 233` and
  `media_count: 233`.
- Major: `d-salicin` is an active exact synonym and is exported in SSSOM
  `other`, but a live PubChem lookup resolves `d-salicin` to salicin
  (`C13H18O7`), not sucrose.
- Major: `nutritional_roles.ENERGY_SOURCE` and the duplicate lower-confidence
  `nutritional_roles.CARBON_SOURCE` assertion are supported only by
  `COMPUTATIONAL_PREDICTION`. The record also has a source-backed
  `CARBON_SOURCE` entry from the original CultureMech role text; that entry
  supports the carbon-source role.

## Completeness

- The exact sucrose identity, CAS, structure, aggregate row, occurrence count,
  `D-Sucrose` merge, source-backed `CARBON_SOURCE`, and most final SSSOM
  synonyms agree.
- An ignored/hidden search of local curated, mapping, generated, report, source,
  and documentation paths found `d-salicin` only as a kg-microbe synonym on this
  Sucrose record and in its final generated synonym surfaces.

## Recommended Edits

- Major: in `data/ingredients/mapped/Sucrose.yaml`, retype or remove the
  `d-salicin` synonym so the final SSSOM row stops exporting salicin as a
  sucrose name.
- Major: remove the duplicate provisional `CARBON_SOURCE` assertion and either
  replace `ENERGY_SOURCE` with inspected evidence or remove the provisional
  energy-source role facet.
