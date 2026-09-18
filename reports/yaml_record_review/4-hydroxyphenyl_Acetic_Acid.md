# `data/ingredients/mapped/4-hydroxyphenyl_Acetic_Acid.yaml`

## Verdict

Needs curation, major. The repaired `CHEBI:18101` identity, CAS, chemistry,
occurrence count, and SSSOM row pass, but two exact synonyms still denote
`CHEBI:156387` aspyrone and the `CARBON_SOURCE` role is an unreviewed
provisional LLM assertion.

## Identity

- Reviewed record: `data/ingredients/mapped/4-hydroxyphenyl_Acetic_Acid.yaml`.
- Identifier and grounding: `identifier: CHEBI:18101` with
  `ontology_mapping.ontology_id: CHEBI:18101`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Official OLS/ChEBI check: `CHEBI:18101` is active, resolves to
  `4-hydroxyphenylacetic acid`, has formula `C8H8O3`, CAS `156-38-7`, SMILES
  `O=C(O)Cc1ccc(O)cc1`, and the stored InChI.
- PubChem CAS lookup for `156-38-7` resolves to CID `127` with formula
  `C8H8O3` and the same InChI.
- Official OLS/ChEBI check: the still-exported synonym `aspyrone` is the label
  of `CHEBI:156387`, a distinct 2-pyranone with formula `C9H12O4`, CAS
  `17398-00-4`, and the systematic name stored as the second bad synonym.
- `ingredient_type: SINGLE_INGREDIENT` is present.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/4-hydroxybutyrate.yaml data/ingredients/mapped/4-hydroxybutyric_Acid.yaml data/ingredients/mapped/4-hydroxychalcone.yaml data/ingredients/mapped/4-hydroxyphenyl_Acetic_Acid.yaml data/ingredients/mapped/4-methylumbelliferone_Beta-d-glucuronide.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/4-hydroxyphenyl_Acetic_Acid.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- Whole-corpus component partonomy, SSSOM invariants, and flat-export coverage
  passed in the immediately preceding batch; only SSSOM Rule B4 was skipped
  because the sibling `kg-microbe` ontology transforms are absent.

## Evidence

- The 2026-04-18 remap from `CHEBI:156387` to `CHEBI:18101` was correct: the
  active ChEBI term, CAS `156-38-7`, PubChem properties, formula, SMILES, and
  InChI all support 4-hydroxyphenylacetic acid.
- Major: the synonyms `aspyrone` and
  `(5S,6R)-5-hydroxy-6-methyl-3-[(2S,3S)-3-methyloxiran-2-yl]-5,6-dihydro-2H-pyran-2-one`
  are exact names of `CHEBI:156387`, not `CHEBI:18101`. The record history
  explicitly says `CHEBI:156387` was the old wrong compound, but the
  `ADDED_SYNONYMS` event on the same day reintroduced the old aspyrone labels.
- The bad aspyrone strings publish in `mappings/ingredient_mappings.sssom.tsv`
  `other` beside the legitimate 4-hydroxyphenylacetic acid synonyms and
  `CAS:156-38-7`.
- Major: `nutritional_roles.CARBON_SOURCE` is only
  `COMPUTATIONAL_PREDICTION` from in-session reasoning, says no external API
  was used, and explicitly says review is recommended.
- `mappings/ingredient_mappings_row_review_manifest.tsv` found the row-review
  synonym candidate already represented, but that only confirms the bad
  aspyrone strings were present; it does not make them valid synonyms.
- The hidden/ignored-inclusive search over `data`, `mappings`, `reports`,
  `docs`, `src`, `tests`, `scripts`, `conf`, `.github`, and `.claude` found the
  active YAML, aggregate copy, SSSOM row, OAK/OLS synonym-enrichment row,
  generated docs, CultureMech occurrence rows, stale advisory rows, and ignored
  aggregate backups.

## Completeness

- CAS, formula, InChI, SMILES, occurrence counts, kg-microbe node ID, and
  `ingredient_type` are populated.
- The legitimate ChEBI synonyms `(4-hydroxyphenyl)acetic acid`,
  `(p-hydroxyphenyl)acetic acid`, and `4-Hydroxyphenylacetate` are acceptable.
- No components, environment, or discussion entries need review.

## Recommended Edits

1. Remove the two aspyrone-derived `kg_microbe` exact synonyms from
   `data/ingredients/mapped/4-hydroxyphenyl_Acetic_Acid.yaml` and
   `data/curated/mapped_ingredients.yaml`, then regenerate the SSSOM and docs
   so they no longer publish through `other`.
2. Remove `nutritional_roles.CARBON_SOURCE`, or replace its evidence with a
   source that specifically supports 4-hydroxyphenylacetic acid as a carbon
   source in a curated medium context.
