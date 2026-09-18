# `data/ingredients/mapped/Aconitate.yaml`

## Verdict

Needs curation. The close grounding to ChEBI `aconitate(3-)` is internally
consistent, but the record still has stale unresolved-import prose, a stale
evidence note, and no ChEBI-backed structure block for a term that now has
exact trianion chemistry.

## Identity

- Reviewed record: `data/ingredients/mapped/Aconitate.yaml`.
- Identifier and grounding: `identifier: CHEBI:22210` with
  `ontology_mapping.ontology_id: CHEBI:22210`, source `CHEBI`,
  `mapping_quality: CLOSE_MATCH`, and `mapping_status: MAPPED`.
- Local OAK and the official ChEBI page resolve `CHEBI:22210` to
  `aconitate(3-)` with formula `C6H3O6`, SMILES
  `O=C([O-])C=C(CC(=O)[O-])C(=O)[O-]`, InChIKey
  `GTZCVFVGUGFEME-UHFFFAOYSA-K`, and no CAS.
- Local OAK does not list bare `Aconitate` as a synonym of `CHEBI:22210`, which
  supports `CLOSE_MATCH` instead of `SYNONYM_MATCH`.
- `ingredient_type: SINGLE_INGREDIENT` is present and agrees with the ChEBI
  trianion term.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Acetylated_Xylan.yaml data/ingredients/mapped/Acetylene.yaml data/ingredients/mapped/Achromoviromycin.yaml data/ingredients/mapped/Aconitate.yaml data/ingredients/mapped/Acridine_Orange.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Aconitate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen runoak -i sqlite:obo:chebi aliases CHEBI:134431 CHEBI:27518 CHEBI:22210 CHEBI:51739`:
  returned the expected ChEBI labels and synonyms for all four ChEBI terms in
  the batch.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:134431 CHEBI:27518 CHEBI:22210 CHEBI:51739`:
  returned the exact formula, SMILES, InChI, InChIKey, charge, average mass,
  and monoisotopic mass for `CHEBI:22210`.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed; 2951
  records, 83 decompositions, 505 components, 0 violations.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.
- `uv run --frozen python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`:
  passed; all id/label pairs correspond, with 104 non-blocking plausibility
  warnings elsewhere in the corpus.

## Evidence

- `data/custom/microbedecoder/unmapped_labels.tsv` contains
  `kgmicrobe.trait:aconitate` in `BacDive_Metabolite_utilization` with count
  `2`, matching `source_occurrences`.
- The OAK aliases show `aconitate(3-)` as the canonical ChEBI label and do not
  show bare `Aconitate` as an exact or related synonym.
- `mappings/ingredient_mappings.sssom.tsv` row 329 maps `MIM:Aconitate` to
  `CHEBI:22210` with the expected `PROMOTED` trailer.
- The top-level `notes` still say the MicrobeDecoder import had no CAS or
  CHEBI/NCIT match and needed curator review even though the same file now maps
  to `CHEBI:22210`.
- The `MIM curation (#213)` evidence note still says naive first-match
  enumeration would have picked a mono-anion; advisory research-validation rows
  under `mappings/record_research_validation.tsv` flagged that sentence as
  stale boilerplate because ChEBI did not expose an aconitate mono-anion term in
  the checked OLS searches.
- The hidden/ignored-inclusive search over `data`, `mappings`, `reports`,
  `src`, `tests`, `scripts`, and `history` found the active YAML, aggregate
  copy, SSSOM row, MicrobeDecoder raw occurrence, advisory
  `record_research_validation` rows, generated indexes, and ignored aggregate
  backups.

## Completeness

- The record is missing `chemical_properties` even though ChEBI has a complete
  trianion formula and structure for `CHEBI:22210`.
- No role, component, environmental context, discussion, or dataset entry is
  required.
- The aggregate copy in `data/curated/mapped_ingredients.yaml` matches the
  per-record YAML.

## Recommended Edits

- In `data/ingredients/mapped/Aconitate.yaml`, refresh the stale top-level
  `notes` to reflect the `CHEBI:22210` close mapping and remove or correct the
  stale mono-anion sentence in `ontology_mapping.evidence`.
- Add `chemical_properties` from `CHEBI:22210` without borrowing a CAS from
  aconitic acid.
- Regenerate synchronized products, then rerun
  `uv run --frozen python scripts/validate_strict.py`, `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Aconitate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`,
  `uv run --frozen python scripts/validate_component_partonomy.py`, and
  `uv run --frozen python scripts/validate_sssom_invariants.py`.
