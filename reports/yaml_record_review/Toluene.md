# `data/ingredients/mapped/Toluene.yaml`

## Verdict

Pass. The exact CHEBI identity, CAS RN, real ChEBI/kg-microbe synonyms,
CultureMech carbon-source role, occurrence count, aggregate row, and final
SSSOM row for toluene are synchronized.

## Identity

- Reviewed record: `data/ingredients/mapped/Toluene.yaml`.
- Identifier and grounding: `identifier: CHEBI:17578` with matching
  `ontology_mapping.ontology_id`, label `toluene`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`,
  `kg_microbe_node_id: CHEBI:17578`, and `ingredient_type:
  SINGLE_INGREDIENT`.
- CAS RN: `108-88-3`.
- Synonyms: raw CultureMech role/cross-reference text plus exact labels
  `Toluen`, `Toluol`, `methylbenzene`, and `phenylmethane`.
- Occurrences: 13 CultureMech recipe occurrences in 13 media.
- Roles: `nutritional_roles.CARBON_SOURCE` imported from original CultureMech
  role text.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Titanium_chloride` through `Tomatidine_Hydrochloride`: exited 0 and wrote
  zero ERROR rows.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh OLS4 search for `toluene` returns `CHEBI:17578` with label `toluene`.
- Fresh PubChem lookup for CAS `108-88-3` returns formula `C7H8`, SMILES
  `CC1=CC=CC=C1`, and the same InChI as the YAML.
- The final SSSOM row has `MIM:Toluene skos:exactMatch CHEBI:17578`, exports
  only real synonyms plus `CAS:108-88-3`, and correctly filters the raw
  `Role:` and `Cross-references:` strings out of `other`.

## Completeness

- The CHEBI identity, CAS RN, structure fields, exact synonyms, occurrence
  count, aggregate copy, CultureMech `CARBON_SOURCE` evidence, and final SSSOM
  row agree.
- No components or environmental contexts are asserted.

## Recommended Edits

- None.
