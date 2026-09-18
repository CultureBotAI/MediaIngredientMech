# `data/ingredients/mapped/Guanine.yaml`

## Verdict

Pass with minor issues. The exact ChEBI identity, CAS RN, chemical structure,
occurrence count, exported synonyms, and final SSSOM row pass, but the
top-level notes still carry the older FEBA occurrence count.

## Identity

- Reviewed record: `data/ingredients/mapped/Guanine.yaml`.
- Identifier and grounding: `identifier: CHEBI:16235` with
  `ontology_mapping.ontology_id: CHEBI:16235`, label `guanine`, source
  `CHEBI`, `mapping_quality: CAS_RN_LOOKUP`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS RN `73-40-5`, formula `C5H5N5O`, InChI
  `InChI=1S/C5H5N5O/c6-5-9-3-2(4(11)10-5)7-1-8-3/h1H,(H4,6,7,8,9,10,11)`,
  and SMILES `Nc1nc(=O)c2ncnc2n1`.
- Occurrence statistics: `total_occurrences: 26` and `media_count: 26`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Guanidinium_Chloride.yaml data/ingredients/mapped/Guanine.yaml data/ingredients/mapped/Guanosine.yaml data/ingredients/mapped/Gum_Arabic_From_Acacia_Tree.yaml data/ingredients/mapped/H23-methyl_Mercaptopropionate.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `linkml-term-validator` passed for `CHEBI:16235`.
- The matching aggregate `data/curated/mapped_ingredients.yaml` entry is
  identical to the split per-record YAML.

## Evidence

- OLS4 resolves `CHEBI:16235` as active `guanine` with CAS `73-40-5`.
- The formula, InChI, and SMILES match the exact guanine identity.
- The four exported final-SSSOM synonym tokens are real guanine synonyms, and
  the final `CAS:73-40-5` token matches `chemical_properties.cas_rn`.
- The final SSSOM publishes one `skos:exactMatch` row from `MIM:Guanine` to
  `CHEBI:16235`.
- Minor: `notes` still says the record was used in 22 FEBA media formulations,
  while `occurrence_statistics` was refreshed to `26/26`.

## Completeness

- The active ChEBI identifier, CAS RN, formula, InChI, SMILES, exact synonyms,
  occurrence statistics, and final SSSOM row are present and consistent.
- Only the stale free-text occurrence count in `notes` remains to clean up.

## Recommended Edits

- Minor: update `notes` so it no longer reports the pre-refresh FEBA count of
  22 formulations.
