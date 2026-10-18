# `data/ingredients/mapped/L-methionine.yaml`

## Verdict

Needs curation. The L-methionine identity, CAS RN, PubChem structure,
occurrence count, reviewed synonyms, and final SSSOM row pass, but the role
facet is a provisional amino-acid-source inference instead of the
CultureMech-backed nitrogen-source role recorded in the raw source text.

## Identity

- Reviewed record: `data/ingredients/mapped/L-methionine.yaml`.
- Identifier and grounding: `identifier: CHEBI:16643` with
  `ontology_mapping.ontology_id: CHEBI:16643`, label `L-methionine`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS RN `63-68-3`, molecular formula `C5H11NO2S`,
  InChI, and SMILES.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/L-lysine_Hcl.yaml data/ingredients/mapped/L-lyxose.yaml data/ingredients/mapped/L-malate.yaml data/ingredients/mapped/L-methionine.yaml data/ingredients/mapped/L-norleucine.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/L-lysine_Hcl.yaml data/ingredients/mapped/L-lyxose.yaml data/ingredients/mapped/L-malate.yaml data/ingredients/mapped/L-methionine.yaml data/ingredients/mapped/L-norleucine.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  exited 0 for the 5 ChEBI records.

## Evidence

- EBI OLS4 resolves `CHEBI:16643` as active `L-methionine` and lists CAS
  `63-68-3`.
- PubChem resolves CAS RN `63-68-3` to CID `6137` with formula `C5H11NO2S` and
  the same InChI as the YAML record.
- The final SSSOM publishes one `skos:exactMatch` row to `CHEBI:16643`; exact
  OLS search for `METHIONINE` confirms the uppercase token is also an exact
  synonym of `CHEBI:16643`.
- Major: the original CultureMech raw text says `Role: Nitrogen source`, but
  the role facet now contains only `nutritional_roles.AMINO_ACID_SOURCE` from
  `COMPUTATIONAL_PREDICTION` evidence through `CHEBI:33709`. The migrated
  role should be backed by the original nitrogen-source text, and the
  ancestry-derived amino-acid role is still provisional.
- The hidden and ignored-inclusive search over `data`, `mappings`, `reports`,
  `docs`, `src`, and `tests` found the current YAML, aggregate copy, final
  SSSOM row, docs projections, the generic DL-methionine sibling, and
  component references from multicomponent amino-acid records.

## Completeness

- The active ChEBI identity, CAS RN, formula, structure, occurrence count,
  synonyms, aggregate copy, and final SSSOM row are present and consistent.
- The role facet needs curation to reflect the claim-level source role.

## Recommended Edits

- Major: replace or supplement `nutritional_roles.AMINO_ACID_SOURCE` in
  `data/ingredients/mapped/L-methionine.yaml` with a `NITROGEN_SOURCE` role
  backed by `DATABASE_ENTRY` evidence from the CultureMech `Role: Nitrogen
  source` text; remove the provisional amino-acid-source inference unless
  exact support is added.
- Sync the aggregate copy and regenerate derived products after the YAML
  changes; rerun strict, term, round-trip, component, and SSSOM validation.
