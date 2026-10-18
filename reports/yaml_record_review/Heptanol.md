# `data/ingredients/mapped/Heptanol.yaml`

## Verdict

Needs curation. The record has CAS RN `111-70-6`, which resolves to the specific
primary alcohol 1-heptanol, but the YAML and final SSSOM exact-match the broader
positional-isomer class `CHEBI:195607` `heptanol`.

## Identity

- Reviewed record: `data/ingredients/mapped/Heptanol.yaml`.
- Identifier and grounding: `identifier: CHEBI:195607` with
  `ontology_mapping.ontology_id: CHEBI:195607`, label `heptanol`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`,
  `mapping_status: MAPPED`, and `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS RN `111-70-6`, with no stored formula, InChI, SMILES,
  or PubChem CID.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Hepes.yaml data/ingredients/mapped/Heptadecane.yaml data/ingredients/mapped/Heptadecanoic_Acid.yaml data/ingredients/mapped/Heptanoic_Acid.yaml data/ingredients/mapped/Heptanol.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `linkml-term-validator` passed for `CHEBI:195607`.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip_20260916_1421`
  aggregated 2951 records.
- `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip_20260916_1421`
  passed with 2 files compared, 0 data differences, and only expected
  `generation_date` metadata differences.

## Evidence

- OLS4 resolves `CHEBI:195607` as active `heptanol`, defined as a seven-carbon
  straight-chain fatty alcohol whose hydroxy group can be at any position.
- OLS4 also has active `CHEBI:43003` `heptan-1-ol` with `1-heptanol`,
  `heptane-1-ol`, `heptanol`, and `n-heptanol` as synonyms.
- PubChem resolves CAS RN `111-70-6` to `Heptanol`, formula `C7H16O`, SMILES
  `CCCCCCCO`, and InChI `InChI=1S/C7H16O/c1-2-3-4-5-6-7-8/h8H,2-7H2,1H3`,
  matching the straight-chain primary alcohol rather than a positional-isomer
  class.
- Major: because `chemical_properties.cas_rn` fixes the subject as 1-heptanol,
  the exact mapping to the broader `CHEBI:195607` heptanol class overstates the
  current identity.
- The final SSSOM publishes one `skos:exactMatch` row from `MIM:Heptanol` to
  `CHEBI:195607` and exports only `CAS:111-70-6` in `other`.

## Completeness

- The CAS RN is present, valid, and points to the more specific primary-alcohol
  identity.
- The record is incomplete until the exact ChEBI target is changed to
  `CHEBI:43003` and the formula, InChI, and SMILES are backfilled for the same
  CAS-resolved structure.

## Recommended Edits

- Major: remap the record from `CHEBI:195607` `heptanol` to `CHEBI:43003`
  `heptan-1-ol`, keep CAS `111-70-6`, backfill the 1-heptanol formula/InChI/
  SMILES, regenerate the final SSSOM row, and rerun strict, term, round-trip,
  id-label, and SSSOM validation.
