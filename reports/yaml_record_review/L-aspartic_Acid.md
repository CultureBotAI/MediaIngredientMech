# `data/ingredients/mapped/L-aspartic_Acid.yaml`

## Verdict

Needs curation. The CultureMech exact ChEBI identity, CAS value, PubChem
structure, occurrence count, and final SSSOM row pass, but `AMINO_ACID_SOURCE`
is only a provisional CHEBI-ancestry inference.

## Identity

- Reviewed record: `data/ingredients/mapped/L-aspartic_Acid.yaml`.
- Identifier and grounding: `identifier: CHEBI:17053` with
  `ontology_mapping.ontology_id: CHEBI:17053`, label `L-aspartic acid`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS RN `56-84-8`, molecular formula `C4H7NO4`, InChI,
  and SMILES.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/L-ascorbic_Acid.yaml data/ingredients/mapped/L-asparagine.yaml data/ingredients/mapped/L-aspartate.yaml data/ingredients/mapped/L-aspartic_Acid.yaml data/ingredients/mapped/L-citrulline.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- Engine A LinkML term validation passed for all 5 ChEBI records.

## Evidence

- EBI OLS4 resolves `CHEBI:17053` as active `L-aspartic acid`, lists CAS
  `56-84-8`, and includes the exact and related ChEBI synonyms exported for
  this record.
- PubChem resolves CAS RN `56-84-8` to CID `5960` with formula `C4H7NO4` and
  the same InChI as the YAML record.
- The final SSSOM publishes one `skos:exactMatch` row to `CHEBI:17053` with
  curated synonyms and `CAS:56-84-8` in `other`; every exported token resolves
  on the same ChEBI identity.
- Major: `nutritional_roles.AMINO_ACID_SOURCE` is backed only by
  `COMPUTATIONAL_PREDICTION` evidence from CHEBI ancestry and says review is
  recommended. Class ancestry can propose this role, but the record still lacks
  inspected source evidence that L-aspartic acid was used as an amino-acid
  source in a medium.
- The hidden and ignored-inclusive search over `data`, `mappings`, `reports`,
  `docs`, `src`, and `tests` found the current YAML, aggregate copy, final
  SSSOM row, docs projections, and OAK/OLS row-review confirmation.

## Completeness

- The exact ChEBI identity, CAS RN, structure, occurrence count, and aggregate
  copy are present and consistent.
- The amino-acid role remains provisional until a curator either sources it to
  a medium-level claim or removes it.

## Recommended Edits

- Major: either replace
  `nutritional_roles.AMINO_ACID_SOURCE` in
  `data/ingredients/mapped/L-aspartic_Acid.yaml` with source-backed evidence
  for this exact compound, or remove the provisional role; then sync the
  aggregate copy and rerun strict, term, round-trip, component, and SSSOM
  validation.
