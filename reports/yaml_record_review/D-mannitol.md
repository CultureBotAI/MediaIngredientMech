# `data/ingredients/mapped/D-mannitol.yaml`

## Verdict

Needs curation. The `CHEBI:16899` D-mannitol identity, CAS, formula, structure,
35/35 CultureMech count, and most final SSSOM synonyms pass, but the record has
a provisional computational carbon-source role and the final SSSOM exports
`dulcite`, which PubChem resolves to galactitol rather than D-mannitol.

## Identity

- Reviewed record: `data/ingredients/mapped/D-mannitol.yaml`.
- Identifier and grounding: `identifier: CHEBI:16899` with
  `ontology_mapping.ontology_id: CHEBI:16899`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Local OAK resolves `CHEBI:16899` to `D-mannitol` with formula `C6H14O6`,
  charge `0`, InChI, SMILES, CAS `69-65-8`, and exact D-mannitol synonyms,
  matching the stored `kg_microbe_node_id` and chemistry block.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/D-histidine.yaml data/ingredients/mapped/D-limonene.yaml data/ingredients/mapped/D-malate.yaml data/ingredients/mapped/D-mannitol.yaml data/ingredients/mapped/D-mannose.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/D-histidine.yaml data/ingredients/mapped/D-malate.yaml data/ingredients/mapped/D-mannitol.yaml data/ingredients/mapped/D-mannose.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed the 4-file CHEBI subset. `D-limonene` was skipped because its `cas:`
  fallback crashes the OAK SQL label lookup with
  `sqlite3.OperationalError: no such table: rdfs_label_statement`.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:27947 CHEBI:15588 CHEBI:16899 CHEBI:16024`:
  returned formula, charge, CAS, InChI, SMILES, mass, synonyms, and xrefs for
  `CHEBI:16899`.
- `curl -L ... /compound/name/dulcite/property/.../JSON`: PubChem resolved
  `dulcite` to `Galactitol` with InChIKey `FBPFZTCFMRRESA-GUCUJZIJSA-N`, not
  to the D-mannitol InChIKey `FBPFZTCFMRRESA-KVTDHHQDSA-N`.
- `curl -L ... q=dulcite&ontology=chebi&exact=true`: OLS returned
  `CHEBI:16899`, preserving a live registry conflict for that synonym.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- `mappings/culturemech_recipe_membership.tsv` contains 35 rows for
  `CHEBI:16899`, matching `occurrence_statistics.media_count: 35` and
  `total_occurrences: 35`.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:D-mannitol` to `CHEBI:16899` with `skos:exactMatch`, canonical object
  label `D-mannitol`, CHEBI object source, CAS `69-65-8`, and a kg-microbe /
  ChEBI synonym payload in `other`.
- Most `other` tokens are ChEBI synonyms for `CHEBI:16899`, but `dulcite` is
  suspect: OLS keeps it on `CHEBI:16899` while PubChem resolves the same label
  to galactitol, a different stereoisomer.
- The `CARBON_SOURCE` role is supported only by a
  `COMPUTATIONAL_PREDICTION` evidence object whose curator note says the role
  was inferred from ChEBI ancestry and recommends review.

## Completeness

- The hidden/ignored-inclusive exact-identifier search over active `data`
  surfaces found no second primary record for `CHEBI:16899`; the only other
  active data hit is `NLDM_metabolites`, where D-mannitol is a mixture
  component.
- CAS, formula, InChI, SMILES, occurrence statistics, and kg-microbe node id are
  populated.
- No mixture decomposition is required for the free D-mannitol record.

## Recommended Edits

- Decide whether `dulcite` should be removed from
  `data/ingredients/mapped/D-mannitol.yaml` despite the live ChEBI synonym, or
  whether the conflict should be escalated upstream to ChEBI before continuing
  to publish it in final SSSOM `other`.
- Remove the provisional `CARBON_SOURCE` role or replace its
  `COMPUTATIONAL_PREDICTION` evidence with inspected claim-level evidence.
- Regenerate synchronized curated and SSSOM products, then rerun
  `uv run --frozen python scripts/validate_strict.py`,
  `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/D-mannitol.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`,
  and `uv run --frozen python scripts/validate_sssom_invariants.py`.
