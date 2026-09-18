# `data/ingredients/mapped/L-aspartate.yaml`

## Verdict

Pass with minor issues. The MicrobeDecoder promotion to active
CHEBI:29991, ChEBI synonym grade, monoanion structure, occurrence count, and
final SSSOM row are consistent; only stale importer notes still describe the
record as needing CHEBI/NCIT review.

## Identity

- Reviewed record: `data/ingredients/mapped/L-aspartate.yaml`.
- Identifier and grounding: `identifier: CHEBI:29991` with
  `ontology_mapping.ontology_id: CHEBI:29991`, label `L-aspartate(1-)`,
  source `CHEBI`, `mapping_quality: SYNONYM_MATCH`, `mapping_status: MAPPED`,
  and `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: molecular formula `C4H6NO4`, charge-implied InChI and
  SMILES for the monoanion, and molecular weight from ChEBI plus PubChem.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/L-ascorbic_Acid.yaml data/ingredients/mapped/L-asparagine.yaml data/ingredients/mapped/L-aspartate.yaml data/ingredients/mapped/L-aspartic_Acid.yaml data/ingredients/mapped/L-citrulline.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- Engine A LinkML term validation passed for all 5 ChEBI records.

## Evidence

- EBI OLS4 resolves `CHEBI:29991` as active `L-aspartate(1-)`, lists
  `L-aspartate` as an exact synonym, and reports the same formula, InChI, and
  SMILES as the YAML.
- The final SSSOM publishes one `skos:exactMatch` row to `CHEBI:29991`; its
  blank `other` field does not publish unsupported synonym payload.
- The hidden and ignored-inclusive search over `data`, `mappings`, `reports`,
  `docs`, `src`, and `tests` found the current YAML, aggregate copy,
  MicrobeDecoder source rows, final SSSOM row, docs projections, and the
  resolved-unmapped grounding row that supports the promotion.
- Minor: the top-level `notes` and original import history still say there was
  no CHEBI/NCIT match and curator review was needed. That was true at import,
  but the record was later promoted to CHEBI:29991.

## Completeness

- The ChEBI identity, synonym-grade mapping, structure, occurrence count,
  source occurrence count, aggregate copy, and final SSSOM row are present and
  consistent.

## Recommended Edits

- Minor: update the stale top-level `notes` in
  `data/ingredients/mapped/L-aspartate.yaml` and the aggregate copy the next
  time the record is touched so the current review text does not imply that the
  CHEBI search is still unresolved.
