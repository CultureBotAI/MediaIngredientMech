# `data/ingredients/mapped/Syringic_Acid.yaml`

## Verdict

Pass. The exact `CHEBI:68329` syringic-acid identity, CAS RN, IUPAC synonym,
structure fields, occurrence count, aggregate row, and final SSSOM row all
pass.

## Identity

- Reviewed record: `data/ingredients/mapped/Syringic_Acid.yaml`.
- Identifier and grounding: `identifier: CHEBI:68329` with
  `ontology_mapping.ontology_id: CHEBI:68329`, label `syringic acid`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS `530-57-4`, formula `C9H10O5`, and ChEBI/PubChem
  InChI/SMILES.
- Occurrences: 6 occurrences across 6 CultureMech media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Synergistin_A` through `TAPS_Sodium_Salt`: exited 0 and wrote zero ERROR
  rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI record.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh OLS4 lookup resolves active `CHEBI:68329` with label `syringic acid`,
  CAS `530-57-4`, formula `C9H10O5`, exact IUPAC synonym
  `4-hydroxy-3,5-dimethoxybenzoic acid`, and structure fields matching the
  YAML.
- `mappings/culturemech_recipe_membership.tsv` has six `CHEBI:68329` rows,
  agreeing with `total_occurrences: 6` and `media_count: 6`.
- The final SSSOM row exact-matches `CHEBI:68329`, uses
  `semapv:LexicalMatching`, and publishes only the real IUPAC synonym and
  `CAS:530-57-4` in `other`.

## Completeness

- The exact CHEBI identity, CAS, aggregate row, occurrence count, structure
  fields, and final SSSOM row agree.
- The record has no components, roles, environmental contexts, or datasets
  needing narrower evidence.
- An ignored/hidden search of local curated, mapping, generated, report,
  source, and documentation paths found the expected CultureBotHT, occurrence
  membership, aggregate, generated index, and final SSSOM rows, and no second
  active MIM record for `CHEBI:68329`.

## Recommended Edits

- None.
