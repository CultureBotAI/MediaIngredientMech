# `data/ingredients/mapped/H2wo4.yaml`

## Verdict

Pass. The tungstic-acid ChEBI identity, synonym-grade mapping, CAS RN,
chemical structure, CultureMech mineral role, occurrence count, exported
synonyms, and final SSSOM row are internally consistent.

## Identity

- Reviewed record: `data/ingredients/mapped/H2wo4.yaml`.
- Identifier and grounding: `identifier: CHEBI:36272` with
  `ontology_mapping.ontology_id: CHEBI:36272`, label `tungstic acid`, source
  `CHEBI`, `mapping_quality: SYNONYM_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS RN `7783-03-1`, formula `H2O4W`, InChI
  `InChI=1S/2H2O.2O.W/h2*1H2;;;/q;;;;+2/p-2`, and SMILES
  `[H][O][W](=[O])(=[O])[O][H]`.
- Occurrence statistics: `total_occurrences: 32` and `media_count: 32`.
- Role facet: `TRACE_ELEMENT` with `DATABASE_ENTRY` evidence preserving the
  CultureMech original role text `Mineral`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/H2tetramethylammonium.yaml data/ingredients/mapped/H2trimethylamine.yaml data/ingredients/mapped/H2wo4.yaml data/ingredients/mapped/H3PO4.yaml data/ingredients/mapped/H3bo2.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `linkml-term-validator` passed for `CHEBI:36272` and the CAS registry CURIE.
- The matching aggregate `data/curated/mapped_ingredients.yaml` entry is
  identical to the split per-record YAML.

## Evidence

- OLS4 resolves `CHEBI:36272` as active `tungstic acid` with CAS `7783-03-1`,
  formula `H2O4W`, the same InChI, and the same SMILES.
- OLS4 lists `H2WO4` as a related synonym for `CHEBI:36272`, so the record's
  `SYNONYM_MATCH` grade correctly reflects the source surface form.
- The final SSSOM synonym tokens `[WO2(OH)2]`,
  `dihydrogen wolframate`, `dihydroxidodioxidotungsten`, and
  `tungstic(VI) acid` all occur as ChEBI synonyms; the final `CAS:7783-03-1`
  token matches `chemical_properties.cas_rn`.
- The raw CultureMech `Role:`/`Properties:` synonym is correctly filtered from
  final SSSOM.
- The final SSSOM publishes one `skos:exactMatch` row from `MIM:H2wo4` to
  `CHEBI:36272`.

## Completeness

- The active ChEBI identifier, CAS RN, formula, InChI, SMILES, occurrence
  statistics, CultureMech role facet, and final SSSOM row are present and
  consistent.

## Recommended Edits

- None.
