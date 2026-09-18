# `data/ingredients/mapped/Thiamine.yaml`

## Verdict

Needs curation. The synonym match to `CHEBI:18385`, CAS RN, structure fields,
source-backed vitamin role, occurrence counts, and aggregate row pass, but the
final SSSOM `other` field exports broader or plural vitamin labels and a
concentration-qualified CultureMech surface as exact thiamine synonyms.

## Identity

- Reviewed record: `data/ingredients/mapped/Thiamine.yaml`.
- Identifier and grounding: `identifier: CHEBI:18385` with the same
  `ontology_mapping.ontology_id`, label `thiamine(1+)`, source `CHEBI`,
  `mapping_quality: SYNONYM_MATCH`, `mapping_status: MAPPED`,
  `kg_microbe_node_id: CHEBI:18385`, and `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS `70-16-6`, formula `C12H17N4OS`, and matching
  PubChem InChI/SMILES for the thiamine cation.
- Occurrences: 159 CultureMech recipe occurrences in 159 media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Thiamine-hcl_X_2_H2o` through `Thiamine_monophosphate`: exited 0 and wrote
  zero ERROR rows.
- `uv run --frozen linkml-term-validator validate-data` on the CHEBI subset
  from this batch: `Thiamine-hcl_X_2_H2o`, `Thiamine`, `Thiamine_Hcl`, and
  `Thiamine_monophosphate` all passed. The local `Thiamine_Vitamin_Solution`
  row was skipped because its exact `kgmicrobe.ingredient` ID and close `MICRO`
  parent are outside the CHEBI-focused term-validator subset.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Local OAK resolves `CHEBI:18385` with canonical label `thiamine(1+)` and the
  exact cation synonym
  `3-[(4-amino-2-methylpyrimidin-5-yl)methyl]-5-(2-hydroxyethyl)-4-methyl-1,3-thiazol-3-ium`.
- Fresh PubChem lookup by CAS `70-16-6` resolves CID 1130, formula
  `C12H17N4OS+`, and the same InChI as the curated record.
- The CultureMech `VITAMIN_SOURCE` role is source-backed by the original
  `DATABASE_ENTRY` role text `Vitamin Source`.
- Major: the final SSSOM row for `MIM:Thiamine` publishes non-exact
  kg-microbe enrichment labels such as `vitamin B1 vitamer`, `vitamin B1
  vitamers`, and plural thiamine labels, plus the concentration-qualified
  recipe text `Thiamine (0.05 ug/mL)`, in `other`.

## Completeness

- The CHEBI identity, CAS RN, structure fields, source-backed role, occurrence
  count, aggregate copy, and final SSSOM row identity agree.
- No components or environmental contexts are asserted.
- An ignored/hidden search of the active local curated, mapping, generated,
  source, and report paths found the expected CultureMech import, CAS-conflict
  repair, alias backfill, OAK/OLS row-review, aggregate, and final SSSOM rows.

## Recommended Edits

- Major: in `data/ingredients/mapped/Thiamine.yaml`, remove or retype the
  broader/plural `vitamin B1 vitamer`, `vitamin B1 vitamers`, `thiamines`,
  `thiamins`, and `vitamins B1` labels so they do not publish as exact
  `other` values for `CHEBI:18385`.
- Major: in `data/ingredients/mapped/Thiamine.yaml`, keep the CultureMech
  occurrence surface `Thiamine (0.05 ug/mL)` as provenance only or filter it
  from SSSOM export. Then rerun strict validation, SSSOM publication,
  synonym-row review, and `scripts/validate_sssom_invariants.py`.
