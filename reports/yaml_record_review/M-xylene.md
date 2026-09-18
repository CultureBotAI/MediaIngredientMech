# `data/ingredients/mapped/M-xylene.yaml`

## Verdict

Needs curation. The CultureMech exact CHEBI:28488 identity, CAS RN, ChEBI and
PubChem structure, curated synonyms, and final SSSOM row are consistent, but
`nutritional_roles.CARBON_SOURCE` is supported only by provisional in-session
LLM reasoning.

Severity: major.

## Identity

- Reviewed record: `data/ingredients/mapped/M-xylene.yaml`.
- Identifier and grounding: `identifier: CHEBI:28488` with
  `ontology_mapping.ontology_id: CHEBI:28488`, label `m-xylene`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS RN `108-38-3`, molecular formula `C8H10`, InChI,
  and SMILES.
- Occurrences: 9 total occurrences in 9 CultureMech recipes.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `M-inositol` through `MES_sodium_salt`: exited 0 and wrote zero ERROR rows.
- `uv run --frozen linkml-term-validator validate-data` exited 0 for the
  CHEBI-primary subset `M-inositol`, `M-xylene`, and `MES_sodium_salt`;
  `MES_Buffer` and `MES_Hydrat` were skipped because their primary identifiers
  use local and CAS prefixes outside the CHEBI/OBO term adapter scope.

## Evidence

- EBI OLS4 resolves `CHEBI:28488` as active `m-xylene`, lists CAS RN
  `108-38-3`, and records the same formula, InChI, and SMILES as the YAML
  record.
- PubChem resolves CAS RN `108-38-3` to CID `7929` with formula `C8H10` and the
  same InChI as the YAML record.
- The final SSSOM publishes one `skos:exactMatch` row to `CHEBI:28488`; its
  `other` field contains the curated exact synonyms and `CAS:108-38-3`.

## Completeness

- The active CHEBI identity, CAS RN, formula, structure block, occurrence
  count, aggregate copy, and final SSSOM row are present and consistent.
- The `CARBON_SOURCE` facet is based on `reference_type:
  COMPUTATIONAL_PREDICTION` with `reference_text: Assigned by in-session Claude
  reasoning (no external API)` and a curator note marking the role as
  provisional. No literature, database, or recipe evidence supports the
  asserted carbon-source activity in this record.

## Recommended Edits

- Curate evidence for `CARBON_SOURCE`, or remove the role if no supporting
  ingredient-level evidence is available.
