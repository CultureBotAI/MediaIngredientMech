# `data/ingredients/mapped/K-acetate.yaml`

## Verdict

Needs curation. The record is correctly grounded to potassium acetate, and its
CAS RN, structure, kg-microbe synonyms, occurrence count, and ChEBI
id-label pair pass, but the final SSSOM still publishes generic acetate and
acetyl ester class labels as K-acetate synonyms, and the `CARBON_SOURCE` role is
not supported by the original `Mineral` CultureMech role.

## Identity

- Reviewed record: `data/ingredients/mapped/K-acetate.yaml`.
- Identifier and grounding: `identifier: CHEBI:32029` with
  `ontology_mapping.ontology_id: CHEBI:32029`, label `potassium acetate`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS RN `127-08-2`, formula `C2H3O2.K`, InChI
  `InChI=1S/C2H4O2.K/c1-2(3)4;/h1H3,(H,3,4);/q;+1/p-1`, and SMILES
  `CC(=O)[O-].[K+]`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Jasmonic_Acid.yaml data/ingredients/mapped/Juglone.yaml data/ingredients/mapped/K-acetate.yaml data/ingredients/mapped/K-phosphate_Buffer.yaml data/ingredients/mapped/K2co3.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- Engine A LinkML term validation passed for this CHEBI record.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip_20260916_2130`
  aggregated 2951 records.
- `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip_20260916_2130`
  passed with 2 files compared, 0 data differences, and only expected
  `generation_date` metadata differences.

## Evidence

- OLS4 resolves `CHEBI:32029` as the active ChEBI class `potassium acetate`,
  with CAS xref `127-08-2`, formula `C2H3O2.K`, the same InChI and SMILES
  stored on the record, and the curated `AcOK`, `CH3CO2K`, `E261`, `KOAc`,
  `Kaliumazetat`, `MeCO2K`, and `Potassium acetate` labels as synonyms.
- PubChem resolves CAS RN `127-08-2` to the same potassium acetate InChI stored
  on the record.
- The final SSSOM publishes one `skos:exactMatch` row from `MIM:K-acetate` to
  `CHEBI:32029`; the row correctly carries the specific kg-microbe synonyms
  and `CAS:127-08-2`, and correctly omits the raw CultureMech `Role:` and
  `Properties:` strings.
- Major: the YAML and the final SSSOM `other` include `Acetic ester`,
  `Acetyl ester`, `acetate ester`, `acetate esters`, `acetates`,
  `acetyl esters`, and `an acetyl ester` from `sssom_other_backfill`. These are
  broader acetate or acetyl ester class labels, not synonyms of the potassium
  salt.
- Major: `nutritional_roles.CARBON_SOURCE` is backed by a `DATABASE_ENTRY`
  whose curator note says `Original role text: Mineral`; that evidence
  supports the imported mineral annotation, but it does not support recasting
  the ingredient as a carbon source.
- The hidden and ignored-inclusive search over `data`, `src`, `tests`,
  `mappings`, `scripts`, `conf`, `docs`, and `.claude` found the bad backfilled
  class labels in the source YAML, the final SSSOM row, docs label surfaces,
  and no narrower evidence supporting `CARBON_SOURCE`.

## Completeness

- The active ChEBI identifier, CAS RN, formula, InChI, SMILES, specific
  potassium acetate synonyms, aggregate copy, and occurrence count are present
  and consistent.
- The record is incomplete until the broader ester labels stop exporting as
  K-acetate synonyms and the migrated carbon-source role is either supported by
  claim-level evidence or removed/recurated from the original `Mineral` source.

## Recommended Edits

- Major: remove the seven `sssom_other_backfill` class-label synonyms from
  `data/ingredients/mapped/K-acetate.yaml`, synchronize the curated aggregate,
  and rebuild the final SSSOM/docs surfaces so only true potassium acetate
  synonyms remain in `other`.
- Major: fix `nutritional_roles.CARBON_SOURCE` in
  `data/ingredients/mapped/K-acetate.yaml`; either remove it or attach inspected
  evidence that specifically supports potassium acetate as a carbon source,
  then rerun strict, term, round-trip, id-label, component, and SSSOM
  validation.
