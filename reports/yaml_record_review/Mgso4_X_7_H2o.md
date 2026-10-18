# `data/ingredients/mapped/Mgso4_X_7_H2o.yaml`

## Verdict

Needs curation. The exact `CHEBI:31795` magnesium sulfate heptahydrate identity,
CAS, ChEBI/PubChem structure, hydrate grounding audit, occurrence count, and
duplicate merges pass, but malformed, anhydrous, monohydrate, and CAS/vendor
decorated labels still publish in final SSSOM `other`, and the role evidence is
attached to the wrong role.

Severity: major.

## Identity

- Reviewed record: `data/ingredients/mapped/Mgso4_X_7_H2o.yaml`.
- Identifier and grounding: `identifier: CHEBI:31795` with
  `ontology_mapping.ontology_id: CHEBI:31795`, label
  `magnesium sulfate heptahydrate`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 5,673 total occurrences across 5,619 CultureMech recipes.
- Chemical identity: CAS `10034-99-8`, formula `7H2O.Mg.O4S`, SMILES, and
  InChI.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Mgso4_X_7_H2o` through `Middlebrook_7H10_Agar`: exited 0 and wrote zero
  ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record and the two other CHEBI-primary records in the same batch.

## Evidence

- EBI OLS4 resolves `CHEBI:31795` as active
  `magnesium sulfate heptahydrate` with `magnesium sulfate--water (1/7)` as an
  exact synonym.
- PubChem resolves CAS `10034-99-8` to CID 24843 with formula `H14MgO11S` and
  the same seven-water InChI carried in the YAML.
- `reports/hydrate_grounding.tsv` marks this row `OK_HYDRATE_TERM`.
- The final SSSOM publishes one `skos:exactMatch` row from
  `MIM:Mgso4_X_7_H2o` to `CHEBI:31795`.

## Completeness

- The active heptahydrate target, CAS, structure, merged occurrence count, and
  tombstone merge history agree.
- The final SSSOM `other` field still exports non-exact heptahydrate text,
  including 1-water `MgSO4` labels, bare anhydrous magnesium sulfate labels,
  malformed formulas such as `.MgSO4`, `MgSO`, and `MgSO2`, and
  CAS/vendor-decorated 7-water labels.
- `SULFUR_SOURCE` carries the CultureMech `DATABASE_ENTRY` evidence for
  mineral-source uses. That source text supports the mineral role, not the
  sulfur role.
- `MINERAL_SOURCE` is present but has `confidence: 0.8` and an empty evidence
  list, so the supported role is the unsupported one in the current YAML.

## Recommended Edits

- Major: mark the 1-water, anhydrous, malformed, and CAS/vendor-decorated
  strings as `REJECTED_LABEL`, or otherwise filter them from final SSSOM
  `other` for `data/ingredients/mapped/Mgso4_X_7_H2o.yaml`.
- Major: move the CultureMech mineral-source evidence to `MINERAL_SOURCE`, and
  either add independent source-backed evidence for `SULFUR_SOURCE` or remove
  that role.
