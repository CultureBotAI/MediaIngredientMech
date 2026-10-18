# `data/ingredients/mapped/L-ascorbic_Acid.yaml`

## Verdict

Pass. The CultureMech exact ChEBI identity, CAS value, PubChem structure,
claim-level vitamin role, occurrence count, duplicate merge, and final SSSOM
row are consistent.

## Identity

- Reviewed record: `data/ingredients/mapped/L-ascorbic_Acid.yaml`.
- Identifier and grounding: `identifier: CHEBI:29073` with
  `ontology_mapping.ontology_id: CHEBI:29073`, label `L-ascorbic acid`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS RN `50-81-7`, molecular formula `C6H8O6`, InChI,
  and SMILES.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/L-ascorbic_Acid.yaml data/ingredients/mapped/L-asparagine.yaml data/ingredients/mapped/L-aspartate.yaml data/ingredients/mapped/L-aspartic_Acid.yaml data/ingredients/mapped/L-citrulline.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- Engine A LinkML term validation passed for all 5 ChEBI records.

## Evidence

- EBI OLS4 resolves `CHEBI:29073` as active `L-ascorbic acid`, lists CAS
  `50-81-7`, and includes all curated ChEBI/KG-Microbe synonyms that the final
  SSSOM publishes for this record.
- PubChem resolves CAS RN `50-81-7` to CID `54670067` with formula `C6H8O6`
  and the same InChI as the YAML record.
- The final SSSOM publishes one `skos:exactMatch` row to `CHEBI:29073` with
  only curated synonyms plus `CAS:50-81-7` in `other`; raw CultureMech `Role:`
  text is correctly filtered out.
- `nutritional_roles.VITAMIN_SOURCE` has `DATABASE_ENTRY` evidence from the
  CultureMech pipeline with original role text `Vitamin Source`, matching the
  migrated role enum.
- The hidden and ignored-inclusive search over `data`, `mappings`, `reports`,
  `docs`, `src`, and `tests` found the current YAML, aggregate copy, final
  SSSOM row, docs projections, duplicate-merge history, and OAK/OLS row-review
  confirmation.

## Completeness

- The active ChEBI identity, CAS RN, formula, structure, occurrence count,
  vitamin role, aggregate copy, and final SSSOM row are present and consistent.

## Recommended Edits

- None.
