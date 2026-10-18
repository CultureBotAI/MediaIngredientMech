# `data/ingredients/mapped/L-arginine.yaml`

## Verdict

Pass. The CultureMech exact ChEBI identity, CAS value, PubChem structure,
claim-level nitrogen-source role, occurrence count, and final SSSOM row are
consistent.

## Identity

- Reviewed record: `data/ingredients/mapped/L-arginine.yaml`.
- Identifier and grounding: `identifier: CHEBI:16467` with
  `ontology_mapping.ontology_id: CHEBI:16467`, label `L-arginine`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS RN `74-79-3`, molecular formula `C6H14N4O2`, InChI,
  and SMILES.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/L-alanylglycine.yaml data/ingredients/mapped/L-alliin.yaml data/ingredients/mapped/L-alpha-Phosphatidylcholine.yaml data/ingredients/mapped/L-arginine.yaml data/ingredients/mapped/L-arginine_X_Hcl.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- Engine A LinkML term validation passed for all 5 ChEBI records.

## Evidence

- EBI OLS4 resolves `CHEBI:16467` as active `L-arginine`, lists CAS
  `74-79-3`, and includes all seven ChEBI/KG-Microbe exact synonyms carried by
  the record.
- PubChem resolves CAS RN `74-79-3` to CID `6322` with formula `C6H14N4O2` and
  the same InChI as the YAML record.
- The final SSSOM publishes one `skos:exactMatch` row to `CHEBI:16467` with the
  curated exact synonyms and `CAS:74-79-3` in `other`; raw `Cross-references:`
  and `Role:` CultureMech provenance strings are correctly filtered out.
- `nutritional_roles.NITROGEN_SOURCE` has `DATABASE_ENTRY` evidence from the
  CultureMech pipeline with original role text `Nitrogen Source`, matching the
  migrated role enum.
- The hidden and ignored-inclusive search over `data`, `mappings`, `reports`,
  `docs`, `src`, and `tests` found the current YAML, aggregate copy, final
  SSSOM row, docs projections, CultureMech occurrence rows, and row-review
  confirmation. The separate `Arginine` record denotes the non-stereospecific
  CHEBI:29016 identity and does not make this L-specific record inconsistent.

## Completeness

- The active ChEBI identity, CAS RN, formula, structure, occurrence count,
  nitrogen-source role, aggregate copy, and final SSSOM row are present and
  consistent.

## Recommended Edits

- None.
