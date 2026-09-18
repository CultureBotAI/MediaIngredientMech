# `data/ingredients/mapped/3-Aminopropionitrile_Fumarate.yaml`

## Verdict

Pass with minor issues, minor. The CAS-derived `CHEBI:91084`
`beta-aminopropionitrile hemifumarate` identity, chemistry, SSSOM row, and
aggregate row pass; only stale advisory rows still ask for ChEBI and structure
verification that now pass.

## Identity

- Reviewed record:
  `data/ingredients/mapped/3-Aminopropionitrile_Fumarate.yaml`.
- Identifier and grounding: `identifier: CHEBI:91084` with
  `ontology_mapping.ontology_id: CHEBI:91084`, source `CHEBI`,
  `mapping_quality: CAS_RN_LOOKUP`, and `mapping_status: MAPPED`.
- Official ChEBI check: the refreshed EMBL-EBI ChEBI page for `CHEBI:91084`
  resolves to `beta-aminopropionitrile hemifumarate`, lists formula
  `2C3H6N2.C4H4O4`, carries CAS `2079-89-2`, and matches the record formula,
  InChI, and SMILES.
- `ingredient_type: SINGLE_INGREDIENT` is present, and the
  `bis(2-cyanoethan-1-aminium) (2E)-but-2-enedioate` ChEBI synonym is already
  represented.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/24-Dinitrophenol.yaml data/ingredients/mapped/24-diamino-67-di-iso-propylpteridine_phosphate.yaml data/ingredients/mapped/25-Dihydroxy-4-Methoxychalcone.yaml data/ingredients/mapped/3-Aminophenol.yaml data/ingredients/mapped/3-Aminopropionitrile_Fumarate.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/3-Aminopropionitrile_Fumarate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- Whole-corpus checks run earlier in this review pass passed; only the shared
  evidence validator was unavailable because `../culturebotai-claw` is absent.
- Per-record/aggregate comparison against `data/curated/mapped_ingredients.yaml`:
  exact equality passed.
- `mappings/ingredient_mappings.sssom.tsv` contains the expected exact
  `MIM:3-Aminopropionitrile_Fumarate` to `CHEBI:91084` row, with the
  represented IUPAC synonym and CAS `2079-89-2` in the SSSOM `other` field.

## Evidence

- The active ChEBI page verifies the hemifumarate stoichiometry and matches the
  record formula, InChI, and SMILES.
- `occurrence_statistics` reports `0/0`; the record came from CultureBotHT CAS
  input rather than a counted CultureMech recipe occurrence.
- `mappings/ingredient_mappings_synonym_enrich_review.tsv` already resolved the
  proposed synonym enrichment as `ALREADY_REPRESENTED`.
- Stale: `mappings/record_research_validation.tsv` still contains old P1/P2
  rows asking for direct `CHEBI:91084` and InChI verification; the current
  ChEBI page verifies the exact target and the active full InChI.
- The hidden/ignored-inclusive search over `data/custom`, `data/curated`,
  `data/ingredients`, `mappings`, and `reports` found the active YAML,
  aggregate, SSSOM, synonym-enrichment review, OAK/OLS review, and advisory
  rows.

## Completeness

- `ingredient_type: SINGLE_INGREDIENT` is present.
- Core chemistry is complete for the active ChEBI identity.
- No record-local curation defect remains.

## Recommended Edits

No YAML edit is required for this record. The stale advisory rows can be
ignored or refreshed when `mappings/record_research_validation.tsv` is rebuilt.
