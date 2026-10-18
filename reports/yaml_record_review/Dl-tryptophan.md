# `data/ingredients/mapped/Dl-tryptophan.yaml`

## Verdict

Needs curation. The source surface is DL-tryptophan, but the record is grounded
to `CHEBI:57912` L-tryptophan zwitterion and its final SSSOM row publishes only
L-tryptophan-specific 2S synonyms. The CultureMech nitrogen-source role is
source-backed, but it is attached to the wrong ontology identity.

## Identity

- Reviewed record: `data/ingredients/mapped/Dl-tryptophan.yaml`.
- Identifier and grounding: `identifier: CHEBI:57912` with
  `ontology_mapping.ontology_id: CHEBI:57912`, source `CHEBI`,
  `mapping_quality: SYNONYM_MATCH`, `mapping_status: MAPPED`,
  `ingredient_type: SINGLE_INGREDIENT`, and 5 CultureMech source occurrences.
- Local OAK resolves `CHEBI:57912` to `L-tryptophan zwitterion`, an L-amino
  acid zwitterion with an isomeric InChIKey, not DL-tryptophan.
- Local ChEBI search for `tryptophan` found generic `CHEBI:27897` tryptophan,
  `CHEBI:16828` L-tryptophan, `CHEBI:57912` L-tryptophan zwitterion, and
  `CHEBI:57719` D-tryptophan zwitterion; a search for the exact
  `DL-Tryptophan` surface returned no local ChEBI term.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Dl-histidine.yaml data/ingredients/mapped/Dl-malic_Acid.yaml data/ingredients/mapped/Dl-methionine.yaml data/ingredients/mapped/Dl-mevalonic_Acid.yaml data/ingredients/mapped/Dl-tryptophan.yaml`:
  exited 0 for the 5-file batch.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Dl-histidine.yaml data/ingredients/mapped/Dl-malic_Acid.yaml data/ingredients/mapped/Dl-methionine.yaml data/ingredients/mapped/Dl-mevalonic_Acid.yaml data/ingredients/mapped/Dl-tryptophan.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed all 5 records.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:27570 CHEBI:6650 CHEBI:16811 CHEBI:25351 CHEBI:57912`:
  returned the canonical ChEBI label, definition, synonyms, formula, InChI,
  SMILES, charge, and mass for `CHEBI:57912`.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:27897 CHEBI:16828 CHEBI:57719`:
  returned local metadata for the generic, L-, and D-tryptophan comparators.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.
- `uv run --frozen python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`:
  passed; all id-label pairs corresponded, with only full-corpus plausibility
  warnings.

## Evidence

- `data/curated/mapped_ingredients.yaml` contains the same maintained record
  body as the per-record YAML.
- PubChem resolves the literal `DL-Tryptophan` name to CID 1148 with formula
  `C11H12N2O2` and the same non-isomeric InChIKey as generic `CHEBI:27897`, not
  the isomeric L-tryptophan zwitterion key on `CHEBI:57912`.
- A hidden/ignored-inclusive exact search over `data/ingredients` and
  `mappings` for `CHEBI:57912` and `DL-Tryptophan` found the active
  DL-tryptophan record, generated membership rows, stale row-review rows, and
  the final SSSOM row.
- Major: the ontology mapping points at L-tryptophan zwitterion even though the
  preferred term and source surface are DL-tryptophan.
- Major: the final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:Dl-tryptophan` to `CHEBI:57912` with L-tryptophan-specific 2S synonyms
  in `other`.
- `nutritional_roles.NITROGEN_SOURCE` carries `DATABASE_ENTRY` evidence
  imported from the CultureMech `Nitrogen Source` role text, so the role
  evidence itself is not provisional.

## Completeness

- The 5 CultureMech source occurrences are accounted for.
- The old PubChem name lookup recorded `200-194-9` in curation history, but
  current `chemical_properties` correctly omit a CAS RN rather than publishing
  that non-CAS registry number.
- Supplied forms, mixture components, physicochemical roles, biological roles,
  and environmental contexts are correctly empty.

## Recommended Edits

- Major: remap `data/ingredients/mapped/Dl-tryptophan.yaml` from L-specific
  `CHEBI:57912` to generic `CHEBI:27897` or to a local DL-tryptophan identity
  after curator review; then synchronize `data/curated/mapped_ingredients.yaml`.
- Major: remove the two L-tryptophan-specific 2S synonyms or demote them to
  `REJECTED_LABEL` provenance; then regenerate
  `mappings/ingredient_mappings.sssom.tsv`.
