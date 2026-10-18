# `data/ingredients/mapped/L-galactonic_Acid_Gamma-lactone.yaml`

## Verdict

Pass with minor issues. The MicrobeDecoder synonym promotion to active
CHEBI:17464, lactone structure, empty final synonym payload, source occurrence
count, and final SSSOM row are consistent; only stale importer notes still say
the record lacked a CHEBI/NCIT match.

## Identity

- Reviewed record:
  `data/ingredients/mapped/L-galactonic_Acid_Gamma-lactone.yaml`.
- Identifier and grounding: `identifier: CHEBI:17464` with
  `ontology_mapping.ontology_id: CHEBI:17464`, label
  `L-galactono-1,4-lactone`, source `CHEBI`, `mapping_quality:
  SYNONYM_MATCH`, `mapping_status: MAPPED`, and `ingredient_type:
  SINGLE_INGREDIENT`.
- Chemical properties: molecular formula `C6H10O6`, InChI, SMILES, and
  molecular weight from ChEBI plus PubChem.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/L-cystine.yaml data/ingredients/mapped/L-fructose.yaml data/ingredients/mapped/L-fucose.yaml data/ingredients/mapped/L-galactonate.yaml data/ingredients/mapped/L-galactonic_Acid_Gamma-lactone.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- Engine A LinkML term validation passed for all 5 ChEBI records.

## Evidence

- EBI OLS4 resolves `CHEBI:17464` as active `L-galactono-1,4-lactone`, lists
  CAS `1668-08-2`, and reports the same formula and InChI as the YAML.
- PubChem resolves `L-galactono-1,4-lactone` to CID `6857365` with formula
  `C6H10O6` and the same InChI as the YAML record.
- The resolved-unmapped promotion records that L-galactonic acid gamma-lactone
  is L-galactono-1,4-lactone, the gamma-lactone, so the
  `SYNONYM_MATCH` mapping is appropriate.
- The final SSSOM publishes one `skos:exactMatch` row to `CHEBI:17464` with an
  empty `other` field, so no raw MicrobeDecoder text is exported.
- The hidden and ignored-inclusive search over `data`, `mappings`, `reports`,
  `docs`, `src`, and `tests` found the current YAML, aggregate copy, final
  SSSOM row, docs projections, and the resolved-unmapped grounding row that
  supports the promotion.
- Minor: the top-level `notes` and original import history still say there was
  no CHEBI/NCIT match and curator review was needed. That was true at import,
  but the record was later promoted to CHEBI:17464.

## Completeness

- The ChEBI identity, synonym-grade mapping, structure, source occurrence
  count, aggregate copy, and final SSSOM row are present and consistent.

## Recommended Edits

- Minor: update the stale top-level `notes` in
  `data/ingredients/mapped/L-galactonic_Acid_Gamma-lactone.yaml` and the
  aggregate copy the next time the record is touched so the current review text
  does not imply that the CHEBI search is still unresolved.
