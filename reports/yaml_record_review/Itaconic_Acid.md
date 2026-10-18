# `data/ingredients/mapped/Itaconic_Acid.yaml`

## Verdict

Pass. The CultureBotHT exact ChEBI identity, CAS RN, structure fields, exact
synonym, and final SSSOM row all describe neutral itaconic acid.

## Identity

- Reviewed record: `data/ingredients/mapped/Itaconic_Acid.yaml`.
- Identifier and grounding: `identifier: CHEBI:30838` with
  `ontology_mapping.ontology_id: CHEBI:30838`, label `itaconic acid`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS RN `97-65-4`, formula `C5H6O4`, InChI
  `InChI=1S/C5H6O4/c1-3(5(8)9)2-4(6)7/h1-2H2,(H,6,7)(H,8,9)`, and SMILES
  `C=C(CC(=O)O)C(=O)O`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Isovitalex.yaml data/ingredients/mapped/Isovitexin.yaml data/ingredients/mapped/Itaconate.yaml data/ingredients/mapped/Itaconic_Acid.yaml data/ingredients/mapped/Izalpinin.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- Engine A LinkML term validation passed for the 3 CHEBI records.
  `Isovitalex` and `Izalpinin` were outside adapter scope because their primary
  identifiers are local `kgmicrobe.ingredient` and CAS registry CURIEs.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip_20260916_2120`
  aggregated 2951 records.
- `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip_20260916_2120`
  passed with 2 files compared, 0 data differences, and only expected
  `generation_date` metadata differences.

## Evidence

- OLS4 resolves `CHEBI:30838` as the active ChEBI class `itaconic acid`, with
  CAS xref `97-65-4`, formula `C5H6O4`, the same InChI and SMILES stored on
  the record, and the recorded IUPAC synonym as an exact ChEBI synonym.
- PubChem resolves CAS RN `97-65-4` to formula `C5H6O4` and the same InChI
  stored on the record.
- The final SSSOM publishes one `skos:exactMatch` row from
  `MIM:Itaconic_Acid` to `CHEBI:30838` and exports only the inspected exact
  synonym plus `CAS:97-65-4`.
- The hidden and ignored-inclusive search over `data`, `src`, `tests`,
  `mappings`, `scripts`, `conf`, `docs`, and `.claude` found the current
  aggregate row, final SSSOM row, docs projections, and existing
  OAK/OLS-confirmed review row.

## Completeness

- The active ChEBI identifier, CAS RN, formula, InChI, SMILES, exact synonym,
  aggregate copy, and final SSSOM row are present and consistent.
- No unsupported roles or non-synonym final `other` tokens are asserted.

## Recommended Edits

- None.
