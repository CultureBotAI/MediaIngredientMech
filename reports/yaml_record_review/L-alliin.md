# `data/ingredients/mapped/L-alliin.yaml`

## Verdict

Needs curation. The CAS-to-ChEBI identity, active CHEBI:2596 grounding, curated
IUPAC synonym, PubChem structure, and final SSSOM row pass, but
`AMINO_ACID_SOURCE` is only a provisional CHEBI-ancestry inference.

## Identity

- Reviewed record: `data/ingredients/mapped/L-alliin.yaml`.
- Identifier and grounding: `identifier: CHEBI:2596` with
  `ontology_mapping.ontology_id: CHEBI:2596`, label `alliin`, source `CHEBI`,
  `mapping_quality: CAS_RN_LOOKUP`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS RN `556-27-4`, molecular formula `C6H11NO3S`,
  InChI, and SMILES.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/L-alanylglycine.yaml data/ingredients/mapped/L-alliin.yaml data/ingredients/mapped/L-alpha-Phosphatidylcholine.yaml data/ingredients/mapped/L-arginine.yaml data/ingredients/mapped/L-arginine_X_Hcl.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- Engine A LinkML term validation passed for all 5 ChEBI records.

## Evidence

- EBI OLS4 resolves `CHEBI:2596` as active `alliin`, lists CAS `556-27-4`, and
  includes the curated IUPAC synonym
  `3-[(S)-prop-2-ene-1-sulfinyl]-L-alanine`.
- PubChem resolves CAS RN `556-27-4` to CID `9576089` with formula
  `C6H11NO3S` and the same InChI as the YAML record.
- The final SSSOM publishes one `skos:exactMatch` row to `CHEBI:2596` with the
  curated ChEBI synonym and `CAS:556-27-4` in `other`; both tokens denote the
  same alliin identity.
- Major: `nutritional_roles.AMINO_ACID_SOURCE` is backed only by
  `COMPUTATIONAL_PREDICTION` evidence from CHEBI ancestry and says review is
  recommended. Class ancestry can propose this role, but the record still lacks
  inspected source evidence that alliin was used as an amino-acid source in a
  medium.
- The hidden and ignored-inclusive search over `data`, `mappings`, `reports`,
  `docs`, `src`, and `tests` found the current YAML, aggregate copy, final
  SSSOM row, CAS lookup history, docs projections, and the old synonym-enrich
  review row.

## Completeness

- The exact ChEBI identity, CAS RN, structure, SSSOM synonym payload, and
  aggregate copy are complete enough.
- The amino-acid role remains provisional until a curator either sources it to
  a medium-level claim or removes it.

## Recommended Edits

- Major: either replace
  `nutritional_roles.AMINO_ACID_SOURCE` in
  `data/ingredients/mapped/L-alliin.yaml` with source-backed evidence for this
  exact compound, or remove the provisional role; then sync the aggregate copy
  and rerun strict, term, round-trip, component, and SSSOM validation.
