# `data/ingredients/mapped/3-O-methylgallate.yaml`

## Verdict

Needs curation, major. The active `CHEBI:28647` neutral
`3-O-methylgallic acid` identity, IUPAC synonym, ChEBI chemistry, SSSOM row, and
aggregate row pass, but the synonym list still contains source context
`reduction: 3-O-methylgallate` that is not an ingredient label and now leaks
into SSSOM and the public label index.

## Identity

- Reviewed record: `data/ingredients/mapped/3-O-methylgallate.yaml`.
- Identifier and grounding: `identifier: CHEBI:28647` with
  `ontology_mapping.ontology_id: CHEBI:28647`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Official ChEBI check: the refreshed EMBL-EBI ChEBI page for `CHEBI:28647`
  resolves to `3-O-methylgallic acid`, lists formula `C8H8O5`, SMILES
  `COc1cc(C(=O)O)cc(O)c1O`, the same standard InChI recorded in the YAML, and
  CAS `3934-84-7`.
- The `3,4-dihydroxy-5-methoxybenzoic acid` synonym is the ChEBI IUPAC name and
  is represented as an `EXACT_SYNONYM`.
- `ingredient_type: SINGLE_INGREDIENT` is present.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/3-Methylglutaric_Acid.yaml data/ingredients/mapped/3-O-Methyl-D-glucopyranose.yaml data/ingredients/mapped/3-O-methyl-glucose.yaml data/ingredients/mapped/3-O-methyl_Alpha-D-glucopyranoside.yaml data/ingredients/mapped/3-O-methylgallate.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/3-O-methylgallate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- Whole-corpus checks run earlier in this review pass passed; only the shared
  evidence validator was unavailable because `../culturebotai-claw` is absent.
- Per-record/aggregate comparison against `data/curated/mapped_ingredients.yaml`:
  exact equality passed.
- `mappings/ingredient_mappings.sssom.tsv` contains the expected exact
  `MIM:3-O-methylgallate` to `CHEBI:28647` row, but its `other` field also
  carries `reduction: 3-O-methylgallate`.

## Evidence

- The active ChEBI page confirms the neutral acid's formula, structure, IUPAC
  name, and CAS RN.
- The OAK/OLS row-review candidate for `3-O-methylgallate` is already
  represented by the record's preferred term.
- Unsupported as an active label: `reduction: 3-O-methylgallate` is a
  source-surface context phrase recovered by the SSSOM `other` backfill, not a
  synonym that denotes the chemical form. It is exported as a synonym in
  `docs/data/label_index.csv` and in the SSSOM `other` field.
- Advisory: `mappings/record_research_validation.tsv` reports CAS `3934-84-7`
  as available for this exact neutral acid; ChEBI now independently confirms
  that registry number.
- The hidden/ignored-inclusive search over `data`, `mappings`, `reports`,
  `docs`, `scripts`, `conf`, `src`, and `tests` found the active YAML,
  aggregate, SSSOM, synonym-enrichment review, generated docs, and CAS advisory
  row.

## Completeness

- `ingredient_type: SINGLE_INGREDIENT` is present.
- Formula, InChI, and SMILES are populated from ChEBI.
- CAS `3934-84-7` can be added from the official ChEBI page if this record is
  touched for the synonym cleanup.

## Recommended Edits

1. In `data/ingredients/mapped/3-O-methylgallate.yaml`, remove the
   `sssom_other_backfill` raw synonym `reduction: 3-O-methylgallate` or move the
   `reduction` context into provenance that does not export as an exact label.
2. Optionally add `chemical_properties.cas_rn: 3934-84-7` while preserving the
   existing ChEBI formula, InChI, and SMILES.
3. Run the per-record strict validator, compare the record against
   `data/curated/mapped_ingredients.yaml`, rebuild the SSSOM/docs with the
   maintained generators, and then rerun the whole-corpus SSSOM and flat-export
   checks.
