# `data/ingredients/mapped/Maltose_Hydrate.yaml`

## Verdict

Pass. The local exact maltose-hydrate identity, close anhydrous ChEBI parent,
MicrobeDecoder source count, final registry row, and hydrate-grounding audit
all pass.

## Identity

- Reviewed record: `data/ingredients/mapped/Maltose_Hydrate.yaml`.
- Identifier and grounding:
  `identifier: kgmicrobe.compound:maltose_hydrate` with
  `ontology_mapping.ontology_id: CHEBI:17306`, label `maltose`, source
  `CHEBI`, `mapping_quality: CLOSE_MATCH`, and `mapping_status: MAPPED`.
- Local exact subject: `kgmicrobe.compound:maltose_hydrate`.
- Occurrences: zero CultureMech recipe occurrences and eight MicrobeDecoder
  `BacDive_Metabolite_utilization` source occurrences.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Maltose_2` through `Maltotriose_Hydrate`: exited 0 and wrote zero ERROR
  rows.
- LinkML term validation was skipped for this local-primary record because the
  subject identifier is outside the CHEBI/OBO term adapter scope.

## Evidence

- EBI OLS4 resolves the parent `CHEBI:17306` as active `maltose`.
- The 2026-08-13 regrade changed the parent relation from `NARROW_MATCH` to
  `CLOSE_MATCH` so the hydrate no longer asserts subsumption by anhydrous
  maltose.
- The final SSSOM publishes one close row to `CHEBI:17306` and one exact Rule
  B1 registry row to `kgmicrobe.compound:maltose_hydrate`.
- `reports/hydrate_grounding.tsv` reports
  `kgmicrobe.compound:maltose_hydrate` as `OK_LOCAL_REGISTRY_ID`.

## Completeness

- The hydrate label is preserved on the hydrate subject, not exported as an
  `other` value on this record.
- The record does not publish unsupported roles or non-exact synonyms.

## Recommended Edits

- None.
