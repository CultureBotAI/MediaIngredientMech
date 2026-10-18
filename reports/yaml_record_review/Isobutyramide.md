# `data/ingredients/mapped/Isobutyramide.yaml`

## Verdict

Pass. The mediadive exact ChEBI grounding, active ChEBI structure fields, exact
synonym, occurrence statistics, and final SSSOM row all describe
isobutyramide.

## Identity

- Reviewed record: `data/ingredients/mapped/Isobutyramide.yaml`.
- Identifier and grounding: `identifier: CHEBI:193555` with
  `ontology_mapping.ontology_id: CHEBI:193555`, label `isobutyramide`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: formula `C4H9NO` from ChEBI, InChI
  `InChI=1S/C4H9NO/c1-3(2)4(5)6/h3H,1-2H3,(H2,5,6)`, SMILES
  `CC(C)C(N)=O`, and molecular weight `87.12`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Iron_Powder.yaml data/ingredients/mapped/Iron_Stock.yaml data/ingredients/mapped/Isepamicin.yaml data/ingredients/mapped/Isobutyl_Alcohol.yaml data/ingredients/mapped/Isobutyramide.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- Engine A LinkML term validation passed for the 4 CHEBI records.
  `Iron_Stock` was outside adapter scope because its primary identifier is a
  local `kgmicrobe.ingredient` CURIE.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip_20260916_1645`
  aggregated 2951 records.
- `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip_20260916_1645`
  passed with 2 files compared, 0 data differences, and only expected
  `generation_date` metadata differences.

## Evidence

- OLS4 resolves `CHEBI:193555` as the active ChEBI class `isobutyramide`, with
  formula `C4H9NO`, the same InChI and SMILES stored on the record, and the
  recorded `2-methylpropanamide` synonym as an exact ChEBI synonym.
- PubChem resolves the ChEBI CAS xref `563-83-7` to formula `C4H9NO` and the
  same InChI stored on the record.
- The final SSSOM publishes one `skos:exactMatch` row from
  `MIM:Isobutyramide` to `CHEBI:193555` and exports only the inspected exact
  synonym in `other`.
- The hidden and ignored-inclusive search over `data`, `src`, `tests`,
  `mappings`, `scripts`, `conf`, `docs`, and `.claude` found the current
  aggregate row, final SSSOM row, docs projections, occurrence memberships for
  the 3 current recipes, and existing OAK/OLS-confirmed review row.

## Completeness

- The active ChEBI identifier, formula, InChI, SMILES, molecular weight,
  occurrence count, aggregate copy, and final SSSOM row are present and
  consistent.
- No unsupported roles or non-synonym final `other` tokens are asserted.

## Recommended Edits

- None.
