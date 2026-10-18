# `data/ingredients/mapped/Beta-nad.yaml`

## Verdict

Needs curation, minor. The exact `CHEBI:15846` NAD(+) identity, CAS xref,
source aliases, structure values, SSSOM row, and aggregate copy pass, but
`chemical_properties.data_source` still points at PubChem even though the
current protonated structure fields are ChEBI-derived.

## Identity

- Reviewed record: `data/ingredients/mapped/Beta-nad.yaml`.
- Identifier and grounding: `identifier: CHEBI:15846` with
  `ontology_mapping.ontology_id: CHEBI:15846`,
  `ontology_label: NAD(+)`, `ontology_source: CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- OLS confirms `beta-NAD`, `NAD`, `NAD+`, and
  `Nicotinamide adenine dinucleotide` as synonyms or related synonyms of
  `CHEBI:15846`, and it lists CAS `53-84-9` as a database cross-reference.
- OLS also confirms that the stored formula `C21H28N7O14P2`, InChI with
  `/p+1`, SMILES, molecular weight, and charge describe the current
  `CHEBI:15846` NAD(+) term.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Beta-d-glucose.yaml data/ingredients/mapped/Beta-gentiobiose.yaml data/ingredients/mapped/Beta-lactose.yaml data/ingredients/mapped/Beta-nad.yaml data/ingredients/mapped/Betaine_Hydrochloride.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Beta-d-glucose.yaml data/ingredients/mapped/Beta-gentiobiose.yaml data/ingredients/mapped/Beta-lactose.yaml data/ingredients/mapped/Beta-nad.yaml data/ingredients/mapped/Betaine_Hydrochloride.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for all five records.
- The previous full-corpus `uv run --frozen python scripts/validate_sssom_invariants.py`
  run passed Rules A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was
  skipped because the sibling kg-microbe ontology transforms were absent.

## Evidence

- Hidden/ignored-inclusive search over `data/curated`, `mappings`,
  `data/custom`, and `reports`, excluding `data/curated/backups` and generated
  review directories, found the authoritative exact SSSOM row at
  `mappings/ingredient_mappings.sssom.tsv` row 582 and the aggregate copy in
  `data/curated/mapped_ingredients.yaml`.
- `mappings/ingredient_mappings_row_review_manifest.tsv` confirmed the
  `CHEBI:15846` row in the OAK/OLS review.
- `mappings/culturemech_recipe_membership.tsv` contains 17 rows for
  `CHEBI:15846`, matching the record's refreshed 17/17 medium and total
  occurrence counts.
- A parsed comparison against `data/curated/mapped_ingredients.yaml` found
  exactly one aggregate record with the same identifier and preferred term, and
  it is identical to this per-record YAML.
- PubChem's current lookup for CAS `53-84-9` resolves to CID 5892 with formula
  `C21H27N7O14P2` and the same base InChI without ChEBI's protonation layer.
  That is not an identity problem because the record targets `CHEBI:15846`, but
  it does show that the current ChEBI-specific formula and `/p+1` InChI should
  not be attributed solely to `PubChem API`.

## Completeness

- The exact CHEBI identifier, CAS RN, alias set, formula, InChI, SMILES, SSSOM
  row, occurrence statistics, and aggregate copy are populated.
- The cofactor-provider role is explicitly marked as a provisional
  computational prediction and does not claim external experimental support.
- Minor gap: `chemical_properties.data_source` is stale after the ChEBI
  structure backfill and should name ChEBI rather than PubChem alone.

## Recommended Edits

- Minor: update `data/ingredients/mapped/Beta-nad.yaml` so
  `chemical_properties.data_source` accurately names the source of the
  `CHEBI:15846` formula, InChI, SMILES, and mass; then run
  `just sync-curated` and focused strict/term validation for the record.
