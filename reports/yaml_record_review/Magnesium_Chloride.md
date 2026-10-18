# `data/ingredients/mapped/Magnesium_Chloride.yaml`

## Verdict

Needs curation. The record now grounds to the exact magnesium dichloride
hexahydrate ChEBI term, but several non-exact surface forms still publish in
the final SSSOM `other` field for `MIM:Magnesium_Chloride`.

Severity: major.

## Identity

- Reviewed record: `data/ingredients/mapped/Magnesium_Chloride.yaml`.
- Identifier and grounding: `identifier: CHEBI:86345` with
  `ontology_mapping.ontology_id: CHEBI:86345`, label
  `magnesium dichloride hexahydrate`, source `CHEBI`,
  `mapping_quality: SYNONYM_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 4,026 total occurrences in 4,019 CultureMech recipes.
- Chemical identity: `cas_rn: 7791-18-6`, formula `2Cl.6H2O.Mg`, InChI and
  SMILES copied from ChEBI.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Magnesium_Acetate` through `Malachite_Green`: exited 0 and wrote zero
  ERROR rows.
- `uv run --frozen linkml-term-validator validate-data` exited 0 for this
  CHEBI-primary record.

## Evidence

- EBI OLS4 resolves `CHEBI:86345` as active `magnesium dichloride
  hexahydrate` with CAS `7791-18-6`, formula `2Cl.6H2O.Mg`, and the same
  InChI and SMILES carried in the YAML.
- The final SSSOM publishes one exact row from `MIM:Magnesium_Chloride` to
  `CHEBI:86345`; the exact predicate is appropriate because the record points
  at the hexahydrate term even though the local preferred term is shorter.
- The `MINERAL_SOURCE` role is backed by a CultureMech `DATABASE_ENTRY` whose
  excerpt and curator note both document the original `Mineral source` role.

## Completeness

- Exact hexahydrate labels such as `MgCl2x6H2O` are safe to export.
- The final `other` field also contains `magnesium dichloride--water (1/2)`,
  which names the dihydrate rather than the hexahydrate.
- `MgCl 2` erases the six waters from the curated hexahydrate identity, and
  `MgCl2 x 6 H2O (200 g/l stock solution)` is a concentration-qualified stock
  solution label rather than a synonym of the compound.

## Recommended Edits

- Mark the dihydrate, anhydrous, and concentration-qualified stock text as
  `REJECTED_LABEL` or otherwise exclude them from the final SSSOM `other`
  field for the hexahydrate record.
