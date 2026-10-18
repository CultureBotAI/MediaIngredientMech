# `data/ingredients/mapped/Aminophenazone.yaml`

## Verdict

Pass. The exact `CHEBI:160246` identity, MicrobeDecoder occurrence,
ChEBI/PubChem chemistry, review-ingredients approval, SSSOM row, and aggregate
copy pass.

## Identity

- Reviewed record: `data/ingredients/mapped/Aminophenazone.yaml`.
- Identifier and grounding: `identifier: CHEBI:160246` with
  `ontology_mapping.ontology_id: CHEBI:160246`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Local OAK and the official ChEBI page resolve `CHEBI:160246` to
  `aminophenazone` with formula `C13H17N3O`, CAS `58-15-1`, SMILES
  `Cc1c(N(C)C)c(=O)n(-c2ccccc2)n1C`, and InChIKey
  `RMMXTBMQSGEXHJ-UHFFFAOYSA-N`.
- `ingredient_type: SINGLE_INGREDIENT` is present.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Aminoacids.yaml data/ingredients/mapped/Aminoglycoside_Antibiotic.yaml data/ingredients/mapped/Aminophenazone.yaml data/ingredients/mapped/Aminovalerate.yaml data/ingredients/mapped/Ammonia.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Aminophenazone.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen runoak -i sqlite:obo:chebi aliases CHEBI:22507 CHEBI:160246 CHEBI:16134 CHEBI:28938`:
  returned canonical `aminophenazone`, exact structural name, and expected
  aminopyrine/dimethylaminoantipyrine aliases for `CHEBI:160246`.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:22507 CHEBI:160246 CHEBI:16134`:
  returned formula, charge, SMILES, InChI, InChIKey, CAS, average mass, and
  monoisotopic mass for `CHEBI:160246`.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed; 2951
  records, 83 decompositions, 505 components, 0 violations.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- `data/custom/microbedecoder/unmapped_labels.tsv` contains
  `kgmicrobe.trait:aminophenazone` in `BacDive_Metabolite_utilization` with
  count `1`, matching `source_occurrences`.
- `mappings/microbedecoder_auto_mapped_review.tsv` approved
  `Aminophenazone.yaml` after `CHEBI:160246` resolved locally with canonical
  label `aminophenazone`.
- `mappings/ingredient_mappings.sssom.tsv` row 395 maps
  `MIM:Aminophenazone` to `CHEBI:160246` with `skos:exactMatch` and the
  expected review-ingredients `APPROVED` trailer.
- The ChEBI page and local ChEBI metadata support the stored formula, SMILES,
  InChI, and molecular weight.
- A hidden/ignored-inclusive search over `data`, `mappings`, `reports`, `src`,
  `tests`, `scripts`, `.claude`, `justfile`, and `CLAUDE.md` found the active
  YAML, aggregate copy, SSSOM row, MicrobeDecoder raw occurrence, review row,
  and generated reports.

## Completeness

- Formula, SMILES, InChI, molecular weight, source occurrence, curation
  history, and `ingredient_type` are populated.
- No CAS, synonym, role, component, environmental context, discussion, or
  dataset entry is needed.
- `mappings/culturemech_recipe_membership.tsv` has no `CHEBI:160246` row,
  which is consistent with `occurrence_statistics.total_occurrences: 0`
  because the record is sourced from MicrobeDecoder rather than CultureMech.
- The aggregate copy in `data/curated/mapped_ingredients.yaml` matches the
  per-record YAML.

## Recommended Edits

- None.
