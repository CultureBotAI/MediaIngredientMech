# `data/ingredients/mapped/Mgso4_X_6_H2o.yaml`

## Verdict

Needs curation. The formula-supported local magnesium sulfate hexahydrate
identity, local kg-microbe exact row, anhydrous parent row, occurrence count,
and filtered final SSSOM synonyms pass, but its nutritional role evidence is
attached to the wrong role and leaves `MINERAL_SOURCE` unsupported.

Severity: major.

## Identity

- Reviewed record: `data/ingredients/mapped/Mgso4_X_6_H2o.yaml`.
- Identifier and grounding:
  `identifier: kgmicrobe.compound:mgso4_x_6_h2o` with
  `ontology_mapping.ontology_id: CHEBI:32599`, label `magnesium sulfate`,
  source `CHEBI`, `mapping_quality: NARROW_MATCH`, `mapping_status: MAPPED`,
  and `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 35 CultureMech recipe occurrences.
- Chemical identity: curated formula `Mg.O4S.6H2O`; parent-derived CAS, InChI,
  and SMILES were cleared when #652 localized the hexahydrate identity.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Mgcl2x_6_H2o` through `Mgso4_X_6_H2o`: exited 0 and wrote zero ERROR rows.
- Direct Engine A term validation was skipped for this local registry record
  because its primary `kgmicrobe.compound` identifier is outside the OBO subset
  used for the batch.

## Evidence

- EBI OLS4 exact search resolves magnesium sulfate heptahydrate but finds no
  ChEBI term for magnesium sulfate hexahydrate.
- `mappings/hydrate_review.tsv` keeps this row as a local hydrate identity
  because no exact external ontology term has been verified. It retains
  `CHEBI:32599` only as the anhydrous parent and records the curated
  `Mg.O4S.6H2O` formula with no parent CAS, InChI, or SMILES.
- The final SSSOM publishes the intended two-row shape:
  `skos:narrowMatch` to the anhydrous `CHEBI:32599` parent and
  `skos:exactMatch` to `kgmicrobe.compound:mgso4_x_6_h2o`.
- The final `other` tokens are limited to two 6-water magnesium sulfate labels;
  1-water, 7-water, concentration-qualified, and malformed formulas are stored
  as `REJECTED_LABEL` in YAML and do not publish.

## Completeness

- The local identity, curated formula, rejected false synonyms, active
  occurrence count, ingredient type, parent row, and exact registry row are
  populated and agree.
- `SULFUR_SOURCE` carries the CultureMech `DATABASE_ENTRY` evidence for 20
  occurrences as `Mineral source`; that source text supports the mineral role,
  not the sulfur role.
- `MINERAL_SOURCE` is present but has `confidence: 0.8` and an empty evidence
  list, so the supported role is the unsupported one in the current YAML.

## Recommended Edits

- Major: move the CultureMech mineral-source evidence to `MINERAL_SOURCE`, and
  either add independent source-backed evidence for `SULFUR_SOURCE` or remove
  that role from `data/ingredients/mapped/Mgso4_X_6_H2o.yaml`.
