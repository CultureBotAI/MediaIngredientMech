# `data/ingredients/mapped/4-azido-L-phenylalanine.yaml`

## Verdict

Needs curation, major. The `CHEBI:228211` identity, CAS, chemistry, SSSOM row,
and aggregate row pass, but the inherited `AMINO_ACID_SOURCE` role is only a
provisional ChEBI-ancestry inference for a bioorthogonal unnatural amino acid.

## Identity

- Reviewed record: `data/ingredients/mapped/4-azido-L-phenylalanine.yaml`.
- Identifier and grounding: `identifier: CHEBI:228211` with
  `ontology_mapping.ontology_id: CHEBI:228211`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Official OLS/ChEBI check: `CHEBI:228211` is active, resolves to
  `4-azido-L-phenylalanine`, has formula `C9H10N4O2`, CAS `33173-53-4`,
  SMILES `[N-]=[N+]=Nc1ccc(C[C@H](N)C(=O)O)cc1`, and the stored InChI.
- PubChem CAS lookup for `33173-53-4` resolves to CID `3080772` with formula
  `C9H10N4O2` and the same InChI.
- `ingredient_type: SINGLE_INGREDIENT` is present.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/4-acetoxyphenol.yaml data/ingredients/mapped/4-aminobenzoate.yaml data/ingredients/mapped/4-aminobutyrate.yaml data/ingredients/mapped/4-azido-L-phenylalanine.yaml data/ingredients/mapped/4-benzoyl-L-phenylalanine.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/4-acetoxyphenol.yaml data/ingredients/mapped/4-aminobenzoate.yaml data/ingredients/mapped/4-aminobutyrate.yaml data/ingredients/mapped/4-azido-L-phenylalanine.yaml data/ingredients/mapped/4-benzoyl-L-phenylalanine.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- Whole-corpus checks run earlier in this review pass passed; only the shared
  evidence validator was unavailable because `../culturebotai-claw` is absent.
- The active aggregate and `mappings/ingredient_mappings.sssom.tsv` contain the
  same exact `MIM:4-azido-L-phenylalanine` to `CHEBI:228211` row.

## Evidence

- The CultureBotHT import, current ChEBI CAS xref, PubChem CAS lookup, formula,
  InChI, and SMILES all support the exact L-stereochemistry and azido
  substitution.
- The OAK/OLS row-review manifest confirmed this mapping and asked for no
  curation action.
- The SSSOM `other` field carries only `CAS:33173-53-4`; no rejected or broader
  synonym is exported for this record.
- Major: `nutritional_roles.AMINO_ACID_SOURCE` is only a
  `COMPUTATIONAL_PREDICTION` from ChEBI ancestry and explicitly says review is
  recommended. The live ChEBI term describes this exact molecule as a
  bioorthogonal click-chemistry reagent, not as evidence that it is supplied as
  a nutrient amino acid in media.
- The hidden/ignored-inclusive search over `data`, `mappings`, `reports`,
  `docs`, `scripts`, `conf`, `src`, `tests`, `.github`, and `.claude` found the
  active YAML, aggregate copy, SSSOM row, OAK/OLS confirmation row, generated
  docs, ChEBI-ancestry role inference surfaces, and ignored aggregate backups.

## Completeness

- CAS, formula, InChI, SMILES, and `ingredient_type` are populated.
- This CultureBotHT import has no recipe-count occurrence; no component,
  environment, or discussion entries need review.
- The amino-acid role should remain absent unless an inspected source supports
  this azido derivative as a medium nutrient rather than merely a phenylalanine
  derivative.

## Recommended Edits

Remove `nutritional_roles.AMINO_ACID_SOURCE`, or replace its evidence with a
specific source showing 4-azido-L-phenylalanine itself functions as an amino
acid source in the curated medium context. Then resync the aggregate and rebuild
docs.
