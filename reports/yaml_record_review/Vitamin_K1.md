# `data/ingredients/mapped/Vitamin_K1.yaml`

## Verdict

Needs curation. The exact `CHEBI:18067` phylloquinone identity,
source-backed vitamin role, aggregate row, and final exact SSSOM row pass, but
the final `other` synonym list exports a concentration-qualified CultureMech
surface form.

## Identity

- Reviewed record: `data/ingredients/mapped/Vitamin_K1.yaml`.
- Identifier and grounding: `identifier: CHEBI:18067` with matching
  `ontology_mapping.ontology_id`, label `phylloquinone`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- CAS RN: `84-80-0`.
- Chemical fields: formula `C31H46O2` with populated InChI and SMILES strings.
- Synonyms: raw CultureMech role/property strings, exact kg-microbe
  phylloquinone labels, and the raw CultureMech occurrence surface form
  `Vitamin K1 (1 mg/ml)`.
- Occurrences: 127 CultureMech recipe occurrences across 127 media.
- Role: `VITAMIN_SOURCE` imported from CultureMech original role text.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Vitamin_K1` through `Vitamins-solution`: exited 0 and wrote zero ERROR rows.
- `uv run --frozen linkml-term-validator validate-data` on this CHEBI-primary
  record exited 0.
- Engine A label validation was skipped for the other four records in this
  batch because their primary identifiers are `MICRO` or local
  `kgmicrobe.ingredient` identifiers.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh OLS4 lookup for `CHEBI:18067` returns active label `phylloquinone`, CAS
  `84-80-0`, formula `C31H46O2`, matching structure strings, and active synonym
  coverage for the clean kg-microbe synonym set.
- The `VITAMIN_SOURCE` role is backed by `DATABASE_ENTRY` evidence carrying the
  original CultureMech role text `Vitamin Source`.
- The final SSSOM row correctly has
  `MIM:Vitamin_K1 skos:exactMatch CHEBI:18067`.
- The raw `Role:`/`Properties:` CultureMech strings are filtered from final
  SSSOM `other`, as intended.

## Issues

- Major: the final exact `CHEBI:18067` row exports the concentration-qualified
  recipe surface form `Vitamin K1 (1 mg/ml)` as an `other` synonym. That string
  describes a specific stock concentration or recipe annotation, not a
  synonymous label for phylloquinone itself.

## Completeness

- The exact CHEBI mapping, structure fields, CAS RN, occurrence count,
  source-backed vitamin role, aggregate copy, and SSSOM predicate agree.
- The final synonym set needs to be restricted to phylloquinone labels that do
  not encode recipe-specific concentration context.

## Recommended Edits

- Remove `Vitamin K1 (1 mg/ml)` from the record's exported synonym set, either
  by dropping the stale raw alias or by teaching the final SSSOM export to
  suppress concentration-qualified CultureMech surface forms.
- Rebuild SSSOM and rerun strict validation, LinkML term validation, SSSOM
  invariant validation, and the cross-record `other` synonym audit.
