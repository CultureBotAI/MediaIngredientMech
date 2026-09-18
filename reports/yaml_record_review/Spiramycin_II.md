# `data/ingredients/mapped/Spiramycin_II.yaml`

## Verdict

Pass. The MicrobeDecoder source label, `Acetylspiramycin` synonym, exact CHEBI
identity, structure fields, and final SSSOM row all agree for Spiramycin II.

## Identity

- Reviewed record: `data/ingredients/mapped/Spiramycin_II.yaml`.
- Identifier and grounding: `identifier: CHEBI:31168` with
  `ontology_mapping.ontology_id: CHEBI:31168`, label `spiramycin II`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Synonyms: `Acetylspiramycin`, retained as MicrobeDecoder raw text after
  duplicate merge.
- Chemical properties: formula `C45H76N2O15` with ChEBI/PubChem structure
  values.
- Occurrences: 0 CultureMech occurrences, with a MicrobeDecoder source
  occurrence for two `BacDive_Antibiotic_sensitivity` traits.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Sphondin` through `Spiramycin_II`: exited 0 and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI record.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh OLS4 lookup resolves active `CHEBI:31168` with label `spiramycin II`
  and related synonym `Acetylspiramycin`, matching the duplicate-merge note
  that absorbed `Acetylspiramycin` as a source label.
- PubChem resolves `Spiramycin II` to CID `49787020`, whose formula
  `C45H76N2O15`, InChI, and synonyms agree with `CHEBI:31168` and
  `Acetylspiramycin`.
- The final SSSOM row exact-matches `CHEBI:31168` and publishes only
  `Acetylspiramycin` in `other`.

## Completeness

- The sibling generic `Spiramycin` record has a stale Spiramycin-I structure,
  but this specific Spiramycin II record is not conflated with it.
- No unsupported active synonym, role, component, or final SSSOM payload was
  found.

## Recommended Edits

- None.
