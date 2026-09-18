# `data/ingredients/mapped/Sulfate.yaml`

## Verdict

Pass. The exact `CHEBI:16189` sulfate identity, MicrobeDecoder source
occurrence, CultureMech occurrence count, structure fields, aggregate row, and
final SSSOM row all pass.

## Identity

- Reviewed record: `data/ingredients/mapped/Sulfate.yaml`.
- Identifier and grounding: `identifier: CHEBI:16189` with
  `ontology_mapping.ontology_id: CHEBI:16189`, label `sulfate`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: formula `O4S`, ChEBI/PubChem InChI, ChEBI/PubChem
  SMILES, and molecular weight `96.063`.
- Occurrences: 4 occurrences across 4 CultureMech media and 28 MicrobeDecoder
  rows.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Sulfaquinoxaline_Sodium_Salt` through `Sulfisoxazole`: exited 0 and wrote
  zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI record.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh OLS4 lookup resolves active `CHEBI:16189` with label `sulfate`, formula
  `O4S`, and structure fields matching the YAML.
- `data/custom/microbedecoder/unmapped_labels.tsv` and
  `mappings/microbedecoder_auto_mapped_review.tsv` preserve the
  MicrobeDecoder import and the reviewed lexical approval for the same label.
- `mappings/culturemech_recipe_membership.tsv` has four `CHEBI:16189` rows,
  agreeing with `total_occurrences: 4` and `media_count: 4`.
- The final SSSOM row exact-matches `CHEBI:16189`, uses
  `semapv:LexicalMatching`, and leaves `other` empty.

## Completeness

- The exact sulfate identity, aggregate row, occurrence count, structure fields,
  and final SSSOM row agree.
- The record has no active synonyms, components, roles, environmental contexts,
  or datasets needing narrower evidence.
- An ignored/hidden search of local curated, mapping, generated, report,
  source, and documentation paths found the expected MicrobeDecoder, occurrence
  membership, aggregate, generated index, and final SSSOM rows, and no second
  active MIM record for `CHEBI:16189`.

## Recommended Edits

- None.
