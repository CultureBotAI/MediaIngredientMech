# `data/ingredients/mapped/Amikacin.yaml`

## Verdict

Pass. The exact `CHEBI:2637` identity, high-count MicrobeDecoder occurrence,
ChEBI/PubChem chemistry, review-ingredients approval, SSSOM row, and aggregate
copy pass.

## Identity

- Reviewed record: `data/ingredients/mapped/Amikacin.yaml`.
- Identifier and grounding: `identifier: CHEBI:2637` with
  `ontology_mapping.ontology_id: CHEBI:2637`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Local OAK and the official ChEBI page resolve `CHEBI:2637` to `amikacin` with
  formula `C22H43N5O13`, CAS `37517-28-5`, SMILES
  `NCC[C@H](O)C(=O)N[C@@H]1C[C@H](N)[C@@H](O[C@H]2O[C@H](CN)[C@@H](O)[C@H](O)[C@H]2O)[C@H](O)[C@H]1O[C@H]1O[C@H](CO)[C@@H](O)[C@H](N)[C@H]1O`,
  and InChIKey `LKCWBDHBTVXHDL-RMDFUYIESA-N`.
- `ingredient_type: SINGLE_INGREDIENT` is present.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Aluminum_Chloride_Hydrate.yaml data/ingredients/mapped/Amicoumacin_B.yaml data/ingredients/mapped/Amikacin.yaml data/ingredients/mapped/Amikacin_Disulfate_Salt.yaml data/ingredients/mapped/Amino_Acid.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Amikacin.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen runoak -i sqlite:obo:chebi aliases CHEBI:216618 CHEBI:2637 CHEBI:2638 CHEBI:33709`:
  returned canonical `amikacin`, `Amikacin`, and other aliases for
  `CHEBI:2637`.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:216618 CHEBI:2637 CHEBI:2638 CHEBI:33709`:
  returned formula, charge, SMILES, InChI, InChIKey, CAS, average mass, and
  monoisotopic mass for `CHEBI:2637`.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed; 2951
  records, 83 decompositions, 505 components, 0 violations.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- `data/custom/microbedecoder/unmapped_labels.tsv` contains
  `kgmicrobe.trait:amikacin` in the BacDive antibiotic resistance and
  sensitivity columns with count `192`, matching `source_occurrences`.
- `mappings/microbedecoder_auto_mapped_review.tsv` approved `Amikacin.yaml`
  after `CHEBI:2637` resolved locally with canonical label `amikacin`.
- `mappings/ingredient_mappings.sssom.tsv` row 390 maps `MIM:Amikacin` to
  `CHEBI:2637` with `skos:exactMatch` and the expected review-ingredients
  `APPROVED` trailer.
- A hidden/ignored-inclusive search over `data`, `mappings`, `reports`, `src`,
  `tests`, `scripts`, `.claude`, `justfile`, and `CLAUDE.md` found the active
  YAML, aggregate copy, SSSOM row, MicrobeDecoder raw occurrence, review row,
  generated reports, and the separate amikacin-disulfate salt record.

## Completeness

- Formula, SMILES, InChI, molecular weight, source occurrence, curation
  history, and `ingredient_type` are populated.
- No CAS, synonym, role, component, environmental context, discussion, or
  dataset entry is needed.
- `mappings/culturemech_recipe_membership.tsv` has no `CHEBI:2637` row, which
  is consistent with `occurrence_statistics.total_occurrences: 0` because the
  record is sourced from MicrobeDecoder rather than CultureMech.
- The aggregate copy in `data/curated/mapped_ingredients.yaml` matches the
  per-record YAML.

## Recommended Edits

- None.
