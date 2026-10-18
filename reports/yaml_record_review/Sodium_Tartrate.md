# `data/ingredients/mapped/Sodium_Tartrate.yaml`

## Verdict

Needs curation - major. The exact `CHEBI:63017` sodium L-tartrate identity,
CAS-backed structure, merged `Na-tartrate` label, occurrence count, and final
SSSOM row pass, but `CARBON_SOURCE` is not supported by the stored `Mineral`
role evidence.

## Identity

- Reviewed record: `data/ingredients/mapped/Sodium_Tartrate.yaml`.
- Identifier and grounding: `identifier: CHEBI:63017` with
  `ontology_mapping.ontology_id: CHEBI:63017`, label `sodium L-tartrate`,
  source `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 25 source occurrences across 25 CultureMech media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Sodium_Salicylate` through `Sodium_Thiophosphate_Tribasic_Hydrate`: exited 0
  and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh EBI OLS4 lookup resolves active `CHEBI:63017` with label
  `sodium L-tartrate`, CAS `868-18-8`, and the curated sodium L-tartrate
  synonyms.
- Fresh PubChem lookup for CAS `868-18-8` resolves to sodium tartrate with the
  same stereospecific InChI and SMILES as the record.
- Final SSSOM keeps the same-substance ChEBI aliases, the merged raw
  `Na-tartrate` label, and `CAS:868-18-8`; the raw CultureMech role strings are
  correctly filtered out of final synonyms.
- Major: `nutritional_roles.CARBON_SOURCE` has
  `reference_type: DATABASE_ENTRY`, but its curator note says the original
  imported role text was `Mineral`. That text does not support a carbon-source
  assertion.

## Completeness

- The ChEBI ID, CAS RN, formula, structure, occurrence count, exact row, and
  safe synonyms agree.
- The only consequential gap is repairing the migrated role facet.

## Recommended Edits

- Major: in `data/ingredients/mapped/Sodium_Tartrate.yaml`, remove
  `nutritional_roles.CARBON_SOURCE` unless checked source evidence supports
  that role for sodium L-tartrate.
