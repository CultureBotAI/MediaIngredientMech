# `data/ingredients/mapped/Hexanol.yaml`

## Verdict

Needs curation. The record has CAS RN `111-27-3`, which resolves to the specific
primary alcohol 1-hexanol, but the YAML and final SSSOM exact-match the broader
positional-isomer class `CHEBI:143552` `hexanol`.

## Identity

- Reviewed record: `data/ingredients/mapped/Hexanol.yaml`.
- Identifier and grounding: `identifier: CHEBI:143552` with
  `ontology_mapping.ontology_id: CHEBI:143552`, label `hexanol`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`,
  `mapping_status: MAPPED`, and `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS RN `111-27-3`, with no stored formula, InChI, SMILES,
  or PubChem CID.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Hexanoate.yaml data/ingredients/mapped/Hexanol.yaml data/ingredients/mapped/Hippuric_Acid.yaml data/ingredients/mapped/Histamine.yaml data/ingredients/mapped/Hitachimycin.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `linkml-term-validator` passed for `CHEBI:143552`.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip_20260916_1428`
  aggregated 2951 records.
- `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip_20260916_1428`
  passed with 2 files compared, 0 data differences, and only expected
  `generation_date` metadata differences.

## Evidence

- OLS4 resolves `CHEBI:143552` as active `hexanol`, defined as a six-carbon
  straight-chain fatty alcohol whose hydroxy group can be at any position.
- OLS4 also has active `CHEBI:87393` `hexan-1-ol` with `1-hexanol`, `hexanol`,
  and `n-hexanol` as synonyms.
- PubChem resolves CAS RN `111-27-3` to `1-Hexanol`, formula `C6H14O`, SMILES
  `CCCCCCO`, and InChI `InChI=1S/C6H14O/c1-2-3-4-5-6-7/h7H,2-6H2,1H3`,
  matching the straight-chain primary alcohol rather than a positional-isomer
  class.
- Major: because `chemical_properties.cas_rn` fixes the subject as 1-hexanol,
  the exact mapping to the broader `CHEBI:143552` hexanol class overstates the
  current identity.
- The final SSSOM publishes one `skos:exactMatch` row from `MIM:Hexanol` to
  `CHEBI:143552` and exports only `CAS:111-27-3` in `other`.

## Completeness

- The CAS RN is present, valid, and points to the more specific primary-alcohol
  identity.
- The record is incomplete until the exact ChEBI target is changed to
  `CHEBI:87393` and the formula, InChI, and SMILES are backfilled for the same
  CAS-resolved structure.

## Recommended Edits

- Major: remap the record from `CHEBI:143552` `hexanol` to `CHEBI:87393`
  `hexan-1-ol`, keep CAS `111-27-3`, backfill the 1-hexanol formula/InChI/
  SMILES, regenerate the final SSSOM row, and rerun strict, term, round-trip,
  id-label, and SSSOM validation.
