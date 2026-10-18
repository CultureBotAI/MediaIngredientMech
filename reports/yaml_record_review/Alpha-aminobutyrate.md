# `data/ingredients/mapped/Alpha-aminobutyrate.yaml`

## Verdict

Pass. The exact `CHEBI:86508` identity, MicrobeDecoder occurrence,
ChEBI/PubChem chemistry, review-ingredients approval, SSSOM row, and aggregate
copy pass.

## Identity

- Reviewed record: `data/ingredients/mapped/Alpha-aminobutyrate.yaml`.
- Identifier and grounding: `identifier: CHEBI:86508` with
  `ontology_mapping.ontology_id: CHEBI:86508`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Local OAK and the official ChEBI page resolve `CHEBI:86508` to
  `alpha-aminobutyrate` with formula `C4H8NO2`, charge `-1`, SMILES
  `CCC(N)C(=O)[O-]`, and InChIKey `QWCKQJZIFLGMSD-UHFFFAOYSA-M`.
- `ingredient_type: SINGLE_INGREDIENT` is present.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Alpha-Tocopherol.yaml data/ingredients/mapped/Alpha-aminobutyrate.yaml data/ingredients/mapped/Alpha-bisabolol.yaml data/ingredients/mapped/Alpha-d-glucose.yaml data/ingredients/mapped/Alpha-hydroxyglutarate-gamma-lactone.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Alpha-aminobutyrate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen runoak -i sqlite:obo:chebi aliases CHEBI:18145 CHEBI:86508 CHEBI:125 CHEBI:17925`:
  returned canonical `alpha-aminobutyrate` and exact synonym `2-aminobutanoate`
  for `CHEBI:86508`.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:18145 CHEBI:86508 CHEBI:125 CHEBI:17925`:
  returned formula, charge, SMILES, InChI, InChIKey, average mass, and
  monoisotopic mass for `CHEBI:86508`.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed; 2951
  records, 83 decompositions, 505 components, 0 violations.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- `data/custom/microbedecoder/unmapped_labels.tsv` contains
  `kgmicrobe.compound:alpha_aminobutyrate` in `bergey:minor_end_products` with
  count `1`, matching `source_occurrences`.
- `mappings/microbedecoder_auto_mapped_review.tsv` approved
  `Alpha-aminobutyrate.yaml` after `CHEBI:86508` resolved locally with
  canonical label `alpha-aminobutyrate`.
- `mappings/ingredient_mappings.sssom.tsv` row 377 maps
  `MIM:Alpha-aminobutyrate` to `CHEBI:86508` with `skos:exactMatch` and the
  expected review-ingredients `APPROVED` trailer.
- The ChEBI page and local ChEBI metadata support the stored formula, SMILES,
  InChI, and molecular weight.
- A hidden/ignored-inclusive search over `data`, `mappings`, `reports`, `src`,
  `tests`, `scripts`, `.claude`, `justfile`, and `CLAUDE.md` found the active
  YAML, aggregate copy, SSSOM row, MicrobeDecoder raw occurrence, generated
  indexes, and ignored aggregate backups.

## Completeness

- Formula, SMILES, InChI, source occurrence, curation history, and
  `ingredient_type` are populated.
- No CAS, role, component, environmental context, discussion, or dataset entry
  is needed.
- `mappings/culturemech_recipe_membership.tsv` has no `CHEBI:86508` row, which
  is consistent with `occurrence_statistics.total_occurrences: 0` because the
  record is sourced from MicrobeDecoder rather than CultureMech.
- The aggregate copy in `data/curated/mapped_ingredients.yaml` matches the
  per-record YAML.

## Recommended Edits

- None.
