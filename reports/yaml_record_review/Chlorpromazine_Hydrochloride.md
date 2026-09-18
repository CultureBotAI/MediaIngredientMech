# `data/ingredients/mapped/Chlorpromazine_Hydrochloride.yaml`

## Verdict

Pass. The CultureBotHT chlorpromazine hydrochloride record is exactly grounded
to active `CHEBI:3649`, and its CAS, formula, InChI, SMILES, exact synonym,
SSSOM row, zero occurrence count, and aggregate copy agree.

## Identity

- Reviewed record:
  `data/ingredients/mapped/Chlorpromazine_Hydrochloride.yaml`.
- Identifier and grounding: `identifier: CHEBI:3649`,
  `ontology_mapping.ontology_id: CHEBI:3649`,
  `ontology_label: chlorpromazine hydrochloride`, `ontology_source: CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Direct ChEBI and OLS lookups for `CHEBI:3649` return one active ChEBI term
  labelled `chlorpromazine hydrochloride`. ChEBI publishes CAS `69-09-0`,
  formula `H.C17H19ClN2S.Cl`, mass `355.334`, the same SMILES, the same
  standard InChI, and the same IUPAC name stored as this record's exact
  synonym.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Chloridazon.yaml data/ingredients/mapped/Chlorogenic_Acid.yaml data/ingredients/mapped/Chlororaphin.yaml data/ingredients/mapped/Chlorpromazine_Hydrochloride.yaml data/ingredients/mapped/Chlortetracycline.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Chloridazon.yaml data/ingredients/mapped/Chlorogenic_Acid.yaml data/ingredients/mapped/Chlorpromazine_Hydrochloride.yaml data/ingredients/mapped/Chlortetracycline.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for all 4 CHEBI-grounded records in this batch. `Chlororaphin` was
  intentionally skipped because its `kgmicrobe.compound` placeholder CURIE is a
  local registry ID outside Engine A's OBO prefix scope.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip.wqYt47`
  followed by
  `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip.wqYt47`:
  passed; both curated collection files had 0 data differences and only the
  expected scratch `generation_date` metadata differences.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K. Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- Hidden/ignored-inclusive search over `data`, `mappings`, `docs`, and
  `reports` found the active exact `MIM:Chlorpromazine_Hydrochloride` SSSOM
  row, the `CONFIRMED` row-review disposition, and matching aggregate and docs
  rows for `CHEBI:3649`.
- Hidden/ignored-inclusive search over repository TSV, CSV, YAML, and Markdown
  files found the `CultureBotHT` import history carrying CAS `69-09-0`, and
  PubChem lookup of that CAS returned the same hydrochloride InChI as
  ChEBI/MIM.
- The active SSSOM row includes CAS `69-09-0` and the ChEBI-reviewed exact
  synonym already present in YAML.
- Hidden/ignored-inclusive search of `mappings/culturemech_recipe_membership.tsv`
  plus `data` found no CultureMech membership rows for `CHEBI:3649`, matching
  the explicit 0/0 `occurrence_statistics`.
- The record carries no role, component, or environment claims.

## Completeness

- The exact ChEBI identifier, CAS, formula, InChI, SMILES, exact synonym, SSSOM
  row, aggregate copy, docs row, and zero occurrence count are populated and
  agree.

## Recommended Edits

- None for this record.
