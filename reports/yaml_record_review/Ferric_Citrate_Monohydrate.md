# `data/ingredients/mapped/Ferric_Citrate_Monohydrate.yaml`

## Verdict

Pass. The ChEBI ferric citrate monohydrate identity, CAS-backed hydrate
structure, prior cadmium nitrate repair, and final SSSOM synonym payload are
consistent.

## Identity

- Reviewed record:
  `data/ingredients/mapped/Ferric_Citrate_Monohydrate.yaml`.
- Identifier and grounding: `identifier: CHEBI:144434` with matching
  `ontology_mapping.ontology_id`, canonical label
  `iron(III) citrate monohydrate`, source `CHEBI`, `mapping_quality:
  SYNONYM_MATCH`, `mapping_status: MAPPED`, and `ingredient_type:
  SINGLE_INGREDIENT`.
- `mappings/hydrate_review.tsv` marks the `Ferric citrate monohydrate` to
  `CHEBI:144434` hydrate mapping as correct and high-confidence.
- PubChem lookup by CAS RN `153531-98-7` resolved to CID 22178220 with formula
  `C6H7FeO8` and the same monohydrate InChI recorded under
  `chemical_properties`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Fecl3_X_6_H2o.yaml data/ingredients/mapped/Fepo4.yaml data/ingredients/mapped/Fermented_Rumen_Extract.yaml data/ingredients/mapped/Ferric_Ammonium_Citrate.yaml data/ingredients/mapped/Ferric_Citrate_Monohydrate.yaml`:
  exited 0 for the 5-file batch.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Ferric_Citrate_Monohydrate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 skipped because the
  sibling kg-microbe ontology transforms are not checked out.

## Evidence

- The matching `data/curated/mapped_ingredients.yaml` entry carries the same
  ChEBI identifier, CAS RN, formula, InChI, SMILES, and refreshed occurrence
  counts as the per-record YAML.
- The OAK/OLS row-review manifest confirms `MIM:Ferric_Citrate_Monohydrate` to
  `CHEBI:144434` as correct, and the active mapping evidence/history document
  the repair away from the unrelated `CHEBI:77732` cadmium nitrate target and
  CAS RN `10325-94-7`.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps the subject to
  `CHEBI:144434` with `skos:exactMatch`.
- The final SSSOM `other` tokens,
  `iron(3+) 2-hydroxypropane-1,2,3-tricarboxylate hydrate` and
  `CAS:153531-98-7`, denote the same monohydrate or its CAS RN.
- A hidden/ignored-inclusive search over `data/ingredients`, `data/curated`,
  `mappings`, `scripts`, `src`, `tests`, and `reports` for
  `Ferric_Citrate_Monohydrate`, `Ferric citrate monohydrate`, and
  `CHEBI:144434` found the active YAML, aggregate copy, final SSSOM row,
  hydrate review row, OAK/OLS row-review provenance, notes in the repaired
  calcium and cadmium nitrate records, and ignored aggregate backups.

## Completeness

- The exact monohydrate identity, CAS RN, structure fields, ingredient type,
  occurrence counts, accepted exact synonym, and cadmium nitrate repair
  provenance are populated.
- Empty role, component, environment, and discussion slots are acceptable for
  this single-ingredient record.

## Recommended Edits

- None.
