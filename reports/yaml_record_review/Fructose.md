# `data/ingredients/mapped/Fructose.yaml`

## Verdict

Needs curation, with major final-SSSOM synonym and role-evidence issues. The
record now maps to the broad ChEBI `fructose` class, but CAS and synonym data
from the prior beta-D-fructofuranose mapping still leak into the active record
and final SSSOM, and `ENERGY_SOURCE` is still only computational.

## Identity

- Reviewed record: `data/ingredients/mapped/Fructose.yaml`.
- Identifier and grounding: `identifier: CHEBI:28757` with matching
  `ontology_mapping.ontology_id`, canonical label `fructose`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`,
  `kg_microbe_node_id: CHEBI:28757`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Local ChEBI metadata for `CHEBI:28757` confirms the broad `fructose` class;
  PubChem lookup by the stored CAS RN `53188-23-1` instead resolves to CID
  439709 titled `beta-D-fructose`, the beta-D-fructofuranose identity formerly
  used by this record.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Fructose-asparagine.yaml data/ingredients/mapped/Fructose.yaml data/ingredients/mapped/Fucoidan.yaml data/ingredients/mapped/Fucose.yaml data/ingredients/mapped/Fumarate.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Fructose.yaml data/ingredients/mapped/Fucoidan.yaml data/ingredients/mapped/Fucose.yaml data/ingredients/mapped/Fumarate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for the four CHEBI-primary records in the batch.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:28757 CHEBI:5181 CHEBI:33984 CHEBI:29806`:
  returned the active ChEBI label, synonyms, xrefs, and ontology metadata for
  `CHEBI:28757`.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 skipped because the
  sibling kg-microbe ontology transforms are not checked out.

## Evidence

- The matching `data/curated/mapped_ingredients.yaml` entry carries the same
  ChEBI identifier, corrected kg-microbe node ID, stale beta-D CAS RN,
  beta-D-specific synonyms, occurrence counts, supported carbon-source role,
  and computational energy-source role as the per-record YAML.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps `MIM:Fructose`
  to `CHEBI:28757` with `skos:exactMatch`.
- Major: `CAS:53188-23-1` exports in final SSSOM `other`, but it is the CAS xref
  of beta-D-fructofuranose `CHEBI:28645`, not of broad `CHEBI:28757`.
- Major: the beta-D-specific kg-microbe synonyms `beta-D-Fructose`,
  `beta-D-arabino-Hexulose`, `beta-Fruit sugar`, and `beta-Levulose` still
  export in `other` even though the active record was corrected to the broader
  fructose term.
- Major: `nutritional_roles.ENERGY_SOURCE` has only
  `COMPUTATIONAL_PREDICTION` evidence added alongside the carbon-source role
  and the evidence note explicitly says the role is provisional.
- `nutritional_roles.CARBON_SOURCE` is backed by CultureMech `DATABASE_ENTRY`
  evidence for the original `Role: Carbon source` import surface, and the raw
  `Role:` / `Properties:` aliases are filtered out of final SSSOM.
- A hidden/ignored-inclusive search over `data`, `src`, `tests`, `mappings`,
  `scripts`, and `reports`, excluding prior per-record review reports and
  historical aggregate backups, found the active YAML, aggregate copy, final
  SSSOM row, CultureMech memberships, label-index precedence tests, the
  separate exact `D-fructose` record, and beta-D synonym-enrichment provenance.

## Completeness

- The exact fructose identity, supported carbon-source role, occurrence counts,
  kg-microbe node ID, and final SSSOM row are populated.
- The CAS slot and beta-D synonyms are stale after the 2026-04-19 move from
  `CHEBI:28645` to `CHEBI:28757`.

## Recommended Edits

- Major: remove or demote the beta-D-fructofuranose-specific CAS RN and
  beta-D-specific synonyms from `data/ingredients/mapped/Fructose.yaml`, sync
  `data/curated/mapped_ingredients.yaml`, regenerate
  `mappings/ingredient_mappings.sssom.tsv`, and rerun the SSSOM invariant
  gates.
- Major: either replace `nutritional_roles.ENERGY_SOURCE` with inspected
  source-backed evidence for generic fructose in media, or remove the
  unsupported role.
