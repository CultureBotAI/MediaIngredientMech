# `data/ingredients/mapped/Tryptophan.yaml`

## Verdict

Needs curation, major. The generic CHEBI identity, structure fields,
CultureMech role, aggregate row, and non-CAS final SSSOM synonyms pass, but
the generic record carries and publishes the L-tryptophan CAS RN already owned
by the local L-tryptophan sibling.

## Identity

- Reviewed record: `data/ingredients/mapped/Tryptophan.yaml`.
- Identifier and grounding: `identifier: CHEBI:27897` with matching
  `ontology_mapping.ontology_id`, label `tryptophan`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- CAS RN: `73-22-3`.
- Synonyms: raw CultureMech role/property strings plus exact CHEBI-derived
  generic tryptophan synonyms.
- Occurrences: 38 CultureMech recipe occurrences.
- Roles: one CultureMech-imported `nutritional_roles.NITROGEN_SOURCE` facet.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Tryptoneyeastbeef_(tyb)` through `Tuberactinamine_A`: exited 0 and wrote
  zero ERROR rows.
- `uv run --frozen linkml-term-validator validate-data` on this file with
  `--labels`: passed.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh OLS4 lookup for `CHEBI:27897` returns active label `tryptophan`,
  generic formula `C11H12N2O2`, the same stereo-unspecified InChI and SMILES
  as the YAML, and the exported non-CAS SSSOM `other` labels as CHEBI
  synonyms.
- Fresh OLS4 lookup for `CHEBI:16828` returns active label `L-tryptophan`, an
  L-specific InChI/SMILES, and `cas:73-22-3`.
- The final SSSOM row for `MIM:Tryptophan` exports `CAS:73-22-3`, while the
  local `MIM:L-tryptophan` row also maps to `CHEBI:16828` and exports
  `CAS:73-22-3`.

## Issues

### Major: `CAS:73-22-3` belongs to the L-tryptophan sibling

`chemical_properties.cas_rn` currently contains `73-22-3`, so the final SSSOM
`other` surface publishes `CAS:73-22-3` for the generic `CHEBI:27897`
Tryptophan record. OLS cross-references `cas:73-22-3` on the form-specific
`CHEBI:16828` L-tryptophan term instead; the active generic `CHEBI:27897`
object cross-references a different CAS, `54-12-6`.

This leaks stereospecific registry metadata from L-tryptophan onto the generic
tryptophan record and duplicates the same CAS token from the local
`L-Tryptophan` record.

## Completeness

- The generic CHEBI mapping, generic synonyms, structure fields, aggregate
  copy, and CultureMech nitrogen-source role agree.
- The raw `Role:` / `Properties:` CultureMech strings are kept out of final
  SSSOM `other`.
- A hidden/ignored-inclusive search across `mappings`, `data/curated`, and
  `reports` found the existing `CHEBI:16828` L-tryptophan sibling and its
  `CAS:73-22-3` final SSSOM token.

## Recommended Edits

- Re-audit the source labels behind the generic `Tryptophan` import. If those
  labels should denote L-tryptophan, merge this record into the existing
  `data/ingredients/mapped/L-tryptophan.yaml` sibling.
- If the record stays generic, remove `73-22-3` from
  `chemical_properties.cas_rn` and regenerate final SSSOM so
  `MIM:Tryptophan` stops exporting `CAS:73-22-3`.
