# `data/ingredients/mapped/L-galactonate.yaml`

## Verdict

Pass. The MicrobeDecoder exact-label promotion to active CHEBI:53071, charged
L-galactonate structure, empty synonym payload, source occurrence count, and
final SSSOM row are consistent.

## Identity

- Reviewed record: `data/ingredients/mapped/L-galactonate.yaml`.
- Identifier and grounding: `identifier: CHEBI:53071` with
  `ontology_mapping.ontology_id: CHEBI:53071`, label `L-galactonate`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: molecular formula `C6H11O7`, anion InChI and SMILES,
  and molecular weight from ChEBI plus PubChem.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/L-cystine.yaml data/ingredients/mapped/L-fructose.yaml data/ingredients/mapped/L-fucose.yaml data/ingredients/mapped/L-galactonate.yaml data/ingredients/mapped/L-galactonic_Acid_Gamma-lactone.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- Engine A LinkML term validation passed for all 5 ChEBI records.

## Evidence

- EBI OLS4 resolves `CHEBI:53071` as active `L-galactonate` with the same
  charged formula, InChI, and SMILES as the YAML.
- PubChem resolves `L-galactonate` to CID `44229140` with formula
  `C6H11O7-` and an InChI matching CHEBI:53071 and the YAML record.
- The MicrobeDecoder import grounded
  `kgmicrobe.trait:l_galactonate` by exact OLS label match and records one
  `BacDive_Metabolite_utilization` source occurrence; the later
  `review-ingredients` event promoted the held mapping back to `MAPPED`.
- The final SSSOM publishes one `skos:exactMatch` row to `CHEBI:53071` with an
  empty `other` field, so no unreviewed synonyms are exported.
- The hidden and ignored-inclusive search over `data`, `mappings`, `reports`,
  `docs`, `src`, and `tests` found the current YAML, aggregate copy,
  MicrobeDecoder source rows, final SSSOM row, and docs projections.

## Completeness

- The active ChEBI identity, charged structure, source occurrence count, empty
  synonym list, aggregate copy, and final SSSOM row are present and consistent.
- The empty CultureMech `occurrence_statistics` count is expected for this
  MicrobeDecoder-only import because its evidence is captured under
  `source_occurrences`.

## Recommended Edits

- None.
