# `data/ingredients/mapped/Maltotriose.yaml`

## Verdict

Needs curation. The MicrobeDecoder exact ChEBI identity, ChEBI structure,
source occurrence count, and exact final SSSOM predicate pass, but final SSSOM
exports `Maltotriose hydrate` as an `other` synonym of anhydrous
`MIM:Maltotriose`.

Severity: major.

## Identity

- Reviewed record: `data/ingredients/mapped/Maltotriose.yaml`.
- Identifier and grounding: `identifier: CHEBI:61993` with
  `ontology_mapping.ontology_id: CHEBI:61993`, label `maltotriose`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: zero CultureMech recipe occurrences and two MicrobeDecoder
  `BacDive_Metabolite_utilization` source occurrences.
- Chemical identity: formula `C18H32O16`, InChI and SMILES copied from ChEBI.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Maltose_2` through `Maltotriose_Hydrate`: exited 0 and wrote zero ERROR
  rows.
- `uv run --frozen linkml-term-validator validate-data` exited 0 for this
  CHEBI-primary record.

## Evidence

- EBI OLS4 resolves `CHEBI:61993` as active `maltotriose` with CAS
  `1109-28-0`, formula `C18H32O16`, and the same InChI and SMILES carried in
  the YAML.
- The 2026-08-04 MicrobeDecoder review promoted the exact `maltotriose`
  grounding after the local OAK adapter resolved the id and canonical label.
- The final SSSOM publishes one `skos:exactMatch` row from `MIM:Maltotriose`
  to `CHEBI:61993`, but its `other` field contains `Maltotriose hydrate`.

## Completeness

- The active anhydrous identity and source occurrence count are correct.
- The hydrate label belongs on `MIM:Maltotriose_Hydrate`, where it is the
  CAS-primary record label, not in the `other` field for anhydrous maltotriose.

## Recommended Edits

- Reject or relocate `Maltotriose hydrate` so final SSSOM no longer emits it
  on the anhydrous maltotriose row.
