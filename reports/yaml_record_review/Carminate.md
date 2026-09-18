# `data/ingredients/mapped/Carminate.yaml`

## Verdict

Pass with minor issues. The MicrobeDecoder label is grounded to active
`CHEBI:149531` carminate(2-) and the formula, structure fields, SSSOM row, and
aggregate copy agree, but the local evidence note overstates this dianion as a
fully deprotonated species.

## Identity

- Reviewed record: `data/ingredients/mapped/Carminate.yaml`.
- Identifier and grounding: `identifier: CHEBI:149531`,
  `ontology_mapping.ontology_id: CHEBI:149531`,
  `ontology_label: carminate(2-)`, `ontology_source: CHEBI`,
  `mapping_quality: SYNONYM_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Direct OLS lookup for `CHEBI:149531` returns the active carminate(2-) term
  with formula `C22H18O13`, charge `-2.0`, mass `490.373`, and the same
  InChI/SMILES as the local `chemical_properties`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Carboxymethyl_Cellulose.yaml data/ingredients/mapped/Carcinomycin.yaml data/ingredients/mapped/Carminate.yaml data/ingredients/mapped/Carminomycin.yaml data/ingredients/mapped/Carnitine_Dl_Hydrochloride.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Carboxymethyl_Cellulose.yaml data/ingredients/mapped/Carcinomycin.yaml data/ingredients/mapped/Carminate.yaml data/ingredients/mapped/Carminomycin.yaml data/ingredients/mapped/Carnitine_Dl_Hydrochloride.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  validated `Carboxymethyl_Cellulose`, then stopped on `Carcinomycin` because
  the local kgmicrobe adapter has no `rdfs_label_statement` table.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Carboxymethyl_Cellulose.yaml data/ingredients/mapped/Carminate.yaml data/ingredients/mapped/Carminomycin.yaml data/ingredients/mapped/Carnitine_Dl_Hydrochloride.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed all 4 external-ontology records.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip.GkFQqh`
  followed by
  `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip.GkFQqh`:
  passed; both curated collection files had 0 data differences and only the
  expected scratch `generation_date` metadata differences.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K. Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- Hidden/ignored-inclusive search over `data/curated`, `mappings`,
  `docs/data`, and `reports`, excluding bulky backups and generated
  review-report directories, found the active `MIM:Carminate` SSSOM row with
  the exact ChEBI target and matching aggregate/docs rows.
- The current `mappings/culturemech_recipe_membership.tsv` table has 0 rows
  for `CHEBI:149531`, matching `occurrence_statistics` `0/0`.
- The retained raw `Carminate` synonym is scoped to the one MicrobeDecoder
  `BacDive_Metabolite_utilization` source occurrence.
- The #213 evidence note says the record was grounded to "the fully
  deprotonated species". ChEBI instead defines `CHEBI:149531` as the dianion
  from deprotonating the 3-hydroxy and 7-carboxy groups of carminic acid and
  as the major species at pH 7.3; the local CURIE and structure are right, but
  that phrase should be narrowed.

## Completeness

- The exact ChEBI identifier, formula, InChI, SMILES, molecular weight,
  MicrobeDecoder source occurrence, SSSOM row, aggregate copy, and docs row
  are populated.
- CAS is correctly absent: OLS lists no CAS xref for the carminate dianion.

## Recommended Edits

- Minor: update the #213
  `data/ingredients/mapped/Carminate.yaml` evidence note to say
  `CHEBI:149531` is carminate(2-), the major pH 7.3 dianion, instead of
  calling it fully deprotonated; then rerun strict validation, SSSOM QC,
  aggregate roundtrip, and `git diff --check`.
