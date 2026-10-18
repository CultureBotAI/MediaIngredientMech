# `data/ingredients/mapped/Calcium_Pantothenate.yaml`

## Verdict

Needs curation, major. The `CHEBI:31345` calcium pantothenate identity and
structure fields pass, but four capsaicin/Zostrix labels are stored as active
raw synonyms and are published in the SSSOM `other` field and generated label
tables for calcium pantothenate.

## Identity

- Reviewed record: `data/ingredients/mapped/Calcium_Pantothenate.yaml`.
- Identifier and grounding: `identifier: CHEBI:31345`,
  `ontology_mapping.ontology_id: CHEBI:31345`,
  `ontology_label: Calcium pantothenate`,
  `ontology_source: CHEBI`, `mapping_quality: EXACT_MATCH`,
  `mapping_status: MAPPED`, and `ingredient_type: SINGLE_INGREDIENT`.
- Direct OLS lookup for `CHEBI:31345` returns the active label
  `Calcium pantothenate`, CAS `137-08-6`, formula `2C9H16NO5.Ca`, and ChEBI
  InChI/SMILES matching the local structure fields.
- PubChem resolves CAS `137-08-6` to CID `443753` with formula
  `C18H32CaN2O10`, the Hill form of the local and ChEBI calcium pantothenate
  formula.

## Validation

- `uv run --frozen python scripts/validate_strict.py 'data/ingredients/mapped/Calcium(2).yaml' data/ingredients/mapped/Calcium.yaml data/ingredients/mapped/Calcium_Chloride.yaml data/ingredients/mapped/Calcium_D-Pantothenate.yaml data/ingredients/mapped/Calcium_Pantothenate.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data 'data/ingredients/mapped/Calcium(2).yaml' data/ingredients/mapped/Calcium.yaml data/ingredients/mapped/Calcium_Chloride.yaml data/ingredients/mapped/Calcium_D-Pantothenate.yaml data/ingredients/mapped/Calcium_Pantothenate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
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

- The calcium pantothenate CAS, formula, InChI, SMILES, exact ChEBI mapping,
  2375/2348 occurrence count, and same-substance duplicate merges are
  internally consistent.
- The direct OLS `CHEBI:31345` synonym list does not contain
  `(E)-8-Methyl-N-vanillyl-6-nonenamide`, `Isodecenoic acid vanillylamide`,
  `Zostrix`, or `trans-8-Methyl-N-vanillyl-6-nonenamide`; those labels denote
  capsaicin/Zostrix, not calcium pantothenate.
- Hidden/ignored-inclusive search over `data/ingredients` found those four
  labels only in `data/ingredients/mapped/Calcium_Pantothenate.yaml`.
- Hidden/ignored-inclusive search over `data/curated`, `mappings`,
  `docs/data`, and `reports`, excluding bulky backups and generated
  review-report directories, found the same four labels on the active
  `MIM:Calcium_Pantothenate` SSSOM row and as unique synonyms in
  `docs/data/label_index.csv`.

## Completeness

- The exact ChEBI identifier, CAS, formula, InChI, SMILES, single-ingredient
  classification, CultureMech occurrence refresh, aggregate copy, and SSSOM row
  are populated.
- A second `VITAMIN_SOURCE` role was inherited from the rejected
  `Calcium_D-Pantothenate` record with only a 0.8 name-pattern prediction. The
  1.0 CultureMech role already captures the supported vitamin-source claim, so
  the provisional duplicate is redundant.

## Recommended Edits

- In `data/ingredients/mapped/Calcium_Pantothenate.yaml`, remove the four
  `sssom_other_backfill` aliases that denote capsaicin/Zostrix, then trace the
  #520 backfill source to decide whether those labels belong on the capsaicin
  record or should simply disappear.
- Remove the redundant 0.8 `VITAMIN_SOURCE` role inherited from
  `Calcium_D-Pantothenate`; the 1.0 CultureMech-supported role is sufficient.
- Regenerate `data/curated/mapped_ingredients.yaml`,
  `mappings/ingredient_mappings.sssom.tsv`, docs data, and label indexes; prove
  the cleanup with strict validation, round-trip verification, and
  `scripts/validate_sssom_invariants.py`.
