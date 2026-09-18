# `data/ingredients/mapped/Na2glycerophosphate5h2o.yaml`

## Verdict

Needs curation - major. The CAS-primary disodium glycerophosphate pentahydrate
identity, `CHEBI:15978` parent, 6/6 occurrence count, and final exact registry
rows pass, but final SSSOM publishes a generic glycerol-phosphate label and
CAS-decorated raw labels as synonyms of this CAS-specific pentahydrate.

## Identity

- Reviewed record: `data/ingredients/mapped/Na2glycerophosphate5h2o.yaml`.
- Identifier and grounding: `identifier: cas:13408-09-8` with
  `ontology_mapping.ontology_id: CHEBI:15978`, label
  `sn-glycerol 3-phosphate`, source `CHEBI`,
  `mapping_quality: NARROW_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 6 CultureMech recipe occurrences across 6 media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Na2edta2h2o` through `Na2hpo4_X_12_H2o`: exited 0 and wrote zero ERROR
  rows.
- Direct `linkml-term-validator validate-data` exited 0 for the
  `CHEBI:15978` parent label.

## Evidence

- A fresh EBI OLS4 lookup resolves `CHEBI:15978` as active
  `sn-glycerol 3-phosphate`. A fresh PubChem lookup for CAS RN `13408-09-8`
  resolves to a disodium glycerophosphate pentahydrate formula and InChI, so the
  CAS identity is narrower than the ChEBI parent.
- `reports/hydrate_grounding.tsv` classifies `cas:13408-09-8` as
  `OK_OWN_CAS_ID`; the final SSSOM keeps both an exact CAS row and an exact
  `kgmicrobe.compound` registry sibling beside the ChEBI parent row.
- Major: the final SSSOM `other` column still publishes `Glycerol 3-phosphate`
  and four parenthetical CAS raw labels. The first token erases the sodium
  pentahydrate boundary, and the parenthetical CAS labels are source strings,
  not canonical same-subject synonyms.

## Completeness

- The CAS identifier, ChEBI parent, #296/#461 promotion path, zero unsupported
  role facets, duplicate merge, 6/6 occurrence count, and final registry rows
  agree.
- The remaining consequential gap is the unsafe `other` payload on the parent
  final SSSOM row.

## Recommended Edits

- Major: demote `Glycerol 3-phosphate` and the CAS-decorated raw labels so they
  no longer publish as exact synonyms of `cas:13408-09-8`; preserve raw
  CultureMech labels as provenance-only evidence where useful. Rebuild final
  SSSOM and rerun the final SSSOM plus product label validators.
