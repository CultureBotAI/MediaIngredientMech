# `data/ingredients/mapped/N-lauroylsarcosine_Sodium_Salt.yaml`

## Verdict

Pass. The #455 repair correctly preserves sodium lauroylsarcosinate as local CAS
identity `cas:137-16-6`, maps it narrowly to the verified free-acid parent
`CHEBI:183705`, rejects inherited non-subject ChEBI labels, and publishes the
expected registry rows.

## Identity

- Reviewed record:
  `data/ingredients/mapped/N-lauroylsarcosine_Sodium_Salt.yaml`.
- Identifier and grounding: `identifier: cas:137-16-6` with
  `ontology_mapping.ontology_id: CHEBI:183705`, label
  `N-Lauroylsarcosine`, source `CHEBI`, `mapping_quality: NARROW_MATCH`,
  `mapping_status: MAPPED`, and `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: no direct CultureMech recipe occurrences.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `N-lauroylsarcosine_Sodium_Salt` through
  `NNNN-Tetramethylethylenediamine`: exited 0 and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-parent
  record.

## Evidence

- Fresh EBI OLS4 lookups resolve active `CHEBI:183705` as free
  N-Lauroylsarcosine with formula `C15H29NO3`, while the previous
  `CHEBI:183704` target still carries the salt CAS on a non-sodium structure
  that does not match the supplied form.
- A fresh PubChem lookup for CID `23668817` returns the sodium salt formula
  `C15H28NNaO3` and the stored component SMILES/InChI for `CAS:137-16-6`.
- The inherited labels from `CHEBI:183704` are present only as
  `REJECTED_LABEL` YAML provenance and are absent from final SSSOM `other`.
- The final SSSOM publishes the required trio of rows: a
  `skos:narrowMatch` to `CHEBI:183705`, an exact `cas:137-16-6` registry row,
  and an exact `kgmicrobe.compound:n-lauroylsarcosine_sodium_salt` sibling row.

## Completeness

- The local CAS identity, parent ChEBI mapping, sodium-salt structure, rejected
  old target labels, and registry rows agree.
- The record does not assert components, roles, or unsafe final synonym text.

## Recommended Edits

- None.
