# `data/ingredients/mapped/Antimonate.yaml`

## Verdict

Needs curation. The promoted ChEBI grounding is sound: `Antimonate` is an exact
synonym of `CHEBI:30295` `antimonate(3-)`, and the formula, structure, SSSOM
row, MicrobeDecoder source occurrence, and aggregate copy are synchronized. The
only active defect is stale top-level text still saying the old unmapped import
needs curator review.

## Identity

- Reviewed record: `data/ingredients/mapped/Antimonate.yaml`.
- Identifier and grounding: `identifier: CHEBI:30295` with
  `ontology_mapping.ontology_id: CHEBI:30295`, `ontology_source: CHEBI`,
  `mapping_quality: SYNONYM_MATCH`, and `mapping_status: MAPPED`.
- Local OAK and EBI OLS resolve `CHEBI:30295` to non-obsolete ChEBI
  `antimonate(3-)`, charge -3, formula `O4Sb`, exact synonym `antimonate`,
  SMILES `[O]=[Sb]([O-])([O-])[O-]`, and the stored InChI.
- `ingredient_type: SINGLE_INGREDIENT` is present and fits the ChEBI anion.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Antimonate.yaml data/ingredients/mapped/Antimycin_A.yaml data/ingredients/mapped/Antimycin_A3.yaml data/ingredients/mapped/Antipyrine.yaml data/ingredients/mapped/Aphidicolin.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Antimonate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:30295 CHEBI:2762 CHEBI:197950 CHEBI:31225 CHEBI:2766`:
  returned charge, formula, SMILES, InChI, and mass metadata for `CHEBI:30295`.
- `uv run --frozen runoak -i sqlite:obo:chebi aliases CHEBI:30295 CHEBI:2762 CHEBI:197950 CHEBI:31225 CHEBI:2766`:
  returned `antimonate` as an exact ChEBI synonym of `CHEBI:30295`.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed; 2951
  records, 83 decompositions, 505 components, 0 violations.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- `data/custom/microbedecoder/unmapped_labels.tsv` contains
  `kgmicrobe.trait:antimonate` with raw label `antimonate`, source column
  `BacDive_Metabolite_utilization`, and count 1, matching the record
  `source_occurrences` entry.
- `mappings/microbedecoder_residual_grounded.tsv` records the residual repair
  that promoted `UNMAPPED_0797` / `Antimonate` to `CHEBI:30295` by a
  `SYNONYM_MATCH` through exact ChEBI synonym `Antimonate`.
- `mappings/ingredient_mappings.sssom.tsv` row 437 maps `MIM:Antimonate` to
  `CHEBI:30295` with `skos:exactMatch` and the
  `manual:promote_resolved_unmapped|PROMOTED|2026-08-04` trailer.
- A hidden, ignored-inclusive search across `data`, `src`, `tests`,
  `mappings`, `scripts`, and non-review `reports` found the active YAML,
  aggregate copy, raw ignored MicrobeDecoder row, residual grounding row, and
  SSSOM row. The search also found `Sodium_Antimonate`, a non-target salt
  sibling that is curated separately.

## Completeness

- Formula, SMILES, InChI, ChEBI identity, non-media source occurrence, curation
  history, `ingredient_type`, SSSOM, and the aggregate copy are populated.
- No component, role, environmental context, discussion, or dataset entry is
  needed.
- `notes` still says the MicrobeDecoder import had no CAS/CHEBI/NCIT match and
  needed curator review, even though the record has since been promoted.

## Recommended Edits

- In `data/ingredients/mapped/Antimonate.yaml`, remove or replace the stale
  top-level `notes` text with the supported `CHEBI:30295` synonym-match
  decision.
- Regenerate synchronized products, then rerun
  `uv run --frozen python scripts/validate_strict.py`,
  `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Antimonate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`,
  and `uv run --frozen python scripts/validate_sssom_invariants.py`.
