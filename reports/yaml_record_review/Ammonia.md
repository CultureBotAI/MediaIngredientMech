# `data/ingredients/mapped/Ammonia.yaml`

## Verdict

Pass. The exact `CHEBI:16134` ammonia identity, MicrobeDecoder occurrence,
ChEBI/PubChem chemistry, review-ingredients approval, SSSOM row, and aggregate
copy pass; the adjacent `NH4+` residual is correctly grounded to the separate
ammonium record.

## Identity

- Reviewed record: `data/ingredients/mapped/Ammonia.yaml`.
- Identifier and grounding: `identifier: CHEBI:16134` with
  `ontology_mapping.ontology_id: CHEBI:16134`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Local OAK and the official ChEBI page resolve `CHEBI:16134` to `ammonia` with
  formula `H3N`, CAS `7664-41-7`, SMILES `[H]N([H])[H]`, and InChIKey
  `QGZKDVFQNNGYKY-UHFFFAOYSA-N`.
- Local OAK resolves `NH4+` under `CHEBI:28938` ammonium, not this ammonia
  record, matching the nearby CultureMech residual grounding.
- `ingredient_type: SINGLE_INGREDIENT` is present.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Aminoacids.yaml data/ingredients/mapped/Aminoglycoside_Antibiotic.yaml data/ingredients/mapped/Aminophenazone.yaml data/ingredients/mapped/Aminovalerate.yaml data/ingredients/mapped/Ammonia.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Ammonia.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen runoak -i sqlite:obo:chebi aliases CHEBI:22507 CHEBI:160246 CHEBI:16134 CHEBI:28938`:
  returned canonical `ammonia`, exact `azane`, `NH3`, and separate
  `CHEBI:28938` ammonium aliases.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:22507 CHEBI:160246 CHEBI:16134`:
  returned formula, charge, SMILES, InChI, InChIKey, CAS, average mass, and
  monoisotopic mass for `CHEBI:16134`.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed; 2951
  records, 83 decompositions, 505 components, 0 violations.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- `data/custom/microbedecoder/unmapped_labels.tsv` contains
  `kgmicrobe.trait:ammonia` in BacDive metabolite production and utilization
  columns with count `22`, matching `source_occurrences`.
- `mappings/microbedecoder_auto_mapped_review.tsv` approved `Ammonia.yaml`
  after `CHEBI:16134` resolved locally with canonical label `ammonia`.
- `mappings/ingredient_mappings.sssom.tsv` row 397 maps `MIM:Ammonia` to
  `CHEBI:16134` with `skos:exactMatch` and the expected review-ingredients
  `APPROVED` trailer; row 398 separately maps `MIM:Ammonium` to `CHEBI:28938`.
- `mappings/culturemech_residual_groundings.tsv` grounds the `NH4+` residual to
  `CHEBI:28938` ammonium, keeping ammonia and ammonium separate.
- A hidden/ignored-inclusive search over `data`, `mappings`, `reports`, `src`,
  `tests`, `scripts`, `.claude`, `justfile`, and `CLAUDE.md` found the active
  YAML, aggregate copy, SSSOM row, MicrobeDecoder raw occurrence, review row,
  ammonium residual rows, and generated reports.

## Completeness

- Formula, SMILES, InChI, molecular weight, source occurrence, curation
  history, and `ingredient_type` are populated.
- No CAS, synonym, role, component, environmental context, discussion, or
  dataset entry is needed.
- `mappings/culturemech_recipe_membership.tsv` has no `CHEBI:16134` row, which
  is consistent with `occurrence_statistics.total_occurrences: 0` because the
  record is sourced from MicrobeDecoder rather than CultureMech.
- The aggregate copy in `data/curated/mapped_ingredients.yaml` matches the
  per-record YAML.

## Recommended Edits

- None.
