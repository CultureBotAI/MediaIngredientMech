# `data/ingredients/mapped/L-asparagine.yaml`

## Verdict

Pass. The CultureMech exact ChEBI identity, CAS value, PubChem structure,
claim-level nitrogen-source role, occurrence count, duplicate merge, and final
SSSOM row are consistent.

## Identity

- Reviewed record: `data/ingredients/mapped/L-asparagine.yaml`.
- Identifier and grounding: `identifier: CHEBI:17196` with
  `ontology_mapping.ontology_id: CHEBI:17196`, label `L-asparagine`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS RN `70-47-3`, molecular formula `C4H8N2O3`, InChI,
  and SMILES.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/L-ascorbic_Acid.yaml data/ingredients/mapped/L-asparagine.yaml data/ingredients/mapped/L-aspartate.yaml data/ingredients/mapped/L-aspartic_Acid.yaml data/ingredients/mapped/L-citrulline.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- Engine A LinkML term validation passed for all 5 ChEBI records.

## Evidence

- EBI OLS4 resolves `CHEBI:17196` as active `L-asparagine`, lists CAS
  `70-47-3`, and includes the exact and related ChEBI synonyms exported for
  this record.
- PubChem resolves CAS RN `70-47-3` to CID `6267` with formula `C4H8N2O3` and
  the same InChI as the YAML record.
- The final SSSOM publishes one `skos:exactMatch` row to `CHEBI:17196` with
  curated synonyms and `CAS:70-47-3` in `other`; raw `Cross-references:` and
  `Role:` CultureMech provenance strings are correctly filtered out.
- `nutritional_roles.NITROGEN_SOURCE` has `DATABASE_ENTRY` evidence from the
  CultureMech pipeline with original role text `Nitrogen Source`, matching the
  migrated role enum.
- The hidden and ignored-inclusive search over `data`, `mappings`, `reports`,
  `docs`, `src`, and `tests` found the current YAML, aggregate copy, final
  SSSOM row, MicrobeDecoder source rows, docs projections, duplicate-merge
  history, and OAK/OLS row-review confirmation.

## Completeness

- The active ChEBI identity, CAS RN, formula, structure, occurrence count,
  nitrogen-source role, aggregate copy, and final SSSOM row are present and
  consistent.

## Recommended Edits

- None.
