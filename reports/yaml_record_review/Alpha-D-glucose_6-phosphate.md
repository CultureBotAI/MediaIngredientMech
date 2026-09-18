# `data/ingredients/mapped/Alpha-D-glucose_6-phosphate.yaml`

## Verdict

Pass. The exact `CHEBI:17665` identity, MicrobeDecoder occurrence, ChEBI/PubChem
chemistry, review-ingredients approval, SSSOM row, and aggregate copy pass.

## Identity

- Reviewed record: `data/ingredients/mapped/Alpha-D-glucose_6-phosphate.yaml`.
- Identifier and grounding: `identifier: CHEBI:17665` with
  `ontology_mapping.ontology_id: CHEBI:17665`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Local OAK and the official ChEBI page resolve `CHEBI:17665` to
  `alpha-D-glucose 6-phosphate` with formula `C6H13O9P`, SMILES
  `O=P(O)(O)OC[C@H]1O[C@H](O)[C@H](O)[C@@H](O)[C@@H]1O`, and InChIKey
  `NBSCHQHZLSJFNQ-DVKNGEFBSA-N`.
- `ingredient_type: SINGLE_INGREDIENT` is present.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Allura_Red_AC.yaml data/ingredients/mapped/Aloin.yaml data/ingredients/mapped/Alpha-D-glucose_6-phosphate.yaml data/ingredients/mapped/Alpha-L-rhamnose.yaml data/ingredients/mapped/Alpha-Lactose.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Alpha-D-glucose_6-phosphate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen runoak -i sqlite:obo:chebi aliases CHEBI:172687 CHEBI:73222 CHEBI:17665 CHEBI:27907 CHEBI:189432 CHEBI:36219`:
  returned canonical `alpha-D-glucose 6-phosphate` plus ChEBI aliases for
  `CHEBI:17665`.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:172687 CHEBI:73222 CHEBI:17665 CHEBI:27907 CHEBI:189432 CHEBI:36219`:
  returned formula, charge, SMILES, InChI, InChIKey, average mass, and
  monoisotopic mass for `CHEBI:17665`.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed; 2951
  records, 83 decompositions, 505 components, 0 violations.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- `data/custom/microbedecoder/unmapped_labels.tsv` contains
  `kgmicrobe.trait:alpha_d_glucose_6_phosphate` in
  `BacDive_Metabolite_utilization` with count `13`, matching
  `source_occurrences`.
- `mappings/microbedecoder_auto_mapped_review.tsv` approved
  `Alpha-D-glucose_6-phosphate.yaml` after `CHEBI:17665` resolved locally with
  canonical label `alpha-D-glucose 6-phosphate`.
- `mappings/ingredient_mappings.sssom.tsv` row 373 maps
  `MIM:Alpha-D-glucose_6-phosphate` to `CHEBI:17665` with `skos:exactMatch`
  and the expected review-ingredients `APPROVED` trailer.
- The ChEBI page and local ChEBI metadata support the stored formula, SMILES,
  InChI, and molecular weight.
- The hidden/ignored-inclusive search over `data`, `mappings`, `reports`,
  `src`, `tests`, `scripts`, `.claude`, `justfile`, and `CLAUDE.md` found the
  active YAML, aggregate copy, SSSOM row, MicrobeDecoder raw occurrence,
  generated indexes, and ignored aggregate backups.

## Completeness

- Formula, SMILES, InChI, source occurrence, curation history, and
  `ingredient_type` are populated.
- No CAS, role, component, environmental context, discussion, or dataset entry
  is needed.
- `mappings/culturemech_recipe_membership.tsv` has no `CHEBI:17665` row, which
  is consistent with `occurrence_statistics.total_occurrences: 0` because the
  record is sourced from MicrobeDecoder rather than CultureMech.
- The aggregate copy in `data/curated/mapped_ingredients.yaml` matches the
  per-record YAML.

## Recommended Edits

- None.
