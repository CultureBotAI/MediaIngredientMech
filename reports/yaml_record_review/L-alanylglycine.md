# `data/ingredients/mapped/L-alanylglycine.yaml`

## Verdict

Pass with minor issues. The MicrobeDecoder promotion to active CHEBI:73757,
ChEBI synonym grade, structure, empty MIM occurrence count, and final SSSOM row
are consistent; only stale importer notes still describe the record as needing
CHEBI/NCIT review.

## Identity

- Reviewed record: `data/ingredients/mapped/L-alanylglycine.yaml`.
- Identifier and grounding: `identifier: CHEBI:73757` with
  `ontology_mapping.ontology_id: CHEBI:73757`, label `Ala-Gly`, source
  `CHEBI`, `mapping_quality: SYNONYM_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: molecular formula `C5H10N2O3`, InChI, SMILES, and
  molecular weight from ChEBI plus PubChem.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/L-alanylglycine.yaml data/ingredients/mapped/L-alliin.yaml data/ingredients/mapped/L-alpha-Phosphatidylcholine.yaml data/ingredients/mapped/L-arginine.yaml data/ingredients/mapped/L-arginine_X_Hcl.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- Engine A LinkML term validation passed for all 5 ChEBI records.

## Evidence

- EBI OLS4 resolves `CHEBI:73757` as active `Ala-Gly`, lists
  `L-alanylglycine` as a synonym, and reports the same molecular formula,
  SMILES, InChI, and monoisotopic identity as the YAML.
- PubChem resolves the `L-alanylglycine` name to CID `6998029` with formula
  `C5H10N2O3` and the same InChI as the YAML record.
- The final SSSOM publishes one `skos:exactMatch` row to `CHEBI:73757`; its
  blank `other` field does not publish unsupported synonym payload.
- The hidden and ignored-inclusive search over `data`, `mappings`, `reports`,
  `docs`, `src`, and `tests` found the current YAML, aggregate copy,
  MicrobeDecoder source row, final SSSOM row, docs projections, and the
  resolved-unmapped grounding row that supports the promotion.
- Minor: the top-level `notes` and original import history still say there was
  no CHEBI/NCIT match and curator review was needed. That was true at
  import, but the record was later promoted to CHEBI:73757.

## Completeness

- The ChEBI identity, synonym-grade mapping, structure, source occurrence count,
  aggregate copy, and final SSSOM row are present and consistent.

## Recommended Edits

- Minor: update the stale top-level `notes` in
  `data/ingredients/mapped/L-alanylglycine.yaml` and the aggregate copy the
  next time the record is touched so the current review text does not imply
  that the CHEBI search is still unresolved.
