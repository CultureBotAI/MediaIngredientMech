# `data/ingredients/mapped/Ferric_Ammonium_Citrate.yaml`

## Verdict

Pass. The ChEBI ferric ammonium citrate identity, CAS RN, CultureMech
nitrogen-source role, duplicate-merge history, and final SSSOM synonym payload
are consistent.

## Identity

- Reviewed record:
  `data/ingredients/mapped/Ferric_Ammonium_Citrate.yaml`.
- Identifier and grounding: `identifier: CHEBI:31604` with matching
  `ontology_mapping.ontology_id`, canonical label `ferric ammonium citrate`,
  source `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`,
  `kg_microbe_node_id: CHEBI:31604`, and `ingredient_type:
  SINGLE_INGREDIENT`.
- PubChem lookup by CAS RN `1185-57-5` resolved to CID 118984355, agreeing
  with the record's CAS RN.
- `nutritional_roles.NITROGEN_SOURCE` is supported by a `DATABASE_ENTRY`
  carrying CultureMech's original `Nitrogen Source` role text.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Fecl3_X_6_H2o.yaml data/ingredients/mapped/Fepo4.yaml data/ingredients/mapped/Fermented_Rumen_Extract.yaml data/ingredients/mapped/Ferric_Ammonium_Citrate.yaml data/ingredients/mapped/Ferric_Citrate_Monohydrate.yaml`:
  exited 0 for the 5-file batch.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Ferric_Ammonium_Citrate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 skipped because the
  sibling kg-microbe ontology transforms are not checked out.

## Evidence

- The matching `data/curated/mapped_ingredients.yaml` entry carries the same
  ChEBI identifier, CAS RN, kg-microbe node ID, supported nitrogen-source role,
  duplicate-merge history, and refreshed occurrence counts as the per-record
  YAML.
- The OAK/OLS row review found a synonym-enrichment candidate,
  `Fe(NH4)citrate`, and the row-review manifest marks it
  `ALREADY_REPRESENTED`; no remapping was required.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:Ferric_Ammonium_Citrate` to `CHEBI:31604` with `skos:exactMatch`.
- The final SSSOM `other` tokens, `Ammonium ferric citrate`, `E381`,
  `Fe(NH4)citrate`, `FerriSeltz`, `ammonium iron(III) citrate`,
  `Ferric ammmonium citrate`, and `CAS:1185-57-5`, are same-substance labels,
  a raw spelling variant, or the current CAS RN.
- A hidden/ignored-inclusive search over `data/ingredients`, `data/curated`,
  `mappings`, `scripts`, `src`, `tests`, and `reports` for
  `Ferric_Ammonium_Citrate`, `Ferric ammonium citrate`, and `CHEBI:31604`
  found the active YAML, aggregate copy, final SSSOM row, synonym-enrichment
  review row, OAK/OLS row-review provenance, duplicate-merge history, and
  ignored aggregate backups.

## Completeness

- The exact identity, CAS RN, supported nitrogen-source role, kg-microbe
  cross-reference, ingredient type, occurrence counts, and accepted exact
  synonyms are populated.
- I found no consequential missing component, structure field, environment,
  discussion, or final SSSOM payload for this single ingredient. The record has
  CAS-level chemical properties but no formula/InChI/SMILES fields; that is a
  non-blocking gap here because the PubChem CAS lookup and ChEBI grounding
  agree.

## Recommended Edits

- None.
