# `data/ingredients/mapped/Sulfisoxazole.yaml`

## Verdict

Pass. The exact `CHEBI:102484` identity, structure fields, MicrobeDecoder
source occurrence, aggregate row, and final SSSOM row all pass.

## Identity

- Reviewed record: `data/ingredients/mapped/Sulfisoxazole.yaml`.
- Identifier and grounding: `identifier: CHEBI:102484` with
  `ontology_mapping.ontology_id: CHEBI:102484`, label `sulfisoxazole`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: formula `C11H13N3O3S`, ChEBI/PubChem InChI,
  ChEBI/PubChem SMILES, and molecular weight `267.31`.
- Occurrences: zero CultureMech recipe occurrences and 3 MicrobeDecoder
  antibiotic rows.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Sulfaquinoxaline_Sodium_Salt` through `Sulfisoxazole`: exited 0 and wrote
  zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI record.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh OLS4 lookup resolves active `CHEBI:102484` with label
  `sulfisoxazole`, formula `C11H13N3O3S`, and structure fields matching the
  YAML.
- `data/custom/microbedecoder/unmapped_labels.tsv` preserves the
  MicrobeDecoder import for the same label.
- `mappings/culturemech_recipe_membership.tsv` has no `CHEBI:102484` rows,
  agreeing with `total_occurrences: 0` and `media_count: 0`.
- The final SSSOM row exact-matches `CHEBI:102484`, uses
  `semapv:LexicalMatching`, and leaves `other` empty.

## Completeness

- The exact CHEBI identity, aggregate row, occurrence count, structure fields,
  and final SSSOM row agree.
- The record has no active synonyms, components, roles, environmental contexts,
  or datasets needing narrower evidence.
- An ignored/hidden search of local curated, mapping, generated, report,
  source, and documentation paths found the expected MicrobeDecoder, aggregate,
  generated index, and final SSSOM rows, and no second active MIM record for
  `CHEBI:102484`.

## Recommended Edits

- None.
