# `data/ingredients/mapped/Chalcopyrite.yaml`

## Verdict

Needs curation; major issue. The exact ChEBI identity, formula-derived
structure fields, formula/name synonyms, three CultureMech occurrence rows,
SSSOM row, and aggregate copy pass. The `IRON_SOURCE` role is too narrow for
the attached claim-level evidence, which only preserves the generic imported
role text `Mineral`.

## Identity

- Reviewed record: `data/ingredients/mapped/Chalcopyrite.yaml`.
- Identifier and grounding: `identifier: CHEBI:86202`,
  `ontology_mapping.ontology_id: CHEBI:86202`,
  `ontology_label: chalcopyrite`, `ontology_source: CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`,
  `kg_microbe_node_id: CHEBI:86202`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Direct OLS lookup for `CHEBI:86202` returns one active ChEBI term labelled
  `chalcopyrite` with formula `Cu.Fe.2S`, InChI
  `InChI=1S/Cu.Fe.2S/q2*+2;2*-2`, SMILES `[Cu+2].[Fe+2].[S-2].[S-2]`, and
  synonyms `CuFeS2` and `Cupric ferrous sulfide`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Cetocycline.yaml data/ingredients/mapped/Cetomacrogol_1000.yaml data/ingredients/mapped/Cetrimonium_Bromide.yaml data/ingredients/mapped/Chalcopyrite.yaml data/ingredients/mapped/Champamycin_B.yaml`:
  passed.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Chalcopyrite.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed. The same focused validator also passed for `Cetocycline`,
  `Cetomacrogol_1000`, and `Cetrimonium_Bromide`; `Champamycin_B` was skipped
  because its `kgmicrobe.compound` placeholder CURIE is a local registry ID
  outside Engine A's OBO prefix scope.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip.wqYt47`
  followed by
  `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip.wqYt47`:
  passed; both curated collection files had 0 data differences and only the
  expected scratch `generation_date` metadata differences.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K. Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- Hidden/ignored-inclusive search over `data`, `mappings`, `docs`, and
  `reports` found the active exact `MIM:Chalcopyrite` SSSOM row, the
  `CONFIRMED` row-review disposition, matching aggregate and docs rows for
  `CHEBI:86202`, and no current CHEBI mapping dispute.
- PubChem lookup of stored CAS `12015-76-8` resolves to title `Chalcopyrite`
  with formula `CuFeS2` and the same InChI as the ChEBI-backed structure.
- Hidden/ignored-inclusive anchored search of
  `mappings/culturemech_recipe_membership.tsv` found exactly three
  `CHEBI:86202` rows, for `CultureMech:002876`, `CultureMech:009918`, and
  `CultureMech:013326`; that matches the explicit 3/3
  `occurrence_statistics`.
- The `Role: Mineral source; Properties: ...` raw synonym is still present in
  YAML, but final synonym/search export filters that raw role/property string
  through `src/mediaingredientmech/synonym_policy.py`.
- `TRACE_ELEMENT` and `IRON_SOURCE` both cite only a CultureMech
  `DATABASE_ENTRY` with curator note `Original role text: Mineral`. The broad
  `TRACE_ELEMENT` facet is consistent with chalcopyrite's copper/iron mineral
  identity, but the stored evidence does not directly assert this ingredient as
  an `IRON_SOURCE`.

## Completeness

- The exact ChEBI identifier, formula, InChI, SMILES, synonyms, SSSOM row,
  aggregate copy, docs row, and occurrence count are populated and agree.
- No component, environment, or dataset entry is required for this mineral
  record.
- The only consequential gap is the over-specific iron role evidence.

## Recommended Edits

- Major: in `data/ingredients/mapped/Chalcopyrite.yaml`, either replace
  `nutritional_roles.IRON_SOURCE` with inspected source evidence that
  Chalcopyrite is used as an iron source in this corpus, or remove the role.
- Regenerate synchronized outputs and rerun strict validation, SSSOM QC,
  aggregate roundtrip, and `git diff --check`.
