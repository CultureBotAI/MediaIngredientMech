# `data/ingredients/mapped/Carnitine_Hydrochloride.yaml`

## Verdict

Pass. The record intentionally keeps a local carnitine hydrochloride identity
with a `skos:narrowMatch` to active parent `CHEBI:17126` after rejecting a
wrong carnitinamide chloride CAS backfill, and its occurrence count, SSSOM
rows, aggregate copy, and docs row agree.

## Identity

- Reviewed record: `data/ingredients/mapped/Carnitine_Hydrochloride.yaml`.
- Identifier and grounding:
  `identifier: kgmicrobe.compound:carnitine_hydrochloride`,
  `ontology_mapping.ontology_id: CHEBI:17126`,
  `ontology_label: carnitine`, `ontology_source: CHEBI`,
  `mapping_quality: NARROW_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Direct OLS lookup for `CHEBI:17126` returns active parent carnitine, and this
  record no longer carries the incorrect `CHEBI:48601` carnitinamide chloride
  mapping or the old `461-05-2` CAS assertion.
- Direct OLS search for `Carnitine Hydrochloride` returned adjacent exact terms
  for acetyl-L-carnitine hydrochloride and DL-carnitine hydrochloride, but no
  exact unqualified carnitine hydrochloride term that supersedes the local
  kgmicrobe salt identity.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Carnitine_Hydrochloride.yaml data/ingredients/mapped/Carnosic_Acid.yaml data/ingredients/mapped/Carotenoid.yaml data/ingredients/mapped/Carrageenan.yaml data/ingredients/mapped/Carrot.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Carnitine_Hydrochloride.yaml data/ingredients/mapped/Carnosic_Acid.yaml data/ingredients/mapped/Carotenoid.yaml data/ingredients/mapped/Carrageenan.yaml data/ingredients/mapped/Carrot.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed all 5 files.
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
  review-report directories, found the expected two active SSSOM rows: a
  `skos:narrowMatch` to parent `CHEBI:17126` and an exact local registry row
  for `kgmicrobe.compound:carnitine_hydrochloride`.
- The same search found the stale row-review artifacts for `CHEBI:48601`
  carnitinamide chloride, but the curated YAML no longer uses that amide
  mapping and the current SSSOM uses the corrected parent carnitine target.
- The current `mappings/culturemech_recipe_membership.tsv` rows contain 14
  distinct recipes and 14 occurrences, matching `occurrence_statistics`.

## Completeness

- The local salt identifier, broader ChEBI parent, exact local registry row,
  14/14 occurrence count, SSSOM rows, aggregate copy, and docs rows are
  populated.
- CAS and structure fields are correctly absent after the amide CAS/chemistry
  backfill was removed.

## Recommended Edits

- None for this record.
