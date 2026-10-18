# `data/ingredients/mapped/Amygdalin.yaml`

## Verdict

Pass. The exact `CHEBI:27613` identity, MicrobeDecoder occurrence, review
approval, chemistry, SSSOM row, aggregate copy, and deliberate separation from
the narrower `(R)-amygdalin` sibling agree.

## Identity

- Reviewed record: `data/ingredients/mapped/Amygdalin.yaml`.
- Identifier and grounding: `identifier: CHEBI:27613` with
  `ontology_mapping.ontology_id: CHEBI:27613`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Local OAK and the official ChEBI page resolve `CHEBI:27613` to `amygdalin`
  with formula `C20H27NO11`, the stored SMILES and InChI, and InChIKey
  `XUCIJNAGGSZNQT-SWRVSKMJSA-N`.
- `ingredient_type: SINGLE_INGREDIENT` is present.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Amphotericin_A.yaml data/ingredients/mapped/Amphotericin_B.yaml data/ingredients/mapped/Ampicillin.yaml data/ingredients/mapped/Ampicillin_Sodium_Salt.yaml data/ingredients/mapped/Amygdalin.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Amygdalin.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen runoak -i sqlite:obo:chebi aliases CHEBI:2682 CHEBI:28971 CHEBI:34535 CHEBI:27613`:
  returned canonical `amygdalin` and exact/related structural aliases for
  `CHEBI:27613`.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:2682 CHEBI:28971 CHEBI:34535 CHEBI:27613`:
  returned the formula, SMILES, InChI, InChIKey, average mass, and
  monoisotopic mass for `CHEBI:27613`.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed; 2951
  records, 83 decompositions, 505 components, 0 violations.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- `data/custom/microbedecoder/unmapped_labels.tsv` contains exactly the source
  row the active record cites: `kgmicrobe.trait:amygdalin` with count 720 from
  `BacDive_Metabolite_utilization`.
- `mappings/microbedecoder_auto_mapped_review.tsv` approved `Amygdalin.yaml`
  for promotion after confirming the local OAK ChEBI label.
- `mappings/ingredient_mappings.sssom.tsv` row 415 maps `MIM:Amygdalin` to
  `CHEBI:27613` with `skos:exactMatch` and the manual review-ingredients
  approval trailer.
- A hidden/ignored-inclusive search over active YAML records, the curated
  aggregate, SSSOM and row-review TSVs, MicrobeDecoder imports, and existing
  record-review reports found the active parent Amygdalin record, the separate
  `(R)-amygdalin` sibling, the raw MicrobeDecoder source occurrence, and no
  evidence that the parent should be silently collapsed onto `(R)-amygdalin`.

## Completeness

- MicrobeDecoder occurrence provenance, formula, SMILES, InChI, curation
  history, and `ingredient_type` are populated.
- `occurrence_statistics.total_occurrences: 0` is consistent with no
  CultureMech recipe memberships; the 720 non-CultureMech MicrobeDecoder source
  occurrences are stored separately.
- No synonym, component, role, environmental context, discussion, or dataset
  entry is needed.
- The aggregate copy in `data/curated/mapped_ingredients.yaml` matches the
  per-record YAML.

## Recommended Edits

None.
