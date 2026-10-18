# `data/ingredients/mapped/Sulfadimethoxine.yaml`

## Verdict

Pass. The exact `CHEBI:32161` identity, structure fields, MicrobeDecoder source
occurrence, aggregate row, and final SSSOM row all pass.

## Identity

- Reviewed record: `data/ingredients/mapped/Sulfadimethoxine.yaml`.
- Identifier and grounding: `identifier: CHEBI:32161` with
  `ontology_mapping.ontology_id: CHEBI:32161`, label `sulfadimethoxine`,
  source `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`,
  and `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: formula `C12H14N4O4S`, ChEBI/PubChem InChI,
  ChEBI/PubChem SMILES, and molecular weight `310.335`.
- Occurrences: zero CultureMech recipe occurrences and one MicrobeDecoder
  antibiotic-resistance row.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Sulbactam` through `Sulfamethizole`: exited 0 and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI record.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh OLS4 lookup resolves active `CHEBI:32161` with label
  `sulfadimethoxine`, formula `C12H14N4O4S`, and structure fields matching the
  YAML.
- `data/custom/microbedecoder/unmapped_labels.tsv` and
  `mappings/microbedecoder_auto_mapped_review.tsv` preserve the
  MicrobeDecoder import and the reviewed lexical approval for the same label.
- `mappings/culturemech_recipe_membership.tsv` has no `CHEBI:32161` rows,
  agreeing with `total_occurrences: 0` and `media_count: 0`.
- The final SSSOM row exact-matches `CHEBI:32161`, uses
  `semapv:LexicalMatching`, and leaves `other` empty.

## Completeness

- The record has no active synonyms, components, roles, environmental contexts,
  or datasets needing narrower evidence.
- An ignored/hidden search of local curated, mapping, generated, report,
  source, and documentation paths found the expected MicrobeDecoder, aggregate,
  generated index, and final SSSOM rows, and no second active MIM record for
  the exact `CHEBI:32161` identity.

## Recommended Edits

- None.
