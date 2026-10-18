# `data/ingredients/mapped/4-hydroxybutyric_Acid.yaml`

## Verdict

Needs curation, major. The `CHEBI:30830` neutral-acid identity, CAS, chemistry,
SSSOM row, and aggregate copy pass, but the `CARBON_SOURCE` role is only a
provisional name-pattern inference and has no inspected source.

## Identity

- Reviewed record: `data/ingredients/mapped/4-hydroxybutyric_Acid.yaml`.
- Identifier and grounding: `identifier: CHEBI:30830` with
  `ontology_mapping.ontology_id: CHEBI:30830`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Official OLS/ChEBI search resolves `CHEBI:30830` to active
  `4-hydroxybutyric acid`, defined as butyric acid hydroxylated at position 4,
  and lists `4-Hydroxybutanoic acid` as an exact synonym.
- PubChem CAS lookup for `591-81-1` resolves to CID `10413` with formula
  `C4H8O3` and the same neutral-acid InChI stored in the record.
- `ingredient_type: SINGLE_INGREDIENT` is present.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/4-hydroxybutyrate.yaml data/ingredients/mapped/4-hydroxybutyric_Acid.yaml data/ingredients/mapped/4-hydroxychalcone.yaml data/ingredients/mapped/4-hydroxyphenyl_Acetic_Acid.yaml data/ingredients/mapped/4-methylumbelliferone_Beta-d-glucuronide.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/4-hydroxybutyric_Acid.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- Whole-corpus component partonomy, SSSOM invariants, and flat-export coverage
  passed in the immediately preceding batch; only SSSOM Rule B4 was skipped
  because the sibling `kg-microbe` ontology transforms are absent.

## Evidence

- The CultureBotHT CAS import, active ChEBI label, PubChem CAS lookup, stored
  formula, stored InChI, and stored SMILES all support the neutral
  4-hydroxybutyric acid identity.
- `mappings/ingredient_mappings_oak_ols_review.tsv` confirmed the
  `CHEBI:30830` mapping and asked for no curation action.
- The SSSOM row maps `MIM:4-hydroxybutyric_Acid` to `CHEBI:30830` with
  `skos:exactMatch` and carries only `4-Hydroxybutanoic acid` plus
  `CAS:591-81-1` in `other`.
- Major: `nutritional_roles.CARBON_SOURCE` is a
  `COMPUTATIONAL_PREDICTION` from a curated media-role name pattern and its
  `curator_note` explicitly says review is recommended. No active occurrence
  row demonstrates 4-hydroxybutyric acid being supplied as a carbon source in a
  specific curated medium.
- The hidden/ignored-inclusive search over `data`, `mappings`, `reports`,
  `docs`, `src`, `tests`, `scripts`, `conf`, `.github`, and `.claude` found the
  active YAML, aggregate copy, SSSOM row, OAK/OLS confirmation row, generated
  docs, stale advisory rows, and ignored aggregate backups.

## Completeness

- CAS, formula, InChI, SMILES, exact synonym, and `ingredient_type` are
  populated.
- The CultureBotHT import has no recipe-count occurrence; no components,
  environment, datasets, or discussion entries need review.
- A carbon-source role should remain absent unless an inspected CultureMech,
  CultureBotHT, MediaDive, or literature source supports this exact acid in a
  medium context.

## Recommended Edits

Remove `nutritional_roles.CARBON_SOURCE`, or replace its evidence with a
specific source showing 4-hydroxybutyric acid itself functions as a carbon
source in the curated medium context. Then resync the aggregate and rebuild
docs.
