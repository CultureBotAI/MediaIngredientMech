# `data/ingredients/mapped/Alpha-Lactose.yaml`

## Verdict

Needs curation. The `#320` regrounding to the CAS-specific
`CHEBI:189432` alpha-lactose monohydrate identity was correct, and CAS
`5989-81-1` resolves to that hydrated form, but the record still stores the old
anhydrous `CHEBI:36219` formula/SMILES/InChI, exports anhydrous lactose aliases
in SSSOM, lacks the MicrobeDecoder alpha-lactose occurrence, and retains two
provisional nutrient roles.

## Identity

- Reviewed record: `data/ingredients/mapped/Alpha-Lactose.yaml`.
- Identifier and grounding: `identifier: CHEBI:189432` with
  `ontology_mapping.ontology_id: CHEBI:189432`, source `CHEBI`,
  `mapping_quality: SYNONYM_MATCH`, and `mapping_status: MAPPED`.
- Local OAK and the official ChEBI page resolve `CHEBI:189432` to
  `Alpha-lactose monohydrate` with formula `C12H22O11.H2O`, SMILES prefixed
  with a water component, InChI containing a `.H2O` layer, InChIKey
  `WSVLPVUVIUVCRA-KPKNDVKVSA-N`, and CAS `5989-81-1`.
- PubChem also resolves CAS `5989-81-1` to alpha-lactose monohydrate/lactose
  monohydrate names.
- The old anhydrous term, `CHEBI:36219`, has formula `C12H22O11`, SMILES with
  no water component, and InChIKey `GUBGYTABKSRVRQ-XLOQQCSPSA-N`, matching the
  stale local `chemical_properties` rather than the active `CHEBI:189432`
  identity.
- `ingredient_type: SINGLE_INGREDIENT` is present.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Allura_Red_AC.yaml data/ingredients/mapped/Aloin.yaml data/ingredients/mapped/Alpha-D-glucose_6-phosphate.yaml data/ingredients/mapped/Alpha-L-rhamnose.yaml data/ingredients/mapped/Alpha-Lactose.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Alpha-Lactose.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen runoak -i sqlite:obo:chebi aliases CHEBI:172687 CHEBI:73222 CHEBI:17665 CHEBI:27907 CHEBI:189432 CHEBI:36219`:
  returned `Alpha-lactose monohydrate` for `CHEBI:189432` and showed that
  `Anhydrous lactose`, `Milk sugar`, and the older alpha-lactose aliases belong
  to `CHEBI:36219`.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:172687 CHEBI:73222 CHEBI:17665 CHEBI:27907 CHEBI:189432 CHEBI:36219`:
  returned distinct hydrated and anhydrous formula, SMILES, InChI, InChIKey,
  and mass values for `CHEBI:189432` versus `CHEBI:36219`.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed; 2951
  records, 83 decompositions, 505 components, 0 violations.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- `mappings/ingredient_mappings.sssom.tsv` row 375 maps `MIM:Alpha-Lactose` to
  `CHEBI:189432` with `skos:exactMatch` and CAS `5989-81-1`, which agrees with
  the `#320` regrounding decision.
- The same SSSOM row exports `Anhydrous lactose`, `Milk sugar`,
  `1-beta-D-Galactopyranosyl-4-alpha-D-glucopyranose`, and other aliases copied
  from the old `CHEBI:36219` anhydrous alpha-lactose surface. At least
  `Anhydrous lactose` is directly incompatible with a monohydrate exact row.
- Current `chemical_properties.molecular_formula`, `smiles`, and `inchi` match
  the old `CHEBI:36219` alpha-lactose metadata, not `CHEBI:189432`; the formula
  is missing `.H2O`, the SMILES omits the water molecule, and the InChI has no
  hydrate layer.
- `data/custom/microbedecoder/unmapped_labels.tsv` contains
  `kgmicrobe.trait:alpha_lactose` in `BacDive_Metabolite_utilization` with
  count `126`, but the active YAML has no `source_occurrences` entry for
  MicrobeDecoder alpha-lactose.
- The `CARBON_SOURCE` and `ENERGY_SOURCE` roles are both provisional
  computational predictions and still say review is recommended.
- `mappings/ingredient_mappings_oak_ols_review.tsv` row 245 and
  `mappings/ingredient_mappings_row_review_manifest.tsv` row 245 refer to the
  pre-`#320` `CHEBI:36219` mapping; they are historical review artifacts, not
  evidence that `CHEBI:189432` carries the old anhydrous aliases.
- The hidden/ignored-inclusive search over `data`, `mappings`, `reports`,
  `src`, `tests`, `scripts`, `.claude`, `justfile`, and `CLAUDE.md` found the
  active YAML, aggregate copy, SSSOM row, stale OAK/OLS confirmation rows,
  MicrobeDecoder raw alpha-lactose occurrence, generated indexes, and ignored
  aggregate backups.

## Completeness

- CAS, curation history, and `ingredient_type` are populated.
- The record lacks monohydrate-specific formula, SMILES, and InChI values and
  lacks the MicrobeDecoder source occurrence.
- No component, environmental context, discussion, or dataset entry is needed.
- `mappings/culturemech_recipe_membership.tsv` has no `CHEBI:189432` row, which
  is consistent with `occurrence_statistics.total_occurrences: 0` because this
  record is sourced from CultureBotHT and MicrobeDecoder rather than
  CultureMech.
- The aggregate copy in `data/curated/mapped_ingredients.yaml` matches the
  per-record YAML, so the stale chemistry and anhydrous aliases have already
  propagated to generated surfaces.

## Recommended Edits

- Replace `chemical_properties.molecular_formula`, `smiles`, and `inchi` in
  `data/ingredients/mapped/Alpha-Lactose.yaml` with the `CHEBI:189432`
  monohydrate values and update the stale `AUTO_BACKFILL_CHEBI_CHEMISTRY`
  history prose so future reviewers can see when the structure changed.
- Remove exact `CHEBI:36219`/anhydrous alpha-lactose aliases from the
  monohydrate record, especially `Anhydrous lactose`; keep them on the
  anhydrous `Lactose`/`CHEBI:36219` record if they belong there.
- Add or recover a `source_occurrences` entry for
  `kgmicrobe.trait:alpha_lactose` so the 126 MicrobeDecoder utilization
  mentions are represented.
- Curate claim-level support for `nutritional_roles.CARBON_SOURCE` and
  `nutritional_roles.ENERGY_SOURCE`, or remove them until source-backed.
- Regenerate synchronized products, then rerun
  `uv run --frozen python scripts/validate_strict.py`, `uv run linkml-term-validator validate-data data/ingredients/mapped/Alpha-Lactose.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`,
  `uv run --frozen python scripts/validate_component_partonomy.py`, and
  `uv run --frozen python scripts/validate_sssom_invariants.py`.
