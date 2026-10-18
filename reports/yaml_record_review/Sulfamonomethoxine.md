# `data/ingredients/mapped/Sulfamonomethoxine.yaml`

## Verdict

Pass. The exact `CHEBI:32164` identity, CAS, structure fields, aggregate row,
and final SSSOM row all pass.

## Identity

- Reviewed record: `data/ingredients/mapped/Sulfamonomethoxine.yaml`.
- Identifier and grounding: `identifier: CHEBI:32164` with
  `ontology_mapping.ontology_id: CHEBI:32164`, label `Sulfamonomethoxine`,
  source `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`,
  and `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS `1220-83-3`, formula `C11H12N4O3S`, and
  ChEBI-derived InChI/SMILES.
- Occurrences: zero CultureMech recipe occurrences.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Sulfamethoxazole` through `Sulfaquinoxaline`: exited 0 and wrote zero ERROR
  rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI record.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh OLS4 lookup resolves active `CHEBI:32164` with label
  `Sulfamonomethoxine`, CAS xref `1220-83-3`, formula `C11H12N4O3S`, and
  structure fields matching the YAML.
- `mappings/culturemech_recipe_membership.tsv` has no `CHEBI:32164` rows,
  agreeing with `total_occurrences: 0` and `media_count: 0`.
- The final SSSOM row exact-matches `CHEBI:32164` and publishes only
  `CAS:1220-83-3` in `other`, which is a true CAS label for the same subject.

## Completeness

- The record has no active synonyms, components, roles, environmental contexts,
  or datasets needing narrower evidence.
- An ignored/hidden search of local curated, mapping, generated, report,
  source, and documentation paths found the expected CultureBotHT,
  MicrobeDecoder candidate, aggregate, generated index, final SSSOM, and
  row-review rows, and no second active MIM record for `CHEBI:32164` or CAS
  `1220-83-3`.

## Recommended Edits

- None.
