# `data/ingredients/mapped/Na2_Beta-glycerol_PO4_X_5_H2O.yaml`

## Verdict

Pass. The record is a curated local identity for disodium
beta-glycerophosphate pentahydrate, honestly maps that form narrower than
`CHEBI:15978` `sn-glycerol 3-phosphate`, and publishes both the ChEBI parent
and local registry rows with no unsupported `other` synonyms.

## Identity

- Reviewed record:
  `data/ingredients/mapped/Na2_Beta-glycerol_PO4_X_5_H2O.yaml`.
- Identifier and grounding: `identifier:
  kgmicrobe.compound:na2_beta-glycerol_po4_x_5_h2o` with
  `ontology_mapping.ontology_id: CHEBI:15978`, label
  `sn-glycerol 3-phosphate`, source `CHEBI`,
  `mapping_quality: NARROW_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 0 CultureMech recipe occurrences across 0 media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Na2_Alpha-ketoglutarate` through `Na2co3`: exited 0 and wrote zero ERROR
  rows.
- Direct `linkml-term-validator validate-data` exited 0 for the
  `CHEBI:15978` parent label.

## Evidence

- #296 classified this formerly unmapped surface as a known isolable disodium
  beta-glycerophosphate pentahydrate with no confirmed exact external ontology
  term, so minting a `kgmicrobe.compound` identifier and retaining
  `CHEBI:15978` as a narrow parent is the right Section 3 pattern.
- `reports/hydrate_grounding.tsv` classifies the local
  `kgmicrobe.compound:na2_beta-glycerol_po4_x_5_h2o` row as
  `OK_LOCAL_REGISTRY_ID` against the `CHEBI:15978` parent.
- The final SSSOM rows for `MIM:Na2_Beta-glycerol_PO4_X_5_H2O` include the
  `skos:narrowMatch` parent row and a sibling `skos:exactMatch` local registry
  row. Both rows leave `other` empty.

## Completeness

- The local identity, parent ChEBI term, #296 and #461 promotion provenance,
  zero occurrence count, empty role facets, empty chemical-properties block, and
  final SSSOM rows agree.
- CAS `13408-09-8` remains deliberately unresolved; the record does not assert
  it, and the local identity plus parent row preserve the hydrate boundary.

## Recommended Edits

- None.
