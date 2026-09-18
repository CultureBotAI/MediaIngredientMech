# `data/ingredients/mapped/Surfactant.yaml`

## Verdict

Needs curation - major. The exact `CHEBI:35195` surfactant identity,
occurrence count, aggregate row, and final SSSOM row pass, but the
`SURFACTANT` role is still a provisional ChEBI-ancestry inference with no
source-backed evidence.

## Identity

- Reviewed record: `data/ingredients/mapped/Surfactant.yaml`.
- Identifier and grounding: `identifier: CHEBI:35195` with
  `ontology_mapping.ontology_id: CHEBI:35195`, label `surfactant`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 3 occurrences across 3 CultureMech media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Supplemented_Seawater` through `Synephrine_Tartrate`: exited 0 and wrote
  zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI record.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh OLS4 lookup resolves active `CHEBI:35195` with label `surfactant`, a
  definition for substances that lower surface or interfacial tension, and
  surfactant synonyms.
- `mappings/culturemech_recipe_membership.tsv` has three `CHEBI:35195` rows,
  agreeing with `total_occurrences: 3` and `media_count: 3`.
- The final SSSOM row exact-matches `CHEBI:35195`, uses
  `semapv:LexicalMatching`, and leaves `other` empty.
- Major: `physicochemical_roles.SURFACTANT` cites only
  `reference_type: COMPUTATIONAL_PREDICTION` from ChEBI ancestry and explicitly
  notes that review is recommended. That is still a provisional inference, not
  source-backed role evidence for this ingredient.

## Completeness

- The exact CHEBI identity, aggregate row, occurrence count, and final SSSOM row
  agree.
- The record has no active synonyms, components, environmental contexts, or
  datasets needing narrower evidence.
- An ignored/hidden search of local curated, mapping, generated, report,
  source, and documentation paths found the expected MediaDive, CultureMech,
  role-inference, aggregate, generated index, row-review, and final SSSOM rows,
  and no second active MIM record for `CHEBI:35195`.

## Recommended Edits

- Major: replace the provisional computational `SURFACTANT` role in
  `data/ingredients/mapped/Surfactant.yaml` with source-backed evidence from
  the maintained MediaDive or CultureMech rows, or remove the role facet as
  redundant with the exact `CHEBI:35195` mapping if no narrow role evidence is
  available.
