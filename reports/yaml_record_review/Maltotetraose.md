# `data/ingredients/mapped/Maltotetraose.yaml`

## Verdict

Needs curation. The exact ChEBI identity, CAS number, ChEBI structure, exact
IUPAC synonym, and final SSSOM row pass, but `CARBON_SOURCE` is still
supported only by provisional ChEBI-ancestry evidence.

Severity: major.

## Identity

- Reviewed record: `data/ingredients/mapped/Maltotetraose.yaml`.
- Identifier and grounding: `identifier: CHEBI:28460` with
  `ontology_mapping.ontology_id: CHEBI:28460`, label `maltotetraose`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: zero CultureMech recipe occurrences.
- Chemical identity: `cas_rn: 34612-38-9`, formula `C24H42O21`, InChI and
  SMILES copied from ChEBI.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Maltose_2` through `Maltotriose_Hydrate`: exited 0 and wrote zero ERROR
  rows.
- `uv run --frozen linkml-term-validator validate-data` exited 0 for this
  CHEBI-primary record.

## Evidence

- EBI OLS4 resolves `CHEBI:28460` as active `maltotetraose` with CAS
  `34612-38-9`, formula `C24H42O21`, and the same InChI and SMILES carried in
  the YAML.
- ChEBI carries the exported long-form IUPAC string as an exact synonym.
- The final SSSOM publishes one `skos:exactMatch` row from
  `MIM:Maltotetraose` to `CHEBI:28460` with the exact IUPAC synonym and
  `CAS:34612-38-9` in `other`.

## Completeness

- The identity, chemistry, exact synonym, and final SSSOM predicate are
  consistent.
- `CARBON_SOURCE` is backed only by `COMPUTATIONAL_PREDICTION` evidence from
  ChEBI carbohydrate ancestry with a provisional curator note.

## Recommended Edits

- Remove `CARBON_SOURCE` unless source-backed evidence for maltotetraose as a
  media carbon source can be attached.
