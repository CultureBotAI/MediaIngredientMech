# `data/ingredients/mapped/Hydroxy-l-proline.yaml`

## Verdict

Needs curation. The CAS-derived exact ChEBI identity, structure fields,
synonyms, and final SSSOM row pass, but `AMINO_ACID_SOURCE` is still only a
provisional CHEBI-ancestry assertion.

## Identity

- Reviewed record: `data/ingredients/mapped/Hydroxy-l-proline.yaml`.
- Identifier and grounding: `identifier: CHEBI:18095` with
  `ontology_mapping.ontology_id: CHEBI:18095`, label
  `trans-4-hydroxy-L-proline`, source `CHEBI`,
  `mapping_quality: CAS_RN_LOOKUP`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS RN `51-35-4`, formula `C5H9NO3`, InChI
  `InChI=1S/C5H9NO3/c7-3-1-4(5(8)9)6-2-3/h3-4,6-7H,1-2H2,(H,8,9)/t3-,4+/m1/s1`,
  and SMILES `O=C(O)[C@@H]1C[C@@H](O)CN1`.
- Source occurrences: three FEBA media occurrences.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Hydrogen_gas.yaml data/ingredients/mapped/Hydroquinone.yaml data/ingredients/mapped/Hydrous_Ferric_Oxide.yaml data/ingredients/mapped/Hydroxocobalamin_hydrochloride.yaml data/ingredients/mapped/Hydroxy-l-proline.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Hydroxy-l-proline.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip_20260916_1501`
  aggregated 2951 records.
- `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip_20260916_1501`
  passed with 2 files compared, 0 data differences, and only expected
  `generation_date` metadata differences.

## Evidence

- OLS4 resolves `CHEBI:18095` as the active ChEBI class
  `trans-4-hydroxy-L-proline`; the stored KG-Microbe synonyms are present on
  that ChEBI term.
- PubChem resolves CAS RN `51-35-4` to `L-Hydroxyproline`, formula `C5H9NO3`,
  and the same stereospecific InChI stored on the record.
- The final SSSOM publishes one `skos:exactMatch` row from
  `MIM:Hydroxy-l-proline` to `CHEBI:18095` and exports only inspected
  ChEBI-compatible synonyms plus `CAS:51-35-4` in `other`.
- Major: `nutritional_roles.AMINO_ACID_SOURCE` has only provisional
  `COMPUTATIONAL_PREDICTION` evidence from CHEBI ancestry.
- The hidden and ignored-inclusive search over `data`, `src`, `tests`,
  `mappings`, `scripts`, `conf`, `docs`, and `.claude` found the current
  aggregate row, final SSSOM row, legacy MIM CURIE alias, docs projections, and
  OAK/OLS review row marking the mapping `CONFIRMED`.

## Completeness

- The active ChEBI identifier, CAS RN, formula, InChI, SMILES, source
  occurrences, aggregate copy, and final SSSOM row are present and consistent.
- The record is incomplete until the amino-acid-source role is either supported
  by inspected claim-level evidence or removed.

## Recommended Edits

- Major: remove `nutritional_roles.AMINO_ACID_SOURCE` unless an inspected FEBA
  source or literature source can support hydroxy-L-proline as an amino acid
  source, then rerun strict, term, round-trip, id-label, component, and SSSOM
  validation.
