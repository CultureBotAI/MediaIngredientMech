# `data/ingredients/mapped/Asiaticoside.yaml`

## Verdict

Pass. The record exactly denotes ChEBI `asiaticoside`, and its CAS, formula,
InChI, SMILES, ChEBI synonym, SSSOM row, and aggregate copy agree.

## Identity

- Reviewed record: `data/ingredients/mapped/Asiaticoside.yaml`.
- Identifier and grounding: `identifier: CHEBI:79928` with
  `ontology_mapping.ontology_id: CHEBI:79928`, `ontology_source: CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- OLS resolves `CHEBI:79928` to non-obsolete ChEBI `asiaticoside` with CAS xref
  `16830-15-2`, formula `C48H78O19`, and the same InChI and SMILES as the
  record.
- PubChem resolves CAS `16830-15-2` to CID `11954171` with the same formula and
  InChI.
- The single exact synonym in the record is the ChEBI IUPAC exact synonym for
  this term.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Ascorbate.yaml data/ingredients/mapped/Ascorbic_Acid.yaml data/ingredients/mapped/Ascosin.yaml data/ingredients/mapped/Asialofetuin.yaml data/ingredients/mapped/Asiaticoside.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Asiaticoside.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- OLS4 lookup for `CHEBI:79928`: resolved the current ChEBI label, formula,
  InChI, SMILES, CAS xref, and IUPAC synonym.
- PubChem lookup for CAS `16830-15-2`: resolved the same formula and InChI.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed;
  2951 records, 83 decompositions, 505 components, 0 violations.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.
- `uv run --frozen python scripts/check_flat_export_coverage.py`: passed before
  this review batch; docs data were fresh and every curated label was
  resolvable.
- `uv run --frozen python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`:
  passed before this review batch; all id/label pairs corresponded and 104
  non-blocking plausibility warnings were reported.

## Evidence

- `mappings/ingredient_mappings_oak_ols_review.tsv` row 330 and
  `mappings/ingredient_mappings_row_review_manifest.tsv` row 330 both confirm
  the `MIM:Asiaticoside` to `CHEBI:79928` mapping.
- `mappings/ingredient_mappings.sssom.tsv` row 488 maps `MIM:Asiaticoside` to
  `CHEBI:79928` with `skos:exactMatch` and carries the same IUPAC synonym and
  CAS xref.
- A hidden, ignored-inclusive search across the active checkout, excluding
  stale `data/curated/backups` and review output, found this identity in the
  per-record YAML, aggregate YAML, SSSOM, row-review TSVs, and generated docs.

## Completeness

- CAS, molecular formula, structure strings, exact synonym, `ingredient_type`,
  curation history, SSSOM, and the aggregate copy are populated.
- Zero occurrence counts are expected for this CultureBotHT compound with no
  known CultureMech recipes.
- No roles, components, environmental context, datasets, or discussions are
  needed.

## Recommended Edits

- None.
