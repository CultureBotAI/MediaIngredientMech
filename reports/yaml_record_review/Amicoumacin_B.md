# `data/ingredients/mapped/Amicoumacin_B.yaml`

## Verdict

Pass. The exact `CHEBI:216618` identity, MicrobeDecoder occurrence,
ChEBI/PubChem chemistry, review-ingredients approval, SSSOM row, and aggregate
copy pass.

## Identity

- Reviewed record: `data/ingredients/mapped/Amicoumacin_B.yaml`.
- Identifier and grounding: `identifier: CHEBI:216618` with
  `ontology_mapping.ontology_id: CHEBI:216618`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Local OAK and the official ChEBI page resolve `CHEBI:216618` to
  `Amicoumacin B` with formula `C20H30N2O9`, SMILES
  `CC(C)C[C@H](NC(=O)[C@@H](O)C(O)C(N)CC(=O)O)C(O)Cc1cccc(O)c1C(=O)O`,
  and InChIKey `ZVMJOYORHWNPCZ-MLXNOORUSA-N`.
- `ingredient_type: SINGLE_INGREDIENT` is present.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Aluminum_Chloride_Hydrate.yaml data/ingredients/mapped/Amicoumacin_B.yaml data/ingredients/mapped/Amikacin.yaml data/ingredients/mapped/Amikacin_Disulfate_Salt.yaml data/ingredients/mapped/Amino_Acid.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Amicoumacin_B.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen runoak -i sqlite:obo:chebi aliases CHEBI:216618 CHEBI:2637 CHEBI:2638 CHEBI:33709`:
  returned canonical `Amicoumacin B` and its structural-name alias for
  `CHEBI:216618`.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:216618 CHEBI:2637 CHEBI:2638 CHEBI:33709`:
  returned formula, charge, SMILES, InChI, InChIKey, average mass, and
  monoisotopic mass for `CHEBI:216618`.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed; 2951
  records, 83 decompositions, 505 components, 0 violations.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- `data/custom/microbedecoder/unmapped_labels.tsv` contains
  `kgmicrobe.trait:amicoumacin_b` in `BacDive_Metabolite_production` with
  count `1`, matching `source_occurrences`.
- `mappings/microbedecoder_auto_mapped_review.tsv` approved
  `Amicoumacin_B.yaml` after `CHEBI:216618` resolved locally with canonical
  label `Amicoumacin B`.
- `mappings/ingredient_mappings.sssom.tsv` row 389 maps
  `MIM:Amicoumacin_B` to `CHEBI:216618` with `skos:exactMatch` and the
  expected review-ingredients `APPROVED` trailer.
- A hidden/ignored-inclusive search over `data`, `mappings`, `reports`, `src`,
  `tests`, `scripts`, `.claude`, `justfile`, and `CLAUDE.md` found the active
  YAML, aggregate copy, SSSOM row, MicrobeDecoder raw occurrence, review row,
  and generated reports.

## Completeness

- Formula, SMILES, InChI, molecular weight, source occurrence, curation
  history, and `ingredient_type` are populated.
- No CAS, synonym, role, component, environmental context, discussion, or
  dataset entry is needed.
- `mappings/culturemech_recipe_membership.tsv` has no `CHEBI:216618` row,
  which is consistent with `occurrence_statistics.total_occurrences: 0`
  because the record is sourced from MicrobeDecoder rather than CultureMech.
- The aggregate copy in `data/curated/mapped_ingredients.yaml` matches the
  per-record YAML.

## Recommended Edits

- None.
