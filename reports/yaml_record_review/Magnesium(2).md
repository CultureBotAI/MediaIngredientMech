# `data/ingredients/mapped/Magnesium(2).yaml`

## Verdict

Pass. The MicrobeDecoder exact CHEBI:18420 Mg2+ identity, transferred
CultureMech occurrence count, structure block, aggregate copy, and final SSSOM
row are internally consistent after the magnesium-atom merge.

## Identity

- Reviewed record: `data/ingredients/mapped/Magnesium(2).yaml`.
- Identifier and grounding: `identifier: CHEBI:18420` with
  `ontology_mapping.ontology_id: CHEBI:18420`, label `magnesium(2+)`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: molecular formula `Mg`, InChI, SMILES, and molecular
  weight.
- Occurrences: 3 total occurrences in 3 CultureMech recipes, plus 12
  MicrobeDecoder source occurrences.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Macro_Component_2_For_J_Medium` through `Magnesium`: exited 0 and wrote zero
  ERROR rows.
- `uv run --frozen linkml-term-validator validate-data` exited 0 for the
  CHEBI-primary subset `Macrolide_Antibiotic`, `Magainin_I`, `Magnesium(2)`,
  and `Magnesium`; `Macro_Component_2_For_J_Medium` was skipped because its
  primary identifier uses a local prefix outside the CHEBI/OBO term adapter
  scope.

## Evidence

- EBI OLS4 resolves `CHEBI:18420` as active `magnesium(2+)` and records the same
  formula, InChI, and SMILES as the YAML record.
- The 2026-09-11 `fix_element_atom_overclaims` merge moved three CultureMech
  rows from the neutral ChEBI atom term to `CHEBI:18420` because the source rows
  carried KEGG `mg2`.
- The final SSSOM publishes one `skos:exactMatch` row to `CHEBI:18420` under
  `MIM:Magnesium~282~29`, retains `Magnesium` in `other`, and no longer
  publishes a `CHEBI:25107` magnesium-atom row.

## Completeness

- The active CHEBI ion identity, occurrence statistics, MicrobeDecoder source
  occurrence count, formula, structure block, aggregate copy, and final SSSOM
  row are present and consistent.
- No nutritional, physicochemical, cellular, or environmental role is asserted.

## Recommended Edits

- None.
