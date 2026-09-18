# `data/ingredients/mapped/Na2hpo4_X_2_H2o.yaml`

## Verdict

Needs curation - major. The exact `CHEBI:91258` disodium hydrogenphosphate
dihydrate identity, corrected CAS RN, source-backed `BUFFER` role, node-id
repair, occurrence count, and final exact row pass, but the stored InChI and
SMILES still describe the anhydrous parent rather than the dihydrate.

## Identity

- Reviewed record: `data/ingredients/mapped/Na2hpo4_X_2_H2o.yaml`.
- Identifier and grounding: `identifier: CHEBI:91258` with
  `ontology_mapping.ontology_id: CHEBI:91258`, label
  `disodium hydrogenphosphate dihydrate`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 304 CultureMech recipe occurrences across 304 media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Na2hpo4_X_2_H2o` through `Na2moo4`: exited 0 and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.

## Evidence

- A fresh EBI OLS4 lookup resolves `CHEBI:91258` as active
  `disodium hydrogenphosphate dihydrate`.
- `reports/hydrate_grounding.tsv` classifies `CHEBI:91258` as
  `OK_HYDRATE_TERM`, and #554 corrected `kg_microbe_node_id` so the exported
  node ID now matches the specific ChEBI hydrate identifier.
- Major: a fresh PubChem lookup for CAS RN `10028-24-7` resolves the dihydrate
  with two waters in the formula and InChI. The YAML has the hydrate formula,
  but `chemical_properties.inchi` and `chemical_properties.smiles` are still the
  anhydrous `CHEBI:34683` structure.
- The final SSSOM row maps exactly to `CHEBI:91258`, publishes the corrected
  CAS RN, and keeps only dihydrate spelling variants in `other`.
- Minor: the active `ontology_mapping.evidence` list still contains superseded
  #321/#334/#342 notes about minting a local registry term and close-matching
  this record. Later history entries fixed that detour, but the stale evidence
  attached to the current exact ChEBI mapping is confusing.

## Completeness

- The active ChEBI target, corrected CAS RN, source-backed buffer role, 304/304
  occurrence count, corrected node ID, rejected sibling hydrate labels, and
  final exact row agree.
- The remaining consequential gap is the anhydrous structure stored beside the
  dihydrate formula.

## Recommended Edits

- Major: in `data/ingredients/mapped/Na2hpo4_X_2_H2o.yaml`, replace the
  inherited anhydrous InChI and SMILES with structure values that include two
  waters of hydration. Rerun strict validation and final product validation.
- Minor: prune or explicitly mark the superseded registry-mint and close-match
  `ontology_mapping.evidence` notes so the active exact ChEBI mapping carries
  only current evidence.
