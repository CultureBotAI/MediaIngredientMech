# `data/ingredients/mapped/Acetate.yaml`

## Verdict

Needs curation, with major role and surface-form issues. The exact
`CHEBI:30089` acetate identity, CAS, formula, chemistry, and duplicate merge
pass, but the record still has duplicate/provisional nutritional roles and the
SSSOM `other` column exports contextual catabolization labels as if they were
ingredient surfaces.

## Identity

- Reviewed record: `data/ingredients/mapped/Acetate.yaml`.
- Identifier and grounding: `identifier: CHEBI:30089` with
  `ontology_mapping.ontology_id: CHEBI:30089`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- The official ChEBI page resolves `CHEBI:30089` to `acetate` with formula
  `C2H3O2` and InChIKey `QTBSBXVTEAMEQO-UHFFFAOYSA-M`.
- Local OAK carries the same formula, SMILES, InChI, exact identity, and CAS
  `71-50-1`; PubChem maps CAS `71-50-1` to acetate CID `175` with the same
  InChIKey.
- The rejected `Acetate_Carbon_Source` tombstone was merged into this active
  record, and the active record now owns the `Acetate (carbon source)` raw
  surface.
- `ingredient_type: SINGLE_INGREDIENT` is present.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Acetamide.yaml data/ingredients/mapped/Acetate.yaml data/ingredients/mapped/Acetate_Carbon_Source.yaml data/ingredients/mapped/Acetic_Acid.yaml data/ingredients/mapped/Acetoacetate.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Acetate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen runoak -i sqlite:obo:chebi aliases CHEBI:27856 CHEBI:30089 CHEBI:15366 CHEBI:13705`:
  returned the expected ChEBI labels and synonyms for all four target ChEBI
  identifiers.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:27856 CHEBI:30089 CHEBI:15366 CHEBI:13705`:
  returned formula and structure metadata for all four target ChEBI identifiers.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed; 2951
  records, 83 decompositions, 505 components, 0 violations.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- The CultureMech direct match, CAS `71-50-1`, official ChEBI record, local
  OAK metadata, and PubChem CID all support the exact acetate identity.
- The resolved CAS conflict correctly kept the OAK canonical xref `71-50-1`
  and dropped `758-12-3`.
- The active record absorbed the duplicate `CHEBI:30089`
  `Acetate (carbon source)` tombstone in August 2026.
- The SSSOM row maps `MIM:Acetate` to `CHEBI:30089` with `skos:exactMatch`,
  but also exports `Acetate (carbon source)`,
  `aerobic catabolization: acetate`, and
  `anaerobic catabolization: acetate` in `other`. Those strings are source or
  role-bearing phrases, not exact names for the acetate anion.
- One `CARBON_SOURCE` role is supported by the imported CultureMech role text,
  but the record also has a second provisional `CARBON_SOURCE` assertion from
  a name-pattern rule and a provisional `ENERGY_SOURCE` assertion.
- The hidden/ignored-inclusive search over `data`, `mappings`, `src`, `tests`,
  `scripts`, and `reports/yaml_record_review_batch` found the active YAML,
  rejected tombstone, aggregate copies, SSSOM row, synonym-enrich review rows,
  row-review manifest rows, and ignored aggregate backups.

## Completeness

- CAS, formula, InChI, SMILES, ChEBI grounding, `ingredient_type`, occurrence
  counts, and the duplicate tombstone merge are populated.
- The SSSOM `other` surfaces and nutritional role list need review before this
  record is complete: the contextual catabolization phrases should stay
  traceable without being exported as ingredient-like surfaces, and the
  provisional/duplicate role assertions need either evidence or removal.

## Recommended Edits

- In `data/ingredients/mapped/Acetate.yaml`, replace or remove the provisional
  `ENERGY_SOURCE` role and the duplicate provisional `CARBON_SOURCE` role after
  inspecting evidence that specifically supports those assertions for acetate.
- Move `aerobic catabolization: acetate` and
  `anaerobic catabolization: acetate` out of SSSOM-exported synonym surfaces
  while preserving their source traceability in the maintained record input.
- Rebuild `mappings/ingredient_mappings.sssom.tsv` from the maintained YAML and
  re-run `scripts/validate_strict.py` plus
  `scripts/validate_sssom_invariants.py`.
