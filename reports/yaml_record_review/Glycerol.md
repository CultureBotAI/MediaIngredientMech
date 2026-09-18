# `data/ingredients/mapped/Glycerol.yaml`

## Verdict

Needs curation. The CultureMech exact match to active `CHEBI:17754` glycerol,
the source-backed carbon-source role, the absorbed duplicate synonyms, and the
final SSSOM synonyms pass, but `ENERGY_SOURCE` remains an unsupported
computational role.

## Identity

- Reviewed record: `data/ingredients/mapped/Glycerol.yaml`.
- Identifier and grounding: `identifier: CHEBI:17754` with matching
  `ontology_mapping.ontology_id`, canonical label `glycerol`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS-RN `56-81-5`, formula `C3H8O3`, InChI
  `InChI=1S/C3H8O3/c4-1-3(6)2-5/h3-6H,1-2H2`, and SMILES `OCC(O)CO`.

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

- The matching active `Glycerol` aggregate entry carries the same ChEBI exact
  match, CultureMech occurrence count, CAS RN, formula, InChI, SMILES,
  source-backed carbon role, computational energy role, and singleton type as
  the per-record YAML. The aggregate also contains a separate rejected lowercase
  `glycerol` tombstone with the same identifier, so duplicate-identifier
  comparisons must include the preferred term.
- OLS4 resolves `CHEBI:17754` as `glycerol`, matching the YAML
  `ontology_mapping`.
- PubChem resolves CAS `56-81-5` to formula `C3H8O3`, IUPAC name
  `propane-1,2,3-triol`, and the same InChI as the record.
- The `CARBON_SOURCE` role is supported by `DATABASE_ENTRY` evidence from
  CultureMech and preserved original role text.
- Major: `nutritional_roles.ENERGY_SOURCE` is still backed only by
  `COMPUTATIONAL_PREDICTION` with a provisional curator note and no
  CultureMech or literature evidence for glycerol as an energy source.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps `MIM:Glycerol`
  to `CHEBI:17754` by `skos:exactMatch`; raw `Role: ...; Properties: ...`
  strings are correctly filtered from `other`, while curated glycerol synonyms
  and `CAS:56-81-5` remain.
- A hidden/ignored-inclusive search over `data`, `src`, `tests`, `mappings`,
  `reports`, and `.claude` found the active YAML, aggregate copies, final SSSOM
  row, OAK/OLS row-review confirmations, the rejected lowercase glycerol
  tombstone, generated indexes, old batch validation reports, and ignored
  aggregate backups.

## Completeness

- The exact glycerol identity, CAS RN, formula, InChI, SMILES, CultureMech
  occurrence count, source-backed carbon-source role, ingredient type, and final
  SSSOM row are populated.
- The energy-source role needs claim-level support or removal.

## Recommended Edits

- Major: remove `nutritional_roles.ENERGY_SOURCE` from
  `data/ingredients/mapped/Glycerol.yaml`, or replace the provisional
  computational evidence with inspected source evidence that specifically
  supports glycerol as an energy source.
