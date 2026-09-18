# `data/ingredients/mapped/Hymecromone_Methyl_Ether.yaml`

## Verdict

Pass. The CAS-primary record was correctly regraded from a same-formula parent
to an exact synonym match, and its CHEBI, CAS registry, structure fields, and
final SSSOM rows now agree.

## Identity

- Reviewed record:
  `data/ingredients/mapped/Hymecromone_Methyl_Ether.yaml`.
- Identifier and grounding: `identifier: cas:2555-28-4` with
  `ontology_mapping.ontology_id: CHEBI:107662`, label
  `7-methoxy-4-methyl-1-benzopyran-2-one`, source `CHEBI`,
  `mapping_quality: SYNONYM_MATCH`,
  `mapping_status: MAPPED`, and `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS RN `2555-28-4`, PubChem CID `390807`, formula
  `C11H10O3`, InChI
  `InChI=1S/C11H10O3/c1-7-5-11(12)14-10-6-8(13-2)3-4-9(7)10/h3-6H,1-2H3`,
  and SMILES `CC1=CC(=O)OC2=C1C=CC(=C2)OC`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Hygromycin.yaml data/ingredients/mapped/Hygromycin_A.yaml data/ingredients/mapped/Hygromycin_B.yaml data/ingredients/mapped/Hymecromone_Methyl_Ether.yaml data/ingredients/mapped/Hypotaurine.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Hymecromone_Methyl_Ether.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip_20260916_1520`
  aggregated 2951 records.
- `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip_20260916_1520`
  passed with 2 files compared, 0 data differences, and only expected
  `generation_date` metadata differences.

## Evidence

- OLS4 resolves `CHEBI:107662` as the active ChEBI class
  `7-methoxy-4-methyl-1-benzopyran-2-one`.
- PubChem resolves both the record CAS RN `2555-28-4` and stored CID `390807`
  to the same formula and InChI stored on the record.
- The row-review manifest classifies the CAS and local
  `kgmicrobe.compound` `UNKNOWN_TERM` rows as expected registry identifiers.
- The final SSSOM publishes one `skos:exactMatch` row to `CHEBI:107662` and
  one exact CAS registry row, both exporting only `CAS:2555-28-4` in `other`.
- The hidden and ignored-inclusive search over `data`, `src`, `tests`,
  `mappings`, `scripts`, `conf`, `docs`, and `.claude` found the current
  aggregate rows, final SSSOM rows, docs projections, and #326 regrade
  provenance.

## Completeness

- The active ChEBI identifier, CAS RN, PubChem CID, formula, InChI, SMILES,
  aggregate copy, and final SSSOM rows are present and consistent.
- No unsupported roles or non-synonym final `other` tokens are asserted.

## Recommended Edits

- None.
