# `data/ingredients/mapped/Isobutyl_Alcohol.yaml`

## Verdict

Pass. The CultureBotHT CAS-derived identity correctly maps isobutyl alcohol CAS
RN `78-83-1` to isobutanol, and the ChEBI structure fields, synonyms, CAS
alias, and final SSSOM row are consistent.

## Identity

- Reviewed record: `data/ingredients/mapped/Isobutyl_Alcohol.yaml`.
- Identifier and grounding: `identifier: CHEBI:46645` with
  `ontology_mapping.ontology_id: CHEBI:46645`, label `isobutanol`, source
  `CHEBI`, `mapping_quality: CAS_RN_LOOKUP`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS RN `78-83-1`, formula `C4H10O`, InChI
  `InChI=1S/C4H10O/c1-4(2)3-5/h4-5H,3H2,1-2H3`, and SMILES `CC(C)CO`.

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

- OLS4 resolves `CHEBI:46645` as the active ChEBI class `isobutanol`, with CAS
  xref `78-83-1`, formula `C4H10O`, the same InChI and SMILES stored on the
  record, and `2-methylpropan-1-ol` and isobutyl-alcohol labels among its exact
  synonyms.
- PubChem resolves CAS RN `78-83-1` to formula `C4H10O` and the same InChI
  stored on the record.
- The final SSSOM publishes one `skos:exactMatch` row from
  `MIM:Isobutyl_Alcohol` to `CHEBI:46645` and exports only the inspected exact
  ChEBI synonym, the reviewed `Iso-butanol` synonym, and `CAS:78-83-1`.
- The hidden and ignored-inclusive search over `data`, `src`, `tests`,
  `mappings`, `scripts`, `conf`, `docs`, and `.claude` found the current
  aggregate row, final SSSOM row, docs projections, reviewed kg-microbe
  duplicate merge, and existing OAK/OLS-confirmed review row.

## Completeness

- The active ChEBI identifier, CAS RN, formula, InChI, SMILES, exact synonyms,
  aggregate copy, and final SSSOM row are present and consistent.
- No unsupported roles or non-synonym final `other` tokens are asserted.

## Recommended Edits

- None.
