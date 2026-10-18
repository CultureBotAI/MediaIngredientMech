# `data/ingredients/mapped/Malonamide.yaml`

## Verdict

Pass. The MicrobeDecoder exact ChEBI identity, reviewed promotion, ChEBI
structure, source occurrence count, empty exported `other` field, and final
SSSOM row all pass.

## Identity

- Reviewed record: `data/ingredients/mapped/Malonamide.yaml`.
- Identifier and grounding: `identifier: CHEBI:48537` with
  `ontology_mapping.ontology_id: CHEBI:48537`, label `malonamide`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: zero CultureMech recipe occurrences and two MicrobeDecoder
  `BacDive_Metabolite_utilization` source occurrences.
- Chemical identity: formula `C3H6N2O2`, InChI and SMILES copied from ChEBI.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Malate` through `Malondialdehyde_Tetrabutylammonium_Salt`: exited 0 and
  wrote zero ERROR rows.
- `uv run --frozen linkml-term-validator validate-data` exited 0 for this
  CHEBI-primary record.

## Evidence

- EBI OLS4 resolves `CHEBI:48537` as active `malonamide` with formula
  `C3H6N2O2`, CAS `108-13-4`, and the same InChI and SMILES carried in the
  YAML.
- The 2026-08-04 MicrobeDecoder review promoted the auto-grounding after the
  local OAK adapter resolved the id and canonical label.
- The final SSSOM publishes one `skos:exactMatch` row from `MIM:Malonamide` to
  `CHEBI:48537` with an empty `other` field.

## Completeness

- The source count is preserved under `source_occurrences`.
- No unsupported roles or stale synonyms publish for this MicrobeDecoder-only
  record.

## Recommended Edits

- None.
