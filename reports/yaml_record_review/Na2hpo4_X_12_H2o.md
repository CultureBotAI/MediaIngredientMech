# `data/ingredients/mapped/Na2hpo4_X_12_H2o.yaml`

## Verdict

Needs curation - major. The exact `CHEBI:91259` disodium hydrogenphosphate
dodecahydrate identity, corrected CAS RN, hydrate formula, source-backed
`BUFFER` role, node-id repair, occurrence count, and final exact row pass, but
final SSSOM still publishes anhydrous disodium-phosphate aliases as synonyms of
the dodecahydrate and the stored InChI/SMILES still describe the anhydrous
parent.

## Identity

- Reviewed record: `data/ingredients/mapped/Na2hpo4_X_12_H2o.yaml`.
- Identifier and grounding: `identifier: CHEBI:91259` with
  `ontology_mapping.ontology_id: CHEBI:91259`, label
  `disodium hydrogenphosphate dodecahydrate`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 159 CultureMech recipe occurrences across 159 media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Na2edta2h2o` through `Na2hpo4_X_12_H2o`: exited 0 and wrote zero ERROR
  rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.

## Evidence

- A fresh EBI OLS4 lookup resolves `CHEBI:91259` as active
  `disodium hydrogenphosphate dodecahydrate`.
- Major: a fresh PubChem lookup for CAS RN `10039-32-4` resolves the
  dodecahydrate with twelve waters in the formula and InChI. The YAML has the
  dodecahydrate formula, but `chemical_properties.inchi` and
  `chemical_properties.smiles` are still the anhydrous `CHEBI:34683` structure.
- `reports/hydrate_grounding.tsv` classifies `CHEBI:91259` as
  `OK_HYDRATE_TERM`, and #554 corrected `kg_microbe_node_id` so the exported
  node ID now matches the specific ChEBI hydrate identifier.
- The 2026-09-12 hidden-hydrate cleanup correctly marks non-dodecahydrate
  sibling labels as rejected; the final SSSOM row no longer publishes the
  dihydrate, trihydrate, hexahydrate, heptahydrate, or monohydrate strings.
- The `physicochemical_roles.BUFFER` facet is source-backed by CultureMech raw
  role text naming `Buffer`.
- Major: final SSSOM still publishes `disodium acid orthophosphate`,
  `disodium monohydrogen phosphate`, and `disodium orthophosphate` as
  dodecahydrate synonyms. Those are anhydrous-parent names for
  `CHEBI:34683`, not exact names for `CHEBI:91259`.
- Minor: the active `ontology_mapping.evidence` list still contains superseded
  #321/#334/#342 notes about minting a local registry term and close-matching
  this record. Later history entries fixed that detour, but the stale evidence
  attached to the current exact ChEBI mapping is confusing.

## Completeness

- The active ChEBI target, corrected CAS RN, source-backed buffer role,
  159/159 occurrence count, corrected node ID, rejected sibling hydrate labels,
  and final exact row agree.
- The remaining consequential gaps are the anhydrous structure stored beside
  the dodecahydrate formula and cleanup of the anhydrous-parent labels that
  still reach final SSSOM `other`.

## Recommended Edits

- Major: in `data/ingredients/mapped/Na2hpo4_X_12_H2o.yaml`, mark the three
  anhydrous-parent labels as `REJECTED_LABEL` or otherwise keep them
  provenance-only, then rebuild final SSSOM and rerun the final SSSOM plus
  product label validators.
- Major: replace the inherited anhydrous InChI and SMILES with structure values
  that include twelve waters of hydration.
- Minor: prune or explicitly mark the superseded registry-mint and close-match
  `ontology_mapping.evidence` notes so the active exact ChEBI mapping carries
  only current evidence.
