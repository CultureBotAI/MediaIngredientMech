# `data/ingredients/mapped/Althiomycin.yaml`

## Verdict

Pass. The exact `CHEBI:157683` identity, MicrobeDecoder occurrence, Matamycin
merge, ChEBI/PubChem chemistry, review-ingredients approval, SSSOM row, and
aggregate copy pass.

## Identity

- Reviewed record: `data/ingredients/mapped/Althiomycin.yaml`.
- Identifier and grounding: `identifier: CHEBI:157683` with
  `ontology_mapping.ontology_id: CHEBI:157683`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Local OAK and the official ChEBI page resolve `CHEBI:157683` to
  `althiomycin` with formula `C16H17N5O6S2`, SMILES
  `COC1=CC(=O)N(C(=O)[C@H]2CSC(C(CO)NC(=O)c3csc(/C=N/O)n3)=N2)C1`,
  and InChIKey `VQQNQKXWJMRPHT-GMLCBOFYSA-N`.
- ChEBI lists `matamycin` as an alias of `althiomycin`; the local `Matamycin`
  source form is therefore appropriate as `RAW_TEXT`.
- `ingredient_type: SINGLE_INGREDIENT` is present.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Alpha-ketoglutaric_Acid.yaml data/ingredients/mapped/Alpha-toxicarol_Dl.yaml data/ingredients/mapped/Alphaalpha-Trehalose.yaml data/ingredients/mapped/Althiomycin.yaml data/ingredients/mapped/Aluminium_Sulfate.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Althiomycin.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen runoak -i sqlite:obo:chebi aliases CHEBI:30915 CHEBI:16551 CHEBI:157683 CHEBI:74772 CHEBI:9643`:
  returned canonical `althiomycin`, exact structural name, and related
  `matamycin`/`altiomycin` aliases for `CHEBI:157683`.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:30915 CHEBI:16551 CHEBI:157683 CHEBI:74772 CHEBI:9643`:
  returned formula, charge, SMILES, InChI, InChIKey, CAS, average mass, and
  monoisotopic mass for `CHEBI:157683`.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed; 2951
  records, 83 decompositions, 505 components, 0 violations.
- `uv run --frozen python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`:
  passed; all id/label pairs correspond, with the same 104 non-blocking
  plausibility warnings seen at corpus scope.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- `data/custom/microbedecoder/unmapped_labels.tsv` contains
  `kgmicrobe.trait:althiomycin` in `BacDive_Metabolite_production` with count
  `1`, matching `source_occurrences`.
- `mappings/microbedecoder_auto_mapped_review.tsv` approved
  `Althiomycin.yaml` after `CHEBI:157683` resolved locally with canonical label
  `althiomycin`.
- `mappings/ingredient_mappings.sssom.tsv` row 384 maps `MIM:Althiomycin` to
  `CHEBI:157683` with `skos:exactMatch`, the `manual:review-ingredients`
  approval trailer, and `Matamycin` as an exported source label.
- The `UNMAPPED_0826` merge note says `Matamycin` was absorbed because it is a
  synonym for althiomycin; local ChEBI confirms `matamycin` as a
  `CHEBI:157683` related synonym.
- A hidden/ignored-inclusive search over `data`, `mappings`, `reports`, `src`,
  `tests`, `scripts`, `.claude`, `justfile`, and `CLAUDE.md` found the active
  YAML, aggregate copy, SSSOM row, MicrobeDecoder raw occurrence, review row,
  generated indexes, and ignored aggregate backups.

## Completeness

- Formula, SMILES, InChI, molecular weight, source occurrence, curation
  history, Matamycin source label, and `ingredient_type` are populated.
- No CAS, role, component, environmental context, discussion, or dataset entry
  is needed.
- `mappings/culturemech_recipe_membership.tsv` has no `CHEBI:157683` row,
  which is consistent with `occurrence_statistics.total_occurrences: 0`
  because the record is sourced from MicrobeDecoder rather than CultureMech.
- The aggregate copy in `data/curated/mapped_ingredients.yaml` matches the
  per-record YAML.

## Recommended Edits

- None.
