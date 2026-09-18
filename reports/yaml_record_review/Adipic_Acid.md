# `data/ingredients/mapped/Adipic_Acid.yaml`

## Verdict

Pass with minor issues. The exact `CHEBI:30832` identity, CAS xref, exact
`hexanedioic acid` synonym, ChEBI structure block, SSSOM row, and aggregate copy
pass; only one historical auto-backfill event has a truncated InChI string in
its change prose.

## Identity

- Reviewed record: `data/ingredients/mapped/Adipic_Acid.yaml`.
- Identifier and grounding: `identifier: CHEBI:30832` with
  `ontology_mapping.ontology_id: CHEBI:30832`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Local OAK and the official ChEBI page resolve `CHEBI:30832` to `adipic acid`
  with formula `C6H10O4`, CAS `124-04-9`, SMILES `O=C(O)CCCCC(=O)O`, and
  InChIKey `WNLRTRBMVRJNCN-UHFFFAOYSA-N`.
- Local OAK lists `hexanedioic acid` as an exact ChEBI synonym, matching the
  retained `EXACT_SYNONYM`.
- `ingredient_type: SINGLE_INGREDIENT` is present.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Adipate.yaml data/ingredients/mapped/Adipic_Acid.yaml data/ingredients/mapped/Aesculetin.yaml data/ingredients/mapped/Agar.yaml data/ingredients/mapped/Agarose.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Adipic_Acid.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen runoak -i sqlite:obo:chebi aliases CHEBI:17128 CHEBI:30832 CHEBI:2509 CHEBI:2511 CHEBI:490095`:
  returned the expected labels and aliases for all ChEBI terms checked in this
  batch, including canonical `adipic acid` and exact `hexanedioic acid`.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:17128 CHEBI:30832 CHEBI:2509 CHEBI:2511 CHEBI:490095`:
  returned the exact formula, SMILES, InChI, InChIKey, charge, average mass,
  and monoisotopic mass for `CHEBI:30832`.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed; 2951
  records, 83 decompositions, 505 components, 0 violations.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- ChEBI supports the exact primary identity, exact `hexanedioic acid` synonym,
  CAS `124-04-9`, and stored formula/structure fields.
- `mappings/ingredient_mappings.sssom.tsv` row 351 maps
  `MIM:Adipic_Acid` to `CHEBI:30832` with `skos:exactMatch` and exports
  `hexanedioic acid|CAS:124-04-9` in `other`.
- The historical `2026-05-01T08:08:27.895526+00:00`
  `AUTO_BACKFILL_CHEBI_CHEMISTRY` event truncates the InChI in its `changes`
  text, but the current `chemical_properties.inchi` is complete.
- The hidden/ignored-inclusive search over `data`, `mappings`, `reports`,
  `src`, `tests`, `scripts`, `.claude`, `justfile`, and `CLAUDE.md` found the
  active YAML, aggregate copy, SSSOM row, generated indexes, and ignored
  aggregate backups.

## Completeness

- CAS, formula, SMILES, InChI, curation history, and `ingredient_type` are
  populated.
- No role, component, environmental context, discussion, source occurrence, or
  dataset entry is needed.
- The aggregate copy in `data/curated/mapped_ingredients.yaml` matches the
  per-record YAML.

## Recommended Edits

- None for current identity or mapping. Avoid rewriting the old append-only
  history entry solely to expand its truncated InChI prose.
