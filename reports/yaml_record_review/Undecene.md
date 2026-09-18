# `data/ingredients/mapped/Undecene.yaml`

## Verdict

Pass. The CAS-backed mapping to 1-undecene, structure fields, synonym,
aggregate row, and final SSSOM row pass.

## Identity

- Reviewed record: `data/ingredients/mapped/Undecene.yaml`.
- Identifier and grounding: `identifier: CHEBI:77444` with matching
  `ontology_mapping.ontology_id`, label `1-undecene`, source `CHEBI`,
  `mapping_quality: CAS_RN_LOOKUP`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- CAS RN: `821-95-4`.
- Synonyms: one CHEBI synonym, `undec-1-ene`.
- Occurrences: no CultureMech recipe occurrences.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `UW_Concentrated_Base` through `Uracil`: exited 0 and wrote zero ERROR rows.
- `uv run --frozen linkml-term-validator validate-data` on this file with
  `--labels`: passed.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh OLS4 exact search for `1-undecene` resolves active `CHEBI:77444` with
  label `1-undecene`, `Undecene` as a related synonym, and `undec-1-ene` as an
  exact synonym.
- Fresh PubChem lookup for `821-95-4` returns formula `C11H22` and the same
  InChI as the YAML. Its canonical SMILES is the same terminal alkene written
  in the opposite direction from the YAML SMILES.
- The final SSSOM row correctly has
  `MIM:Undecene skos:exactMatch CHEBI:77444`, with `undec-1-ene` and
  `CAS:821-95-4` in `other`.

## Issues

None.

## Completeness

- The CAS-backed CHEBI mapping, structure fields, synonym, aggregate copy, and
  final SSSOM row agree.
- OLS4 returned 404 for the direct `CHEBI:77444` term URL but resolved the same
  active CURIE through exact label search; the local Engine A term validator
  also resolved the id-label pair.

## Recommended Edits

None.
