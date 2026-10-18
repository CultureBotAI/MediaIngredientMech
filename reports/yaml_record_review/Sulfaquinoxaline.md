# `data/ingredients/mapped/Sulfaquinoxaline.yaml`

## Verdict

Pass. The CAS-primary `Sulfaquinoxaline` identity, synonym match to
`CHEBI:94719`, PubChem structure fields, aggregate row, and final SSSOM rows
all pass.

## Identity

- Reviewed record: `data/ingredients/mapped/Sulfaquinoxaline.yaml`.
- Identifier and grounding: `identifier: cas:59-40-5` with
  `ontology_mapping.ontology_id: CHEBI:94719`, label
  `4-amino-N-(2-quinoxalinyl)benzenesulfonamide`, source `CHEBI`,
  `mapping_quality: SYNONYM_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS `59-40-5`, PubChem CID `5338`, formula
  `C14H12N4O2S`, and PubChem InChI/SMILES.
- Occurrences: zero CultureMech recipe occurrences.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Sulfamethoxazole` through `Sulfaquinoxaline`: exited 0 and wrote zero ERROR
  rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI record.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh PubChem lookup resolves CAS `59-40-5` to CID `5338` with formula
  `C14H12N4O2S` and InChI/SMILES matching the YAML.
- Fresh OLS4 lookup resolves active `CHEBI:94719` with label
  `4-amino-N-(2-quinoxalinyl)benzenesulfonamide`, formula `C14H12N4O2S`,
  InChI matching the YAML, and `sulfaquinoxaline` as a related synonym.
- `mappings/culturemech_recipe_membership.tsv` has no `cas:59-40-5` rows,
  agreeing with `total_occurrences: 0` and `media_count: 0`.
- The final SSSOM row exact-matches `CHEBI:94719` under
  `semapv:ManualMappingCuration`, and its exact CAS registry row preserves
  `cas:59-40-5` with `CAS:59-40-5` as the only published `other` synonym.

## Completeness

- The same-formula parent regrade in
  `scripts/regrade_identical_formula_parents.py` documents the intentional move
  from the PubChem-derived parent relation to a synonym identity relation.
- The record has no active synonyms, components, roles, environmental contexts,
  or datasets needing narrower evidence.
- An ignored/hidden search of local curated, mapping, generated, report,
  source, and documentation paths found the expected CultureBotHT, same-formula
  regrade, aggregate, generated index, final SSSOM, and row-review rows; the
  adjacent `Sulfaquinoxaline_Sodium_Salt` record is a distinct sodium salt and
  not a duplicate of CAS `59-40-5`.

## Recommended Edits

- None.
