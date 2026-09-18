# `data/ingredients/mapped/Actein.yaml`

## Verdict

Pass with minor issues. The exact `CHEBI:70241` identity, CAS-backed import,
ChEBI chemistry, SSSOM row, and aggregate copy pass; one historical
auto-backfill change string has truncated structure text.

## Identity

- Reviewed record: `data/ingredients/mapped/Actein.yaml`.
- Identifier and grounding: `identifier: CHEBI:70241` with
  `ontology_mapping.ontology_id: CHEBI:70241`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Local OAK and the official ChEBI page resolve `CHEBI:70241` to `Actein` with
  formula `C37H56O11`, SMILES, InChI, and InChIKey
  `NEWMWGLPJQHSSQ-PSDKAYTQSA-N`.
- `ingredient_type: SINGLE_INGREDIENT` is present and agrees with the ChEBI
  molecular entity.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Acriflavine.yaml data/ingredients/mapped/Actein.yaml data/ingredients/mapped/Actinohivin.yaml data/ingredients/mapped/Actinomycetin.yaml data/ingredients/mapped/Actinomycin_A.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Actein.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen runoak -i sqlite:obo:chebi aliases CHEBI:70241 CHEBI:15369`:
  returned the expected ChEBI labels for Actein and the broader actinomycin
  term.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:70241 CHEBI:15369`:
  returned formula and structure metadata for `CHEBI:70241`.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed; 2951
  records, 83 decompositions, 505 components, 0 violations.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- The CultureBotHT CAS import and official ChEBI record support the exact
  Actein identity.
- The official ChEBI page and local OAK metadata support the stored formula,
  SMILES, and InChI.
- `mappings/ingredient_mappings_oak_ols_review.tsv` confirms `CHEBI:70241`;
  `mappings/ingredient_mappings.sssom.tsv` row 334 maps `MIM:Actein` to
  `CHEBI:70241` with `skos:exactMatch` and exports `CAS:18642-44-9`.
- The hidden/ignored-inclusive search over `data`, `mappings`, `reports`,
  `src`, `tests`, `scripts`, and `history` found the active YAML, aggregate
  copy, SSSOM row, OAK/OLS confirmation row, generated indexes, and ignored
  aggregate backups.
- The only defect is historical: the 2026-05-01
  `AUTO_BACKFILL_CHEBI_CHEMISTRY` change string cuts off the InChI and SMILES,
  while the active `chemical_properties` block stores the full ChEBI values.

## Completeness

- CAS, formula, SMILES, InChI, curation history, and `ingredient_type` are
  populated.
- No role, component, environmental context, discussion, or dataset entry is
  needed.
- The aggregate copy in `data/curated/mapped_ingredients.yaml` matches the
  per-record YAML.

## Recommended Edits

- Optionally annotate the stale 2026-05-01 history `changes` prose in
  `data/ingredients/mapped/Actein.yaml`; the active `chemical_properties` fields
  are already correct.
