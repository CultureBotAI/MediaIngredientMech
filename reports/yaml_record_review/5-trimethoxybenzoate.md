# `data/ingredients/mapped/5-trimethoxybenzoate.yaml`

## Verdict

Needs curation, major. The corrected `CHEBI:58989`
3,4,5-trimethoxybenzoate identity passes, but the grade is still
`CLOSE_MATCH`, the anion chemistry is missing, and two non-exact raw source
labels are exported as SSSOM `other` surfaces.

## Identity

- Reviewed record: `data/ingredients/mapped/5-trimethoxybenzoate.yaml`.
- Identifier and grounding: `identifier: CHEBI:58989` with
  `ontology_mapping.ontology_id: CHEBI:58989`, source `CHEBI`,
  stale `mapping_quality: CLOSE_MATCH`, and `mapping_status: MAPPED`.
- The official ChEBI page resolves `CHEBI:58989` to
  `3,4,5-trimethoxybenzoate` with formula `C10H11O5`, charge `-1`, SMILES
  `COc1cc(C(=O)[O-])cc(OC)c1OC`, and the expected anion InChI.
- Local OAK metadata agrees that `CHEBI:58989` is the conjugate base of
  3,4,5-trimethoxybenzoic acid.
- `ingredient_type: SINGLE_INGREDIENT` is present.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/5-trimethoxybenzoate.yaml data/ingredients/mapped/56-dihydro-5-azathymidine.yaml data/ingredients/mapped/574-Trimethoxyisoflavone.yaml data/ingredients/mapped/5z-4-bromo-5-_Bromomethylene-2_5h-furanone.yaml data/ingredients/mapped/6-Hydroxyflavone.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/5-trimethoxybenzoate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen runoak -i sqlite:obo:chebi aliases CHEBI:58989 CHEBI:34472`:
  returned `CHEBI:58989` with canonical label `3,4,5-trimethoxybenzoate`.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:58989 CHEBI:34472`:
  returned the anion formula, charge, structure strings, and mass for
  `CHEBI:58989`.

## Evidence

- The active ChEBI term supports the corrected preferred term and exact
  `CHEBI:58989` identity.
- `mapping_quality: CLOSE_MATCH` is stale after
  `apply_locant_corrections`: the preferred term now exactly matches
  `CHEBI:58989`, and the history explicitly says the old close-match reason no
  longer holds.
- `5-trimethoxybenzoate` is an impossible comma-truncated label missing its
  first two locants, and bare `Trimethoxybenzoate` omits all three locants. Both
  are source labels, not exact synonyms of 3,4,5-trimethoxybenzoate, but both
  are exported in SSSOM `other`.
- The `chemical_properties` block is absent even though OAK and ChEBI provide
  formula `C10H11O5`, charge `-1`, SMILES, InChI, average mass, and
  monoisotopic mass for the mapped anion. CAS `118-41-2` belongs to the neutral
  acid and should not be copied onto this anion record.
- The hidden/ignored-inclusive search over `data`, `mappings`, `reports`,
  `scripts`, `tests`, and `src` found the active YAML, aggregate copy, SSSOM
  row, microbedecoder source row, `truncated_locants.tsv` evidence for the lost
  locants, stale advisory rows, and ignored aggregate backups.

## Completeness

- `ingredient_type` and the exact ChEBI grounding are populated.
- Chemistry is materially incomplete for a ChEBI-backed anion with structural
  data.

## Recommended Edits

- In `data/ingredients/mapped/5-trimethoxybenzoate.yaml`, change
  `ontology_mapping.mapping_quality` from `CLOSE_MATCH` to `EXACT_MATCH`.
- Remove `5-trimethoxybenzoate` and `Trimethoxybenzoate` from `synonyms`, or
  move them to source-occurrence-only provenance that will not be exported as
  exact SSSOM `other` values.
- Backfill `chemical_properties` from `CHEBI:58989` without adding the neutral
  acid's CAS RN; rebuild `mappings/ingredient_mappings.sssom.tsv` and
  `data/curated/mapped_ingredients.yaml`, then rerun strict validation, SSSOM
  invariants, and the id/label correspondence gate.
