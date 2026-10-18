# `data/ingredients/mapped/Isomaltose.yaml`

## Verdict

Needs curation. The CultureBotHT exact ChEBI identity, CAS RN, structure
fields, exact synonym, and final SSSOM row pass, but `CARBON_SOURCE` is still
only a provisional ChEBI-ancestry assertion.

## Identity

- Reviewed record: `data/ingredients/mapped/Isomaltose.yaml`.
- Identifier and grounding: `identifier: CHEBI:28189` with
  `ontology_mapping.ontology_id: CHEBI:28189`, label `isomaltose`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS RN `499-40-1`, formula `C12H22O11`, InChI
  `InChI=1S/C12H22O11/c13-1-3-5(14)8(17)10(19)12(23-3)21-2-4-6(15)7(16)9(18)11(20)22-4/h3-20H,1-2H2/t3-,4-,5-,6-,7+,8+,9-,10-,11?,12+/m1/s1`,
  and SMILES
  `OC[C@H]1O[C@H](OC[C@H]2OC(O)[C@H](O)[C@@H](O)[C@@H]2O)[C@H](O)[C@@H](O)[C@@H]1O`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Isomaltose.yaml data/ingredients/mapped/Isoniazid.yaml data/ingredients/mapped/Isoorientin.yaml data/ingredients/mapped/Isophthalate.yaml data/ingredients/mapped/Isopropionate.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- Engine A LinkML term validation passed for the 4 CHEBI records.
  `Isopropionate` was outside adapter scope because its primary identifier is a
  local `kgmicrobe.compound` CURIE.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip_20260916_2100`
  aggregated 2951 records.
- `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip_20260916_2100`
  passed with 2 files compared, 0 data differences, and only expected
  `generation_date` metadata differences.

## Evidence

- OLS4 resolves `CHEBI:28189` as the active ChEBI class `isomaltose`, with
  formula `C12H22O11`, the same InChI and SMILES stored on the record, and the
  recorded glucopyranose name as an exact ChEBI synonym.
- PubChem resolves CAS RN `499-40-1` to formula `C12H22O11` and the same InChI
  stored on the record.
- The final SSSOM publishes one `skos:exactMatch` row from `MIM:Isomaltose` to
  `CHEBI:28189` and exports only the inspected exact synonym plus
  `CAS:499-40-1`.
- Major: `nutritional_roles.CARBON_SOURCE` has only
  `COMPUTATIONAL_PREDICTION` evidence from ChEBI ancestry, with no inspected
  CultureMech, FEBA, Hans80, or literature evidence attached to the claim.
- The hidden and ignored-inclusive search over `data`, `src`, `tests`,
  `mappings`, `scripts`, `conf`, `docs`, and `.claude` found the current
  aggregate row, final SSSOM row, docs projections, and existing
  OAK/OLS-confirmed review row.

## Completeness

- The active ChEBI identifier, CAS RN, formula, InChI, SMILES, exact synonym,
  aggregate copy, and final SSSOM row are present and consistent.
- The record is incomplete until the carbon-source role is either supported by
  inspected claim-level evidence or removed.

## Recommended Edits

- Major: remove `nutritional_roles.CARBON_SOURCE` unless an inspected
  CultureMech, FEBA, Hans80, or literature source can support isomaltose as a
  carbon source, then rerun strict, term, round-trip, id-label, component, and
  SSSOM validation.
