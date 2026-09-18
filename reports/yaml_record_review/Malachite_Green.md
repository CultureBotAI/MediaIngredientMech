# `data/ingredients/mapped/Malachite_Green.yaml`

## Verdict

Pass. The exact ChEBI identity, CAS number, structure, kg-microbe exact
synonyms, CultureMech-backed roles, occurrence counts, and final SSSOM row all
pass.

## Identity

- Reviewed record: `data/ingredients/mapped/Malachite_Green.yaml`.
- Identifier and grounding: `identifier: CHEBI:72449` with
  `ontology_mapping.ontology_id: CHEBI:72449`, label `malachite green`,
  source `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`,
  and `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 25 total occurrences in 25 CultureMech recipes.
- Chemical identity: `cas_rn: 569-64-2`, formula `C23H25N2.Cl`, InChI and
  SMILES copied from ChEBI.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Magnesium_Acetate` through `Malachite_Green`: exited 0 and wrote zero ERROR
  rows.
- `uv run --frozen linkml-term-validator validate-data` exited 0 for this
  CHEBI-primary record.

## Evidence

- EBI OLS4 resolves `CHEBI:72449` as active `malachite green` with CAS
  `569-64-2`, formula `C23H25N2.Cl`, and the same InChI and SMILES carried in
  the YAML.
- The final SSSOM publishes one `skos:exactMatch` row from
  `MIM:Malachite_Green` to `CHEBI:72449`.
- The final `other` field contains the 12 exact kg-microbe synonyms plus
  `CAS:569-64-2`; raw CultureMech role/properties text is filtered out.
- `SELECTIVE_AGENT` and `PH_INDICATOR` are both backed by imported
  CultureMech `DATABASE_ENTRY` evidence with matching original role text.

## Completeness

- The record has no stale rejected duplicate rows leaking into final SSSOM.
- The two published roles are the roles imported from the CultureMech source
  rows and are attached to record-specific evidence.

## Recommended Edits

- None.
