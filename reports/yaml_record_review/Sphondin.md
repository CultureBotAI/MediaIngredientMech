# `data/ingredients/mapped/Sphondin.yaml`

## Verdict

Pass. The CultureBotHT CAS import, exact CHEBI grounding, PubChem structure
fields, and final SSSOM row all agree for sphondin.

## Identity

- Reviewed record: `data/ingredients/mapped/Sphondin.yaml`.
- Identifier and grounding: `identifier: CHEBI:81486` with
  `ontology_mapping.ontology_id: CHEBI:81486`, label `Sphondin`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: `cas_rn: 483-66-9` and formula `C12H8O4`.
- Occurrences: 0 source occurrences across 0 CultureMech media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Sphondin` through `Spiramycin_II`: exited 0 and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI record.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh OLS4 lookup resolves active `CHEBI:81486` with label `Sphondin`,
  matching the stored exact target.
- PubChem resolves CAS `483-66-9` to CID `108104`; the CID has formula
  `C12H8O4`, IUPAC name `6-methoxyfuro[2,3-h]chromen-2-one`, and synonym
  `CHEBI:81486`, agreeing with the stored chemical properties and final
  `CAS:483-66-9` payload.
- The final SSSOM row exact-matches `CHEBI:81486` and publishes only
  `CAS:483-66-9` in `other`.

## Completeness

- The identifier, CAS, formula, structure, aggregate row, and final SSSOM row
  agree.
- No unsupported active synonym, role, component, or final SSSOM payload was
  found.

## Recommended Edits

- None.
