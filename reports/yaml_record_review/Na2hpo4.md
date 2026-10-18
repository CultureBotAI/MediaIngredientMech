# `data/ingredients/mapped/Na2hpo4.yaml`

## Verdict

Needs curation - major. The exact `CHEBI:34683` disodium hydrogenphosphate
identity, CAS-backed structure, source-backed `BUFFER` role, duplicate merge,
occurrence count, and final exact row pass, but final SSSOM still publishes
malformed formula strings as exact synonyms.

## Identity

- Reviewed record: `data/ingredients/mapped/Na2hpo4.yaml`.
- Identifier and grounding: `identifier: CHEBI:34683` with
  `ontology_mapping.ontology_id: CHEBI:34683`, label
  `disodium hydrogenphosphate`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 1124 CultureMech recipe occurrences across 1121 media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Na2edta2h2o` through `Na2hpo4_X_12_H2o`: exited 0 and wrote zero ERROR
  rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.

## Evidence

- A fresh EBI OLS4 lookup resolves `CHEBI:34683` as active
  `disodium hydrogenphosphate`. A fresh PubChem lookup for CAS RN `7558-79-4`
  resolves to the same anhydrous disodium hydrogenphosphate formula and InChI
  stored in `chemical_properties`.
- The `physicochemical_roles.BUFFER` facet is supported by a
  `DATABASE_ENTRY` imported from CultureMech raw role text explicitly naming
  `Buffer`; unlike provisional name-pattern roles, this role evidence is placed
  on the narrow role claim.
- The 2026-09-12 hidden-hydrate cleanup correctly marks sibling hydrate labels
  as rejected, and those hydrate labels no longer appear in the final SSSOM
  row.
- Major: final SSSOM still publishes `Na HPO`, `Na HPO anydrous`, and
  `Na2H2PO4` as exact `Na2HPO4` synonyms. They are malformed formulas, not
  resolving surface forms for `CHEBI:34683`.
- Minor: the `PMID:38524547` literature evidence resolves through NCBI
  E-utilities and mentions `Na2HPO4`, but the study is a vascular-calcification
  cell-culture model rather than a media-ingredient grounding source; its own
  explanation still says the evidence was auto-proposed and needs curator
  rephrasing or removal.

## Completeness

- The active ChEBI target, canonical CAS RN, formula, structure, source-backed
  buffer role, 1124/1121 occurrence count, duplicate merge, rejected hydrate
  aliases, and final exact row agree.
- The remaining consequential gap is cleanup of the malformed exact synonyms
  that still reach final SSSOM `other`.

## Recommended Edits

- Major: demote `Na HPO`, `Na HPO anydrous`, and `Na2H2PO4` to
  `REJECTED_LABEL` or otherwise filter them from final SSSOM. Rebuild final
  SSSOM and rerun the final SSSOM plus product label validators.
- Minor: remove or rephrase the `PMID:38524547` auto-proposed evidence object
  so identity evidence relies on database matching rather than an incidental
  cell-culture paper.
