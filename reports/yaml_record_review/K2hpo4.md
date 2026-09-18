# `data/ingredients/mapped/K2hpo4.yaml`

## Verdict

Needs curation. The anhydrous dipotassium hydrogen phosphate identity, CAS RN,
structure fields, buffer role, occurrence count, and exact ChEBI grounding pass,
but the final SSSOM `other` column still exposes a sibling trihydrate label and
raw source variants that are not clean synonyms.

## Identity

- Reviewed record: `data/ingredients/mapped/K2hpo4.yaml`.
- Identifier and grounding: `identifier: CHEBI:131527` with
  `ontology_mapping.ontology_id: CHEBI:131527`, label
  `dipotassium hydrogen phosphate`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS RN `7758-11-4`, formula `HO4P.2K`, InChI
  `InChI=1S/2K.H3O4P/c;;1-5(2,3)4/h;;(H3,1,2,3,4)/q2*+1;/p-2`, and SMILES
  `O=P([O-])([O-])O.[K+].[K+]`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/K2cro4.yaml data/ingredients/mapped/K2hpo4.yaml data/ingredients/mapped/K2hpo4_X_3_H2o.yaml data/ingredients/mapped/K2s4o6.yaml data/ingredients/mapped/K2so4.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- Engine A LinkML term validation passed for all 5 records.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip_20260916_2140`
  aggregated 2951 records.
- `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip_20260916_2140`
  passed with 2 files compared, 0 data differences, and only expected
  `generation_date` metadata differences.

## Evidence

- OLS4 resolves `CHEBI:131527` as active anhydrous
  `dipotassium hydrogen phosphate`, with CAS xref `7758-11-4`, formula
  `HO4P.2K`, the same InChI and SMILES stored on the record, and the curated
  specific salt labels as synonyms.
- PubChem resolves CAS RN `7758-11-4` to the same anhydrous dipotassium hydrogen
  phosphate InChI stored on the record.
- PMID `40302155` resolves through NCBI E-utilities and contains the stored
  `K2HPO4` text, but the article is about potassium fertilizer treatments in
  purple sweet potato rather than media ingredients; its auto-proposed evidence
  row is not needed for the CultureMech exact mapping.
- The `physicochemical_roles.BUFFER` claim is backed by CultureMech
  `Role: Buffer` database text, and the final SSSOM correctly omits all raw
  `Role:` and `Properties:` strings.
- Major: the final SSSOM `other` column exports `K2HPO4 x 3 H2O` on the
  anhydrous parent row even though the trihydrate has its own local
  `kgmicrobe.compound:k2hpo4_x_3_h2o` identity.
- Major: the final SSSOM also exports `K2HPO` and `K2HPO4(Sigma P 3786)` from
  `RAW_TEXT` source variants. The former is an incomplete formula and the
  latter carries a catalog note; neither is curated as a clean resolving
  synonym.
- The hidden and ignored-inclusive search over `data`, `src`, `tests`,
  `mappings`, `scripts`, `conf`, `docs`, and `.claude` found the current
  aggregate row, final SSSOM row, docs projections, row-review dispositions,
  the retired `K2hpo.yaml` normalization row, and the trihydrate sibling
  record.

## Completeness

- The active ChEBI identifier, CAS RN, formula, InChI, SMILES, exact
  anhydrous-salt synonyms, aggregate copy, occurrence count, and buffer role are
  present and consistent.
- The final SSSOM is incomplete until its `other` tokens are limited to true
  anhydrous dipotassium hydrogen phosphate synonyms.

## Recommended Edits

- Major: repair the maintained synonym/provenance source that causes
  `K2HPO4 x 3 H2O`, `K2HPO`, and `K2HPO4(Sigma P 3786)` to be emitted for
  `data/ingredients/mapped/K2hpo4.yaml`, then rebuild the final SSSOM and docs
  surfaces.
- Minor: remove or rephrase the auto-proposed PMID `40302155` evidence row so
  ontology-mapping evidence is limited to sources that support the exact
  media-ingredient identity.
