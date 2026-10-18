# `data/ingredients/mapped/Amphomycin.yaml`

## Verdict

Pass. The exact `CHEBI:201652` identity, MicrobeDecoder occurrence, review
approval, chemistry, SSSOM row, and aggregate copy agree.

## Identity

- Reviewed record: `data/ingredients/mapped/Amphomycin.yaml`.
- Identifier and grounding: `identifier: CHEBI:201652` with
  `ontology_mapping.ontology_id: CHEBI:201652`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Local OAK and the official ChEBI page resolve `CHEBI:201652` to
  `Amphomycin` with formula `C58H91N13O20`, the stored SMILES and InChI, and
  InChIKey `XBNDESPXQUOOBQ-UHFFFAOYSA-N`.
- `ingredient_type: SINGLE_INGREDIENT` is present.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Ammonium_Sulfamate.yaml data/ingredients/mapped/Ammonium_Sulfide_Solution.yaml data/ingredients/mapped/Ammonium_Sulfite_Monohydrate.yaml data/ingredients/mapped/Amoxicillin.yaml data/ingredients/mapped/Amphomycin.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Amphomycin.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen runoak -i sqlite:obo:chebi aliases CHEBI:81950 CHEBI:2676 CHEBI:201652`:
  returned canonical `Amphomycin` and exact structural aliases for
  `CHEBI:201652`.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:81950 CHEBI:2676 CHEBI:201652`:
  returned the formula, SMILES, InChI, InChIKey, average mass, and
  monoisotopic mass for `CHEBI:201652`.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed; 2951
  records, 83 decompositions, 505 components, 0 violations.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- `data/custom/microbedecoder/unmapped_labels.tsv` contains exactly the source
  row the active record cites: `kgmicrobe.trait:amphomycin` with count 1 from
  `BacDive_Metabolite_production`.
- `mappings/microbedecoder_auto_mapped_review.tsv` approved
  `Amphomycin.yaml` for promotion after confirming the local OAK ChEBI label.
- `mappings/ingredient_mappings.sssom.tsv` row 411 maps `MIM:Amphomycin` to
  `CHEBI:201652` with `skos:exactMatch` and the manual review-ingredients
  approval trailer.
- A hidden/ignored-inclusive search over active YAML records, the curated
  aggregate, SSSOM and row-review TSVs, MicrobeDecoder imports, and hydrate
  review files found the active record, aggregate copy, MicrobeDecoder review
  row, exact SSSOM row, and the raw source occurrence.

## Completeness

- MicrobeDecoder occurrence provenance, formula, SMILES, InChI, curation
  history, and `ingredient_type` are populated.
- `occurrence_statistics.total_occurrences: 0` is consistent with no
  CultureMech recipe memberships; the one non-CultureMech MicrobeDecoder source
  occurrence is stored separately.
- No synonym, component, role, environmental context, discussion, or dataset
  entry is needed.
- The aggregate copy in `data/curated/mapped_ingredients.yaml` matches the
  per-record YAML.

## Recommended Edits

None.
