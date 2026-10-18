# `data/ingredients/mapped/Magnesium_Acetate.yaml`

## Verdict

Needs curation. The exact ChEBI identity, CAS number, structure, exact
synonyms, occurrence counts, and final SSSOM row pass, but the
`CARBON_SOURCE` role is supported only by CultureMech evidence for the
original role `Mineral`.

Severity: major.

## Identity

- Reviewed record: `data/ingredients/mapped/Magnesium_Acetate.yaml`.
- Identifier and grounding: `identifier: CHEBI:62964` with
  `ontology_mapping.ontology_id: CHEBI:62964`, label `magnesium acetate`,
  source `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`,
  and `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: four total occurrences in four CultureMech recipes.
- Chemical identity: `cas_rn: 142-72-3`, formula `2C2H3O2.Mg`, InChI and
  SMILES copied from ChEBI.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Magnesium_Acetate` through `Malachite_Green`: exited 0 and wrote zero
  ERROR rows.
- `uv run --frozen linkml-term-validator validate-data` exited 0 for this
  CHEBI-primary record.

## Evidence

- EBI OLS4 resolves `CHEBI:62964` as active `magnesium acetate` with CAS
  `142-72-3`, formula `2C2H3O2.Mg`, and the same InChI and SMILES carried in
  the YAML.
- The final SSSOM publishes one `skos:exactMatch` row from
  `MIM:Magnesium_Acetate` to `CHEBI:62964`.
- Its final `other` field contains exact magnesium acetate synonyms plus
  `CAS:142-72-3`; the raw CultureMech role/properties text is filtered out.

## Completeness

- The identity, structure, CAS, final SSSOM predicate, and exported synonyms
  are aligned to the active anhydrous ChEBI term.
- `MINERAL_SOURCE` is supported by the imported CultureMech database evidence.
- `CARBON_SOURCE` reuses that same evidence block even though its
  `curator_note` is `Original role text: Mineral`. The row does not contain
  source text or external evidence saying magnesium acetate was used as a
  carbon source.

## Recommended Edits

- Remove `CARBON_SOURCE`, or replace its evidence with source-backed carbon
  source evidence that is independent of the imported `Mineral` role.
