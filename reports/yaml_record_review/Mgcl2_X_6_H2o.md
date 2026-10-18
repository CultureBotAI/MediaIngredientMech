# `data/ingredients/mapped/Mgcl2_X_6_H2o.yaml`

## Verdict

Needs curation. The exact `CHEBI:86345` magnesium dichloride hexahydrate
identity, CAS, ChEBI/PubChem structure, hydrate grounding audit, occurrence
count, and CultureMech mineral-source role pass, but stale non-exact labels
still publish in the final SSSOM `other` field.

Severity: major.

## Identity

- Reviewed record: `data/ingredients/mapped/Mgcl2_X_6_H2o.yaml`.
- Identifier and grounding: `identifier: CHEBI:86345` with
  `ontology_mapping.ontology_id: CHEBI:86345`, label
  `magnesium dichloride hexahydrate`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 4,026 total occurrences across 4,019 CultureMech recipes.
- Chemical identity: CAS `7791-18-6`, formula `2Cl.6H2O.Mg`, SMILES, and
  InChI.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Mgcl2` through `Mgcl2_X_H2o`: exited 0 and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record and the three other CHEBI-primary records in the same batch.

## Evidence

- EBI OLS4 resolves `CHEBI:86345` as active
  `magnesium dichloride hexahydrate` with formula `2Cl.6H2O.Mg`, the CAS
  `7791-18-6`, and exact synonym `magnesium dichloride--water (1/6)`.
- PubChem resolves CAS `7791-18-6` to CID 24644 with formula `Cl2H12MgO6` and
  the same six-water InChI carried in the YAML.
- `reports/hydrate_grounding.tsv` marks this row `OK_HYDRATE_TERM`.
- The `MINERAL_SOURCE` role is backed by a CultureMech `DATABASE_ENTRY` whose
  excerpt and curator note both document the original `Mineral source` role.
- The final SSSOM publishes one `skos:exactMatch` row from
  `MIM:Mgcl2_X_6_H2o` to `CHEBI:86345`.

## Completeness

- Exact magnesium chloride hexahydrate labels are safe to export, including the
  recovered spacing/punctuation variants and `magnesium dichloride--water
  (1/6)`.
- The final `other` field still contains `Magnesium chloride anhydrous`, which
  names `CHEBI:6636` rather than the hexahydrate.
- The final `other` field still contains `MgCl2 x 6 H2O (200 g/l stock
  solution)`, a stock-solution label rather than a synonym of the pure
  hexahydrate.
- The final `other` field still contains `MgCl*6H2O`, a malformed magnesium
  chloride hexahydrate surface form restored from KGX that should not be an
  exact synonym.

## Recommended Edits

- Major: mark `Magnesium chloride anhydrous`, `MgCl2 x 6 H2O (200 g/l stock
  solution)`, and `MgCl*6H2O` as `REJECTED_LABEL` or otherwise exclude them
  from the final SSSOM `other` field for
  `data/ingredients/mapped/Mgcl2_X_6_H2o.yaml`.
