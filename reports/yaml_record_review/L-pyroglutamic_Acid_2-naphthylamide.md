# `data/ingredients/mapped/L-pyroglutamic_Acid_2-naphthylamide.yaml`

## Verdict

Pass with minor issues. The manually promoted CHEBI:90601 identity, active
ChEBI term, formula, PubChem structure, source occurrence count, and final
SSSOM row are consistent, but the original unmapped-import notes are stale.

## Identity

- Reviewed record:
  `data/ingredients/mapped/L-pyroglutamic_Acid_2-naphthylamide.yaml`.
- Identifier and grounding: `identifier: CHEBI:90601` with
  `ontology_mapping.ontology_id: CHEBI:90601`, label
  `5-oxo-L-proline 2-naphthylamide`, source `CHEBI`,
  `mapping_quality: SYNONYM_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: molecular formula `C15H14N2O2`, InChI, SMILES, and
  molecular weight from ChEBI plus PubChem.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/L-proline_2-naphthylamide.yaml data/ingredients/mapped/L-pyroglutamic_Acid_2-naphthylamide.yaml data/ingredients/mapped/L-rhamnose.yaml data/ingredients/mapped/L-serine.yaml data/ingredients/mapped/L-serine_2-naphthylamide.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/L-proline_2-naphthylamide.yaml data/ingredients/mapped/L-pyroglutamic_Acid_2-naphthylamide.yaml data/ingredients/mapped/L-rhamnose.yaml data/ingredients/mapped/L-serine.yaml data/ingredients/mapped/L-serine_2-naphthylamide.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  exited 0 for the 5 ChEBI records.

## Evidence

- EBI OLS4 resolves `CHEBI:90601` as active
  `5-oxo-L-proline 2-naphthylamide` and lists CAS `22155-91-5`.
- PubChem resolves `5-oxo-L-proline 2-naphthylamide` to CID `6950551` with
  formula `C15H14N2O2` and the same InChI as the YAML record.
- The manual promotion explains that L-pyroglutamic acid 2-naphthylamide is
  5-oxo-L-proline 2-naphthylamide, supporting the synonym-grade mapping.
- The final SSSOM publishes one `skos:exactMatch` row to `CHEBI:90601` with an
  empty `other` field, so no unreviewed synonyms are exported.
- Minor: the record-level `notes` and initial curation event still say the
  MicrobeDecoder importer found no CHEBI/NCIT match and that curator review is
  needed, even though the record was promoted to CHEBI:90601.
- The hidden and ignored-inclusive search over `data`, `mappings`, `reports`,
  `docs`, `src`, and `tests` found the current YAML, aggregate copy, final
  SSSOM row, docs projections, and the original MicrobeDecoder source row.

## Completeness

- The active ChEBI identity, structure, source occurrence count, aggregate
  copy, and final SSSOM row are present and consistent.
- The stale notes do not affect published SSSOM output, but they make the
  active YAML claim that a now-resolved record still needs curator review.

## Recommended Edits

- Minor: remove the stale unmapped-import `notes` value from
  `data/ingredients/mapped/L-pyroglutamic_Acid_2-naphthylamide.yaml` the next
  time this record is touched.
