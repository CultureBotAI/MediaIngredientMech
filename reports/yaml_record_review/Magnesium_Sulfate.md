# `data/ingredients/mapped/Magnesium_Sulfate.yaml`

## Verdict

Needs curation. The exact anhydrous ChEBI identity, CAS number, structure,
hydrate-synonym filtering, and final SSSOM row pass, but the nutritional role
evidence is attached to the wrong role and leaves `MINERAL_SOURCE` unsupported.

Severity: major.

## Identity

- Reviewed record: `data/ingredients/mapped/Magnesium_Sulfate.yaml`.
- Identifier and grounding: `identifier: CHEBI:32599` with
  `ontology_mapping.ontology_id: CHEBI:32599`, label `magnesium sulfate`,
  source `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`,
  and `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 679 total occurrences in 677 CultureMech recipes.
- Chemical identity: `cas_rn: 7487-88-9`, formula `Mg.O4S`, InChI and SMILES
  copied from ChEBI.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Magnesium_Acetate` through `Malachite_Green`: exited 0 and wrote zero
  ERROR rows.
- `uv run --frozen linkml-term-validator validate-data` exited 0 for this
  CHEBI-primary record.

## Evidence

- EBI OLS4 resolves `CHEBI:32599` as active `magnesium sulfate` with CAS
  `7487-88-9`, formula `Mg.O4S`, and the same InChI and SMILES carried in the
  YAML.
- The final SSSOM publishes one exact row from `MIM:Magnesium_Sulfate` to
  `CHEBI:32599`.
- The final `other` field contains exact anhydrous magnesium sulfate synonyms
  and `CAS:7487-88-9`; the reviewed hydrate labels are now rejected and are
  filtered from final SSSOM output.

## Completeness

- The identity, anhydrous structure, CAS, final SSSOM predicate, and hydrate
  label filtering are consistent.
- `SULFUR_SOURCE` carries the CultureMech `DATABASE_ENTRY` evidence for 525
  occurrences as `Mineral source`; that source text supports the mineral role,
  not the sulfur role.
- `MINERAL_SOURCE` is present but has `confidence: 0.8` and an empty evidence
  list, so the supported role is the unsupported one in the current YAML.

## Recommended Edits

- Move the CultureMech mineral-source evidence to `MINERAL_SOURCE`, and either
  add independent source-backed evidence for `SULFUR_SOURCE` or remove that
  role.
