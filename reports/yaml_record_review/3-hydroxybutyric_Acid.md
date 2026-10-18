# `data/ingredients/mapped/3-hydroxybutyric_Acid.yaml`

## Verdict

Needs curation, major. The exact `CHEBI:20067` neutral
`3-hydroxybutyric acid` identity, CAS, ChEBI chemistry, SSSOM row, and aggregate
row pass; the `CARBON_SOURCE` role is still supported only by provisional
name-pattern evidence.

## Identity

- Reviewed record: `data/ingredients/mapped/3-hydroxybutyric_Acid.yaml`.
- Identifier and grounding: `identifier: CHEBI:20067` with
  `ontology_mapping.ontology_id: CHEBI:20067`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Official ChEBI check: `CHEBI:20067` resolves to `3-hydroxybutyric acid`, lists
  CAS `300-85-6`, formula `C4H8O3`, InChI
  `InChI=1S/C4H8O3/c1-3(5)2-4(6)7/h3,5H,2H2,1H3,(H,6,7)`, and SMILES
  `CC(O)CC(=O)O`; the record matches.
- `3-hydroxybutanoic acid` is an exact ChEBI synonym.
- `ingredient_type: SINGLE_INGREDIENT` is present.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/3-hydroxybutyric_Acid.yaml data/ingredients/mapped/3-indolyl_Acetic_Acid.yaml data/ingredients/mapped/3-methyl-1-butanol.yaml data/ingredients/mapped/3-methyl-2-butenol.yaml data/ingredients/mapped/3-methyl-2-oxopentanoic_Acid.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/3-hydroxybutyric_Acid.yaml data/ingredients/mapped/3-indolyl_Acetic_Acid.yaml data/ingredients/mapped/3-methyl-1-butanol.yaml data/ingredients/mapped/3-methyl-2-butenol.yaml data/ingredients/mapped/3-methyl-2-oxopentanoic_Acid.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- Whole-corpus checks run earlier in this review pass passed; only the shared
  evidence validator was unavailable because `../culturebotai-claw` is absent.
- The active aggregate, `mappings/ingredient_mappings.sssom.tsv`, generated
  indexes, and docs all contain the expected exact `CHEBI:20067` row.

## Evidence

- The CultureBotHT provenance supplies CAS `300-85-6`; ChEBI confirms that CAS,
  formula, neutral charge, InChI, SMILES, and canonical label for the same
  substance.
- The SSSOM row uses `skos:exactMatch` from
  `MIM:3-hydroxybutyric_Acid` to `CHEBI:20067`, which is the correct predicate
  for the neutral, stereochemically unspecified acid.
- Stale: `mappings/record_research_validation.tsv` still reports that direct
  ChEBI inspection was needed. The identifier now resolves and the structure
  matches.
- Major: the `nutritional_roles.CARBON_SOURCE` assertion cites only
  `Inferred from curated media-role name pattern`. That is a discovery hint, not
  inspected source evidence that this exact acid was supplied as a carbon source
  in a medium.
- The hidden/ignored-inclusive search over `data`, `mappings`, `reports`,
  `docs`, `scripts`, `conf`, `src`, `tests`, `.github`, and `.claude` found the
  active YAML, aggregate copy, SSSOM row, generated docs, stale advisory rows,
  and ignored aggregate backups.

## Completeness

- Formula, CAS, InChI, and SMILES are populated and describe the neutral acid.
- The record intentionally stays separate from `3-hydroxybutyrate`
  (`CHEBI:37054`) and from the stereospecific `(R)`/`(S)` records.
- No source occurrence count is missing for this CultureBotHT CAS import.

## Recommended Edits

1. In `data/ingredients/mapped/3-hydroxybutyric_Acid.yaml`, either replace the
   provisional `CARBON_SOURCE` evidence with inspected, claim-level evidence or
   remove the role.
2. Run `just sync-curated`, rebuild SSSOM and docs, then verify with
   `just validate-all`, `just qc-sssom`, `just qc-roundtrip`, and
   `just validate-terms data/ingredients/mapped/3-hydroxybutyric_Acid.yaml`.
