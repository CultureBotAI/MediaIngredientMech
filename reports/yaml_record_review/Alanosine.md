# `data/ingredients/mapped/Alanosine.yaml`

## Verdict

Needs curation. The exact `CHEBI:221124` L-alanosine identity and structure
pass, but the record still stores `produces: alanosine` as a raw synonym and
exports it through SSSOM `other` even though it is a predicate-bearing KG edge
surface, not a name for the chemical.

## Identity

- Reviewed record: `data/ingredients/mapped/Alanosine.yaml`.
- Identifier and grounding: `identifier: CHEBI:221124` with
  `ontology_mapping.ontology_id: CHEBI:221124`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Local OAK and the official ChEBI page resolve `CHEBI:221124` to
  `L-alanosine` with formula `C3H7N3O4`, SMILES
  `N[C@@H](C[N+]([O-])=NO)C(=O)O`, and InChIKey
  `ZGNLFUXWZJGETL-REOHCLBHSA-N`.
- Local OAK lists
  `[(2S)-2-amino-2-carboxyethyl]-hydroxyimino-oxidoazanium` as an exact ChEBI
  synonym, matching the retained `EXACT_SYNONYM`.
- `ingredient_type: SINGLE_INGREDIENT` is present.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Agave.yaml data/ingredients/mapped/Air-dried_Garden_Soil.yaml data/ingredients/mapped/Air.yaml data/ingredients/mapped/Al2_So43_X_18_H2o.yaml data/ingredients/mapped/Alanosine.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Alanosine.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen runoak -i sqlite:obo:chebi aliases CHEBI:74779 CHEBI:221124`:
  returned canonical `L-alanosine` plus the expected exact ChEBI synonym.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:74779 CHEBI:221124`:
  returned formula, charge, SMILES, InChI, InChIKey, average mass, and
  monoisotopic mass for `CHEBI:221124`.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed; 2951
  records, 83 decompositions, 505 components, 0 violations.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- The ChEBI label, exact synonym, and structure metadata support the current
  L-alanosine identity.
- `mappings/ingredient_mappings.sssom.tsv` row 360 maps `MIM:Alanosine` to
  `CHEBI:221124` with `skos:exactMatch` and still exports
  `produces: alanosine` in `other`.
- The `produces: alanosine` surface was intentionally restored from published
  SSSOM by `claude_sssom_surface_form_backfill`, but the string encodes a
  kg-microbe predicate and object rather than a synonym of alanosine.
- The hidden/ignored-inclusive search over `data`, `mappings`, `reports`,
  `src`, `tests`, `scripts`, `.claude`, `justfile`, and `CLAUDE.md` found the
  active YAML, aggregate copy, SSSOM row, synonym-enrichment review row,
  generated indexes, and ignored aggregate backups.

## Completeness

- Formula, SMILES, InChI, exact synonym, curation history, and
  `ingredient_type` are populated.
- No role, component, environmental context, discussion, occurrence, or dataset
  entry is needed.
- The aggregate copy in `data/curated/mapped_ingredients.yaml` matches the
  per-record YAML.

## Recommended Edits

- Remove `produces: alanosine` from
  `data/ingredients/mapped/Alanosine.yaml` synonyms or move it to a provenance
  surface that does not publish predicate text as a synonym.
- Regenerate synchronized products, then rerun
  `uv run --frozen python scripts/validate_strict.py`, `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Alanosine.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`,
  `uv run --frozen python scripts/validate_component_partonomy.py`, and
  `uv run --frozen python scripts/validate_sssom_invariants.py`.
