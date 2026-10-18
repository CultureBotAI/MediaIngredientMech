# `data/ingredients/mapped/A-Cyclodextrin.yaml`

## Verdict

Needs curation, major. The CAS-backed alpha-cyclodextrin identity, exact
ChEBI synonym, chemistry, SSSOM row, and aggregate copy pass, but the
carbon-source role is still only a provisional ancestry inference.

## Identity

- Reviewed record: `data/ingredients/mapped/A-Cyclodextrin.yaml`.
- Identifier and grounding: `identifier: CHEBI:40585` with
  `ontology_mapping.ontology_id: CHEBI:40585`, source `CHEBI`,
  `mapping_quality: CAS_RN_LOOKUP`, and `mapping_status: MAPPED`.
- The official ChEBI page resolves `CHEBI:40585` to `alpha-cyclodextrin` with
  formula `C36H60O30`, SMILES matching the live record, and InChIKey
  `HFHDHCJBZVLPGP-RWMJIURBSA-N`.
- Local OAK metadata carries the same formula, structure strings, average mass,
  monoisotopic mass, CAS `10016-20-3`, and exact synonym `cyclomaltohexaose`.
- PubChem maps CAS `10016-20-3` to CID `444913`, whose formula and InChIKey
  agree with ChEBI.
- `ingredient_type: SINGLE_INGREDIENT` is present.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/8-hydroxy-nitroquinoline.yaml data/ingredients/mapped/84_GL_NaHCO3_Solution.yaml data/ingredients/mapped/A-Cyclodextrin.yaml data/ingredients/mapped/A-Ketoglutaric_Acid_Disodium_Salt_Hydrate.yaml data/ingredients/mapped/AQDS.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/A-Cyclodextrin.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen runoak -i sqlite:obo:chebi aliases CHEBI:67121 CHEBI:32139 CHEBI:40585 CHEBI:30915 CHEBI:85112`:
  returned the expected ChEBI label and exact synonym for `CHEBI:40585`.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:67121 CHEBI:32139 CHEBI:40585 CHEBI:30915 CHEBI:85112`:
  returned the expected formula, structure strings, CAS xref, and mass for
  `CHEBI:40585`.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- CAS `10016-20-3`, PubChem CID `444913`, local OAK metadata, and the official
  ChEBI page all support the alpha-cyclodextrin identity.
- The stored `cyclomaltohexaose` synonym is the ChEBI exact synonym.
- The SSSOM row maps `MIM:A-Cyclodextrin` to `CHEBI:40585` with
  `skos:exactMatch`, exports `cyclomaltohexaose` and `CAS:10016-20-3`, and
  keeps `CAS_RN_LOOKUP` as the active mapping grade under Rule D.
- The `nutritional_roles.CARBON_SOURCE` assertion is supported only by
  computational ancestry from the broad ChEBI carbohydrate class; no source in
  the record establishes alpha-cyclodextrin as a carbon source in a culture
  medium.
- The `AUTO_BACKFILL_CHEBI_CHEMISTRY` event's `changes` string truncates the
  InChI and SMILES, but the live `chemical_properties` values are complete and
  match ChEBI.
- The hidden/ignored-inclusive search over `data`, `mappings`, `src`, `tests`,
  and `scripts` found the active YAML, aggregate copy, SSSOM row, row-review
  synonym confirmation, and ignored aggregate backups.

## Completeness

- CAS, formula, InChI, SMILES, the exact ChEBI synonym, and `ingredient_type`
  are populated.
- The carbon-source role needs curated evidence or demotion before the role
  facet should be considered complete.

## Recommended Edits

- In `data/ingredients/mapped/A-Cyclodextrin.yaml`, either add direct
  alpha-cyclodextrin utilization evidence to
  `nutritional_roles.CARBON_SOURCE` or remove the provisional role.
- Optionally clarify the stale
  `curation_history[AUTO_BACKFILL_CHEBI_CHEMISTRY].changes` string so it no
  longer shows truncated structure strings.
- Regenerate `data/curated/mapped_ingredients.yaml` and
  `mappings/ingredient_mappings.sssom.tsv`, then rerun strict validation and
  SSSOM invariants.
