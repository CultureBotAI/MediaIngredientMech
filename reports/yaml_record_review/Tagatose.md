# `data/ingredients/mapped/Tagatose.yaml`

## Verdict

Pass. The generic MicrobeDecoder surface `Tagatose` maps exactly to active
`CHEBI:33954`, the CHEBI/PubChem structure fields match that generic hexose
identity, and the final SSSOM exports a single clean exact CHEBI row.

## Identity

- Reviewed record: `data/ingredients/mapped/Tagatose.yaml`.
- Identifier and grounding: `identifier: CHEBI:33954` with
  `ontology_mapping.ontology_id: CHEBI:33954`, label `tagatose`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: formula `C6H12O6`, an InChI retrieved from
  ChEBI+PubChem, and molecular weight `180.156`.
- Occurrences: zero CultureMech recipe occurrences and 1 MicrobeDecoder
  metabolite-utilization row.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `TYGVS_Glucose` through `Takara_DO_Supp_MinusHisLeuTrp`: exited 0 and wrote
  zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI record.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh OLS4 lookup resolves active `CHEBI:33954` as `tagatose`.
- The structured mapping evidence preserves the MicrobeDecoder OLS
  label-exact import for `kgmicrobe.trait:tagatose`, and the promotion history
  records a later `review-ingredients` approval.
- The final SSSOM has exactly one exact CHEBI row for `MIM:Tagatose`, points at
  `CHEBI:33954`, names `obo:chebi.owl`, and publishes no unsafe `other`
  synonyms.

## Completeness

- The CHEBI identity, structure fields, aggregate row, MicrobeDecoder source
  occurrence, and final SSSOM row agree.
- More specific curated records for `D-(-)-tagatose` and `D-tagatose` remain
  separate records and do not make this generic `Tagatose` record stale.
- An ignored/hidden search of local curated, mapping, generated, report,
  source, and documentation paths found the expected MicrobeDecoder import,
  promotion, aggregate, generated, and final SSSOM rows.

## Recommended Edits

- None.
