# `data/ingredients/mapped/Sulfite.yaml`

## Verdict

Pass. The exact `CHEBI:17359` sulfite identity, MicrobeDecoder source
occurrence, structure fields, aggregate row, and final SSSOM row all pass.

## Identity

- Reviewed record: `data/ingredients/mapped/Sulfite.yaml`.
- Identifier and grounding: `identifier: CHEBI:17359` with
  `ontology_mapping.ontology_id: CHEBI:17359`, label `sulfite`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: formula `O3S`, ChEBI/PubChem InChI, ChEBI/PubChem
  SMILES, and molecular weight `80.064`.
- Occurrences: zero CultureMech recipe occurrences and 26 MicrobeDecoder
  rows.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Sulfite` through `Sulfur`: exited 0 and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI record.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh OLS4 lookup resolves active `CHEBI:17359` with label `sulfite`,
  formula `O3S`, and structure fields matching the YAML.
- `data/custom/microbedecoder/unmapped_labels.tsv` and
  `mappings/microbedecoder_auto_mapped_review.tsv` preserve the
  MicrobeDecoder import and the reviewed lexical approval for the same label.
- The final SSSOM row exact-matches `CHEBI:17359`, uses
  `semapv:LexicalMatching`, and leaves `other` empty.

## Completeness

- The exact sulfite identity, aggregate row, occurrence count, structure
  fields, and final SSSOM row agree.
- The record has no active synonyms, components, roles, environmental contexts,
  or datasets needing narrower evidence.
- An ignored/hidden search of local curated, mapping, generated, report,
  source, and documentation paths found the expected MicrobeDecoder,
  aggregate, generated index, and final SSSOM rows, and no second active MIM
  record for `CHEBI:17359`.

## Recommended Edits

- None.
