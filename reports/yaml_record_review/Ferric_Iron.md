# `data/ingredients/mapped/Ferric_Iron.yaml`

## Verdict

Pass with a minor provenance issue. The record correctly resolves the
MicrobeDecoder ferric-iron residual to the `CHEBI:29034` ferric cation and
publishes the CultureMech `Fe3+` alias, but its top-level `notes` still carry
the stale import-era "Curator review needed" text.

## Identity

- Reviewed record: `data/ingredients/mapped/Ferric_Iron.yaml`.
- Identifier and grounding: `identifier: CHEBI:29034` with matching
  `ontology_mapping.ontology_id`, canonical label `iron(3+)`, source `CHEBI`,
  `mapping_quality: SYNONYM_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- The structured evidence records the intended decision: ferric iron is the
  Fe(III) cation, `CHEBI:29034` carries the exact cation identity, and the NCIT
  adjective `Ferric` was rejected.
- `chemical_properties` correctly model the cation as formula `Fe`, SMILES
  `[Fe+3]`, and InChI `InChI=1S/Fe/q+3`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Ferric_Iron.yaml data/ingredients/mapped/Ferric_Malate_Solution.yaml data/ingredients/mapped/Ferric_nitrilotriacetate.yaml data/ingredients/mapped/Ferrihydrite.yaml data/ingredients/mapped/Ferrous_Citrate.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Ferric_Iron.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.

## Evidence

- The matching `data/curated/mapped_ingredients.yaml` entry carries the same
  ChEBI identifier, cation structure fields, MicrobeDecoder source occurrence,
  and CultureMech `Fe3+` synonym as the per-record YAML.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:Ferric_Iron` to `CHEBI:29034` with `skos:exactMatch`, and its only
  `other` token is the cation formula alias `Fe3+`.
- `mappings/culturemech_residual_groundings.tsv` records the `Fe3+` surface as
  an alias on the existing `CHEBI:29034` Ferric Iron record, not a new
  substance.
- Minor: the top-level `notes` still say "no CAS-RN or CHEBI/NCIT match.
  Curator review needed." That sentence is stale after the August 2026
  promotion to `CHEBI:29034`.
- A hidden/ignored-inclusive search over `data/ingredients`, `data/curated`,
  `mappings`, `scripts`, `src`, `tests`, and `reports` for `Ferric_Iron`,
  `Ferric Iron`, and `ferric_iron` found the active YAML, aggregate copy, final
  SSSOM row, the applied MicrobeDecoder residual proposal, the deferred NCIT
  adjective row, the `Fe3+` CultureMech residual alias, the companion Ferrous
  Ion note, and ignored aggregate backups.

## Completeness

- The exact ferric-cation identity, structure fields, MicrobeDecoder source
  occurrence, CultureMech alias, and final SSSOM payload are populated.
- Empty component, role, environment, and discussion slots are acceptable for
  this single ion record.

## Recommended Edits

- Minor: replace the stale import-era top-level `notes` in
  `data/ingredients/mapped/Ferric_Iron.yaml`, sync
  `data/curated/mapped_ingredients.yaml`, and rerun strict validation plus the
  roundtrip gate.
