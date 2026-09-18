# `data/ingredients/mapped/L-cystine.yaml`

## Verdict

Pass. The CultureMech exact CHEBI:16283 identity, CAS RN, PubChem structure,
claim-level nitrogen-source role, occurrence count, and final SSSOM row are
consistent.

## Identity

- Reviewed record: `data/ingredients/mapped/L-cystine.yaml`.
- Identifier and grounding: `identifier: CHEBI:16283` with
  `ontology_mapping.ontology_id: CHEBI:16283`, label `L-cystine`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS RN `56-89-3`, molecular formula `C6H12N2O4S2`,
  InChI, and SMILES for L-cystine.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/L-cystine.yaml data/ingredients/mapped/L-fructose.yaml data/ingredients/mapped/L-fucose.yaml data/ingredients/mapped/L-galactonate.yaml data/ingredients/mapped/L-galactonic_Acid_Gamma-lactone.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- Engine A LinkML term validation passed for all 5 ChEBI records.

## Evidence

- EBI OLS4 resolves `CHEBI:16283` as active `L-cystine`, lists CAS
  `56-89-3`, and includes the exported exact synonyms.
- PubChem resolves CAS RN `56-89-3` to CID `67678` with formula
  `C6H12N2O4S2` and the same InChI as the YAML record.
- `nutritional_roles.NITROGEN_SOURCE` has `DATABASE_ENTRY` evidence from the
  CultureMech pipeline with original role text `Nitrogen Source`, matching the
  migrated role enum.
- The final SSSOM publishes one `skos:exactMatch` row to `CHEBI:16283`; its
  `other` field contains exact ChEBI or kg-microbe synonyms plus
  `CAS:56-89-3`, with no broader sibling or raw role text.
- The hidden and ignored-inclusive search over `data`, `mappings`, `reports`,
  `docs`, `src`, and `tests` found the current YAML, aggregate copy,
  MicrobeDecoder source rows, final SSSOM row, docs projections, and prior
  sibling-review references.

## Completeness

- The active ChEBI identity, CAS RN, structure, occurrence count, role,
  aggregate copy, and final SSSOM row are present and consistent.

## Recommended Edits

- None.
