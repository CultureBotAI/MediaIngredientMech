# `data/ingredients/mapped/N-acetyl-lysine.yaml`

## Verdict

Pass. The CAS-backed `CHEBI:35704` N(2)-acetyl-L-lysine identity, FEBA
provenance, structure, occurrence count, synonyms, and final exact row pass.

## Identity

- Reviewed record: `data/ingredients/mapped/N-acetyl-lysine.yaml`.
- Identifier and grounding: `identifier: CHEBI:35704` with
  `ontology_mapping.ontology_id: CHEBI:35704`, label
  `N(2)-acetyl-L-lysine`, source `CHEBI`, `mapping_quality: CAS_RN_LOOKUP`,
  `mapping_status: MAPPED`, and `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: ten recipe occurrences, reflected by ten
  `mappings/culturemech_recipe_membership.tsv` rows for `CHEBI:35704`.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `N-acetyl-lysine` through `N-acetylmuramic_Acid`: exited 0 and wrote zero
  ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.

## Evidence

- A fresh EBI OLS4 lookup resolves `CHEBI:35704` as active
  `N(2)-acetyl-L-lysine`, with `cas:1946-82-3`, formula `C8H16N2O3`, the
  stored InChI/SMILES, and the same-substance aliases held in YAML.
- The final SSSOM publishes one `skos:exactMatch` row from
  `MIM:N-acetyl-lysine` to `CHEBI:35704`; every `other` token is either a
  ChEBI synonym of that same L-lysine acetylation product or `CAS:1946-82-3`.

## Completeness

- The active ChEBI target, CAS RN, structure, FEBA occurrence count, and final
  row agree.
- The record does not assert components, roles, or non-synonym final `other`
  text.

## Recommended Edits

- None.
