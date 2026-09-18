# `data/ingredients/mapped/Fecl3_X_6_H2o.yaml`

## Verdict

Needs curation, with major final-SSSOM synonym issues. The ChEBI ferric
chloride hexahydrate identity, CAS-backed hydrate structure, supported
CultureMech iron-source role, and core hydrate synonyms pass, but the final
SSSOM `other` column still exports concentration-bearing and mixture labels as
exact synonyms.

## Identity

- Reviewed record: `data/ingredients/mapped/Fecl3_X_6_H2o.yaml`.
- Identifier and grounding: `identifier: CHEBI:86254` with matching
  `ontology_mapping.ontology_id`, canonical label
  `iron trichloride hexahydrate`, source `CHEBI`, `mapping_quality:
  SYNONYM_MATCH`, `mapping_status: MAPPED`, `kg_microbe_node_id:
  CHEBI:86254`, and `ingredient_type: SINGLE_INGREDIENT`.
- `mappings/hydrate_review.tsv` marks the `FeCl3 x 6 H2O` to `CHEBI:86254`
  hydrate mapping as correct and high-confidence.
- PubChem lookup by CAS RN `10025-77-1` resolved to CID 6093258 with formula
  `Cl3FeH12O6` and the same hexahydrate InChI recorded under
  `chemical_properties`.
- `nutritional_roles.IRON_SOURCE` is supported by a `DATABASE_ENTRY` reference
  to CultureMech's original `Mineral source` role text.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Fecl3_X_6_H2o.yaml data/ingredients/mapped/Fepo4.yaml data/ingredients/mapped/Fermented_Rumen_Extract.yaml data/ingredients/mapped/Ferric_Ammonium_Citrate.yaml data/ingredients/mapped/Ferric_Citrate_Monohydrate.yaml`:
  exited 0 for the 5-file batch.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Fecl3_X_6_H2o.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 skipped because the
  sibling kg-microbe ontology transforms are not checked out.

## Evidence

- The matching `data/curated/mapped_ingredients.yaml` entry carries the same
  ChEBI identifier, CAS RN, formula, InChI, SMILES, kg-microbe node ID,
  supported `IRON_SOURCE` role, and refreshed occurrence counts as the
  per-record YAML.
- The row-review manifest confirms `MIM:Fecl3_X_6_H2o` to `CHEBI:86254` as an
  OAK/OLS-confirmed mapping, and the final
  `mappings/ingredient_mappings.sssom.tsv` row maps the subject to that ChEBI
  term with `skos:exactMatch`.
- The core final SSSOM `other` tokens, including `FeCl3.6H2O`,
  `FeCl3 . 6H2O`, `FeCl3 x6H2O`, `FeCl3*6 H2O`, `Ferric chloride
  hexahydrate`, `Iron (III) chloride hexahydrate`,
  `trichloroiron--water (1/6)`, and `CAS:10025-77-1`, denote the same
  hexahydrate or its CAS RN.
- Major: the final SSSOM `other` column also exports
  `FeCl3 x 6 H2O (0.1% w/v in 0.2 N HCl)`,
  `FeCl3 x 6 H2O (0.5%)`, `FeCl3 x 6 H2O (w/v=1%)`, and
  `FeCl3 x 6 H2O solution (2%)`, which are concentration or solution labels
  rather than exact synonyms of the dry hexahydrate.
- Major: the final SSSOM `other` column exports `FeCl3 x 6 H2O NaEDTA`, which
  denotes a combined ferric chloride hexahydrate plus EDTA surface, not a name
  for the single hexahydrate.
- A hidden/ignored-inclusive search over `data/ingredients`, `data/curated`,
  `mappings`, `scripts`, `src`, `tests`, and `reports` for
  `Fecl3_X_6_H2o`, `FeCl3 x 6 H2O`, and `CHEBI:86254` found the active YAML,
  aggregate copy, final SSSOM row, OAK/OLS row-review provenance, hydrate
  review rows, stock-solution component references, schema examples, and
  ignored aggregate backups.

## Completeness

- The exact hexahydrate identity, CAS RN, structure fields, supported
  iron-source role, ingredient type, occurrence counts, and accepted hydrate
  synonyms are populated.
- The final SSSOM synonym payload needs filtering for the concentration,
  solution, and EDTA-mixture tokens.

## Recommended Edits

- Major: remove or filter the concentration-bearing `FeCl3 x 6 H2O` strings
  and `FeCl3 x 6 H2O NaEDTA` from exact final SSSOM `other` export, sync
  `data/curated/mapped_ingredients.yaml`, regenerate
  `mappings/ingredient_mappings.sssom.tsv`, and rerun strict validation plus
  the final SSSOM invariant gates.
