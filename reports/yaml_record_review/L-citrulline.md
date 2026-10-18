# `data/ingredients/mapped/L-citrulline.yaml`

## Verdict

Needs curation. The CAS-to-ChEBI identity, active CHEBI:16349 grounding,
PubChem structure, occurrence count, and final SSSOM row pass, but
`AMINO_ACID_SOURCE` is only a provisional CHEBI-ancestry inference.

## Identity

- Reviewed record: `data/ingredients/mapped/L-citrulline.yaml`.
- Identifier and grounding: `identifier: CHEBI:16349` with
  `ontology_mapping.ontology_id: CHEBI:16349`, label `L-citrulline`, source
  `CHEBI`, `mapping_quality: CAS_RN_LOOKUP`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS RN `372-75-8`, molecular formula `C6H13N3O3`,
  InChI, and SMILES.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/L-ascorbic_Acid.yaml data/ingredients/mapped/L-asparagine.yaml data/ingredients/mapped/L-aspartate.yaml data/ingredients/mapped/L-aspartic_Acid.yaml data/ingredients/mapped/L-citrulline.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- Engine A LinkML term validation passed for all 5 ChEBI records.

## Evidence

- EBI OLS4 exact search for `L-citrulline` returns active `CHEBI:16349`
  with label `L-citrulline` and the exact and related ChEBI synonyms exported
  for this record. The direct term URL for `CHEBI:16349` returned 404 in this
  session, so the exact search result plus Engine A term validation were used
  to verify the current OLS identity.
- PubChem resolves CAS RN `372-75-8` to CID `9750` with formula `C6H13N3O3`
  and the same InChI as the YAML record.
- The final SSSOM publishes one `skos:exactMatch` row to `CHEBI:16349` with
  curated synonyms and `CAS:372-75-8` in `other`; every exported token resolves
  on the same ChEBI identity.
- Major: `nutritional_roles.AMINO_ACID_SOURCE` is backed only by
  `COMPUTATIONAL_PREDICTION` evidence from CHEBI ancestry and says review is
  recommended. Class ancestry can propose this role, but the record still lacks
  inspected source evidence that L-citrulline was used as an amino-acid source
  in a medium.
- The hidden and ignored-inclusive search over `data`, `mappings`, `reports`,
  `docs`, `src`, and `tests` found the current YAML, aggregate copy, final
  SSSOM row, docs projections, alias rows for the older `MIM:L_Citrulline`
  spelling, and OAK/OLS row-review confirmation.

## Completeness

- The exact ChEBI identity, CAS RN, structure, occurrence count, and aggregate
  copy are present and consistent.
- The amino-acid role remains provisional until a curator either sources it to
  a medium-level claim or removes it.

## Recommended Edits

- Major: either replace
  `nutritional_roles.AMINO_ACID_SOURCE` in
  `data/ingredients/mapped/L-citrulline.yaml` with source-backed evidence for
  this exact compound, or remove the provisional role; then sync the aggregate
  copy and rerun strict, term, round-trip, component, and SSSOM validation.
