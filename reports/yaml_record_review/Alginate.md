# `data/ingredients/mapped/Alginate.yaml`

## Verdict

Pass with minor issues. The exact `CHEBI:58187` alginate identity,
MicrobeDecoder source occurrence, ChEBI/PubChem chemistry, review-ingredients
approval, SSSOM row, and aggregate copy pass; one adjacent
`alginate (brown algae)` CultureMech residual remains triaged outside this
record and should be accepted or rejected separately.

## Identity

- Reviewed record: `data/ingredients/mapped/Alginate.yaml`.
- Identifier and grounding: `identifier: CHEBI:58187` with
  `ontology_mapping.ontology_id: CHEBI:58187`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Local OAK and the official ChEBI page resolve `CHEBI:58187` to `alginate`
  with formula `(C6H7O6)n.H2O`, charge `-1`, SMILES
  `[H]O[C@@H]1C(C(=O)[O-])O[C@@H](O)[C@@H](O)[C@H]1O`, and InChIKey
  `AEMOLEFTQBMNLQ-QTWKXLRFSA-M`.
- `ingredient_type: SINGLE_INGREDIENT` is present and appropriate for the
  ChEBI alginate anion/polymer entry.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Alginate.yaml data/ingredients/mapped/Alk_So42.yaml data/ingredients/mapped/Alk_So42_X_12_H2o.yaml data/ingredients/mapped/Allantoin.yaml data/ingredients/mapped/Allopurinol.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Alginate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen runoak -i sqlite:obo:chebi aliases CHEBI:58187 CHEBI:86463 CHEBI:86465 CHEBI:15676 CHEBI:40279`:
  returned canonical `alginate` plus ChEBI aliases for `CHEBI:58187`.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:58187 CHEBI:86463 CHEBI:86465 CHEBI:15676 CHEBI:40279`:
  returned formula, charge, SMILES, InChI, InChIKey, average mass, and
  monoisotopic mass for `CHEBI:58187`.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed; 2951
  records, 83 decompositions, 505 components, 0 violations.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.
- `uv run --frozen python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`:
  passed; all id/label pairs correspond, with 104 non-blocking plausibility
  warnings.

## Evidence

- `data/custom/microbedecoder/unmapped_labels.tsv` contains
  `kgmicrobe.trait:alginate` in `BacDive_Metabolite_utilization` with count
  `52`, matching `source_occurrences`.
- `mappings/microbedecoder_auto_mapped_review.tsv` approved `Alginate.yaml`
  after `CHEBI:58187` resolved locally with canonical label `alginate`.
- `mappings/ingredient_mappings.sssom.tsv` row 366 maps `MIM:Alginate` to
  `CHEBI:58187` with `skos:exactMatch` and the expected review-ingredients
  `APPROVED` trailer.
- The ChEBI page and local ChEBI metadata support the stored formula, SMILES,
  InChI, InChIKey, and molecular weight.
- A hidden/ignored-inclusive search over `data`, `mappings`, `reports`, `src`,
  `tests`, `scripts`, `.claude`, `justfile`, and `CLAUDE.md` found the active
  YAML, aggregate copy, SSSOM row, MicrobeDecoder raw occurrence, generated
  indexes, ignored aggregate backups, and a single `alginate (brown algae)`
  CultureMech residual that remains outside this record.

## Completeness

- Formula, SMILES, InChI, source occurrence, curation history, and
  `ingredient_type` are populated.
- No CAS, role, component, environmental context, discussion, or dataset entry
  is needed for the MicrobeDecoder alginate record itself.
- `mappings/culturemech_recipe_membership.tsv` has no `CHEBI:58187` row, which
  is consistent with `occurrence_statistics.total_occurrences: 0` because the
  record is sourced from MicrobeDecoder rather than CultureMech.
- The aggregate copy in `data/curated/mapped_ingredients.yaml` matches the
  per-record YAML.

## Recommended Edits

- Review the one `alginate (brown algae)` CultureMech residual in
  `mappings/culturemech_residual_triage.tsv`; either map it to the existing
  alginate record when the source text denotes alginate from brown algae, or
  leave it rejected with an explicit rationale if the parenthetical denotes a
  source material that should not be folded into `CHEBI:58187`.
