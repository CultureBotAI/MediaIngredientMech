# `data/ingredients/mapped/Ferrous_Ion.yaml`

## Verdict

Pass with a minor provenance issue. The record correctly resolves the
MicrobeDecoder ferrous-ion residual to the `CHEBI:29033` ferrous cation and
publishes the CultureMech `Fe2+` alias, but its top-level `notes` still carry
the stale import-era "Curator review needed" text.

## Identity

- Reviewed record: `data/ingredients/mapped/Ferrous_Ion.yaml`.
- Identifier and grounding: `identifier: CHEBI:29033` with matching
  `ontology_mapping.ontology_id`, canonical label `iron(2+)`, source `CHEBI`,
  `mapping_quality: SYNONYM_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- The structured evidence records the intended decision: ferrous ion is the
  Fe(II) cation, `CHEBI:29033` carries that exact identity, and it is the
  Ferrous Ion companion to the Ferric Iron curation.
- `chemical_properties` correctly model the cation as formula `Fe`, SMILES
  `[Fe+2]`, and InChI `InChI=1S/Fe/q+2`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Ferrous_Ion.yaml data/ingredients/mapped/Ferrous_ammonium_sulfate.yaml data/ingredients/mapped/Ferroverdin.yaml data/ingredients/mapped/Ferulate.yaml data/ingredients/mapped/Ferulic_Acid.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Ferrous_Ion.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.

## Evidence

- The matching `data/curated/mapped_ingredients.yaml` entry carries the same
  ChEBI identifier, cation structure fields, MicrobeDecoder source occurrence,
  and CultureMech `Fe2+` synonym as the per-record YAML.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:Ferrous_Ion` to `CHEBI:29033` with `skos:exactMatch`, and its only
  `other` token is the cation formula alias `Fe2+`.
- `mappings/culturemech_residual_groundings.tsv` records the `Fe2+` surface as
  an alias on the existing `CHEBI:29033` Ferrous Ion record, not a new
  substance.
- Minor: the top-level `notes` still say "no CAS-RN or CHEBI/NCIT match.
  Curator review needed." That sentence is stale after the August 2026
  promotion to `CHEBI:29033`.
- A hidden/ignored-inclusive search over `data/ingredients`, `data/curated`,
  `mappings`, `scripts`, `src`, `tests`, and `reports` for `Ferrous_Ion`,
  `Ferrous Ion`, and `ferrous_ion` found the active YAML, aggregate copy, final
  SSSOM row, the `Fe2+` CultureMech residual alias, old batch validation
  output, and ignored aggregate backups.

## Completeness

- The exact ferrous-cation identity, structure fields, MicrobeDecoder source
  occurrence, CultureMech alias, and final SSSOM payload are populated.
- Empty component, role, environment, and discussion slots are acceptable for
  this single ion record.

## Recommended Edits

- Minor: replace the stale import-era top-level `notes` in
  `data/ingredients/mapped/Ferrous_Ion.yaml`, sync
  `data/curated/mapped_ingredients.yaml`, and rerun strict validation plus the
  roundtrip gate.
