# `data/ingredients/mapped/Kanamycin_Sulfate.yaml`

## Verdict

Needs curation. The exact ChEBI kanamycin A sulfate identity, formula, InChI,
SMILES, kg-microbe synonyms, occurrence count, and final SSSOM predicate pass,
but the CAS RN is transposed and the selective-agent role is only provisional
name-pattern evidence.

## Identity

- Reviewed record: `data/ingredients/mapped/Kanamycin_Sulfate.yaml`.
- Identifier and grounding: `identifier: CHEBI:6109` with
  `ontology_mapping.ontology_id: CHEBI:6109`, label `kanamycin A sulfate`,
  source `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: formula `C18H36N4O11.H2O4S`, InChI
  `InChI=1S/C18H36N4O11.H2O4S/c19-2-6-10(25)12(27)13(28)18(30-6)33-16-5(21)1-4(20)15(14(16)29)32-17-11(26)8(22)9(24)7(3-23)31-17;1-5(2,3)4/h4-18,23-29H,1-3,19-22H2;(H2,1,2,3,4)/t4-,5+,6-,7-,8+,9-,10-,11-,12+,13-,14-,15+,16-,17-,18-;/m1./s1`,
  and SMILES matching active ChEBI, but CAS RN `25839-94-0` does not match the
  active ChEBI term.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/K2so4_X_7_H2o.yaml data/ingredients/mapped/KH2PO3.yaml data/ingredients/mapped/Kanamycin.yaml data/ingredients/mapped/Kanamycin_Sulfate.yaml data/ingredients/mapped/Kanchanomycin.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- Engine A LinkML term validation passed for all 5 records.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip_20260916_2150`
  aggregated 2951 records.
- `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip_20260916_2150`
  passed with 2 files compared, 0 data differences, and only expected
  `generation_date` metadata differences.

## Evidence

- OLS4 resolves `CHEBI:6109` as the active ChEBI class
  `kanamycin A sulfate`, with formula `C18H36N4O11.H2O4S`, the same InChI and
  SMILES stored on the record, and the exported kg-microbe labels as synonyms.
- Major: OLS4 lists CAS xref `25389-94-0` for `CHEBI:6109`; PubChem resolves
  `25389-94-0` to the same InChI stored on this record, while the stored
  `25839-94-0` returns 404 and is also exported by final SSSOM as
  `CAS:25839-94-0`.
- The final SSSOM publishes one `skos:exactMatch` row from
  `MIM:Kanamycin_Sulfate` to `CHEBI:6109` and exports only specific Kanamycin A
  sulfate synonyms apart from the bad CAS token.
- Major: `physicochemical_roles.SELECTIVE_AGENT` has only
  `COMPUTATIONAL_PREDICTION` evidence from a curated name-pattern rule, with no
  inspected CultureMech, FEBA, Hans80, or literature evidence attached to the
  claim.
- The hidden and ignored-inclusive search over `data/ingredients`, `mappings`,
  `reports/kg_microbe_node_id_mismatches.tsv`, `reports/hydrate_grounding.tsv`,
  `docs/data`, `src`, `tests`, `conf`, and `.claude` found the current
  per-record YAML, final SSSOM row, docs projections, OAK/OLS confirmation, and
  five current CultureMech membership rows.

## Completeness

- The active ChEBI identifier, formula, InChI, SMILES, specific synonyms,
  aggregate copy, occurrence count, and final SSSOM identity row are present and
  consistent.
- The record is incomplete until the CAS RN is corrected and the
  selective-agent role is either supported by inspected claim-level evidence or
  removed.

## Recommended Edits

- Major: replace `chemical_properties.cas_rn: 25839-94-0` with
  `25389-94-0` in `data/ingredients/mapped/Kanamycin_Sulfate.yaml` and rebuild
  final SSSOM/docs surfaces so `CAS:25839-94-0` is no longer published.
- Major: remove `physicochemical_roles.SELECTIVE_AGENT` unless an inspected
  CultureMech, FEBA, Hans80, or literature source can support kanamycin sulfate
  as a selective agent, then rerun strict, term, round-trip, id-label,
  component, and SSSOM validation.
