# `data/ingredients/mapped/Glycylglycine.yaml`

## Verdict

Pass with minor issues. This rejected duplicate tombstone still points at the
same `CHEBI:17201` glycylglycine identity as the active `Glycyl-glycine`
record, and it no longer has a final SSSOM row, but stale active-mapping fields,
a provisional buffer role, and a CAS-decorated raw synonym remain on the
tombstone.

## Identity

- Reviewed record: `data/ingredients/mapped/Glycylglycine.yaml`.
- Current status: `mapping_status: REJECTED` after merge into active
  `data/ingredients/mapped/Glycyl-glycine.yaml`.
- Stale grounding retained on the tombstone: `identifier: CHEBI:17201` with
  matching `ontology_mapping.ontology_id`, canonical label `glycylglycine`,
  `mapping_quality: EXACT_MATCH`, and `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS-RN `556-50-3`, formula `C4H8N2O3`, SMILES
  `NCC(=O)NCC(=O)O`, and the ChEBI glycylglycine InChI.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Glycylglycine.yaml data/ingredients/mapped/Glycylglycylglycine.yaml data/ingredients/mapped/Glycyrrhizic_Acid_Ammonium_Salt.yaml data/ingredients/mapped/Glyoxylate.yaml data/ingredients/mapped/Gold_Iii_Chloride_Hydrate.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Glycylglycine.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.

## Evidence

- The matching aggregate `data/curated/mapped_ingredients.yaml` entry is
  identical to the split per-record YAML.
- OLS4 resolves `CHEBI:17201` as `glycylglycine` with CAS `556-50-3`, formula
  `C4H8N2O3`, the same InChI, and the same SMILES as this record.
- The 2026-08-05 history entry records that this former active record was
  merged into active `CHEBI:17201` `Glycyl-glycine`, occurrences were
  transferred, and final SSSOM rows were dropped.
- The final `mappings/ingredient_mappings.sssom.tsv` has no
  `MIM:Glycylglycine` row, so the duplicate tombstone is no longer a published
  subject.
- Minor: the tombstone still carries active-only shape: an exact
  `ontology_mapping`, `ingredient_type: SINGLE_INGREDIENT`, ChEBI/PubChem
  `chemical_properties`, the CAS-decorated raw synonym
  `Glycylglycine(CAS: 556-50-3)`, and a provisional `BUFFER` role. These stale
  fields do not currently reach final SSSOM because the record is rejected.
- A hidden/ignored-inclusive search over `data`, `src`, `tests`, `mappings`,
  `scripts`, `conf`, `docs`, and `.claude` found the rejected tombstone, the
  active merged `Glycyl-glycine` record, matching aggregate copies, generated
  products, final SSSOM rows only for the active survivor, row-review TSVs, and
  ignored aggregate backups.

## Completeness

- The rejected tombstone preserves the old exact ChEBI identity and merge
  history enough for duplicate provenance.
- No `MIM:Glycylglycine` subject remains in final SSSOM; the only graph-facing
  issue in this duplicate cluster is the active survivor's CAS-decorated raw
  synonym.

## Recommended Edits

- Minor: trim the rejected tombstone in
  `data/ingredients/mapped/Glycylglycine.yaml` to the fields needed for merge
  provenance, or at least remove/retype the stale `BUFFER` role and
  `Glycylglycine(CAS: 556-50-3)` raw synonym when the active
  `Glycyl-glycine` synonym payload is fixed.
