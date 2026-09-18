# `data/ingredients/mapped/Verbascose.yaml`

## Verdict

Needs curation. The exact CHEBI identity, CAS RN, structure fields, synonym,
aggregate row, and final SSSOM row pass, but `CARBON_SOURCE` is still a
provisional ChEBI-ancestry role.

## Identity

- Reviewed record: `data/ingredients/mapped/Verbascose.yaml`.
- Identifier and grounding: `identifier: CHEBI:28586` with matching
  `ontology_mapping.ontology_id`, label `verbascose`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- CAS RN: `546-62-3`.
- Synonyms: one exact IUPAC synonym.
- Chemical fields: formula `C30H52O26` and ChEBI-backed SMILES/InChI.
- Occurrences: 0.
- Role: `CARBON_SOURCE` with provisional ChEBI-ancestry evidence.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Veratrine_Hydrochloride` through `Viomycin`: exited 0 and wrote zero ERROR
  rows.
- `uv run --frozen linkml-term-validator validate-data` on the CHEBI subset of
  this batch exited 0 for `Verbascose`, `Vibriostat`, and `Viomycin`.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh OLS4 lookup for `CHEBI:28586` returns active label `verbascose`, CAS
  xref `546-62-3`, formula `C30H52O26`, and the same SMILES/InChI as the YAML.
- The exported exact IUPAC synonym is present on `CHEBI:28586`, so final SSSOM
  `other` contains a real synonym plus `CAS:546-62-3`.

## Issues

- Major: `nutritional_roles.CARBON_SOURCE` rests on
  `COMPUTATIONAL_PREDICTION` evidence from the ChEBI `CHEBI:16646`
  carbohydrate closure, and its curator note explicitly marks the role as
  provisional.

## Completeness

- The exact CHEBI mapping, CAS RN, structure fields, synonym, aggregate copy,
  and final SSSOM row agree.
- The carbon-source role still needs source-backed evidence from maintained
  media data before it is reviewable as a curated role facet.

## Recommended Edits

- Replace or remove `data/ingredients/mapped/Verbascose.yaml`
  `nutritional_roles.CARBON_SOURCE`; keep it only if a maintained source
  supports verbascose as a carbon source in the specific media records that use
  it, then rerun strict validation and SSSOM invariant checks.
