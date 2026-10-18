# `data/ingredients/mapped/Maltohexaose.yaml`

## Verdict

Needs curation. The exact ChEBI identity, CAS number, ChEBI structure, exact
IUPAC synonym, and final SSSOM row pass, but `CARBON_SOURCE` is still
supported only by provisional ChEBI-ancestry evidence.

Severity: major.

## Identity

- Reviewed record: `data/ingredients/mapped/Maltohexaose.yaml`.
- Identifier and grounding: `identifier: CHEBI:27445` with
  `ontology_mapping.ontology_id: CHEBI:27445`, label `maltohexaose`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: zero CultureMech recipe occurrences.
- Chemical identity: `cas_rn: 34620-77-4`, formula `C36H62O31`, InChI and
  SMILES copied from ChEBI.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Malt_Extract_Broth` through `Maltose`: exited 0 and wrote zero ERROR rows.
- `uv run --frozen linkml-term-validator validate-data` exited 0 for this
  CHEBI-primary record.

## Evidence

- EBI OLS4 resolves `CHEBI:27445` as active `maltohexaose` with CAS
  `34620-77-4`, formula `C36H62O31`, and the same InChI and SMILES carried in
  the YAML.
- ChEBI carries the exported long-form IUPAC string as an exact synonym.
- The final SSSOM publishes one `skos:exactMatch` row from `MIM:Maltohexaose`
  to `CHEBI:27445` with the exact IUPAC synonym and `CAS:34620-77-4` in
  `other`.

## Completeness

- The identity, chemistry, exact synonym, and final SSSOM predicate are
  consistent.
- `CARBON_SOURCE` is backed only by `COMPUTATIONAL_PREDICTION` evidence from
  ChEBI carbohydrate ancestry with a provisional curator note.

## Recommended Edits

- Remove `CARBON_SOURCE` unless source-backed evidence for maltohexaose as a
  media carbon source can be attached.
