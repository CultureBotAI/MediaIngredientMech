# `data/ingredients/mapped/4-hydroxychalcone.yaml`

## Verdict

Pass, none. The `CHEBI:34423` identity, CAS, exact synonym, chemistry, SSSOM
row, and aggregate copy pass.

## Identity

- Reviewed record: `data/ingredients/mapped/4-hydroxychalcone.yaml`.
- Identifier and grounding: `identifier: CHEBI:34423` with
  `ontology_mapping.ontology_id: CHEBI:34423`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Official OLS/ChEBI check: `CHEBI:34423` is active, resolves to
  `4-hydroxychalcone`, defines trans-chalcone with a 4-hydroxy substitution,
  and has formula `C15H12O2`, CAS `20426-12-4`, SMILES
  `O=C(/C=C/c1ccc(O)cc1)c1ccccc1`, and the stored E-alkene InChI.
- PubChem CAS lookup for `20426-12-4` resolves to CID `5282361` with formula
  `C15H12O2` and the same InChI.
- `ingredient_type: SINGLE_INGREDIENT` is present.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/4-hydroxybutyrate.yaml data/ingredients/mapped/4-hydroxybutyric_Acid.yaml data/ingredients/mapped/4-hydroxychalcone.yaml data/ingredients/mapped/4-hydroxyphenyl_Acetic_Acid.yaml data/ingredients/mapped/4-methylumbelliferone_Beta-d-glucuronide.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/4-hydroxychalcone.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- Whole-corpus component partonomy, SSSOM invariants, and flat-export coverage
  passed in the immediately preceding batch; only SSSOM Rule B4 was skipped
  because the sibling `kg-microbe` ontology transforms are absent.

## Evidence

- The CultureBotHT CAS import, active ChEBI CAS xref, PubChem CAS lookup,
  formula, InChI, and SMILES all support the exact neutral
  4-hydroxychalcone identity with E stereochemistry at the alkene.
- The active synonym `(2E)-3-(4-hydroxyphenyl)-1-phenylprop-2-en-1-one` is
  ChEBI's exact IUPAC synonym and is correctly exported through SSSOM `other`
  together with `CAS:20426-12-4`.
- `mappings/ingredient_mappings_oak_ols_review.tsv` confirmed the mapping and
  asked for no curation action.
- The hidden/ignored-inclusive search over `data`, `mappings`, `reports`,
  `docs`, `src`, `tests`, `scripts`, `conf`, `.github`, and `.claude` found the
  active YAML, aggregate copy, SSSOM row, OAK/OLS confirmation row, generated
  docs, stale advisory rows, and ignored aggregate backups.

## Completeness

- CAS, formula, InChI, SMILES, an exact IUPAC synonym, and `ingredient_type` are
  populated.
- This CultureBotHT import has no recipe-count occurrence; no roles,
  components, environment, or discussion entries need review.

## Recommended Edits

No YAML edit is required for this record.
