# `data/ingredients/mapped/N-N_Dimethyl_Glycine.yaml`

## Verdict

Needs curation. The CAS-backed `CHEBI:17724` N,N-dimethylglycine identity,
structure, CAS provenance, and final exact row pass, but the amino-acid-source
role is only a provisional ChEBI-ancestry prediction.

Severity: major.

## Identity

- Reviewed record: `data/ingredients/mapped/N-N_Dimethyl_Glycine.yaml`.
- Identifier and grounding: `identifier: CHEBI:17724` with
  `ontology_mapping.ontology_id: CHEBI:17724`, label `N,N-dimethylglycine`,
  source `CHEBI`, `mapping_quality: CAS_RN_LOOKUP`,
  `mapping_status: MAPPED`, and `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: no direct CultureMech recipe occurrences.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `N-Acetyl-L-Glutamic_Acid` through
  `N-_2-acetamido-2-aminoethanesulfonic_Acid`: exited 0 and wrote zero ERROR
  rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.

## Evidence

- A fresh EBI OLS4 lookup resolves `CHEBI:17724` as active
  `N,N-dimethylglycine` with capitalization variants as exact synonyms.
- The final SSSOM publishes one `skos:exactMatch` row from
  `MIM:N-N_Dimethyl_Glycine` to `CHEBI:17724` with `CAS:1118-68-9` in `other`.

## Completeness

- The active ChEBI target, CAS RN, structure, and final row agree.
- `AMINO_ACID_SOURCE` has only `COMPUTATIONAL_PREDICTION` evidence from
  ChEBI-ancestry closure with a provisional curator note.

## Recommended Edits

- Major: add source-backed evidence that N,N-dimethylglycine is used as an amino
  acid source in media, or remove the provisional `AMINO_ACID_SOURCE` role.
