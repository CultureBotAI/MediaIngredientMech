# `data/ingredients/mapped/Medicamycin.yaml`

## Verdict

Pass. The local fallback registry identity, MicrobeDecoder occurrence, and final
SSSOM row pass, and fresh exact OLS/PubChem checks did not find a better public
term.

## Identity

- Reviewed record: `data/ingredients/mapped/Medicamycin.yaml`.
- Identifier and grounding: `identifier: kgmicrobe.compound:medicamycin` with
  `ontology_mapping.ontology_id: kgmicrobe.compound:medicamycin`, label
  `Medicamycin`, source `kgmicrobe.compound`, `mapping_quality:
  FALLBACK_REGISTRY`, and `mapping_status: MAPPED`.
- Occurrences: one MicrobeDecoder `BacDive_Antibiotic_sensitivity` occurrence
  and zero CultureMech recipe occurrences.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Meat_peptone` through `Melezitose`: exited 0 and wrote zero ERROR rows.
- `uv run --frozen linkml-term-validator validate-data` exited 0 for the
  batch.
- Direct Engine A term validation was skipped for this local
  `kgmicrobe.compound` record because it is intentionally outside the OBO
  adapter scope.

## Evidence

- `mappings/record_research_validation.tsv` agrees with keeping this substance
  as a fallback registry row: the research recommendation was effectively
  unmapped, and the local `kgmicrobe.compound` primary identifier encodes that
  no ontology term denotes it.
- A fresh exact all-ontology OLS4 search for `Medicamycin` returned zero
  results.
- A fresh PubChem name search for `Medicamycin` returned no CID.
- The final SSSOM publishes one registry-preserving `skos:exactMatch` row from
  `MIM:Medicamycin` to `kgmicrobe.compound:medicamycin` with empty `other`.

## Completeness

- The record does not assert unsupported roles or external chemistry.

## Recommended Edits

- None.
