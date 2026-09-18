# `data/ingredients/mapped/Acetylated_Xylan.yaml`

## Verdict

Needs curation. The `CHEBI:134431` grounding is a supported synonym-level match
to ChEBI `acetyl xylan`, but the record still carries an unsupported
computational `CARBON_SOURCE` role.

## Identity

- Reviewed record: `data/ingredients/mapped/Acetylated_Xylan.yaml`.
- Identifier and grounding: `identifier: CHEBI:134431` with
  `ontology_mapping.ontology_id: CHEBI:134431`, source `CHEBI`,
  `mapping_quality: SYNONYM_MATCH`, and `mapping_status: MAPPED`.
- Local OAK and the official ChEBI page resolve `CHEBI:134431` to
  `acetyl xylan`.
- Local OAK lists `acetylated xylan` as a ChEBI related synonym, supporting the
  existing demotion from `EXACT_MATCH` to `SYNONYM_MATCH` and the retained
  `skos:exactMatch` identity row.
- The ChEBI term has a textual class definition for an acetylated xylan
  derivative, but no formula, SMILES, InChI, charge, or mass in OAK or on the
  official ChEBI page; leaving `chemical_properties` empty is therefore
  appropriate.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Acetylated_Xylan.yaml data/ingredients/mapped/Acetylene.yaml data/ingredients/mapped/Achromoviromycin.yaml data/ingredients/mapped/Aconitate.yaml data/ingredients/mapped/Acridine_Orange.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Acetylated_Xylan.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen runoak -i sqlite:obo:chebi aliases CHEBI:134431 CHEBI:27518 CHEBI:22210 CHEBI:51739`:
  returned the expected ChEBI labels and synonyms for all four ChEBI terms in
  the batch.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:134431 CHEBI:27518 CHEBI:22210 CHEBI:51739`:
  returned ChEBI metadata for all four terms; `CHEBI:134431` has no structural
  fields.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed; 2951
  records, 83 decompositions, 505 components, 0 violations.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.
- `uv run --frozen python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`:
  passed; all id/label pairs correspond, with 104 non-blocking plausibility
  warnings elsewhere in the corpus.

## Evidence

- The `local kg-microbe CHEBI transform` and `MIM curation (#322)` mapping
  evidence matches the current ChEBI term: the record label is not the ChEBI
  primary label, but it is an OAK alias on the same term.
- `mappings/unmapped_ingredients_ols_exact_audit.tsv` also records
  `CHEBI:134431` as the exact-synonym candidate that promoted the former
  unmapped record.
- `mappings/ingredient_mappings.sssom.tsv` row 326 maps
  `MIM:Acetylated_Xylan` to `CHEBI:134431` with the expected OAK/OLS-confirmed
  trailer.
- The hidden/ignored-inclusive search over `data`, `mappings`, `reports`,
  `src`, `tests`, `scripts`, and `history` found the active YAML, aggregate
  copy, SSSOM row, exact-audit lead, generated indexes, ignored aggregate
  backups, and stale advisory batch rows.
- The `nutritional_roles.CARBON_SOURCE` row is only a name-pattern prediction;
  no inspected source supports acetylated xylan as a carbon source in a defined
  growth-medium context.

## Completeness

- `chemical_properties` is correctly empty for the ChEBI class term because no
  exact formula or structure is available for arbitrary acetyl xylan.
- No component, environment, dataset, or discussion entry is required for the
  current identity.
- The aggregate copy in `data/curated/mapped_ingredients.yaml` matches the
  per-record YAML.

## Recommended Edits

- In `data/ingredients/mapped/Acetylated_Xylan.yaml`, remove or evidence the
  provisional `nutritional_roles.CARBON_SOURCE` assertion, then run
  `uv run --frozen python scripts/validate_strict.py`, `uv run --frozen python scripts/validate_component_partonomy.py`,
  and `uv run --frozen python scripts/validate_sssom_invariants.py`.
