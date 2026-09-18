# `data/ingredients/mapped/Na2haso4_X_7_H2o.yaml`

## Verdict

Needs curation - major. The exact `CHEBI:91257` disodium hydrogenarsenate
heptahydrate identity, CAS-backed structure, hydrate grounding, occurrence
count, and final exact row pass, but one malformed one-sodium formula and one
anhydrous formula token are still active synonyms and still publish to final
SSSOM `other`.

## Identity

- Reviewed record: `data/ingredients/mapped/Na2haso4_X_7_H2o.yaml`.
- Identifier and grounding: `identifier: CHEBI:91257` with
  `ontology_mapping.ontology_id: CHEBI:91257`, label
  `disodium hydrogenarsenate heptahydrate`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 14 CultureMech recipe occurrences across 14 media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Na2edta2h2o` through `Na2hpo4_X_12_H2o`: exited 0 and wrote zero ERROR
  rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.

## Evidence

- A fresh EBI OLS4 lookup resolves `CHEBI:91257` as active
  `disodium hydrogenarsenate heptahydrate`. A fresh PubChem lookup for CAS RN
  `10048-95-0` resolves to the same heptahydrate formula and InChI stored in
  `chemical_properties`.
- `reports/hydrate_grounding.tsv` classifies `CHEBI:91257` as
  `OK_HYDRATE_TERM`; the record preserves the heptahydrate identity.
- Major: the active synonym list and final SSSOM `other` include `NaHAsO4.7H2O`,
  which drops one sodium from disodium hydrogenarsenate heptahydrate, and
  `Na2HAsO4`, which drops all seven waters of hydration. Neither is a clean
  synonym for the `CHEBI:91257` subject.

## Completeness

- The active ChEBI target, canonical CAS RN, formula, structure, 14/14
  occurrence count, and final exact row agree.
- The remaining consequential gap is cleanup of malformed or anhydrous arsenate
  labels from exact synonyms and final SSSOM `other`.

## Recommended Edits

- Major: in `data/ingredients/mapped/Na2haso4_X_7_H2o.yaml`, mark the
  one-sodium heptahydrate and anhydrous formula tokens as `REJECTED_LABEL` or
  otherwise keep them provenance-only, then rebuild final SSSOM and rerun the
  final SSSOM plus product label validators.
