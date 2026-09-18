# `data/ingredients/mapped/Syringaldehyde.yaml`

## Verdict

Pass. The exact `CHEBI:67380` syringaldehyde identity, CAS RN, IUPAC synonym,
structure fields, aggregate row, and final SSSOM row all pass.

## Identity

- Reviewed record: `data/ingredients/mapped/Syringaldehyde.yaml`.
- Identifier and grounding: `identifier: CHEBI:67380` with
  `ontology_mapping.ontology_id: CHEBI:67380`, label `syringaldehyde`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS `134-96-3`, formula `C9H10O4`, and ChEBI/PubChem
  InChI/SMILES.
- Occurrences: zero CultureMech recipe occurrences.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Synergistin_A` through `TAPS_Sodium_Salt`: exited 0 and wrote zero ERROR
  rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI record.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh OLS4 lookup resolves active `CHEBI:67380` with label
  `syringaldehyde`, CAS `134-96-3`, formula `C9H10O4`, exact IUPAC synonym
  `4-hydroxy-3,5-dimethoxybenzaldehyde`, and structure fields matching the
  YAML.
- The final SSSOM row exact-matches `CHEBI:67380`, uses
  `semapv:LexicalMatching`, and publishes only the real IUPAC synonym and
  `CAS:134-96-3` in `other`.

## Completeness

- The exact CHEBI identity, CAS, aggregate row, zero occurrence count, structure
  fields, and final SSSOM row agree.
- The record has no components, roles, environmental contexts, or datasets
  needing narrower evidence.
- An ignored/hidden search of local curated, mapping, generated, report,
  source, and documentation paths found the expected CultureBotHT, aggregate,
  generated index, and final SSSOM rows, and no second active MIM record for
  `CHEBI:67380`.

## Recommended Edits

- None.
